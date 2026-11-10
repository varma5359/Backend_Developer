# Day 67: API Error Handling, Status Codes and Response Structure

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–68 — DRF endpoints, serializers, authentication, permissions and filtering  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** Standardized API Response System

> **Trainer guidance:** API correctness requires more than a 200 response. Teach the learner to verify the status code, response body, database state, authentication behavior and automated tests.

## 1. Learning objectives

- Explain api error handling, status codes and response structure.
- Implement the example step by step.
- Understand how API consumers interpret responses or documentation.
- Verify successful and unsuccessful behavior.
- Complete Standardized API Response System.

## 2. Concept introduction

An API should communicate success and failure consistently. HTTP status codes indicate the outcome, while the response body provides machine-readable details. DRF handles common exceptions, and a project can customize exception formatting carefully without hiding unexpected server failures.

## 3. File-by-file implementation

### profiles/api_views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(["POST"])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "message": "Validation failed",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    product = serializer.save()
    return Response(
        {
            "success": True,
            "message": "Product created",
            "data": ProductSerializer(product).data,
        },
        status=status.HTTP_201_CREATED,
    )
```

### config/settings.py — custom exception handler

```python
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "config.api_exceptions.custom_exception_handler",
}
```

### config/api_exceptions.py

```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "errors": response.data,
        }

    return response
```

## 4. Explain the important statements

### profiles/api_views.py

1. `from rest_framework.decorators import api_view` — Imports DRF, Django or test components.
2. `from rest_framework.response import Response` — Imports DRF, Django or test components.
3. `from rest_framework import status` — Imports DRF, Django or test components.
4. `from .models import Product` — Imports DRF, Django or test components.
5. `from .serializers import ProductSerializer` — Imports DRF, Django or test components.
6. ` ` — Part of the configuration or test; explain its responsibility.
7. `@api_view(["POST"])` — Part of the configuration or test; explain its responsibility.
8. `def create_product(request):` — Defines an API view, exception handler or test method.
9. `    serializer = ProductSerializer(data=request.data)` — Part of the configuration or test; explain its responsibility.
10. `    if not serializer.is_valid():` — Part of the configuration or test; explain its responsibility.
11. `        return Response(` — Builds a response body and status.
12. `            {` — Part of the configuration or test; explain its responsibility.
13. `                "success": False,` — Part of the configuration or test; explain its responsibility.
14. `                "message": "Validation failed",` — Part of the configuration or test; explain its responsibility.
15. `                "errors": serializer.errors,` — Part of the configuration or test; explain its responsibility.
16. `            },` — Part of the configuration or test; explain its responsibility.
17. `            status=status.HTTP_400_BAD_REQUEST,` — Uses a named HTTP status constant.
18. `        )` — Part of the configuration or test; explain its responsibility.
19. ` ` — Part of the configuration or test; explain its responsibility.
20. `    product = serializer.save()` — Part of the configuration or test; explain its responsibility.
21. `    return Response(` — Builds a response body and status.
22. `        {` — Part of the configuration or test; explain its responsibility.
23. `            "success": True,` — Part of the configuration or test; explain its responsibility.
24. `            "message": "Product created",` — Part of the configuration or test; explain its responsibility.
25. `            "data": ProductSerializer(product).data,` — Part of the configuration or test; explain its responsibility.
26. `        },` — Part of the configuration or test; explain its responsibility.
27. `        status=status.HTTP_201_CREATED,` — Uses a named HTTP status constant.
28. `    )` — Part of the configuration or test; explain its responsibility.

### config/settings.py — custom exception handler

1. `REST_FRAMEWORK = {` — Part of the configuration or test; explain its responsibility.
2. `    "EXCEPTION_HANDLER": "config.api_exceptions.custom_exception_handler",` — Part of the configuration or test; explain its responsibility.
3. `}` — Part of the configuration or test; explain its responsibility.

### config/api_exceptions.py

1. `from rest_framework.views import exception_handler` — Imports DRF, Django or test components.
2. ` ` — Part of the configuration or test; explain its responsibility.
3. `def custom_exception_handler(exc, context):` — Defines an API view, exception handler or test method.
4. `    response = exception_handler(exc, context)` — Part of the configuration or test; explain its responsibility.
5. ` ` — Part of the configuration or test; explain its responsibility.
6. `    if response is not None:` — Part of the configuration or test; explain its responsibility.
7. `        response.data = {` — Part of the configuration or test; explain its responsibility.
8. `            "success": False,` — Part of the configuration or test; explain its responsibility.
9. `            "errors": response.data,` — Part of the configuration or test; explain its responsibility.
10. `        }` — Part of the configuration or test; explain its responsibility.
11. ` ` — Part of the configuration or test; explain its responsibility.
12. `    return response` — Part of the configuration or test; explain its responsibility.

## 5. Status code reference

| Status | Meaning | Example |
|---|---|---|
| 200 | OK | Successful retrieval |
| 201 | Created | Resource successfully created |
| 204 | No Content | Successful deletion |
| 400 | Bad Request | Invalid payload |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated user lacks permission |
| 404 | Not Found | Resource does not exist |
| 405 | Method Not Allowed | Unsupported HTTP method |
| 500 | Internal Server Error | Unexpected server failure |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| API returns wrong status | View branch and status constant |
| Error response shape differs | DRF exception handler and custom response code |
| Schema omits endpoint | URL registration and schema introspection |
| Swagger UI fails | Schema URL and package configuration |
| Test returns 401/403 | Authentication setup and permissions |
| Test database missing table | Migrations and test setup |
| Tests pass locally but fail in CI | Environment dependencies and test isolation |

## 7. Industry scenario

An API should communicate success and failure consistently. HTTP status codes indicate the outcome, while the response body provides machine-readable details. DRF handles common exceptions, and a project can customize exception formatting carefully without hiding unexpected server failures.

## 8. Approved mini-project — Standardized API Response System

**Objective:** Standardized API Response System.

### Required tasks

1. Review common HTTP status codes used by APIs.
2. Create a consistent success response structure.
3. Return 400 for invalid request data.
4. Return 201 after successful resource creation.
5. Use 404 for missing resources and 401/403 for authentication/permission outcomes.
6. Understand DRF's default exception handling.
7. Add a custom exception handler only when the project needs a consistent format.
8. Test validation, missing resource and unexpected server errors separately.

### Suggested structure

```text
projects/day_67/
├── README.md
├── postman/
│   ├── collection.json
│   └── environment.example.json
├── config/
└── application/
    └── tests/
