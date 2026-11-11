# Day 45: Database Constraints, Field Validation and Model Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Duration:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–44 — Django models, forms, CRUD, QuerySets, relationships and query optimization  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django and configured database  
**Approved mini-project:** Data Integrity Management System

> **Self-learning method:** You will strengthen the Product model created on Day 43. Do not create a second Product model. This lesson is about making invalid data difficult to save, even when data is submitted through a path other than your browser form.

---

## 1. What you will build

Imagine an online store. A product must follow these business rules:

- Every product must have a unique SKU.
- Product name cannot be empty or only spaces.
- Product price must be greater than zero.
- Stock cannot be negative.
- A product's data must remain valid even when another script or admin operation attempts to save it.

You will implement these rules using:
1. Field validators.
2. Model clean() validation.
3. Database constraints.
4. ModelForm validation.
5. Tests for valid and invalid data.

### Learning outcomes

By the end, you should be able to:
- Explain validation versus a database constraint.
- Use MinValueValidator.
- Override model clean().
- Call full_clean() deliberately.
- Add UniqueConstraint and CheckConstraint.
- Explain why model.save() does not automatically call full_clean().
- Understand IntegrityError and ValidationError.
- Create migrations safely when existing data may violate a new rule.
- Test invalid input through forms and database constraints.

## 2. Understand the three layers

A useful backend validates data at more than one layer.

~~~text
User submits data
       |
       v
Django Form / ModelForm
       |
       | Field and form validation
       v
Model validation (full_clean)
       |
       | clean_fields(), clean(), validate_unique(),
       | validate_constraints()
       v
Database constraints
       |
       v
Data stored only if database rules pass
~~~

### 2.1 Field validation

A field validator checks an individual field value.

Example: price must be at least 0.01.

### 2.2 Model validation

Model clean() checks rules involving model fields or multiple fields. Example: product name cannot contain only whitespace.

### 2.3 Database constraints

A database constraint protects stored data at the database level. It remains important when data is written by a script, admin operation, bulk operation or another application path.

**Important distinction:** Validators and clean() run when Django's validation process is called. Database constraints are enforced by the database when a write is attempted.

## 3. Check your Day 43 Product model

Open the Django project containing manage.py. Your catalog/models.py should contain the Product model from Day 43.

~~~python
class Product(models.Model):
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
~~~

If your file is different, compare it with Day 43 first. Preserve any other models or app code.

Run:

~~~powershell
python manage.py check
python manage.py showmigrations catalog
~~~

Expected: catalog migrations are applied.

## 4. Understand ValidationError and IntegrityError

These two exceptions are not the same.

| Exception | Usually means | Example |
|---|---|---|
| ValidationError | Django validation rejected the value | Price is below minimum |
| IntegrityError | Database rejected a write due to a constraint | Duplicate SKU or negative stock |

A form normally displays validation errors to a user. A database IntegrityError must be handled carefully, especially when concurrent requests can attempt the same unique value.

Do not catch every exception and silently continue. Handle expected failures and keep the database transaction safe.

## 5. Add field validators

Open catalog/models.py. Add imports:

~~~python
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
~~~

Update the price field:

~~~python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.01"))],
)
~~~

### 5.1 Explain the validator

- DecimalField stores decimal numbers, suitable for monetary values.
- max_digits=10 allows at most ten digits in total.
- decimal_places=2 allows two digits after the decimal point.
- MinValueValidator checks that the value is at least the supplied minimum.
- Decimal("0.01") avoids representing a decimal amount using a binary floating-point literal.

Examples:

~~~python
MinValueValidator(Decimal("0.01"))
~~~

Accepts 0.01 and 100.00, but rejects 0.00 and negative values during validation.

**Important:** A field validator is not a substitute for a database constraint. A direct model.save() call does not automatically execute full_clean().

## 6. Add database constraints

Inside the Product model, add a Meta class:

