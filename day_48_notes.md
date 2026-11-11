# Day 48: Password Management, Password Reset and Secure Password Storage

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–5 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–47 — Django user model, registration, login, logout, forms and sessions  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config / profiles  
**Approved mini-project:** Password Recovery System

> **Self-learning promise:** This lesson explains how passwords should be created, stored, changed and reset. You will use Django's password APIs and built-in password forms/views rather than inventing a security mechanism. Use fictional local test accounts only. Never share a real password, reset token, or session cookie.

---

# PART 1 — UNDERSTAND THE PASSWORD PROBLEM

## 1. A real-world situation

A student has an account in the institute portal. The student:
- Creates a password during registration.
- Signs in using that password.
- Later wants to change the password.
- One day forgets the password.
- Needs a safe way to regain access.

The portal must protect the password throughout this journey.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain why passwords must not be stored as plain text.
2. Distinguish hashing from encryption.
3. Explain what a password hash is.
4. Describe Django's password hashing workflow.
5. Use set_password() and check_password().
6. Explain why direct assignment to user.password is unsafe.
7. Identify Django password validators.
8. Configure password validation.
9. Use Django's password change form and view.
10. Explain password reset using email.
11. Configure the console email backend for local practice.
12. Configure password reset URLs and templates.
13. Explain uidb64 and reset tokens at a high level.
14. Test valid and invalid password changes.
15. Test the password reset workflow locally.
16. Understand session behavior after a password change.
17. Diagnose common password form and email issues.
18. Complete Password Recovery System.

## 3. Important vocabulary

| Term | Beginner meaning |
|---|---|
| Plain text | Original readable password |
| Hashing | Converting data into a one-way representation |
| Password hash | Stored representation used to verify a password |
| Salt | Random data used by a password hashing process to make identical passwords produce different stored hashes |
| Hashing algorithm | The algorithm used to calculate a hash |
| Encryption | Transforming data so it can be decrypted with the correct key |
| Password validator | A rule that checks whether a new password is acceptable |
| Password change | Updating a password when the user can authenticate |
| Password reset | Setting a new password through a recovery process |
| Reset token | A time-sensitive value used to validate a reset link |
| Email backend | Component that sends or records outgoing email |
| Session | State associated with a browser after authentication |
| Session authentication hash | Value Django uses to detect whether the user's password state has changed |

## 4. Hashing versus encryption

These concepts are not the same.

### Hashing

- Designed to be one-way.
- Used for password verification.
- The application stores the hash, not the original password.
- When a user signs in, Django checks a submitted password against the stored hash.

### Encryption

- Designed to be reversible with the correct key.
- Used when an application must recover the original data.
- Requires secure key management.

Passwords should be stored using password hashing, not reversible encryption.

| Hashing | Encryption |
|---|---|
| One-way by design | Reversible with a key |
| Used for password verification | Used when original data must be recovered |
| No decryption step | Decryption uses a key |
| Django password hashers | Encryption libraries and key management |

## 5. Why a normal fast hash is not enough

A password is often short and can be guessed.

A fast general-purpose hash can allow an attacker to test many guesses quickly if a database is stolen.

Password hashing algorithms are deliberately designed to make guessing more expensive. They may use configurable work factors and memory requirements.

Django provides password hashers and manages the stored format. Use the framework rather than writing your own algorithm.

## 6. Password lifecycle

~~~text
Registration
    |
    v
User submits password
    |
    v
Django validates password
    |
    v
Django password hasher creates stored hash
    |
    v
Database stores encoded password value
    |
    v
User later submits login password
    |
    v
Django verifies candidate against stored hash
    |
    +---- Match ----> Authentication may succeed
    |
    +---- No match -> Authentication fails

Forgot password
    |
    v
Submit account email
    |
    v
Django generates reset link/token
    |
    v
Email delivery
    |
    v
User opens valid link
    |
    v
Choose a new password
    |
    v
Django validates and stores new hash
~~~

---

# PART 2 — DJANGO PASSWORD HASHING

## 7. Where is the password stored?

The configured user model contains a password field.

The field stores an encoded representation produced by Django's configured password hasher.

When you inspect a test user's password field, you should see a value that is not the original password.

Do not display the field in a browser page, API response or log.

