# Day 37: Django ORM Fundamentals and Querying Records

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–37 as applicable; review Django projects, models and migrations  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Product Query Explorer

> **Trainer guidance:** Show the exact file or shell first. Ask the learner to run each command, read the output and explain what it proves. Do not skip migrations or database checks.

## 1. Learning objectives

- Explain django orm fundamentals and querying records.
- Identify the Django component responsible for the feature.
- Implement the example step by step.
- Explain the resulting database or admin behavior.
- Handle common errors.
- Complete Product Query Explorer.

## 2. Concept introduction

The Django ORM lets Python code interact with database records through model classes and QuerySets. A QuerySet represents a database query and is generally evaluated when its results are needed. ORM methods such as all(), filter(), exclude(), get(), order_by() and values() help retrieve records.

## 3. File-by-file implementation

### Django shell

```bash
python manage.py shell
```

### Shell examples

```bash
from profiles.models import Employee

# Retrieve all employees
Employee.objects.all()

# Filter by department
Employee.objects.filter(department="ENG")

# Exclude inactive employees
Employee.objects.exclude(is_active=False)

# Get exactly one record by unique code
Employee.objects.get(employee_code="EMP101")

# Sort by name
Employee.objects.order_by("full_name")

# Return selected fields as dictionaries
Employee.objects.values("employee_code", "full_name")
```

## 4. Explain the code and commands

### Django shell

1. `python manage.py shell` — Runs a Django management command.

### Shell examples

1. `from profiles.models import Employee` — Imports a Django component or model.
2. ` ` — Part of the configuration; understand its role in the complete feature.
3. `# Retrieve all employees` — Part of the configuration; understand its role in the complete feature.
4. `Employee.objects.all()` — Uses the Django ORM manager to build or evaluate a query.
5. ` ` — Part of the configuration; understand its role in the complete feature.
6. `# Filter by department` — Part of the configuration; understand its role in the complete feature.
7. `Employee.objects.filter(department="ENG")` — Uses the Django ORM manager to build or evaluate a query.
8. ` ` — Part of the configuration; understand its role in the complete feature.
9. `# Exclude inactive employees` — Part of the configuration; understand its role in the complete feature.
10. `Employee.objects.exclude(is_active=False)` — Uses the Django ORM manager to build or evaluate a query.
11. ` ` — Part of the configuration; understand its role in the complete feature.
12. `# Get exactly one record by unique code` — Part of the configuration; understand its role in the complete feature.
13. `Employee.objects.get(employee_code="EMP101")` — Uses the Django ORM manager to build or evaluate a query.
14. ` ` — Part of the configuration; understand its role in the complete feature.
15. `# Sort by name` — Part of the configuration; understand its role in the complete feature.
16. `Employee.objects.order_by("full_name")` — Uses the Django ORM manager to build or evaluate a query.
17. ` ` — Part of the configuration; understand its role in the complete feature.
18. `# Return selected fields as dictionaries` — Part of the configuration; understand its role in the complete feature.
19. `Employee.objects.values("employee_code", "full_name")` — Uses the Django ORM manager to build or evaluate a query.

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

The Django ORM lets Python code interact with database records through model classes and QuerySets. A QuerySet represents a database query and is generally evaluated when its results are needed. ORM methods such as all(), filter(), exclude(), get(), order_by() and values() help retrieve records.

## 9. Approved mini-project — Product Query Explorer

**Objective:** Product Query Explorer.

### Required tasks

1. Run python manage.py shell from the project folder.
2. Import the Employee model.
3. Inspect all() and understand that it returns a QuerySet.
4. Use filter() with an exact field value.
5. Use exclude() to remove matching records.
6. Use get() for a record expected to match exactly one row and understand DoesNotExist/MultipleObjectsReturned.
7. Use order_by() to sort results.
8. Use values() to return selected fields as dictionaries.
9. Compare the ORM query with the SQL concept it represents.

### Suggested structure

```text
projects/day_37/
├── README.md
├── manage.py
└── application/
    ├── models.py
    ├── admin.py
    └── migrations/
```

### Validation checklist

- [ ] The model imports successfully.
- [ ] all() returns a QuerySet.
- [ ] filter() returns matching rows.
- [ ] get() handles zero/multiple match cases appropriately.
- [ ] order_by() sorts as requested.
- [ ] values() returns dictionaries with selected keys.

### Submission evidence

- Updated model/admin code.
- Migration files where required.
- Terminal output.
- Admin screenshots or ORM query results.
- README with setup and explanation.
- At least three validation cases.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Product Query Explorer. List the model/admin/query changes, commands, expected outputs and tests. Do not provide a complete solution."

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

**Q1. Explain django orm fundamentals and querying records.**  
**Answer:** The Django ORM lets Python code interact with database records through model classes and QuerySets. A QuerySet represents a database query and is generally evaluated when its results are needed. ORM methods such as all(), filter(), exclude(), get(), order_by() and values() help retrieve records.

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
- [ ] Complete Product Query Explorer.
- [ ] Test normal and invalid cases.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence.

**Next lesson:** Day 38.
