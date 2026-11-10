# Day 23: Relational Database Concepts, Tables, Primary Keys and Foreign Keys

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations, OOP and basic data structures  
**Tools:** Python 3.10+, SQLite (built into Python), VS Code and terminal  
**Approved mini-project:** Student Database Designer

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why applications need databases.
2. Distinguish a database, table, row and column.
3. Understand records, fields and data types.
4. Explain primary keys and foreign keys.
5. Identify one-to-one, one-to-many and many-to-many relationships.
6. Design a simple relational database for students and courses.
7. Understand constraints such as NOT NULL and UNIQUE.
8. Create tables and insert related records using SQLite.
9. Identify why duplicate data and invalid references cause problems.

## 2. Why do applications need databases?

Imagine a college portal.

It stores:
- Thousands of students.
- Hundreds of courses.
- Student contact information.
- Course enrollment records.
- Attendance and marks.

If the program stores everything in Python variables, the data normally disappears when the program stops. Files can store data, but managing relationships, searching, updating and concurrent access becomes difficult as the application grows.

A database provides an organized way to store, retrieve and manage data.

A backend developer commonly uses a database to store persistent application information.

## 3. What is a database?

A **database** is an organized collection of data that can be stored and accessed electronically.

Examples:
- Student database.
- Employee database.
- Banking database.
- E-commerce database.
- Hospital appointment database.

A database management system (DBMS) is software that manages databases.

Examples include PostgreSQL, MySQL, SQLite, SQL Server and Oracle Database.

In this pathway:
- PostgreSQL is the primary database technology.
- SQLite is used for local exercises because Python includes SQLite support without requiring a separate database server.

## 4. What is a relational database?

A relational database organizes data into tables and represents relationships between tables using keys.

Example college database:

```text
STUDENTS                 COURSES
+----+-------+           +----+------------+
| id | name  |           | id | title      |
+----+-------+           +----+------------+
| 1  | Asha  |           | 10 | Python     |
| 2  | Ravi  |           | 20 | Django     |
+----+-------+           +----+------------+

ENROLLMENTS
+------------+-----------+
| student_id | course_id |
+------------+-----------+
| 1          | 10        |
| 1          | 20        |
| 2          | 10        |
+------------+-----------+
```

The tables represent different concepts. The enrollment table connects students and courses.

## 5. Database, table, row and column

| Term | Meaning | Example |
|---|---|---|
| Database | Container/organized collection of data | college_db |
| Table | Data organized for one entity or relationship | students |
| Row | One record | Asha's record |
| Column | One attribute/field | student_name |
| Value | Data in a cell | Asha |

Example students table:

| student_id | name | city |
|---:|---|---|
| 1 | Asha | Hyderabad |
| 2 | Ravi | Vijayawada |
| 3 | Meera | Chennai |

- One row represents one student.
- The name column stores student names.
- The value Hyderabad is in the city column for Asha.

## 6. What is a primary key?

A **primary key** uniquely identifies each row in a table.

Example:

| student_id | name |
|---:|---|
| 101 | Asha |
| 102 | Ravi |
| 103 | Meera |

student_id is the primary key.

Primary key rules:
- Each row must have a unique key value.
- A primary key cannot be NULL.
- A table has one primary key constraint, which may contain one or more columns.
- A primary key should identify a record reliably.

### 6.1 Why not use name as a primary key?

Two students may have the same name. A name can also change.

An ID is usually a better identifier because it is designed to be unique and stable.

### 6.2 Primary key example

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

This defines student_id as the primary key.

## 7. What is a foreign key?

A **foreign key** is a column or group of columns that references a candidate key—commonly a primary key—in another table.

Example:

students:

| student_id | name |
|---:|---|
| 101 | Asha |
| 102 | Ravi |

enrollments:

| enrollment_id | student_id | course |
|---:|---:|---|
| 1 | 101 | Python |
| 2 | 102 | Django |

The student_id in enrollments references student_id in students.

The foreign key helps prevent an enrollment from referring to a student record that does not exist, when enforcement is enabled.