## 8. What does set_password() do?

Django user objects provide set_password().

Example:

~~~python
user.set_password("New-Local-Demo-Password-123!")
user.save()
~~~

Explanation:
- set_password() prepares a password hash using Django's configured password hasher.
- The original password is not stored as plain text.
- save() writes the changed password field to the database.

Important: set_password() changes the password on the in-memory model instance. You must save the user for the change to persist.

## 9. What does check_password() do?

Use:

~~~python
user.check_password("New-Local-Demo-Password-123!")
~~~

The method returns:
- True when the candidate password matches.
- False when it does not match.

It verifies the candidate without exposing the original password.

## 10. Why direct assignment is wrong

Do not use:

~~~python
user.password = "Plain-Text-Password"
user.save()
~~~

This bypasses Django's normal password-setting workflow. The database can end up containing a raw value that Django cannot authenticate as a correctly encoded password.

Correct:

~~~python
user.set_password("New-Local-Demo-Password-123!")
user.save()
~~~

Or use the appropriate Django form or user manager.

## 11. Create a local practice user

Open the project terminal, activate the existing environment and run:

~~~powershell
python manage.py shell
~~~

Enter:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

user, created = User.objects.get_or_create(
    username="password_demo_user",
    defaults={"email": "password-demo@example.test"},
)

if created:
    user.set_password("Old-Local-Demo-Password-123!")
    user.save()
~~~

Explanation:
- get_user_model() returns the configured user model.
- get_or_create() looks for the username.
- If no record exists, Django creates one using the defaults.
- created is True for a newly created record and False for an existing record.
- set_password() hashes the practice password.
- save() persists the hash.

This avoids a duplicate-username error when the learner repeats the shell exercise.

## 12. Verify the password

Run:

~~~python
user.check_password("Old-Local-Demo-Password-123!")
~~~

Expected:

~~~text
True
~~~

Run:

~~~python
user.check_password("Wrong-Password-123!")
~~~

Expected:

~~~text
False
~~~

Do not print the password field to inspect it.

## 13. Change the password in the shell

For demonstration only:

~~~python
user.set_password("New-Local-Demo-Password-456!")
user.save()
~~~

Now verify:

~~~python
user.check_password("Old-Local-Demo-Password-123!")
~~~

Expected: False.

~~~python
user.check_password("New-Local-Demo-Password-456!")
~~~

Expected: True.

A production application should normally use a password change form so that the current password can be checked and validation errors can be displayed.

## 14. Understand make_password()

Django also provides a helper function named make_password().

Example:

~~~python
from django.contrib.auth.hashers import make_password

encoded = make_password("Local-Demo-Password-789!")
~~~

It returns an encoded password representation.

Use this API when you specifically need to create a password hash. Most user-account code should use set_password(), create_user() or a built-in form.

Do not create a separate custom hashing implementation.

## 15. Understand check_password helper

Django's password hashers also provide a check_password() helper, but ordinary application code should normally call the user instance's check_password() method.

Use the APIs at the correct level:
- User object: user.check_password(candidate)
- Password-setting on a user: user.set_password(raw_password)
- General encoded value creation: make_password(raw_password)

---

# PART 3 — PASSWORD VALIDATION

## 16. What is password validation?

Password validation checks whether a proposed new password follows configured rules.

Possible rules:
- Minimum length.
- Not too similar to personal information.
- Not a commonly used password.
- Not entirely numeric.

Validation does not replace password hashing. They solve different problems.

## 17. Inspect AUTH_PASSWORD_VALIDATORS

Open config/settings.py.

A generated Django project commonly includes validators similar to:

~~~python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
~~~

Read the names carefully.

## 18. UserAttributeSimilarityValidator

This validator checks whether a password is too similar to user attributes such as username, first name, last name or email.

Example:
- Username: asha_student
- Password: asha_student123

A similar password may be rejected.

The goal is to avoid passwords that can be guessed from account information.

## 19. MinimumLengthValidator

This validator checks password length.

The default minimum length may be configured by the validator. Inspect the exact setting in your project and do not assume a different value.

A longer password or passphrase is generally harder to guess than a very short password.

## 20. CommonPasswordValidator

This validator rejects passwords found in a list of commonly used passwords.

