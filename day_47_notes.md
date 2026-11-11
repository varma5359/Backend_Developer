# Day 47: User Registration, Login and Logout

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–5 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–46 — Django project setup, URLs, views, templates, forms, ORM and the configured user model  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config / profiles  
**Approved mini-project:** User Authentication Application

> **Self-learning promise:** You will build a complete registration, login and logout journey using Django's authentication APIs. You will understand the difference between creating an account and signing in, protect pages, handle invalid credentials, and test the complete browser flow. Use fictional local accounts only.

---

# PART 1 — THE USER JOURNEY

## 1. What are we building?

A new student visits an institute portal. The student has no account yet.

The student needs to:
1. Open a registration page.
2. Enter a username and password twice.
3. Submit the registration form.
4. Receive a clear success or validation message.
5. Sign in using the new account.
6. Open a page available only to signed-in users.
7. Sign out safely.
8. Be prevented from opening the protected page after signing out.

These steps form an authentication journey.

## 2. Important words

| Term | Meaning |
|---|---|
| Registration | Creating a new account |
| Login | Verifying credentials and establishing an authenticated session |
| Logout | Ending the current authenticated session |
| Credential | Information used to prove account identity |
| Authentication backend | Component that checks submitted credentials |
| Session | State that allows requests from the same browser session to remain associated with a user |
| CSRF token | A security token used to help protect state-changing browser requests |
| Redirect | An HTTP response that tells the browser to request another URL |
| Validation | Checking whether submitted values follow rules |
| POST request | HTTP request method commonly used to submit form data that changes server state |

## 3. Registration versus login

| Registration | Login |
|---|---|
| Creates a new account | Uses an existing account |
| Validates new account details | Verifies submitted credentials |
| Saves a user record | Establishes a signed-in session |
| Must prevent duplicate usernames | Must reject invalid credentials |
| Usually uses UserCreationForm or a custom form | Uses authenticate() and login() |

Do not use the words registration and login as if they mean the same operation.

## 4. Complete request flow

~~~text
New visitor
   |
   v
Registration page
   |
   v
Submit username + password + confirmation
   |
   v
Validate form
   |
   +---- Invalid ----> Show field errors
   |
   +---- Valid ------> Create user with hashed password
                           |
                           v
                       Registration success
                           |
                           v
                       Login page
                           |
                           v
                  Submit username + password
                           |
                           v
                    authenticate()
                           |
                  +--------+--------+
                  |                 |
               Invalid            Valid
                  |                 |
             Show error          login()
                                    |
                                    v
                              Authenticated session
                                    |
                                    v
                              Protected page
                                    |
                                    v
                              POST logout
                                    |
                                    v
                              Anonymous visitor
~~~

## 5. Learning outcomes

By the end, you can:
- Explain the registration and login workflows.
- Explain why password confirmation is needed.
- Use Django's UserCreationForm.
- Explain what form.is_valid() does.
- Use authenticate() to verify credentials.
- Use login() to establish an authenticated session.
- Use logout() to end the session.
- Protect views with login_required.
- Use POST for logout.
- Include CSRF protection in HTML forms.
- Display validation errors.
- Test successful and failed workflows.
- Complete User Authentication Application.

---

# PART 2 — PREPARE THE EXISTING PROJECT

## 6. Open the project root

Open the existing student_portal directory in VS Code.

In PowerShell:

~~~powershell
Get-Location
Get-ChildItem
.\.venv\Scripts\Activate.ps1
python -m django --version
~~~

The current directory must contain manage.py. Do not create a second project.

## 7. Confirm the authentication configuration

Open config/settings.py.

Check that these apps are present in INSTALLED_APPS:

~~~python
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
~~~

Check the middleware:

~~~python
"django.contrib.sessions.middleware.SessionMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
~~~

SessionMiddleware must come before AuthenticationMiddleware.

## 8. Confirm templates configuration

In config/settings.py, the generated TEMPLATES configuration normally includes:

