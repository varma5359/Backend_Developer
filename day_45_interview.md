# Day 45: Interview Questions — Database Constraints, Field Validation and Model Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 45 class notes](day_45_notes.md)  
**Approved mini-project:** Data Integrity Management System

## Core technical questions

### Q1. Explain database constraints, field validation and model validation.
**Answer:** Database constraints protect data integrity at the database level. Field validators and model clean() provide application-level validation. UniqueConstraint and CheckConstraint express rules that should remain true for stored rows. Django does not automatically call full_clean() every time model.save() is used, so validation strategy must be deliberate.

### Q2. Which Django APIs or files are involved?
**Answer:** profiles/models.py, Validation example. Explain the role of each API and how the feature is verified.

### Q3. What is a common mistake?
**Answer:** Duplicate SKU is rejected. Test the behavior rather than assuming the code is correct.

### Q4. How do you verify the implementation?
**Answer:** Use local test data and accounts, exercise valid and invalid cases, inspect the database/session and verify access restrictions.

### Q5. What security concern should you explain?
**Answer:** Protect credentials, validate data, enforce permissions and avoid exposing private information.

## Scenario-based questions

### Q6. A user can log in but should not be able to modify another employee's record. What is missing?
**Suggested answer:** Authorization. The application must check permissions for the requested operation and object, not merely check that the user is authenticated.

### Q7. Invalid data is being stored. What do you inspect?
**Suggested answer:** Field validation, model validation, database constraints and the exact save path. Remember that model.save() does not automatically call full_clean().

## Project viva — Data Integrity Management System

1. What problem does it solve?
2. Which validation or authentication APIs are used?
3. How are invalid values rejected?
4. How are credentials handled safely?
5. How are access restrictions verified?
6. What test cases did you run?
7. What would you improve for production?

## Rapid revision

- **1.** Identify the business rules that must always hold.
- **2.** Add field validators for individual field values.
- **3.** Add a UniqueConstraint for unique business identifiers.
- **4.** Add a CheckConstraint for a database-level condition.
- **5.** Override clean() for model-wide business validation where appropriate.
- **6.** Call full_clean() explicitly in the demonstration before save.
- **7.** Test duplicate and invalid values.
- **8.** Explain why database constraints are still important.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the security implications.
- [ ] Demonstrate valid and invalid workflows.
- [ ] Explain authentication versus authorization.
- [ ] Present Data Integrity Management System without exposing secrets.
