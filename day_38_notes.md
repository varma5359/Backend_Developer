# Day 38: Django Model Relationships — ForeignKey, OneToOneField and ManyToManyField

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours  
**Level:** Beginner to Intermediate  
**Prerequisites:** Day 34 models and field types; Day 35 migrations; Day 37 ORM querying  
**Environment:** Windows 10/11, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** College Relationship Manager

> **How to use this lesson:** Read one section, make the change in the named file, save it, run the command and compare your result with the expected result. Do not paste all code at once. If a step fails, stop and use the troubleshooting table before continuing.

---

## 1. What you will build today

A college wants to store students, departments, courses and student contact profiles.

The college's rules are:

1. A department can have many students.
2. Each student belongs to one department for this exercise.
3. A student can have one optional contact profile.
4. A student can enroll in many courses.
5. Each course can contain many students.

By the end, you will be able to:

- Explain why related data is stored in separate tables.
- Choose ForeignKey, OneToOneField or ManyToManyField for a business rule.
- Define each relationship in Django models.
- Explain where the foreign key is stored.
- Create and apply a migration safely.
- Create sample records without creating duplicates every time you repeat the lesson.
- Query relationships in both directions.
- Understand PROTECT and CASCADE behavior.
- Complete an independent relationship-design challenge.

## 2. First understand the problem without Django

Imagine storing every detail in one large spreadsheet:

| Student code | Student name | Department | Courses | Phone |
|---|---|---|---|---|
| STU1001 | Asha Rao | Engineering | Python, Django | 9000000001 |
| STU1002 | Rahul Kumar | Engineering | Python | 9000000002 |
| STU1003 | Meera Das | Business | Excel, SQL | 9000000003 |

This looks simple, but it creates problems:

- The department name is repeated for every student.
- Course names are stored as multiple values in one cell.
- Updating a course name may require changing many rows.
- A student may have no phone number yet.
- It is difficult to enforce that a student has only one profile.

Relational databases solve this by separating entities into tables and connecting them with keys.

### 2.1 What is a primary key?

A primary key uniquely identifies one row in a table. Django normally creates an automatic primary key if you do not define one.

For example:

| id | name |
|---:|---|
| 1 | Engineering |
| 2 | Business |

The value `id=1` identifies the Engineering department row.

### 2.2 What is a foreign key?

A foreign key is a column that refers to a row in another table.

For example, the Student table can store `department_id`:

| id | student_code | full_name | department_id |
|---:|---|---|---:|
| 1 | STU1001 | Asha Rao | 1 |
| 2 | STU1002 | Rahul Kumar | 1 |
| 3 | STU1003 | Meera Das | 2 |

Both Asha and Rahul point to the same department row. This is why the relationship is described as **many students to one department**.

---

## 3. Understand the three relationship types

### 3.1 ForeignKey — many-to-one

**Business rule:** One department has many students. Each student points to one department.

```text
Department
    1
    |
    | referenced by
    |
    many
Student
```

The ForeignKey is placed on the **many side**, which is Student.

Django example:

```python
department = models.ForeignKey(
    Department,
    on_delete=models.PROTECT,
    related_name="students",
)
```

Meaning:

- `Department` is the model being referenced.
- `on_delete=models.PROTECT` prevents deletion of a department while students still refer to it.
- `related_name="students"` gives us a convenient reverse accessor.

### 3.2 OneToOneField — one-to-one

**Business rule:** A student can have one profile, and one profile belongs to one student.

```text
Student  1 -------- 1  StudentProfile
```

Django example:

```python
student = models.OneToOneField(
    Student,
    on_delete=models.CASCADE,
    related_name="profile",
)
```

The database enforces uniqueness on the profile's student reference. Two profile rows cannot point to the same student.

### 3.3 ManyToManyField — many-to-many

**Business rule:** A student can enroll in many courses, and a course can have many students.

```text
Student  many ----- many  Course
```

Django example:

```python
courses = models.ManyToManyField(
    Course,
    related_name="students",
    blank=True,
)
```

Django creates an intermediary join table. That table stores pairs of student IDs and course IDs.

Example:

| student_id | course_id |
|---:|---:|
| 1 | 1 |
| 1 | 2 |
| 2 | 1 |

Asha (student 1) is enrolled in Python (course 1) and Django (course 2). Rahul (student 2) is enrolled in Python.

### 3.4 Quick decision table