~~~python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["sku"],
            name="catalog_product_sku_unique",
        ),
        models.CheckConstraint(
            condition=Q(price__gt=0),
            name="catalog_product_price_positive",
        ),
        models.CheckConstraint(
            condition=Q(stock__gte=0),
            name="catalog_product_stock_nonnegative",
        ),
    ]
~~~

### 6.1 UniqueConstraint

~~~python
models.UniqueConstraint(
    fields=["sku"],
    name="catalog_product_sku_unique",
)
~~~

This tells the database that two Product rows cannot have the same SKU.

Why is this important?
- Two users may submit the same SKU at almost the same time.
- Form validation can check duplicates, but both requests might pass before either saves.
- The database constraint is the final protection against duplicate rows.

### 6.2 CheckConstraint for price

~~~python
models.CheckConstraint(
    condition=Q(price__gt=0),
    name="catalog_product_price_positive",
)
~~~

This means price must be greater than zero.

### 6.3 CheckConstraint for stock

~~~python
models.CheckConstraint(
    condition=Q(stock__gte=0),
    name="catalog_product_stock_nonnegative",
)
~~~

This means stock must be greater than or equal to zero.

### 6.4 Constraint naming

Constraint names must be unique within the database table and should be descriptive. A clear name helps identify which rule failed when debugging a database error.

## 7. Add model-level clean() validation

Inside the Product class, add:

~~~python
def clean(self):
    super().clean()

    if self.sku:
        self.sku = self.sku.strip().upper()

    if self.name and not self.name.strip():
        raise ValidationError({
            "name": "Product name cannot contain only spaces."
        })

    if self.name:
        self.name = self.name.strip()

    if self.category and not self.category.strip():
        raise ValidationError({
            "category": "Category cannot contain only spaces."
        })

    if self.category:
        self.category = self.category.strip()
~~~

### 7.1 Understand the code

- clean() is a model validation hook.
- super().clean() preserves any validation behavior from the parent class.
- strip() removes spaces at the beginning and end.
- upper() normalizes SKU to uppercase.
- A whitespace-only name is rejected.
- A whitespace-only category is rejected.
- ValidationError reports a useful field-level message.

### 7.2 Why normalize SKU?

These values should represent the same business identifier:

- kb-101
- KB-101
- " KB-101 "

Normalizing the value in the model validation path makes the stored representation consistent when full_clean() is called.

**Important limitation:** clean() does not automatically run when you call save(). The application must use a validation path deliberately. Database uniqueness remains case-sensitive or case-insensitive according to the database collation and constraint behavior; if case-insensitive uniqueness is a requirement, design and test a suitable database expression constraint for your supported database.

## 8. Understand full_clean()

Django models provide:

~~~python
product.full_clean()
~~~

This runs the model validation stages:
1. clean_fields() — validates individual model fields and their validators.
2. clean() — runs custom model-level validation.
3. validate_unique() — checks uniqueness rules supported by model validation.
4. validate_constraints() — validates model constraints.

If validation fails, Django raises ValidationError.

### 8.1 Important: save() does not call full_clean()

This is a critical Django behavior.

~~~python
product = Product(
    sku="P-100",
    name="Keyboard",
    category="Accessories",
    price=Decimal("799.00"),
    stock=10,
)

product.save()
~~~

Calling save() does not automatically run the complete model validation sequence. Database constraints still protect the rules that are represented as database constraints, but field validators and clean() are not automatically run by save().

For a deliberate model validation workflow:

~~~python
product.full_clean()
product.save()
~~~

A ModelForm performs validation as part of its normal is_valid() flow. Do not assume every script, bulk operation or direct save() uses a ModelForm.

## 9. Update catalog/models.py completely

Your Product model should now look like this. If you already have other models in the file, preserve them.

~~~python
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q


