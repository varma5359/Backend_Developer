# Day 45: Database Constraints, Field Validation and Model Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–46 — Django fundamentals, ORM, forms and user concepts  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Data Integrity Management System

> **Trainer guidance:** Authentication and data integrity are important backend responsibilities. Use local test users and sample records. Never ask learners to paste real passwords, tokens or secret keys into code or shared screenshots.

## 1. Learning objectives

- Explain database constraints, field validation and model validation.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Test valid and invalid cases.
- Explain the security and data-integrity implications.
- Complete Data Integrity Management System.

## 2. Concept introduction

Database constraints protect data integrity at the database level. Field validators and model clean() provide application-level validation. UniqueConstraint and CheckConstraint express rules that should remain true for stored rows. Django does not automatically call full_clean() every time model.save() is used, so validation strategy must be deliberate.

## 3. File-by-file implementation

### profiles/models.py

```python
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

class Product(models.Model):
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    stock = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["sku"], name="unique_product_sku"),
            models.CheckConstraint(condition=Q(stock__gte=0), name="stock_non_negative"),
        ]

    def clean(self):
        super().clean()
        if self.name and self.name.strip() == "":
            from django.core.exceptions import ValidationError
            raise ValidationError({"name": "Name cannot be blank"})
```

### Validation example

```python
from django.core.exceptions import ValidationError
from profiles.models import Product

product = Product(sku="P100", name="Keyboard", price=799, stock=10)
try:
    product.full_clean()
    product.save()
except ValidationError as error:
    print(error.message_dict)
```

## 4. Explain the important statements

### profiles/models.py

1. `from django.core.validators import MinValueValidator` — Imports Django authentication, model or validation components.
2. `from django.db import models` — Imports Django authentication, model or validation components.
3. `from django.db.models import Q` — Imports Django authentication, model or validation components.
4. ` ` — Part of the example; explain its role in the complete workflow.
5. `class Product(models.Model):` — Defines a model or class.
6. `    sku = models.CharField(max_length=30)` — Part of the example; explain its role in the complete workflow.
7. `    name = models.CharField(max_length=120)` — Part of the example; explain its role in the complete workflow.
8. `    price = models.DecimalField(` — Part of the example; explain its role in the complete workflow.
9. `        max_digits=10,` — Part of the example; explain its role in the complete workflow.
10. `        decimal_places=2,` — Part of the example; explain its role in the complete workflow.
11. `        validators=[MinValueValidator(0.01)]` — Part of the example; explain its role in the complete workflow.
12. `    )` — Part of the example; explain its role in the complete workflow.
13. `    stock = models.IntegerField(default=0)` — Part of the example; explain its role in the complete workflow.
14. ` ` — Part of the example; explain its role in the complete workflow.
15. `    class Meta:` — Defines a model or class.
16. `        constraints = [` — Part of the example; explain its role in the complete workflow.
17. `            models.UniqueConstraint(fields=["sku"], name="unique_product_sku"),` — Declares a database-level integrity rule.
18. `            models.CheckConstraint(condition=Q(stock__gte=0), name="stock_non_negative"),` — Declares a database-level integrity rule.
19. `        ]` — Part of the example; explain its role in the complete workflow.
20. ` ` — Part of the example; explain its role in the complete workflow.
21. `    def clean(self):` — Defines a view or validation method.
22. `        super().clean()` — Part of the example; explain its role in the complete workflow.
23. `        if self.name and self.name.strip() == "":` — Part of the example; explain its role in the complete workflow.
24. `            from django.core.exceptions import ValidationError` — Imports Django authentication, model or validation components.
25. `            raise ValidationError({"name": "Name cannot be blank"})` — Part of the example; explain its role in the complete workflow.

### Validation example

1. `from django.core.exceptions import ValidationError` — Imports Django authentication, model or validation components.
2. `from profiles.models import Product` — Imports Django authentication, model or validation components.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `product = Product(sku="P100", name="Keyboard", price=799, stock=10)` — Part of the example; explain its role in the complete workflow.
5. `try:` — Part of the example; explain its role in the complete workflow.
6. `    product.full_clean()` — Runs model field and model-level validation.
7. `    product.save()` — Part of the example; explain its role in the complete workflow.
8. `except ValidationError as error:` — Part of the example; explain its role in the complete workflow.
9. `    print(error.message_dict)` — Part of the example; explain its role in the complete workflow.

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

Database constraints protect data integrity at the database level. Field validators and model clean() provide application-level validation. UniqueConstraint and CheckConstraint express rules that should remain true for stored rows. Django does not automatically call full_clean() every time model.save() is used, so validation strategy must be deliberate.

## 9. Approved mini-project — Data Integrity Management System

**Objective:** Data Integrity Management System.

### Required tasks

1. Identify the business rules that must always hold.
2. Add field validators for individual field values.
3. Add a UniqueConstraint for unique business identifiers.
4. Add a CheckConstraint for a database-level condition.
5. Override clean() for model-wide business validation where appropriate.
6. Call full_clean() explicitly in the demonstration before save.
7. Test duplicate and invalid values.
8. Explain why database constraints are still important.

### Suggested structure

```text
projects/day_45/
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

- [ ] Duplicate SKU is rejected.
- [ ] Negative stock is rejected by the database constraint.
- [ ] Invalid price fails field validation.
- [ ] Model clean() rejects whitespace-only names.
- [ ] The learner understands save() does not automatically call full_clean().

### Submission evidence

- Source code and URL patterns.
- Registration and login screenshots using test accounts.
- Valid and invalid test results.
- Database evidence showing safe user creation.
- README with setup instructions and security notes.
- No passwords, access tokens or private data in the repository.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Data Integrity Management System. List the forms, views, URLs, templates, validation rules and test cases. Do not provide a complete solution."

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

**Q1. Explain database constraints, field validation and model validation.**  
**Answer:** Database constraints protect data integrity at the database level. Field validators and model clean() provide application-level validation. UniqueConstraint and CheckConstraint express rules that should remain true for stored rows. Django does not automatically call full_clean() every time model.save() is used, so validation strategy must be deliberate.

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
- [ ] Complete Data Integrity Management System.
- [ ] Review security notes.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence without secrets.

**Next lesson:** Day 46.