| Requirement | Django field | Where is the relationship stored? |
|---|---|---|
| Many students belong to one department | ForeignKey | On Student, the many side |
| One profile belongs to one student | OneToOneField | On StudentProfile, with a unique reference |
| Students can take many courses and courses have many students | ManyToManyField | In an intermediary join table |

**Interview shortcut:** Ask how many records on each side may be connected. One-to-many → ForeignKey. Exactly one-to-one → OneToOneField. Many-to-many → ManyToManyField.

---

## 4. Prepare the existing project

Do not create a second Django project today.

### Step 1 — Open the correct folder

Open the existing `student_portal` folder in VS Code.

### Step 2 — Open PowerShell terminal

In VS Code choose **Terminal → New Terminal**.

### Step 3 — Confirm your location

Run:

```powershell
Get-Location
Get-ChildItem
```

You should see `manage.py` in the current folder. If you do not, move into the folder that contains it using `Set-Location`.

### Step 4 — Activate the virtual environment

If the environment is in the project root:

```powershell
.\.venv\Scripts\Activate.ps1
```

The terminal prompt should show `(.venv)`. If PowerShell blocks activation, follow the environment troubleshooting instructions from Day 27; do not disable security settings globally.

### Step 5 — Confirm the versions and project

```powershell
python --version
python -m django --version
python manage.py check
```

Expected check result for a correctly configured project:

```text
System check identified no issues (0 silenced).
```

This check validates project configuration. It does not yet prove that the new relationships work.

---

## 5. Inspect the existing model file before editing

Open:

`profiles/models.py`

Day 34 introduced an Employee model. Keep it. We are adding a separate college domain schema for relationship practice.

The file should ultimately contain:

- Existing `Employee` model.
- New `Department` model.
- New `Course` model.
- New `Student` model.
- New `StudentProfile` model.

Do not delete Employee. Do not paste the same model class twice.

## 6. Add the relationship models

In `profiles/models.py`, keep the existing import:

```python
from django.db import models
```

Add these model classes after the existing Employee class:

```python
class Department(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    student_code = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="students",
        null=True,
        blank=True,
    )
    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True,
    )

    def __str__(self):
        return f"{self.student_code} - {self.full_name}"


class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Profile: {self.student.full_name}"
```

### 6.1 Understand Department

```python
class Department(models.Model):
```

- `class Department` defines a Python class named Department.
- `models.Model` tells Django this class is a database model.
- Django creates a table for this model when its migration is applied.

```python
name = models.CharField(max_length=80, unique=True)
```

- `name` is the field name.
- `CharField` stores bounded text.
- `max_length=80` allows up to 80 characters.
- `unique=True` prevents duplicate department names at the database level after migration.

```python
def __str__(self):
    return self.name
```

This gives the object a readable label in the admin and shell instead of a generic object representation.

### 6.2 Understand Course

Course uses the same idea. The title is unique so the same course title cannot be inserted twice.

### 6.3 Understand Student

`student_code` is a unique student identifier. `full_name` stores the student's name. `email` uses EmailField and is unique.

The Department ForeignKey is optional in this teaching schema:

- `null=True` allows the database column to store NULL.
- `blank=True` allows forms to accept an empty value.
- This lets us create a student before assigning a department. A real college may choose to require department assignment in its form or business rules.

The `courses` field is many-to-many. We set `blank=True` so a student can initially exist without course enrollments.

### 6.4 Understand StudentProfile

The profile points to Student using OneToOneField. The relationship is stored on the StudentProfile table. The unique constraint means one student cannot have two profile rows.

### 6.5 Why do we keep Employee?

Employee was the model introduced in Day 34 and used in the earlier examples. This lesson introduces a second business domain because student/department/course relationships make all three relationship types easy to understand. Both sets of models can exist in the same Django app during this training project.

---

## 7. Understand on_delete

Django requires an on_delete behavior for ForeignKey and OneToOneField.

| Option | What happens when the referenced row is deleted? | Example |
|---|---|---|
| CASCADE | Delete dependent rows too | Delete a student's profile when that student is deleted |
| PROTECT | Block deletion while references exist | Do not delete a department while students belong to it |
| SET_NULL | Set the relationship column to NULL | Keep a student but clear the department; requires null=True |
| SET_DEFAULT | Replace the reference with the configured default | Move to a designated default department |

In this lesson:

- StudentProfile uses CASCADE because the profile belongs to the student.
- Student.department uses PROTECT because deleting a department should not silently remove or orphan student records.

