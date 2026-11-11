
# Day 46: Django Authentication System and User Model

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 3–4 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–45 — Django project structure, views, templates, models, migrations, ORM, forms, CRUD and data integrity  
**Environment:** Windows 10/11, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal project, config project package, profiles application  
**Approved mini-project:** User Account Management

> **Self-learning promise:** This lesson starts with the meaning of authentication and the purpose of a user account. You will inspect Django's existing user model, safely create test accounts, read user information, and display a protected account summary. Follow the steps in order. Use fictional practice data only.

---

# PART 1 — UNDERSTAND THE PROBLEM BEFORE DJANGO CODE

## 1. What problem are we solving?

Imagine an institute has a Student Portal.

A student opens the portal and wants to:
- Create an account.
- Sign in with a username and password.
- View their own profile.
- Change account information.
- Sign out when finished.

The application must answer important questions:
- Who is making this request?
- Has this person proved control of the account?
- Is the person currently signed in?
- Which account information belongs to this person?
- Should an anonymous visitor be allowed to open this page?
- How should the application store passwords safely?

Django provides an authentication system to help answer these questions.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain authentication in simple language.
2. Distinguish authentication from authorization.
3. Explain what a user account represents.
4. Identify Django's built-in user model.
5. Explain common user fields and status flags.
6. Explain the purpose of authentication-related database tables.
7. Use get_user_model() in Python code.
8. Use settings.AUTH_USER_MODEL in model relationship declarations.
9. Explain why application code should not hard-code the default User class.
10. Explain the difference between a raw password and a password hash.
11. Create a safe local test user.
12. Read user information without exposing credentials.
13. Use request.user to identify the current request's user.
14. Distinguish an authenticated user from an anonymous user.
15. Protect a page with login_required.
16. Run checks and verify account behavior.
17. Diagnose common user-model and authentication mistakes.
18. Complete the User Account Management mini-project.

## 3. Important words — beginner definitions

| Word | Simple meaning | Example |
|---|---|---|
| User | A person or account that interacts with an application | A student account |
| Account | Stored information used to represent a user | Username and email |
| Authentication | Checking whether a person is signed in as a claimed account | Checking login credentials |
| Authorization | Checking whether that signed-in user may perform an action | Only staff can edit all students |
| Credential | Information used to prove identity | Username and password |
| Password hash | A one-way encoded representation used for password verification | Django's stored password value |
| Anonymous | A request that is not associated with a signed-in user | A visitor who has not logged in |
| Authenticated | A request associated with a successfully signed-in user | A logged-in student |
| Session | Server-managed state associated with a browser session | Remembering the signed-in user |
| Permission | A rule allowing or denying an operation | Permission to delete an employee |
| User model | The Django model representing user accounts | The configured User model |
| ORM | Django's Python interface for database operations | User.objects.filter() |

Do not try to memorize every word immediately. Use the table while reading the examples.

## 4. Authentication versus authorization

These two terms are related, but they are not the same.

### Authentication asks: who are you?

Example:
- A student enters a username and password.
- Django checks the submitted credentials.
- If the credentials are valid, Django can sign the user in.
- The request is now associated with that user.

### Authorization asks: what are you allowed to do?

Example:
- A student is signed in.
- The student can view their own profile.
- The student cannot automatically edit every student's profile.
- A staff member may have additional permissions.

| Authentication | Authorization |
|---|---|
| Verifies identity | Checks access rights |
| Usually happens during login | Happens when a protected action is requested |
| Example: valid credentials | Example: permission to delete |
| Answers "Who are you?" | Answers "What may you do?" |

A successful login does not automatically give a user permission to perform every action.

## 5. Where authentication fits in a web request

~~~text
Browser
   |
   | Request to a protected page
   v
Django URL dispatcher
   |
   v
Authentication middleware
   |
   v
request.user is available
   |
   v
login_required / permission check
   |
   +---- Not signed in ----> Redirect to login page
   |
   +---- Signed in --------> Run the view
                                  |
                                  v
                              HTTP response
~~~

This is a simplified view of the flow. Middleware and session configuration help Django associate a browser request with a user.

## 6. What Django provides

Django includes a reusable authentication system. It provides:
- A configured user model.
- Password hashing and password verification.
- Login and logout functions.
- Authentication forms.
- Session integration.
- Permission and group support.
- View decorators for common access checks.
- Management commands for creating administrative users.

You do not need to write your own password hashing algorithm. Use Django's authentication APIs.

---

# PART 2 — INSPECT THE EXISTING PROJECT

## 7. Open the correct project

The project from previous Django lessons is called student_portal.

Its important structure is:

~~~text
student_portal/
├── .venv/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
~~~

Do not create another project if you already have the working project from Days 27–45.

## 8. Open the terminal in VS Code

1. Open VS Code.
2. Select File → Open Folder.
3. Open the existing student_portal folder.
4. Select Terminal → New Terminal.
5. Confirm the current folder contains manage.py.