class Product(models.Model):
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=60)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sku"],
                name="catalog_product_sku_unique",
            ),
            models.CheckConstraint(
                condition=Q(price__gt=0),
                name="catalog_product_price_positive",
            ),
            models.CheckConstraint(
                condition=Q(stock__gte=0),
                name="catalog_product_stock_nonnegative",
            ),
        ]

    def clean(self):
        super().clean()

        if self.sku:
            self.sku = self.sku.strip().upper()

        if self.name and not self.name.strip():
            raise ValidationError({
                "name": "Product name cannot contain only spaces."
            })

        if self.name:
            self.name = self.name.strip()

        if self.category and not self.category.strip():
            raise ValidationError({
                "category": "Category cannot contain only spaces."
            })

        if self.category:
            self.category = self.category.strip()

    def __str__(self):
        return f"{self.sku} - {self.name}"
~~~

The Decimal import is used for the minimum validator. ValidationError is used by clean(). Q is used to express database check conditions.

## 10. Before creating migrations — inspect existing data

You already created sample products on Day 43. A new unique constraint can fail to apply if duplicate SKUs already exist.

Before applying the migration, inspect the data.

Open shell:

~~~powershell
python manage.py shell
~~~

Find duplicate SKUs:

~~~python
from django.db.models import Count
from catalog.models import Product

Product.objects.values("sku").annotate(total=Count("id")).filter(total__gt=1)
~~~

Find invalid stock:

~~~python
Product.objects.filter(stock__lt=0)
~~~

Find invalid prices:

~~~python
Product.objects.filter(price__lte=0)
~~~

Expected for the Day 43 sample data: no duplicates, negative stock or zero/negative prices.

If invalid records exist:
- Do not delete them blindly.
- Identify why they exist.
- Back up the database before any correction.
- Decide the correct business value.
- Correct records using an approved data-cleaning process.
- Re-run the checks before applying the migration.

Exit shell.

## 11. Create and apply the migration

~~~powershell
python manage.py makemigrations catalog
python manage.py sqlmigrate catalog 0002
python manage.py migrate
python manage.py check
~~~

**Note:** The migration number may differ if you already created additional catalog migrations. Use the actual migration filename shown by makemigrations in the sqlmigrate command.

Expected:
- A new migration adds the constraints.
- sqlmigrate displays the database operations Django plans to perform.
- migrate applies the migration.
- check reports no system-check errors.

### Why inspect sqlmigrate?

It shows the SQL operations generated by Django for the migration. This is especially useful before adding constraints to an existing table.

## 12. Test validation in Django shell

Open:

~~~powershell
python manage.py shell
~~~

Import:

~~~python
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from catalog.models import Product
~~~

### Test 1 — Valid product

~~~python
product = Product(
    sku=" new-200 ",
    name="  USB Hub  ",
    category="  Accessories  ",
    price=Decimal("499.00"),
    stock=15,
)

product.full_clean()
product.save()

product.sku, product.name, product.category
~~~

Expected:

~~~text
('NEW-200', 'USB Hub', 'Accessories')
~~~

The model clean() method normalized the values because full_clean() was called.

### Test 2 — Invalid price

~~~python
product = Product(
    sku="BAD-PRICE",
    name="Invalid Price Product",
    category="Accessories",
    price=Decimal("0.00"),
    stock=5,
)

product.full_clean()
~~~

Expected: ValidationError because price is below the minimum.

### Test 3 — Whitespace-only name

~~~python
product = Product(
    sku="BAD-NAME",
    name="   ",
    category="Accessories",
    price=Decimal("100.00"),
    stock=5,
)

product.full_clean()
~~~

Expected: ValidationError for name.

### Test 4 — Duplicate SKU

First, verify that the sample SKU exists:

~~~python
Product.objects.filter(sku="KB-101").exists()
~~~

If True, try:

~~~python
duplicate = Product(
    sku="KB-101",
    name="Another Keyboard",
    category="Accessories",
    price=Decimal("500.00"),
    stock=10,
)

duplicate.full_clean()
~~~

Expected: ValidationError for the uniqueness rule. The database constraint also protects the table if a write bypasses the normal model validation path.

### Test 5 — Database-level check constraint

The following is an intentionally invalid direct database write. Use a transaction savepoint so the expected database error does not leave the shell connection in a broken transaction.

