# Day 51: Custom User Models and User Profile Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–6 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–50 — Django models, relationships, authentication, password management, sessions, permissions and groups  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** Main student_portal remains on its existing user model; a separate fresh project is used for the custom user model experiment  
**Approved mini-project:** Custom User Profile System

> **Critical migration warning:** The existing student_portal has already applied migrations. Do not casually change AUTH_USER_MODEL in that project. Changing the user model after the first migrations can require complex schema and data migrations. This lesson uses a separate fresh practice project for the custom user model, and explains profile management separately.

---

# PART 1 — WHY CUSTOM USER MODELS EXIST

## 1. The default user model

Django provides a built-in user model.

It already supports:
- Username.
- Password.
- First and last name.
- Email field.
- Active status.
- Staff status.
- Superuser status.
- Permissions and groups.

For many applications, the default model is sufficient.

## 2. When might a project need a custom user model?

Imagine a company portal where:
- Users sign in using email rather than username.
- Every account has an employee number.
- The application has a required account category.
- The organization needs a custom authentication identity field.

A custom user model lets the project define user fields and behavior that fit its requirements.

Do not create a custom user model just because it looks more advanced. It creates long-term design and migration responsibilities.

## 3. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain the default Django user model.
2. Explain why a project might use a custom user model.
3. Explain AbstractUser and AbstractBaseUser at a high level.
4. Identify the correct point to configure AUTH_USER_MODEL.
5. Explain why changing user models after migrations is difficult.
6. Create a separate fresh practice project.
7. Create an accounts application.
8. Define a custom user model based on AbstractUser.
9. Configure AUTH_USER_MODEL before the first migration.
10. Run migrations in the correct order.
11. Use get_user_model() in Python code.
12. Use settings.AUTH_USER_MODEL in model relationships.
13. Understand why reusable code should avoid hard-coded User imports.
14. Distinguish a custom user model from a profile model.
15. Build a one-to-one user profile in the main project without changing its user model.
16. Validate and update profile data.
17. Test profile ownership and privacy.
18. Complete Custom User Profile System.

## 4. Important terms

| Term | Simple meaning |
|---|---|
| Default user model | User model supplied by Django |
| Custom user model | Project-defined user model |
| AbstractUser | Django base class with common user fields and behavior |
| AbstractBaseUser | Lower-level base class for a more customized user model |
| AUTH_USER_MODEL | Setting that identifies the project's configured user model |
| get_user_model() | Function returning the configured user model class |
| Profile model | Separate model holding additional user details |
| OneToOneField | Relationship where one record connects to one record |
| Migration | Versioned database schema operation |
| Swappable model | Model that can be replaced through Django's model configuration |
| Manager | Object providing database creation/query operations for a model |

---

# PART 2 — CUSTOM USER MODEL DESIGN

## 5. AbstractUser

AbstractUser is a Django abstract model that already includes the common user fields and authentication behavior.

A project can inherit from it and add or adjust fields.

Example idea:

~~~python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    employee_code = models.CharField(max_length=20, unique=True)
~~~

This is often easier than building authentication from a lower-level base class.

## 6. AbstractBaseUser

AbstractBaseUser provides a more minimal foundation for custom authentication.

A developer using it must define more of the account model behavior, such as:
- Which field identifies the user.
- Required fields.
- User manager behavior.
- Permission integration as needed.
- Admin integration.
- Authentication-related methods and properties.

It provides flexibility but requires more careful implementation.

For this pathway, use AbstractUser. Do not build a custom authentication backend from scratch.

## 7. AbstractUser versus AbstractBaseUser

| AbstractUser | AbstractBaseUser |
|---|---|
| Includes common username and user fields | Provides a more minimal foundation |
| Includes much of Django's standard user behavior | Requires more configuration |
| Good for adding fields or changing some defaults | Good for substantially different identity design |
| Easier for beginners | More advanced |
| Less custom code | More responsibility |

## 8. Custom user model versus profile model

These are not the same.

A custom user model changes the account model itself.

A profile model stores additional information in a separate table linked to a user.

Examples:
- User account: username, password, email, active status.
- Profile: phone number, address, biography, profile photo, department.

A project can use the default user model and a separate profile model.

## 9. Decision guide

