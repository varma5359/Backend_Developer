# Day 34: Django Models and Database Field Types

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Previous Django lessons; Python, OOP, HTTP and SQL foundations  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment and Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Employee Management Model

> **Teaching rule:** Do not copy a command without understanding it. Use the exact file path, run one step at a time, inspect the output and explain what the framework is doing.

## 1. Learning objectives

1. Explain how a Django model maps to a database table.
2. Choose appropriate field types and options.
3. Understand primary keys, null, blank, default, unique and __str__.
4. Run system checks and create a migration preview.

## 2. Concept introduction — start from zero

A model is a Python class that describes the data Django stores. Each model normally maps to a database table; each model instance represents one row; and model fields describe columns. Django's ORM uses model definitions to create queries. Writing a model does not immediately change the database: migrations are required and applied in the next lesson.

### Why a backend developer needs this

The Student Portal is being developed as a real, growing application. The code must remain organized and the result must be repeatable. Today's lesson adds one building block to that system. A junior developer should be able to explain the purpose of the component, not only remember its syntax.

## 3. Mental model

```text
Student / Browser
       |
       v
Django project (config)
       |
       v
profiles application
       |
       v
Today's Django component
       |
       +----> optional database / template / response work
       |
       v
Visible result or persisted schema
```

## 4. File map

- `profiles/models.py`
- `profiles/migrations/ (generated in next lesson)`

Project context:

```text
student_portal/
├── .venv/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── profiles/
    └── static/
        └── profiles/
```

Files are introduced gradually. Create a file only when this lesson tells you to.

## 5. Prepare the terminal

1. Open the existing `student_portal` folder in VS Code.
2. Open Terminal → New Terminal.
3. Confirm the current directory contains `manage.py`.
4. Activate the same virtual environment created earlier.
5. Confirm the interpreter and Django version.

```powershell
Get-Location
python --version
python -m django --version
```

If the current folder does not contain manage.py, move to the project root. Do not create a second project to avoid a path mistake.

## 6. Commands — exact order

```powershell
python manage.py check
python manage.py makemigrations profiles
# Do not run migrate until Day 35's migration lesson.
```

### Understand every command

### Step 1 — `Import models`

Django's model field classes are available through django.db.models.

### Step 2 — `Inherit from models.Model`

This tells Django that Employee is a model class managed by the ORM.

### Step 3 — `CharField`

Stores bounded text. max_length is required. employee_code is unique, so the database will reject duplicate codes after the schema constraint is applied.

### Step 4 — `EmailField`

Stores email-like text and provides email-format validation in Django model/form validation. It does not verify that a mailbox exists.

### Step 5 — `DecimalField`

Stores exact decimal values, appropriate for currency-like amounts. max_digits is the total number of digits and decimal_places is the number after the decimal point.

### Step 6 — `DateField`

Stores a calendar date. It does not store a time of day.

### Step 7 — `BooleanField`

Stores a true/false value. default=True supplies the value when a new object does not specify one.

### Step 8 — `DateTimeField(auto_now_add=True)`

Sets the creation timestamp when the object is first created. It is not intended as a freely editable field.

### Step 9 — `__str__`

Returns a readable representation used by admin, shell and debugging.

## 7. Implementation — correct files

### Code demonstration

The code below may contain Python, HTML or CSS sections. Use the filename comments to put each section into the correct file. Never paste HTML into a .py file.

```python
# profiles/models.py
from django.db import models

class Employee(models.Model):
    employee_code = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_code} - {self.full_name}"
```

### Before saving

1. Read the existing file.
2. Preserve working code from earlier days.
3. Add the new code at the correct location.
4. Check spelling and indentation.
5. Save the file.
6. Run the relevant Django command.
7. Inspect terminal output before opening the browser.

## 8. Detailed explanation

### Model, object, table and row
Employee is a Python class and Django model. The database table stores rows. An Employee instance represents one row in Python. Model fields describe the columns and their types.

### Primary key
Django adds an automatic primary-key field if you do not define one. In current Django defaults this is typically a BigAutoField when configured by default_auto_field. The primary key uniquely identifies each row.

