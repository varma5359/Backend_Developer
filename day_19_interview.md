# Day 19: Interview Questions — SQL filtering, sorting, joins, grouping and aggregate functions

**Pathway:** Python Backend Developer (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools

## 1. Core technical questions

### Q1. What is the difference between WHERE and HAVING?
**Answer:**
- WHERE filters rows before grouping; HAVING filters grouped results after aggregation.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A retail manager wants total sales by customer and highest-value orders.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q2. What is the difference between INNER JOIN and LEFT JOIN?
**Answer:**
- INNER JOIN returns matching rows; LEFT JOIN retains all rows from the left table, filling unmatched right-side columns with NULL.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A retail manager wants total sales by customer and highest-value orders.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q3. What is the main purpose of WHERE?
**Answer:** WHERE filters rows, ORDER BY sorts, JOIN combines related tables, GROUP BY aggregates categories. COUNT, SUM, AVG, MIN and MAX summarize records.

**Follow-up:** What would go wrong if the concept were misunderstood?

### Q4. Which tools are appropriate for this lesson?
**Answer:** Python and VS Code for demonstrations, terminal commands for execution, and SQLite for local practice and PostgreSQL for later production database work.

**Follow-up:** What would change in a deployed Django service?

### Q5. How do you verify the implementation?
**Answer:** Define expected inputs and outputs, run normal and edge cases, inspect actual responses or database state, and document failures.

**Follow-up:** Why is a successful command not always proof of correct business behavior?

## 2. Scenario-based interview questions

### Q6. A retail manager wants total sales by customer and highest-value orders. What should the developer verify?
**Answer:**
- Define the expected result before implementation.
- Check that the chosen WHERE behavior matches the requirement.
- Validate inputs and inspect actual results.
- Record reproducible test evidence.

**Follow-up:** What error case would you test first?

### Q7. A beginner's output differs from the expected result. How do you troubleshoot?
**Answer:**
- Reproduce the issue with the smallest sample.
- Check tool installation, file location and input.
- Inspect exceptions, response status or SQL result.
- Change one variable at a time and rerun.
- Document the fix and regression test.

**Follow-up:** How would you explain the root cause to a non-technical colleague?

## 3. Project and practical questions

### Q8. Explain your Sales Database Analyzer.
**Answer:**
- I defined the inputs, operations and expected outputs.
- I implemented a small demonstration of sql filtering, sorting, joins, grouping and aggregate functions.
- I tested normal and edge cases.
- I captured evidence and documented limitations.
- I did not assume a learning exercise was production-ready.

**Follow-up:** Which part would you improve first for production use?

### Q9. What mistakes should you avoid in this project?
**Answer:**
- Skipping validation.
- Failing to verify observable results.
- Mixing unrelated responsibilities.
- Hardcoding secrets or private data.
- Ignoring error cases.

**Follow-up:** What is one automated test you would add?

## 4. Rapid revision
- **WHERE:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **ORDER BY:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **INNER JOIN:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **LEFT JOIN:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **GROUP BY:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **HAVING:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **SUM:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.
- **COUNT:** explain its role in sql filtering, sorting, joins, grouping and aggregate functions.

**Interview preparation tip:** Give a definition, show a small practical example, explain a failure mode, and state how you would verify it.