Run:

~~~powershell
Get-Location
Get-ChildItem
~~~

Expected observation:
- The current path should end in student_portal.
- The folder listing should include manage.py.
- You should see the config and profiles folders.

If manage.py is not present, stop. You are probably in the wrong directory.

## 9. Activate the existing virtual environment

Run this in PowerShell:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

The terminal prompt normally displays (.venv).

Now check the interpreter:

~~~powershell
python --version
python -c "import sys; print(sys.executable)"
python -m django --version
~~~

Why do these commands matter?
- python --version shows the Python version.
- sys.executable shows the exact Python executable.
- python -m django --version confirms the Django version available to that interpreter.

Do not install another Django version just because a command fails. First check whether the correct environment is active.

## 10. Confirm the Django configuration

Open config/settings.py.

Find INSTALLED_APPS.

A standard Django project contains the authentication apps:

~~~python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
]
~~~

Understand the relevant entries:

- django.contrib.auth provides authentication models, forms, permissions and related APIs.
- django.contrib.contenttypes supports Django's content-type framework, which is used by permissions and other features.
- django.contrib.sessions provides session support.
- django.contrib.admin provides the administration site.
- profiles.apps.ProfilesConfig registers the application's own configuration.

Do not remove standard Django apps to make this example shorter.

## 11. Confirm middleware

In the same file, find MIDDLEWARE.

A standard Django project includes middleware similar to:

~~~python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
~~~

The important item for today's lesson is:

~~~python
"django.contrib.auth.middleware.AuthenticationMiddleware",
~~~

This middleware makes the current user available as request.user after Django processes the session information.

The session middleware must appear before the authentication middleware. Keep the standard generated ordering unless you understand the consequences of changing it.

## 12. Confirm the database migrations

Django's default user model and authentication tables are created through migrations.

Run:

~~~powershell
python manage.py showmigrations
~~~

You should see app names such as:
- admin
- auth
- contenttypes
- sessions
- profiles

A checked migration is displayed with an [X] marker.

If the standard migrations are not applied, run:

~~~powershell
python manage.py migrate
~~~

What does migrate do?
1. Django reads migration files.
2. Django checks which migrations have already been applied.
3. Django applies pending database schema operations.
4. Django records applied migrations.
5. The database receives the tables required by the installed apps.

Do not delete migration files or the database to solve an ordinary migration problem.

---

# PART 3 — UNDERSTAND THE DJANGO USER MODEL

## 13. What is a user model?

A model is a Python class that describes data stored in a database.

Django's configured user model describes user accounts.

The default Django user model is commonly imported through Django's authentication APIs. It provides fields and methods for account identity and password management.

The user model is not the same as a browser login page:
- The model represents stored account data.
- A form collects and validates submitted values.
- A view coordinates the request.
- A template displays the page.
- Authentication functions verify credentials and establish login state.

## 14. Common fields in Django's default user model

| Field | Purpose | Example |
|---|---|---|
| username | Account's username | student101 |
| first_name | Given name | Asha |
| last_name | Family name | Rao |
| email | Email address | asha@example.test |
| password | Encoded password representation | A Django password hash |
| is_active | Whether the account is active | True |
| is_staff | Whether the user can access the admin site, subject to permissions | False |
| is_superuser | Whether the user has all permissions | False |
| date_joined | Account creation timestamp | Date and time |
| last_login | Most recent login timestamp | Date and time |

The default user model has additional behavior and fields. This table introduces the fields most beginners encounter.

## 15. Understand status flags

### is_active

This flag indicates whether the account is active.

Typical use:
- Active account: the user can normally authenticate.
- Inactive account: the user is not allowed to authenticate through Django's standard authentication behavior.

Do not confuse inactive with deleted. The account record may still exist.

### is_staff

This flag indicates whether a user is marked as staff for Django admin access.

Important:
- is_staff=True does not mean the user is a superuser.
- Admin access also depends on authentication and applicable permissions.
- Do not make every registered student a staff user.

### is_superuser

This flag indicates that the user has all permissions without assigning each permission individually.

Important:
- Superuser accounts are powerful.
- Use them only for trusted administrators.
- Never create every user as a superuser.
- Do not use a superuser account for ordinary student testing.

## 16. How the fields relate to a real portal

Imagine three local test accounts:

| Account | is_active | is_staff | is_superuser | Purpose |
|---|---:|---:|---:|---|
| student_demo | True | False | False | Ordinary student |
| staff_demo | True | True | False | Staff demonstration |
| admin_demo | True | True | True | Local administrator |

These are example account types, not real credentials.

The account's flags affect different parts of the application. A later lesson will explain permissions and role-based access in more detail.

## 17. What is stored in the password field?

A password must not be stored as readable plain text.

A plain-text password would look like a normal word or phrase. If a database leak exposed plain-text passwords, attackers could immediately read them.