Examples of weak choices include:
- password
- 12345678
- qwerty

Do not use these as actual account passwords.

## 21. NumericPasswordValidator

This validator rejects a password that consists entirely of numeric characters.

A password containing only a short sequence of digits is easy to guess.

## 22. Validate a password manually

Django provides validate_password().

~~~python
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

candidate = "password"

try:
    validate_password(candidate)
    print("Password accepted by configured validators")
except ValidationError as error:
    print(error.messages)
~~~

Explanation:
- validate_password() runs the configured validators.
- ValidationError is raised when one or more validators reject the candidate.
- error.messages contains human-readable validation messages.

The example uses a deliberately weak candidate to demonstrate validation. Never use it as an account password.

## 23. Validate using a user context

Some validators compare the password with user attributes.

Example:

~~~python
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()

user = User(
    username="asha_student",
    email="asha@example.test",
)

validate_password("AshaStudent123!", user=user)
~~~

The validator can use the user's attributes when deciding whether a password is too similar.

## 24. Password validation and forms

Django's built-in password forms use the configured password validation system.

This is one reason to prefer the built-in forms over manually processing raw password values.

A form can:
- Collect the proposed password.
- Run validation.
- Display validation errors.
- Save the password using Django's password APIs.

---

# PART 4 — PASSWORD CHANGE

## 25. Change versus reset

A password change normally happens when a signed-in user knows the current password and wants to replace it.

A password reset is used when a user cannot sign in because the password is forgotten.

| Password change | Password reset |
|---|---|
| User is normally authenticated | User may be anonymous |
| Usually asks for current password | Uses a time-limited recovery link |
| User chooses a new password | User chooses a new password after token validation |
| Protects an existing session | Re-establishes account access |

## 26. Django PasswordChangeForm

Django provides PasswordChangeForm.

It typically asks for:
- Current password.
- New password.
- New password confirmation.

It validates the current password and the new password according to configured rules.

## 27. Built-in PasswordChangeView

Django includes a class-based view for password changes.

A class-based view is a view implemented as a Python class rather than a function.

The built-in PasswordChangeView handles common password change behavior and uses PasswordChangeForm by default.

## 28. Add password change URL

Open profiles/urls.py.

Add the required imports:

~~~python
from django.contrib.auth import views as auth_views
~~~

Add this route:

~~~python
path(
    "password/change/",
    auth_views.PasswordChangeView.as_view(
        template_name="profiles/password_change.html",
        success_url="/password/change/done/",
    ),
    name="password_change",
),
~~~

For a maintainable application, use reverse URL names rather than hard-coding a path. We will add a named success route in the next step.

## 29. Add a password change success view

Use Django's PasswordChangeDoneView:

~~~python
path(
    "password/change/done/",
    auth_views.PasswordChangeDoneView.as_view(
        template_name="profiles/password_change_done.html",
    ),
    name="password_change_done",
),
~~~

Update the password change route to use the named destination:

~~~python
path(
    "password/change/",
    auth_views.PasswordChangeView.as_view(
        template_name="profiles/password_change.html",
        success_url="/password/change/done/",
    ),
    name="password_change",
),
~~~

The success URL is a fixed local path in this simple example. In a larger project, use reverse_lazy() with a named route to avoid repeating URL strings.

## 30. Protect password change

PasswordChangeView requires an authenticated user.

If an anonymous visitor tries to open the page, Django redirects to the login page.

This is appropriate because password change is an account-management action.

## 31. Create password_change.html

Create:

profiles/templates/profiles/password_change.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change Password</title>
</head>
<body>
    <main>
        <h1>Change your password</h1>

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

            <button type="submit">Update password</button>
        </form>
    </main>
</body>
</html>
~~~

## 32. Explain the template loop

{% for field in form %} repeats the HTML block for each form field.

field.label_tag renders the field's label.

field renders the input widget.

field.errors displays errors for that field.

The form may also have non-field errors, so display form.non_field_errors.

## 33. Create password_change_done.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Updated</title>
</head>
<body>
    <main>
        <h1>Password updated</h1>
        <p>Your password has been changed successfully.</p>
        <a href="{% url 'account_summary' %}">Return to account</a>
    </main>
</body>
</html>
~~~

## 34. Understand session preservation

