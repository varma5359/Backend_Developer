# Day 37: Django ORM Fundamentals and Querying Records

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–36 — Django setup, models, migrations and the admin demonstration  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Employee Query Explorer

> **Self-paced method:** Read the query requirement, run one ORM operation at a time in the Django shell, inspect the returned value and compare it with the expected result. Use the troubleshooting section whenever the output differs.

## 1. Learning objectives

1. Explain the ORM, model manager and QuerySet.
2. Create, retrieve, filter and order records.
3. Understand get() exceptions and QuerySet laziness.
4. Update and delete records carefully.

## 2. Start from the business requirement

The Employee model created on Day 34 is the data source for today's ORM practice. The approved mini-project is Employee Query Explorer. Day 38 introduces the separate Student, Department, Course and StudentProfile relationship schema.

The Django ORM lets a developer work with database records through Python models and QuerySets rather than writing SQL for every operation. A QuerySet represents a database query. Many QuerySets are lazy: Django builds the query first and sends it to the database when results are needed. The ORM does not remove the need to understand SQL, indexes or query performance.

A junior developer must understand both the Python code and the underlying relational data. Django makes database work convenient, but it does not remove the need to reason about keys, constraints and data integrity.

## 3. Mental model

```text
Student Portal requirement
        |
        v
Django model / admin / ORM
        |
        v
Django database backend
        |
        v
Relational database tables and constraints
        |
        v
Python model instances / QuerySets
```

## 4. Files to open

- `profiles/models.py`
- `Django shell via manage.py`

The app's models live in `profiles/models.py`. Migration files are generated under `profiles/migrations/`; do not create schema history by hand unless an advanced lesson specifically requires it.

## 5. Prepare the terminal

1. Open the existing project folder in VS Code.
2. Open the integrated terminal.
3. Activate the .venv environment.
4. Confirm manage.py is in the current directory.
5. Check the Django version.

```powershell
Get-Location
python --version
python -m django --version
```

## 6. Commands — run in order

```powershell
python manage.py shell
# In the shell:
from profiles.models import Employee
Employee.objects.count()
Employee.objects.all()
exit()
```

### Command explanation

### Step 1 — `Open Django shell`

python manage.py shell loads the Django project environment so you can import models and execute ORM queries interactively.

### Step 2 — `Import Employee`

The model class represents the table and provides the objects manager.

### Step 3 — `objects.create()`

Creates and saves a record, then returns the created model instance. Required model fields must be supplied.

### Step 4 — `objects.all()`

Returns a QuerySet representing all rows. The database query may not execute until the QuerySet is evaluated.

### Step 5 — `objects.filter()`

Builds a query for rows matching conditions. No match returns an empty QuerySet, not DoesNotExist.

### Step 6 — `Lookup suffixes`

__icontains performs case-insensitive substring matching. Other common lookups include exact, iexact, contains, gt, gte, lt, lte, in, startswith and isnull.

### Step 7 — `order_by()`

Sorts the result. A field name means ascending; a leading minus means descending.

### Step 8 — `objects.get()`

Returns exactly one object. It raises Employee.DoesNotExist if there are zero and Employee.MultipleObjectsReturned if more than one.

### Step 9 — `save()`

Persists changes to the current model instance. update_fields can limit which fields are written.

### Step 10 — `delete()`

Deletes the selected object. Verify the target before running destructive operations.

## 7. Implementation

```python
from profiles.models import Employee

# CREATE
employee = Employee.objects.create(
    employee_code="EMP1001",
    full_name="Asha Rao",
    email="asha@example.com",
    salary="55000.00",
    joining_date="2026-11-01",
)

# READ
all_employees = Employee.objects.all()
active_employees = Employee.objects.filter(is_active=True)
search_result = Employee.objects.filter(full_name__icontains="asha")
ordered = Employee.objects.order_by("full_name")
latest_first = Employee.objects.order_by("-joining_date")

# GET exactly one record
employee = Employee.objects.get(employee_code="EMP1001")

# UPDATE
employee.is_active = False
employee.save(update_fields=["is_active"])

# DELETE only after confirming the target
# employee.delete()
```