Django stores a password hash generated by a configured password hasher.

A hash:
- Is produced by a password hashing algorithm.
- Is stored instead of the original password.
- Is used by Django to verify a password candidate.
- Is not intended to be reversed to reveal the original password.

Do not write your own password storage code.

## 18. Why password values look unfamiliar

When you inspect a test user's password field, you will see a long encoded value rather than the original password.

This is expected.

Never:
- Print a real password in logs.
- Put a password into a template.
- Return a password field in an API response.
- Commit test credentials to a public repository.
- Ask a learner to send their real password in a screenshot.

The application should use Django's password APIs instead.

---

# PART 4 — USE THE CONFIGURED USER MODEL CORRECTLY

## 19. Why hard-coded user imports can become a problem

A Django project may use the default user model or a custom user model.

If application code directly assumes the built-in class forever, it can become difficult to adapt when the configured user model changes.

Django provides APIs to refer to the configured user model.

There are two important forms:
- get_user_model() for Python code that needs the model class at runtime.
- settings.AUTH_USER_MODEL for model relationship declarations.

## 20. Use get_user_model()

Example:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()
~~~

Explanation:
- from django.contrib.auth import get_user_model imports Django's helper function.
- get_user_model() returns the user model configured for the current project.
- User is a Python variable referring to that model class.

The variable name User is conventional. You could use another clear name, but keep the code readable.

## 21. Query users using the configured model

Open the Django shell:

~~~powershell
python manage.py shell
~~~

Type:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.count()
~~~

Explanation:
- User.objects is the model's manager.
- count() asks the database for the number of matching user records.
- The result is an integer.

Example result:

~~~text
3
~~~

Your result may be different because it depends on the accounts in your local database.

Exit the shell:

~~~python
exit()
~~~

## 22. Filter users

Start the shell again:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

active_users = User.objects.filter(is_active=True)
active_users.count()
~~~

Understand the expression:
- filter() builds a database query.
- is_active=True is a condition.
- The returned value is a QuerySet.
- count() evaluates a count query.

A QuerySet is Django's object representing a database query and its results.

## 23. Retrieve one user safely

Use get() when you expect exactly one matching record.

~~~python
user = User.objects.get(username="student_demo")
user.username
user.email
~~~

Possible problems:
- No matching account: Django raises User.DoesNotExist.
- More than one matching row: Django raises User.MultipleObjectsReturned.
- Exactly one matching account: Django returns the model instance.

The default username field is unique, so a matching username should identify one record.

## 24. Prefer get_object_or_404 in a web view

In a view, use Django's shortcut when a missing record should produce a 404 response.

~~~python
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

def example_view(request):
    user = get_object_or_404(User, username="student_demo")
~~~

This is only an illustration of the lookup. Do not expose arbitrary users' private account data. Authorization and ownership checks are required for user-specific pages.

## 25. Use settings.AUTH_USER_MODEL in model relationships

When a model has a relationship to the configured user model, use the setting as the relationship target.

Example:

~~~python
from django.conf import settings
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    phone_number = models.CharField(max_length=20, blank=True)
~~~

Explanation:
- settings.AUTH_USER_MODEL points to the configured user model.
- OneToOneField means one profile is connected to one user.
- on_delete=models.CASCADE means deleting the user deletes the related profile.
- related_name defines the reverse relationship name.
- blank=True allows the field to be empty in form validation.

Do not add this model to the existing project without checking whether the project already has a profile model. The example explains the pattern; Day 51 develops the profile design.

---

# PART 5 — CREATE A SAFE LOCAL TEST ACCOUNT

## 26. Why we need a test account

A test account lets you practice user queries and authentication behavior without using a real student's personal details.

Use fictional values such as:
- username: student_demo
- first name: Demo
- last name: Student
- email: student@example.test

The .test domain is intended for testing examples.

Do not use an actual learner's email or password in this lesson.

## 27. Create a superuser only when needed

Django provides a management command:

~~~powershell
python manage.py createsuperuser
~~~

The command asks for values such as:
- Username.
- Email address, depending on configuration.
- Password.
- Password confirmation.

Use a local-only practice password. Do not use a password that you use for email, banking or any real service.

A superuser is not the same as an ordinary student. Use the command only when you need a local admin account.

## 28. Create an ordinary user through the shell

Open the shell:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.create_user(
    username="student_demo",
    email="student@example.test",
    password="Local-Only-Demo-Password-123!",
    first_name="Demo",
    last_name="Student",
)

print(user.username)
print(user.is_active)
print(user.is_staff)
print(user.is_superuser)
~~~

Expected observations for a newly created ordinary user:
- The username is student_demo.
- The account is active by default.
- The account is not staff by default.
- The account is not a superuser by default.

If the username already exists, use a different fictional username or inspect the existing test record.

## 29. Why create_user is important