Use the default user model when:
- Standard account fields are sufficient.
- Username/password login is appropriate.
- The project has no strong identity customization requirement.

Use a custom user model when:
- The identity field must differ.
- Additional account-level fields are essential.
- The project has a clear long-term requirement.
- The decision is made before initial migrations.

Use a profile model when:
- Authentication identity can remain standard.
- Additional personal or business information belongs separately.
- The project already uses the default user model and changing it would be risky.

---

# PART 3 — MIGRATION TIMING: READ BEFORE CODING

## 10. Why the first migration matters

Django's user model is referenced by several authentication and application tables.

Other models may contain foreign keys to the user model.

When migrations are created and applied, the database schema and migration history become dependent on the configured user model.

If you change AUTH_USER_MODEL later:
- Existing foreign keys may point to the previous user table.
- Migration dependencies may no longer match.
- Existing account records may need transformation.
- Permission and group relationships may need migration.
- Data loss can occur if the change is not planned carefully.

## 11. The rule for this lesson

The main student_portal project has already applied migrations. It also already has a StudentProfile model linked to the Student domain model from Day 38. That existing StudentProfile must remain unchanged for the college relationship exercises.

Do not change its AUTH_USER_MODEL or repurpose StudentProfile.

We will create a separate fresh practice project named custom_user_demo.

This project will:
1. Start with a new folder.
2. Have a new virtual environment.
3. Install the agreed Django version.
4. Create the accounts app.
5. Define the custom user model.
6. Set AUTH_USER_MODEL.
7. Only then run the first migrations.

## 12. Why not delete the main database?

Deleting the main database to test a custom user model is unsafe.

It may destroy:
- Employee records.
- Student records.
- Product records.
- User accounts.
- Migration history.
- Other learner work.

A separate practice project avoids this risk.

Never use a destructive reset as a shortcut.

---

# PART 4 — CREATE A FRESH PRACTICE PROJECT

## 13. Create a workspace folder

Open PowerShell in a location where you keep practice projects.

Example:

~~~powershell
mkdir custom_user_demo
cd custom_user_demo
~~~

Check:

~~~powershell
Get-Location
~~~

## 14. Create a virtual environment

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
~~~

Verify:

~~~powershell
python --version
python -c "import sys; print(sys.executable)"
~~~

## 15. Install Django

~~~powershell
python -m pip install "Django==5.2.19"
python -m django --version
~~~

Expected version:

~~~text
5.2.19
~~~

## 16. Create the project

~~~powershell
django-admin startproject config .
~~~

The dot means the current directory.

Expected structure:

~~~text
custom_user_demo/
├── .venv/
├── manage.py
└── config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
~~~

## 17. Create accounts app

~~~powershell
python manage.py startapp accounts
~~~

Django creates the app folder and its standard files.

Expected:

~~~text
accounts/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
~~~

## 18. Register the app

Open config/settings.py.

Add accounts to INSTALLED_APPS:

~~~python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts.apps.AccountsConfig",
]
~~~

Do not add a custom user model to the main project. This setting is for the separate fresh custom_user_demo project.

---

# PART 5 — CREATE THE CUSTOM USER MODEL

## 19. Open accounts/models.py

Replace the empty generated file with:

~~~python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    employee_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.username
~~~

This is a beginner custom user model based on AbstractUser.

## 20. Explain the imports

AbstractUser:
- Supplies Django's standard user fields and behavior.
- Allows the project to add fields without rebuilding the entire authentication model.

models:
- Provides Django model field classes.
- CharField stores short text.

## 21. Explain class inheritance

~~~python
class User(AbstractUser):
~~~

This defines a new model named User.

It inherits the fields and methods from AbstractUser.

The new model includes the standard user behavior plus the custom fields.

## 22. Explain employee_code

~~~python
employee_code = models.CharField(
    max_length=20,
    unique=True,
    blank=True,
    null=True,
)
~~~

- CharField stores text.
- max_length=20 limits the text length.
- unique=True prevents duplicate non-null employee codes.
- blank=True allows a form to leave it empty.
- null=True allows the database column to contain NULL.

For a real application, decide carefully whether employee_code is optional. The combination of blank and null is a design choice, not a universal rule.

## 23. Explain department

~~~python
department = models.CharField(
    max_length=100,
    blank=True,
)
~~~

