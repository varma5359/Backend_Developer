# Day 42: Interview Questions — CRUD Operations: Create, Read, Update and Delete

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 42 class notes](day_42_notes.md)  
**Approved mini-project:** Employee CRUD Application

## Core technical questions

### Q1. Explain crud operations: create, read, update and delete.
**Answer:** CRUD describes the four basic operations performed on stored records. Django views and forms can create a record, retrieve records, update an existing record and delete a record. A record should be identified using a stable primary key, and delete operations should be protected by authentication and authorization.

### Q2. Which methods or files are involved?
**Answer:** profiles/views.py, profiles/urls.py. Explain the responsibility of each.

### Q3. What is one common mistake?
**Answer:** Create adds one record. Check the actual database state and request behavior rather than assuming a command worked.

### Q4. How do you verify the implementation?
**Answer:** Use sample records, execute the relevant view or query, inspect the database and test missing or invalid cases.

### Q5. What should be considered before production?
**Answer:** Authentication, authorization, data integrity, safe handling of destructive actions, query performance and test coverage.

## Scenario questions

### Q6. A user reports an incorrect record or slow page. How do you investigate?
**Suggested answer:** Reproduce with known data, inspect the ORM query and related-object access, check affected records, measure query count and verify the result after a focused correction.

### Q7. How would you explain your implementation to another developer?
**Suggested answer:** State the requirement, identify the view/model/query, explain the data change or query behavior, show test evidence and mention limitations.

## Project viva — Employee CRUD Application

1. What does the project do?
2. Which model and ORM methods are used?
3. How are invalid inputs handled?
4. How do you verify the database result?
5. What security or performance risk did you consider?
6. What tests did you run?
7. What would you improve?

## Rapid revision

- **1.** Create a list view that retrieves employee records.
- **2.** Create a form view for adding an employee.
- **3.** Use get_object_or_404() to retrieve a record for editing.
- **4.** Pass instance=employee to ModelForm so it updates the existing record.
- **5.** Create a delete confirmation page and use POST for deletion.
- **6.** Add URL patterns with an integer primary-key converter.
- **7.** Test create, read, update and delete operations.
- **8.** Verify database state after every operation.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the important methods.
- [ ] Demonstrate the project.
- [ ] Verify the database behavior.
- [ ] Explain one failure case.
- [ ] Present evidence.