### 7.1 Foreign key syntax

```sql
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_name TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

## 8. Primary key versus foreign key

| Primary key | Foreign key |
|---|---|
| Identifies a row in its own table | References a key in another or the same table |
| Must be unique | Can repeat unless additional constraints prevent it |
| Cannot be NULL | NULL may be allowed if column definition permits |
| One primary key constraint per table | A table can have multiple foreign key constraints |
| Example: students.student_id | Example: enrollments.student_id |

A foreign key does not automatically have to be named id. Good column names make the relationship clear.

## 9. What is referential integrity?

Referential integrity means relationships between records remain valid.

Suppose students contains IDs 101 and 102.

An enrollment row with student_id 999 should not be accepted if the foreign key is enforced, because student 999 does not exist.

This protects the database from orphaned references.

## 10. Relationship types

### 10.1 One-to-one

One record in table A relates to at most one record in table B, and vice versa.

Example:
- One user has one profile.
- One profile belongs to one user.

A database design can enforce this with a foreign key plus a UNIQUE constraint.

### 10.2 One-to-many

One record in the parent table can relate to multiple records in the child table.

Example:
- One department has many employees.
- Each employee belongs to one department.

```text
DEPARTMENT
id | name
1  | IT
2  | HR

EMPLOYEE
id | name  | department_id
1  | Anil  | 1
2  | Priya | 2
3  | Ravi  | 1
```

department_id in employee references department.id.

### 10.3 Many-to-many

Many records in table A can relate to many records in table B.

Example:
- A student can enroll in multiple courses.
- A course can have multiple students.

A relational database normally represents this with a junction/bridge table.

```text
STUDENTS 1 ---- many ENROLLMENTS many ---- 1 COURSES
```

## 11. Why use a junction table?

Do not store several course IDs as comma-separated text in one student row.

Weak design:

| student_id | name | course_ids |
|---:|---|---|
| 1 | Asha | 10,20,30 |

Problems:
- Searching one course becomes difficult.
- Foreign key validation cannot easily apply to each embedded value.
- Adding/removing one course requires string manipulation.
- Data is not represented as individual relationships.

Better design:

students table, courses table and enrollments table.

Each enrollment is one row. This makes the relationship explicit.

## 12. Constraints: rules applied to data

Constraints help the database protect data quality.

| Constraint | Meaning |
|---|---|
| PRIMARY KEY | Uniquely identifies a row |
| FOREIGN KEY | Requires a valid referenced key |
| NOT NULL | Value cannot be NULL |
| UNIQUE | Values must be unique within the constraint |
| CHECK | Value must satisfy a condition |
| DEFAULT | Supplies a value when one is omitted |

Example:

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    sku TEXT UNIQUE,
    price REAL NOT NULL CHECK (price >= 0),
    active INTEGER NOT NULL DEFAULT 1
);
```

This says:
- Product ID uniquely identifies the product.
- Name cannot be NULL.
- SKU must be unique when supplied.
- Price cannot be negative.
- Active defaults to 1.

## 13. Data types: first look

SQL database systems support data types such as:
- INTEGER.
- DECIMAL / NUMERIC.
- VARCHAR / TEXT.
- DATE / TIMESTAMP.
- BOOLEAN (implementation varies).

SQLite uses a flexible type system with storage classes and type affinity. PostgreSQL has stricter and richer native data types. The examples today use SQLite syntax for easy local execution.

For money in production systems, prefer an exact decimal representation such as PostgreSQL NUMERIC rather than binary floating-point types.

## 14. Build the Student Database Designer

We will create:
- students table.
- courses table.
- enrollments table.

### 14.1 Project structure

```text
day_23_student_database/
├── main.py
└── README.md
```

### 14.2 Create the database and tables

Save as `main.py`:

```python
import sqlite3

connection = sqlite3.connect("college.db")
connection.execute("PRAGMA foreign_keys = ON")

connection.executescript("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_on TEXT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
""")

connection.commit()
print("Database and tables created")
connection.close()
```