~~~python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
~~~

Do not replace the whole setting if your project already has additional configuration. Check the important values:
- APP_DIRS is enabled for app templates.
- Authentication context processor is present.
- Messages context processor is present if you use messages in the templates.

## 9. Configure named redirect destinations

Add or confirm these settings:

~~~python
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "account_summary"
LOGOUT_REDIRECT_URL = "login"
~~~

A URL name is not a path. It is a stable name used by Django's reverse URL system.

These names must exist in the URL configuration. This lesson will create login, register and logout routes.

## 10. Check the current URL structure

The project URL file config/urls.py should include the profiles application.

The profiles app should have its own urls.py.

Do not remove existing routes for earlier projects. Add today's routes while preserving the working routes.

---

# PART 3 — REGISTRATION WITH UserCreationForm

## 11. What is a form?

A form collects values from a user and validates them before the application uses them.

Example:
- Username field.
- Password field.
- Password confirmation field.
- Submit button.

A browser form sends values to the server. The server must validate them again. Never assume browser-side validation is sufficient.

## 12. What is UserCreationForm?

Django provides UserCreationForm for creating users.

It includes:
- Username input.
- Password input.
- Password confirmation.
- Validation that the two passwords match.
- Password validation according to configured validators.
- User creation behavior that uses Django's password handling.

This saves you from manually implementing common password rules.

## 13. Why not create a user from raw POST values?

Unsafe idea:

~~~python
username = request.POST["username"]
password = request.POST["password"]
User.objects.create(username=username, password=password)
~~~

Problems:
- It does not provide complete form validation.
- It may store a raw password incorrectly.
- It does not handle password confirmation.
- It may fail to handle missing fields safely.
- It mixes request parsing, validation and database logic.

Use Django forms and the authentication APIs.

## 14. Create the registration view

Open profiles/views.py.

Keep earlier views. Add these imports if they are not already present:

~~~python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
~~~

Add the view:

~~~python
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                "Your account has been created. You can now sign in."
            )
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "profiles/register.html",
        {"form": form},
    )
~~~

## 15. Understand request.method

A browser can request a page using different HTTP methods.

GET:
- Usually requests a page or reads information.
- Does not normally create an account.
- Opens an empty registration form.

POST:
- Submits the form data.
- The server validates the submitted values.
- A valid submission may create an account.

The view checks the method so it can distinguish opening the form from submitting it.

## 16. Understand request.POST

request.POST contains submitted form values for a POST request.

Passing request.POST to UserCreationForm binds the submitted values to the form.

A bound form can validate those values and report errors.

Do not print passwords from request.POST into logs or terminal output.

## 17. Understand form.is_valid()

form.is_valid() runs the form's validation.

For UserCreationForm, validation includes checks such as:
- Required username.
- Username uniqueness.
- Password confirmation match.
- Password validation.
- Any configured field validation.

If validation fails:
- is_valid() returns False.
- The form contains errors.
- The view renders the form again.
- The template can display those errors.

If validation succeeds:
- is_valid() returns True.
- The form is ready to save.

## 18. Understand form.save()

form.save() creates and saves the user.

UserCreationForm uses Django's user creation behavior. The password is handled through Django's password-setting mechanism.

The returned object is the newly created user instance.

Do not replace this with direct assignment to the password field.

## 19. Create the registration template

Create this file:

profiles/templates/profiles/register.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Account</title>
</head>
<body>
    <main>
        <h1>Create your account</h1>

        <form method="post">
            {% csrf_token %}

            {{ form.non_field_errors }}

            <div>
                {{ form.username.label_tag }}
                {{ form.username }}
                {{ form.username.errors }}
            </div>

            <div>
                {{ form.password1.label_tag }}
                {{ form.password1 }}
                {{ form.password1.errors }}
            </div>

            <div>
                {{ form.password2.label_tag }}
                {{ form.password2 }}
                {{ form.password2.errors }}
            </div>

            <button type="submit">Register</button>
        </form>

        <p>
            Already registered?
            <a href="{% url 'login' %}">Sign in</a>
        </p>
    </main>
