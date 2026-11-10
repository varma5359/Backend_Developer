# Day 36: Django Admin Panel and Model Registration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–37 as applicable; review Django projects, models and migrations  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Admin-Based Inventory Manager

> **Trainer guidance:** Show the exact file or shell first. Ask the learner to run each command, read the output and explain what it proves. Do not skip migrations or database checks.

## 1. Learning objectives

- Explain django admin panel and model registration.
- Identify the Django component responsible for the feature.
- Implement the example step by step.
- Explain the resulting database or admin behavior.
- Handle common errors.
- Complete Admin-Based Inventory Manager.

## 2. Concept introduction

Django Admin is a built-in interface for trusted staff to manage registered models. A model becomes available in the admin site after it is registered with an admin site. The admin interface uses Django authentication and permissions; it should not be exposed carelessly.

## 3. File-by-file implementation

### profiles/admin.py

```python
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "full_name", "department", "is_active")
    search_fields = ("employee_code", "full_name", "email")
    list_filter = ("department", "is_active")
    ordering = ("full_name",)
```

### Terminal commands

```bash
python manage.py createsuperuser
python manage.py runserver
# Open http://127.0.0.1:8000/admin/
```

## 4. Explain the code and commands

### profiles/admin.py

1. `from django.contrib import admin` — Imports a Django component or model.
2. `from .models import Employee` — Imports a Django component or model.
3. ` ` — Part of the configuration; understand its role in the complete feature.
4. `@admin.register(Employee)` — Registers the model with Django Admin.
5. `class EmployeeAdmin(admin.ModelAdmin):` — Defines a model or admin configuration class.
6. `    list_display = ("employee_code", "full_name", "department", "is_active")` — Selects columns shown in the admin changelist.
7. `    search_fields = ("employee_code", "full_name", "email")` — Part of the configuration; understand its role in the complete feature.
8. `    list_filter = ("department", "is_active")` — Part of the configuration; understand its role in the complete feature.
9. `    ordering = ("full_name",)` — Part of the configuration; understand its role in the complete feature.

### Terminal commands

1. `python manage.py createsuperuser` — Runs a Django management command.
2. `python manage.py runserver` — Runs a Django management command.
3. `# Open http://127.0.0.1:8000/admin/` — Part of the configuration; understand its role in the complete feature.

## 5. Practical verification

1. Activate the virtual environment.
2. Change to the folder containing manage.py.
3. Run `python manage.py check`.
4. Execute the shell or admin commands.
5. Inspect the resulting object, record or admin page.
6. Test an invalid or missing-record case.
7. Record the result in the README.

## 6. Important terms

| Term | Meaning |
|---|---|
| Model | Python class describing database-backed data |
| Manager | Entry point for model-level database operations, commonly objects |
| QuerySet | A collection-like representation of a database query |
| Admin registration | Making a model available in Django Admin |
| ForeignKey | Many-to-one relationship |
| OneToOneField | One-to-one relationship |
| ManyToManyField | Many-to-many relationship |
| on_delete | Defines behavior when a referenced object is deleted |

## 7. Common errors

| Symptom | What to inspect |
|---|---|
| Model missing in admin | Import and register the model in admin.py |
| Login fails | Superuser credentials and authentication configuration |
| ImportError | App name and model class name |
| DoesNotExist | Query matched no records |
| MultipleObjectsReturned | get() matched more than one record |
| Relationship migration error | Model references, app labels and migration order |
| Cannot delete related object | on_delete behavior and existing related records |

## 8. Industry scenario

Django Admin is a built-in interface for trusted staff to manage registered models. A model becomes available in the admin site after it is registered with an admin site. The admin interface uses Django authentication and permissions; it should not be exposed carelessly.

## 9. Approved mini-project — Admin-Based Inventory Manager

**Objective:** Admin-Based Inventory Manager.

### Required tasks

1. Confirm Employee is defined in profiles/models.py.
2. Open profiles/admin.py.
3. Import django.contrib.admin and Employee.
4. Register Employee using admin.site.register or @admin.register.
5. Add list_display to show useful columns.
6. Add search_fields and list_filter.
7. Create a superuser using the management command.
8. Start the development server and sign in at /admin/.
9. Create, update and delete a sample record in the admin interface.

### Suggested structure

```text
projects/day_36/
├── README.md
├── manage.py
└── application/
    ├── models.py
    ├── admin.py
    └── migrations/
```

### Validation checklist

- [ ] Employee appears in the admin index.
- [ ] A superuser can sign in.
- [ ] List display shows the selected fields.
- [ ] Search and filters work.
- [ ] A created record is visible in the database-backed admin list.

### Submission evidence

- Updated model/admin code.
- Migration files where required.
- Terminal output.
- Admin screenshots or ORM query results.
- README with setup and explanation.
- At least three validation cases.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Admin-Based Inventory Manager. List the model/admin/query changes, commands, expected outputs and tests. Do not provide a complete solution."

**Guided prompt:** "Explain the next file and show one small change. Wait for my output before continuing."

**Debugging prompt:** "Here is my model, admin registration or ORM query and exact traceback. Explain the root cause and the smallest correction."

**Review prompt:** "Review my implementation for correctness, relationship behavior, query results and maintainability."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's Django feature?**  
A. Provide structured access to application records or management functions.  
B. Replace the Python language.  
C. Remove the database.  
D. Disable security.  
**Answer: A.** The feature supports structured data management.

**Q2. What should you do when a model is not visible?**  
A. Delete the app.  
B. Check imports, registration, installed apps and migrations as appropriate.  
C. Ignore it.  
D. Reinstall the browser.  
**Answer: B.** Check the Django model and configuration path.

**Q3. Which practice helps prevent incorrect database changes?**  
A. Never inspect queries.  
B. Delete migration files.  
C. Test with sample records and verify the result.  
D. Commit passwords.  
**Answer: C.** Always verify database behavior.

**Q4. What should you do if get() returns no record?**  
A. Assume the query succeeded.  
B. Delete the model.  
C. Ignore the exception.  
D. Handle DoesNotExist or use a query method suited to the requirement.  
**Answer: D.** get() expects one matching record.

**Q5. What is the strongest evidence of completion?**  
A. Verified admin or ORM behavior with test cases.  
B. A folder exists.  
C. A screenshot of code only.  
D. A project title.  
**Answer: A.** Verify the actual behavior.

## 12. Interview preparation

**Q1. Explain django admin panel and model registration.**  
**Answer:** Django Admin is a built-in interface for trusted staff to manage registered models. A model becomes available in the admin site after it is registered with an admin site. The admin interface uses Django authentication and permissions; it should not be exposed carelessly.

**Q2. Which files and commands are important?**  
**Answer:** Explain the model, admin or ORM shell example and the relevant management commands.

**Q3. How would you test the feature?**  
**Answer:** Create sample records, verify the expected relationship/query/admin result, test a missing or invalid case and document the output.

**Follow-up:** What is one production concern?  
**Answer:** Permissions, data integrity, query performance and safe migrations should be considered.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run Django system checks.
- [ ] Verify database or admin behavior.
- [ ] Complete Admin-Based Inventory Manager.
- [ ] Test normal and invalid cases.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence.

**Next lesson:** Day 37.
