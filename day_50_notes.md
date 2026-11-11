# Day 50: Authorization, Permissions and Role-Based Access

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–5 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–49 — Django models, ORM, authentication, registration, sessions and protected views  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config / profiles / catalog  
**Approved mini-project:** Role-Based Employee Portal

> **Self-learning promise:** This lesson teaches the difference between being signed in and being allowed to perform an action. You will inspect Django permissions, create groups, assign permissions, protect views and test allowed and denied requests. Never assume that hiding a button is a security check.

---

# PART 1 — AUTHENTICATION IS NOT AUTHORIZATION

## 1. Business problem

Imagine an institute portal with three types of users:

- Student: views their own information.
- HR staff: manages employee records.
- Administrator: manages system-wide settings and users.

All three people may be authenticated. They should not all have the same access.

A student should not be able to delete employee records. HR staff may update employee details. Only an administrator may manage user permissions.

This is an authorization problem.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain authorization in simple language.
2. Distinguish authentication and authorization.
3. Explain permissions, groups and roles.
4. Identify Django's default model permissions.
5. Explain add, change, delete and view permissions.
6. Inspect a user's permissions.
7. Use has_perm().
8. Use permission_required.
9. Use PermissionRequiredMixin in a class-based view.
10. Create a group.
11. Assign permissions to a group.
12. Add a user to a group.
13. Test access for different user roles.
14. Understand why hiding a button is not authorization.
15. Understand the limits of model-level permissions.
16. Explain object-level authorization and ownership checks.
17. Diagnose 403, 302 and 404 access outcomes.
18. Complete Role-Based Employee Portal.

## 3. Important words

| Term | Simple meaning |
|---|---|
| Authentication | Proving which user is making the request |
| Authorization | Deciding what that user is allowed to do |
| Permission | A specific allowed action |
| Group | A collection of users that can share permissions |
| Role | A job responsibility such as HR staff or student |
| Access control | Rules that allow or deny access |
| Least privilege | Give each user only the access required |
| Model permission | Permission associated with a Django model operation |
| Object-level permission | Permission decision for one particular record |
| 403 Forbidden | Server understood the request but refuses access |
| 404 Not Found | Requested resource does not exist or is intentionally concealed |
| Decorator | Python wrapper that adds behavior to a function |
| Mixin | Reusable class behavior that can be combined with a class-based view |

## 4. Authentication versus authorization

| Authentication | Authorization |
|---|---|
| Who are you? | What may you do? |
| Verifies credentials | Checks access rules |
| Login is a common authentication action | Permission check is a common authorization action |
| Can create an authenticated session | Can allow or deny an operation |
| Example: student signs in | Example: student cannot delete employee records |

A user can be authenticated and still be denied access.

## 5. Example role matrix

| Action | Student | HR Staff | Administrator |
|---|---:|---:|---:|
| View own profile | Yes | Yes | Yes |
| View employee directory | Limited | Yes | Yes |
| Add employee | No | Yes | Yes |
| Change employee | No | Yes | Yes |
| Delete employee | No | No or restricted | Yes |
| Manage users and permissions | No | No | Yes |

This is a sample business policy. A real organization must define its own rules.

## 6. Least privilege

Least privilege means:
- Do not give every user administrator access.
- Give only the permissions needed for the user's work.
- Review permissions when responsibilities change.
- Remove access when a user no longer needs it.
- Test denied actions, not only successful actions.

It reduces the impact of mistakes and compromised accounts.

---

# PART 2 — DJANGO'S BUILT-IN PERMISSIONS

## 7. Where do model permissions come from?

Django can create default permissions for models.

For a model named Product in an app named catalog, common permissions include:
- add_product
- change_product
- delete_product
- view_product

The full permission strings are commonly:
- catalog.add_product
- catalog.change_product
- catalog.delete_product
- catalog.view_product

The app label and model name form the permission codename.

## 8. What does each permission mean?

### add

Allows a user to add a new object of the model.

