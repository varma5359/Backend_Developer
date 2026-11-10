# Day 55: Introduction to REST APIs and Django REST Framework Installation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–54 — Django fundamentals, models, forms, authentication and permissions  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** REST API Environment Setup

> **Trainer guidance:** An API is not just JSON text. Teach the request, validation, permission, database operation and response as one workflow. Test both successful and unsuccessful requests.

## 1. Learning objectives

- Explain introduction to rest apis and django rest framework installation.
- Identify the DRF component responsible for the behavior.
- Implement the example step by step.
- Understand the data passed between API clients and Django.
- Validate normal and invalid cases.
- Complete REST API Environment Setup.

## 2. Concept introduction

A REST API exposes resources and operations over HTTP so clients such as browsers, mobile applications and other services can exchange data. Django REST Framework (DRF) adds serializers, API views, authentication, permissions, pagination and browsable API support to Django.

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

### Terminal commands

```bash
# Activate the project's virtual environment
python -m pip install djangorestframework

# Verify package installation
python -m pip show djangorestframework

# Run project checks
python manage.py check
```

### config/settings.py

```python
INSTALLED_APPS = [
    # Django applications...
    "rest_framework",
    "profiles",
]
```

## 5. Explain the important statements

### Terminal commands

1. `# Activate the project's virtual environment` — Part of the example; explain how it contributes to API data handling.
2. `python -m pip install djangorestframework` — Part of the example; explain how it contributes to API data handling.
3. ` ` — Part of the example; explain how it contributes to API data handling.
4. `# Verify package installation` — Part of the example; explain how it contributes to API data handling.
5. `python -m pip show djangorestframework` — Part of the example; explain how it contributes to API data handling.
6. ` ` — Part of the example; explain how it contributes to API data handling.
7. `# Run project checks` — Part of the example; explain how it contributes to API data handling.
8. `python manage.py check` — Part of the example; explain how it contributes to API data handling.

### config/settings.py

1. `INSTALLED_APPS = [` — Part of the example; explain how it contributes to API data handling.
2. `    # Django applications...` — Part of the example; explain how it contributes to API data handling.
3. `    "rest_framework",` — Part of the example; explain how it contributes to API data handling.
4. `    "profiles",` — Part of the example; explain how it contributes to API data handling.
5. `]` — Part of the example; explain how it contributes to API data handling.

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

A REST API exposes resources and operations over HTTP so clients such as browsers, mobile applications and other services can exchange data. Django REST Framework (DRF) adds serializers, API views, authentication, permissions, pagination and browsable API support to Django.

## 9. Approved mini-project — REST API Environment Setup

**Objective:** REST API Environment Setup.

### Required tasks

1. Explain resource-based API design using an Employee resource.
2. Install djangorestframework into the active virtual environment.
3. Add rest_framework to INSTALLED_APPS.
4. Run python manage.py check.
5. Understand JSON request and response representations.
6. Compare a server-rendered Django page with an API endpoint.
7. Create a short API environment README with package version and setup steps.

### Suggested structure

```text
projects/day_55/
├── README.md
├── config/
└── profiles/
    ├── models.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] DRF is installed in the active environment.
- [ ] rest_framework is listed in INSTALLED_APPS.
- [ ] Django system check passes.
- [ ] The learner can explain resource, endpoint, request and response.
- [ ] No API keys or credentials are committed.

### Submission evidence

- Serializer source file.
- Shell or API output.
- Valid and invalid sample payloads.
- README with setup and field decisions.
- Explanation of how serializer data differs from a model instance.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan REST API Environment Setup. List the serializer fields, validation rules, sample payloads and test cases. Do not write the complete API."

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

**Q1. Explain introduction to rest apis and django rest framework installation.**  
**Answer:** A REST API exposes resources and operations over HTTP so clients such as browsers, mobile applications and other services can exchange data. Django REST Framework (DRF) adds serializers, API views, authentication, permissions, pagination and browsable API support to Django.

**Q2. What is one common mistake?**  
**Answer:** DRF is installed in the active environment. Explain how you tested and corrected it.

**Q3. How do you verify the result?**  
**Answer:** Test a valid payload, an invalid payload and a missing-field case. Inspect serializer.data, validated_data or errors as appropriate.

**Follow-up:** Why should serializer fields be selected explicitly?  
**Answer:** It prevents accidental exposure of internal or sensitive model fields and creates a stable API contract.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the serializer example.
- [ ] Run valid and invalid cases.
- [ ] Explain the serializer fields.
- [ ] Complete REST API Environment Setup.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, payloads and evidence.

**Next lesson:** Day 56.