Use create_user() to create an ordinary user account.

It handles password setting through Django's user model manager.

Do not do this:

~~~python
user = User(
    username="unsafe_demo",
    password="Local-Only-Demo-Password-123!",
)
user.save()
~~~

This example assigns the raw password string to the model field. It does not use the normal password hashing workflow.

Use:

~~~python
user = User.objects.create_user(
    username="safe_demo",
    password="Local-Only-Demo-Password-123!",
)
~~~

The password manager method prepares the password using Django's configured hashing system.

## 30. Verify the password without printing it

Django provides check_password().

~~~python
user.check_password("Local-Only-Demo-Password-123!")
~~~

Expected result for the matching practice password:

~~~text
True
~~~

Try a different candidate:

~~~python
user.check_password("Wrong-Demo-Password")
~~~

Expected result:

~~~text
False
~~~

The method returns a Boolean:
- True: the candidate matches the stored password hash.
- False: the candidate does not match.

Do not print or return the stored password field to check it.

## 31. Update safe account fields

A user can update non-password fields through model attributes.

~~~python
user.first_name = "Demo Updated"
user.last_name = "Learner"
user.email = "updated@example.test"
user.save(update_fields=["first_name", "last_name", "email"])
~~~

Explanation:
- The first three statements change values in memory.
- save() writes changes to the database.
- update_fields limits the fields included in the save operation.
- The password is not changed by this code.

Always validate user-submitted data through a form before saving it in a real application.

## 32. Deactivate a test account

For local practice:

~~~python
user.is_active = False
user.save(update_fields=["is_active"])
~~~

This changes the account status.

To reactivate the test account:

~~~python
user.is_active = True
user.save(update_fields=["is_active"])
~~~

Do not deactivate an account as a substitute for a proper account-deletion policy.

---

# PART 6 — UNDERSTAND request.user

## 33. What is request?

In a Django view, the first parameter commonly named request represents the incoming HTTP request.

The request contains information such as:
- HTTP method.
- Path.
- Query parameters.
- Submitted form data.
- Headers.
- Current user.
- Session data.

The exact available attributes depend on Django and the request processing configuration.

## 34. What is request.user?

When Django's authentication middleware is configured, a view can access the user associated with the request through:

~~~python
request.user
~~~

If the visitor has not signed in, the value is an anonymous user object.

If the visitor has signed in successfully, the value represents the authenticated user.

## 35. Check whether a user is authenticated

Use:

~~~python
request.user.is_authenticated
~~~

This is a Boolean property.

Do not call it as a function:
- Correct: request.user.is_authenticated
- Incorrect: request.user.is_authenticated()

For a signed-in request, it evaluates to True.

For an anonymous request, it evaluates to False.

## 36. Check the current user's username

~~~python
request.user.username
~~~

Only display user information that the current page needs.

Do not assume every user has the same profile fields if the project later changes to a custom user model.

## 37. AnonymousUser

Django uses an anonymous user representation when a request is not authenticated.

It allows views and templates to check login status without requiring the developer to manually handle a missing user object.

For example:

~~~python
if request.user.is_authenticated:
    message = "Welcome back"
else:
    message = "Please sign in"
~~~

This code selects a message. It does not sign anyone in or grant a permission.

---

# PART 7 — BUILD A USER ACCOUNT SUMMARY PAGE

## 38. Today's guided feature

Create a page that displays a small account summary for the currently signed-in user.

The page should:
- Require the user to be signed in.
- Display the username.
- Display the email address.
- Display the first and last name.
- Display whether the account is active.
- Never display the password field.
- Never display another user's private account information.

This page is a learning example, not a complete profile-editing system.

## 39. Files used today

You will inspect or update:
- profiles/views.py
- profiles/urls.py
- config/urls.py
- config/settings.py
- profiles/templates/profiles/account_summary.html

Create the templates folders if they do not exist.

## 40. Add the view

Open profiles/views.py.

Add the following code without deleting unrelated views from previous lessons:

~~~python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def account_summary(request):
    user = request.user

    context = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_active": user.is_active,
    }

    return render(
        request,
        "profiles/account_summary.html",
        context,
    )
~~~

## 41. Explain the imports

### login_required

~~~python
from django.contrib.auth.decorators import login_required
~~~

This imports a decorator that protects a view from anonymous access.

A decorator is a Python feature that wraps another function to add behavior.

### render

~~~python
from django.shortcuts import render
~~~

The render() shortcut combines a template with a context dictionary and returns an HTTP response.

## 42. Explain the decorator

~~~python
@login_required
~~~

This line is placed immediately above the view function.

When an anonymous visitor requests the page, Django redirects the visitor to the configured login URL.

When an authenticated user requests the page, Django continues to the view.

This is an authentication check. It does not automatically check whether the user owns a separate record or has a specific permission.

## 43. Explain the view function

~~~python
def account_summary(request):
~~~

