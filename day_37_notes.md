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
Employee Portal requirement
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

second_employee = Employee.objects.create(
    employee_code="EMP1002",
    full_name="Rahul Kumar",
    email="rahul@example.com",
    salary="48000.00",
    joining_date="2026-10-15",
    is_active=False,
)

# READ
all_employees = Employee.objects.all()
active_employees = Employee.objects.filter(is_active=True)
search_result = Employee.objects.filter(full_name__icontains="asha")
ordered = Employee.objects.order_by("full_name")
latest_first = Employee.objects.order_by("-joining_date")

# GET exactly one record
employee = Employee.objects.get(employee_code="EMP1001")

# UPDATE — run this only after checking the initial query results
# employee.is_active = False
# employee.save(update_fields=["is_active"])

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


## 10A. Expected shell results

The following output assumes a fresh database or that the two sample employees are the only matching records. If you already have records, your totals will be different; use the filtered query to inspect the sample records.

After creating Asha and Rahul, run:

```python
print(list(Employee.objects.order_by("employee_code").values_list("employee_code", "full_name")))
print(Employee.objects.filter(is_active=True).count())
print(list(Employee.objects.filter(full_name__icontains="asha").values_list("full_name", flat=True)))
```

Expected:

```python
[('EMP1001', 'Asha Rao'), ('EMP1002', 'Rahul Kumar')]
1
['Asha Rao']
```

The first query orders by employee code so the output order is predictable. The second counts active employees; Asha is active by default and Rahul is created as inactive. The third searches for the text asha without case sensitivity.

After recording the initial count, run the update:

```python
employee.is_active = False
employee.save(update_fields=["is_active"])
print(Employee.objects.filter(is_active=True).count())
```

Expected after this update: `0` active employees among these two sample records. Do not assume an update worked just because save() returned without an error; query the record again.

If you repeat the create example, choose new unique employee codes and emails or use get_or_create after inspecting existing records. Employee code and email are unique fields.

## 12. Troubleshooting

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

## 13. Industry scenario

An HR team needs to answer questions about employee records: how many employees are active, who joined most recently, and whether a particular employee code exists. ORM queries let the backend answer these questions without manually writing SQL for every operation.

Discuss:
- Which query should return zero or more rows?
- When is get() safer than filter()?
- Why should a query be ordered before displaying it?
- Why should a developer inspect the database after an update?

## 14. Approved mini-project — Employee Query Explorer

### Objective
Build the admin/query feature described in today's lesson using the existing Employee model in the profiles app.

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

## 15. AI-assisted learning prompts

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

## 16. Daily MCQs

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

## 17. Interview preparation

### Q1. Explain today's concept.
**Answer:** The Django ORM lets a developer work with database records through Python models and QuerySets rather than writing SQL for every operation. A QuerySet represents a database query. Many QuerySets are lazy: Django builds the query first and sends it to the database when results are needed. The ORM does not remove the need to understand SQL, indexes or query performance.

**Follow-up:** Explain it using the Employee model example from Day 34.

### Q2. Which model, field, command or query is important?
**Answer:** `profiles/models.py`, `Django shell via manage.py`. Describe the responsibility and the data behavior.

**Follow-up:** What happens if the expected record is missing or duplicated?

### Q3. How do you verify the implementation?
**Answer:** Run Django checks, inspect migration state if applicable and query actual records through admin or shell.

**Follow-up:** Why is a successful system check not enough?

**Answer:** System checks do not execute every data operation or prove the business relationship is correct.

## 18. Completion checklist

- [ ] I can explain the business rule.
- [ ] I can explain the model/query/relationship.
- [ ] I know the exact file path.
- [ ] I ran the required commands.
- [ ] I inspected the actual database behavior.
- [ ] I tested an edge case.
- [ ] I completed Product Query Explorer.
- [ ] I submitted code and evidence.
- [ ] I can explain one data integrity concern.

## 19. Independent completion test