Run:

```powershell
python main.py
```

Output:

`Database and tables created`

A file named college.db is created in the current folder.

### 14.3 Understand the code

- sqlite3 imports Python's SQLite interface.
- connect opens or creates a database file.
- PRAGMA foreign_keys = ON enables foreign key enforcement for this SQLite connection.
- executescript runs multiple SQL statements.
- CREATE TABLE IF NOT EXISTS creates a table only if it does not already exist.
- PRIMARY KEY identifies rows.
- FOREIGN KEY declares relationships.
- commit saves the changes.
- close releases the connection.

Important: SQLite foreign key enforcement is configured per connection. Enable it on every connection used by the application.

## 15. Insert related records

Add this code before commit and close:

```python
connection.executemany(
    "INSERT INTO students (student_id, name, city) VALUES (?, ?, ?)",
    [
        (101, "Asha", "Hyderabad"),
        (102, "Ravi", "Vijayawada"),
        (103, "Meera", "Chennai")
    ]
)

connection.executemany(
    "INSERT INTO courses (course_id, title) VALUES (?, ?)",
    [
        (10, "Python"),
        (20, "Django"),
        (30, "SQL")
    ]
)

connection.executemany(
    "INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES (?, ?, ?)",
    [
        (101, 10, "2026-11-10"),
        (101, 20, "2026-11-10"),
        (102, 10, "2026-11-10")
    ]
)

connection.commit()
print("Sample records inserted")
```

The question marks are parameter placeholders. The values are passed separately so SQLite can bind them safely.

If you run the insert statements again, primary key and unique constraints will prevent duplicates. For a repeatable demo, either create a fresh database or add appropriate cleanup/upsert logic.

## 16. Inspect table structure and data

Run a query:

```python
students = connection.execute(
    "SELECT student_id, name, city FROM students ORDER BY student_id"
).fetchall()

for student in students:
    print(student)
```

Expected rows:

```text
(101, 'Asha', 'Hyderabad')
(102, 'Ravi', 'Vijayawada')
(103, 'Meera', 'Chennai')
```

Check the enrollment table:

```python
rows = connection.execute(
    "SELECT student_id, course_id, enrolled_on FROM enrollments"
).fetchall()

for row in rows:
    print(row)
```

## 17. Test referential integrity

Try inserting an enrollment for a student who does not exist:

```python
connection.execute(
    "INSERT INTO enrollments VALUES (?, ?, ?)",
    (999, 10, "2026-11-10")
)
connection.commit()
```

With foreign key enforcement enabled, SQLite raises an IntegrityError because student 999 does not exist.

Run this invalid test separately or inside a try/except block so it does not interrupt your main demonstration.

## 18. Test uniqueness and NOT NULL

Try inserting a duplicate course title:

```python
connection.execute(
    "INSERT INTO courses (course_id, title) VALUES (?, ?)",
    (40, "Python")
)
```

The UNIQUE constraint rejects the duplicate title.

Try inserting a student without a name:

```python
connection.execute(
    "INSERT INTO students (student_id, name, city) VALUES (?, ?, ?)",
    (104, None, "Hyderabad")
)
```

The NOT NULL constraint rejects the row.

These are database-level protections. Application validation should also provide clear feedback before a query is attempted.

## 19. Why relationships matter in Django

Django models represent database tables through Python classes.

Later, you will learn fields such as:
- models.AutoField / BigAutoField.
- models.CharField.
- models.ForeignKey.
- models.OneToOneField.
- models.ManyToManyField.

Today, understand the relational idea first. Django's field classes are a framework interface for defining database structure.

## 20. Mini-project deliverables

For Student Database Designer, submit:
1. A simple ER diagram or table relationship sketch.
2. A students table with a primary key.
3. A courses table with a primary key.
4. An enrollments junction table.
5. Foreign keys from enrollments to students and courses.
6. At least three student records.
7. At least three course records.
8. At least three enrollment records.
9. Evidence of a rejected invalid foreign key.
10. A README explaining the relationships.

