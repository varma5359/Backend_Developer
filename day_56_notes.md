# Day 56: Serializers and Converting Django Models into JSON

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–54 — Django fundamentals, models, forms, authentication and permissions  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** Employee Data Serializer

> **Trainer guidance:** An API is not just JSON text. Teach the request, validation, permission, database operation and response as one workflow. Test both successful and unsuccessful requests.

## 1. Learning objectives

- Explain serializers and converting django models into json.
- Identify the DRF component responsible for the behavior.
- Implement the example step by step.
- Understand the data passed between API clients and Django.
- Validate normal and invalid cases.
- Complete Employee Data Serializer.

## 2. Concept introduction

A serializer converts complex Python objects such as Django model instances into primitive data types that can be rendered as JSON. It can also deserialize incoming data and validate it before creating or updating model instances. ModelSerializer can derive fields and default validation from a Django model.

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
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_code",
            "full_name",
            "email",
            "department",
            "salary",
            "joining_date",
            "is_active",
        ]
        read_only_fields = ["id"]
```

### Django shell

```bash
python manage.py shell
```

### Serializer usage

```python
from profiles.models import Employee
from profiles.serializers import EmployeeSerializer

employee = Employee.objects.first()
serializer = EmployeeSerializer(employee)

print(serializer.data)
```

## 5. Explain the important statements

### profiles/serializers.py

1. `from rest_framework import serializers` — Imports DRF or the Django model.
2. `from .models import Employee` — Imports DRF or the Django model.
3. ` ` — Part of the example; explain how it contributes to API data handling.
4. `class EmployeeSerializer(serializers.ModelSerializer):` — Defines a serializer or configuration class.
5. `    class Meta:` — Defines a serializer or configuration class.
6. `        model = Employee` — Part of the example; explain how it contributes to API data handling.
7. `        fields = [` — Selects which data fields are included.
8. `            "id",` — Part of the example; explain how it contributes to API data handling.
9. `            "employee_code",` — Part of the example; explain how it contributes to API data handling.
10. `            "full_name",` — Part of the example; explain how it contributes to API data handling.
11. `            "email",` — Part of the example; explain how it contributes to API data handling.
12. `            "department",` — Part of the example; explain how it contributes to API data handling.
13. `            "salary",` — Part of the example; explain how it contributes to API data handling.
14. `            "joining_date",` — Part of the example; explain how it contributes to API data handling.
15. `            "is_active",` — Part of the example; explain how it contributes to API data handling.
16. `        ]` — Part of the example; explain how it contributes to API data handling.
17. `        read_only_fields = ["id"]` — Selects which data fields are included.

### Django shell

1. `python manage.py shell` — Part of the example; explain how it contributes to API data handling.

### Serializer usage

1. `from profiles.models import Employee` — Imports DRF or the Django model.
2. `from profiles.serializers import EmployeeSerializer` — Imports DRF or the Django model.
3. ` ` — Part of the example; explain how it contributes to API data handling.
4. `employee = Employee.objects.first()` — Part of the example; explain how it contributes to API data handling.
5. `serializer = EmployeeSerializer(employee)` — Part of the example; explain how it contributes to API data handling.
6. ` ` — Part of the example; explain how it contributes to API data handling.
7. `print(serializer.data)` — Reads the serialized representation.

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

A serializer converts complex Python objects such as Django model instances into primitive data types that can be rendered as JSON. It can also deserialize incoming data and validate it before creating or updating model instances. ModelSerializer can derive fields and default validation from a Django model.

## 9. Approved mini-project — Employee Data Serializer

**Objective:** Employee Data Serializer.

### Required tasks

1. Create profiles/serializers.py.
2. Import serializers and the Employee model.
3. Create EmployeeSerializer inheriting from ModelSerializer.
4. Set Meta.model to Employee.
5. Select the API fields explicitly.
6. Mark database-generated ID as read-only.
7. Serialize one model instance and inspect serializer.data.
8. Serialize a queryset using many=True.
9. Explain that serializer.data contains primitive values, not a raw database connection.

### Suggested structure

```text
projects/day_56/
├── README.md
├── config/
└── profiles/
    ├── models.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] Serializer imports successfully.
- [ ] Meta.model points to Employee.
- [ ] Only approved fields are exposed.
- [ ] A model instance serializes correctly.
- [ ] A queryset uses many=True.
- [ ] Read-only ID is not treated as client-editable.

### Submission evidence

- Serializer source file.
- Shell or API output.
- Valid and invalid sample payloads.
- README with setup and field decisions.
- Explanation of how serializer data differs from a model instance.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Employee Data Serializer. List the serializer fields, validation rules, sample payloads and test cases. Do not write the complete API."

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

**Q1. Explain serializers and converting django models into json.**  
**Answer:** A serializer converts complex Python objects such as Django model instances into primitive data types that can be rendered as JSON. It can also deserialize incoming data and validate it before creating or updating model instances. ModelSerializer can derive fields and default validation from a Django model.

**Q2. What is one common mistake?**  
**Answer:** Serializer imports successfully. Explain how you tested and corrected it.

**Q3. How do you verify the result?**  
**Answer:** Test a valid payload, an invalid payload and a missing-field case. Inspect serializer.data, validated_data or errors as appropriate.

**Follow-up:** Why should serializer fields be selected explicitly?  
**Answer:** It prevents accidental exposure of internal or sensitive model fields and creates a stable API contract.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the serializer example.
- [ ] Run valid and invalid cases.
- [ ] Explain the serializer fields.
- [ ] Complete Employee Data Serializer.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, payloads and evidence.

**Next lesson:** Day 57.
