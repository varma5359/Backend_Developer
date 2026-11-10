# Day 38: Model Relationships — Student, Department, Course and Profile

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Prerequisites:** Day 34 models and field types; Day 35 migrations; Day 37 ORM basics  
**Approved mini-project:** College Relationship Manager

## 1. Learning objectives
- Explain one-to-one, many-to-one and many-to-many relationships.
- Use ForeignKey, OneToOneField and ManyToManyField.
- Navigate relationships in both directions.
- Understand on_delete and related_name.

## 2. Business scenario
A college maintains departments, students, courses and student contact profiles.
- One department has many students.
- One student has one optional profile.
- A student can enroll in many courses.
- A course can have many students.

## 3. Relationship diagram
```text
Department 1 -------- many Student
Student    1 -------- 1    StudentProfile
Student    many ----- many Course
```

## 4. Define the models

**File: profiles/models.py**

Add these classes in this order after the existing Employee model. Keep the existing Employee model unchanged.

```python
from django.db import models

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

### Understand every relationship

**ForeignKey — many-to-one**

The ForeignKey is on Student because many students can point to one department. The database stores the department ID in each student's row. The Department table does not store a list of student IDs.

- Forward access: `student.department`
- Reverse access: `department.students.all()`

**OneToOneField — one-to-one**

StudentProfile has a OneToOneField to Student. The database enforces uniqueness on the student reference, so a student cannot have two profile rows through this relationship.

- From profile to student: `profile.student`
- From student to profile: `student.profile` (only when a profile exists)

**ManyToManyField — many-to-many**

Student and Course can each have multiple related records. Django creates an intermediary join table that stores student/course pairs.

- From student: `student.courses.all()`
- From course: `course.students.all()`

### on_delete behavior

- CASCADE: deleting the referenced student also deletes the dependent profile.
- PROTECT: prevents a department from being deleted while students still refer to it.
- SET_NULL: sets the foreign key to NULL; the field must allow null=True.
- SET_DEFAULT: sets the configured default value.

We use PROTECT for department because deleting a department should not silently remove students.

### Why department is nullable in this learning migration

The Employee model and database already exist from earlier days. The Student table is new, so the field is not strictly required for the lesson, but null=True and blank=True make it safe to register a student before assigning a department. The business can require assignment later using form validation.

## 5. Apply the schema

Run these commands from the folder containing manage.py:

```powershell
python manage.py check
python manage.py makemigrations profiles
python manage.py sqlmigrate profiles 0002
python manage.py migrate
python manage.py showmigrations profiles
```

The migration number may differ if the app already has other migrations. Use the filename printed by makemigrations rather than assuming it will always be 0002.

- check validates project configuration.
- makemigrations creates schema instructions.
- sqlmigrate previews SQL; it does not apply it.
- migrate applies the migration.
- showmigrations displays applied state.

Commit migration files to Git. Do not commit the local SQLite database file for shared development.

## 6. Create and inspect related records

```powershell
python manage.py shell
```

Then enter:

```python
from profiles.models import Department, Course, Student, StudentProfile

engineering = Department.objects.create(name="Engineering")
python_course = Course.objects.create(title="Python")
django_course = Course.objects.create(title="Django")

student_one = Student.objects.create(
    student_code="STU1001",
    full_name="Asha Rao",
    email="asha@example.com",
    department=engineering,
)
student_two = Student.objects.create(
    student_code="STU1002",
    full_name="Rahul Kumar",
    email="rahul@example.com",
    department=engineering,
)

student_one.courses.add(python_course, django_course)

profile = StudentProfile.objects.create(
    student=student_one,
    phone="9000000001",
)