</body>
</html>
~~~

## 20. Explain the HTML form

method="post":
- Sends the form values using POST.
- Registration changes database state, so POST is appropriate.

{% csrf_token %}:
- Generates the CSRF token field.
- Helps protect the request against cross-site request forgery.
- Must be included in internal POST forms.

{{ form.username }}:
- Renders the username input widget.

{{ form.username.errors }}:
- Displays validation errors for that field.

{{ form.non_field_errors }}:
- Displays errors that do not belong to a single field.

The template displays errors rather than hiding them. A beginner must be able to understand why a submission failed.

## 21. Why password inputs are not displayed as readable text

Django's password form fields render password inputs.

The browser masks the characters while typing. This is a user-interface behavior, not the password hashing mechanism.

Password masking and password hashing solve different problems:
- Masking hides characters on the screen.
- Hashing protects stored password representations.

## 22. Add the registration URL

Open profiles/urls.py.

Add the import if needed:

~~~python
from django.urls import path
from . import views
~~~

Add this route to the existing urlpatterns list:

~~~python
path("register/", views.register_view, name="register"),
~~~

The route name is register. The browser path is /register/.

Do not create a second urlpatterns list. There should be one list containing the app's routes.

## 23. Verify the registration page

Run:

~~~powershell
python manage.py check
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/register/
~~~

Expected:
- A registration heading.
- Username input.
- Password input.
- Password confirmation input.
- Register button.
- Link to the login page.

If the login page is not ready yet, the named login link will not resolve. Complete the login route in the next section before testing the full page.

---

# PART 4 — LOGIN WITH authenticate() AND login()

## 24. What happens during login?

A user submits credentials.

Django must:
1. Receive the username and password.
2. Pass the credentials to an authentication backend.
3. Verify whether they are valid.
4. Return a user object if authentication succeeds.
5. Return None if authentication fails.
6. Establish a session after successful verification.

These are two separate operations:
- authenticate() verifies credentials.
- login() associates the user with the current session.

## 25. Import the required functions

In profiles/views.py:

~~~python
from django.contrib.auth import authenticate, login, logout
~~~

Do not confuse these function names with URL routes.

## 26. Create the login view

Add:

~~~python
def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            messages.success(request, "You are now signed in.")
            return redirect("account_summary")

        error_message = "Invalid username or password."

    return render(
        request,
        "profiles/login.html",
        {"error_message": error_message},
    )
~~~

## 27. Understand request.POST.get()

request.POST.get("username", ""):
- Reads the username value.
- Returns an empty string if the key is missing.
- Avoids a KeyError when the field is absent.

strip():
- Removes whitespace from the beginning and end of the username.
- It should not be used to alter passwords because spaces may be intentional password characters.

The password is read without strip().

## 28. Understand authenticate()

authenticate() asks the configured authentication backends to verify the supplied credentials.

Example:

~~~python
user = authenticate(
    request,
    username=username,
    password=password,
)
~~~

Possible outcomes:
- Valid credentials: a user object is returned.
- Invalid credentials: None is returned.
- Inactive user: standard authentication behavior normally rejects the account.

The exact credential fields depend on the configured user model and authentication backend.

## 29. Understand login()

login(request, user) stores the authenticated user's identity in the session and rotates or establishes session state as appropriate.

It does not validate the password itself.

The safe order is:
1. Call authenticate().
2. Check that a user object was returned.
3. Call login() with the request and user.

Do not call login() with an arbitrary user ID supplied by a browser.

## 30. Why return a generic error?

A login page should normally show a generic message such as:

"Invalid username or password."

Do not reveal whether:
- A username exists.
- A password is wrong.
- A particular account is registered.

Detailed account-existence messages can help attackers enumerate accounts.

## 31. Create the login template

Create:

profiles/templates/profiles/login.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In</title>
</head>
<body>
    <main>
        <h1>Sign in</h1>

        {% if error_message %}
            <p role="alert">{{ error_message }}</p>
        {% endif %}

        <form method="post">
            {% csrf_token %}

            <div>
                <label for="username">Username</label>
                <input
                    type="text"
                    id="username"
                    name="username"
                    autocomplete="username"
                    required
                >
            </div>

            <div>
                <label for="password">Password</label>
                <input
                    type="password"
                    id="password"
                    name="password"
                    autocomplete="current-password"
                    required
                >
            </div>

            <button type="submit">Sign in</button>
        </form>

        <p>
            New user?
            <a href="{% url 'register' %}">Create an account</a>
        </p>
    </main>
</body>
</html>
~~~

## 32. Understand the input attributes

| Attribute | Purpose |
|---|---|
| type="text" | Shows a normal text input |
| type="password" | Masks typed characters |
| name="username" | Key used in request.POST |
| id="username" | Connects a label to the input |
| required | Browser-side required-field check |
| autocomplete="username" | Helps password managers identify the field |
| autocomplete="current-password" | Identifies an existing account password |

Browser validation is helpful, but Django must still validate the request.

## 33. Add the login URL

In profiles/urls.py, add:

~~~python
path("login/", views.login_view, name="login"),
~~~

Now the route name login exists.

## 34. Test valid login

1. Register a fictional test account.
2. Open /login/.
3. Enter the same username.
4. Enter the matching practice password.
5. Submit.

Expected:
- authenticate() returns the test user.
- login() establishes the session.
- The browser is redirected to account_summary.
- The protected account page displays the signed-in user's details.

## 35. Test invalid login

Try:
- Correct username and wrong password.
- Unknown username.
- Empty username.
- Empty password.

Expected:
- The user is not signed in.
- The page displays a generic error or browser required-field validation.
- The protected account page remains inaccessible to the anonymous visitor.

Do not create an authenticated session after a failed credential check.

---

# PART 5 — LOGOUT SAFELY

## 36. What is logout?

Logout ends the current authenticated session.

After logout:
- The browser should no longer be associated with the signed-in user.
- request.user should become anonymous on subsequent requests.
- Protected views should redirect the visitor to login.

## 37. Why logout should use POST

Logging out changes server-side authentication state.

A normal link performs GET. GET requests should not be used for actions that change state.

Use a form with method POST and a CSRF token.

## 38. Create the logout view

In profiles/views.py:

~~~python
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
~~~

Add:

~~~python
@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, "You have signed out.")
    return redirect("login")
~~~

Explanation:
- login_required prevents anonymous visitors from using the logout action.
- require_POST restricts the view to POST requests.
- logout(request) ends the authenticated session.
- redirect("login") sends the browser to the named login route.

## 39. Create a logout form

Add this to the account summary template:

~~~html
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Sign out</button>
</form>
~~~

Do not replace the form with a normal GET link.

## 40. Add the logout URL

In profiles/urls.py:

~~~python
path("logout/", views.logout_view, name="logout"),
~~~

## 41. Test logout

1. Sign in.
2. Open the account summary page.
3. Click Sign out.
4. Confirm that the browser reaches the login page.
5. Manually type /account/ in the address bar.
6. Confirm that the protected page redirects to login.

Try opening /logout/ using GET.

Expected:
- The route should not perform logout through GET.
- Django should reject the unsupported method with HTTP 405.

A 405 response means the URL exists but the HTTP method is not allowed.

---

# PART 6 — DISPLAY FEEDBACK WITH DJANGO MESSAGES

## 42. Why messages matter

Users need feedback after actions.

Examples:
- Account created successfully.
- Login successful.
- Logout successful.
- Profile saved.
- Invalid form submission.

Django's messages framework provides temporary messages that can be displayed after redirects.

## 43. Add a message area to templates

Add this block near the top of the body in login.html and register.html:

~~~html
{% if messages %}
    <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
~~~