**Important:** on_delete is a Django ORM deletion policy. Do not assume every database backend represents it as an identical SQL ON DELETE rule.

---

## 8. Create and apply a migration

A model edit changes Python code. It does not automatically change the database.

Run these commands from the folder containing manage.py.

### Step 1 — Check the project

```powershell
python manage.py check
```

Expected:

```text
System check identified no issues (0 silenced).
```

If there is an error, fix it before creating a migration.

### Step 2 — Generate the migration

```powershell
python manage.py makemigrations profiles
```

Django prints a new migration filename and the operations it plans to perform. Your migration number may not be the same as another learner's because it depends on earlier migrations.

Expected kind of output (the exact filename and operations may differ):

```text
Migrations for 'profiles':
  profiles\migrations\000X_....py
    + Create model Course
    + Create model Department
    + Create model Student
    + Create model StudentProfile
```

Do not create this migration file manually. Django generates it.

### Step 3 — Inspect the migration file

Open the exact new file printed by the command under:

`profiles/migrations/`

Check that it includes the four new models and the relationship fields. The generated migration number is not guaranteed to be 0002.

### Step 4 — Apply the migration

```powershell
python manage.py migrate
```

Django applies unapplied migrations to the configured database.

### Step 5 — Verify migration state

```powershell
python manage.py showmigrations profiles
```

A tick `[X]` beside the new migration means it has been applied.

### Step 6 — Run the system check again

```powershell
python manage.py check
```

**Never delete migration files or reset the database just because a migration number differs from this example.** Read the generated output and inspect the migration state.

---

## 9. Create sample records safely

We will use Django shell. The sample code uses `get_or_create()` so that running it again does not fail simply because the unique sample records already exist.

### Step 1 — Open Django shell

```powershell
python manage.py shell
```

You should see the Python interactive prompt, usually `>>>`.

### Step 2 — Import the models

Type:

```python
from profiles.models import Department, Course, Student, StudentProfile
```

This imports the model classes into the interactive shell.

### Step 3 — Create or retrieve a department

```python
engineering, created = Department.objects.get_or_create(name="Engineering")
business, created = Department.objects.get_or_create(name="Business")
```

`get_or_create` first looks for a matching row. If it exists, Django returns it. If it does not exist, Django creates it. The returned `created` value tells you whether a new row was inserted.

### Step 4 — Create or retrieve courses

```python
python_course, created = Course.objects.get_or_create(title="Python")
django_course, created = Course.objects.get_or_create(title="Django")
sql_course, created = Course.objects.get_or_create(title="SQL")
```

### Step 5 — Create or retrieve students

```python
asha, created = Student.objects.get_or_create(
    student_code="STU1001",
    defaults={
        "full_name": "Asha Rao",
        "email": "asha@example.com",
        "department": engineering,
    },
)

rahul, created = Student.objects.get_or_create(
    student_code="STU1002",
    defaults={
        "full_name": "Rahul Kumar",
        "email": "rahul@example.com",
        "department": engineering,
    },
)

meera, created = Student.objects.get_or_create(
    student_code="STU1003",
    defaults={
        "full_name": "Meera Das",
        "email": "meera@example.com",
        "department": business,
    },
)
```

The unique student code is used to find each student. The `defaults` dictionary supplies values only when a new student needs to be created.

If you already created one of these codes with different details, inspect and update that record deliberately. Do not delete data blindly.

### Step 6 — Add course enrollments

```python
asha.courses.add(python_course, django_course)
rahul.courses.add(python_course)
meera.courses.add(sql_course)
```

This writes relationship rows to the many-to-many intermediary table. It does not put a comma-separated list into the Student table.

### Step 7 — Create student profiles

```python
asha_profile, created = StudentProfile.objects.get_or_create(
    student=asha,
    defaults={"phone": "9000000001"},
)

rahul_profile, created = StudentProfile.objects.get_or_create(
    student=rahul,
    defaults={"phone": "9000000002"},
)
```

A student can exist without a profile because the relationship is stored on StudentProfile. The reverse accessor is only available after a profile row exists.

---

## 10. Query the relationships in both directions

Run each query in the same Django shell.

### 10.1 Department to students — reverse ForeignKey

```python
list(engineering.students.order_by("full_name").values_list("full_name", flat=True))
```

Expected:

```python
['Asha Rao', 'Rahul Kumar']
```

Why? The ForeignKey declares `related_name="students"`. That is why the Department object can access its related Student records using `engineering.students`.

### 10.2 Student to department — forward ForeignKey

