# Day 44: Interview Questions — Query Optimization Basics: select_related and prefetch_related

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 44 class notes](day_44_notes.md)  
**Approved mini-project:** Optimized Order Management System

## Core technical questions

### Q1. Explain query optimization basics: select_related and prefetch_related.
**Answer:** A page that loops through related objects can accidentally execute one query per row (the N+1 query problem). select_related() uses SQL joins for single-valued relationships such as ForeignKey and OneToOneField. prefetch_related() performs additional queries and joins results in Python, which is useful for many-to-many and reverse relationships.

### Q2. Which methods or files are involved?
**Answer:** profiles/views.py, ORM comparison. Explain the responsibility of each.

### Q3. What is one common mistake?
**Answer:** The related fields used in the template are identified. Check the actual database state and request behavior rather than assuming a command worked.

### Q4. How do you verify the implementation?
**Answer:** Use sample records, execute the relevant view or query, inspect the database and test missing or invalid cases.

### Q5. What should be considered before production?
**Answer:** Authentication, authorization, data integrity, safe handling of destructive actions, query performance and test coverage.

## Scenario questions

### Q6. A user reports an incorrect record or slow page. How do you investigate?
**Suggested answer:** Reproduce with known data, inspect the ORM query and related-object access, check affected records, measure query count and verify the result after a focused correction.

### Q7. How would you explain your implementation to another developer?
**Suggested answer:** State the requirement, identify the view/model/query, explain the data change or query behavior, show test evidence and mention limitations.

## Project viva — Optimized Order Management System

1. What does the project do?
2. Which model and ORM methods are used?
3. How are invalid inputs handled?
4. How do you verify the database result?
5. What security or performance risk did you consider?
6. What tests did you run?
7. What would you improve?

## Rapid revision

- **1.** Identify a page that accesses related objects in a loop.
- **2.** Inspect model relationships to determine whether they are single-valued or multi-valued.
- **3.** Use select_related() for ForeignKey and OneToOneField access.
- **4.** Use prefetch_related() for ManyToManyField and reverse relations.
- **5.** Compare the number of database queries using Django Debug Toolbar or assertNumQueries in tests.
- **6.** Verify that the output is unchanged after optimization.
- **7.** Avoid adding optimization methods without measuring the query behavior.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the important methods.
- [ ] Demonstrate the project.
- [ ] Verify the database behavior.
- [ ] Explain one failure case.
- [ ] Present evidence.