Example:
- Create a new product.

### change

Allows a user to change existing objects of the model.

Example:
- Edit product name or price.

### delete

Allows a user to delete objects of the model.

Example:
- Remove a product record.

### view

Allows a user to view objects of the model through permission-aware application logic.

Important: Django does not automatically block every custom view just because a model has a view permission. Your view must check it.

## 9. When are default permissions created?

Django creates default model permissions as part of its permission/content-type machinery when migrations are applied and the app is installed.

Run:

~~~powershell
python manage.py migrate
~~~

If you add a new model, create and apply migrations:

~~~powershell
python manage.py makemigrations
python manage.py migrate
~~~

Do not create permission rows manually unless you have a specific custom permission requirement.

## 10. Inspect permissions in the shell

Run:

~~~powershell
python manage.py shell
~~~

Enter:

~~~python
from django.contrib.auth.models import Permission

Permission.objects.filter(
    content_type__app_label="catalog",
    content_type__model="product",
).values_list("codename", flat=True)
~~~

You should see codenames for the installed Product model, including default permissions if the migrations and permission creation have completed.

The exact output may contain additional custom permissions.

## 11. Understand content types

Django's contenttypes framework records which models exist in installed applications.

A Permission points to a content type and has a codename.

This is how Django can distinguish:
- catalog.change_product
- profiles.change_employee
- another_app.change_record

Do not confuse two permissions just because their codenames look similar. The app label is part of the permission identity.

## 12. Inspect the permission model

Django provides Permission through:

~~~python
from django.contrib.auth.models import Permission
~~~

A permission contains:
- name: human-readable description.
- codename: short internal identifier.
- content_type: model to which the permission belongs.

Use the permission API rather than hard-coding database IDs.

---

# PART 3 — CHECK A USER'S PERMISSIONS

## 13. Get the configured user model

Use:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()
~~~

This avoids assuming that the project always uses the default User class.

## 14. Retrieve a practice user

~~~python
user = User.objects.get(username="hr_demo")
~~~

If the user does not exist, Django raises User.DoesNotExist.

Create a fictional local account first if needed. Do not use a real staff account for experiments.

## 15. Check has_perm()

Example:

~~~python
user.has_perm("catalog.change_product")
~~~

The result is Boolean:
- True: the user has the permission.
- False: the user does not have the permission.

The user must be authenticated in the normal application workflow. Superusers are treated as having all permissions by Django's default permission handling.

## 16. Check multiple permissions

~~~python
user.has_perms([
    "catalog.view_product",
    "catalog.change_product",
])
~~~

This returns True only when all listed permissions are available.

## 17. Check any permission

~~~python
user.has_perms([
    "catalog.change_product",
    "catalog.delete_product",
])
~~~

This still requires all permissions. If the business rule is "either permission", check them separately:

~~~python
can_change = user.has_perm("catalog.change_product")
can_delete = user.has_perm("catalog.delete_product")

can_manage = can_change or can_delete
~~~

Understand the difference between AND and OR conditions.

## 18. Check a group membership

~~~python
user.groups.filter(name="HR Staff").exists()
~~~

This checks whether the user belongs to a group with that name.

For authorization decisions, checking the actual permission is often more flexible than checking a role label.

## 19. Why permission checks are better than username checks

Fragile approach:

~~~python
if request.user.username == "ravi":
    # allow edit
    ...
~~~

Problems:
- Usernames can change.
- Another administrator may need the same responsibility.
- Access policy is hidden inside application code.
- It is difficult to audit and maintain.

Better:

~~~python
if request.user.has_perm("catalog.change_product"):
    # allow edit
    ...
~~~

The permission can be assigned to an individual or group.

---

# PART 4 — PROTECT FUNCTION-BASED VIEWS

## 20. What is a function-based view?

A function-based view is a Python function that receives a request and returns a response.

Example:

~~~python
def product_list(request):
    ...
~~~