- def defines a Python function.
- account_summary is the function name.
- request receives the current Django request.
- The function returns an HTTP response.

## 44. Explain the context dictionary

~~~python
context = {
    "username": user.username,
    "first_name": user.first_name,
    "last_name": user.last_name,
    "email": user.email,
    "is_active": user.is_active,
}
~~~

A context dictionary passes values from a view to a template.

The key on the left is the name used by the template.

The value on the right comes from the current user's model instance.

We deliberately do not include:
- password
- password hash
- session key
- reset token
- private authentication internals

## 45. Create the template folder

In the profiles app, create:

~~~text
profiles/
└── templates/
    └── profiles/
        └── account_summary.html
~~~

The nested profiles directory helps avoid template-name collisions between applications.

## 46. Create account_summary.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Account</title>
</head>
<body>
    <main>
        <h1>My Account</h1>

        <p>
            <strong>Username:</strong>
            {{ username }}
        </p>

        <p>
            <strong>First name:</strong>
            {{ first_name|default:"Not provided" }}
        </p>

        <p>
            <strong>Last name:</strong>
            {{ last_name|default:"Not provided" }}
        </p>

        <p>
            <strong>Email:</strong>
            {{ email|default:"Not provided" }}
        </p>

        <p>
            <strong>Account active:</strong>
            {{ is_active }}
        </p>
    </main>
</body>
</html>
~~~

## 47. Understand the template syntax

| Syntax | Meaning |
|---|---|
| {{ username }} | Display the username value |
| {{ email }} | Display the email value |
| default:"Not provided" | Show fallback text when the value is empty |
| strong | HTML element for strong importance |
| main | Main content area of the page |

Django template variables are not Python expressions. Use the supported template syntax.

## 48. Add an app URL

Open profiles/urls.py.

Keep existing URL patterns. Add the route if it is not already present:

~~~python
from django.urls import path
from . import views

urlpatterns = [
    # Keep the routes from earlier lessons.
    path(
        "account/",
        views.account_summary,
        name="account_summary",
    ),
]
~~~

If the file already imports path and views, do not duplicate those imports.

## 49. Confirm the project URL includes the app

Open config/urls.py.

A standard setup includes the app URL configuration:

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
~~~

Do not replace other project routes without checking them first.

## 50. Configure the login URL

Open config/settings.py.

Add or confirm:

~~~python
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "account_summary"
LOGOUT_REDIRECT_URL = "login"
~~~

Important:
- These settings refer to named URL patterns.
- The login route will be added in Day 47.
- If the login route does not exist yet, the redirect target cannot be resolved.
- Do not assume the account summary can be fully tested before the login route is configured.

For a temporary test, you may use Django admin login, but the final learner journey should use the application login flow taught in Day 47.

## 51. Why the login URL matters

When an anonymous visitor opens a protected page:
1. Django sees that the user is anonymous.
2. login_required redirects the visitor.
3. The redirect target comes from LOGIN_URL.
4. After login, the application can redirect to the original requested page or the configured success URL, depending on the login workflow.

A missing or misspelled URL name can cause a reverse-resolution error.

---

# PART 8 — TEST AND VERIFY THE FEATURE

## 52. Run Django's system check

In the project root, run:

~~~powershell
python manage.py check
~~~

Expected result when no configuration issue is detected:

~~~text
System check identified no issues (0 silenced).
~~~

This check does not prove that the login journey works. Browser and test checks are still required.

## 53. Start the development server

~~~powershell
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/account/
~~~

If the account summary route is protected and you are not signed in, the browser should redirect to the configured login route.

The final login route is completed in Day 47.

## 54. Test with a signed-in user

After the login route is implemented:
1. Open the login page.
2. Sign in with your local demo account.
3. Open the account summary page.
4. Check the displayed username.
5. Check the email and name fields.
6. Confirm that no password or password hash is displayed.
7. Sign out.
8. Try opening the account page again.

Expected behavior:
- Signed-in user: sees their own summary.
- Signed-out visitor: is redirected to login.
- No password data appears in the page.

## 55. Test a second account

Create a second fictional local user.

Sign in as the second user and open the same URL.

The page should display the second user's information, not the first user's information.

This proves that the view reads from request.user, rather than using a hard-coded username.

## 56. What if the page displays another user's information?

Inspect the view.

Incorrect pattern:

~~~python
user = User.objects.get(username="student_demo")
~~~

This always looks up the same named account.

Correct pattern for the current signed-in account:

~~~python
user = request.user
~~~

The current user comes from the authenticated request.

For other record types, ownership checks are still needed. Do not assume that knowing a URL or primary key grants access.

---

# PART 9 — COMMON ERRORS AND PRECISE FIXES

## 57. Error: NoReverseMatch for login

**Possible reason:** LOGIN_URL points to a URL name that has not been created or is misspelled.