1. Create or query records without copying the entire example.
2. Explain the file and data flow in your own words.
3. Change one admin setting or query filter and predict the result before running it.
4. Compare the actual result with your prediction.
5. Diagnose and fix one controlled mistake. Do not mark the lesson complete based only on copied code.

**Next lesson:** Day 38 — Model Relationships: One-to-One, One-to-Many and Many-to-Many

---

# Extended Beginner Lab — QuerySet Behavior and Practical ORM Patterns

## 19. What is the Django ORM?

ORM means Object-Relational Mapper.

Django ORM lets Python code work with database records through model classes and QuerySets.

Instead of writing SQL for every common operation, developers use methods such as:
- all().
- filter().
- exclude().
- get().
- create().
- update().
- delete().
- order_by().
- values().

The ORM translates supported operations into database queries.

## 20. QuerySet laziness

A QuerySet is lazy in common operations.

Example:

~~~python
employees = Employee.objects.filter(is_active=True)
~~~

This builds a QuerySet. It does not necessarily retrieve all matching records immediately.

The query is evaluated when results are needed, such as:
- Iteration.
- list().
- bool() in some contexts.
- len().
- Accessing certain results.
- Serialization/rendering that iterates over it.

Understanding evaluation helps avoid unnecessary queries.

## 21. all()

~~~python
Employee.objects.all()
~~~

Returns a QuerySet representing all records for the model.

Do not assume that all() immediately loads every record.

Use filters and pagination for large tables.

## 22. filter()

~~~python
Employee.objects.filter(is_active=True)
~~~

Returns records matching the supplied conditions.

Multiple keyword conditions are normally combined with AND.

Example:

~~~python
Employee.objects.filter(
    department="Engineering",
    is_active=True,
)
~~~

This means department is Engineering AND is_active is True.

## 23. exclude()

~~~python
Employee.objects.exclude(is_active=False)
~~~

Returns records that do not match the condition.

Read the business meaning carefully. Excluding False may also behave differently for nullable fields than an explicit True filter.

## 24. get()

~~~python
Employee.objects.get(employee_code="EMP101")
~~~

get() expects exactly one matching row.

Possible exceptions:
- Employee.DoesNotExist.
- Employee.MultipleObjectsReturned.

Use get() when the lookup is expected to be unique.

## 25. first() and last()

~~~python
Employee.objects.order_by("full_name").first()
Employee.objects.order_by("full_name").last()
~~~

first() and last() return one object or None if the QuerySet is empty.

They are useful when a missing record is an expected outcome.

## 26. exists()

~~~python
Employee.objects.filter(is_active=True).exists()
~~~

exists() checks whether at least one row matches.

It is usually clearer and more efficient than loading all matching objects merely to check whether the result is non-empty.

## 27. count()

~~~python
Employee.objects.count()
~~~

count() asks the database for the number of matching records.

Use it when you need a count rather than the full object list.

## 28. order_by()

~~~python
Employee.objects.order_by("full_name")
Employee.objects.order_by("-salary")
~~~

A field name sorts ascending. A leading minus sign sorts descending.

For stable pagination, add a unique tie-breaker such as primary key.

## 29. values()

~~~python
Employee.objects.values(
    "employee_code",
    "full_name",
)
~~~

values() returns dictionaries containing selected fields.

Use it when the code needs field values rather than full model instances.

## 30. values_list()

~~~python
Employee.objects.values_list(
    "department",
    flat=True,
).distinct()
~~~

values_list() returns tuples by default.

flat=True returns a flat list-like result for one selected field.

## 31. distinct()

distinct() removes duplicate rows from a QuerySet result.

Example:

~~~python
Employee.objects.values_list(
    "department",
    flat=True,
).distinct()
~~~

The generated SQL and behavior can depend on the database backend and selected fields.

## 32. Field lookups

Common lookups:

| Lookup | Meaning |
|---|---|
| exact | Exact match |
| iexact | Case-insensitive exact match |
| contains | Case-sensitive containment |
| icontains | Case-insensitive containment |
| gt | Greater than |
| gte | Greater than or equal |
| lt | Less than |
| lte | Less than or equal |
| in | Matches any value in a collection |
| isnull | Checks NULL |
| range | Value within a range |