It can use decorators to enforce access rules before the main function runs.

## 21. Import permission_required

~~~python
from django.contrib.auth.decorators import permission_required
~~~

The decorator checks whether the current user has a required permission.

## 22. Protect a product update page

In catalog/views.py:

~~~python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product


@permission_required("catalog.change_product", raise_exception=True)
def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # Validate and save the submitted form here.
        ...
    else:
        # Display the form here.
        ...

    return render(
        request,
        "catalog/product_edit.html",
        {"product": product},
    )
~~~

This is a protection pattern. The ellipses are placeholders, not runnable implementation code. Use the ModelForm pattern from earlier lessons to complete the form behavior.

## 23. Understand raise_exception=True

By default, permission_required can redirect an unauthenticated user to the login page and may deny an authenticated user without permission.

With raise_exception=True, a user who lacks the permission receives PermissionDenied, which Django handles as a 403 response when DEBUG is False or through the configured error handling.

The setting is useful when the application should clearly deny the operation rather than redirect an authenticated user.

## 24. Protect add and delete separately

A user who can change a product should not automatically be allowed to delete it.

Use separate permission checks:

~~~python
@permission_required("catalog.add_product", raise_exception=True)
def product_create(request):
    ...
~~~

~~~python
@permission_required("catalog.delete_product", raise_exception=True)
def product_delete(request, product_id):
    ...
~~~

The view implementation must still validate input and use safe HTTP methods.

## 25. Permission checks do not replace form validation

A permission check answers:
"May this user perform the action?"

A form answers:
"Are the submitted values valid?"

You need both:
- Authorization check.
- Input validation.
- CSRF protection.
- Correct database operation.

---

# PART 5 — PROTECT CLASS-BASED VIEWS

## 26. What is a class-based view?

A class-based view defines behavior through a Python class.

Django provides generic class-based views for common tasks such as:
- ListView.
- DetailView.
- CreateView.
- UpdateView.
- DeleteView.

A class-based view can use mixins to add reusable behavior.

## 27. What is PermissionRequiredMixin?

PermissionRequiredMixin checks whether a user has the permission required by a class-based view.

Import:

~~~python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView
~~~

Example:

~~~python
class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "category", "price", "stock", "is_active"]
    template_name = "catalog/product_edit.html"
    permission_required = "catalog.change_product"
    raise_exception = True
~~~

This example assumes the model and template exist.

## 28. Understand the class attributes

| Attribute | Meaning |
|---|---|
| model | Model whose records are edited |
| fields | Form fields exposed by the view |
| template_name | Template used for display |
| permission_required | Permission needed to use the view |
| raise_exception | Raise PermissionDenied when access is denied |

Do not expose sensitive model fields in a generic form.

## 29. Add the class-based view URL

~~~python
from django.urls import path
from .views import ProductUpdateView

urlpatterns = [
    path(
        "products/<int:pk>/edit/",
        ProductUpdateView.as_view(),
        name="product_edit",
    ),
]
~~~

If the file already imports views or has other routes, merge the new route into the existing urlpatterns.

## 30. Function-based versus class-based protection

| Function-based view | Class-based view |
|---|---|
| permission_required decorator | PermissionRequiredMixin |
| Applied above function | Inherited by view class |
| Uses function arguments | Uses class attributes and methods |
| Good for direct custom flow | Good for reusable generic view behavior |

Choose the style that makes the view easiest to understand and maintain.

---

# PART 6 — GROUPS AND ROLE-BASED ACCESS

## 31. What is a group?

A group is a collection of users.

You can assign permissions to a group. Users who belong to that group receive those permissions through Django's permission system.

Example groups:
- Students.
- HR Staff.
- Product Managers.
- Administrators.

A group is not automatically a role-based security system. You must define the policy and enforce it in views.

## 32. Why groups are useful

Imagine 30 HR employees need permission to change employee records.

Without groups:
- You might assign the permission to each user individually.
- New HR staff require repeated manual changes.
- Removing access requires editing multiple accounts.

