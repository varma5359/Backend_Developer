# Day 57: Serializer Fields, Validation and Custom Validation Methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–54 — Django fundamentals, models, forms, authentication and permissions  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** Product Validation API

> **Trainer guidance:** An API is not just JSON text. Teach the request, validation, permission, database operation and response as one workflow. Test both successful and unsuccessful requests.

## 1. Learning objectives

- Explain serializer fields, validation and custom validation methods.
- Identify the DRF component responsible for the behavior.
- Implement the example step by step.
- Understand the data passed between API clients and Django.
- Validate normal and invalid cases.
- Complete Product Validation API.

## 2. Concept introduction

DRF serializers validate incoming API data before saving it. Field options define required, read-only, write-only and default behavior. validate_<field>() handles one field; validate() handles rules involving multiple fields. Raise serializers.ValidationError with useful messages when data is invalid.

## 3. API request-response flow

```text
API client (Postman / frontend)
       ↓ HTTP request
Django URL pattern
       ↓
DRF view
       ↓
Authentication and permissions
       ↓
Serializer validation
       ↓
Model / database
       ↓
Serializer representation
       ↓
HTTP response (JSON)
```

Not every endpoint uses every component, but this flow is a useful mental model for API development.

## 4. File-by-file implementation

### profiles/serializers.py

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "sku", "name", "price", "stock"]
        read_only_fields = ["id"]

    def validate_sku(self, value):
        normalized = value.strip().upper()
        if not normalized.startswith("P"):
            raise serializers.ValidationError(
                "SKU must start with P."
            )
        return normalized

    def validate(self, attrs):
        price = attrs.get("price")
        stock = attrs.get("stock")
        if price is not None and price <= 0:
            raise serializers.ValidationError(
                {"price": "Price must be greater than zero."}
            )
        if stock is not None and stock < 0:
            raise serializers.ValidationError(
                {"stock": "Stock cannot be negative."}
            )
        return attrs
```

### Serializer validation test

```python
serializer = ProductSerializer(data={
    "sku": "p-100",
    "name": "Keyboard",
    "price": "799.00",
    "stock": 12,
})

if serializer.is_valid():
    print(serializer.validated_data)
else:
    print(serializer.errors)
```

## 5. Explain the important statements

### profiles/serializers.py

1. `from rest_framework import serializers` — Imports DRF or the Django model.
2. `from .models import Product` — Imports DRF or the Django model.
3. ` ` — Part of the example; explain how it contributes to API data handling.
4. `class ProductSerializer(serializers.ModelSerializer):` — Defines a serializer or configuration class.
5. `    class Meta:` — Defines a serializer or configuration class.
6. `        model = Product` — Part of the example; explain how it contributes to API data handling.
7. `        fields = ["id", "sku", "name", "price", "stock"]` — Selects which data fields are included.
8. `        read_only_fields = ["id"]` — Selects which data fields are included.
9. ` ` — Part of the example; explain how it contributes to API data handling.
10. `    def validate_sku(self, value):` — Defines field-specific validation.
11. `        normalized = value.strip().upper()` — Part of the example; explain how it contributes to API data handling.
12. `        if not normalized.startswith("P"):` — Part of the example; explain how it contributes to API data handling.
13. `            raise serializers.ValidationError(` — Part of the example; explain how it contributes to API data handling.
14. `                "SKU must start with P."` — Part of the example; explain how it contributes to API data handling.
15. `            )` — Part of the example; explain how it contributes to API data handling.
16. `        return normalized` — Part of the example; explain how it contributes to API data handling.
17. ` ` — Part of the example; explain how it contributes to API data handling.
18. `    def validate(self, attrs):` — Defines object-level validation.
19. `        price = attrs.get("price")` — Part of the example; explain how it contributes to API data handling.
20. `        stock = attrs.get("stock")` — Part of the example; explain how it contributes to API data handling.
21. `        if price is not None and price <= 0:` — Part of the example; explain how it contributes to API data handling.
22. `            raise serializers.ValidationError(` — Part of the example; explain how it contributes to API data handling.
23. `                {"price": "Price must be greater than zero."}` — Part of the example; explain how it contributes to API data handling.
24. `            )` — Part of the example; explain how it contributes to API data handling.
25. `        if stock is not None and stock < 0:` — Part of the example; explain how it contributes to API data handling.
26. `            raise serializers.ValidationError(` — Part of the example; explain how it contributes to API data handling.
27. `                {"stock": "Stock cannot be negative."}` — Part of the example; explain how it contributes to API data handling.
28. `            )` — Part of the example; explain how it contributes to API data handling.
29. `        return attrs` — Part of the example; explain how it contributes to API data handling.

### Serializer validation test

1. `serializer = ProductSerializer(data={` — Part of the example; explain how it contributes to API data handling.
2. `    "sku": "p-100",` — Part of the example; explain how it contributes to API data handling.
3. `    "name": "Keyboard",` — Part of the example; explain how it contributes to API data handling.
4. `    "price": "799.00",` — Part of the example; explain how it contributes to API data handling.
5. `    "stock": 12,` — Part of the example; explain how it contributes to API data handling.
6. `})` — Part of the example; explain how it contributes to API data handling.
7. ` ` — Part of the example; explain how it contributes to API data handling.
8. `if serializer.is_valid():` — Runs validation before saving or using the data.
9. `    print(serializer.validated_data)` — Part of the example; explain how it contributes to API data handling.
10. `else:` — Part of the example; explain how it contributes to API data handling.
11. `    print(serializer.errors)` — Part of the example; explain how it contributes to API data handling.

## 6. Important API terminology

| Term | Meaning |
|---|---|
| Resource | Data or functionality exposed by an API |
| Endpoint | URL where a client accesses an API operation |
| Serializer | Converts complex objects to primitive data and validates incoming data |
| Representation | Data form sent to the client, often JSON |
| Validation | Checks submitted data against field and business rules |
| Read-only field | Included in output but not accepted as client-editable input |
| Write-only field | Accepted as input but not included in output |
| QuerySet | Collection of database records represented by a Django ORM query |

## 7. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| No module named rest_framework | Package installation and active environment |
| Serializer import error | App path and model name |
| Field does not exist | Model field name and Meta.fields |
| Serializer returns a list incorrectly | Use many=True for a queryset |
| Validation is skipped | Call is_valid() |
| Sensitive field exposed | Explicitly select serializer fields |
| Data saved before validation | Move save after successful validation |

## 8. Industry scenario

DRF serializers validate incoming API data before saving it. Field options define required, read-only, write-only and default behavior. validate_<field>() handles one field; validate() handles rules involving multiple fields. Raise serializers.ValidationError with useful messages when data is invalid.

## 9. Approved mini-project — Product Validation API

**Objective:** Product Validation API.

### Required tasks

1. Add a ModelSerializer for Product.
2. Choose fields and read-only fields explicitly.
3. Create validate_sku() for one-field normalization and checks.
4. Create validate() for rules involving more than one field.
5. Raise serializers.ValidationError with field-specific messages.
6. Call is_valid() before accessing validated_data.
7. Test valid, invalid and missing values.
8. Explain the difference between serializer validation and database constraints.

### Suggested structure

```text
projects/day_57/
├── README.md
├── config/
└── profiles/
    ├── models.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] Valid SKU is normalized.