Example:

~~~python
Employee.objects.filter(salary__gte=50000)
~~~

This returns employees with salary greater than or equal to 50000.

## 33. Q objects

Q objects support complex conditions.

Example:

~~~python
from django.db.models import Q

Employee.objects.filter(
    Q(full_name__icontains="asha")
    | Q(employee_code__icontains="asha")
)
~~~

The vertical bar represents OR.

Use parentheses to make complex logic easy to read.

## 34. F expressions

F expressions refer to model field values in database operations.

Example:

~~~python
from django.db.models import F

Employee.objects.filter(
    salary__gt=F("bonus")
)
~~~

This compares two database fields in the query rather than loading values and comparing them in Python.

F expressions are useful for atomic field updates and comparisons.

## 35. Update records

~~~python
Employee.objects.filter(
    department="Support"
).update(is_active=False)
~~~

update() performs a direct database update.

Important:
- It does not call each model instance's save() method.
- It does not run model save signals in the same way as saving each object.
- It can bypass custom model save logic.

Use it when a bulk update is intended and those side effects are not required.

## 36. Delete records

~~~python
Employee.objects.filter(
    is_active=False
).delete()
~~~

delete() removes matching records and may also delete related rows according to on_delete rules.

Do not run bulk deletion on important data without checking the QuerySet first.

Inspect the matching records before deleting.

## 37. Aggregation

Aggregation calculates a summary value over a QuerySet.

Example:

~~~python
from django.db.models import Avg, Max, Min

Employee.objects.aggregate(
    average_salary=Avg("salary"),
    highest_salary=Max("salary"),
    lowest_salary=Min("salary"),
)
~~~

The result is a dictionary of summary values.

## 38. Annotation

annotate() adds a calculated value to each returned object.

Example:

~~~python
from django.db.models import Count

Department.objects.annotate(
    employee_count=Count("employees")
)
~~~

The reverse relationship name must match the actual model relationship.

## 39. QuerySet chaining

QuerySet methods can be chained:

~~~python
employees = (
    Employee.objects
    .filter(is_active=True)
    .exclude(department="Archived")
    .order_by("full_name", "pk")
)
~~~

Each method returns a QuerySet-like result that can be further refined.

The final SQL is generally executed when the result is evaluated.

## 40. Inspect SQL

A QuerySet can expose the SQL representation through its query attribute for debugging:

~~~python
queryset = Employee.objects.filter(is_active=True)
print(queryset.query)
~~~

Use this to understand how ORM expressions are translated.

Do not build raw SQL by concatenating user input.

## 41. Common ORM mistakes

| Mistake | Risk | Better approach |
|---|---|---|
| Use get() for a non-unique field | MultipleObjectsReturned | Use filter() |
| Load all rows to check existence | Unnecessary data retrieval | Use exists() |
| Load all rows to count | Extra memory/work | Use count() |
| Delete without inspecting | Data loss | Review QuerySet and test |
| Use float for money | Precision issues | DecimalField |
| Use raw SQL concatenation | SQL injection risk | ORM parameters or safe raw query APIs |
| Ignore QuerySet laziness | Unexpected repeated queries | Understand evaluation |
| Use update() when save hooks matter | Custom logic may be skipped | Save instances deliberately |

## 42. Guided ORM exercise

Using the Employee model:
1. Retrieve all active employees.
2. Filter by department.
3. Search by name.
4. Find salary greater than a threshold.
5. Exclude inactive employees.
6. Retrieve one employee by employee code.
7. Count employees.
8. Check whether any employee exists.
9. List distinct departments.
10. Calculate average salary.
11. Explain when each QuerySet executes.

## 43. Self-check questions

1. What is a QuerySet?
2. What does lazy evaluation mean?
3. What is the difference between filter() and exclude()?
4. When should get() be used?
5. What does exists() do?
6. What does count() do?
7. What does order_by() do?
8. What is the difference between values() and values_list()?
9. What is a Q object?
10. What is an F expression?
11. What is aggregation?
12. What is annotation?
13. Why can bulk update skip model save behavior?
14. Why should bulk delete be used carefully?