**Important:** If a code section says "add inside the existing model", paste it inside that class with the correct indentation. Do not create duplicate model classes or put model fields at module level. Preserve code from earlier days.

## 8. Deep concept explanation

### What is the ORM?
ORM means Object-Relational Mapper. It maps Python model classes and instances to relational database tables and rows. You still benefit from knowing SQL because ORM operations become SQL queries.

### Model manager: objects
The default manager is commonly accessed through `Employee.objects`. It is the starting point for building queries.

### QuerySet
A QuerySet represents a collection of database records. It supports chaining:
`Employee.objects.filter(is_active=True).order_by("full_name")`.
Chaining usually builds a query rather than immediately running it.

### Lazy evaluation
A QuerySet is lazy until evaluated. Iteration, list conversion, len(), bool(), count(), exists() and other operations can cause database work. Be aware of repeated evaluation.

### filter versus get
filter returns zero, one or many records as a QuerySet. get expects exactly one and raises exceptions when the count is not exactly one. Use filter when zero results are normal; use get when uniqueness is part of the requirement.

### Common field lookups
- exact: exact match.
- iexact: case-insensitive exact match.
- contains / icontains: substring match.
- gt / gte: greater than / greater than or equal.
- lt / lte: less than / less than or equal.
- in: value belongs to a collection.
- isnull: checks NULL.

### Values and values_list
`values("employee_code", "full_name")` returns dictionaries with selected fields. `values_list()` returns tuples or a flat list when flat=True is valid.

### count and exists
Use count() when you need the number of matching rows. Use exists() when you only need to know whether at least one matching row exists.

### Update and delete
Changing a Python attribute does not persist until save() is called. delete() is destructive. Verify the selected object and consider foreign-key deletion behavior.

### Avoid SQL injection
Use ORM filters with values; do not build SQL by concatenating user input. When raw SQL is genuinely required, use parameterized queries.

### Troubleshooting
- FieldError: field name or lookup is invalid.
- DoesNotExist: get() found no row.
- MultipleObjectsReturned: get() matched multiple rows.
- IntegrityError: unique, not-null or foreign-key constraint failed.
- Data not saved: call save() or use create()/update() as appropriate.

## 9. How to reason about the result

Ask yourself:
1. What business rule is represented?
2. What model or query represents it?
3. What database structure or SQL behavior is expected?
4. What does Django generate or execute?
5. What happens when the record is missing or duplicated?
6. How do we verify the data rather than assuming it was saved?

## 10. Verification checklist

- [ ] create() creates a row.
- [ ] all() lists records.
- [ ] filter() returns matching records.
- [ ] icontains search works.
- [ ] order_by sorts results.
- [ ] get() returns exactly one or raises the documented exception.
- [ ] save() persists a field update.
- [ ] The learner explains QuerySet laziness.

Run:

```powershell
python manage.py check
```

Expected for a valid project:

```text
System check identified no issues (0 silenced).
```

A system check does not prove every query or relationship is correct. Run the shell/admin exercises above.

## 11. Troubleshooting

| Symptom | Likely reason | What to inspect |
|---|---|---|
| Model import fails | Wrong app/module name | Check profiles/models.py and app registration |
| Table does not exist | Migrations not applied | showmigrations and migrate |
| IntegrityError | Unique, required or foreign-key constraint failed | Inspect field values and referenced rows |
| DoesNotExist | get() returned no match | Verify lookup value or use filter when zero matches are expected |
| MultipleObjectsReturned | get() matched multiple rows | Use a unique lookup or filter |
| ProtectedError | PROTECT blocked deletion | Check related records and business rule |
| RelatedObjectDoesNotExist | One-to-one object not created | Create the related profile before accessing it |
| Query returns unexpected data | Wrong lookup or relationship | Inspect filters and actual records |

## 12. Industry scenario

A college portal stores students, departments, courses and student-specific profiles. The institute needs reliable links between records. A relationship design error can allow orphaned records, duplicate data or invalid associations.

Discuss:
- Which record owns the foreign key?
- Can one student belong to multiple departments?
- Can a course contain many students?
- What should happen if a department is deleted?
- What constraints should the database enforce?

## 13. Approved mini-project — Product Query Explorer