## 21. Common mistakes and troubleshooting

| Problem | Likely cause | Correction |
|---|---|---|
| Foreign key insert succeeds unexpectedly | SQLite foreign keys not enabled | Run PRAGMA foreign_keys = ON on the connection |
| Duplicate primary key | ID already exists | Choose a unique ID |
| NOT NULL constraint failed | Required value omitted | Supply a valid value |
| UNIQUE constraint failed | Duplicate unique value | Check existing values |
| No such table | Table not created or wrong database file | Check path and table creation |
| Database is locked | Another connection/transaction holds a lock | Close unused connections and keep transactions short |
| Orphan relationship | Foreign key not declared or enforced | Add and enable the foreign key |
| Many-to-many stored as comma-separated IDs | Relationship not normalized | Use a junction table |

## 22. Practice exercises

1. Design departments and employees as a one-to-many relationship.
2. Design users and profiles as a one-to-one relationship.
3. Design students and courses using a junction table.
4. Add a CHECK constraint for marks between 0 and 100.
5. Attempt a duplicate primary key and inspect the error.
6. Attempt a foreign key insert referencing a missing student.
7. Draw the relationship between orders and products using an order_items junction table.
8. Explain why an employee name should not normally be the primary key.

## 23. Interview questions

**1. What is a relational database?**  
A database that organizes data in tables and represents relationships using keys.

**2. What is a table?**  
A structure containing rows and columns for a particular entity or relationship.

**3. What is a primary key?**  
A column or set of columns that uniquely identifies each row in a table.

**4. What is a foreign key?**  
A column or set of columns referencing a candidate key in another or the same table.

**5. What is referential integrity?**  
A rule that keeps references between related records valid.

**6. What is a one-to-many relationship?**  
One parent record can be related to many child records.

**7. How do you represent many-to-many in a relational database?**  
Use a junction table containing foreign keys to the related tables.

**8. What is a UNIQUE constraint?**  
A constraint that prevents duplicate values for the constrained column or column combination.

**9. Difference between primary key and foreign key?**  
A primary key identifies a row in its own table; a foreign key references a key in another or the same table.

**10. Why use a junction table?**  
It represents each many-to-many relationship as a separate row and supports foreign key validation.

## 24. MCQs

**Q1. What identifies a row uniquely?**  
A. Primary key  
B. Foreign key only  
C. Column name  
D. Database filename  
**Answer: A.** A primary key uniquely identifies a row.

**Q2. What does a foreign key do?**  
A. References a key in a related table  
B. Formats a text file  
C. Creates a Python class  
D. Sorts records automatically  
**Answer: A.** It represents a database relationship.

**Q3. What table commonly represents many-to-many relationships?**  
A. Junction table  
B. Temporary variable  
C. Log file  
D. HTML table only  
**Answer: A.** A junction table connects the two entity tables.

**Q4. Which constraint prevents NULL values?**  
A. NOT NULL  
B. ORDER BY  
C. GROUP BY  
D. LIMIT  
**Answer: A.** NOT NULL requires a value.

**Q5. Which relationship fits one department with many employees?**  
A. One-to-one  
B. One-to-many  
C. Many-to-many only  
D. No relationship  
**Answer: B.** A department can be referenced by many employee records.

**Q6. What does referential integrity protect?**  
A. Valid relationships between records  
B. Python indentation  
C. Network speed  
D. File naming  
**Answer: A.** It prevents invalid references when constraints are enforced.

## 25. Completion checklist

- [ ] I can explain database, table, row and column.
- [ ] I can explain primary and foreign keys.
- [ ] I understand referential integrity.
- [ ] I can identify one-to-one, one-to-many and many-to-many.
- [ ] I can design a junction table.
- [ ] I understand common constraints.
- [ ] I created the college database in SQLite.
- [ ] I tested invalid references and duplicate values.
- [ ] I completed Student Database Designer.

**Next lesson:** Day 24 — SQL Fundamentals: CREATE, INSERT, SELECT, UPDATE and DELETE.
