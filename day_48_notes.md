# Day 48: Password Management, Password Reset and Secure Password Storage

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–49 — Django fundamentals, models, forms and authentication basics  
**Tools:** Python, Django, VS Code, terminal, browser and local test accounts  
**Approved mini-project:** Password Recovery System

> **Security reminder:** Use fake users and test data. Never paste real passwords, reset tokens, session cookies or private credentials into source control or shared messages.

## 1. Learning objectives

- Explain password management, password reset and secure password storage.
- Identify the Django APIs and settings involved.
- Implement the example step by step.
- Explain the security implications.
- Test both permitted and denied workflows.
- Complete Password Recovery System.

## 2. Concept introduction

Django stores passwords using configured password hashers, not as readable plaintext. set_password() hashes a new password and check_password() verifies a candidate. Django includes password change and reset views/forms that can be configured with templates and email delivery.

## 3. File-by-file implementation

### Password API example

```python
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(username="asha")

# Set a password through Django's hashing API
user.set_password("Local-Test-Password-123")
user.save()

# Verify a candidate password
print(user.check_password("Local-Test-Password-123"))
```

### config/urls.py — built-in password views

```python
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change_form.html",
            success_url="/password-change/done/"
        ),
        name="password_change",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"
        ),
        name="password_reset",
    ),
]
```

## 4. Explain the important statements

### Password API example

1. `from django.contrib.auth import get_user_model` — Imports Django authentication, session or model utilities.
2. ` ` — Part of the example; explain its role in the security workflow.
3. `User = get_user_model()` — Part of the example; explain its role in the security workflow.
4. `user = User.objects.get(username="asha")` — Part of the example; explain its role in the security workflow.
5. ` ` — Part of the example; explain its role in the security workflow.
6. `# Set a password through Django's hashing API` — Part of the example; explain its role in the security workflow.
7. `user.set_password("Local-Test-Password-123")` — Stores a password using Django's configured hashing mechanism.
8. `user.save()` — Part of the example; explain its role in the security workflow.
9. ` ` — Part of the example; explain its role in the security workflow.
10. `# Verify a candidate password` — Part of the example; explain its role in the security workflow.
11. `print(user.check_password("Local-Test-Password-123"))` — Checks a candidate password against the stored hash.

### config/urls.py — built-in password views

1. `from django.contrib.auth import views as auth_views` — Imports Django authentication, session or model utilities.
2. `from django.urls import path` — Imports Django authentication, session or model utilities.
3. ` ` — Part of the example; explain its role in the security workflow.
4. `urlpatterns = [` — Part of the example; explain its role in the security workflow.
5. `    path(` — Part of the example; explain its role in the security workflow.
6. `        "password-change/",` — Part of the example; explain its role in the security workflow.
7. `        auth_views.PasswordChangeView.as_view(` — Part of the example; explain its role in the security workflow.
8. `            template_name="registration/password_change_form.html",` — Part of the example; explain its role in the security workflow.
9. `            success_url="/password-change/done/"` — Part of the example; explain its role in the security workflow.
10. `        ),` — Part of the example; explain its role in the security workflow.
11. `        name="password_change",` — Part of the example; explain its role in the security workflow.
12. `    ),` — Part of the example; explain its role in the security workflow.
13. `    path(` — Part of the example; explain its role in the security workflow.
14. `        "password-reset/",` — Part of the example; explain its role in the security workflow.
15. `        auth_views.PasswordResetView.as_view(` — Part of the example; explain its role in the security workflow.
16. `            template_name="registration/password_reset_form.html"` — Part of the example; explain its role in the security workflow.
17. `        ),` — Part of the example; explain its role in the security workflow.
18. `        name="password_reset",` — Part of the example; explain its role in the security workflow.
19. `    ),` — Part of the example; explain its role in the security workflow.
20. `]` — Part of the example; explain its role in the security workflow.

## 5. Important security concepts

