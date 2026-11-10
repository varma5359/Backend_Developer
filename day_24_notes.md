# Day 24: SQL Fundamentals — CREATE, INSERT, SELECT, UPDATE and DELETE

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Day 23 — Relational Databases and Keys  
**Tools:** SQLite, Python 3.10+, VS Code and terminal  
**Approved mini-project:** Employee Database Manager

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain what SQL is and why backend developers use it.
2. Distinguish DDL and DML at a beginner level.
3. Create a database table using CREATE TABLE.
4. Insert records using INSERT INTO.
5. Retrieve records using SELECT.
6. Update records using UPDATE and WHERE.
7. Delete records using DELETE and WHERE.
8. Use constraints and parameterized queries.
9. Commit or roll back a transaction in a simple SQLite workflow.
10. Build an Employee Database Manager.

## 2. What is SQL?

SQL stands for Structured Query Language.

It is used to define, retrieve and manipulate data in relational databases.

A backend application may use SQL to:
- Create database structures.
- Add employee records.
- Retrieve products.
- Update customer information.
- Delete obsolete records.
- Calculate business summaries.

Django ORM can generate SQL for you, but a backend developer should understand SQL because it helps with database design, debugging and performance analysis.

## 3. The five operations

| Operation | Purpose |
|---|---|
| CREATE | Create database objects such as tables |
| INSERT | Add rows |
| SELECT | Retrieve rows |
| UPDATE | Modify existing rows |
| DELETE | Remove rows |

Remember:
- CREATE TABLE defines structure.
- INSERT adds data.
- SELECT reads data.
- UPDATE changes data.
- DELETE removes data.

## 4. DDL and DML

SQL statements are often grouped by their purpose.

**DDL (Data Definition Language)** defines or changes database structures.

Examples: CREATE, ALTER, DROP.

**DML (Data Manipulation Language)** changes data stored in tables.

Examples: INSERT, UPDATE, DELETE. SELECT is often classified separately as DQL (Data Query Language), though terminology varies by learning resource.

## 5. Create a table

Syntax:

```sql
CREATE TABLE table_name (
    column_name data_type constraint,
    column_name data_type constraint
);
```

Example:

```sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
);
```

Explanation:
- employees is the table name.
- employee_id identifies each row.
- name cannot be NULL.
- department cannot be NULL.
- salary stores a numeric value in this SQLite exercise.

For real financial applications, choose an exact decimal type such as PostgreSQL NUMERIC rather than relying on floating-point arithmetic.

## 6. Run SQL using Python SQLite

Create `day_24/main.py`:

```python
import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

connection.commit()
print("Employees table is ready")

connection.close()
```

Run:

```powershell
python main.py
```

Output:

`Employees table is ready`

A file named employees.db is created in the current directory.

## 7. INSERT — add records

SQL syntax:

```sql
INSERT INTO employees (employee_id, name, department, salary)
VALUES (101, 'Anil', 'IT', 45000);
```

The column list tells the database which values are being supplied.

### 7.1 Insert through Python safely

```python
connection.execute(
    "INSERT INTO employees (employee_id, name, department, salary) VALUES (?, ?, ?, ?)",
    (101, "Anil", "IT", 45000)
)
connection.commit()
```

The question marks are placeholders. The values are passed separately.

Do not construct SQL by joining user input into the query string.

### 7.2 Insert multiple rows

```python
employees = [
    (102, "Priya", "HR", 42000),
    (103, "Ravi", "IT", 50000),
    (104, "Meera", "Finance", 48000)
]

connection.executemany(
    "INSERT INTO employees (employee_id, name, department, salary) VALUES (?, ?, ?, ?)",
    employees
)
connection.commit()
```

executemany runs the same parameterized statement for multiple sets of values.

## 8. SELECT — retrieve records

Basic SQL:

```sql
SELECT * FROM employees;
```

The asterisk means all columns.

It is often better to specify the columns you need:

```sql
SELECT employee_id, name, department
FROM employees;
```

Python example:

```python
rows = connection.execute(
    "SELECT employee_id, name, department, salary FROM employees"
).fetchall()

for row in rows:
    print(row)
```

fetchall returns all rows in the result. Each row is returned as a tuple by default.

### 8.1 fetchone

```python
row = connection.execute(
    "SELECT name, salary FROM employees WHERE employee_id = ?",
    (101,)
).fetchone()

print(row)
```

fetchone returns one row or None if no row matches.

### 8.2 fetchmany

```python
cursor = connection.execute(
    "SELECT employee_id, name FROM employees ORDER BY employee_id"
)

rows = cursor.fetchmany(2)
print(rows)
```

fetchmany returns up to the requested number of rows from the remaining result set.

## 9. UPDATE — modify records

SQL:

```sql
UPDATE employees
SET salary = 47000
WHERE employee_id = 101;
```

The WHERE condition identifies which row to update.

Python:

```python
cursor = connection.execute(
    "UPDATE employees SET salary = ? WHERE employee_id = ?",
    (47000, 101)
)
connection.commit()

print("Rows changed:", cursor.rowcount)
```

rowcount reports the number of rows modified according to the database driver.

### 9.1 Why WHERE is important

Dangerous query:

```sql
UPDATE employees SET department = 'IT';
```

This updates every row in the table because there is no WHERE clause.

Safer query:

```sql
UPDATE employees
SET department = 'IT'
WHERE employee_id = 102;
```

Before running an update, run a SELECT with the same WHERE condition to inspect the target rows.

## 10. DELETE — remove records

SQL:

```sql
DELETE FROM employees
WHERE employee_id = 104;
```

Python:

```python
cursor = connection.execute(
    "DELETE FROM employees WHERE employee_id = ?",
    (104,)
)
connection.commit()

print("Rows deleted:", cursor.rowcount)
```

### 10.1 DELETE without WHERE

```sql
DELETE FROM employees;
```

This deletes all rows from the table. The table structure remains.

Do not run destructive queries without checking the target data and having an appropriate backup or recovery plan.

## 11. WHERE and basic conditions

Day 25 explores filtering in more detail. For now, understand that WHERE selects the rows affected or returned.

Examples:

```sql
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees WHERE salary >= 45000;
SELECT * FROM employees WHERE employee_id = 101;
```

Comparison operators include:
- = equal.
- != or <> not equal.
- > greater than.
- < less than.
- >= greater than or equal.
- <= less than or equal.

## 12. Parameterized queries and SQL injection

Never build a SQL query using untrusted input concatenation.

Unsafe:

```python
name = input("Employee name: ")
query = "SELECT * FROM employees WHERE name = '" + name + "'"
rows = connection.execute(query).fetchall()
```

If a user enters crafted SQL text, the query structure can be altered. This is a SQL injection risk.

Safe:

```python
name = input("Employee name: ")

rows = connection.execute(
    "SELECT * FROM employees WHERE name = ?",
    (name,)
).fetchall()
```

The database driver binds the value as data rather than treating it as part of the SQL syntax.

Use placeholders for values. Table names and column names generally cannot be supplied as ordinary value parameters; if dynamic identifiers are required, use a strict allowlist.

## 13. Transactions: commit and rollback

A transaction groups database operations into a unit of work.

- commit saves the transaction.
- rollback cancels uncommitted changes in the current transaction.

Example:

```python
try:
    connection.execute(
        "UPDATE employees SET salary = ? WHERE employee_id = ?",
        (52000, 103)
    )

    connection.execute(
        "UPDATE employees SET salary = ? WHERE employee_id = ?",
        (46000, 102)
    )

    connection.commit()
    print("Changes saved")

except sqlite3.Error:
    connection.rollback()
    print("Changes rolled back")
    raise
```

If a database error occurs before commit, rollback cancels the uncommitted changes in this transaction.