Django's built-in password change form updates the session authentication hash after a successful password change. This allows the current user to remain signed in after changing their password.

When implementing a custom password change view, use Django's update_session_auth_hash() where appropriate. Do not assume a custom implementation automatically preserves the session.

A password reset is a different flow and may invalidate existing sessions according to Django's authentication hash behavior.

---

# PART 5 — PASSWORD RESET

## 35. What happens when a user forgets a password?

A user cannot provide the current password because they do not know it.

The application should not:
- Email the existing password.
- Display the stored password hash.
- Let the user change any account password by submitting only a username.
- Trust an arbitrary user ID without proof of account access.

A reset workflow sends a time-limited link to the account's registered email address.

## 36. Password reset flow

~~~text
Forgot password page
       |
       v
User enters registered email
       |
       v
Django searches for eligible account(s)
       |
       v
Django generates reset token and URL
       |
       v
Email backend sends or records message
       |
       v
User opens reset link
       |
       v
Django validates token
       |
       +---- Invalid/expired ----> Reject reset
       |
       +---- Valid -------------> Show new password form
                                      |
                                      v
                               Validate new password
                                      |
                                      v
                               Save new password hash
                                      |
                                      v
                               Reset complete page
~~~

## 37. Django's built-in reset views

Django provides:
- PasswordResetView
- PasswordResetDoneView
- PasswordResetConfirmView
- PasswordResetCompleteView

These views manage the standard password reset workflow.

## 38. Why use the built-in views?

They handle important details such as:
- Account lookup.
- Reset token generation.
- Reset token validation.
- Password form validation.
- Saving the new password.
- Completion behavior.

Do not create a reset token using a random string and assume that it is secure.

## 39. Configure local email output

For development, Django can write outgoing email content to the terminal instead of delivering it to a real mailbox.

Open config/settings.py and add:

~~~python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@example.test"
~~~

This is a development setting.

It does not send a real email. It prints the email content in the runserver terminal.

Never leave the console backend as the intended production email delivery configuration.

## 40. Add password reset routes

In profiles/urls.py, import auth_views if it is not already imported.

Add:

~~~python
path(
    "password/reset/",
    auth_views.PasswordResetView.as_view(
        template_name="profiles/password_reset.html",
        email_template_name="profiles/password_reset_email.txt",
        subject_template_name="profiles/password_reset_subject.txt",
        success_url="/password/reset/done/",
    ),
    name="password_reset",
),
path(
    "password/reset/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="profiles/password_reset_done.html",
    ),
    name="password_reset_done",
),
path(
    "password/reset/confirm/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="profiles/password_reset_confirm.html",
        success_url="/password/reset/complete/",
    ),
    name="password_reset_confirm",
),
path(
    "password/reset/complete/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="profiles/password_reset_complete.html",
    ),
    name="password_reset_complete",
),
~~~

The fixed success paths are shown for clarity. A production-quality URL configuration should prefer named reverse destinations with reverse_lazy().

## 41. Understand uidb64

The reset URL contains a user identifier encoded for safe use in a URL.

The encoded identifier is not a secret password.

The reset token is the security-sensitive proof that the reset request is valid.

Do not manually trust an identifier from a URL without validating the reset token.

## 42. Understand the reset token

Django generates a token tied to the account state.

The token is designed to become invalid when the relevant account state changes or the token expires according to the configured behavior.

Do not store or publish reset tokens in source control, screenshots or issue comments.

## 43. Create password_reset.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Forgot Password</title>
</head>
<body>
    <main>
        <h1>Reset your password</h1>
        <p>Enter the email address associated with your account.</p>

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

            <button type="submit">Send reset link</button>
        </form>
    </main>
</body>
</html>
~~~

## 44. Create password_reset_done.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reset Request Received</title>
</head>
<body>
    <main>
        <h1>Check your email</h1>
        <p>
            If an eligible account exists for that email address,
            password reset instructions have been sent.
        </p>
    </main>
</body>
</html>
~~~

This wording avoids confirming whether an email address belongs to an account.

## 45. Create the email subject template

Create:

profiles/templates/profiles/password_reset_subject.txt

~~~text
Password reset for your Student Portal account
~~~

Keep the subject concise.

## 46. Create the plain-text email body template