This field stores a department label.

It is optional at the form-validation level because blank=True is set.

If the application needs a normalized Department table with relationships, use a ForeignKey instead of free-text values.

## 24. Explain __str__()

~~~python
def __str__(self):
    return self.username
~~~

This method returns a readable string representation of the model instance.

It improves the display in:
- Django admin.
- Shell output.
- Debugging.
- Related object selection.

---

# PART 6 — CONFIGURE AUTH_USER_MODEL BEFORE MIGRATIONS

## 25. Open config/settings.py

Add:

~~~python
AUTH_USER_MODEL = "accounts.User"
~~~

This value uses:
- accounts: app label.
- User: model name.

The setting tells Django which model represents users in this project.

## 26. Why the setting must be added now

We have not applied the first migrations in this fresh project.

This is the correct time to select the custom user model.

Do not copy this setting into the already-migrated student_portal project.

## 27. Confirm the setting

Run:

~~~powershell
python manage.py shell
~~~

Enter:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()
User
~~~

Expected model:

~~~text
<class 'accounts.models.User'>
~~~

Exit:

~~~python
exit()
~~~

If Django reports the default auth user model, check the spelling and location of AUTH_USER_MODEL.

---

# PART 7 — CREATE MIGRATIONS IN THE CORRECT ORDER

## 28. Run makemigrations

~~~powershell
python manage.py makemigrations accounts
~~~

Django creates a migration describing the custom User model.

## 29. Inspect the migration

~~~powershell
python manage.py showmigrations
~~~

The accounts app should now have a migration file.

The migration file is Python code describing database schema operations. Do not edit it casually.

## 30. Apply migrations

~~~powershell
python manage.py migrate
~~~

Django creates:
- Custom user table.
- Group and permission relationships.
- Authentication tables.
- Session table.
- Admin and content type tables.

The exact table names are generated by Django based on app and model configuration.

## 31. Verify the model

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.count()
~~~

Expected: an integer, often 0 in a fresh database.

## 32. Create a test user

~~~python
User.objects.create_user(
    username="custom_demo",
    password="Custom-Demo-Password-123!",
    employee_code="EMP-CUSTOM-01",
    department="Engineering",
)
~~~

Use fictional local data only.

## 33. Verify the custom fields

~~~python
user = User.objects.get(username="custom_demo")
user.employee_code
user.department
user.check_password("Custom-Demo-Password-123!")
~~~

Expected:
- Employee code: EMP-CUSTOM-01.
- Department: Engineering.
- Password check: True.

---

# PART 8 — CUSTOM USER MODEL ADMIN

## 34. Why admin configuration matters

The default Django UserAdmin is designed for Django's default user model.

A custom model may contain extra fields. The admin must be configured to display and edit them appropriately.

## 35. Register the custom user model

Open accounts/admin.py.

Use:

~~~python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Organization details",
            {
                "fields": (
                    "employee_code",
                    "department",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Organization details",
            {
                "fields": (
                    "employee_code",
                    "department",
                )
            },
        ),
    )
~~~

This extends the standard UserAdmin with the custom fields.

## 36. Create a superuser in the fresh project

~~~powershell
python manage.py createsuperuser
~~~

Enter fictional local practice details.

Then run:

~~~powershell
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/admin/
~~~

Sign in using the local superuser.

Verify that employee_code and department appear in the admin form.

---

# PART 9 — USE THE CUSTOM USER MODEL IN OTHER MODELS

## 37. Use settings.AUTH_USER_MODEL

In a model that points to the user, use:

~~~python
from django.conf import settings
from django.db import models


class UserPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="preference",
    )
    theme = models.CharField(
        max_length=20,
        default="light",
    )
~~~

This relationship works with the configured user model.

## 38. Why not import User directly?

A direct import can create a hard dependency on one model class.

Using settings.AUTH_USER_MODEL lets Django resolve the configured user model through its model relationship system.

## 39. Use get_user_model() in runtime code

In views or service functions:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()
~~~

This obtains the model class configured for the current project.

## 40. Use string references carefully

In model relationship declarations, the setting is generally preferred:

~~~python
settings.AUTH_USER_MODEL
~~~

For a specific model in the same or another app, a string reference can be used where appropriate. Follow Django's model relationship guidance.

