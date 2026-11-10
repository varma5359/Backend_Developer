# Day 25: SQL Filtering, Sorting, Joins, Grouping and Aggregate Functions

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Day 23 — Relational Databases; Day 24 — SQL CRUD  
**Tools:** SQLite, Python 3.10+, VS Code and terminal  
**Approved mini-project:** Sales Database Analyzer

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Filter rows using WHERE.
2. Combine conditions using AND, OR and NOT.
3. Use IN, BETWEEN, LIKE and IS NULL.
4. Sort records using ORDER BY.
5. Limit the number of returned rows.
6. Combine related tables using INNER JOIN and LEFT JOIN.
7. Summarize records using COUNT, SUM, AVG, MIN and MAX.
8. Group records using GROUP BY.
9. Filter groups using HAVING.
10. Build a Sales Database Analyzer and explain each query.

## 2. Why do we need these SQL operations?

Imagine a company has thousands of orders.

A manager asks:
- Show only delivered orders.
- Find orders above ₹3,000.
- Sort orders from highest value to lowest.
- Show customer names beside their orders.
- Calculate total sales per customer.
- Show only customers whose total sales exceed ₹5,000.

Retrieving every row and calculating everything manually in Python would be inefficient. SQL allows the database to filter, combine and summarize data.

## 3. Prepare a practice database

Create `day_25/sales_analysis.py`.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")