With groups:
1. Create HR Staff group.
2. Assign the required permissions once.
3. Add HR users to the group.
4. New members inherit the group's permissions.
5. Remove a member from the group when the role changes.

## 33. Import Group and Permission

Open the Django shell:

~~~powershell
python manage.py shell
~~~

Enter:

~~~python
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model

User = get_user_model()
~~~

## 34. Create an HR Staff group

~~~python
hr_group, created = Group.objects.get_or_create(
    name="HR Staff"
)
~~~

get_or_create() prevents a duplicate group name when the command is repeated.

## 35. Find product permissions

~~~python
change_product = Permission.objects.get(
    content_type__app_label="catalog",
    codename="change_product",
)

view_product = Permission.objects.get(
    content_type__app_label="catalog",
    codename="view_product",
)

add_product = Permission.objects.get(
    content_type__app_label="catalog",
    codename="add_product",
)
~~~

The permission lookup uses the app label and codename.

If the permission is missing:
- Confirm catalog is installed.
- Confirm Product model exists.
- Run migrations.
- Confirm the actual app label and model name.

## 36. Assign permissions to the group

~~~python
hr_group.permissions.add(
    view_product,
    change_product,
)
~~~

This group can view and change products according to these model permissions.

We intentionally did not add delete_product.

## 37. Add a user to the group

~~~python
hr_user = User.objects.get(username="hr_demo")
hr_user.groups.add(hr_group)
~~~

The user now receives the group's permissions.

## 38. Verify group permissions

~~~python
hr_user.has_perm("catalog.view_product")
hr_user.has_perm("catalog.change_product")
hr_user.has_perm("catalog.delete_product")
~~~

Expected:
- view_product: True.
- change_product: True.
- delete_product: False.

The result assumes the user is not a superuser and no other group or direct permission grants delete access.

## 39. Create a Student group

~~~python
student_group, created = Group.objects.get_or_create(
    name="Students"
)
~~~

Assign only the permissions that match the business policy.

For example, if students may view the product catalog:

~~~python
student_group.permissions.add(view_product)
~~~

Add a fictional student:

~~~python
student_user = User.objects.get(username="student_demo")
student_user.groups.add(student_group)
~~~

## 40. Remove a user from a group

~~~python
hr_user.groups.remove(hr_group)
~~~

The user's permissions from that group are removed.

Other direct or group permissions may still grant access. Always test the final permission result.

## 41. Remove a permission from a group

~~~python
hr_group.permissions.remove(change_product)
~~~

Now HR Staff group members no longer receive that permission from this group.

## 42. Why group names are not enough

A view could check:

~~~python
request.user.groups.filter(name="HR Staff").exists()
~~~

This is sometimes useful for displaying role-specific UI, but the actual access decision should normally use the permission:

~~~python
request.user.has_perm("catalog.change_product")
~~~

Permissions are more flexible because the same action can be granted to different groups.

---

# PART 7 — BUILD A ROLE-BASED EMPLOYEE PORTAL

## 43. Project scenario

An institute wants an employee portal with three user categories:
- Student.
- HR Staff.
- Administrator.

For this mini-project, use the existing Employee model from the profiles app if it is already part of the pathway project.

The goal is to enforce a clear policy:
- HR staff can view and update employee records.
- Students cannot update employee records.
- Only users with the delete permission can delete records.

The project should not rely on a username hard-coded into a view.

## 44. Identify the model and permissions

Before writing code:
1. Open profiles/models.py.
2. Locate the Employee model.
3. Confirm the app label is profiles.
4. Confirm the Employee model exists.
5. Confirm migrations have been applied.
6. Inspect the permission codenames.

For a model named Employee in profiles, default permissions normally use:
- profiles.view_employee
- profiles.add_employee
- profiles.change_employee
- profiles.delete_employee

If your actual model or app name differs, use the real permission string.

## 45. Create groups for the Employee model