### Objective
Build the relationship/query/admin feature described in today's lesson using the existing Student Portal.

### Tasks

1. Open Django shell and import Employee.
2. Create two sample employee records with unique codes and emails.
3. List all employees and count them.
4. Filter active employees and search by a name fragment.
5. Order by salary or joining date.
6. Use get() with an existing code and with a missing code; observe DoesNotExist.
7. Update one employee and verify the saved value.
8. Explain why delete() should be used cautiously.

### Acceptance criteria

- [ ] create() creates a row.
- [ ] all() lists records.
- [ ] filter() returns matching records.
- [ ] icontains search works.
- [ ] order_by sorts results.
- [ ] get() returns exactly one or raises the documented exception.
- [ ] save() persists a field update.
- [ ] The learner explains QuerySet laziness.

### Submission evidence
- Updated model/admin/query code.
- Migration files where the schema changes.
- Terminal output from checks and migrations.
- Shell/admin evidence showing real records.
- Short explanation of one data integrity rule.
- README with reproducible commands.

### Optional extension
Add a small query or admin improvement and explain the data behavior before and after.

## 14. AI-assisted learning prompts

**Planning**
```text
Help me plan Product Query Explorer in small steps. Do not provide the complete solution.
Explain the data requirement and the files I need to inspect.
```

**Guided implementation**
```text
Guide me one model/query/admin step at a time. Explain the database meaning,
the Django code and the verification command. Wait for my result.
```

**Debugging**
```text
Here is my model, migration state, exact ORM query and complete traceback.
Explain the likely cause and smallest safe correction. Do not delete migrations.
```

## 15. Daily MCQs

### Q1. What is the Django ORM?

A. A Python interface for working with relational data
B. A CSS framework
C. A web server
D. A password manager

**Answer: A.** The ORM maps model operations to database queries.

### Q2. What does filter() return when no records match?

A. DoesNotExist exception
B. An empty QuerySet
C. A new model
D. A 404 page automatically

**Answer: B.** filter returns a QuerySet that can contain zero records.

### Q3. What happens if get() finds no matching record?

A. Returns None
B. Returns empty list
C. Raises Model.DoesNotExist
D. Creates a row

**Answer: C.** get requires exactly one matching record.

### Q4. What does order_by('-joining_date') mean?

A. Sort oldest first
B. Sort descending by joining_date
C. Filter NULL dates
D. Delete old rows

**Answer: B.** A leading minus requests descending order.

### Q5. When are QuerySets often evaluated?

A. Always immediately at construction
B. When results are needed, such as iteration
C. Only at server shutdown
D. Only in templates

**Answer: B.** QuerySets are lazy and defer database work until evaluation.

## 16. Interview preparation

### Q1. Explain today's concept.
**Answer:** The Django ORM lets a developer work with database records through Python models and QuerySets rather than writing SQL for every operation. A QuerySet represents a database query. Many QuerySets are lazy: Django builds the query first and sends it to the database when results are needed. The ORM does not remove the need to understand SQL, indexes or query performance.

**Follow-up:** Explain it using the Student Portal example.

### Q2. Which model, field, command or query is important?
**Answer:** `profiles/models.py`, `Django shell via manage.py`. Describe the responsibility and the data behavior.

**Follow-up:** What happens if the expected record is missing or duplicated?

### Q3. How do you verify the implementation?
**Answer:** Run Django checks, inspect migration state if applicable and query actual records through admin or shell.

**Follow-up:** Why is a successful system check not enough?

**Answer:** System checks do not execute every data operation or prove the business relationship is correct.

## 17. Completion checklist

- [ ] I can explain the business rule.
- [ ] I can explain the model/query/relationship.
- [ ] I know the exact file path.
- [ ] I ran the required commands.
- [ ] I inspected the actual database behavior.
- [ ] I tested an edge case.
- [ ] I completed Product Query Explorer.
- [ ] I submitted code and evidence.
- [ ] I can explain one data integrity concern.

## 18. Trainer validation

Ask the student to create or query records independently. Change one relationship or filter and ask them to predict the outcome. Do not mark complete based only on copied model code.

**Next lesson:** Day 38 — Model Relationships: One-to-One, One-to-Many and Many-to-Many
