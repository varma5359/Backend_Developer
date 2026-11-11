from django.db import models


class Employee(models.Model):
    employee_code = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_code} - {self.full_name}"


class Department(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    student_code = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="students",
        null=True,
        blank=True,
    )
    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True,
    )

    def __str__(self):
        return f"{self.student_code} - {self.full_name}"


class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Profile: {self.student.full_name}"
