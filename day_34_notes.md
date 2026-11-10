# Day 34: Django Models and Database Field Types

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–34 as applicable; review the previous Django lessons before continuing  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Employee Management Model

> **Trainer guidance:** Show the learner the exact file path before showing the code. Explain why the file exists, what each important line does, how to run the project and how to verify the result.

## 1. Learning objectives

- Explain django models and database field types.
- Identify the Django files and folders used.
- Implement the example step by step.
- Explain the relationship between Django code and the browser or database.
- Verify the result and troubleshoot common errors.
- Complete Employee Management Model.

## 2. Concept introduction

A Django model is a Python class that inherits from django.db.models.Model. Its fields describe data stored in a database table. Django's ORM uses model metadata to create and query database records. A normal Python class is not automatically a database table; a Django model participates in the ORM.

## 3. Why the concept matters

A Django application becomes easier to maintain when shared presentation is reused, data is represented consistently and database changes are tracked. These practices help teams review code and understand how a feature evolved.

## 4. File-by-file implementation

### File or command: `profiles/models.py`

```python
from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ("ENG", "Engineering"),
        ("HR", "Human Resources"),
        ("FIN", "Finance"),
    ]

    employee_code = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.CharField(
        max_length=3,
        choices=DEPARTMENT_CHOICES
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_code} - {self.full_name}"
```

## 5. Explain the important statements

### profiles/models.py

1. `from django.db import models` — Imports the Django component used by this file.
2. ` ` — Part of the file structure or configuration; understand how it supports the feature.
3. `class Employee(models.Model):` — Defines a reusable class or model.
4. `    DEPARTMENT_CHOICES = [` — Part of the file structure or configuration; understand how it supports the feature.
5. `        ("ENG", "Engineering"),` — Part of the file structure or configuration; understand how it supports the feature.
6. `        ("HR", "Human Resources"),` — Part of the file structure or configuration; understand how it supports the feature.
7. `        ("FIN", "Finance"),` — Part of the file structure or configuration; understand how it supports the feature.
8. `    ]` — Part of the file structure or configuration; understand how it supports the feature.
9. ` ` — Part of the file structure or configuration; understand how it supports the feature.
10. `    employee_code = models.CharField(max_length=20, unique=True)` — Declares a database field or model option.
11. `    full_name = models.CharField(max_length=120)` — Declares a database field or model option.
12. `    email = models.EmailField(unique=True)` — Declares a database field or model option.
13. `    department = models.CharField(` — Declares a database field or model option.
14. `        max_length=3,` — Part of the file structure or configuration; understand how it supports the feature.
15. `        choices=DEPARTMENT_CHOICES` — Part of the file structure or configuration; understand how it supports the feature.
16. `    )` — Part of the file structure or configuration; understand how it supports the feature.
17. `    salary = models.DecimalField(max_digits=10, decimal_places=2)` — Declares a database field or model option.
18. `    joining_date = models.DateField()` — Declares a database field or model option.
19. `    is_active = models.BooleanField(default=True)` — Declares a database field or model option.
20. ` ` — Part of the file structure or configuration; understand how it supports the feature.
21. `    def __str__(self):` — Defines a method or view function.
22. `        return f"{self.employee_code} - {self.full_name}"` — Part of the file structure or configuration; understand how it supports the feature.

## 6. How to run and verify

1. Activate the project's virtual environment.
2. Open the terminal in the folder containing manage.py.
3. Run `python manage.py check`.
4. Execute the commands or start the development server as appropriate.
5. Open the page in a browser or inspect migration status.
6. Compare actual behavior with the expected result.
7. Record any warning and explain whether it is expected.

## 7. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Template block is not rendered | extends path and matching block names |
| CSS is missing | static directory, STATIC_URL, {% load static %} and URL |
| Model is not detected | app in INSTALLED_APPS and model import |
| Field configuration error | Field type and required field arguments |
| No migration is generated | Check whether model changes exist and the correct app is selected |
| Migration fails | Read the full database error and inspect migration dependencies |
| Database does not reflect model change | Run makemigrations and then migrate |