| Concept | What it protects |
|---|---|
| Password hashing | Avoids storing readable passwords |
| Password validation | Rejects weak or unsuitable passwords |
| Reset token | Provides a controlled password reset workflow |
| Session | Associates requests with server-side user state |
| HttpOnly cookie | Prevents ordinary client-side scripts from reading the cookie |
| Secure cookie | Restricts cookie transmission to HTTPS |
| CSRF token | Helps protect browser POST requests |
| Permission | Defines an allowed action |
| Group | Collects users and permissions into a role-like set |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Password check fails | Confirm set_password() was used and the saved user was refreshed |
| Reset email not sent | Email backend and environment settings |
| Session data disappears | Session middleware, cookie and session backend |
| Cart does not update | POST method, session assignment and modified flag |
| User can access restricted page | View decorator and permission check |
| User sees 403 unexpectedly | Group membership and assigned permission |
| Secure cookie missing in local HTTP | Secure flag requires HTTPS; configure by environment |

## 7. Industry scenario

Django stores passwords using configured password hashers, not as readable plaintext. set_password() hashes a new password and check_password() verifies a candidate. Django includes password change and reset views/forms that can be configured with templates and email delivery.

## 8. Approved mini-project — Password Recovery System

**Objective:** Password Recovery System.

### Required tasks

1. Explain password hashing and why plaintext storage is unsafe.
2. Use set_password() when setting a password programmatically.
3. Use check_password() to verify a candidate password.
4. Inspect Django's password validation settings.
5. Understand built-in password change and reset views.
6. Configure email backend for local development and production separately.
7. Use generic user-facing reset messages to avoid account enumeration.
8. Test valid, invalid and expired reset workflows.

### Suggested structure

```text
projects/day_48/
├── README.md
├── config/
└── application/
    ├── views.py
    ├── urls.py
    ├── templates/
    └── tests/
```

### Validation checklist

- [ ] Password is stored as a hash.
- [ ] check_password() verifies the expected value.
- [ ] Raw password is never stored or logged.
- [ ] Password validators are configured.
- [ ] Password reset flow does not reveal whether an email is registered.
- [ ] Email configuration is environment-specific.

### Submission evidence

- Source files and settings relevant to the task.
- Screenshots from local test accounts.
- Valid and denied access test results.
- README with setup and security decisions.
- No passwords, reset tokens or session cookies in evidence.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Password Recovery System. Identify views, settings, URL patterns, templates, security controls and test cases. Do not provide the complete implementation."

**Guided prompt:** "Help me implement one safe workflow at a time. Explain the security setting and wait for my test result."

**Debugging prompt:** "Here is my local test configuration and error. Diagnose the issue without asking me to share real credentials, tokens or cookies."

**Review prompt:** "Review the feature for password handling, session security, authorization and negative test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Securely manage credentials, sessions or access rights.  
B. Replace HTTP.  
C. Store secrets in HTML.  
D. Disable authentication.  
**Answer: A.** These controls protect user identity and application data.

**Q2. What should never be committed to Git?**  
A. A README.  
B. A real password, reset token or session cookie.  
C. A test case.  
D. A public CSS file.  
**Answer: B.** Credentials and session secrets must remain private.

**Q3. Which check should protect a sensitive operation?**  
A. Hiding the button only.  
B. A CSS class.  
C. Server-side authentication and authorization.  
D. A comment in the code.  
**Answer: C.** Security decisions must be enforced on the server.

**Q4. What is a safe way to test access?**  
A. Use a real customer's account.  
B. Share a session cookie.  
C. Disable all permissions.  
D. Use separate local test users with different permissions.  
**Answer: D.** Test accounts allow controlled positive and negative tests.

**Q5. What is the best evidence of completion?**  
A. Verified permitted and denied workflows.  
B. A login page screenshot only.  
C. A project folder only.  
D. A code snippet with no test.  
**Answer: A.** Security behavior requires both positive and negative testing.

## 11. Interview preparation

**Q1. Explain password management, password reset and secure password storage.**  
**Answer:** Django stores passwords using configured password hashers, not as readable plaintext. set_password() hashes a new password and check_password() verifies a candidate. Django includes password change and reset views/forms that can be configured with templates and email delivery.

**Q2. What is one security mistake to avoid?**  
**Answer:** Do not expose passwords, tokens or session identifiers. Do not rely on frontend-only checks for access control.

**Q3. How do you verify the feature?**  
**Answer:** Use local test accounts with different states and permissions. Test allowed and denied requests and inspect the server-side result.

**Follow-up:** Why is hiding a link not sufficient authorization?  
**Answer:** A user can send a direct request to the URL. The view must enforce the permission on the server.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid workflows.
- [ ] Verify security settings and access checks.
- [ ] Complete Password Recovery System.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 49.