Create:

profiles/templates/profiles/password_reset_email.txt

~~~text
Hello,

A password reset was requested for your Student Portal account.

Use the link below to choose a new password:

{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

If you did not request this change, you can ignore this email.

Student Portal
~~~

The template uses values supplied by Django's password reset view.

## 47. Create password_reset_confirm.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Choose a New Password</title>
</head>
<body>
    <main>
        <h1>Choose a new password</h1>

        {% if validlink %}
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

                <button type="submit">Save new password</button>
            </form>
        {% else %}
            <p>This reset link is invalid or has expired.</p>
            <a href="{% url 'password_reset' %}">Request another link</a>
        {% endif %}
    </main>
</body>
</html>
~~~

## 48. Create password_reset_complete.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Reset Complete</title>
</head>
<body>
    <main>
        <h1>Password reset complete</h1>
        <p>You can now sign in using your new password.</p>
        <a href="{% url 'login' %}">Sign in</a>
    </main>
</body>
</html>
~~~

## 49. Add a forgot-password link to login

In profiles/templates/profiles/login.html, add:

~~~html
<p>
    <a href="{% url 'password_reset' %}">Forgot your password?</a>
</p>
~~~

Keep the existing login form and registration link.

## 50. Verify template paths

The expected template structure is:

~~~text
profiles/
└── templates/
    └── profiles/
        ├── login.html
        ├── register.html
        ├── password_change.html
        ├── password_change_done.html
        ├── password_reset.html
        ├── password_reset_done.html
        ├── password_reset_email.txt
        ├── password_reset_subject.txt
        ├── password_reset_confirm.html
        └── password_reset_complete.html
~~~

Check spelling and folder nesting carefully.

---

# PART 6 — TEST THE RESET FLOW LOCALLY

## 51. Important local testing limitation

The console email backend does not send email to an inbox.

It prints the message to the terminal running Django.

You must:
1. Start runserver.
2. Open the password reset page.
3. Submit the email address for a fictional test account.
4. Inspect the runserver terminal.
5. Copy the reset link only into your local browser.
6. Complete the reset flow.

Do not paste the reset link into a public issue, commit or shared screenshot.

## 52. Ensure the test user has an email address

Open the Django shell:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username="password_demo_user")
user.email = "password-demo@example.test"
user.save(update_fields=["email"])
~~~

PasswordResetView needs an eligible user with an email address.

## 53. Start the development server

~~~powershell
python manage.py check
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/password/reset/
~~~

Submit:

~~~text
password-demo@example.test
~~~

The browser should show the reset request confirmation page.

## 54. Inspect the runserver terminal

The console email backend prints the outgoing message.

Find the full reset URL in the terminal output.

The exact URL contains:
- Local host/domain information.
- Encoded user identifier.
- Reset token.

Treat the complete URL as sensitive while it is valid.

## 55. Open the reset URL

Copy the link from the local terminal and open it in your local browser.

Expected:
- Django validates the reset link.
- The new password form appears if the link is valid.
- An invalid or expired token is rejected.

## 56. Choose a new password

Enter a strong fictional practice password twice.

Submit.

Expected:
- Password validators accept the new password.
- Django stores the new password hash.
- The completion page appears.

## 57. Verify the new password

Open the Django shell:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
user = User.objects.get(username="password_demo_user")
user.check_password("New-Local-Recovery-Password-456!")
~~~

Expected: True, if that is the password you selected.

Verify the previous password returns False.

Do not display the password hash.

---

# PART 7 — SECURITY AND SESSION BEHAVIOR

## 58. What happens to existing sessions after a password change?

Django uses a session authentication hash to detect password changes.

A password change can invalidate other sessions associated with the account.

The built-in password change flow updates the current session's authentication hash so the user can remain signed in.

A password reset normally changes the password state and can cause previously authenticated sessions to become invalid.

The exact session behavior depends on the built-in flow and any custom authentication logic.

## 59. Why this matters

Imagine a student leaves a shared computer without signing out.

If the account password is changed from another device, old sessions should not remain trusted indefinitely.

Password changes and resets are important account-security events.

## 60. Do not reveal whether an email exists

The password reset confirmation page should not say:
- "This email exists."
- "No account found."
- "The user is registered."