### Field types
- CharField: bounded text such as names and codes.
- TextField: longer text.
- EmailField: email-formatted text with validation support.
- IntegerField: whole numbers.
- DecimalField: exact decimal numbers such as currency values.
- FloatField: floating-point numbers; avoid for exact monetary values.
- BooleanField: true/false.
- DateField: date only.
- DateTimeField: date and time.
- ForeignKey: many-to-one relationship, taught on Day 38.

### null versus blank
`null=True` affects database storage and allows SQL NULL. `blank=True` affects validation and permits an empty value in forms. They are not interchangeable. For text fields, Django conventionally recommends blank=True rather than null=True unless there is a specific reason to distinguish NULL from empty string.

### default and unique
default supplies a value when creating an object without that field. unique=True creates a database uniqueness constraint after migrations are applied. Application-level validation can improve error messages, but the database constraint protects integrity against concurrent writes too.

### DecimalField example
For salary up to 99,999,999.99, max_digits=10 and decimal_places=2 allows ten total digits, two after the decimal. Choose limits based on the business domain.

### __str__
Return a human-readable string. Without it, admin lists and shell output may display generic object labels.

### Model versus database schema
Changing models.py changes Python model definitions. It does not automatically update the database. makemigrations generates migration files; migrate applies them. That process is taught tomorrow.

### Avoid unsafe defaults
Do not use a mutable list/dictionary as a shared field default. Use a callable when a mutable default is genuinely needed. Do not store passwords in plain text model fields; use Django's authentication mechanisms.

## 9. Execution trace

Explain these questions aloud:
1. What is the input or requested operation?
2. Which file or command handles it?
3. What does Django do automatically?
4. What did the developer implement?
5. What result should be produced?
6. How do we prove that result is correct?

## 10. Verification checklist

- [ ] System check passes.
- [ ] Employee inherits from models.Model.
- [ ] employee_code and email have unique constraints in the model definition.
- [ ] salary uses DecimalField with decimal_places=2.
- [ ] __str__ returns a readable employee label.
- [ ] The learner distinguishes model definitions from applied database schema.

Run the general project check:

```powershell
python manage.py check
```

Expected when project configuration is valid:

```text
System check identified no issues (0 silenced).
```

The system check does not prove every browser interaction or database operation. Perform the specific checks above.

## 11. Troubleshooting

| Symptom | Likely cause | Diagnostic |
|---|---|---|
| manage.py not found | Wrong directory | Get-Location and locate manage.py |
| No module named django | Wrong environment | Check sys.executable and Django version |
| App not loaded | Missing app registration | Inspect INSTALLED_APPS |
| Template not found | Incorrect folder/file path | Check app/templates/app_name/ |
| Route returns 404 | URL pattern missing or order issue | Inspect root and app URLconf |
| Database table missing | Migration not applied | Run showmigrations and migrate |
| CSS missing | Incorrect static path | Inspect browser Network tab |
| SyntaxError | Incorrect Python syntax | Read traceback file and line |

### Safe debugging process
1. Reproduce the problem.
2. Read the complete error.
3. Locate the first relevant line in your own code.
4. Confirm the correct Python environment and project folder.
5. Check the filename, imports, spelling and configuration.
6. Change one thing at a time.
7. Rerun the appropriate check.
8. Verify the actual behavior again.

## 12. Industry scenario

A training institute needs to maintain a Student Portal. A backend developer must make the application easy to extend and debug. Today's concept is useful because it gives a predictable way to organize or operate one part of the system.

Discuss:
- What problem does the user face?
- Which component is responsible?
- What information enters the feature?
- What result should the user or developer observe?
- What failure case should be tested?

## 13. Approved mini-project — Employee Management Model

### Objective
Build a working demonstration of today's approved concept in the existing Student Portal.

### Ordered tasks

1. Create the Employee model exactly as shown.
2. Explain each field type and its chosen options.
3. Run python manage.py check.
4. Run makemigrations profiles and inspect the generated file.
5. Explain why the table is not yet guaranteed to exist until migrate is applied.