## 8. Industry scenario

A staff management website needs a consistent page header and styling, an employee data model and a repeatable way to update its database structure. Django's template inheritance, static files, model fields and migrations support these needs.

## 9. Approved mini-project — Employee Management Model

**Objective:** Employee Management Model.

### Functional requirements

1. Open profiles/models.py.
2. Import django.db.models.
3. Create Employee inheriting from models.Model.
4. Choose field types that match the data.
5. Add max_length to character fields.
6. Use DecimalField for money-like values rather than float.
7. Add unique constraints where business rules require unique values.
8. Add __str__() for a readable object representation.
9. Run python manage.py check.

### Suggested structure

```text
projects/day_34/
├── manage.py
├── config/
└── profiles/
    ├── models.py
    ├── migrations/
    ├── templates/
    └── static/
```

### Validation checklist

- [ ] Employee inherits from models.Model.
- [ ] Every field has a suitable type.
- [ ] Character fields define max_length.
- [ ] Salary uses DecimalField.
- [ ] Unique rules match the requirements.
- [ ] __str__ returns a readable string.
- [ ] Django system check passes.

### Submission evidence

- Updated source files.
- Commands executed and terminal output.
- Browser screenshot or migration status.
- README with exact file paths and setup instructions.
- Explanation of one design decision and one error handled.

## 10. AI-assisted implementation guide

**Planning prompt:** "Help me plan Employee Management Model. List the files, ordered tasks, commands and verification checks. Do not write the complete solution."

**Guided prompt:** "Guide me through one file at a time. Explain why the file is needed, show only the next change and wait for my output."

**Debugging prompt:** "Inspect my exact Django error, file path and command. Explain the likely cause and how to verify the fix."

**Review prompt:** "Review my implementation against the approved requirements. Identify missing validation, naming issues and maintainability concerns."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Organize Django presentation, data or database structure changes in a maintainable way.  
B. Replace Python.  
C. Disable validation.  
D. Remove all configuration.  
**Answer: A.** The concept supports a maintainable Django application.

**Q2. What should you inspect when the result is missing?**  
A. Only the browser theme.  
B. The relevant file path, setting and Django output.  
C. Delete the project.  
D. Ignore the warning.  
**Answer: B.** File paths and configuration commonly determine whether Django discovers the component.

**Q3. Which practice is safest?**  
A. Edit generated files without understanding them.  
B. Ignore migrations.  
C. Follow the correct workflow and verify each change.  
D. Commit local secrets.  
**Answer: C.** Use a repeatable workflow and inspect the result.

**Q4. What is the best evidence of completion?**  
A. A file exists.  
B. The code is long.  
C. The learner watched a video.  
D. The feature works and its behavior is verified.  
**Answer: D.** Evidence should show the required behavior.

**Q5. What should the README contain?**  
A. Setup, file paths, commands and validation results.  
B. Only a title.  
C. A private password.  
D. No instructions.  
**Answer: A.** Clear instructions make the project reproducible.

## 12. Interview preparation

**Q1. Explain django models and database field types.**  
**Answer:** A Django model is a Python class that inherits from django.db.models.Model. Its fields describe data stored in a database table. Django's ORM uses model metadata to create and query database records. A normal Python class is not automatically a database table; a Django model participates in the ORM.

**Q2. Which files or commands are important?**  
**Answer:** Explain each file or command from the demonstration and its responsibility.

**Q3. How would you troubleshoot a failure?**  
**Answer:** Read the full traceback, confirm file paths and configuration, run Django system checks and verify the result after one focused correction.

**Follow-up:** What evidence would you show another developer?  
**Answer:** The source change, command output, browser behavior or migration status and a concise README.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Identify the relevant file paths.
- [ ] Implement the example.
- [ ] Run the required checks or commands.
- [ ] Verify the expected result.
- [ ] Complete Employee Management Model.
- [ ] Test normal and error cases.
- [ ] Complete all five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 35.
