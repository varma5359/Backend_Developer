# Day 45: Interview Guide — Database Constraints, Field Validation and Model Validation

**Related class notes:** [Day 45 notes](day_45_notes.md)  
**Approved mini-project:** Data Integrity Management System  
**Level:** Intermediate

## 1. Core questions

### Q1. What is data integrity?
**Answer:** Data integrity means stored data remains accurate, consistent and valid according to the application's business rules.

### Q2. What is the difference between validation and a database constraint?
**Answer:** Validation checks input in application code and can provide useful error messages. A database constraint protects stored data at the database level, including writes that bypass a form.

### Q3. What is a field validator?
**Answer:** A callable that checks a field value and raises ValidationError when the value does not satisfy a rule.

### Q4. What does model clean() do?
**Answer:** It provides model-level validation for rules involving one or more model fields. It is not automatically called by every save() operation.

### Q5. What does full_clean() do?
**Answer:** It runs model field validation, model clean(), uniqueness validation and constraint validation where applicable. Developers must call it deliberately when needed; model.save() does not automatically call full_clean().

### Q6. What is UniqueConstraint?
**Answer:** It enforces uniqueness across one or more fields at the database level.

### Q7. What is CheckConstraint?
**Answer:** It enforces a database condition that each stored row must satisfy, such as price greater than zero or minimum salary less than or equal to maximum salary.

### Q8. Why use both form validation and constraints?
**Answer:** Forms provide friendly feedback before saving. Constraints protect the database against invalid writes from other code paths or concurrent requests.

### Q9. What is ValidationError?
**Answer:** It is Django's structured exception for validation failures. Forms and model validation can capture it and display useful errors.

### Q10. What is a race condition in uniqueness checks?
**Answer:** Two requests can check that a value is unused at nearly the same time and both attempt to insert it. A database unique constraint is the final protection.

## 2. Debugging and scenario questions

### Q11. save() stores invalid model data even though clean() exists.
**Answer:** save() does not automatically call full_clean(). Call validation deliberately in the appropriate application workflow and enforce critical invariants with database constraints.

### Q12. Form rejects duplicate SKU but shell insert succeeds.
**Answer:** The uniqueness rule may exist only in the form. Add a database UniqueConstraint or unique field so all write paths are protected.

### Q13. CheckConstraint fails during migration.
**Answer:** Inspect existing data for rows that violate the new rule, confirm the condition and database support, then plan a safe data cleanup/migration before applying the constraint.

### Q14. Two users submit the same unique value simultaneously.
**Answer:** Keep the database uniqueness constraint and handle IntegrityError safely. Application-level validation alone cannot guarantee uniqueness under concurrency.

## 3. Practical demonstration

Be prepared to:
1. Add a field validator.
2. Add a form clean method.
3. Add model clean().
4. Call full_clean() deliberately.
5. Add UniqueConstraint.
6. Add CheckConstraint.
7. Test valid and invalid data.
8. Explain why the database remains the final integrity boundary.

## 4. Readiness checklist

- [ ] I can distinguish validation and constraints.
- [ ] I can explain clean() and full_clean().
- [ ] I can use UniqueConstraint and CheckConstraint.
- [ ] I understand that save() does not automatically call full_clean().
- [ ] I can explain race conditions and IntegrityError.
- [ ] I can demonstrate Data Integrity Management System.

**Related notes:** [Day 45 class notes](day_45_notes.md)