Transactions are essential for multi-step business operations. Day 77 later covers database transactions and atomic operations in a Django context.

## 14. Complete Employee Database Manager

### 14.1 Requirements

Create a small application that:
1. Creates an employees table.
2. Adds employees.
3. Lists all employees.
4. Finds one employee by ID.
5. Updates an employee salary.
6. Deletes an employee.
7. Uses parameterized SQL.
8. Handles duplicate IDs and missing employees.

### 14.2 Project structure

```text
day_24_employee_database/
├── main.py
└── README.md
```

### 14.3 Complete runnable code

```python
import sqlite3


def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL CHECK (salary >= 0)
        )
    """)
    connection.commit()


def add_employee(connection, employee_id, name, department, salary):
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if salary < 0:
        raise ValueError("Salary cannot be negative")

    connection.execute(
        """
        INSERT INTO employees
        (employee_id, name, department, salary)
        VALUES (?, ?, ?, ?)
        """,
        (employee_id, name.strip(), department.strip(), salary)
    )
    connection.commit()


def list_employees(connection):
    rows = connection.execute("""
        SELECT employee_id, name, department, salary
        FROM employees
        ORDER BY employee_id
    """).fetchall()

    for row in rows:
        print(row)


def get_employee(connection, employee_id):
    return connection.execute(
        """
        SELECT employee_id, name, department, salary
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id,)
    ).fetchone()


def update_salary(connection, employee_id, new_salary):
    if new_salary < 0:
        raise ValueError("Salary cannot be negative")

    cursor = connection.execute(
        "UPDATE employees SET salary = ? WHERE employee_id = ?",
        (new_salary, employee_id)
    )
    connection.commit()

    if cursor.rowcount == 0:
        print("Employee not found")
    else:
        print("Salary updated")


def delete_employee(connection, employee_id):
    cursor = connection.execute(
        "DELETE FROM employees WHERE employee_id = ?",
        (employee_id,)
    )
    connection.commit()

    if cursor.rowcount == 0:
        print("Employee not found")
    else:
        print("Employee deleted")


def main():
    connection = sqlite3.connect("employees.db")

    try:
        create_table(connection)

        add_employee(connection, 101, "Anil", "IT", 45000)
        add_employee(connection, 102, "Priya", "HR", 42000)
        add_employee(connection, 103, "Ravi", "IT", 50000)

        print("ALL EMPLOYEES")
        list_employees(connection)

        print("FIND EMPLOYEE 102")
        print(get_employee(connection, 102))

        print("UPDATE EMPLOYEE 101")
        update_salary(connection, 101, 47000)
        print(get_employee(connection, 101))

        print("DELETE EMPLOYEE 103")
        delete_employee(connection, 103)

        print("FINAL EMPLOYEE LIST")
        list_employees(connection)

    except sqlite3.IntegrityError as error:
        connection.rollback()
        print("Database constraint error:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
```

### 14.4 Important note about rerunning

The example uses fixed employee IDs. Running the script again against the same employees.db file will attempt to insert duplicate IDs and raise an integrity error.

For a repeatable classroom run, choose one of these approaches:
- Delete employees.db before each fresh demonstration.
- Add a separate setup/reset routine for practice data.
- Add carefully designed upsert logic only after explaining its behavior.

Do not hide duplicate errors by blindly ignoring them. They teach an important primary-key rule.

### 14.5 Run

```powershell
python main.py
```

The program creates the table, inserts sample employees, reads records, updates one salary, deletes one employee and displays the final list.

## 15. SQL command summary

| SQL | Purpose | Example |
|---|---|---|
| CREATE TABLE | Define a table | CREATE TABLE employees (...) |
| INSERT INTO | Add a row | INSERT INTO employees (...) VALUES (...) |
| SELECT | Read rows | SELECT name FROM employees |
| UPDATE | Modify rows | UPDATE employees SET salary=... WHERE id=... |
| DELETE | Remove rows | DELETE FROM employees WHERE id=... |

