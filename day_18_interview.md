# Day 18: Interview Questions — SQL fundamentals: CREATE, INSERT, SELECT, UPDATE and DELETE

**Pathway:** Python Backend Developer (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools

## 1. Core technical questions

### Q1. Why is WHERE important in UPDATE and DELETE?
**Answer:**
- Without WHERE, these statements can affect every row in the table.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** An HR team maintains employee records and needs safe updates.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q2. How can SQL injection be prevented?
**Answer:**
- Use parameterized queries for values, validate inputs and follow least-privilege database access.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** An HR team maintains employee records and needs safe updates.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q3. What is the main purpose of DDL?
**Answer:** SQL defines and manipulates relational data. CREATE makes tables; INSERT adds rows; SELECT retrieves; UPDATE modifies; DELETE removes. WHERE restricts changes to selected rows.

**Follow-up:** What would go wrong if the concept were misunderstood?

### Q4. Which tools are appropriate for this lesson?
**Answer:** Python and VS Code for demonstrations, terminal commands for execution, and SQLite for local practice and PostgreSQL for later production database work.

**Follow-up:** What would change in a deployed Django service?

### Q5. How do you verify the implementation?
**Answer:** Define expected inputs and outputs, run normal and edge cases, inspect actual responses or database state, and document failures.

**Follow-up:** Why is a successful command not always proof of correct business behavior?

## 2. Scenario-based interview questions

### Q6. An HR team maintains employee records and needs safe updates. What should the developer verify?
**Answer:**
- Define the expected result before implementation.
- Check that the chosen DDL behavior matches the requirement.
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

### Q8. Explain your Employee Database Manager.
**Answer:**
- I defined the inputs, operations and expected outputs.
- I implemented a small demonstration of sql fundamentals: create, insert, select, update and delete.
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
- **DDL:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **DML:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **CREATE:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **INSERT:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **SELECT:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **UPDATE:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **DELETE:** explain its role in sql fundamentals: create, insert, select, update and delete.
- **WHERE:** explain its role in sql fundamentals: create, insert, select, update and delete.

**Interview preparation tip:** Give a definition, show a small practical example, explain a failure mode, and state how you would verify it.
