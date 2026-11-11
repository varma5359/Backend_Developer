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

First attempt each step using the lesson. If you are still stuck, use an optional AI learning assistant for hints and explanations; do not ask it to hide the implementation from you.

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

## 18. Independent completion test

Do not mark the day complete merely because a file contains code. Complete every check yourself:
1. Demonstrate the result in the browser or terminal.
2. Explain the execution flow without reading the notes.
3. Modify one small part independently and predict the result before running it.
4. Compare the actual result with your prediction.
5. Diagnose and fix one controlled mistake, such as a misspelled variable, template path or setting.

**Next lesson:** Day 35 — Django Migrations: makemigrations and migrate

---

# Extended Beginner Lab — Model Design and Field Types

## 19. What is a Django model?

A model is a Python class that describes data stored by the application.

Django uses model definitions to:
- Describe fields.
- Define relationships.
- Generate database schema migrations.
- Query and update records through the ORM.
- Apply model metadata and constraints.

A model is not the same as a database row. A model class describes the structure; an instance represents one object.

## 20. Model class versus model instance

Model class:

~~~python
class Employee(models.Model):
    full_name = models.CharField(max_length=120)
~~~

Model instance:

~~~python
employee = Employee(full_name="Asha Rao")
~~~

The class describes the field. The instance contains one employee's value.

The instance is not stored in the database until it is saved.

## 21. Field selection guide

| Data | Common field |
|---|---|
| Short name | CharField |
| Long description | TextField |
| Whole number | IntegerField |
| Decimal amount | DecimalField |
| True/False | BooleanField |
| Date only | DateField |
| Date and time | DateTimeField |
| Email | EmailField |
| URL | URLField |
| File path/upload | FileField |
| Image upload | ImageField |
| Unique identifier | UUIDField |
| Relationship | ForeignKey / OneToOneField / ManyToManyField |

Choose a field based on the meaning and validation requirements of the data.

## 22. CharField and TextField

CharField:
- Stores short text.
- Requires max_length.
- Common for names, codes and categories.

TextField:
- Stores longer text.
- Common for descriptions and notes.
- Does not require max_length in the same way as CharField.

Do not use TextField for every text value. Choose the field that represents the data.

## 23. IntegerField versus DecimalField

IntegerField stores whole numbers.

DecimalField stores fixed-precision decimal values.

Examples:
- Stock quantity: IntegerField.
- Salary: DecimalField.
- Product price: DecimalField.

Do not store money using FloatField unless there is a specific technical reason and rounding behavior is understood.

## 24. BooleanField

BooleanField stores a true/false value.

Example:

~~~python
is_active = models.BooleanField(default=True)
~~~

This is useful for status flags.

A BooleanField should represent a genuinely two-state value. If there are more than two business states, use choices or a related model.

## 25. DateField versus DateTimeField

DateField stores a date.

DateTimeField stores a date and time.

Examples:
- Date of joining: DateField.
- Record created timestamp: DateTimeField.
- Appointment time: DateTimeField.

Timezone-aware settings matter for datetime values.

## 26. null versus blank

These options are different.

null:
- Database-level option.
- Allows SQL NULL.

blank:
- Validation/form-level option.
- Allows the field to be empty in forms.

Do not set both automatically for every optional field.

For text fields, many Django projects use blank=True and keep an empty string rather than NULL. Follow a consistent data policy.

## 27. default

default supplies a value when one is not provided.

Example:

~~~python
stock = models.IntegerField(default=0)
~~~

The default is used when a new instance is created without an explicit stock value.

Do not use a mutable object such as a list or dictionary as a shared default without a callable factory.

## 28. auto_now and auto_now_add

auto_now_add:
- Sets a datetime when the row is first created.

auto_now:
- Updates a datetime when the model is saved.

Example:

~~~python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
~~~

These fields are generally not editable through a normal form.

## 29. unique

unique=True enforces uniqueness for a field.

Example:

~~~python
employee_code = models.CharField(
    max_length=20,
    unique=True,
)
~~~

The database prevents duplicate values.

A form can also validate uniqueness and display a helpful error.

## 30. choices

Choices restrict a field to a defined set of values at the application validation layer.

Example:

~~~python
STATUS_CHOICES = [
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
]

status = models.CharField(
    max_length=10,
    choices=STATUS_CHOICES,
    default="ACTIVE",
)
~~~

Use stable stored values and human-readable display labels.

## 31. primary key

A primary key uniquely identifies each row.