This is a preview of Day 52, where the messages framework is studied in detail.

## 44. Confirm messages configuration

Check config/settings.py:
- django.contrib.messages is in INSTALLED_APPS.
- MessageMiddleware is enabled.
- messages context processor is enabled.

Do not add duplicate middleware entries.

---

# PART 7 — COMPLETE URL CONFIGURATION

## 45. Example profiles/urls.py

Your file may contain earlier routes. The following is a compact illustration of the new routes. Merge these entries into your existing urlpatterns.

~~~python
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("account/", views.account_summary, name="account_summary"),
]
~~~

## 46. Confirm config/urls.py

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
~~~

If your project has another root route, preserve it.

## 47. Route reference table

| Browser path | URL name | View | Method |
|---|---|---|---|
| /register/ | register | register_view | GET, POST |
| /login/ | login | login_view | GET, POST |
| /logout/ | logout | logout_view | POST |
| /account/ | account_summary | account_summary | GET |

---

# PART 8 — SECURITY CHECKLIST

## 48. Password handling

- Use Django's user creation form or manager.
- Never store raw passwords.
- Never log submitted passwords.
- Never display password hashes.
- Do not email a user's existing password.
- Use password reset workflows rather than asking for the old password when it is forgotten.

## 49. CSRF protection

Every internal HTML form that sends POST data should include the CSRF token.

~~~html
<form method="post">
    {% csrf_token %}
    ...
</form>
~~~

Do not disable CSRF protection to make a form work.

## 50. Authentication versus authorization

login_required proves that the visitor is signed in.

It does not prove:
- The user owns a particular employee record.
- The user can edit every product.
- The user can access staff-only pages.
- The user can delete another user's data.

Add the correct permission or ownership check for each sensitive operation.

## 51. Safe redirect handling

Use named routes such as redirect("account_summary") for fixed destinations.

If you accept a next URL from query parameters or form data, validate that it is safe before redirecting. Do not redirect users to arbitrary untrusted external URLs.

## 52. Account enumeration

Use generic login errors. Avoid responses that reveal whether a username is registered.

Registration can also require careful messaging and throttling in production systems.

## 53. Production considerations

This lesson uses Django's local development server and local database.

A production deployment also needs:
- HTTPS.
- Secure cookie settings.
- Appropriate password validators.
- Rate limiting or abuse controls.
- Email verification where required.
- Monitoring and logging without credentials.
- Secure secret management.
- A tested account recovery process.

Do not claim the local demo is production-ready.

---

# PART 9 — TEST THE FULL JOURNEY

## 54. Manual test plan

| Test | Action | Expected result |
|---|---|---|
| Open registration | GET /register/ | Registration form appears |
| Valid registration | Submit unused username and valid matching passwords | Account created |
| Duplicate username | Register same username again | Validation error |
| Password mismatch | Enter different password values | Validation error |
| Weak password | Submit a password rejected by validators | Validation error |
| Open login | GET /login/ | Login form appears |
| Valid login | Submit correct credentials | Signed-in session |
| Wrong password | Submit incorrect password | Generic error |
| Unknown user | Submit unknown username | Generic error |
| Protected page anonymous | GET /account/ while signed out | Redirect to login |
| Protected page signed in | GET /account/ after login | Account summary appears |
| Logout POST | Submit logout form | Session ends |
| Logout GET | Open /logout/ with GET | Method not allowed |
| Protected page after logout | GET /account/ | Redirect to login |

## 55. Add automated tests

Open profiles/tests.py.

If earlier tests exist, keep them. Add the following class and merge imports:

~~~python
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AuthenticationFlowTests(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_valid_registration_creates_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "register_test_user",
                "password1": "Test-Only-Password-123!",
                "password2": "Test-Only-Password-123!",
            },
        )

        self.assertRedirects(response, reverse("login"))
        self.assertTrue(
            User.objects.filter(username="register_test_user").exists()
        )

    def test_invalid_registration_does_not_create_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "mismatch_user",
                "password1": "Test-Only-Password-123!",
                "password2": "Different-Password-456!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            User.objects.filter(username="mismatch_user").exists()
        )

    def test_valid_login_authenticates_user(self):
        User.objects.create_user(
            username="login_test_user",
            password="Test-Only-Password-123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "login_test_user",
                "password": "Test-Only-Password-123!",
            },
        )

        self.assertRedirects(response, reverse("account_summary"))
        self.assertTrue(
            "_auth_user_id" in self.client.session
        )

    def test_invalid_login_does_not_authenticate(self):
        User.objects.create_user(
            username="wrong_password_user",
            password="Test-Only-Password-123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "wrong_password_user",
                "password": "Wrong-Password-456!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            "_auth_user_id" in self.client.session
        )

    def test_logout_requires_post(self):
        user = User.objects.create_user(
            username="logout_test_user",
            password="Test-Only-Password-123!",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 405)

    def test_logout_ends_session(self):
        user = User.objects.create_user(
            username="logout_post_user",
            password="Test-Only-Password-123!",
        )
        self.client.force_login(user)

        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("login"))
        self.assertFalse(
            "_auth_user_id" in self.client.session
        )
~~~

Important:
- These tests assume the exact route names and view behavior described in this lesson.
- The test user passwords are fictional and exist only in Django's temporary test database.
- Do not copy test credentials into a production database.
- If you change a redirect destination, update the corresponding assertion.

## 56. Run the tests

~~~powershell
python manage.py check
python manage.py test profiles
~~~

Read the test summary. A passing run should end with OK.

If a test fails:
1. Identify the failing test method.
2. Read the assertion message.
3. Check the view and URL name.
4. Check the submitted form field names.
5. Re-run the single test or the app test suite.

## 57. Test with two different users

Create two fictional accounts.

Test:
- User A registers and signs in.
- User A sees their own account summary.
- User A signs out.
- User B signs in.
- User B sees their own account summary.

Do not hard-code one user's ID or username into the view.

---

# PART 10 — COMMON ERRORS

## 58. TemplateDoesNotExist

Cause:
- Template folder path is wrong.
- File name is wrong.
- App is not registered.
- APP_DIRS is not enabled.

Expected paths:
- profiles/templates/profiles/register.html
- profiles/templates/profiles/login.html

## 59. NoReverseMatch

Cause:
- URL name does not exist.
- Name is misspelled.
- App URL file is not included.
- Duplicate or conflicting URL configuration.

Check:
1. profiles/urls.py.
2. config/urls.py.
3. The exact route name used by redirect() and {% url %}.
4. Run python manage.py check.

## 60. CSRF verification failed

Cause:
- Missing {% csrf_token %}.
- Form is not submitting to the expected same-site endpoint.
- CSRF middleware was removed or changed.
- Browser cookies or session state are not working as expected.

Fix:
- Restore CSRF middleware.
- Include the token inside the POST form.
- Do not disable CSRF protection as a shortcut.

## 61. User is created but login fails

Check:
- Did registration actually save the account?
- Is the username typed exactly?
- Is the password the same?
- Is the account active?
- Is the authentication backend configured?
- Did the account creation use UserCreationForm or create_user()?

Do not inspect or attempt to decode the password hash.

## 62. Login succeeds but protected page fails

Check:
- LOGIN_REDIRECT_URL points to an existing route.
- The account summary route exists.
- The account summary template exists.
- AuthenticationMiddleware is enabled.
- The view uses request.user.

## 63. Logout returns 405

A 405 on GET is expected in this lesson because logout is restricted to POST.

Use the logout form with:
- method="post"
- action pointing to logout
- {% csrf_token %}

## 64. Form errors do not appear

Check that the template displays:
- form.non_field_errors
- individual field errors
- the bound form passed from the view

When form.is_valid() is False, render the same bound form so its errors remain available.

---

# PART 11 — APPROVED MINI-PROJECT

## 65. User Authentication Application