~~~python
try:
    with transaction.atomic():
        Product.objects.create(
            sku="BAD-STOCK",
            name="Invalid Stock Product",
            category="Accessories",
            price=Decimal("100.00"),
            stock=-5,
        )
except IntegrityError:
    print("Database rejected negative stock.")
~~~

Expected:

~~~text
Database rejected negative stock.
~~~

The database constraint rejects the invalid row even though QuerySet.create() did not call model full_clean().

### Test 6 — Verify the invalid row was not stored

~~~python
Product.objects.filter(sku="BAD-STOCK").exists()
~~~

Expected: False.

Exit the shell.

## 13. Understand ModelForm validation

A ModelForm uses model field definitions and model validation as part of its validation process.

Example in catalog/forms.py:

~~~python
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "sku",
            "name",
            "category",
            "price",
            "stock",
            "is_active",
        ]
~~~

When a view calls:

~~~python
form = ProductForm(request.POST)
if form.is_valid():
    form.save()
~~~

Django validates the submitted values. If the form is invalid, display the errors and do not save.

**Do not create a second ProductForm if Day 43 already created one.** Add or merge the required fields into the existing form only if needed.

## 14. Validation versus database protection

| Rule | Field validator / model validation | Database constraint |
|---|---|---|
| Price must be positive | MinValueValidator | CheckConstraint |
| Stock cannot be negative | Can add MinValueValidator(0) | CheckConstraint |
| SKU must be unique | Model uniqueness validation can check | UniqueConstraint |
| Name cannot be only spaces | clean() | Not included in this lesson's DB constraints |
| Normalize SKU | clean() | Not a database normalization rule |

Why both layers?

- Django validation gives users useful error messages.
- Database constraints protect stored data even when validation is bypassed.
- A database constraint cannot replace every user-friendly validation rule.
- A validator cannot replace database protection when concurrent writes occur.

## 15. Common errors and troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| Migration fails adding unique SKU | Duplicate existing values | Inspect duplicates, back up, correct data, retry |
| IntegrityError on duplicate SKU | Unique constraint rejected write | Use a unique SKU and show a friendly form error |
| Negative stock saved through save() | No database check constraint or migration not applied | Confirm constraint and migration |
| full_clean() raises ValidationError | Field or model rule failed | Inspect error.message_dict |
| save() accepts invalid field value | save() does not call full_clean() | Validate explicitly and add database constraints |
| CheckConstraint API error | Wrong Django version or syntax | Check installed Django version and supported API |
| No such table | Migration not applied | Run showmigrations and migrate |
| Migration conflict | Multiple migration branches | Inspect migration graph; do not delete migration files blindly |
| Duplicate migration operation | Repeated or conflicting model edits | Inspect makemigrations output before applying |
| Existing tests fail after constraint | Test data violates new rule | Update test fixtures to valid business values |

## 16. Independent mini-project — Data Integrity Management System

**Business requirement:** Build a product data management feature that rejects invalid product records and protects stored data.

### Required rules

1. SKU is required and unique.
2. SKU is normalized to uppercase in the validation path.
3. Product name cannot be blank or whitespace-only.
4. Category cannot be blank or whitespace-only.
5. Price must be greater than zero.
6. Stock must be zero or greater.

### Required implementation

- Add field validators.
- Add model clean().
- Add a UniqueConstraint.
- Add CheckConstraint rules.
- Use full_clean() in a direct model validation demonstration.
- Use a ModelForm for browser input.
- Create and apply migrations.
- Test both ValidationError and IntegrityError paths.
- Preserve valid Day 43 products and Day 44 order records.

### Acceptance checklist

- [ ] Valid Product can be created.
- [ ] SKU normalization works when full_clean() is called.
- [ ] Duplicate SKU is rejected.
- [ ] Whitespace-only name is rejected.
- [ ] Whitespace-only category is rejected.
- [ ] Zero or negative price fails validation.
- [ ] Negative stock is rejected by the database.
- [ ] Invalid records are not stored.
- [ ] Existing valid products remain available.
- [ ] Existing order items still refer to the correct Product.
- [ ] The learner can explain why save() does not automatically call full_clean().