Open shell:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth.models import Group, Permission

hr_group, _ = Group.objects.get_or_create(name="HR Staff")
student_group, _ = Group.objects.get_or_create(name="Students")

view_employee = Permission.objects.get(
    content_type__app_label="profiles",
    codename="view_employee",
)

change_employee = Permission.objects.get(
    content_type__app_label="profiles",
    codename="change_employee",
)

hr_group.permissions.add(
    view_employee,
    change_employee,
)

student_group.permissions.add(view_employee)
~~~

This is an example policy:
- HR Staff can view and change.
- Students can view.
- Neither group receives delete permission here.

## 46. Create a protected employee directory view

In profiles/views.py, add:

~~~python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Employee


@permission_required(
    "profiles.view_employee",
    raise_exception=True,
)
def employee_directory(request):
    employees = Employee.objects.all().order_by("full_name")

    return render(
        request,
        "profiles/employee_directory.html",
        {"employees": employees},
    )
~~~

This assumes Employee has a full_name field. If the approved model uses a different field, update the ordering to match the actual model.

## 47. Create a protected update view pattern

A complete update should use a ModelForm from the existing Employee model.

The access-control pattern is:

~~~python
@permission_required(
    "profiles.change_employee",
    raise_exception=True,
)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    # Bind and validate the Employee ModelForm.
    # Save only when the form is valid.
    # Return the form with errors otherwise.
~~~

This snippet illustrates the permission boundary. It is not a complete view until the form handling from Days 39–40 is connected.

## 48. Add URLs

In profiles/urls.py, add or merge:

~~~python
path(
    "employees/",
    views.employee_directory,
    name="employee_directory",
),
path(
    "employees/<int:pk>/edit/",
    views.employee_update,
    name="employee_update",
),
~~~

Make sure the views are defined and the import path is correct.

## 49. Template-level visibility

A template can hide an edit link from a user without the permission:

~~~django
{% if perms.profiles.change_employee %}
    <a href="{% url 'employee_update' employee.pk %}">
        Edit employee
    </a>
{% endif %}
~~~

This improves the user interface.

It is not the security boundary. A user can manually enter the edit URL. The view must still enforce permission_required.

## 50. Test direct URL access

Use two different test accounts:
- hr_demo belongs to HR Staff.
- student_demo belongs to Students.

Test:
1. Sign in as HR.
2. Open employee directory.
3. Open employee edit URL.
4. Confirm allowed access.
5. Sign out.
6. Sign in as student.
7. Open employee directory.
8. Try employee edit URL directly.

Expected:
- HR can access the edit view if the permission is assigned.
- Student is denied the edit view.
- Hiding the link alone is not considered a successful authorization test.

---

# PART 8 — MODEL PERMISSIONS VERSUS OBJECT PERMISSIONS

## 51. What does a model permission control?

A model permission is generally about an operation on a model type.

Example:
- catalog.change_product

It does not automatically mean the user can edit every object under every business rule.

## 52. What is object-level authorization?

Object-level authorization decides whether a user can access one particular record.

Example:
- A student can view their own StudentProfile.
- The student cannot view another student's profile.
- An employee manager can edit employees in their department.
- A support agent can view tickets assigned to them.

## 53. Why model permissions are not enough

Suppose every signed-in student has profiles.view_studentprofile.

That permission alone does not prove the student should see every student profile.

The view must also check ownership or another object-level rule.

## 54. Example ownership check

~~~python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

@login_required
def my_profile(request):
    profile = get_object_or_404(
        StudentProfile,
        user=request.user,
    )

    return render(
        request,
        "profiles/my_profile.html",
        {"profile": profile},
    )
~~~

This query returns only the profile connected to the current user.

It does not accept a user ID from the browser.

## 55. Example department restriction

Suppose an HR user can manage employees only in their department.

A model-level permission can grant general change capability, but the view must also filter by department.

Conceptual example:

~~~python
employee = get_object_or_404(
    Employee,
    pk=employee_id,
    department=request.user.profile.department,
)
~~~

This is illustrative. The actual relationship names must match your models.

## 56. Avoid insecure direct object references

Do not assume that a URL such as /employees/15/edit/ is safe because the user cannot see the link.

A user can change 15 to 16.

Always:
- Authenticate the user.
- Check the required permission.
- Check object ownership or scope.
- Return a safe response if access is denied.

---

# PART 9 — TESTING PERMISSIONS

## 57. Why test allowed and denied users?

A permission feature is incomplete if it tests only the administrator.

You must test:
- User with permission.
- User without permission.
- Anonymous visitor.
- User with permission through a group.
- User whose permission was removed.

## 58. Test permission behavior in the shell

~~~python
hr_user.has_perm("profiles.change_employee")
student_user.has_perm("profiles.change_employee")
~~~

Expected:
- HR: True if group assignment is correct.
- Student: False if no other grant exists.

## 59. Add a permission test

In profiles/tests.py, add or merge:

~~~python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class EmployeePermissionTests(TestCase):
    def setUp(self):
        self.hr_user = User.objects.create_user(
            username="test_hr_user",
            password="Test-Only-Password-123!",
        )
        self.student_user = User.objects.create_user(
            username="test_student_user",
            password="Test-Only-Password-123!",
        )

        self.hr_group = Group.objects.create(name="Test HR Staff")
        self.view_permission = Permission.objects.get(
            content_type__app_label="profiles",
            codename="view_employee",
        )
        self.change_permission = Permission.objects.get(
            content_type__app_label="profiles",
            codename="change_employee",
        )

        self.hr_group.permissions.add(
            self.view_permission,
            self.change_permission,
        )
        self.hr_user.groups.add(self.hr_group)

    def test_hr_user_has_change_permission(self):
        self.assertTrue(
            self.hr_user.has_perm("profiles.change_employee")
        )

    def test_student_does_not_have_change_permission(self):
        self.assertFalse(
            self.student_user.has_perm("profiles.change_employee")
        )
~~~

These tests verify permission assignment. Add request-level tests for your actual protected view after confirming the route and model form are integrated.

## 60. Test request-level access

For a protected view that exists:

~~~python
self.client.force_login(self.student_user)
response = self.client.get(
    reverse("employee_update", args=[employee.pk])
)
self.assertEqual(response.status_code, 403)
~~~

This assumes:
- employee_update exists.
- It uses permission_required with raise_exception=True.
- employee exists.
- URL name and arguments match the project.

A test must reflect the actual project implementation.

## 61. Run tests

~~~powershell
python manage.py check
python manage.py test profiles
~~~

Read the output. Do not ignore a failing permission test.

---

# PART 10 — COMMON HTTP ACCESS RESPONSES

## 62. HTTP 302 redirect

A redirect tells the browser to request another URL.

A protected view may redirect an anonymous visitor to login.

## 63. HTTP 403 Forbidden

The request is understood, but the application refuses access.

An authenticated user without a required permission may receive 403 when the view is configured to raise PermissionDenied.

## 64. HTTP 404 Not Found

The requested resource does not exist.

Some applications intentionally return 404 for objects the current user is not allowed to discover. This can reduce information disclosure.

Choose the response deliberately and consistently.

## 65. Do not confuse the responses

| Status | Meaning | Example |
|---|---|---|
| 200 | Request succeeded | Authorized user sees page |
| 302 | Redirect | Anonymous visitor sent to login |
| 403 | Forbidden | Authenticated user lacks permission |
| 404 | Not found | Missing or concealed object |
| 405 | Method not allowed | GET sent to POST-only action |

---

# PART 11 — SECURITY CHECKLIST

## 66. Never trust the interface

A hidden button does not protect a URL.

The backend view must enforce the permission.

## 67. Never use username as a role

Do not grant access because a username matches a hard-coded string.

Use permissions and groups.