## 44. Answers

1. A database query representation and its result interface.
2. Query execution is deferred until results are needed.
3. filter returns matches; exclude returns non-matches.
4. When exactly one matching row is expected.
5. Checks whether at least one row matches.
6. Counts matching rows.
7. Defines result ordering.
8. Dictionaries versus tuples/flat values.
9. Complex query condition object.
10. Reference to a model field in a database expression.
11. Calculates summary values.
12. Adds calculated values to each object.
13. It performs a direct SQL update rather than saving each instance.
14. It can remove many records and related data.

## 45. Independent challenge — Employee Insights with ORM

Produce:
- Active employee count.
- Department-wise employee counts.
- Highest salary.
- Average salary.
- Employees above a salary threshold.
- Distinct department list.
- Search by name or employee code.

For each result, explain the QuerySet method and what data is returned.

---

# Practice Workbook — ORM Query Planning

## 46. Predict the returned records

Given a small Employee table, write the expected records for:
1. all().
2. filter(is_active=True).
3. exclude(department="HR").
4. order_by("-salary").
5. values("full_name", "department").
6. distinct department values.

Do not run the code until you have predicted the result.

## 47. Choose the right QuerySet method

| Requirement | Method |
|---|---|
| Check whether any active employee exists | exists() |
| Count all employees | count() |
| Retrieve one unique employee | get() |
| Retrieve the first match or None | first() |
| Return selected field dictionaries | values() |
| Return selected field tuples | values_list() |
| Calculate average salary | aggregate() |

Explain why each method is more appropriate than loading all objects.

## 48. QuerySet evaluation drill

Create a QuerySet and print its representation.

Then:
- Iterate through it.
- Convert it to list.
- Call count().
- Call exists().

Observe which operations execute database queries in your environment.

Do not assume every method evaluates the same way.

## 49. Safe update drill

Before a bulk update:
1. Build the filter.
2. Inspect matching records.
3. Count matching records.
4. Confirm the business rule.
5. Run update.
6. Query again to verify.

Never run a bulk update with an empty or overly broad filter without understanding the effect.

## 50. Safe delete drill

Before a delete:
- Inspect the QuerySet.
- Count the records.
- Understand related on_delete rules.
- Use a practice database.
- Confirm the expected number of deletions.
- Verify related records afterward.

## 51. ORM performance reflection

For each page, ask:
- How many queries run?
- Are related objects accessed in loops?
- Does the template need every field?
- Is the QuerySet paginated?
- Is the ordering stable?
- Is an index justified by measured query behavior?

## 52. Final workbook submission

Submit:
- QuerySet predictions.
- Method selection table.
- Evaluation observations.
- Safe update and delete checklist.
- One example using Q.
- One example using F.
- One aggregation result.

## 53. Final ORM assessment

For one business question, show:
1. The QuerySet.
2. The expected records.
3. The ORM method used.
4. The approximate SQL operation.
5. When the QuerySet is evaluated.
6. One edge case.
7. One test.

Explain why the database should perform filtering and aggregation rather than loading every record into Python for a large dataset.


## 54. Query review rubric

For each important QuerySet, document:
- Business question.
- Filter conditions.
- Ordering.
- Fields returned.
- Related objects accessed.
- Expected row count.
- Evaluation point.
- Query count when measured.
- Index rationale if any.
- Test coverage.

Do not optimize based on assumptions alone. Measure a representative workflow and preserve the same business result.


## 55. Explain-back assessment

Without reading the notes, explain:
1. What a QuerySet represents.
2. What lazy evaluation means.
3. How filter and exclude differ.
4. When get is appropriate.
5. Why exists and count are useful.
6. How order_by works.
7. How values differs from values_list.
8. How Q represents OR conditions.
9. How F references a database field.
10. How aggregate differs from annotate.

## 56. Submission reflection

Choose one QuerySet from your project and explain the business question it answers, the SQL work it represents, when it executes and how you verified the returned records.