---

# PART 10 — PROFILE MODEL IN THE MAIN STUDENT PORTAL

## 41. A profile does not require a custom user model

The main student_portal already has a migrated database and a configured user model.

We can still store additional user details in a separate profile model.

This is a different exercise from custom_user_demo.

Do not change AUTH_USER_MODEL in student_portal.

## 42. What belongs in a profile?

Possible profile fields:
- Phone number.
- Biography.
- City.
- Profile image.
- Department.
- LinkedIn URL.

Do not place every business record into the user model.

Keep authentication identity separate from optional profile information where appropriate.

## 43. Inspect the existing profiles app

Open student_portal/profiles/models.py.

Before adding a model:
1. Read the complete file.
2. Identify existing Employee, Student, Department and Course models.
3. Check whether a profile model already exists.
4. Do not create duplicate classes.
5. Choose a model name that matches the approved pathway design.

## 44. Add a UserProfile model only if it does not already exist

Example:

~~~python
from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )
    city = models.CharField(
        max_length=80,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f"Profile for {self.user.username}"
~~~

If an equivalent model already exists, extend it carefully rather than adding another profile model.

## 45. Understand OneToOneField

OneToOneField means:
- One user can have one profile record.
- One profile belongs to one user.
- The relationship is unique at the database level.

It is useful when optional profile data is kept separate from account identity.

## 46. Understand on_delete

CASCADE means that when the referenced user is deleted, the related profile is also deleted.

This is a business/data-retention decision.

Other on_delete choices include PROTECT and SET_NULL, each with different behavior. Choose based on the data-retention requirements.

## 47. Create migrations only for the main profile change

If you actually add the model to student_portal:

~~~powershell
python manage.py makemigrations profiles
python manage.py migrate
~~~

Do not run these commands inside custom_user_demo by mistake.

Check Get-Location and confirm which project contains manage.py.

---

# PART 11 — PROFILE FORM AND OWNERSHIP

## 48. Create a profile ModelForm

In profiles/forms.py, add or merge:

~~~python
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "phone_number",
            "city",
            "bio",
        ]
~~~

This form deliberately does not allow the browser to choose the user relationship.

The view assigns the profile to request.user.

## 49. Why exclude the user field?

If the browser can submit an arbitrary user ID, one student may attempt to create or update another student's profile.

The view should determine the current user from the authenticated request.

Do not trust a user_id value submitted by the browser.

## 50. Create or update the current user's profile

In profiles/views.py, add:

~~~python
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def edit_user_profile(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            instance=profile,
        )

        if form.is_valid():
            form.save()
            return redirect("account_summary")
    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        "profiles/edit_user_profile.html",
        {"form": form},
    )
~~~

## 51. Understand get_or_create

get_or_create() tries to find a profile for the current user.

If one exists:
- It returns the existing profile.
- created is False.

If one does not exist:
- It creates a profile connected to request.user.
- created is True.

The OneToOneField uniqueness rule prevents multiple profiles for one user.

## 52. Understand ModelForm instance

Passing instance=profile tells the ModelForm which model object it should update.

Without an instance, a valid ModelForm save normally creates a new model object.

With an instance, the form updates the existing profile.

## 53. Create the profile template

Create profiles/templates/profiles/edit_user_profile.html:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Profile</title>
</head>
<body>
    <main>
        <h1>Edit my profile</h1>

        <form method="post">
            {% csrf_token %}

            {{ form.non_field_errors }}

            {% for field in form %}
                <div>
                    {{ field.label_tag }}
                    {{ field }}
                    {{ field.errors }}
                </div>
            {% endfor %}

            <button type="submit">Save profile</button>
        </form>
    </main>
</body>
</html>
~~~

## 54. Add the profile URL

In profiles/urls.py:

~~~python
path(
    "account/profile/edit/",
    views.edit_user_profile,
    name="edit_user_profile",
),
~~~

Keep all earlier routes.

## 55. Add a profile link

In the account summary template:

~~~html
<a href="{% url 'edit_user_profile' %}">
    Edit my profile
</a>
~~~

The view is protected by login_required.

---

# PART 12 — PROFILE PRIVACY AND DATA VALIDATION

## 56. Never accept arbitrary user ownership

Unsafe idea:

~~~python
profile = UserProfile.objects.get(
    user_id=request.POST["user_id"]
)
~~~

A user could change the submitted ID.

Safer:
- Use request.user.
- Query only the current user's profile.
- Enforce authentication.
- Apply permission checks for staff workflows.

## 57. Validate profile data

ModelForm performs model and field validation.

Additional business validation can be implemented in:
- Form clean methods.
- Model clean methods.
- Field validators.

Do not assume blank=True means every value is valid.

## 58. Phone number validation

A phone number should usually be stored as text, not an integer.

Reasons:
- It may begin with zero.
- It may contain a country prefix.
- It may contain separators.
- It is an identifier/contact value, not a quantity for arithmetic.

For production, use an appropriate phone-number validation library or a carefully defined business rule.

## 59. Profile image considerations

If you add an image field:
- Configure MEDIA_ROOT and MEDIA_URL.
- Validate file type and size.
- Do not trust the filename extension alone.
- Store uploads outside executable source locations.
- Use safe storage permissions.
- Consider image processing and malware scanning for public uploads.

This lesson does not implement image upload. It is an extension topic.

---

# PART 13 — TESTS

## 60. Test custom user model in the fresh project

In custom_user_demo/accounts/tests.py:

~~~python
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class CustomUserModelTests(TestCase):
    def test_custom_fields_are_available(self):
        user = User.objects.create_user(
            username="custom_test_user",
            password="Custom-Test-Password-123!",
            employee_code="EMP-TEST-01",
            department="Engineering",
        )

        self.assertEqual(
            user.employee_code,
            "EMP-TEST-01",
        )
        self.assertEqual(
            user.department,
            "Engineering",
        )
        self.assertTrue(
            user.check_password("Custom-Test-Password-123!")
        )
~~~

Run inside custom_user_demo:

~~~powershell
python manage.py test accounts
~~~

## 61. Test profile ownership in the main project

In student_portal/profiles/tests.py, add tests after confirming UserProfile exists:

~~~python
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import UserProfile

User = get_user_model()