Use neutral wording.

This makes it harder for someone to test which email addresses have accounts.

## 61. Protect reset links

A reset link is a temporary credential.

Never:
- Publish it.
- Commit it.
- Add it to analytics logs.
- Include it in screenshots shared publicly.
- Forward it to another person.
- Store it in an unprotected text file.

If a link is exposed, request a new reset link and treat the old one as compromised.

## 62. Production email configuration

The console backend is for local development.

A production application needs:
- A trusted email provider.
- SMTP or API credentials stored securely.
- TLS/secure transport.
- Correct sender-domain configuration.
- Delivery monitoring.
- Rate limiting.
- A safe retry strategy.
- No secrets in Git.

Do not put email passwords or API keys directly in settings.py.

## 63. Password policy

A useful password policy should:
- Avoid overly short passwords.
- Reject common passwords.
- Avoid passwords based on account information.
- Encourage long, unique passwords.
- Support password managers.
- Avoid arbitrary frequent forced changes without a risk reason.

Django's configured validators are a baseline. Review the policy for the application's risk and user population.

---

# PART 8 — AUTOMATED TESTS

## 64. Why test password behavior?

Password flows are security-sensitive.

Test that:
- Passwords are stored using Django's password API.
- Correct passwords verify.
- Wrong passwords fail.
- Password change requires authentication.
- Password reset pages load.
- Invalid reset tokens are rejected.
- The new password works after a successful reset.

## 65. Test password hashing

In profiles/tests.py, add or merge:

~~~python
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class PasswordStorageTests(TestCase):
    def test_create_user_hashes_password(self):
        user = User.objects.create_user(
            username="hash_test_user",
            password="Hash-Test-Password-123!",
        )

        self.assertNotEqual(
            user.password,
            "Hash-Test-Password-123!",
        )
        self.assertTrue(
            user.check_password("Hash-Test-Password-123!")
        )
        self.assertFalse(
            user.check_password("Wrong-Password-123!")
        )
~~~

## 66. Test password change page access

~~~python
from django.urls import reverse

class PasswordChangeAccessTests(TestCase):
    def test_anonymous_user_is_redirected(self):
        response = self.client.get(
            reverse("password_change")
        )

        self.assertEqual(response.status_code, 302)
~~~

This assumes the built-in PasswordChangeView route exists.

## 67. Test reset page

~~~python
class PasswordResetPageTests(TestCase):
    def test_reset_page_loads(self):
        response = self.client.get(
            reverse("password_reset")
        )

        self.assertEqual(response.status_code, 200)
~~~

## 68. Run tests

~~~powershell
python manage.py check
python manage.py test profiles
~~~

If the test file already imports TestCase or User, avoid duplicate definitions and merge the classes.

---

# PART 9 — COMMON ERRORS AND FIXES

## 69. Password is stored as raw text

Cause:
- Direct assignment to user.password.

Fix:
- Use set_password().
- Save the user.
- Use create_user() for ordinary account creation.

Do not try to repair a real production password database with an untested script.

## 70. Password validation fails

Cause:
- Password is too short.
- Password is too common.
- Password resembles user attributes.
- Password is entirely numeric.

Fix:
- Read the actual validation error.
- Choose a longer unique practice passphrase.
- Do not remove validators just to pass the exercise.

## 71. Password reset email is not visible

Check:
1. Is EMAIL_BACKEND set to the console backend?
2. Is runserver still running?
3. Does the user have an email address?
4. Is the account active?
5. Did the reset request return to the confirmation page?
6. Did you inspect the correct terminal window?

The email is printed in the server terminal, not delivered to a real inbox.

## 72. Reset link says invalid

Possible causes:
- Link was copied incompletely.
- Token expired.
- Password was changed after link creation.
- User account state changed.
- The link was already used.
- The URL was altered.

Request a new reset link. Do not try to edit the token manually.

## 73. NoReverseMatch on reset URL

Check:
- password_reset_confirm route name.
- uidb64 and token parameter names.
- URL path converter placeholders.
- Template's {% url %} arguments.
- URL inclusion in config/urls.py.

## 74. PasswordChangeView redirects unexpectedly

Check:
- User is signed in.
- LOGIN_URL exists.
- Password change route name is correct.
- The template path is correct.
- The user submitted the current password correctly.