engineering.students.all()
student_one.department
student_one.profile
student_one.courses.all()
django_course.students.all()
```

### Explain the shell code

- Import the four models so the shell can create and query records.
- Department.objects.create creates and saves a Department row.
- Course.objects.create creates two Course rows.
- Student.objects.create saves each student and links the department foreign key.
- courses.add creates relationship rows in the many-to-many join table.
- StudentProfile.objects.create creates the one-to-one profile.
- engineering.students.all uses the related_name reverse accessor.
- student_one.profile accesses the one-to-one relation.
- student_one.courses.all reads the courses for a student.
- django_course.students.all reads the students enrolled in a course.

## 7. Understand the database shape

Conceptually, the database has:
- Department table with a primary key.
- Student table with a department_id foreign key.
- Course table.
- StudentProfile table with a unique student_id foreign key.
- An automatic many-to-many join table for Student and Course.

The actual SQL table names are generated by Django and can be inspected using the database tools or migration SQL.

## 8. Common mistakes

| Symptom | Cause | Correction |
|---|---|---|
| Student has no department | department is optional in this exercise | Assign one through admin or shell |
| RelatedObjectDoesNotExist | One-to-one profile has not been created | Create StudentProfile before accessing student.profile |
| ProtectedError | Students still refer to department | Reassign/remove related records according to policy |
| IntegrityError | Duplicate unique code/email or invalid foreign key | Check existing records and constraints |
| FieldError | Incorrect related_name or field spelling | Compare exact model definitions |
| Migration asks for a default | A required field is being added to existing rows | Review a safe staged migration; do not guess an ID |

## 9. Approved mini-project — College Relationship Manager

1. Create two departments.
2. Create three courses.
3. Create at least four students.
4. Assign students to departments.
5. Enroll students in multiple courses.
6. Create a profile for at least two students.
7. Query students by department.
8. Query students enrolled in a selected course.
9. Attempt to delete a department that still has students and explain PROTECT.
10. Submit model code, migration files, shell output and a relationship diagram.

## 10. Five MCQs

**Q1. Which field represents many students belonging to one department?**  
A. OneToOneField  
B. ForeignKey  
C. ManyToManyField  
D. CharField  
**Answer: B.** ForeignKey is placed on the many side of a many-to-one relationship.

**Q2. Which field enforces one profile per student?**  
A. OneToOneField  
B. TextField  
C. ManyToManyField  
D. BooleanField  
**Answer: A.** OneToOneField enforces uniqueness on the related reference.

**Q3. What does Django use for many-to-many relationships?**  
A. A template  
B. A join/intermediary table  
C. A cookie  
D. A URL converter  
**Answer: B.** The join table stores pairs of related object IDs.

**Q4. What does PROTECT do?**  
A. Deletes related rows  
B. Prevents deletion while protected references exist  
C. Sets every field to empty  
D. Changes the primary key  
**Answer: B.** PROTECT raises an error instead of allowing deletion.

**Q5. What does related_name define?**  
A. Database name  
B. Reverse ORM accessor  
C. URL route  
D. Form label  
**Answer: B.** It defines how the related objects are accessed from the reverse side.

## 11. Interview preparation

**Q1. Explain ForeignKey, OneToOneField and ManyToManyField.**  
A ForeignKey models many-to-one, OneToOneField models one-to-one and ManyToManyField models many-to-many. Give the college example for each.

**Follow-up:** Where does the foreign key column live for a many-to-one relationship?  
**Answer:** On the many-side table, Student in this example.

**Q2. Why use PROTECT for Department?**  
It prevents deletion of a department while student records still reference it.

**Follow-up:** When might CASCADE be appropriate?  
**Answer:** When dependent data should be deleted together, such as a profile row that has no meaning without its student.

## 12. Completion checklist

- [ ] I can explain all three relationship types.
- [ ] I can identify the foreign-key column.
- [ ] I can use forward and reverse accessors.
- [ ] I applied migrations successfully.
- [ ] I verified many-to-many join behavior.
- [ ] I understand PROTECT and CASCADE.
- [ ] I completed College Relationship Manager.
- [ ] I can explain the model design without reading.

**Next lesson:** Day 39 — Django Forms and ModelForms.
