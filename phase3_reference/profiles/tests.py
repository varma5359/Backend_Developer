from datetime import date
from decimal import Decimal

from django.contrib import admin
from django.db.models.deletion import ProtectedError
from django.test import Client, TestCase
from django.urls import reverse

from .forms import StudentRegistrationForm
from .models import (
    Course,
    Department,
    Employee,
    Student,
    StudentProfile,
)


class StudentPortalModelTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Engineering")
        self.python = Course.objects.create(title="Python")
        self.django = Course.objects.create(title="Django")
        self.asha = Student.objects.create(
            student_code="STU1001",
            full_name="Asha Rao",
            email="asha@example.com",
            department=self.department,
        )
        self.asha.courses.add(self.python, self.django)

    def test_foreign_key_forward_and_reverse_access(self):
        self.assertEqual(self.asha.department, self.department)
        self.assertEqual(
            list(self.department.students.values_list("student_code", flat=True)),
            ["STU1001"],
        )

    def test_many_to_many_forward_and_reverse_access(self):
        self.assertEqual(
            set(self.asha.courses.values_list("title", flat=True)),
            {"Python", "Django"},
        )
        self.assertEqual(
            list(self.python.students.values_list("student_code", flat=True)),
            ["STU1001"],
        )

    def test_one_to_one_forward_and_reverse_access(self):
        profile = StudentProfile.objects.create(
            student=self.asha,
            phone="9000000001",
        )
        self.assertEqual(profile.student, self.asha)
        self.assertEqual(self.asha.profile.phone, "9000000001")

    def test_student_can_exist_without_profile(self):
        student = Student.objects.create(
            student_code="STU1002",
            full_name="Rahul Kumar",
            email="rahul@example.com",
        )
        self.assertFalse(hasattr(student, "profile"))

    def test_department_protects_existing_students(self):
        with self.assertRaises(ProtectedError):
            self.department.delete()

    def test_student_delete_cascades_to_profile(self):
        StudentProfile.objects.create(student=self.asha, phone="9000000001")
        self.asha.delete()
        self.assertFalse(StudentProfile.objects.filter(phone="9000000001").exists())

    def test_employee_model_and_decimal_salary(self):
        employee = Employee.objects.create(
            employee_code="EMP1001",
            full_name="Ravi Kumar",
            email="ravi@example.com",
            salary=Decimal("55000.00"),
            joining_date=date(2026, 11, 1),
        )
        self.assertEqual(employee.salary, Decimal("55000.00"))
        self.assertEqual(str(employee), "EMP1001 - Ravi Kumar")


class StudentRegistrationFormTests(TestCase):
    def valid_data(self):
        return {
            "student_code": "stu9001",
            "full_name": "Asha Rao",
            "email": "asha@example.com",
        }

    def test_valid_form_normalizes_student_code(self):
        form = StudentRegistrationForm(data=self.valid_data())
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["student_code"], "STU9001")

    def test_student_code_must_start_with_stu(self):
        data = self.valid_data()
        data["student_code"] = "BAD9001"
        form = StudentRegistrationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("student_code", form.errors)

    def test_cross_field_rule_rejects_full_name_in_email(self):
        data = self.valid_data()
        data["email"] = "asha.rao@example.com"
        form = StudentRegistrationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_duplicate_student_code_is_rejected(self):
        Student.objects.create(
            student_code="STU9001",
            full_name="Existing Student",
            email="existing@example.com",
        )
        form = StudentRegistrationForm(data=self.valid_data())
        self.assertFalse(form.is_valid())
        self.assertIn("student_code", form.errors)


class StudentPortalViewTests(TestCase):
    def test_student_list_displays_empty_state(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No students registered yet.")

    def test_registration_get_displays_form(self):
        response = self.client.get(reverse("student_register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register Student")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_valid_post_saves_student_and_redirects(self):
        response = self.client.post(
            reverse("student_register"),
            {
                "student_code": "STU2001",
                "full_name": "Meera Das",
                "email": "meera@example.com",
            },
        )
        self.assertRedirects(response, reverse("student_list"))
        self.assertTrue(Student.objects.filter(student_code="STU2001").exists())
        self.assertContains(self.client.get(reverse("student_list")), "Meera Das")

    def test_invalid_post_does_not_save_student(self):
        response = self.client.post(
            reverse("student_register"),
            {
                "student_code": "BAD2001",
                "full_name": "Meera Das",
                "email": "meera@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student code must start with STU.")
        self.assertFalse(Student.objects.filter(student_code="BAD2001").exists())

    def test_csrf_is_required_for_post(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.get(reverse("student_register"))
        response = csrf_client.post(
            reverse("student_register"),
            {
                "student_code": "STU2002",
                "full_name": "Nina Das",
                "email": "nina@example.com",
            },
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(Student.objects.filter(student_code="STU2002").exists())

    def test_csrf_token_allows_valid_post(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.get(reverse("student_register"))
        token = csrf_client.cookies["csrftoken"].value
        response = csrf_client.post(
            reverse("student_register"),
            {
                "student_code": "STU2003",
                "full_name": "Kiran Das",
                "email": "kiran@example.com",
            },
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(student_code="STU2003").exists())


class AdminRegistrationTests(TestCase):
    def test_employee_is_registered_with_expected_admin(self):
        from .admin import EmployeeAdmin
        self.assertIn(Employee, admin.site._registry)
        self.assertIsInstance(admin.site._registry[Employee], EmployeeAdmin)

    def test_admin_login_page_is_available(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)


class RoutingAndTemplateTests(TestCase):
    def test_home_page_uses_base_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/home.html")
        self.assertTemplateUsed(response, "profiles/base.html")
        self.assertContains(response, "Phase 3 Django Reference")
        self.assertContains(response, "/static/profiles/css/site.css")

    def test_about_page_uses_inherited_layout(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/base.html")
        self.assertContains(response, "About this project")

    def test_integer_path_converter(self):
        response = self.client.get("/profile/25/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profile ID: 25")

    def test_string_path_converter(self):
        response = self.client.get("/member/asha/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Member: asha")

    def test_query_string_is_passed_to_template(self):
        response = self.client.get("/welcome/?name=asha")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, Asha")

    def test_query_string_uses_default_when_missing(self):
        response = self.client.get("/welcome/")
        self.assertContains(response, "Welcome, Guest")

    def test_employee_template_variables_tags_and_filters(self):
        response = self.client.get("/employee/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ASHA RAO")
        self.assertContains(response, "Backend Developer")
        self.assertContains(response, "Python")
        self.assertContains(response, "Skills are available.")

    def test_request_method_is_available_to_view(self):
        response = self.client.get("/request-info/")
        self.assertContains(response, "Method: GET")