Check:
1. Does profiles/urls.py define a login route?
2. Does it use the name login?
3. Does config/urls.py include the app URL configuration?
4. Is LOGIN_URL spelled exactly the same?

Day 47 adds the actual login route.

## 58. Error: request.user is not available

Check:
1. Is django.contrib.auth in INSTALLED_APPS?
2. Is AuthenticationMiddleware in MIDDLEWARE?
3. Is SessionMiddleware enabled before authentication middleware?
4. Did you accidentally rename the view parameter or use another variable?
5. Run python manage.py check.

Do not create your own request.user attribute manually.

## 59. Error: User.DoesNotExist

The query did not find a matching account.

Check:
- Is the username correct?
- Does the test account exist?
- Did you use the same database?
- Did the shell use the same project settings?

Inspect available usernames:

~~~python
User.objects.values_list("username", flat=True)
~~~

This returns usernames only. Do not print password fields.

## 60. Error: IntegrityError for duplicate username

The username already exists and the default user model requires unique usernames.

Choose another fictional username or reuse the existing account.

Do not disable uniqueness just to make a practice command succeed.

## 61. Error: No such table

The database may not have the required migrations applied.

Run:

~~~powershell
python manage.py showmigrations
python manage.py migrate
~~~

If the error continues, verify the active settings module and database configuration before changing files.

## 62. Error: TemplateDoesNotExist

Check:
- The exact template filename.
- The nested folder name.
- The app is registered.
- APP_DIRS is enabled in the standard template configuration.
- The view uses the same template path.

The expected path is:

~~~text
profiles/templates/profiles/account_summary.html
~~~

## 63. Error: AttributeError on is_authenticated

Correct:

~~~python
request.user.is_authenticated
~~~

Incorrect:

~~~python
request.user.is_authenticated()
~~~

It is a property, not a method.

## 64. Error: Password check returns False

Check:
- Was the account created with create_user()?
- Are you testing the same user?
- Did you type the same practice password?
- Did you accidentally change the password after creating the user?

Never try to decode the stored password value.

---

# PART 10 — TESTING WITH DJANGO TEST CASES

## 65. Why automated tests matter

A manual browser test is useful, but it is easy to forget a step.

An automated test can repeat the same checks whenever code changes.

Django's test framework provides:
- Test cases.
- A test database.
- A test client for simulating requests.
- Assertions for expected results.

## 66. Add a focused view test

Open profiles/tests.py.

Add a test for the account summary page. If the file already has tests, keep them and add this class.

~~~python
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AccountSummaryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="account_test_user",
            email="account@example.test",
            password="Test-Only-Password-123!",
            first_name="Test",
            last_name="Learner",
        )

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(
            reverse("account_summary")
        )

        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_sees_own_summary(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("account_summary")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "account_test_user")
        self.assertContains(response, "account@example.test")

    def test_password_is_not_displayed(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("account_summary")
        )

        self.assertNotContains(response, self.user.password)
~~~

**Important integration note:** This example assumes the view and URL from this lesson are present. If your tests.py already contains imports and test classes, merge the new test class into the existing file rather than replacing all previous tests.

## 67. Understand setUp()

setUp() runs before each test method.

It creates a test user for the test.

Django creates and manages a separate test database for the test run. Test data should not be confused with the records in your normal development database.

## 68. Understand the test client

self.client simulates a browser request.

Example:

~~~python
response = self.client.get(
    reverse("account_summary")
)
~~~

This sends a GET request to the URL identified by the route name.

## 69. Understand force_login()

force_login() marks the test client as logged in without checking a password.

It is useful when the test is about a protected page rather than the credential-validation flow.

Day 47 will test the actual login process.

## 70. Run the tests

~~~powershell
python manage.py test profiles
~~~

Read the full output.

A passing test run ends with a summary such as:

~~~text
Ran 3 tests
OK
~~~

The exact timing and test database messages will differ.

If the tests fail, read the first failing test name and assertion message. Do not immediately rewrite the entire view.

---

# PART 11 — GUIDED PRACTICE

## 71. Practice A — identify the current user

Question:
- Which object gives the current request's user?
- Which property checks login status?
- Which field gives the username?

Expected answers:
- request.user
- request.user.is_authenticated
- request.user.username

## 72. Practice B — inspect account status

In the Django shell, retrieve your fictional demo user.

Check:
- username
- email
- is_active
- is_staff
- is_superuser

Explain what each value means.

Do not print the password field.

## 73. Practice C — distinguish staff and superuser

Create or inspect one ordinary test account and one staff test account.

Answer:
1. Does staff automatically mean superuser?
2. Does superuser automatically mean staff access is relevant?
3. Should every registered student be staff?
4. Why should administrator accounts be protected?

Use the definitions from this lesson.

## 74. Practice D — modify the account summary

Add one safe display field to the context, such as date_joined.

Use Django's template formatting features to display it.