## 16. Common mistakes and troubleshooting

| Problem | Cause | Correction |
|---|---|---|
| UNIQUE constraint failed | Duplicate primary key or unique value | Use a new ID or inspect existing record |
| NOT NULL constraint failed | Required value missing | Supply required value |
| no such table | Table creation did not run or wrong database file | Verify connection path and setup |
| UPDATE changes every row | WHERE clause missing | Preview target rows and add WHERE |
| DELETE removes every row | WHERE clause missing | Verify condition before deletion |
| SQL injection risk | Untrusted text concatenated into SQL | Use placeholders |
| Changes disappear | Transaction not committed | Commit successful changes |
| Partial work remains after error | Rollback not used | Roll back failed transaction |
| Wrong number of parameters | Placeholder count and tuple length differ | Match each ? to one value |

## 17. Practice exercises

1. Create a departments table.
2. Insert five employees.
3. Retrieve only employee names.
4. Update the salary for one employee ID.
5. Delete one employee by ID.
6. Attempt to insert a duplicate ID.
7. Attempt to insert a negative salary.
8. Write a safe search by employee name using a placeholder.
9. Demonstrate commit and rollback.
10. Explain what happens when UPDATE has no WHERE clause.

## 18. Interview questions

**1. What is SQL?**  
Structured Query Language is used to define, retrieve and manipulate data in relational databases.

**2. What is CREATE TABLE?**  
A DDL statement that defines a table and its columns/constraints.

**3. What is INSERT?**  
A statement that adds rows to a table.

**4. What is SELECT?**  
A query that retrieves data from one or more tables.

**5. What is UPDATE?**  
A statement that modifies existing rows.

**6. What is DELETE?**  
A statement that removes rows from a table.

**7. Why is WHERE important in UPDATE and DELETE?**  
It limits which rows are changed or removed. Without it, all rows can be affected.

**8. What is SQL injection?**  
An attack where untrusted input changes the intended SQL query structure.

**9. How do parameterized queries help?**  
They bind input as values rather than SQL syntax.

**10. Difference between commit and rollback?**  
Commit saves the transaction; rollback cancels uncommitted changes.

## 19. MCQs

**Q1. Which statement creates a table?**  
A. CREATE TABLE  
B. INSERT  
C. UPDATE  
D. DELETE  
**Answer: A.** CREATE TABLE defines database structure.

**Q2. Which statement retrieves data?**  
A. DROP  
B. SELECT  
C. DELETE  
D. ALTER  
**Answer: B.** SELECT reads rows.

**Q3. Which clause limits the rows changed by UPDATE?**  
A. WHERE  
B. ORDER BY  
C. GROUP BY  
D. DISTINCT  
**Answer: A.** WHERE filters target rows.

**Q4. Which statement adds a new row?**  
A. SELECT  
B. INSERT  
C. UPDATE  
D. DELETE  
**Answer: B.** INSERT adds records.

**Q5. Which method saves a transaction?**  
A. rollback  
B. commit  
C. close only  
D. fetchall  
**Answer: B.** commit saves the changes.

**Q6. Which practice helps prevent SQL injection?**  
A. String concatenation  
B. Parameterized queries  
C. Removing all spaces  
D. Printing SQL only  
**Answer: B.** Parameters separate values from query syntax.

## 20. Completion checklist

- [ ] I can explain SQL and its purpose.
- [ ] I can create a table.
- [ ] I can insert one and many rows.
- [ ] I can retrieve rows using SELECT.
- [ ] I can update a selected row.
- [ ] I can delete a selected row.
- [ ] I understand why WHERE is critical.
- [ ] I use parameterized queries.
- [ ] I understand commit and rollback.
- [ ] I completed Employee Database Manager.

**Next lesson:** Day 25 — SQL Filtering, Sorting, Joins, Grouping and Aggregate Functions.
