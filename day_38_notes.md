# Day 38: Model Relationships: One-to-One, One-to-Many and Many-to-Many

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–37 as applicable; review Django projects, models and migrations  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** College Relationship Manager

> **Trainer guidance:** Show the exact file or shell first. Ask the learner to run each command, read the output and explain what it proves. Do not skip migrations or database checks.

## 1. Learning objectives

- Explain model relationships: one-to-one, one-to-many and many-to-many.
- Identify the Django component responsible for the feature.
- Implement the example step by step.
- Explain the resulting database or admin behavior.
- Handle common errors.
- Complete College Relationship Manager.

## 2. Concept introduction

Relational applications need to connect records. Django represents relationships using ForeignKey for many-to-one, OneToOneField for one-to-one and ManyToManyField for many-to-many relationships. These fields express database relationships and provide convenient ORM accessors.

## 3. File-by-file implementation

### profiles/models.py

```python
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=120)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees"
    )

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone = models.CharField(max_length=20)

class Course(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name="students")
```

## 4. Explain the code and commands

### profiles/models.py

1. `from django.db import models` — Imports a Django component or model.
2. ` ` — Part of the configuration; understand its role in the complete feature.
3. `class Department(models.Model):` — Defines a model or admin configuration class.
4. `    name = models.CharField(max_length=80, unique=True)` — Part of the configuration; understand its role in the complete feature.
5. ` ` — Part of the configuration; understand its role in the complete feature.
6. `    def __str__(self):` — Part of the configuration; understand its role in the complete feature.
7. `        return self.name` — Part of the configuration; understand its role in the complete feature.
8. ` ` — Part of the configuration; understand its role in the complete feature.
9. `class Employee(models.Model):` — Defines a model or admin configuration class.
10. `    full_name = models.CharField(max_length=120)` — Part of the configuration; understand its role in the complete feature.
11. `    department = models.ForeignKey(` — Creates a many-to-one database relationship.
12. `        Department,` — Part of the configuration; understand its role in the complete feature.
13. `        on_delete=models.PROTECT,` — Part of the configuration; understand its role in the complete feature.
14. `        related_name="employees"` — Part of the configuration; understand its role in the complete feature.
15. `    )` — Part of the configuration; understand its role in the complete feature.
16. ` ` — Part of the configuration; understand its role in the complete feature.
17. `class EmployeeProfile(models.Model):` — Defines a model or admin configuration class.
18. `    employee = models.OneToOneField(` — Creates a one-to-one database relationship.
19. `        Employee,` — Part of the configuration; understand its role in the complete feature.
20. `        on_delete=models.CASCADE,` — Part of the configuration; understand its role in the complete feature.
21. `        related_name="profile"` — Part of the configuration; understand its role in the complete feature.
22. `    )` — Part of the configuration; understand its role in the complete feature.
23. `    phone = models.CharField(max_length=20)` — Part of the configuration; understand its role in the complete feature.
24. ` ` — Part of the configuration; understand its role in the complete feature.
25. `class Course(models.Model):` — Defines a model or admin configuration class.
26. `    title = models.CharField(max_length=100)` — Part of the configuration; understand its role in the complete feature.
27. ` ` — Part of the configuration; understand its role in the complete feature.
28. `class Student(models.Model):` — Defines a model or admin configuration class.
29. `    name = models.CharField(max_length=100)` — Part of the configuration; understand its role in the complete feature.
30. `    courses = models.ManyToManyField(Course, related_name="students")` — Creates a many-to-many database relationship.

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

Relational applications need to connect records. Django represents relationships using ForeignKey for many-to-one, OneToOneField for one-to-one and ManyToManyField for many-to-many relationships. These fields express database relationships and provide convenient ORM accessors.

## 9. Approved mini-project — College Relationship Manager

**Objective:** College Relationship Manager.

### Required tasks

1. Create a Department model.
2. Add a ForeignKey from Employee to Department.
3. Explain that one department can be related to many employees.
4. Create EmployeeProfile with OneToOneField to Employee.
5. Explain that each employee has at most one profile in this relationship.
6. Create Course and Student models with ManyToManyField.
7. Run makemigrations and migrate.
8. Use the ORM to create and inspect related objects.

### Suggested structure

```text
projects/day_38/
├── README.md
├── manage.py
└── application/
    ├── models.py
    ├── admin.py
    └── migrations/
```

### Validation checklist

- [ ] ForeignKey expresses many employees to one department.
- [ ] OneToOneField links one profile to one employee.
- [ ] ManyToManyField links students and courses in both directions.
- [ ] on_delete behavior is understood.
- [ ] Migrations are created and applied.

### Submission evidence

- Updated model/admin code.
- Migration files where required.
- Terminal output.
- Admin screenshots or ORM query results.
- README with setup and explanation.
- At least three validation cases.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan College Relationship Manager. List the model/admin/query changes, commands, expected outputs and tests. Do not provide a complete solution."

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

**Q1. Explain model relationships: one-to-one, one-to-many and many-to-many.**  
**Answer:** Relational applications need to connect records. Django represents relationships using ForeignKey for many-to-one, OneToOneField for one-to-one and ManyToManyField for many-to-many relationships. These fields express database relationships and provide convenient ORM accessors.

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
- [ ] Complete College Relationship Manager.
- [ ] Test normal and invalid cases.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence.

**Next lesson:** Day 39.