### Evidence to submit

- Updated Product model.
- Migration file.
- Output from duplicate and invalid data tests.
- Output showing negative stock was rejected by the database.
- Screenshot or terminal output of valid Product creation.
- README with business rules and validation layers.
- No secrets or real customer data.

## 17. Knowledge check

1. What is the difference between validation and a database constraint?
2. What does MinValueValidator do?
3. What is the purpose of model clean()?
4. What does full_clean() execute?
5. Does model.save() automatically call full_clean()?
6. What is UniqueConstraint used for?
7. What is CheckConstraint used for?
8. What is the difference between ValidationError and IntegrityError?
9. Why can a form uniqueness check alone be insufficient?
10. Why inspect existing data before adding a unique constraint?
11. What is the purpose of a migration?
12. Why should database credentials and secret keys not be committed?

### Answer key

1. Validation checks data in Django's application layer; constraints enforce rules in the database.
2. It rejects values below a configured minimum during validation.
3. It provides custom model-level validation.
4. Field validation, model clean(), uniqueness validation and constraint validation.
5. No.
6. It prevents duplicate values for the specified fields.
7. It enforces a boolean condition on stored rows.
8. ValidationError comes from Django validation; IntegrityError comes from a database integrity failure.
9. Concurrent requests can both pass a form check before either one saves.
10. Existing duplicate values can make the migration fail.
11. It records and applies database schema changes.
12. They are sensitive credentials and can compromise systems.

## 18. Five MCQs with explanations

### Q1. Which validator checks a minimum numeric value?

A. MaxLengthValidator  
B. MinValueValidator  
C. URLValidator  
D. EmailValidator

**Answer: B.** MinValueValidator checks that a value is not below a configured minimum.

### Q2. Which method runs model field and custom model validation?

A. save()  
B. delete()  
C. full_clean()  
D. refresh_from_db()

**Answer: C.** full_clean() runs the model validation stages.

### Q3. Which constraint prevents duplicate SKU values?

A. CheckConstraint  
B. UniqueConstraint  
C. OrderBy  
D. Prefetch

**Answer: B.** UniqueConstraint enforces uniqueness in the database.

### Q4. Why can save() store a value that a field validator would reject?

A. save() automatically deletes validators  
B. save() does not automatically call full_clean()  
C. Django ignores every field  
D. Database constraints never run

**Answer: B.** Model.save() does not automatically run the full model validation sequence.

### Q5. Which exception usually indicates that a database constraint rejected a write?

A. TemplateDoesNotExist  
B. ValidationError  
C. IntegrityError  
D. NoReverseMatch

**Answer: C.** IntegrityError indicates a database integrity violation.

## 19. Interview preparation

Prepare to explain:
1. What is data integrity?
2. What is the difference between field validation and model validation?
3. What does full_clean() do?
4. Does save() call full_clean()?
5. Explain UniqueConstraint and CheckConstraint.
6. What is the difference between ValidationError and IntegrityError?
7. Why should important rules be enforced at the database layer?
8. How do you add a constraint to an existing table safely?
9. How do you handle duplicate values from concurrent requests?
10. Why should a ModelForm and a database constraint both be used?

Use the separate Day 45 interview guide for model answers, scenarios and project viva.

## 20. Completion checklist

- [ ] I understand the three validation layers.
- [ ] I added the price validator.
- [ ] I added model clean().
- [ ] I added unique and check constraints.
- [ ] I inspected existing data before migration.
- [ ] I created and applied the migration.
- [ ] I tested full_clean().
- [ ] I tested a database IntegrityError safely.
- [ ] I verified invalid records were not stored.
- [ ] I completed Data Integrity Management System.
- [ ] I can explain why save() does not call full_clean() automatically.

## 21. Phase 4 progress and next lesson

Days 42–45 form the database foundation of Phase 4:

~~~text
Day 42: CRUD — create, read, update and delete
       |
       v
Day 43: ORM — search and filter records
       |
       v
Day 44: Optimization — load related data efficiently
       |
       v