class UserProfileOwnershipTests(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(
            username="profile_user_a",
            password="Test-Only-Password-123!",
        )
        self.user_b = User.objects.create_user(
            username="profile_user_b",
            password="Test-Only-Password-123!",
        )

    def test_each_user_can_have_separate_profile(self):
        profile_a = UserProfile.objects.create(
            user=self.user_a,
            city="Hyderabad",
        )
        profile_b = UserProfile.objects.create(
            user=self.user_b,
            city="Vijayawada",
        )

        self.assertNotEqual(
            profile_a.pk,
            profile_b.pk,
        )
        self.assertEqual(
            profile_a.user,
            self.user_a,
        )
        self.assertEqual(
            profile_b.user,
            self.user_b,
        )
~~~

This test checks the model relationship. Add request-level tests for the edit view in the actual project.

## 62. Run checks in the correct project

For custom user model:

~~~powershell
cd path\to\custom_user_demo
python manage.py check
python manage.py test accounts
~~~

For profile model:

~~~powershell
cd path\to\student_portal
python manage.py check
python manage.py test profiles
~~~

Do not mix the two projects or their databases.

---

# PART 14 — COMMON ERRORS

## 63. AUTH_USER_MODEL refers to model that does not exist

Check:
- accounts is in INSTALLED_APPS.
- The model class is named User.
- The setting is exactly accounts.User.
- The setting is in the correct settings.py.

## 64. Changing user model after migrations

Do not attempt to solve this by changing AUTH_USER_MODEL in the existing student_portal.

Use the separate fresh custom_user_demo project.

If a real production migration is required, plan a dedicated schema/data migration with backups and tests.

## 65. CircularDependencyError

Custom user models can affect migration dependencies.

Keep the custom user model in the app's initial migration and follow Django's documented custom-user migration guidance.

Do not randomly reorder or delete migration files.

## 66. Admin does not show custom fields

Check:
- CustomUserAdmin extends UserAdmin.
- fieldsets include the custom fields.
- add_fieldsets includes fields required during creation.
- The model is registered only once.
- The admin server is running the correct project.

## 67. get_user_model returns the wrong model

Check:
- Which settings module is loaded?
- Which project directory contains manage.py?
- Is AUTH_USER_MODEL configured in that project's settings?
- Did you restart the development process after changing settings?

## 68. Duplicate profile error

The OneToOneField permits only one profile per user.

Use get_or_create() in the view or retrieve the existing profile before creating a new one.

Do not remove the uniqueness rule to hide a duplicate creation bug.

## 69. Profile belongs to the wrong user

Check:
- Does the view use request.user?
- Is the form exposing a user field?
- Is the view accepting user_id from POST?
- Does the query filter by the current user?

## 70. ImportError for UserProfile

Check:
- Is the class defined?
- Is the import path correct?
- Did you save the model file?
- Are you running the correct project?
- Does the class name match exactly?

---

# PART 15 — APPROVED MINI-PROJECT

## 71. Custom User Profile System

### Business problem

An institute portal needs account identity and profile information.

The project should demonstrate:
- A custom user model in a clean project created before migrations.
- A profile model that stores optional user details.
- Safe user-to-profile ownership.

### Project tracks

**Track A — Custom user model practice**
- Use custom_user_demo.
- Extend AbstractUser.
- Add employee_code and department.
- Configure AUTH_USER_MODEL before migrations.
- Create and test a custom user.

**Track B — Profile management in the existing pathway**
- Keep student_portal's existing user model.
- Add or reuse UserProfile.
- Connect profile to request.user.
- Let the user update only their own profile.
- Test ownership.

### Acceptance criteria

- [ ] The custom project is separate.
- [ ] AUTH_USER_MODEL is set before initial migrations.
- [ ] Custom model inherits AbstractUser.
- [ ] Custom fields appear in the admin.
- [ ] get_user_model() returns the custom model.
- [ ] Main student_portal user model is not changed.
- [ ] Profile is linked using OneToOneField.
- [ ] Profile form does not allow arbitrary user assignment.
- [ ] Profile view uses request.user.
- [ ] Each user sees or edits only their own profile.
- [ ] Tests pass in the correct project.

---

# PART 16 — SELF-ASSESSMENT

## 72. Short-answer questions

1. What is a custom user model?
2. What is AbstractUser?
3. What is AbstractBaseUser?
4. When should AUTH_USER_MODEL be configured?
5. Why is changing the user model after migrations difficult?
6. What does get_user_model() return?
7. What should be used for user relationships in model declarations?
8. What is the difference between a custom user model and a profile model?
9. What does OneToOneField mean?
10. Why is a separate fresh project used in this lesson?
11. Why should the profile form not expose the user field?
12. Why should the view use request.user?
13. Why might phone number be stored as text?
14. What is the purpose of UserAdmin?
15. What should you do if the project already has migrations?

## 73. Self-check answers

1. A project-defined model representing authenticated accounts.
2. A Django abstract model containing common user fields and behavior.
3. A more minimal base for highly customized user models.
4. Before the first migrations that create user-related tables.
5. Existing tables, foreign keys and migration dependencies may refer to the previous model.
6. The user model configured for the active project.
7. settings.AUTH_USER_MODEL.
8. Custom user model changes account identity; profile stores additional details separately.
9. Each related record is connected one-to-one.
10. It avoids changing the already-migrated pathway database.
11. The browser should not choose which user's profile it edits.
12. It identifies the authenticated user associated with the request.
13. Phone numbers are identifiers and may contain leading zeros or symbols.
14. It configures user account management in Django admin.
15. Keep the existing model unless a planned migration is required; use a separate project for practice.

## 74. MCQ assessment

### Question 1
When should AUTH_USER_MODEL normally be configured?

- A. After production deployment
- B. Before initial migrations
- C. After every login
- D. Inside a template

**Answer: B.** The user model should be selected before migrations create dependent tables.

### Question 2
Which base class retains most standard Django user behavior?

- A. AbstractUser
- B. HttpResponse
- C. ModelAdmin
- D. AnonymousUser

**Answer: A.** AbstractUser is suitable for adding fields to the standard user model.

### Question 3
Which API returns the configured user model?

- A. get_user_model()
- B. get_current_user_table()
- C. get_profile_model()
- D. get_admin_user()

**Answer: A.** It returns the active user model class.

### Question 4
What is a profile model usually used for?

- A. Replacing all authentication
- B. Storing additional user information
- C. Storing session cookies
- D. Storing URL routes

**Answer: B.** A profile can store optional details separately from account identity.

### Question 5
Why should the existing migrated project not be switched casually to a custom user model?

- A. Django cannot use models
- B. Existing migrations and relationships depend on the configured model
- C. Templates will be deleted
- D. Python will stop working

**Answer: B.** Changing the user model later can require complex schema and data migrations.

---

# PART 17 — INTERVIEW PREPARATION

## 75. What is a custom user model?

**Answer:** A custom user model is a project-defined model used by Django authentication. It is useful when the application needs account fields or identity behavior that differ from the default user model.

**Follow-up:** Which base class is suitable for many projects that only need additional fields?

**Answer:** AbstractUser.

## 76. What is the difference between AbstractUser and AbstractBaseUser?

**Answer:** AbstractUser includes common user fields and behavior. AbstractBaseUser provides a more minimal foundation and requires more custom implementation.

**Follow-up:** Which one is more beginner-friendly for adding a field?

**Answer:** AbstractUser.

## 77. Why configure AUTH_USER_MODEL early?

**Answer:** Django's authentication and application models create relationships to the user model. Selecting the model before initial migrations keeps the migration graph and database schema consistent.

**Follow-up:** Can you change it easily after the application has many migrations?

**Answer:** No. It may require complex schema and data migration work.

## 78. What is the difference between a custom user and a profile model?

**Answer:** A custom user model changes the account model used for authentication. A profile model stores additional information linked to the user, often through a OneToOneField.

**Follow-up:** Can a project use the default user model and a profile model?

**Answer:** Yes.

## 79. Scenario: a developer wants to add a phone number to an existing migrated project

**Answer:** If the phone number is optional profile information, a separate profile model or an existing profile model may be appropriate. Do not change AUTH_USER_MODEL merely to add a phone field.

## 80. Scenario: one student can edit another student's profile

**Answer:** The view is not enforcing ownership. It should retrieve the profile using request.user and should not trust a user ID submitted by the browser.

---

# PART 18 — INDEPENDENT COMPLETION

## 81. Explain the two project tracks

Draw:
- Fresh custom_user_demo project.
- AUTH_USER_MODEL before migrations.
- AbstractUser extension.
- Custom user admin.
- Main student_portal with its existing user model.
- Separate UserProfile.
- OneToOneField to settings.AUTH_USER_MODEL.
- Ownership through request.user.

## 82. Controlled debugging

In the fresh practice project:
- Temporarily misspell AUTH_USER_MODEL and observe the check failure.
- Restore the correct setting.
- Remove the accounts app from INSTALLED_APPS in a local copy and observe the error.
- Restore it.
- Inspect get_user_model().

In the main project:
- Try to create a duplicate profile and observe the OneToOne constraint.
- Fix the view using get_or_create().
- Verify one user cannot select another user's profile through submitted data.

Do not change the main project's AUTH_USER_MODEL during this exercise.

## 83. Final checklist

- [ ] I understand why custom user models exist.
- [ ] I understand AbstractUser and AbstractBaseUser.
- [ ] I know when AUTH_USER_MODEL must be set.
- [ ] I created a separate custom user practice project.
- [ ] I ran initial migrations after configuring the model.
- [ ] I registered the model in admin.
- [ ] I used get_user_model().
- [ ] I used settings.AUTH_USER_MODEL for relationships.
- [ ] I understand profile models.
- [ ] I kept the main student_portal user model unchanged.
- [ ] I implemented profile ownership safely.
- [ ] I completed Custom User Profile System.
- [ ] I ran tests in the correct projects.

**Next lesson:** Day 52 — Django Messages Framework and Application Feedback.

---

## 84. Official references

1. Django custom user models: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/
2. Django user model API: https://docs.djangoproject.com/en/5.2/ref/contrib/auth/
3. Django model relationships: https://docs.djangoproject.com/en/5.2/topics/db/models/
4. Django migrations: https://docs.djangoproject.com/en/5.2/topics/migrations/
5. Django admin: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/

**Version reminder:** This lesson targets Django 5.2.19. The custom user model is demonstrated only in the separate fresh project. Do not change AUTH_USER_MODEL in the already-migrated student_portal as part of this lesson.
