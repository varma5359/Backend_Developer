# Day 51: Custom User Models and User Profile Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–53 — Django fundamentals, ORM, forms, users and access control  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Custom User Profile System

> **Trainer guidance:** Explain the relationship between each file and the user journey. Show the learner how to verify the behavior using separate test accounts and sample records.

## 1. Learning objectives

- Explain custom user models and user profile management.
- Identify the Django components and settings involved.
- Implement the example step by step.
- Test normal, invalid and unauthorized cases.
- Explain one design or security decision.
- Complete Custom User Profile System.

## 2. Concept introduction

A custom user model lets a project define its user identity fields and authentication behavior. Django recommends deciding whether to use a custom user model at the start of a project. Set AUTH_USER_MODEL before the first migrations that create user-related tables. Changing user models after a project has already migrated can require complex data and migration work.

## Important migration timing — read before changing settings

The main pathway project already has Django migrations from earlier lessons. Do **not** casually switch that existing database from Django's default user model to a custom user model at Day 51. Changing AUTH_USER_MODEL after tables and relationships have already been created can require complex schema and data migrations.

For this lesson, create a **separate fresh practice project** named `custom_user_demo`, or use a clean branch and a new empty database. Configure `AUTH_USER_MODEL = "accounts.User"` before running the first migrations in that practice project. Keep the existing Job Portal and main pathway project using the user model it was initialized with.

## 3. File-by-file implementation

### accounts/models.py

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    display_name = models.CharField(max_length=100, blank=True)
```

### profiles/models.py

```python
from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=80, blank=True)
```

### config/settings.py

```python
INSTALLED_APPS = [
    # Django applications...
    "accounts",
    "profiles",
]