Day 45: Integrity — prevent invalid data from being stored
       |
       v
Day 46: Authentication — understand users and identity
~~~

**Day 45 is complete only when you can demonstrate both Django validation and database-level rejection of invalid data.**


---

# PART 14 — DEEPER VALIDATION WORKFLOW

## 82. Understand the validation layers

A backend application should not depend on one validation location.

Use multiple layers for different reasons:

| Layer | Responsibility | Example |
|---|---|---|
| Browser input attributes | Convenience for the user | required, min, max |
| Django form field validation | Validate submitted values | Decimal input is valid |
| Form clean methods | Cross-field business rules | Minimum price cannot exceed maximum |
| Model field validators | Reusable field-level rules | Price must be at least 0.01 |
| Model clean() | Model-wide business validation | Start date must be before end date |
| Database constraints | Protect stored rows | SKU must be unique; stock cannot be negative |

The browser is not trusted. A user can send a request without using your HTML form.

## 83. Browser validation is not enough

Example:

~~~html
<input type="number" name="stock" min="0" required>
~~~

This improves the browser experience.

It does not prevent someone from sending:

~~~text
stock=-100
~~~

directly to the server.

The server must validate the value, and the database should enforce important invariants where possible.

## 84. Understand clean_fields()

Django model validation includes field cleaning.

Conceptually, this stage:
- Runs field-level validation.
- Converts values to appropriate Python types.
- Runs validators.
- Collects field errors.

Most application code should use full_clean() rather than calling individual validation methods manually.

## 85. Understand clean()

A model clean() method is useful for rules that depend on multiple fields.

Example for a model with start_date and end_date:

~~~python
from django.core.exceptions import ValidationError

def clean(self):
    if (
        self.start_date
        and self.end_date
        and self.start_date > self.end_date
    ):
        raise ValidationError(
            "Start date cannot be after end date."
        )
~~~

This is a model-level validation example. It is not a replacement for a database constraint if the rule can be expressed and supported by the database.

## 86. Understand validate_unique()

Model uniqueness validation checks uniqueness rules defined for the model.

Database uniqueness constraints remain necessary because validation and saving are separate operations. Two concurrent requests can pass an application-level uniqueness check before either insert is committed.

## 87. Understand full_clean()

Example:

~~~python
product.full_clean()
product.save()
~~~

full_clean() runs model validation before saving.

It can raise ValidationError.

Important:
- save() does not automatically call full_clean().
- A ModelForm performs validation as part of its form lifecycle.
- Code paths that save model instances directly need a deliberate validation strategy.
- Database constraints remain the final protection for supported integrity rules.

## 88. Why a ModelForm is useful

A ModelForm:
- Builds fields from a model.
- Runs form field validation.
- Runs model validation as part of the form validation process.
- Makes it easier to display field errors.
- Can save a validated model instance.

Do not expose every model field automatically. Explicitly choose which fields the user is allowed to submit.

## 89. Add a model clean() example

For the Product model, a model-wide validation method can check business rules.

~~~python
from django.core.exceptions import ValidationError

def clean(self):
    super().clean()

    if self.name and not self.name.strip():
        raise ValidationError({
            "name": "Product name cannot contain only spaces."
        })

    if self.stock is not None and self.stock < 0:
        raise ValidationError({
            "stock": "Stock cannot be negative."
        })
~~~

The Product model's database CheckConstraint should also protect the stock rule if the database supports the constraint.

Do not rely on clean() alone for a critical invariant because direct save() does not automatically call full_clean().

## 90. Normalize values deliberately

Some values should be normalized before they are saved.

Examples:
- SKU: strip surrounding whitespace and convert to uppercase.
- Email: trim whitespace and apply a consistent normalization policy.
- Category: use defined choices or a related model.

Normalization should not silently change meaningful data.

Do not uppercase a person's display name unless the business requirement specifically asks for it.

## 91. Avoid duplicate validation logic

If the same rule appears in:
- Form clean().
- Model clean().
- A view.
- A template.

the rules can drift apart.