```python
asha.department.name
```

Expected:

```python
'Engineering'
```

The student stores a reference to the department.

### 10.3 Student to courses — forward ManyToMany

```python
list(asha.courses.order_by("title").values_list("title", flat=True))
```

Expected:

```python
['Django', 'Python']
```

### 10.4 Course to students — reverse ManyToMany

```python
list(python_course.students.order_by("full_name").values_list("full_name", flat=True))
```

Expected:

```python
['Asha Rao', 'Rahul Kumar']
```

### 10.5 Student to profile — reverse OneToOne

```python
asha.profile.phone
```

Expected:

```python
'9000000001'
```

If a profile does not exist, accessing `student.profile` raises a related-object exception. This is expected behavior, not evidence that the Student row is missing.

Check safely:

```python
hasattr(meera, "profile")
```

Expected for this sample:

```python
False
```

### 10.6 Profile to student — forward OneToOne

```python
asha_profile.student.full_name
```

Expected:

```python
'Asha Rao'
```

### 10.7 Inspect counts

```python
Department.objects.count()
Course.objects.count()
Student.objects.count()
StudentProfile.objects.count()
```

If this is a fresh database containing only these sample records, expected counts are 2, 3, 3 and 2. If you already had records from earlier attempts, the totals may be larger. Use the filtered sample queries above to verify the lesson data.

### Step 8 — Exit the shell

```python
exit()
```

This returns you to PowerShell.

---

## 11. What does the database contain?

Conceptually, Django has these tables:

| Table | Important columns |
|---|---|
| Department | id, name |
| Student | id, student_code, full_name, email, department_id |
| Course | id, title |
| StudentProfile | id, student_id, phone |
| Student-Course intermediary table | student_id, course_id |

The `department_id` column is on Student because Student is the many side. The `student_id` column in StudentProfile is unique because the relationship is one-to-one. The many-to-many join table stores pairs of IDs.

Django generates actual table names. If you want to inspect SQL, use the migration filename created on your machine and the `sqlmigrate` command taught on Day 35.

---

## 12. Understand common errors

| Error or symptom | Why it happens | What to do |
|---|---|---|
| `ModuleNotFoundError: No module named 'profiles'` | Command is being run from the wrong project or app is not installed | Confirm manage.py location and `INSTALLED_APPS` |
| `no such table` | Migration was not applied to the database being used | Run showmigrations, then migrate |
| `IntegrityError` for student_code | The unique code already exists | Query that code; reuse or choose a new unique code |
| `IntegrityError` for email | The email is already used | Check existing Student rows before creating another |
| `RelatedObjectDoesNotExist` on student.profile | That student has no StudentProfile row | Create the profile or check with hasattr |
| `ProtectedError` | Students still reference the department | Reassign students or follow the college's data-retention policy |
| `FieldError` | A field name or related_name is misspelled | Compare the query with the exact model definition |
| Migration asks for a default | A required field is being added to an existing table | Review the model and migration plan; do not guess a default ID |
| Query returns no students | Filter value or sample data differs | Inspect the exact code and query all rows first |

### A safe debugging routine

1. Read the complete traceback from the bottom upward.
2. Find the first line that points to your own file.
3. Confirm the current project folder and active virtual environment.
4. Check the model field spelling.
5. Check migration state.
6. Re-run the smallest failing query.
7. Compare the actual result with the expected result in this lesson.

---

## 13. Guided project — College Relationship Manager

Complete these tasks using the models from this lesson.

1. Create two departments: Engineering and Business.
2. Create three courses: Python, Django and SQL.
3. Create at least four students.
4. Assign at least two students to the same department.
5. Enroll one student in at least two courses.
6. Enroll one course with at least two students.
7. Create profiles for two students and leave one student without a profile.
8. Display the students in a department.
9. Display the courses for one student.
10. Display the students enrolled in one course.
11. Demonstrate that a student without a profile does not have a reverse profile object.
12. Explain why deleting a department with students is blocked.

### Acceptance criteria

- All four models exist and pass `python manage.py check`.
- Migrations are generated and applied.
- The database contains the required records.
- Forward and reverse relationship queries return the expected records.
- The student without a profile is handled without crashing the whole exercise.
- The learner can explain where each relationship is stored.

### Evidence to submit

- Updated `profiles/models.py`.
- New migration file(s).
- Terminal output for the verification queries.
- A relationship diagram drawn by you.
- Short explanation of why each relationship field was selected.

---

## 14. Independent challenge — Training Institute Enrollment

