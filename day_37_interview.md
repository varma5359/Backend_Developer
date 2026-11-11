# Day 37: Interview Guide — Django ORM Fundamentals and Querying Records

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 37 notes](day_37_notes.md)  
**Mini-project:** Employee Query Explorer

## 1. Technical questions with model answers

### Q1. What is the Django ORM?

**Model answer:** It maps Python model operations to database queries. Developers use managers and QuerySets to create, retrieve, update and delete records.

### Q2. What is a QuerySet?

**Model answer:** It is a lazy, chainable representation of a database query. It can represent zero, one or many rows.

### Q3. What is the difference between filter() and get()?

**Model answer:** filter() returns a QuerySet and can return zero or many rows. get() expects exactly one row and raises DoesNotExist or MultipleObjectsReturned otherwise.

### Q4. What does QuerySet laziness mean?

**Model answer:** Django generally builds a query first and executes it when the result is evaluated, such as by iteration, list(), bool(), count() or exists().

### Q5. What is the difference between count() and exists()?

**Model answer:** count() returns the number of matching rows. exists() answers whether at least one row matches and is preferable when only existence is needed.

### Q6. Why should delete() be used carefully?

**Model answer:** It permanently removes selected records and may cascade to related rows depending on relationship rules. Confirm the queryset and deletion behavior first.

## 2. Scenario-based interview question

**Scenario:** A page only needs to show whether any active employees exist. Should it call count() or exists()? Explain.

**Model answer:** Use exists() when only a yes/no answer is required. count() asks the database for the number of matching rows and does unnecessary work if the count is not displayed.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Create two employees, query all/filter/order_by, test get with a unique and missing code, update and re-query a record, and explain QuerySet laziness.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Employee Query Explorer

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Employee Query Explorer with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is QuerySet laziness?
**Answer:** Django can build a QuerySet without immediately retrieving rows. The query is evaluated when the results are needed.

### Q6. What is the difference between filter() and get()?
**Answer:** filter() returns a QuerySet with zero or more matches. get() expects exactly one object and raises exceptions otherwise.

### Q7. What does exists() do?
**Answer:** It checks whether at least one matching row exists without loading all matching model objects.

### Q8. What is the difference between values() and values_list()?
**Answer:** values() returns dictionaries. values_list() returns tuples or a flat list for a single field.

### Q9. What is a Q object?
**Answer:** It represents complex query conditions, including OR and NOT.

### Q10. What is an F expression?
**Answer:** It refers to a model field value inside a database expression, allowing field-to-field comparisons or updates.

### Q11. Scenario: get() raises MultipleObjectsReturned.
**Answer:** The lookup is not unique. Use a unique field or filter() when multiple records are expected.

### Q12. Scenario: a list page runs one query per row.
**Answer:** Inspect related-object access and consider select_related or prefetch_related based on relationship type.

