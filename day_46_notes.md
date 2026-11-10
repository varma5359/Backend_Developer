# Day 46: Django Authentication System and User Model

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–46 — Django fundamentals, ORM, forms and user concepts  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** User Account Management

> **Trainer guidance:** Authentication and data integrity are important backend responsibilities. Use local test users and sample records. Never ask learners to paste real passwords, tokens or secret keys into code or shared screenshots.

## 1. Learning objectives

- Explain django authentication system and user model.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Test valid and invalid cases.
- Explain the security and data-integrity implications.
- Complete User Account Management.

## 2. Concept introduction

Django authentication identifies users and supports password verification, sessions and permissions. The built-in user model includes fields such as username, password hash, email and staff/superuser flags. Use get_user_model() when application code needs the active user model, and settings.AUTH_USER_MODEL for model relationship declarations.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

def user_summary(request):
    total_users = User.objects.count()
    return render(
        request,
        "profiles/user_summary.html",
        {"total_users": total_users}
    )
```

### Model relationship example

```python
from django.conf import settings
from django.db import models

class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile"
    )
    department = models.CharField(max_length=80)
```

## 4. Explain the important statements

### profiles/views.py

1. `from django.contrib.auth import get_user_model` — Imports Django authentication, model or validation components.
2. `from django.shortcuts import render` — Imports Django authentication, model or validation components.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `User = get_user_model()` — Gets the active user model configured for the project.
5. ` ` — Part of the example; explain its role in the complete workflow.
6. `def user_summary(request):` — Defines a view or validation method.
7. `    total_users = User.objects.count()` — Part of the example; explain its role in the complete workflow.
8. `    return render(` — Part of the example; explain its role in the complete workflow.
9. `        request,` — Part of the example; explain its role in the complete workflow.
10. `        "profiles/user_summary.html",` — Part of the example; explain its role in the complete workflow.
11. `        {"total_users": total_users}` — Part of the example; explain its role in the complete workflow.
12. `    )` — Part of the example; explain its role in the complete workflow.

### Model relationship example

1. `from django.conf import settings` — Imports Django authentication, model or validation components.
2. `from django.db import models` — Imports Django authentication, model or validation components.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `class EmployeeProfile(models.Model):` — Defines a model or class.
5. `    user = models.OneToOneField(` — Part of the example; explain its role in the complete workflow.
6. `        settings.AUTH_USER_MODEL,` — Part of the example; explain its role in the complete workflow.
7. `        on_delete=models.CASCADE,` — Part of the example; explain its role in the complete workflow.
8. `        related_name="employee_profile"` — Part of the example; explain its role in the complete workflow.
9. `    )` — Part of the example; explain its role in the complete workflow.
10. `    department = models.CharField(max_length=80)` — Part of the example; explain its role in the complete workflow.

## 5. Important concepts and distinctions

| Concept | Meaning |
|---|---|
| Validation | Checks whether supplied data satisfies rules |
| Constraint | Database rule protecting stored data |
| Authentication | Verifies who the user is |
| Authorization | Determines what the user is allowed to do |
| Password hash | One-way derived representation used for password verification |
| Session | Server-managed state associated with a browser session |
| Anonymous user | Request that is not authenticated |
| Superuser | User with broad administrative permissions |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Duplicate value saved | Unique constraint and validation |
| Invalid value accepted | Field validator, full_clean and database constraint |
| Password stored incorrectly | Use create_user() or set_password() |
| Login always fails | Username, password, authentication backend and user state |
| Protected page accessible | login_required and view authorization |
| Logout does not work | POST method, URL and session configuration |
| User model import mismatch | get_user_model() and AUTH_USER_MODEL |

## 7. Security and reliability notes

- Never store raw passwords.
- Use Django's password management APIs.
- Keep CSRF protection enabled for browser POST forms.
- Protect views that contain private data.
- Authentication does not automatically grant permission to every record.
- Do not expose account existence or sensitive authentication details unnecessarily.
- Keep secret keys and database credentials outside source control.
- Use HTTPS in production.

## 8. Industry scenario

Django authentication identifies users and supports password verification, sessions and permissions. The built-in user model includes fields such as username, password hash, email and staff/superuser flags. Use get_user_model() when application code needs the active user model, and settings.AUTH_USER_MODEL for model relationship declarations.

## 9. Approved mini-project — User Account Management

**Objective:** User Account Management.

### Required tasks

1. Inspect Django's built-in authentication app in INSTALLED_APPS.
2. Understand the default User fields and password hashing.
3. Use get_user_model() in application code that needs the active model class.
4. Use settings.AUTH_USER_MODEL in model relationships.
5. Create a user through create_user() rather than setting a raw password field.
6. Distinguish regular user, staff user and superuser.
7. Explain authentication versus authorization.

### Suggested structure

```text
projects/day_46/
├── README.md
├── config/
└── profiles/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
```

### Validation checklist

- [ ] Authentication app is installed.
- [ ] A user can be created using create_user().
- [ ] Password is stored as a hash, not plaintext.
- [ ] get_user_model() resolves the active model.
- [ ] The learner distinguishes authenticated users from authorized users.

### Submission evidence

- Source code and URL patterns.
- Registration and login screenshots using test accounts.
- Valid and invalid test results.
- Database evidence showing safe user creation.
- README with setup instructions and security notes.
- No passwords, access tokens or private data in the repository.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan User Account Management. List the forms, views, URLs, templates, validation rules and test cases. Do not provide a complete solution."

**Guided prompt:** "Guide me through one authentication or validation step at a time. Explain the security implications and wait for my test result."

**Debugging prompt:** "Here are my exact view, form, settings and error. Identify the cause without asking me to share any real password or secret."

**Review prompt:** "Review this local test implementation for validation, authentication, authorization, CSRF and secret handling."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Protect data integrity or manage user identity securely.  
B. Replace HTTP.  
C. Store passwords as plaintext.  
D. Disable database constraints.  
**Answer: A.** The feature protects application data and user workflows.

**Q2. What should be used for password creation?**  
A. Store raw password in a text field.  
B. Django's create_user() or set_password() API.  
C. Put the password in settings.py.  
D. Commit the password to Git.  
**Answer: B.** Django provides password hashing APIs.

**Q3. What is the difference between authentication and authorization?**  
A. They mean the same thing.  
B. Authentication is database sorting.  
C. Authentication verifies identity; authorization checks permissions.  
D. Authorization creates passwords.  
**Answer: C.** They are separate security decisions.

**Q4. What should happen before data is saved?**  
A. Ignore all validation.  
B. Disable constraints.  
C. Trust the browser.  
D. Validate the data and enforce important integrity rules.  
**Answer: D.** Validation and constraints protect data.

**Q5. What is the strongest evidence of completion?**  
A. Valid and invalid workflows are tested and security rules are explained.  
B. A project title only.  
C. A long code file.  
D. A screenshot of the login button.  
**Answer: A.** Test behavior and explain security choices.

## 12. Interview preparation

**Q1. Explain django authentication system and user model.**  
**Answer:** Django authentication identifies users and supports password verification, sessions and permissions. The built-in user model includes fields such as username, password hash, email and staff/superuser flags. Use get_user_model() when application code needs the active user model, and settings.AUTH_USER_MODEL for model relationship declarations.

**Q2. What is one security risk?**  
**Answer:** Explain the relevant risk such as unsafe password handling, missing authorization, missing CSRF protection or invalid data reaching the database.

**Q3. How do you verify the workflow?**  
**Answer:** Use test accounts and test records. Exercise valid and invalid cases, inspect the session or database result and verify access restrictions.

**Follow-up:** Why is a successful login not proof of authorization?  
**Answer:** Authentication proves identity; authorization must still check whether that user has permission for the requested operation or record.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid cases.
- [ ] Verify data or session behavior.
- [ ] Complete User Account Management.
- [ ] Review security notes.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence without secrets.

**Next lesson:** Day 47.