## 75. New password works in shell but login fails

Check:
- Are you testing the same account?
- Is the browser using the same database/environment?
- Did the user account become inactive?
- Did you enter the exact new password?
- Are you using the correct authentication backend?

Do not manually change the stored password hash.

---

# PART 10 — APPROVED MINI-PROJECT

## 76. Password Recovery System

### Business problem

Students sometimes forget their portal password. The application needs a secure recovery workflow.

### Functional requirements

1. A signed-in user can change a password after supplying the current password.
2. An anonymous user can request a reset link using an email address.
3. The system does not reveal whether an email belongs to an account.
4. The reset link includes Django's token validation.
5. A valid link allows a new password to be saved.
6. An invalid or expired link is rejected.
7. Password validators run on the new password.
8. Passwords are stored using Django's password hashing workflow.
9. Local email output is visible using the console backend.
10. The learner can verify the new password without printing the hash.

### Files

| File | Responsibility |
|---|---|
| config/settings.py | Password validators and local email backend |
| profiles/urls.py | Change and reset routes |
| profiles/templates/profiles/password_change.html | Password change form |
| profiles/templates/profiles/password_change_done.html | Change confirmation |
| profiles/templates/profiles/password_reset.html | Reset request form |
| profiles/templates/profiles/password_reset_done.html | Neutral request confirmation |
| profiles/templates/profiles/password_reset_email.txt | Reset email body |
| profiles/templates/profiles/password_reset_subject.txt | Email subject |
| profiles/templates/profiles/password_reset_confirm.html | New password form |
| profiles/templates/profiles/password_reset_complete.html | Completion page |
| profiles/tests.py | Password behavior tests |

### Acceptance criteria

- [ ] Password is never stored as plain text.
- [ ] Correct password verification returns True.
- [ ] Incorrect password verification returns False.
- [ ] Password change requires authentication.
- [ ] Reset request page loads.
- [ ] Console email is generated for an eligible test account.
- [ ] Valid reset link allows a new password.
- [ ] Invalid link is rejected.
- [ ] Generic confirmation wording does not reveal account existence.
- [ ] Automated tests pass.
- [ ] No real reset token or password is submitted as evidence.

---

# PART 11 — SELF-ASSESSMENT

## 77. Short-answer questions

1. What is password hashing?
2. Why is hashing different from encryption?
3. What is a password salt?
4. What does set_password() do?
5. Why must save() be called after set_password()?
6. What does check_password() return?
7. Why is direct assignment to user.password unsafe?
8. What is a password validator?
9. Name four built-in password validators.
10. What is the difference between password change and reset?
11. What does PasswordChangeForm validate?
12. What is PasswordResetView used for?
13. What does the console email backend do?
14. What is a reset token?
15. Why should reset links be treated as sensitive?
16. Why should reset confirmation wording be neutral?
17. What is update_session_auth_hash() used for?
18. Why should production email credentials not be committed to Git?

## 78. Self-check answers

1. It converts a password into a one-way stored representation for verification.
2. Hashing is one-way; encryption is reversible with a key.
3. Random data used as part of password hashing.
4. It creates a Django-compatible password hash on the user instance.
5. save() persists the changed value to the database.
6. A Boolean indicating whether the candidate matches.
7. It bypasses the password hashing workflow.
8. A rule that checks whether a proposed password is acceptable.
9. Similarity, minimum length, common password and numeric password validators.
10. Change is normally for a signed-in user; reset is for a user who cannot sign in.
11. It checks the current password and validates the new password and confirmation.
12. It starts the account recovery workflow by generating a reset email.
13. It prints email content to the development terminal.
14. A time-sensitive proof used to validate a password reset link.
15. Anyone who obtains a valid link may be able to reset the account password.
16. It avoids revealing whether an email address belongs to an account.
17. It updates the current session's authentication hash after a password change.
18. Credentials in source control can be exposed to anyone with repository access.

## 79. MCQ assessment

### Question 1
Which method should change a user's password safely?

- A. user.password = value
- B. user.set_password(value)
- C. user.username = value
- D. user.save_password(value)

**Answer: B.** set_password() uses Django's password hashing mechanism.

### Question 2
What does check_password() return?