- [ ] Invalid SKU is rejected.
- [ ] Non-positive price is rejected.
- [ ] Negative stock is rejected.
- [ ] Errors are returned in a structured format.
- [ ] No save occurs before validation.

### Submission evidence

- Serializer source file.
- Shell or API output.
- Valid and invalid sample payloads.
- README with setup and field decisions.
- Explanation of how serializer data differs from a model instance.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Product Validation API. List the serializer fields, validation rules, sample payloads and test cases. Do not write the complete API."

**Guided prompt:** "Explain one serializer field or validation method at a time. Wait for me to run the example before continuing."

**Debugging prompt:** "Here is my serializer, model and validation error. Explain why the field is failing and suggest the smallest correction."

**Review prompt:** "Review my serializer for exposed fields, validation rules, read-only behavior and useful error messages."

## 11. Five daily MCQs

**Q1. What is the main purpose of a DRF serializer?**  
A. Convert complex data to primitive representations and validate incoming data.  
B. Start the web server.  
C. Create a Git branch.  
D. Replace the database.  
**Answer: A.** Serializers support representation and validation.

**Q2. What should happen before serializer.save()?**  
A. Delete the model.  
B. Call is_valid() and confirm validation passed.  
C. Disable permissions.  
D. Ignore serializer.errors.  
**Answer: B.** Validate before saving.

**Q3. Which option marks an output field as not client-editable?**  
A. required=False only  
B. blank=True  
C. read_only_fields  
D. ordering  
**Answer: C.** read_only_fields marks serializer fields as read-only.

**Q4. Which method validates one named field?**  
A. validate_all()  
B. clean_model()  
C. save_field()  
D. validate_<field_name>()  
**Answer: D.** DRF calls field-specific validation methods.

**Q5. How do you serialize a queryset?**  
A. Use many=True.  
B. Use login().  
C. Use migrate.  
D. Use path().  
**Answer: A.** many=True indicates multiple objects.

## 12. Interview preparation

**Q1. Explain serializer fields, validation and custom validation methods.**  
**Answer:** DRF serializers validate incoming API data before saving it. Field options define required, read-only, write-only and default behavior. validate_<field>() handles one field; validate() handles rules involving multiple fields. Raise serializers.ValidationError with useful messages when data is invalid.

**Q2. What is one common mistake?**  
**Answer:** Valid SKU is normalized. Explain how you tested and corrected it.

**Q3. How do you verify the result?**  
**Answer:** Test a valid payload, an invalid payload and a missing-field case. Inspect serializer.data, validated_data or errors as appropriate.

**Follow-up:** Why should serializer fields be selected explicitly?  
**Answer:** It prevents accidental exposure of internal or sensitive model fields and creates a stable API contract.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the serializer example.
- [ ] Run valid and invalid cases.
- [ ] Explain the serializer fields.
- [ ] Complete Product Validation API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, payloads and evidence.

**Next lesson:** Day 58.