Django automatically creates a primary key if you do not define one.

You can inspect an instance using:
- object.pk.
- object.id when the default field is named id.

Prefer pk when writing generic code because it refers to the primary key regardless of its field name.

## 32. __str__ method

A readable string representation helps in:
- Admin.
- Shell output.
- Logs.
- Related object widgets.

Example:

~~~python
def __str__(self):
    return self.full_name
~~~

Return a string. Do not return a model object or integer.

## 33. Meta class

A model Meta class configures model metadata.

Examples:
- ordering.
- constraints.
- indexes.
- verbose_name.
- verbose_name_plural.
- db_table.

Example:

~~~python
class Meta:
    ordering = ["full_name"]
    verbose_name_plural = "employees"
~~~

Use Meta options when they describe the model's behavior or database structure.

## 34. Model design checklist

Before adding a field, ask:
1. What business value does it represent?
2. Which field type matches that value?
3. Is it required?
4. Can it be empty?
5. Does it need a default?
6. Must it be unique?
7. Does it need choices?
8. Is there a relationship instead of plain text?
9. Should it be indexed?
10. How will the form validate it?

## 35. Common field design mistakes

| Mistake | Why it is a problem | Better choice |
|---|---|---|
| Store phone number as integer | Leading zero and symbols can be lost | CharField |
| Store money as float | Binary precision issues | DecimalField |
| Use TextField for every value | Loses useful length/field semantics | Choose based on meaning |
| Set null=True and blank=True everywhere | Inconsistent empty-value semantics | Decide database and form behavior |
| Use free text for fixed status | Inconsistent values | choices or related table |
| Expose auto timestamp in form | User can alter system metadata | Keep readonly/server-managed |
| Assume unique form validation is enough | Concurrent writes can collide | Database unique constraint |

## 36. Practical field-selection exercise

Choose a field for:
- Employee full name.
- Employee code.
- Joining date.
- Monthly salary.
- Is currently employed.
- Biography.
- Created timestamp.
- Department relationship.

Explain why each field type is appropriate.

## 37. Self-check questions

1. What is a model class?
2. What is a model instance?
3. What is the difference between CharField and TextField?
4. Why use DecimalField for money?
5. What is the difference between null and blank?
6. What does default do?
7. What is the difference between auto_now and auto_now_add?
8. What does unique=True enforce?
9. What is choices?
10. What is the purpose of __str__?
11. What is a primary key?
12. What does Meta configure?

## 38. Answers

1. Python class describing database data.
2. One object created from the model class.
3. CharField is short bounded text; TextField is longer text.
4. It stores fixed-precision decimal values.
5. null affects database storage; blank affects validation.
6. Supplies a value when one is not provided.
7. One sets creation time; the other updates on save.
8. Prevents duplicate field values.
9. Defines allowed stored values and display labels.
10. Provides a readable representation.
11. A unique identifier for each row.
12. Model metadata such as ordering, constraints and table options.

## 39. Independent challenge — Employee Schema Design

Design a model for an employee directory.

List:
- Field name.
- Field type.
- Required/optional.
- Unique/default/choices.
- Business reason.

Compare the design with the approved Employee model before changing code.

---

# Deep Practice Workbook — Design an Employee Data Model

## 40. Business scenario

An institute needs to store employee records.

Required information:
- Employee code.
- Full name.
- Email address.
- Joining date.
- Salary.
- Active status.
- Biography.
- Department.

## 41. Choose fields deliberately

| Business value | Suggested field | Reason |
|---|---|---|
| Employee code | CharField | May contain letters and leading zeros |
| Full name | CharField | Bounded short text |
| Email | EmailField | Email-oriented validation |
| Joining date | DateField | Date without time |
| Salary | DecimalField | Fixed-precision decimal |
| Active status | BooleanField | Two-state flag |
| Biography | TextField | Longer text |
| Department | ForeignKey | Department is a related entity |

## 42. Avoid storing a relationship as plain text

If every employee stores department as a string:
- Spelling may differ.
- Department names may be duplicated.
- Renaming a department requires many row updates.
- Reporting becomes inconsistent.

A ForeignKey connects each employee to one Department record.

## 43. Required and optional decisions

For every field, decide:
- Is the value required at creation?
- Can it be unknown?
- Can it be empty?
- Does it need a default?
- Does it need uniqueness?
- Is the field controlled by staff or the employee?

Do not set blank=True and null=True automatically.

## 44. Unique employee code

A unique employee code is useful because it identifies an employee within the organization.