- A. A password string
- B. A Boolean
- C. An email
- D. A session ID

**Answer: B.** It indicates whether the candidate password matches.

### Question 3
Which Django view begins a password reset request?

- A. PasswordResetView
- B. PasswordAdminView
- C. UserDeleteView
- D. PasswordLoginView

**Answer: A.** It accepts the account email and starts the reset workflow.

### Question 4
What does the console email backend do?

- A. Sends real mail through a mailbox
- B. Prints email content to the terminal
- C. Stores passwords in the browser
- D. Disables password hashing

**Answer: B.** It is useful for local development and testing.

### Question 5
Why should reset tokens be protected?

- A. They are CSS values.
- B. They can be used to validate a password reset.
- C. They identify a template.
- D. They are database table names.

**Answer: B.** A valid reset token is part of the account recovery proof.

---

# PART 12 — INTERVIEW PREPARATION

## 80. Explain password hashing in Django

**Answer:** Django uses configured password hashers to store an encoded password representation instead of the original password. The application verifies a submitted password using the stored hash. Developers should use set_password(), create_user() and Django forms rather than assigning a raw value to the password field.

**Follow-up:** Can the application recover the original password from the stored hash?

**Answer:** No. It verifies a candidate password; it does not decrypt the stored hash.

## 81. What is the difference between password change and password reset?

**Answer:** Password change is normally performed by a signed-in user who can provide the current password. Password reset is for a user who cannot sign in and uses a time-limited recovery link sent to the registered email address.

**Follow-up:** Why does reset need a token?

**Answer:** The token proves that the reset link was generated by the application and is still valid.

## 82. What does PasswordResetView do?

**Answer:** It accepts an email address, identifies eligible accounts and generates reset instructions. Django's token and confirmation views validate the link and allow the user to choose a new password.

**Follow-up:** Does the console email backend send a real email?

**Answer:** No. It prints the message to the development terminal.

## 83. Scenario: a developer emails a forgotten password

**Answer:** This is unsafe because the application should not be able to recover the original password. It should use a reset workflow that lets the user set a new password after validating a time-limited link.

## 84. Scenario: reset request reveals that an email is not registered

**Answer:** The response reveals account existence. Use neutral confirmation wording so the same message is shown whether or not an eligible account is found.

## 85. Scenario: password changed but user is signed out

**Answer:** Review whether the built-in password change view is used or whether a custom view needs update_session_auth_hash(). Also consider that password reset may invalidate older sessions.

---

# PART 13 — INDEPENDENT COMPLETION

## 86. Explain the complete password lifecycle

Draw:
1. Registration.
2. Password validation.
3. Password hashing.
4. Database storage.
5. Login verification.
6. Password change.
7. Password reset request.
8. Reset token validation.
9. New password storage.

## 87. Controlled debugging

In a local practice environment:
- Try a weak password and read the validation error.
- Remove the email address from the test user and inspect reset behavior.
- Copy an incomplete reset URL and observe rejection.
- Restore the correct values and complete the reset flow.
- Verify the old password fails and the new password succeeds.

Never expose the reset URL or use a real account.

## 88. Final checklist

- [ ] I can explain hashing versus encryption.
- [ ] I can explain set_password() and check_password().
- [ ] I understand password validators.
- [ ] I can explain password change.
- [ ] I can explain password reset.
- [ ] I configured local console email.
- [ ] I understand reset tokens.
- [ ] I tested a valid reset.
- [ ] I tested an invalid reset.
- [ ] I protected reset links and credentials.
- [ ] I completed Password Recovery System.
- [ ] I ran the relevant tests.
- [ ] I completed the MCQs and interview questions.

**Next lesson:** Day 49 — Django Sessions, Cookies and Session Management.

---

## 89. Official references

1. Django password management: https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
2. Django built-in authentication views: https://docs.djangoproject.com/en/5.2/topics/auth/default/
3. Django email: https://docs.djangoproject.com/en/5.2/topics/email/
4. Django settings: https://docs.djangoproject.com/en/5.2/ref/settings/
5. Django testing: https://docs.djangoproject.com/en/5.2/topics/testing/

**Version reminder:** This lesson targets Django 5.2.19. Validate the built-in view configuration and all templates against the installed version before publishing.
