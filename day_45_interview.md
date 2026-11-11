# Day 45: Interview Guide — Database Constraints, Field Validation and Model Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related class notes:** [Day 45 class notes](day_45_notes.md)  
**Approved mini-project:** Data Integrity Management System

> Explain the difference between an application validation error and a database constraint failure. Use the Product model from Days 43–44 for examples.

## 1. Core technical questions

### Q1. What is data integrity?

**Model answer:** Data integrity means stored data remains accurate, consistent and valid according to business rules. For a product catalog, examples include unique SKUs, positive prices and nonnegative stock.

### Q2. What is the difference between field validation and model validation?

**Model answer:** Field validation checks an individual field, such as requiring a positive price. Model validation checks rules involving the model as a whole or multiple fields. Django provides field validators and the model clean() hook.

### Q3. What does full_clean() do?

**Model answer:** full_clean() runs the model validation stages: clean_fields(), clean(), validate_unique() and validate_constraints(). It raises ValidationError when the model does not satisfy validation rules.

### Q4. Does save() call full_clean() automatically?

**Model answer:** No. Calling model.save() does not automatically execute the complete model validation sequence. Code that requires model validation should call full_clean() explicitly or use a form/ModelForm validation path. Database constraints still protect the rules represented at the database layer.

### Q5. What does MinValueValidator do?

**Model answer:** It checks that a field value is not lower than a configured minimum during Django validation. For a price field, MinValueValidator(Decimal("0.01")) rejects zero and negative prices during validation.

### Q6. What is UniqueConstraint?

**Model answer:** UniqueConstraint creates a database-level uniqueness rule for one or more fields. It protects against duplicate values even when a write bypasses normal form validation.

### Q7. What is CheckConstraint?

**Model answer:** CheckConstraint defines a database condition that must be true for stored rows. For example, Q(stock__gte=0) prevents negative stock.

### Q8. What is the difference between ValidationError and IntegrityError?

**Model answer:** ValidationError is raised by Django's validation system when supplied data fails a validation rule. IntegrityError is raised by the database layer when a write violates a database integrity rule, such as uniqueness or a check constraint.

### Q9. Why are database constraints necessary if forms validate data?

**Model answer:** Not every write passes through a form. Scripts, admin actions, background jobs, bulk operations or concurrent requests may bypass or race application validation. Database constraints provide the final protection for rules that the database can enforce.

### Q10. Why inspect existing data before adding a unique constraint?

**Model answer:** If duplicate values already exist, the database may be unable to create the new constraint. I inspect duplicates, back up the database, resolve the records using an approved data-cleaning process and only then apply the migration.

## 2. Code-reading questions

### Q11. Explain this validator.

~~~python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.01"))],
)
~~~

**Model answer:** It defines a decimal price field with up to ten digits and two decimal places. MinValueValidator checks that the price is at least 0.01 when Django validation runs.

### Q12. Explain this constraint.

~~~python
models.UniqueConstraint(
    fields=["sku"],
    name="catalog_product_sku_unique",
)
~~~

**Model answer:** It instructs the database to reject duplicate SKU values. The constraint name identifies the rule for migration and error diagnosis.

### Q13. Explain this constraint.

~~~python
models.CheckConstraint(
    condition=Q(stock__gte=0),
    name="catalog_product_stock_nonnegative",
)
~~~

**Model answer:** It enforces a database condition that stock must be greater than or equal to zero.

### Q14. Why call super().clean()?

**Model answer:** It preserves the parent model's clean behavior before adding custom validation logic.

### Q15. What does this code do?

~~~python
product.full_clean()
product.save()
~~~

**Model answer:** It validates the model fields and model-level rules first. If validation succeeds, it saves the object. If validation fails, full_clean() raises ValidationError and the save line is not reached.

## 3. Scenario-based questions

### Q16. A form rejects duplicate SKUs, but two simultaneous requests still create a duplicate. What is missing?

**Model answer:** A database-level unique constraint. Two requests can both pass an application check before either saves. The database constraint serializes the integrity decision and rejects the conflicting write. The application should catch the expected IntegrityError safely and show a useful message.

### Q17. A direct model.save() stores a negative price even though MinValueValidator exists. Why?

**Model answer:** save() does not automatically call full_clean(). I should validate explicitly and add a CheckConstraint for a rule that must always hold in the database.

### Q18. A migration fails when adding unique SKU. What do you do?

**Model answer:**
1. Stop and read the migration error.
2. Inspect duplicate SKU values.
3. Back up the database.
4. Identify the correct business values for duplicates.
5. Correct the data through an approved process.
6. Re-run the duplicate check.
7. Apply the migration only after the data satisfies the rule.

I do not delete migration files or remove the constraint just to make the command pass.

### Q19. A product name contains only spaces. How do you reject it?

**Model answer:** I add model clean() validation that checks the stripped name. I raise a field-specific ValidationError. A ModelForm can display that error to the user. If this rule must also be enforced by direct database writes, I would design and test an appropriate database constraint for the supported database.

### Q20. The database raises IntegrityError. Should the application display the raw error to the customer?

**Model answer:** No. The application should handle the expected constraint failure safely and display a useful, non-sensitive message. The detailed exception can be logged for debugging without exposing database internals.

## 4. Practical coding round

### Task 1 — Positive price validator

**Expected code:**

~~~python
from decimal import Decimal
from django.core.validators import MinValueValidator

price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.01"))],
)
~~~

### Task 2 — Unique SKU constraint

**Expected code:**

~~~python
models.UniqueConstraint(
    fields=["sku"],
    name="catalog_product_sku_unique",
)
~~~

### Task 3 — Nonnegative stock constraint

**Expected code:**

~~~python
from django.db.models import Q

models.CheckConstraint(
    condition=Q(stock__gte=0),
    name="catalog_product_stock_nonnegative",
)
~~~

### Task 4 — Explicit validation

**Expected code:**

~~~python
product.full_clean()
product.save()
~~~

Explain why the validation line must execute before save().

## 5. Project viva — Data Integrity Management System

### Q21. What business problem does your project solve?

**Suggested answer:** It prevents invalid product records from entering the catalog. It enforces unique product identifiers, positive prices, nonnegative stock and nonblank product names.

### Q22. Which validation layers did you implement?

**Suggested answer:** Field validation with MinValueValidator, model validation with clean(), database constraints with UniqueConstraint and CheckConstraint, and browser form validation through ModelForm.

### Q23. How did you verify duplicate SKU protection?

**Suggested answer:** I tried to validate a second product with an existing SKU and confirmed Django validation rejected it. I also relied on the database unique constraint as the final protection for direct or concurrent writes.

### Q24. How did you test the database stock constraint?

**Suggested answer:** I attempted an intentionally invalid database write inside a transaction.atomic() block, caught IntegrityError outside the atomic block and verified the invalid row was not stored.

### Q25. What did you learn about save()?

**Suggested answer:** save() does not automatically call full_clean(). I must choose a validation path deliberately and use database constraints for rules that must always hold.

## 6. Self-check

- [ ] I can explain validation versus constraints.
- [ ] I can explain full_clean() and save().
- [ ] I can use MinValueValidator.
- [ ] I can explain clean().
- [ ] I can explain UniqueConstraint and CheckConstraint.
- [ ] I can distinguish ValidationError from IntegrityError.
- [ ] I can add a migration safely after inspecting existing data.
- [ ] I can demonstrate Data Integrity Management System.

**Readiness rule:** Move to Day 46 only after both application validation and database constraint behavior have been demonstrated.
