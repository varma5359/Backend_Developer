# Day 43: Interview Questions — Advanced Django ORM: filter, exclude, get, order_by and values

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 43 class notes](day_43_notes.md)  
**Approved mini-project:** Advanced Product Search

## Core technical questions

### Q1. Explain advanced django orm: filter, exclude, get, order_by and values.
**Answer:** Django ORM QuerySets support filtering, excluding, retrieving one record, sorting and selecting fields. Field lookups such as __icontains, __gte, __in and __range express common query conditions. QuerySets are lazy until evaluated, so developers should understand when database queries actually run.

### Q2. Which methods or files are involved?
**Answer:** Django shell, Query examples. Explain the responsibility of each.

### Q3. What is one common mistake?
**Answer:** Each lookup returns expected records. Check the actual database state and request behavior rather than assuming a command worked.

### Q4. How do you verify the implementation?
**Answer:** Use sample records, execute the relevant view or query, inspect the database and test missing or invalid cases.

### Q5. What should be considered before production?
**Answer:** Authentication, authorization, data integrity, safe handling of destructive actions, query performance and test coverage.

## Scenario questions

### Q6. A user reports an incorrect record or slow page. How do you investigate?
**Suggested answer:** Reproduce with known data, inspect the ORM query and related-object access, check affected records, measure query count and verify the result after a focused correction.

### Q7. How would you explain your implementation to another developer?
**Suggested answer:** State the requirement, identify the view/model/query, explain the data change or query behavior, show test evidence and mention limitations.

## Project viva — Advanced Product Search

1. What does the project do?
2. Which model and ORM methods are used?
3. How are invalid inputs handled?
4. How do you verify the database result?
5. What security or performance risk did you consider?
6. What tests did you run?
7. What would you improve?

## Rapid revision

- **1.** Open Django shell and import Employee.
- **2.** Use filter() for exact matching.
- **3.** Use exclude() to remove matching records.
- **4.** Use get() when exactly one record is expected.
- **5.** Use field lookups such as icontains, gte and in.
- **6.** Use order_by() with a minus prefix for descending order.
- **7.** Use values() to select fields as dictionaries.
- **8.** Inspect querysets and evaluate them using list() or iteration.
- **9.** Handle DoesNotExist and MultipleObjectsReturned where appropriate.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the important methods.
- [ ] Demonstrate the project.
- [ ] Verify the database behavior.
- [ ] Explain one failure case.
- [ ] Present evidence.