Choose the right layer:
- Field-level reusable rule: validator.
- Cross-field form feedback: form clean().
- Model invariant: model clean().
- Database-enforceable invariant: constraint.

It can be appropriate to have a rule in both application validation and a database constraint, but the purpose should be clear.

---

# PART 15 — DATABASE CONSTRAINTS IN DETAIL

## 92. UniqueConstraint

UniqueConstraint can enforce uniqueness across one or more fields.

Example:

~~~python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["sku"],
            name="unique_product_sku",
        ),
    ]
~~~

This ensures no two rows can have the same SKU.

## 93. Multi-field uniqueness

Example:

~~~python
models.UniqueConstraint(
    fields=["category", "name"],
    name="unique_product_name_per_category",
)
~~~

This permits the same product name in different categories but prevents a duplicate name within the same category.

Choose this rule only if it matches the business requirement.

## 94. CheckConstraint

Example:

~~~python
models.CheckConstraint(
    condition=models.Q(stock__gte=0),
    name="product_stock_non_negative",
)
~~~

This instructs the database to reject a row where stock is negative.

## 95. Constraint naming

Constraint names should:
- Be unique within the database where required.
- Describe the business rule.
- Be stable and readable.
- Avoid accidental collisions.

Do not use a vague name such as constraint1.

## 96. What happens when a constraint fails?

The database rejects the write.

Django may raise IntegrityError.

The application should:
1. Catch only expected integrity failures.
2. Roll back the relevant transaction.
3. Show a safe message.
4. Keep technical details in secure logs.
5. Avoid claiming that the record was saved.

## 97. Use transaction.atomic() around risky writes

Example:

~~~python
from django.db import IntegrityError, transaction

try:
    with transaction.atomic():
        product.save()
except IntegrityError:
    # Handle the expected constraint failure.
    ...
~~~

The transaction ensures the failed database operation is rolled back.

The ellipsis above represents application-specific handling; do not copy it as a complete view.

## 98. Validation does not eliminate race conditions

Suppose two requests submit the same SKU.

Request A:
- Checks SKU does not exist.
- Validation passes.

Request B:
- Checks SKU does not exist.
- Validation passes.

Both attempt to save.

The database unique constraint ensures that only one can succeed.

This is why application-level validation alone is not enough.

---

# PART 16 — MIGRATIONS AND EXISTING DATA

## 99. Why adding a constraint can fail

A database constraint must be true for existing rows as well as new rows.

Imagine the database already contains:
- A negative stock value.
- Duplicate SKUs.
- A price of zero.

Adding a new constraint may fail because the existing data violates the rule.

## 100. Inspect existing data first

Use the Django shell:

~~~powershell
python manage.py shell
~~~

Example checks:

~~~python
from catalog.models import Product

Product.objects.filter(stock__lt=0).count()
Product.objects.filter(price__lte=0).count()
~~~

For duplicate SKU detection, use aggregation:

~~~python
from django.db.models import Count

duplicates = (
    Product.objects
    .values("sku")
    .annotate(total=Count("id"))
    .filter(total__gt=1)
)
~~~

If the model already enforces uniqueness, duplicates should not normally exist. This query is useful when auditing legacy data before a migration.

## 101. Safe migration sequence

1. Inspect the existing model.
2. Identify the new rule.
3. Inspect existing rows that may violate it.
4. Decide how invalid legacy rows should be corrected.
5. Back up important data.
6. Add the model validator or constraint.
7. Generate the migration.
8. Inspect the migration.
9. Apply it in a development copy.
10. Run tests.
11. Apply through the approved deployment process.

Do not delete the database just to make a migration succeed.

## 102. Use makemigrations and migrate

~~~powershell
python manage.py makemigrations catalog
python manage.py sqlmigrate catalog 0002
python manage.py migrate
python manage.py showmigrations catalog
~~~

Use the actual migration number created by Django. It may not be 0002 in your project.

## 103. Database backend differences

Database engines can differ in how they implement or enforce constraints.