Now solve a different scenario without copying the College code line by line.

A training institute has:

- Batches.
- Learners.
- Modules.
- Learner contact cards.

Business rules:

1. One batch contains many learners.
2. One learner can have one contact card.
3. One learner can study many modules.
4. One module can be studied by many learners.

### Your tasks

1. Decide which model should contain each relationship field.
2. Write a relationship diagram before coding.
3. Create the four models in a new practice app or a separate branch of your work.
4. Add meaningful `related_name` values.
5. Choose suitable on_delete behavior and explain the choice.
6. Create at least three learners and two batches.
7. Enroll learners in multiple modules.
8. Query in both directions.
9. Test a learner without a contact card.
10. Write three test cases for duplicate or missing data.

### Hints

- The ForeignKey belongs on Learner because many learners belong to one batch.
- The OneToOneField belongs on the contact-card model because one card belongs to one learner.
- The ManyToManyField can be declared on Learner to represent module enrollments.
- Choose deletion behavior based on the business rule; do not select CASCADE automatically.

### Self-check rubric (20 marks)

| Area | Marks |
|---|---:|
| Correct relationship diagram | 4 |
| Correct Django field types and placement | 6 |
| Migration and sample records | 3 |
| Forward and reverse queries | 4 |
| Explanation of deletion behavior and edge cases | 3 |
| **Total** | **20** |

Target: 15/20 or higher. If you score below 15, revisit Sections 3, 6, 7 and 10, then attempt the challenge again.

---

## 15. Check your understanding

**Q1. Where should the ForeignKey be placed when one department has many students?**  
Answer: On Student, the many side. It stores the department reference.

**Q2. Why does StudentProfile use OneToOneField?**  
Answer: A student should have at most one profile, and the database must enforce that uniqueness.

**Q3. Does ManyToManyField store a comma-separated list of course names in Student?**  
Answer: No. Django uses an intermediary table containing related record IDs.

**Q4. What does related_name="students" allow?**  
Answer: It provides reverse access such as department.students.all() or course.students.all().

**Q5. Why can student.profile raise an exception?**  
Answer: The reverse OneToOne relation does not exist until a StudentProfile row is created.

**Q6. What is the difference between makemigrations and migrate?**  
Answer: makemigrations creates migration instructions; migrate applies them to the database.

**Q7. What does PROTECT do in the Department relationship?**  
Answer: It prevents deleting a department while students still reference it.

**Q8. Why does get_or_create help in this practice?**  
Answer: It lets us repeat sample setup without inserting another row with the same unique lookup value.

---

## 16. Interview preparation

### Explain all three relationship types in one answer

A ForeignKey represents many-to-one. For example, many students can belong to one department, so the foreign key is stored on Student. A OneToOneField represents one-to-one, such as one profile for one student. A ManyToManyField represents many-to-many, such as students enrolling in multiple courses while each course has multiple students. Django uses an intermediary table for many-to-many relationships.

### Follow-up questions

1. What is the difference between forward and reverse relationship access?
2. Why is the ForeignKey stored on the many side?
3. What database constraint makes OneToOneField different from ForeignKey?
4. What is the purpose of related_name?
5. What happens when a referenced object is deleted with PROTECT?
6. Why should a developer inspect migrations before applying a schema change?

### Practical interview demonstration

Without reading the code, demonstrate:

- One forward ForeignKey query.
- One reverse ForeignKey query.
- One forward ManyToMany query.
- One reverse ManyToMany query.
- One forward and reverse OneToOne query.
- One example of a missing profile and how to handle it.

---

## 17. Completion checklist

Do not mark this lesson complete until you can check all critical items:

- [ ] I can explain ForeignKey, OneToOneField and ManyToManyField with business examples.
- [ ] I know which side stores a ForeignKey.
- [ ] I understand the intermediary table.
- [ ] I can explain related_name and reverse access.
- [ ] I can explain CASCADE and PROTECT.
- [ ] I added the models without deleting Employee.
- [ ] I generated and applied migrations.
- [ ] I created or retrieved the sample records.
- [ ] I reproduced the expected query outputs.
- [ ] I handled a student without a profile.
- [ ] I completed the independent challenge or documented what I could not finish.
- [ ] I can explain my design without memorizing the paragraph.

**Next lesson:** Day 39 — Django Forms and ModelForms.  
**Carry-forward:** The Student model and its fields are now available for the registration form lessons. Keep the migration files and database; do not recreate the project.