## 68. Avoid superuser for normal testing

A superuser has all permissions and can hide mistakes in your permission configuration.

Use ordinary test accounts to verify the role policy.

## 69. Follow least privilege

Do not assign delete permission if the user only needs view and change access.

Do not give all permissions to a group for convenience.

## 70. Review access after role changes

When a staff member changes role:
- Remove them from groups they no longer need.
- Add the new group.
- Review direct permissions.
- Verify the final permission set.

## 71. Keep object ownership separate

A user may have a model permission but still should not see every record.

Check ownership, department, tenant or assignment where required.

## 72. Audit administrative changes

Production systems should record important permission changes:
- Who changed the group.
- Which permission changed.
- Which user was affected.
- When it happened.

Do not log passwords or session tokens.

---

# PART 12 — APPROVED MINI-PROJECT

## 73. Role-Based Employee Portal

### Business problem

Build a portal where different categories of users have different responsibilities.

### Functional requirements

1. Use the existing Employee model.
2. Create Students and HR Staff groups.
3. Assign view/change permissions according to the approved role matrix.
4. Add fictional test users to groups.
5. Protect employee directory access.
6. Protect employee update access.
7. Hide edit controls when the user lacks permission.
8. Enforce permission checks in the backend view.
9. Test direct URL access.
10. Test users with and without permissions.
11. Explain the difference between model permission and object ownership.
12. Document the role policy.

### Acceptance criteria

- [ ] Groups exist.
- [ ] Permissions are assigned correctly.
- [ ] HR user has the expected permission.
- [ ] Student user does not have the change permission.
- [ ] Anonymous user is redirected or denied as configured.
- [ ] Unauthorized direct URL access is blocked.
- [ ] Template visibility matches the permission.
- [ ] Backend protection works even when a URL is typed manually.
- [ ] Tests pass.
- [ ] No user is made superuser merely to bypass a permission problem.

### Submission evidence

- Role/permission matrix.
- Group creation and assignment code.
- Updated protected views.
- Browser screenshots using fictional users.
- Automated test output.
- README explaining how to create the groups and test access.

---

# PART 13 — SELF-ASSESSMENT

## 74. Short-answer questions

1. What is authorization?
2. How is it different from authentication?
3. What is a Django model permission?
4. Name the four default model permissions.
5. What is a group?
6. Why are groups useful?
7. What does has_perm() return?
8. What does permission_required do?
9. What is PermissionRequiredMixin?
10. Why is hiding a button not enough?
11. What is least privilege?
12. What is an object-level permission decision?
13. Why should a student not automatically see every student record?
14. What is the difference between 403 and 404?
15. Why should permission tests use ordinary users rather than superusers?

## 75. Self-check answers

1. Authorization decides which actions or resources a user may access.
2. Authentication verifies identity; authorization checks access rights.
3. A permission associated with an application model operation.
4. add, change, delete and view.
5. A collection of users that can share permissions.
6. One permission assignment can apply to many users.
7. A Boolean indicating whether the user has the permission.
8. It protects a function-based view with a required permission.
9. A reusable class-based view mixin for permission checks.
10. A user can manually request the URL.
11. Give only the access required for the user's task.
12. A decision about access to one specific record.
13. Ownership and privacy rules must be enforced.
14. 403 means access is forbidden; 404 means the resource is not found or concealed.
15. Superusers bypass normal permission restrictions and can hide configuration mistakes.

## 76. MCQ assessment

### Question 1
What does authorization decide?

- A. Which Python interpreter is active
- B. What an authenticated user may do
- C. Which template is loaded
- D. Which database is installed

**Answer: B.** Authorization applies access rules to actions and resources.

### Question 2
Which permission allows changing a Product model record?

- A. catalog.add_product
- B. catalog.change_product
- C. catalog.view_product
- D. catalog.login_product

**Answer: B.** change_product is the model's change permission.

### Question 3
What is the purpose of a Django Group?