### Business problem

Build a small authentication feature for a training institute portal.

A new student must be able to register. An existing student must be able to sign in. Signed-in users can access their account summary. Users can sign out safely.

### Functional requirements

1. Registration page.
2. Username and password confirmation.
3. Password validation.
4. Login page.
5. Credential verification through authenticate().
6. Session creation through login().
7. Protected account page.
8. POST-only logout.
9. CSRF token on every internal POST form.
10. Generic invalid-login message.
11. Registration and login success feedback.
12. Automated tests for success and failure cases.

### File checklist

| File | Work |
|---|---|
| profiles/views.py | Registration, login and logout views |
| profiles/urls.py | Register, login and logout routes |
| profiles/templates/profiles/register.html | Registration form |
| profiles/templates/profiles/login.html | Login form |
| profiles/templates/profiles/account_summary.html | Protected account page |
| config/settings.py | Redirect settings and auth configuration |
| profiles/tests.py | Authentication tests |

### Acceptance criteria

- [ ] A new fictional user can register.
- [ ] Duplicate username is rejected.
- [ ] Password mismatch is rejected.
- [ ] Valid credentials sign in.
- [ ] Invalid credentials do not sign in.
- [ ] Anonymous users cannot open account summary.
- [ ] Authenticated users can open account summary.
- [ ] Logout uses POST.
- [ ] A logged-out user cannot reopen the protected page.
- [ ] No password or password hash is displayed.
- [ ] Tests pass.
- [ ] The learner can explain the complete request flow.

### Submission evidence

- Source code.
- Browser screenshots using fictional data.
- Terminal output from system checks and tests.
- README with setup instructions.
- Test table with actual outcomes.
- Short explanation of one failure and its fix.

---

# PART 12 — SELF-ASSESSMENT

## 66. Short-answer questions

1. What is registration?
2. What is login?
3. Why are registration and login different?
4. What does UserCreationForm provide?
5. What does form.is_valid() do?
6. What happens when form.save() is called?
7. What does authenticate() return for valid credentials?
8. What does authenticate() return for invalid credentials?
9. Why must login() be called after authenticate()?
10. What does logout() do?
11. Why should logout use POST?
12. What does {% csrf_token %} do?
13. Why should a login error message be generic?
14. What does a 405 response mean?
15. Why should a protected page be tested after logout?

## 67. Self-check answers

1. Registration creates a new account.
2. Login verifies credentials and establishes an authenticated session.
3. One creates an account; the other uses an existing account.
4. It provides standard user creation fields and validation.
5. It validates submitted form values.
6. It saves the new user using the form's user-creation behavior.
7. It returns a user object.
8. It returns None.
9. authenticate verifies identity; login establishes session state.
10. It ends the authenticated session.
11. Logout changes server-side state and should not be triggered by a safe GET request.
12. It includes a CSRF token for protection of state-changing form submissions.
13. It avoids revealing account existence to an attacker.
14. The URL exists but does not allow the requested HTTP method.
15. It verifies that the session has actually ended and protected access is blocked.

## 68. MCQ assessment

### Question 1
Which Django form is commonly used for standard user registration?

- A. ModelAdmin
- B. UserCreationForm
- C. LoginRequired
- D. QueryForm

**Answer: B.** UserCreationForm includes standard account creation validation.

### Question 2
Which function verifies credentials?

- A. login()
- B. logout()
- C. authenticate()
- D. redirect()

**Answer: C.** authenticate() checks credentials using configured authentication backends.

### Question 3
Which function establishes the authenticated session?

- A. login()
- B. authenticate()
- C. render()
- D. get_user_model()

**Answer: A.** login() associates the user with the request session.

### Question 4
Which method should be used for a logout form?

- A. GET
- B. POST
- C. TRACE
- D. OPTIONS

**Answer: B.** Logout changes authentication state and should be submitted using POST.

### Question 5
What is the purpose of CSRF token in a POST form?