Do not expose private authentication data.

## 75. Practice E — test the anonymous route

1. Sign out.
2. Open /account/.
3. Observe the redirect.
4. Record the final URL.
5. Explain which setting controls the login destination.

Do not mark the test complete until the login route exists.

---

# PART 12 — APPROVED MINI-PROJECT

## 76. Project: User Account Management

### Business problem

A training institute needs a simple account summary page for signed-in users.

A student should be able to view their own account information. An anonymous visitor should not be able to open the protected page.

### Functional requirements

1. Use the existing student_portal project.
2. Use Django's configured user model.
3. Create a fictional local test account.
4. Use request.user to identify the current account.
5. Protect the account summary view with login_required.
6. Display username, first name, last name, email and active status.
7. Never display the password or password hash.
8. Verify anonymous redirection.
9. Verify two different signed-in users see their own details.
10. Add automated tests for the protected page.

### Files involved

| File | Responsibility |
|---|---|
| config/settings.py | Authentication app, middleware and login URL settings |
| profiles/views.py | Account summary view |
| profiles/urls.py | Account summary route |
| profiles/templates/profiles/account_summary.html | Account summary page |
| profiles/tests.py | Automated access and output tests |

### Build order

1. Inspect the current project.
2. Confirm the virtual environment.
3. Confirm authentication apps and middleware.
4. Confirm migrations.
5. Create a fictional user.
6. Add the account summary view.
7. Add the template.
8. Add the URL.
9. Add login URL settings.
10. Run system checks.
11. Run automated tests.
12. Test the browser behavior after Day 47 login is available.
13. Record evidence.
14. Explain the flow in your own words.

### Acceptance criteria

- [ ] The existing project is used.
- [ ] The configured user model is accessed through get_user_model() where needed.
- [ ] The view uses request.user.
- [ ] Anonymous visitors are redirected.
- [ ] Signed-in users see their own account summary.
- [ ] No password or password hash is displayed.
- [ ] A second test account sees its own values.
- [ ] Automated tests pass.
- [ ] The learner can explain authentication versus authorization.

### Submission evidence

Submit:
- Updated source files.
- Screenshot of the account summary using fictional test data.
- Terminal output from python manage.py check.
- Terminal output from python manage.py test profiles.
- A short README explaining how to reproduce the feature.
- A short note describing one error and how it was fixed.

---

# PART 13 — SELF-ASSESSMENT

## 77. Short-answer questions

1. What problem does authentication solve?
2. How is authorization different?
3. What does the Django user model represent?
4. What is the purpose of get_user_model()?
5. When should settings.AUTH_USER_MODEL be used?
6. What does request.user represent?
7. What is an anonymous user?
8. What does is_authenticated return?
9. What does is_active represent?
10. What is the difference between is_staff and is_superuser?
11. Why should a password not be stored as plain text?
12. Why should a view use login_required?
13. Does login automatically authorize a user to edit every record?
14. Why is create_user() safer than assigning a raw password to the model field?
15. What is the purpose of a Django test client?

## 78. Answers for self-checking

1. Authentication verifies the identity of the account making a request.
2. Authorization checks what the authenticated user may do.
3. It represents the account data and behavior used by Django authentication.
4. It returns the user model configured for the current project.
5. Use it as the target for relationships to the configured user model.
6. It represents the user associated with the current request.
7. It represents a visitor who is not signed in.
8. It returns a Boolean indicating whether the user is authenticated.
9. It indicates whether the account is active.
10. Staff status relates to admin-site access; superuser status grants all permissions.
11. Plain-text passwords are readable if exposed; Django uses password hashing.
12. It redirects anonymous visitors away from a protected view.
13. No. Authorization must be checked separately.
14. It uses the user manager's password-setting workflow.
15. It simulates requests so view behavior can be tested automatically.

## 79. Daily MCQ assessment

### Question 1

What does authentication answer?

- A. Which database is installed?
- B. Who is making the request?
- C. Which CSS file is loaded?
- D. Which URL is shortest?

**Correct answer: B.** Authentication verifies the identity associated with a request.

### Question 2

Which API returns the user model configured for the project?

- A. get_user_model()
- B. get_current_password()
- C. get_admin_site()
- D. get_template_model()

**Correct answer: A.** Use this function in Python code that needs the active user model.

### Question 3

Which property checks whether the current user is authenticated?

- A. request.user.login()
- B. request.user.is_authenticated
- C. request.user.is_staff()
- D. request.user.password

**Correct answer: B.** It is a Boolean property, not a method.

### Question 4

Which flag indicates that a user is a superuser?

- A. is_active
- B. is_staff
- C. is_superuser
- D. is_logged_in

**Correct answer: C.** Superusers have all permissions by default.

### Question 5

Which decorator protects a view from anonymous access?

- A. csrf_exempt
- B. login_required
- C. staticmethod
- D. property