AUTH_USER_MODEL = "accounts.User"
```

## 4. Understand the important statements

### accounts/models.py

1. `from django.contrib.auth.models import AbstractUser` — Imports Django components or the active user model setting.
2. `from django.db import models` — Imports Django components or the active user model setting.
3. ` ` — Part of the implementation; explain its role in the overall workflow.
4. `class User(AbstractUser):` — Defines a model, form or class.
5. `    display_name = models.CharField(max_length=100, blank=True)` — Part of the implementation; explain its role in the overall workflow.

### profiles/models.py

1. `from django.conf import settings` — Imports Django components or the active user model setting.
2. `from django.db import models` — Imports Django components or the active user model setting.
3. ` ` — Part of the implementation; explain its role in the overall workflow.
4. `class UserProfile(models.Model):` — Defines a model, form or class.
5. `    user = models.OneToOneField(` — Links one profile record to one user.
6. `        settings.AUTH_USER_MODEL,` — Part of the implementation; explain its role in the overall workflow.
7. `        on_delete=models.CASCADE,` — Part of the implementation; explain its role in the overall workflow.
8. `        related_name="profile"` — Part of the implementation; explain its role in the overall workflow.
9. `    )` — Part of the implementation; explain its role in the overall workflow.
10. `    phone = models.CharField(max_length=20, blank=True)` — Part of the implementation; explain its role in the overall workflow.
11. `    city = models.CharField(max_length=80, blank=True)` — Part of the implementation; explain its role in the overall workflow.

### config/settings.py

1. `INSTALLED_APPS = [` — Part of the implementation; explain its role in the overall workflow.
2. `    # Django applications...` — Part of the implementation; explain its role in the overall workflow.
3. `    "accounts",` — Part of the implementation; explain its role in the overall workflow.
4. `    "profiles",` — Part of the implementation; explain its role in the overall workflow.
5. `]` — Part of the implementation; explain its role in the overall workflow.
6. ` ` — Part of the implementation; explain its role in the overall workflow.
7. `AUTH_USER_MODEL = "accounts.User"` — Part of the implementation; explain its role in the overall workflow.

## 5. Integration flow

```text
Browser request
   ↓
URL pattern
   ↓
Authentication / permission check
   ↓
View
   ↓
Form validation
   ↓
ORM and database
   ↓
Messages / redirect / template
   ↓
Browser response
```

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| User model import error | AUTH_USER_MODEL and app registration |
| Duplicate record | Database constraint and user feedback |
| Message not visible | Messages middleware, context processor and template |
| Pagination loses search | Preserve query parameters in page links |
| Search results are inconsistent | Ordering and Q conditions |
| User can perform restricted action | Server-side authorization |
| Form accepts untrusted ownership fields | Set owner/applicant in the view from request.user |

## 7. Industry scenario

A custom user model lets a project define its user identity fields and authentication behavior. Django recommends deciding whether to use a custom user model at the start of a project. Set AUTH_USER_MODEL before the first migrations that create user-related tables. Changing user models after a project has already migrated can require complex data and migration work.

## 8. Approved mini-project — Custom User Profile System

**Objective:** Custom User Profile System.

### Required tasks

1. Explain why a project may need a custom user model.
2. Create the accounts app before the initial project migrations.
3. Define User inheriting from AbstractUser.
4. Set AUTH_USER_MODEL in settings.py before initial migrations.
5. Use settings.AUTH_USER_MODEL in relationship fields.
6. Create a separate UserProfile model for additional profile data.
7. Create migrations and apply them in a fresh learning database.
8. Use get_user_model() in application code.
9. Explain why changing user model later is difficult.

### Suggested structure

```text
projects/day_51/
├── manage.py
├── config/
└── jobs/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
```

### Validation checklist

- [ ] Custom user class inherits from AbstractUser.
- [ ] AUTH_USER_MODEL points to the correct app and class.
- [ ] User relationships use settings.AUTH_USER_MODEL.
- [ ] Profile is linked using OneToOneField.
- [ ] The learner understands that the custom model should be configured before initial migrations.

### Test matrix

| User or input | Expected behavior |
|---|---|
| Anonymous visitor | Public pages load; protected action redirects or denies |
| Authenticated user | Allowed action succeeds |
| Invalid form | Errors display; no record is saved |
| Duplicate submission | Constraint prevents duplicate data |
| Missing or inactive record | Not found or denied as appropriate |
| Valid workflow | Database and browser state agree |

### Submission evidence

- Source code and migrations.
- Screenshots of the main user journey.
- Test results for positive and negative cases.
- README with setup and architecture.
- Explanation of authorization and data integrity.
- No real user credentials or personal data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Custom User Profile System. Identify the models, forms, views, URLs, templates, permissions, migrations and test cases. Do not write the full project."

**Guided prompt:** "Guide me through one component at a time. Explain the file path and wait for my test result."

**Debugging prompt:** "Trace my user journey from URL to view to form to database. Identify where the behavior differs from the requirement."

**Review prompt:** "Review the project for integration correctness, duplicate handling, permissions, validation and test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Integrate multiple Django components into a complete user workflow.  
B. Replace the database.  
C. Remove authentication.  
D. Disable URL routing.  
**Answer: A.** Integration connects the individual components into a working feature.

**Q2. Where should the server get the identity of the logged-in applicant?**  
A. A hidden HTML field.  
B. request.user.  
C. A URL parameter supplied by the browser.  
D. A text box.  
**Answer: B.** Use the authenticated user supplied by Django.

**Q3. Why add a database uniqueness constraint?**  
A. To style a template.  
B. To create a URL.  
C. To enforce a rule even if multiple requests reach the database.  
D. To disable migrations.  
**Answer: C.** Database constraints protect integrity.

**Q4. What should an integration test cover?**  
A. Only one Python import.  
B. Only a screenshot.  
C. Only the model class.  
D. A realistic sequence across views, forms, authentication and database.  
**Answer: D.** Integration tests verify components working together.

**Q5. What is the strongest evidence of completion?**  
A. A tested end-to-end user journey with expected database state.  
B. A project folder only.  
C. A long code file.  
D. A list of planned features.  
**Answer: A.** Completion requires verified behavior.

## 11. Interview preparation

**Q1. Explain custom user models and user profile management.**  
**Answer:** A custom user model lets a project define its user identity fields and authentication behavior. Django recommends deciding whether to use a custom user model at the start of a project. Set AUTH_USER_MODEL before the first migrations that create user-related tables. Changing user models after a project has already migrated can require complex data and migration work.

**Q2. What is one important design decision?**  
**Answer:** Explain the relationship, constraint or server-side value assignment used in the implementation.

**Q3. How do you verify the full application?**  
**Answer:** Test the end-to-end user journey with anonymous and authenticated users, valid and invalid inputs and expected database state.

**Follow-up:** Why are integration tests necessary if unit tests pass?  
**Answer:** Unit tests check individual components; integration tests verify that those components work together correctly.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Identify all connected components.
- [ ] Implement the example.
- [ ] Test valid and invalid user journeys.
- [ ] Complete Custom User Profile System.
- [ ] Verify database state.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 52.
