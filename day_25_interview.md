# Day 25: Interview Questions — SQL Filtering, Sorting, Joins, Grouping and Aggregate Functions

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Related notes:** [Day 25 class notes](day_25_notes.md)  
**Approved mini-project:** Sales Database Analyzer

## Core questions

### Q1. What is the difference between WHERE and HAVING?
**Answer:** WHERE filters individual rows before grouping. HAVING filters grouped results after aggregation.

**Example:** WHERE can select delivered orders. HAVING can keep only customer groups whose total revenue exceeds a threshold.

**Follow-up:** Can HAVING be used without GROUP BY? Some SQL engines permit it, but for normal grouped reporting use GROUP BY and HAVING together.

### Q2. What is the difference between INNER JOIN and LEFT JOIN?
**Answer:** INNER JOIN returns rows with matching records on both sides. LEFT JOIN returns every row from the left table and matching right-side values; unmatched right-side columns are NULL.

**Follow-up:** How would you find customers who have no orders? Use LEFT JOIN and filter where the order key is NULL.

### Q3. What does GROUP BY do?
**Answer:** It groups rows with the same selected key values so aggregate functions can calculate summaries for each group.

### Q4. Explain COUNT, SUM and AVG.
**Answer:** COUNT counts rows or non-null values, SUM adds numeric values and AVG calculates the average of numeric values.

### Q5. Why is parameterized SQL important?
**Answer:** Parameters keep supplied values separate from SQL syntax and help prevent SQL injection. Validate business rules as well.

## Scenario-based questions

### Q6. A retail manager wants revenue by customer and order status. How would you design the query?
**Suggested answer:** Join customers and orders on customer_id, group by customer and status, calculate SUM(amount) and COUNT(order_id), and sort by revenue.

### Q7. The report omits customers who have never placed an order. What should you inspect?
**Suggested answer:** Check whether the query uses INNER JOIN. Use LEFT JOIN if all customers must appear, including those with no orders.

## Practical coding questions

1. Write a query to return orders above 3,000.
2. Sort orders from highest to lowest amount.
3. Calculate total revenue.
4. Calculate total revenue per customer.
5. Return customers with no orders.
6. Explain why WHERE and HAVING are not interchangeable.

## Project viva — Sales Database Analyzer

Be ready to explain:
- Table design and keys.
- Why the join condition is needed.
- How NULL values affect LEFT JOIN results.
- Why COUNT(order_id) may differ from COUNT(*).
- How aggregate values were validated manually.
- How query parameters were supplied.
- What business decision the output could support.

## Common mistakes

| Mistake | Correct understanding |
|---|---|
| WHERE filters aggregate results | HAVING filters grouped aggregates |
| INNER JOIN keeps unmatched left rows | LEFT JOIN is needed for that |
| GROUP BY sorts results | ORDER BY sorts results |
| SQL string concatenation is safe | Use parameter placeholders |
| NULL is the same as zero | NULL represents missing/unknown value |

## Rapid revision
- WHERE — row filter.
- ORDER BY — result sorting.
- INNER JOIN — matching rows.
- LEFT JOIN — all left rows plus matches.
- GROUP BY — category grouping.
- HAVING — group filter.
- COUNT — count.
- SUM — total.
- AVG — mean.

## Final checklist
- [ ] Explain WHERE and HAVING.
- [ ] Compare INNER JOIN and LEFT JOIN.
- [ ] Write a grouped aggregate query.
- [ ] Explain NULL behavior.
- [ ] Explain SQL parameterization.
- [ ] Present Sales Database Analyzer and its evidence.