- A. It stores the password.
- B. It protects against cross-site request forgery.
- C. It creates the user.
- D. It sorts the database.

**Answer: B.** The token helps Django verify that the request originated from an expected form flow.

---

# PART 13 — INTERVIEW PREPARATION

## 69. Explain user registration in Django

**Answer:** Registration collects account details, validates the values and creates a user. Django's UserCreationForm provides standard username and password confirmation behavior. Saving the valid form creates the user through Django's password-handling workflow.

**Follow-up:** Why not directly insert the submitted password into the User model?

**Answer:** Direct assignment can store the raw password. Use Django's user creation APIs.

## 70. Explain authenticate() and login()

**Answer:** authenticate() verifies submitted credentials and returns a user object if they are valid. login() establishes the authenticated session for that user. They perform different responsibilities.

**Follow-up:** What happens when authenticate() returns None?

**Answer:** The credentials were not accepted. Do not call login().

## 71. Why should logout be POST-only?

**Answer:** Logout changes the user's authentication state. GET requests should be safe and should not trigger state-changing actions. A POST form with a CSRF token is the appropriate browser interaction.

**Follow-up:** What HTTP status can a disallowed GET request produce?

**Answer:** HTTP 405 Method Not Allowed.

## 72. What is the difference between a bound and unbound form?

**Answer:** A bound form has submitted data attached to it and can be validated. An unbound form is normally an empty form shown before submission.

**Follow-up:** Why render the bound form again after invalid submission?

**Answer:** It contains validation errors that the template can display.

## 73. Scenario: registration saves duplicate users

**Answer:** The form or model validation is not being applied correctly, or the chosen identity field is not configured as unique. Use the appropriate Django form and database uniqueness rule. Do not rely only on browser-side checks.

## 74. Scenario: login always fails

**Answer:** Check the exact submitted field names, password, account active status, authentication backend and whether the account was created through Django's password APIs. Do not attempt to read the stored hash as if it were the original password.

## 75. Scenario: logout link signs a user out through GET

**Answer:** Replace the GET link with a POST form, include the CSRF token, and restrict the view to POST.

---

# PART 14 — INDEPENDENT COMPLETION

## 76. Explain the journey without reading

Draw the flow from registration to logout.

Include:
- Registration form.
- Form validation.
- User creation.
- Login form.
- authenticate().
- login().
- Protected page.
- POST logout.
- Anonymous request.

## 77. Controlled debugging

In a local practice copy only:
1. Remove the CSRF token from a test form and observe the failure.
2. Restore it.
3. Change a URL name and observe the reverse-resolution error.
4. Restore the name.
5. Submit a mismatched password pair.
6. Explain the validation message.
7. Sign in with a wrong password.
8. Explain why the session was not created.

Never leave the intentional mistakes in the final submission.

## 78. Final checklist

- [ ] I understand the difference between registration and login.
- [ ] I can explain UserCreationForm.
- [ ] I can explain form validation.
- [ ] I can explain authenticate().
- [ ] I can explain login().
- [ ] I can explain logout().
- [ ] I used CSRF tokens.
- [ ] I used POST for logout.
- [ ] I tested invalid credentials.
- [ ] I tested anonymous access.
- [ ] I tested logout and subsequent access.
- [ ] I completed User Authentication Application.
- [ ] I ran the automated tests.
- [ ] I completed the MCQs and interview questions.

**Next lesson:** Day 48 — Password Management, Password Reset and Secure Password Storage.

---

## 79. Official references

1. Django authentication: https://docs.djangoproject.com/en/5.2/topics/auth/
2. Built-in authentication views and forms: https://docs.djangoproject.com/en/5.2/topics/auth/default/
3. Password management: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
4. CSRF protection: https://docs.djangoproject.com/en/5.2/howto/csrf/
5. Testing tools: https://docs.djangoproject.com/en/5.2/topics/testing/tools/

**Version reminder:** This lesson targets Django 5.2.19. Re-run the tests if the project version or authentication configuration changes.