- A. Store CSS
- B. Share permissions among users
- C. Replace the database
- D. Generate a URL

**Answer: B.** Users in a group receive the permissions assigned to that group.

### Question 4
Why must the backend check permissions?

- A. Buttons cannot be hidden
- B. Users can manually request URLs
- C. Django has no templates
- D. All users are anonymous

**Answer: B.** Interface visibility is not a security boundary.

### Question 5
Which response means the user is forbidden from accessing a resource?

- A. 200
- B. 302
- C. 403
- D. 500

**Answer: C.** 403 Forbidden indicates the server refuses the request.

---

# PART 14 — INTERVIEW PREPARATION

## 77. Explain authentication versus authorization

**Answer:** Authentication verifies who the user is. Authorization decides what that user may do. A user can sign in successfully and still be denied permission to edit an employee record.

**Follow-up:** Which Django feature helps implement authorization?

**Answer:** Model permissions, groups, permission decorators and permission mixins.

## 78. What are Django model permissions?

**Answer:** Django creates default add, change, delete and view permissions for models. The permission string includes the app label and model codename, such as profiles.change_employee.

**Follow-up:** Does Django automatically protect every custom view using those permissions?

**Answer:** No. The view must explicitly check the required permission.

## 79. What is the use of groups?

**Answer:** Groups allow multiple users to share permissions. Instead of assigning the same permission to each HR user individually, assign it to the HR Staff group and add the users to that group.

**Follow-up:** Does group membership alone define every object-level access rule?

**Answer:** No. A view may also need ownership or department checks.

## 80. Why is hiding a button not authorization?

**Answer:** A user can manually enter the URL or send a request without using the visible button. The server must enforce permission checks inside the view.

## 81. Scenario: a student can edit an employee record

**Answer:** Check the backend view. It may be missing permission_required or an equivalent check. Also inspect group membership and direct permissions. Do not rely on the template hiding the edit link.

## 82. Scenario: HR users can delete products unexpectedly

**Answer:** Inspect all groups and direct permissions assigned to the user. Remove unnecessary delete permissions and test with an ordinary user account.

## 83. Scenario: a user has change permission but should edit only their department

**Answer:** Model-level permission is not enough. The view must also check the employee's department against the user's allowed department.

---

# PART 15 — INDEPENDENT COMPLETION

## 84. Draw the authorization flow

Include:
1. Browser request.
2. Authentication middleware.
3. Current user.
4. Required permission check.
5. Group/direct permission lookup.
6. Allowed or denied response.
7. Optional object ownership check.

## 85. Controlled debugging

In a local practice copy:
- Remove a user's group membership and test again.
- Remove change permission from the group.
- Try a direct URL while logged in as a student.
- Give the student the permission and verify the result changes.
- Remove it again.
- Confirm that the template and backend behavior agree.

Do not perform these tests on a real production account.

## 86. Final checklist

- [ ] I can explain authentication and authorization.
- [ ] I understand model permissions.
- [ ] I understand groups.
- [ ] I can use has_perm().
- [ ] I can protect function-based views.
- [ ] I can protect class-based views.
- [ ] I understand least privilege.
- [ ] I understand object-level authorization.
- [ ] I tested allowed and denied users.
- [ ] I tested direct URL access.
- [ ] I completed Role-Based Employee Portal.
- [ ] I ran the tests.
- [ ] I completed MCQs and interview questions.

**Next lesson:** Day 51 — Custom User Models and User Profile Management.

---

## 87. Official references

1. Django permissions and authorization: https://docs.djangoproject.com/en/5.2/topics/auth/default/
2. Django authentication customization: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/
3. Django class-based view mixins: https://docs.djangoproject.com/en/5.2/topics/auth/default/
4. Django permissions reference: https://docs.djangoproject.com/en/5.2/ref/contrib/auth/

**Version reminder:** This lesson targets Django 5.2.19. Permission strings depend on the real app label and model name. Verify them in the project before using the examples.
