# Day 25: SQL Filtering, Sorting, Joins, Grouping and Aggregate Functions

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Day 24 — SQL CREATE, INSERT, SELECT, UPDATE and DELETE  
**Tools:** Python 3, SQLite for local practice, VS Code and terminal  
**Approved mini-project:** Sales Database Analyzer

## 1. Learning objectives

- Filter rows using WHERE.
- Sort records using ORDER BY.
- Combine related tables using INNER JOIN and LEFT JOIN.
- Group rows using GROUP BY.
- Filter grouped results using HAVING.
- Use COUNT, SUM, AVG, MIN and MAX.
- Explain query output and avoid common SQL mistakes.

## 2. Why these SQL operations matter

A backend application rarely needs every row in a database. An HR portal may need employees from one department. A shopping application may need orders above a certain value. A manager may want total sales per customer.

SQL provides operations to retrieve the exact information required.

## 3. Prepare a practice database

Create a file named `sales_analysis.py`.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")

db.executescript("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Asha', 'Hyderabad'),
(2, 'Ravi', 'Bengaluru'),
(3, 'Meera', 'Hyderabad'),
(4, 'John', 'Chennai');

INSERT INTO orders VALUES
(101, 1, 5000, 'Delivered'),
(102, 1, 2500, 'Delivered'),
(103, 2, 7000, 'Pending'),
(104, 3, 1500, 'Cancelled'),
(105, 3, 3500, 'Delivered');
""")
print("Practice tables and sample rows are ready")
```

Output: `Practice tables and sample rows are ready`

The connection uses an in-memory database. It is created for this program run and disappears when the connection closes.

## 4. WHERE — filter rows

`WHERE` selects only rows that satisfy a condition.

```python
rows = db.execute(
    "SELECT order_id, amount, status FROM orders WHERE amount >= ?",
    (3000,)
).fetchall()

for row in rows:
    print(row)
```

Output:
```text
(101, 5000.0, 'Delivered')
(103, 7000.0, 'Pending')
(105, 3500.0, 'Delivered')
```

Explanation:
1. SELECT chooses the columns to return.
2. FROM identifies the source table.
3. WHERE filters rows before they are returned.
4. The question mark is a parameter placeholder.
5. The tuple `(3000,)` supplies the value safely.
6. fetchall() returns all matching rows.

Use parameters for values. Do not build SQL by concatenating untrusted user input.

## 5. Combine conditions

```python
rows = db.execute(
    "SELECT order_id, amount FROM orders WHERE amount >= ? AND status = ?",
    (3000, "Delivered")
).fetchall()

print(rows)
```

Output:
```text
[(101, 5000.0), (105, 3500.0)]
```

- AND requires both conditions to be true.
- OR requires at least one condition to be true.
- IN checks whether a value belongs to a supplied list.
- BETWEEN checks an inclusive range in SQL.
- LIKE performs pattern matching.

## 6. ORDER BY — sort rows

```python
rows = db.execute(
    "SELECT order_id, amount FROM orders ORDER BY amount DESC"
).fetchall()

print(rows)
```

Output:
```text
[(103, 7000.0), (101, 5000.0), (105, 3500.0), (102, 2500.0), (104, 1500.0)]
```

- ASC sorts ascending and is the default.
- DESC sorts descending.
- You can sort by more than one column.
- Sorting does not change the stored table; it changes the order of the result.

## 7. Aggregate functions

Aggregate functions summarize multiple rows.

| Function | Purpose | Example question |
|---|---|---|
| COUNT | Count rows or non-null values | How many orders exist? |
| SUM | Add numeric values | What is total order value? |
| AVG | Calculate average | What is average order value? |
| MIN | Find smallest value | What is the lowest order? |
| MAX | Find largest value | What is the highest order? |

```python
summary = db.execute("""
SELECT
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount,
    MIN(amount) AS minimum_amount,
    MAX(amount) AS maximum_amount
FROM orders
""").fetchone()

print(summary)
```

Expected result:
```text
(5, 19500.0, 3900.0, 1500.0, 7000.0)
```

COUNT(*) counts rows. SUM adds the amount values. AVG calculates their average. MIN and MAX return the smallest and largest amount.

## 8. GROUP BY — summarize each category

GROUP BY creates groups that share the same value.

```python
rows = db.execute("""
SELECT status, COUNT(*) AS order_count, SUM(amount) AS total_amount
FROM orders
GROUP BY status
ORDER BY total_amount DESC
""").fetchall()

for row in rows:
    print(row)
```

Expected output:
```text
('Delivered', 3, 11000.0)
('Pending', 1, 7000.0)
('Cancelled', 1, 1500.0)
```

The database groups rows by status and calculates the aggregates for each group.

## 9. HAVING — filter groups

WHERE filters individual rows. HAVING filters groups after GROUP BY.

```python
rows = db.execute("""
SELECT status, SUM(amount) AS total_amount
FROM orders
GROUP BY status
HAVING SUM(amount) >= ?
""", (5000,)).fetchall()

print(rows)
```

Expected output:
```text
[('Delivered', 11000.0), ('Pending', 7000.0)]
```

Use WHERE for row-level conditions and HAVING for aggregate/group conditions.

## 10. JOIN — combine related tables

The orders table stores customer_id. The customers table stores customer details. JOIN combines related rows using the matching key.

### INNER JOIN

```python
rows = db.execute("""
SELECT customers.customer_name, orders.order_id, orders.amount
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
ORDER BY orders.order_id
""").fetchall()

for row in rows:
    print(row)
```

INNER JOIN returns rows where a matching customer and order exist.

### LEFT JOIN

```python
rows = db.execute("""
SELECT customers.customer_name, orders.order_id
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
ORDER BY customers.customer_id
""").fetchall()

for row in rows:
    print(row)
```

LEFT JOIN keeps every customer, including John who has no order. The order columns for John are NULL.

| Join | Result |
|---|---|
| INNER JOIN | Only matching rows |
| LEFT JOIN | Every row from left table and matching right rows |
| RIGHT JOIN | Every row from right table where supported |
| FULL OUTER JOIN | Matching and non-matching rows from both sides where supported |

## 11. Full business query

Find each customer's delivered order count and delivered revenue.

```python
rows = db.execute("""
SELECT
    c.customer_name,
    COUNT(o.order_id) AS delivered_orders,
    SUM(o.amount) AS delivered_revenue
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.status = ?
GROUP BY c.customer_id, c.customer_name
ORDER BY delivered_revenue DESC
""", ("Delivered",)).fetchall()

for row in rows:
    print(row)
```

Expected output:
```text
('Asha', 2, 7500.0)
('Meera', 1, 3500.0)
```

This query joins customers and orders, filters delivered orders, groups them by customer, calculates the count and revenue, then sorts the result.

## 12. SQL execution order — conceptual view

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
```

This logical order helps explain why WHERE cannot normally filter on an aggregate alias that is calculated later, while HAVING is designed for grouped conditions.

## 13. Common mistakes

| Mistake | Why it is wrong | Better approach |
|---|---|---|
| Using HAVING for every filter | Row filtering is more naturally done before grouping | Use WHERE for row-level conditions |
| Forgetting JOIN condition | Can produce a Cartesian product | Join using matching keys |
| Using COUNT(*) after LEFT JOIN without understanding null rows | May count unmatched left rows | Count a non-null right-side key when counting matches |
| Omitting GROUP BY columns | Query may fail or produce ambiguous results | Group by the selected non-aggregated columns |
| Concatenating user input into SQL | Can create SQL injection vulnerabilities | Use parameterized queries |
| Assuming ORDER BY changes stored data | It only sorts the result | Use UPDATE only when changing data |
| Ignoring NULL values | Aggregates treat NULL differently from ordinary values | Understand NULL and use COALESCE where appropriate |

## 14. Industry scenario

A retail manager wants to understand total sales by customer, compare order statuses and identify customers without orders. A backend developer uses WHERE, JOIN, GROUP BY and aggregate functions to produce reliable summaries for dashboards and APIs.

## 15. Approved mini-project — Sales Database Analyzer

**Objective:** Analyze a small customer and sales database using filtering, sorting, joins, grouping and aggregate functions.

Requirements:
1. Create customers and orders tables.
2. Add at least five customers and ten orders.
3. Include multiple order statuses.
4. Filter orders above a selected amount.
5. Sort orders by amount.
6. Calculate count, sum and average.
7. Group sales by status.
8. Join customer and order information.
9. Use LEFT JOIN to identify customers without orders.
10. Write a short business interpretation of the results.

Suggested structure:
```text
projects/day_25/
├── README.md
├── sales_analysis.py
└── evidence/
    ├── query_results.txt
    └── business_insights.md
```

Validation:
- [ ] WHERE returns only matching rows.
- [ ] ORDER BY produces the requested order.
- [ ] Aggregates match manual calculations for a small sample.
- [ ] GROUP BY produces one summary per category.
- [ ] HAVING filters groups.
- [ ] INNER JOIN and LEFT JOIN produce different expected results.
- [ ] Queries use parameter placeholders for values.

## 16. Five daily MCQs

**Q1. Which clause filters individual rows before grouping?**  
A. WHERE  
B. HAVING  
C. ORDER BY  
D. LIMIT  
**Answer: A.** WHERE filters rows before grouping.

**Q2. Which clause sorts a query result?**  
A. GROUP BY  
B. ORDER BY  
C. JOIN  
D. INSERT  
**Answer: B.** ORDER BY controls result ordering.

**Q3. Which join keeps every row from the left table?**  
A. INNER JOIN  
B. CROSS JOIN  
C. LEFT JOIN  
D. SELF JOIN  
**Answer: C.** LEFT JOIN retains all left-table rows.

**Q4. Which function calculates the sum of a numeric column?**  
A. COUNT  
B. AVG  
C. MAX  
D. SUM  
**Answer: D.** SUM adds numeric values.

**Q5. Which clause filters groups after aggregation?**  
A. HAVING  
B. WHERE  
C. FROM  
D. INSERT  
**Answer: A.** HAVING filters grouped results.

## 17. Interview preparation

**Q1. What is the difference between WHERE and HAVING?**  
WHERE filters rows before grouping; HAVING filters groups after aggregation.

**Q2. What is the difference between INNER JOIN and LEFT JOIN?**  
INNER JOIN returns matching rows. LEFT JOIN retains every row from the left table and matching values from the right table.

**Q3. Why use GROUP BY?**  
To calculate summaries for categories, such as total sales by customer or count of orders by status.

**Q4. How can SQL injection be prevented?**  
Use parameterized queries, validate input and apply least-privilege database permissions.

**Q5. What happens when a customer has no orders in a LEFT JOIN?**  
The customer remains in the result, and the order columns are NULL.

## 18. Completion checklist

- [ ] Explain WHERE and HAVING.
- [ ] Explain ORDER BY.
- [ ] Use aggregate functions.
- [ ] Write GROUP BY queries.
- [ ] Compare INNER JOIN and LEFT JOIN.
- [ ] Complete Sales Database Analyzer.
- [ ] Answer five MCQs and interview questions.
- [ ] Submit query evidence and business interpretation.

**Next lesson:** Day 26 — Git, GitHub, repositories, commits, branches and merge basics.