Use a database uniqueness rule as well as form validation.

Do not assume that a form check alone protects against concurrent duplicate inserts.

## 45. DecimalField exercise

Choose precision based on business requirements.

~~~python
salary = models.DecimalField(
    max_digits=10,
    decimal_places=2,
)
~~~

Explain:
- Total digits.
- Decimal digits.
- Why salary is not a FloatField.
- What happens if the value exceeds the supported precision.

## 46. Model string representation

A readable string can use employee code and full name.

~~~python
def __str__(self):
    return f"{self.employee_code} - {self.full_name}"
~~~

This is useful in admin and shell output.

## 47. Model metadata exercise

Decide whether the model needs:
- Default ordering.
- Human-readable singular name.
- Human-readable plural name.
- Database indexes.
- Constraints.

Do not add an index to every field. Indexes should support actual query patterns.

## 48. Review before migration

Before creating a migration:
1. Read the model.
2. Check field types.
3. Check max lengths.
4. Check null/blank/default.
5. Check uniqueness.
6. Check relationships.
7. Check on_delete behavior.
8. Check Meta options.
9. Run system checks.
10. Generate and inspect the migration.

## 49. Schema review questions

1. Which field is the primary key?
2. Which field identifies an employee?
3. Which field stores a money value?
4. Which field stores a date?
5. Which field represents a relationship?
6. Which fields are optional?
7. Which fields should a user be allowed to edit?
8. Which values should be generated by the server?

## 50. Answers

1. Django creates a primary key automatically unless one is defined.
2. Employee code.
3. DecimalField.
4. DateField.
5. ForeignKey to Department.
6. Depends on the business requirement.
7. Only approved profile fields.
8. Creation timestamps and ownership fields.

## 51. Common design review findings

- Phone numbers should not be integer fields.
- Monetary values should not use float without a deliberate reason.
- Status fields should use controlled choices when there are more than two states.
- Timestamps should normally be server-managed.
- Relationships should use relational fields rather than copied text when entities are shared.
- Uniqueness should be protected at database level where required.

## 52. Independent design challenge

Design a Course model with:
- Course code.
- Title.
- Description.
- Duration in days.
- Fee.
- Active status.
- Created timestamp.

For each field, write:
- Field class.
- Required/optional decision.
- Validator/constraint if needed.
- One example value.
- One invalid value.

Do not change the approved project model until the design has been reviewed.

## 53. Final model checklist

- [ ] Every field has a business meaning.
- [ ] Field type matches the data.
- [ ] null and blank are intentional.
- [ ] Defaults are appropriate.
- [ ] Unique fields have database protection.
- [ ] Relationships are modeled correctly.
- [ ] Deletion behavior is understood.
- [ ] __str__ returns a readable string.
- [ ] Meta options are intentional.
- [ ] Migration is reviewed before applying.

## 54. Final independent schema assessment

Design a model for a training batch.

Include:
- Batch code.
- Batch title.
- Start date.
- End date.
- Capacity.
- Fee.
- Active flag.
- Course relationship.

For each field explain the chosen field type, required/optional behavior, default, uniqueness and validation.

Then explain which rules should be protected by database constraints.

Do not generate migrations until the schema has been reviewed.


## 55. Model design review rubric

A reviewer should be able to answer:
- What does each field represent?
- Why was this field class selected?
- Which values are permitted?
- Which values are required?
- Which values are unique?
- What happens when a related record is deleted?
- Which fields are generated by the server?
- Which fields can a user edit?
- Which business rules are enforced in the database?

Revise any field whose purpose cannot be explained.


## 56. Explain-back assessment

Without reading the notes, explain:
1. What a model class represents.
2. What a model instance represents.
3. How to select CharField versus TextField.
4. Why money uses DecimalField.
5. Why phone numbers are text.
6. How null differs from blank.
7. How default works.
8. How unique is enforced.
9. What choices provide.
10. What a ForeignKey represents.
11. What a primary key does.
12. Why __str__ is useful.

## 57. Submission reflection

Write a short schema decision record for one field. Include the business meaning, selected field type, required/optional decision, validation, database rule and one rejected alternative. Explain why the selected design is better for this data.

## 58. Final reviewer prompt

Ask another learner to review your schema and identify one field whose type, optionality or relationship design could be improved. Record the feedback and explain whether you accepted the change.

## 59. Final readiness statement

Do not mark the model design complete until you can explain each field to another developer, justify the chosen field type and demonstrate how invalid data is rejected.