Before relying on a constraint in production:
- Confirm the target database supports it.
- Test the migration against that database.
- Test invalid writes.
- Inspect the generated SQL.
- Do not assume SQLite development behavior proves production PostgreSQL behavior.

## 104. Rollback planning

Before applying a schema change to important data:
- Know which migration is being applied.
- Know whether the migration is reversible.
- Back up data.
- Test restore procedures.
- Have a deployment rollback plan.

A migration is not a backup.

---

# PART 17 — ADDITIONAL PRACTICE AND TEST CASES

## 105. Validation test matrix

| Input | Expected result |
|---|---|
| Valid SKU | Accepted |
| Duplicate SKU | Rejected |
| Empty name | Rejected if required |
| Name containing only spaces | Rejected by custom validation |
| Price 0.01 | Accepted |
| Price 0.00 | Rejected |
| Negative price | Rejected |
| Stock 0 | Accepted |
| Negative stock | Rejected |
| Minimum price greater than maximum | Rejected |
| Valid update | Saved |
| Invalid update | Existing record remains unchanged |

## 106. Test form validation

Example:

~~~python
from django.test import TestCase
from catalog.forms import ProductForm


class ProductFormValidationTests(TestCase):
    def test_invalid_price_is_rejected(self):
        form = ProductForm(data={
            "sku": "TEST-PRICE-01",
            "name": "Practice Product",
            "category": "Testing",
            "price": "0.00",
            "stock": 5,
            "is_active": True,
        })

        self.assertFalse(form.is_valid())
~~~

Adapt field values to the exact ProductForm in your project.

## 107. Test database constraints

A database constraint test should attempt to create a row that violates the constraint and assert the expected database error.

Use a transaction-aware test where needed.

Example concept:

~~~python
from django.db import IntegrityError, transaction
from django.test import TransactionTestCase
~~~

A full test must use the actual model fields and constraint name from the project.

Do not catch IntegrityError inside an active broken transaction and continue querying without rolling back to a savepoint or exiting the atomic block.

## 108. Test full_clean()

~~~python
from django.core.exceptions import ValidationError

product = Product(
    sku="CLEAN-TEST-01",
    name="   ",
    category="Testing",
    price=Decimal("10.00"),
    stock=3,
    is_active=True,
)

try:
    product.full_clean()
except ValidationError as error:
    print(error.message_dict)
~~~

Expected: validation reports the name rule if the model clean() method has been added as shown in this lesson.

## 109. Practice: decide the correct validation layer

For each rule, choose the appropriate layer and explain why:

1. Product name cannot be empty.
2. Product SKU must be unique.
3. Minimum salary cannot exceed maximum salary.
4. Product stock cannot be negative.
5. Email must have a valid format.
6. A user can edit only their own profile.

Suggested reasoning:
- Field required/format: form/model field validation.
- Cross-field rule: form clean() and possibly model clean().
- Unique or non-negative stored invariant: database constraint.
- Ownership: authorization check in the view, not a field validator.

## 110. Interview extension

**Question:** Does model.save() call full_clean()?

**Answer:** No. A developer must call full_clean() deliberately or use a form/model workflow that performs validation. Database constraints protect important stored invariants.

**Question:** Why do we need both a form validator and a database constraint?

**Answer:** The form gives a useful error to the user. The database constraint protects the data when another code path or concurrent request bypasses the form.

**Question:** Why can adding a constraint fail on an existing database?

**Answer:** Existing rows may violate the new rule. Inspect and correct legacy data before applying the constraint.

## 111. Final integrity checklist

- [ ] I can explain field validators.
- [ ] I can explain form clean().
- [ ] I can explain model clean().
- [ ] I can explain full_clean().
- [ ] I know save() does not automatically call full_clean().
- [ ] I can explain UniqueConstraint.
- [ ] I can explain CheckConstraint.
- [ ] I can explain IntegrityError.
- [ ] I understand race conditions.
- [ ] I can inspect existing data before adding constraints.
- [ ] I can review and apply migrations safely.
- [ ] I can test invalid data through both forms and the database.