### Acceptance checks

- [ ] System check passes.
- [ ] Employee inherits from models.Model.
- [ ] employee_code and email have unique constraints in the model definition.
- [ ] salary uses DecimalField with decimal_places=2.
- [ ] __str__ returns a readable employee label.
- [ ] The learner distinguishes model definitions from applied database schema.

### Submission evidence
- Relevant source files.
- Terminal output from checks and commands.
- Browser screenshot or database evidence, where relevant.
- README with setup and verification steps.
- Short explanation of one error and its correction.

### Optional extension
Make one small change, predict its result, run it and explain the difference.

## 14. AI-assisted implementation

Use the AI mentor to learn incrementally:

**Planning prompt**
```text
I am a beginner. Help me plan Employee Management Model.
Give me ordered tasks and checkpoints. Do not give me the complete solution.
```

**Guided implementation prompt**
```text
Guide me one file and one step at a time. Explain the command,
the code and the expected output. Wait for my result before continuing.
```

**Debugging prompt**
```text
Here is my exact command, current directory, relevant file and full error.
Explain the likely cause and the smallest safe fix. Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Q1. What does a Django model represent?

A. A database connection only
B. A Python class describing stored data
C. A browser tab
D. A URL route

**Answer: B.** A model defines the fields and behavior for database-backed data.

### Q2. Which field is appropriate for exact currency-like decimal values?

A. FloatField
B. BooleanField
C. DecimalField
D. DateField

**Answer: C.** DecimalField stores decimal values with declared precision.

### Q3. What is the difference between blank=True and null=True?

A. They are identical
B. blank affects validation; null affects database storage
C. null affects CSS; blank affects URL
D. Both mean unique

**Answer: B.** blank is a validation option; null controls whether the database column may contain NULL.

### Q4. Does editing models.py immediately update the database table?

A. Yes, as soon as file is saved
B. Only when runserver starts
C. No; create and apply migrations
D. Only after browser refresh

**Answer: C.** Migrations record and apply schema changes.

### Q5. What is the purpose of __str__?

A. Encrypt the database
B. Return a readable object representation
C. Create a primary key
D. Register the app

**Answer: B.** Django admin and shell use this representation to identify objects.

## 16. Interview preparation

### Q1. Explain today's topic in simple words.
**Answer:** A model is a Python class that describes the data Django stores. Each model normally maps to a database table; each model instance represents one row; and model fields describe columns. Django's ORM uses model definitions to create queries. Writing a model does not immediately change the database: migrations are required and applied in the next lesson.

**Follow-up:** Give an example from the Student Portal.

### Q2. Which files or commands are important?
**Answer:** `profiles/models.py`, `profiles/migrations/ (generated in next lesson)`. Explain the responsibility of each.

**Follow-up:** What would you inspect if the expected behavior did not appear?

### Q3. How do you verify the implementation?
**Answer:** Run the commands, inspect output and verify the browser or database behavior. Explain the edge case you tested.

**Follow-up:** Does a successful system check guarantee that every feature works?

**Answer:** No. It checks selected project configuration and framework conditions. Feature behavior needs direct testing.

### Q4. What is a common beginner mistake?
**Answer:** Running commands from the wrong folder, editing the wrong file or assuming code works without verification. Read the error and isolate the cause.

## 17. Completion checklist

- [ ] I can explain today's concept without reading.
- [ ] I know the exact file paths.
- [ ] I can explain the important code.
- [ ] I ran the required commands.
- [ ] The Django system check passes.
- [ ] I verified the expected behavior.
- [ ] I tested an edge case.
- [ ] I completed Employee Management Model.
- [ ] I submitted reproducible evidence.
- [ ] I can answer the interview questions.

## 18. Trainer validation

Do not mark the day complete merely because a file contains code. Ask the learner to demonstrate the result, explain the flow, modify one small part independently and diagnose one controlled mistake.

**Next lesson:** Day 35 — Django Migrations: makemigrations and migrate