```

### Validation checklist

- [ ] Successful create returns 201.
- [ ] Invalid input returns 400 with structured errors.
- [ ] Missing resource returns 404.
- [ ] Authentication and permission errors use suitable status codes.
- [ ] Unexpected exceptions are not silently converted into success.
- [ ] Response structure is documented.

### Submission evidence

- API response examples.
- OpenAPI schema and documentation screenshots.
- Postman collection with test results.
- Automated test output.
- README with API base URL and endpoint details.
- No real credentials, tokens or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Standardized API Response System. List endpoint behavior, response examples, documentation fields and automated test cases. Do not generate a complete project."

**Guided prompt:** "Help me add one response or test case at a time. Explain what the assertion proves."

**Debugging prompt:** "Here is my Postman request or failing test output, status code and response body. Explain the cause and how to reproduce the fix."

**Review prompt:** "Review the API for consistent errors, accurate OpenAPI documentation and meaningful test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Make API behavior predictable, documented or testable.  
B. Replace the database.  
C. Disable validation.  
D. Remove HTTP methods.  
**Answer: A.** Consistency, documentation and tests help API consumers and developers.

**Q2. Which status is commonly returned after resource creation?**  
A. 404  
B. 201  
C. 500  
D. 403  
**Answer: B.** 201 Created indicates a resource was created.

**Q3. What does OpenAPI describe?**  
A. Python virtual environments.  
B. Git commits.  
C. API paths, operations, parameters, request/response schemas and security.  
D. Database backups only.  
**Answer: C.** OpenAPI is a machine-readable API specification.

**Q4. What should an automated API test assert?**  
A. Only that a file exists.  
B. Only that the server starts.  
C. Only the editor theme.  
D. Expected status, response data and relevant database behavior.  
**Answer: D.** Tests should verify observable behavior.

**Q5. What is the safest test data?**  
A. Fake local users and sample records.  
B. Real customer passwords.  
C. Production access tokens.  
D. Private API keys.  
**Answer: A.** Use isolated test data.

## 11. Interview preparation

**Q1. Explain api error handling, status codes and response structure.**  
**Answer:** An API should communicate success and failure consistently. HTTP status codes indicate the outcome, while the response body provides machine-readable details. DRF handles common exceptions, and a project can customize exception formatting carefully without hiding unexpected server failures.

**Q2. Why are API tests necessary?**  
**Answer:** They verify endpoint behavior independently of the frontend and help detect regressions in status codes, validation, permissions and data handling.

**Q3. What should API documentation contain?**  
**Answer:** Endpoints, HTTP methods, parameters, authentication requirements, request schemas, response schemas and status codes.

**Follow-up:** Why is a 200 status alone not enough?  
**Answer:** The response could still contain incorrect data or the database could be in the wrong state. Test content and side effects as well.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Verify status codes and response structure.
- [ ] Complete Standardized API Response System.
- [ ] Run positive and negative tests.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman, documentation and automated test evidence.

**Next lesson:** Day 68.