connection.executescript("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    amount REAL NOT NULL CHECK (amount >= 0),
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Asha', 'Hyderabad'),
(2, 'Ravi', 'Bengaluru'),
(3, 'Meera', 'Hyderabad'),
(4, 'John', 'Chennai'),
(5, 'Priya', 'Vijayawada');

INSERT INTO orders VALUES
(101, 1, '2026-11-01', 5000, 'Delivered'),
(102, 1, '2026-11-03', 2500, 'Delivered'),
(103, 2, '2026-11-04', 7000, 'Pending'),
(104, 3, '2026-11-05', 1500, 'Cancelled'),
(105, 3, '2026-11-06', 3500, 'Delivered'),
(106, 2, '2026-11-07', 2000, 'Delivered');
""")

print("Practice database is ready")
```

Output:

```text
Practice database is ready
```

We use an in-memory database so the example starts fresh each time. It disappears when the connection closes.

## 4. Understand the two tables

### customers

| customer_id | customer_name | city |
|---:|---|---|
| 1 | Asha | Hyderabad |
| 2 | Ravi | Bengaluru |
| 3 | Meera | Hyderabad |
| 4 | John | Chennai |
| 5 | Priya | Vijayawada |

### orders

| order_id | customer_id | order_date | amount | status |
|---:|---:|---|---:|---|
| 101 | 1 | 2026-11-01 | 5000 | Delivered |
| 102 | 1 | 2026-11-03 | 2500 | Delivered |
| 103 | 2 | 2026-11-04 | 7000 | Pending |
| 104 | 3 | 2026-11-05 | 1500 | Cancelled |
| 105 | 3 | 2026-11-06 | 3500 | Delivered |
| 106 | 2 | 2026-11-07 | 2000 | Delivered |

customer_id in orders is a foreign key referencing customers.customer_id.

## 5. WHERE — filter rows

WHERE returns only rows that satisfy a condition.

Question: show only delivered orders.

```python
rows = connection.execute("""
SELECT order_id, amount, status
FROM orders
WHERE status = 'Delivered'
""").fetchall()

for row in rows:
    print(row)
```

Output:

```text
(101, 5000.0, 'Delivered')
(102, 2500.0, 'Delivered')
(105, 3500.0, 'Delivered')
(106, 2000.0, 'Delivered')
```

Explanation:
1. SELECT chooses the output columns.
2. FROM chooses the source table.
3. WHERE checks each row.
4. Only rows with status Delivered are returned.
5. fetchall collects all matching rows.

## 6. Comparison operators

| Operator | Meaning | Example |
|---|---|---|
| = | Equal | status = 'Delivered' |
| != or <> | Not equal | status <> 'Cancelled' |
| > | Greater than | amount > 3000 |
| < | Less than | amount < 3000 |
| >= | Greater than or equal | amount >= 3000 |
| <= | Less than or equal | amount <= 3000 |

Example:

```python
rows = connection.execute("""
SELECT order_id, amount
FROM orders
WHERE amount >= 3000
""").fetchall()

print(rows)
```

Expected output:

```text
[(101, 5000.0), (103, 7000.0), (105, 3500.0)]
```

## 7. AND — both conditions must be true

Question: find delivered orders with amount at least 3,000.

```python
rows = connection.execute("""
SELECT order_id, amount, status
FROM orders
WHERE status = 'Delivered' AND amount >= ?
""", (3000,)).fetchall()

print(rows)
```

Output:

```text
[(101, 5000.0, 'Delivered'), (105, 3500.0, 'Delivered')]
```

AND means both conditions must be true.

## 8. OR — at least one condition must be true

Question: show pending or cancelled orders.

```python
rows = connection.execute("""
SELECT order_id, status
FROM orders
WHERE status = 'Pending' OR status = 'Cancelled'
""").fetchall()

print(rows)
```

Output:

```text
[(103, 'Pending'), (104, 'Cancelled')]
```

OR returns a row when at least one condition is true.

## 9. NOT — reverse a condition

```python
rows = connection.execute("""
SELECT order_id, status
FROM orders
WHERE NOT status = 'Cancelled'
""").fetchall()

print(rows)
```

This returns rows whose status is not Cancelled.

## 10. IN — match one of several values

Instead of writing multiple OR conditions:

```sql
WHERE status = 'Delivered' OR status = 'Pending'
```

Use IN:

```python
rows = connection.execute("""
SELECT order_id, status
FROM orders
WHERE status IN ('Delivered', 'Pending')
""").fetchall()

print(rows)
```

IN is useful when matching against a list of allowed values.

## 11. BETWEEN — filter a range

```python
rows = connection.execute("""
SELECT order_id, amount
FROM orders
WHERE amount BETWEEN ? AND ?
""", (2000, 5000)).fetchall()

print(rows)
```

BETWEEN includes both endpoints. Here, values 2,000 and 5,000 are included.

## 12. LIKE — pattern matching

LIKE is used for simple text pattern matching.

| Pattern | Meaning |
|---|---|
| 'A%' | Starts with A |
| '%a' | Ends with a |
| '%sh%' | Contains sh |
| '_a%' | Second character is a |

Example:

```python
rows = connection.execute("""
SELECT customer_id, customer_name
FROM customers
WHERE customer_name LIKE 'A%'
""").fetchall()

print(rows)
```

Output:

```text
[(1, 'Asha')]
```

The percent sign represents zero or more characters. The underscore represents one character.

Case sensitivity of LIKE can vary by database and configuration. Do not assume identical behavior across SQLite and PostgreSQL for every collation.

## 13. IS NULL and IS NOT NULL

SQL uses NULL to represent missing or unknown values. Do not compare NULL using `= NULL`.

Use:

```sql
WHERE column_name IS NULL
```

or:

```sql
WHERE column_name IS NOT NULL
```

Our sample data does not contain NULL values, so try this separate table:

```python
connection.execute("""
CREATE TABLE support_tickets (
    ticket_id INTEGER PRIMARY KEY,
    assigned_to TEXT
)
""")

connection.executemany(
    "INSERT INTO support_tickets VALUES (?, ?)",
    [(1, "Anil"), (2, None), (3, "Priya")]
)

rows = connection.execute("""
SELECT ticket_id
FROM support_tickets
WHERE assigned_to IS NULL
""").fetchall()

print(rows)
```

Output:

```text
[(2,)]
```

## 14. ORDER BY — sort rows

Question: display orders from highest amount to lowest.

```python
rows = connection.execute("""
SELECT order_id, amount
FROM orders
ORDER BY amount DESC
""").fetchall()

print(rows)
```

Output:

```text
[(103, 7000.0), (101, 5000.0), (105, 3500.0), (102, 2500.0), (106, 2000.0), (104, 1500.0)]
```

- ASC means ascending.
- DESC means descending.
- ASC is the default.
- ORDER BY changes result ordering, not stored table data.

### 14.1 Sort by multiple columns

```sql
SELECT order_id, status, amount
FROM orders
ORDER BY status ASC, amount DESC;
```

First rows are grouped by the sorted status value, then amounts are sorted descending within each status group.

## 15. LIMIT — restrict the number of rows

Question: show the top three orders by amount.

```python
rows = connection.execute("""
SELECT order_id, amount
FROM orders
ORDER BY amount DESC
LIMIT 3
""").fetchall()

print(rows)
```

Output:

```text
[(103, 7000.0), (101, 5000.0), (105, 3500.0)]
```

Use a deterministic ORDER BY when selecting top rows. Without ordering, the database does not promise which rows appear first.

## 16. Aggregate functions

Aggregate functions calculate a summary across multiple rows.

| Function | Purpose | Business question |
|---|---|---|
| COUNT | Count rows/values | How many orders exist? |
| SUM | Add values | What is total order value? |
| AVG | Calculate average | What is average order value? |
| MIN | Smallest value | What is the lowest order? |
| MAX | Largest value | What is the highest order? |

### 16.1 COUNT

```python
count = connection.execute(
    "SELECT COUNT(*) FROM orders"
).fetchone()[0]

print(count)
```

Output: `6`.

COUNT(*) counts rows. COUNT(column) counts non-NULL values in that column.

### 16.2 SUM

```python
total = connection.execute(
    "SELECT SUM(amount) FROM orders"
).fetchone()[0]

print(total)
```

Output: `21500.0`.

### 16.3 AVG

```python
average = connection.execute(
    "SELECT AVG(amount) FROM orders"
).fetchone()[0]

print(average)
```

Output: `3583.3333333333335`.

### 16.4 MIN and MAX

```python
minimum, maximum = connection.execute("""
SELECT MIN(amount), MAX(amount)
FROM orders
""").fetchone()

print("Minimum:", minimum)
print("Maximum:", maximum)
```

Output:

```text
Minimum: 1500.0
Maximum: 7000.0
```

## 17. GROUP BY — summarize each group

Question: how many orders are in each status?

```python
rows = connection.execute("""
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY status
""").fetchall()

for row in rows:
    print(row)
```

Expected output:

```text
('Cancelled', 1)
('Delivered', 4)
('Pending', 1)
```

Explanation:
1. The database reads the orders.
2. GROUP BY creates one group for each status.
3. COUNT counts the rows in each group.
4. ORDER BY sorts the grouped result.

### 17.1 Total sales per status

```python
rows = connection.execute("""
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM orders
GROUP BY status
ORDER BY total_amount DESC
""").fetchall()

for row in rows:
    print(row)
```

Expected result:

```text
('Delivered', 4, 13000.0, 3250.0)
('Pending', 1, 7000.0, 7000.0)
('Cancelled', 1, 1500.0, 1500.0)
```

## 18. WHERE versus HAVING

This is a common interview topic.

- WHERE filters individual rows before grouping.
- HAVING filters groups after GROUP BY.

Example: include only delivered orders, then show groups with total value above 5,000.

```python
rows = connection.execute("""
SELECT status, SUM(amount) AS total_amount
FROM orders
WHERE status = 'Delivered'
GROUP BY status
HAVING SUM(amount) > 5000
""").fetchall()

print(rows)
```

Output:

```text
[('Delivered', 13000.0)]
```

Use WHERE for row-level conditions. Use HAVING for conditions on aggregate/group results.

## 19. JOIN — combine related tables

The customers table contains customer information. The orders table contains order information and customer_id.

A JOIN combines rows from tables using a matching condition.

### 19.1 INNER JOIN

INNER JOIN returns rows where the join condition matches in both tables.

```python
rows = connection.execute("""
SELECT
    customers.customer_name,
    orders.order_id,
    orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
ORDER BY orders.order_id
""").fetchall()

for row in rows:
    print(row)
```

Expected output:

```text
('Asha', 101, 5000.0)
('Asha', 102, 2500.0)
('Ravi', 103, 7000.0)
('Meera', 104, 1500.0)
('Meera', 105, 3500.0)
('Ravi', 106, 2000.0)
```

John and Priya do not appear because they have no matching order.

### 19.2 Understand the ON condition

```sql
ON customers.customer_id = orders.customer_id
```

This tells the database which customer row matches each order row.

Without a correct join condition, the query may create an unintended Cartesian product or incorrect results.

### 19.3 LEFT JOIN

LEFT JOIN returns every row from the left table and matching rows from the right table. If there is no match, right-side columns are NULL.

```python
rows = connection.execute("""
SELECT
    customers.customer_name,
    orders.order_id,
    orders.amount
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
ORDER BY customers.customer_id, orders.order_id
""").fetchall()

for row in rows:
    print(row)
```

John and Priya appear with NULL order columns because they have no orders.

### 19.4 INNER JOIN versus LEFT JOIN

| INNER JOIN | LEFT JOIN |
|---|---|
| Keeps matching rows from both tables | Keeps all rows from the left table |
| Unmatched left rows are excluded | Unmatched left rows remain |
| Useful when a match is required | Useful when parent rows must remain visible |

## 20. Find customers with no orders

A useful LEFT JOIN pattern:

```python
rows = connection.execute("""
SELECT customers.customer_id, customers.customer_name
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL
""").fetchall()

print(rows)
```

Expected output:

```text
[(4, 'John'), (5, 'Priya')]
```

The query keeps all customers, then selects rows where no order matched.

## 21. Aggregate after JOIN

Question: calculate total order value for each customer.

```python
rows = connection.execute("""
SELECT
    customers.customer_name,
    COUNT(orders.order_id) AS order_count,
    COALESCE(SUM(orders.amount), 0) AS total_amount
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.customer_name
ORDER BY total_amount DESC
""").fetchall()

for row in rows:
    print(row)
```

Expected output:

```text
('Ravi', 2, 9000.0)
('Asha', 2, 7500.0)
('Meera', 2, 5000.0)
('John', 0, 0)
('Priya', 0, 0)
```

Why use LEFT JOIN? We want customers with zero orders to appear too.

Why use COALESCE? SUM over no matching values can return NULL. COALESCE replaces NULL with zero here.

## 22. SQL execution order: a useful mental model

A simplified logical processing order for a SELECT query is:

```text
FROM / JOIN
    ↓
WHERE
    ↓
GROUP BY
    ↓
HAVING
    ↓
SELECT
    ↓
ORDER BY
    ↓
LIMIT
```

This helps explain why WHERE cannot normally use an aggregate result such as SUM(amount), while HAVING can filter grouped results.

Actual database query execution may be optimized internally, but this logical order is useful for understanding SQL.

## 23. Parameterized queries in filters

Use parameters when values come from a user or application variable.

```python
minimum_amount = 3000
status = "Delivered"

rows = connection.execute("""
SELECT order_id, amount
FROM orders
WHERE amount >= ? AND status = ?
""", (minimum_amount, status)).fetchall()

print(rows)
```

Do not concatenate untrusted input into SQL strings. Parameterization helps prevent SQL injection.

## 24. Mini-project — Sales Database Analyzer

### Business questions

Your manager wants answers to these questions:
1. How many customers exist?
2. How many orders exist?
3. What is the total order amount?
4. What is the average order amount?
5. Which is the highest-value order?
6. Which orders are delivered?
7. Which orders are worth at least ₹3,000?
8. Which are the top three orders?
9. How many orders exist per status?
10. What is the total order amount per status?
11. How much did each customer order?
12. Which customers have no orders?
13. Which customer has the highest total order amount?
14. What is the average order amount per customer?
15. Which statuses have total order amount above ₹5,000?

### 24.1 Suggested project structure

```text
projects/day_25_sales_database_analyzer/
├── main.py
└── README.md
```

### 24.2 Query examples

Customer count:

```sql
SELECT COUNT(*) FROM customers;
```

Order count:

```sql
SELECT COUNT(*) FROM orders;
```

Total order value:

```sql
SELECT SUM(amount) FROM orders;
```

Highest order:

```sql
SELECT order_id, amount
FROM orders
ORDER BY amount DESC
LIMIT 1;
```

Delivered orders:

```sql
SELECT order_id, amount
FROM orders
WHERE status = 'Delivered';
```

Order count by status:

```sql
SELECT status, COUNT(*)
FROM orders
GROUP BY status;
```

Customer totals:

```sql
SELECT
    customers.customer_name,
    COALESCE(SUM(orders.amount), 0) AS total_amount
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.customer_name
ORDER BY total_amount DESC;
```

### 24.3 Submission requirements

Submit:
- The Python file that creates the practice database.
- All 15 SQL queries.
- The output for each query.
- A short explanation of what each query answers.
- A README containing setup and run commands.
- At least three additional business questions you created yourself.

## 25. Common mistakes and troubleshooting

| Problem | Cause | Correction |
|---|---|---|
| Wrong rows returned | WHERE condition incorrect | Test each condition separately |
| AND returns too few rows | All conditions must be true | Check whether OR was intended |
| ORDER BY does not change table | It sorts only query output | Remember stored rows are not reordered |
| Top records change between runs | LIMIT used without deterministic ordering | Add ORDER BY with a tie-breaker |
| INNER JOIN misses customers | No matching order exists | Use LEFT JOIN if unmatched customers must remain |
| Duplicate rows after JOIN | One-to-many relationship produces multiple matches | Understand the relationship cardinality |
| SUM returns NULL | No non-NULL values in the group | Use COALESCE if zero is the desired display |
| Aggregate in WHERE causes error | WHERE filters rows before grouping | Use HAVING for aggregate conditions |
| Wrong customer totals | Incorrect JOIN or GROUP BY columns | Verify keys and group at the intended grain |
| SQL injection risk | User input concatenated into SQL | Use parameter placeholders |

## 26. Practice exercises

1. Show all orders below ₹3,000.
2. Show orders with status Delivered or Pending.
3. Find customers whose names start with M.
4. Sort customers alphabetically.
5. Display the top two highest orders.
6. Calculate minimum, maximum and average order value.
7. Count orders for each customer.
8. Find customers without orders.
9. Find the total order value for each city.
10. Show only statuses with at least two orders.
11. Explain why COUNT(order_id) is useful with LEFT JOIN.
12. Compare INNER JOIN and LEFT JOIN using the sample tables.

## 27. Interview questions

**1. What does WHERE do?**  
It filters individual rows based on conditions.

**2. Difference between WHERE and HAVING?**  
WHERE filters rows before grouping; HAVING filters groups after GROUP BY.

**3. What is ORDER BY?**  
It sorts the rows returned by a query.

**4. Difference between ASC and DESC?**  
ASC sorts ascending; DESC sorts descending.

**5. What is INNER JOIN?**  
It returns rows with matching join conditions in both tables.

**6. What is LEFT JOIN?**  
It returns all rows from the left table and matching right-side rows, using NULLs when no match exists.

**7. What is GROUP BY?**  
It groups rows sharing values so aggregate calculations can be made per group.

**8. Name five aggregate functions.**  
COUNT, SUM, AVG, MIN and MAX.

**9. What is COUNT(*)?**  
It counts rows in the result group, including rows whose individual columns may contain NULL.

**10. What does COALESCE do?**  
It returns the first non-NULL expression. It is often used to replace NULL with a display value such as zero.

**11. Why use parameterized queries?**  
To bind values separately from SQL syntax and help prevent SQL injection.

**12. Why does a LEFT JOIN sometimes produce more than one row per left-side record?**  
Because one left-side record may match multiple right-side records in a one-to-many relationship.

## 28. MCQs

**Q1. Which clause filters individual rows?**  
A. WHERE  
B. HAVING  
C. ORDER BY  
D. LIMIT  
**Answer: A.** WHERE filters rows before grouping.

**Q2. Which clause filters aggregate groups?**  
A. FROM  
B. HAVING  
C. WHERE  
D. DISTINCT  
**Answer: B.** HAVING filters grouped results.

**Q3. Which join preserves all rows from the left table?**  
A. INNER JOIN  
B. LEFT JOIN  
C. CROSS JOIN  
D. SELF JOIN only  
**Answer: B.** LEFT JOIN keeps all left-side rows.

**Q4. Which function calculates a total?**  
A. COUNT  
B. SUM  
C. MIN  
D. MAX  
**Answer: B.** SUM adds numeric values.

**Q5. Which function counts all rows?**  
A. COUNT(*)  
B. SUM(*)  
C. AVG(*)  
D. ORDER(*)  
**Answer: A.** COUNT(*) counts rows.

**Q6. What does DESC mean?**  
A. Descending order  
B. Database description  
C. Delete selected columns  
D. Duplicate search  
**Answer: A.** DESC sorts from higher to lower or reverse lexical order.

**Q7. Which pattern finds names beginning with A?**  
A. '%A'  
B. 'A%'  
C. '%A%'  
D. '_A'  
**Answer: B.** A% means starts with A.

**Q8. Which keyword checks for missing SQL values?**  
A. = NULL  
B. IS NULL  
C. == None  
D. EMPTY  
**Answer: B.** SQL uses IS NULL.

## 29. Final completion checklist

- [ ] I can filter rows with WHERE.
- [ ] I can use AND, OR, NOT, IN, BETWEEN and LIKE.
- [ ] I can check NULL values.
- [ ] I can sort using ORDER BY.
- [ ] I can limit results.
- [ ] I can use COUNT, SUM, AVG, MIN and MAX.
- [ ] I can group using GROUP BY.
- [ ] I can filter groups using HAVING.
- [ ] I can explain INNER JOIN and LEFT JOIN.
- [ ] I can calculate customer totals after a JOIN.
- [ ] I completed Sales Database Analyzer.
- [ ] I can explain my SQL queries in an interview.

**Next lesson:** Day 26 — Git, GitHub, Repositories, Commits, Branches and Merge Basics.