**Correct answer: B.** It requires the request to be authenticated before the view runs.

---

# PART 14 — INTERVIEW PREPARATION

## 80. Explain Django authentication

**Answer:** Django authentication verifies the identity of a user. It includes a configured user model, password hashing, login and logout functions, sessions and authentication helpers. A request can access its current user through request.user when authentication middleware is configured.

**Follow-up:** Does authentication decide which records the user may edit?

**Answer:** No. That is an authorization decision.

## 81. What is the difference between is_staff and is_superuser?

**Answer:** is_staff marks a user as eligible to access the Django admin site, subject to permissions. is_superuser grants all permissions. A staff user is not automatically a superuser.

**Follow-up:** Should a normal student account have either flag enabled?

**Answer:** Normally no. A student should receive only the access required for the student workflow.

## 82. Why use get_user_model()?

**Answer:** It returns the user model configured for the project. It avoids hard-coding an assumption that the project always uses Django's default User class.

**Follow-up:** What should be used in a model ForeignKey or OneToOneField?

**Answer:** Use settings.AUTH_USER_MODEL as the relationship target.

## 83. What is request.user?

**Answer:** It is the user associated with the current HTTP request. For an anonymous visitor, it represents an anonymous user. For a signed-in visitor, it represents the authenticated account.

**Follow-up:** Which middleware makes it available?

**Answer:** Django's AuthenticationMiddleware, used with session middleware.

## 84. Why should passwords be hashed?

**Answer:** A password hash prevents the database from storing the original readable password. Django uses configured password hashers and provides methods such as set_password() and check_password().

**Follow-up:** Should an application decrypt the password to compare it?

**Answer:** No. It should use Django's password verification method.

## 85. How do you protect a page?

**Answer:** For a page that requires a signed-in user, use login_required. For actions that require a particular permission, add an authorization check as well.

**Follow-up:** Does login_required check ownership of an object?

**Answer:** No. The view must check whether the current user is allowed to access that particular object.

## 86. Scenario: a student can view another student's account

**Answer:** The view may be retrieving a user using a hard-coded username or an untrusted ID from the URL. For a page showing the current account, use request.user. For another record, enforce ownership or permission checks before returning its data.

## 87. Scenario: an inactive user cannot sign in

**Answer:** Inspect the account's is_active status and the authentication backend behavior. Do not solve the problem by automatically making every user active without understanding the account lifecycle.

## 88. Scenario: a developer stores a raw password in the model

**Answer:** This is unsafe. Use Django's user manager create_user() or the model's set_password() method, then save the account.

---

# PART 15 — INDEPENDENT COMPLETION CHECK

## 89. Do not mark the lesson complete because you copied code

You should be able to perform these tasks without reading the solution line by line:

1. Explain authentication in your own words.
2. Explain authorization in your own words.
3. Locate the user model APIs.
4. Create a fictional test account.
5. Verify a password using check_password().
6. Identify the current user in a view.
7. Protect a page using login_required.
8. Explain why the password is not displayed.
9. Run the automated tests.
10. Diagnose one intentional mistake.

## 90. Intentional debugging exercise

Ask a learner or use your own practice copy to introduce one small mistake:
- Misspell the URL name.
- Remove the authentication middleware in a temporary test branch.
- Misspell the template path.
- Call is_authenticated() as if it were a method.

Before changing the code:
1. Read the error.
2. Identify the file and line.
3. Explain the likely cause.
4. Make one small correction.
5. Run the check again.
6. Verify the browser behavior.

Do not make intentional mistakes in the production branch or in a shared learner database.

## 91. Final checklist

- [ ] I understand authentication.
- [ ] I understand authorization.
- [ ] I can explain the user model.
- [ ] I know the difference between get_user_model() and AUTH_USER_MODEL.
- [ ] I can explain request.user.
- [ ] I can explain is_authenticated.
- [ ] I can explain is_active, is_staff and is_superuser.
- [ ] I created a fictional test account safely.
- [ ] I did not expose password data.
- [ ] I protected the account summary page.
- [ ] I tested an anonymous request.
- [ ] I tested two different user accounts.
- [ ] I ran Django's system check.
- [ ] I ran the automated tests.
- [ ] I completed User Account Management.
- [ ] I answered the interview questions.
- [ ] I completed the MCQ assessment.

**Next lesson:** Day 47 — User Registration, Login and Logout.

---

## 92. Reference links

Use documentation for the Django version used in the project.

1. Django authentication: https://docs.djangoproject.com/en/5.2/topics/auth/
2. Django user model: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/
3. Django authentication API: https://docs.djangoproject.com/en/5.2/topics/auth/default/
4. Django password management: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
5. Django testing tools: https://docs.djangoproject.com/en/5.2/topics/testing/tools/

**Version reminder:** This lesson targets Django 5.2.19. If the course baseline changes, test all commands, imports, settings and examples before publishing the updated lesson.
