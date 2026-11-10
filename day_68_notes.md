# Day 68: API Documentation Using Swagger and OpenAPI

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–68 — DRF endpoints, serializers, authentication, permissions and filtering  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** Documented REST API

> **Trainer guidance:** API correctness requires more than a 200 response. Teach the learner to verify the status code, response body, database state, authentication behavior and automated tests.

## 1. Learning objectives

- Explain api documentation using swagger and openapi.
- Implement the example step by step.
- Understand how API consumers interpret responses or documentation.
- Verify successful and unsuccessful behavior.
- Complete Documented REST API.

## 2. Concept introduction

OpenAPI is a machine-readable specification describing API paths, methods, parameters, request bodies, responses and security schemes. Swagger UI and Redoc can render an OpenAPI schema as interactive documentation. Documentation helps frontend developers and API consumers understand how to call endpoints.

## 3. File-by-file implementation

### Install package

```python
python -m pip install drf-spectacular
```

### config/settings.py

```python
INSTALLED_APPS = [
    # ...
    "drf_spectacular",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Employee Management API",
    "DESCRIPTION": "API documentation for the employee service",
    "VERSION": "1.0.0",
}
```

### config/urls.py

```python
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
```

## 4. Explain the important statements

### Install package

1. `python -m pip install drf-spectacular` — Part of the configuration or test; explain its responsibility.

### config/settings.py

1. `INSTALLED_APPS = [` — Part of the configuration or test; explain its responsibility.
2. `    # ...` — Part of the configuration or test; explain its responsibility.
3. `    "drf_spectacular",` — Part of the configuration or test; explain its responsibility.
4. `]` — Part of the configuration or test; explain its responsibility.
5. ` ` — Part of the configuration or test; explain its responsibility.
6. `REST_FRAMEWORK = {` — Part of the configuration or test; explain its responsibility.
7. `    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",` — Configures DRF's OpenAPI schema generation class.
8. `}` — Part of the configuration or test; explain its responsibility.
9. ` ` — Part of the configuration or test; explain its responsibility.
10. `SPECTACULAR_SETTINGS = {` — Part of the configuration or test; explain its responsibility.
11. `    "TITLE": "Employee Management API",` — Part of the configuration or test; explain its responsibility.
12. `    "DESCRIPTION": "API documentation for the employee service",` — Part of the configuration or test; explain its responsibility.
13. `    "VERSION": "1.0.0",` — Part of the configuration or test; explain its responsibility.
14. `}` — Part of the configuration or test; explain its responsibility.

### config/urls.py

1. `from django.urls import path` — Imports DRF, Django or test components.
2. `from drf_spectacular.views import (` — Imports DRF, Django or test components.
3. `    SpectacularAPIView,` — Connects the OpenAPI schema or rendered documentation view.
4. `    SpectacularSwaggerView,` — Connects the OpenAPI schema or rendered documentation view.
5. `    SpectacularRedocView,` — Connects the OpenAPI schema or rendered documentation view.
6. `)` — Part of the configuration or test; explain its responsibility.
7. ` ` — Part of the configuration or test; explain its responsibility.
8. `urlpatterns = [` — Part of the configuration or test; explain its responsibility.
9. `    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),` — Connects the OpenAPI schema or rendered documentation view.
10. `    path(` — Part of the configuration or test; explain its responsibility.
11. `        "api/docs/",` — Part of the configuration or test; explain its responsibility.
12. `        SpectacularSwaggerView.as_view(url_name="schema"),` — Connects the OpenAPI schema or rendered documentation view.
13. `        name="swagger-ui",` — Part of the configuration or test; explain its responsibility.
14. `    ),` — Part of the configuration or test; explain its responsibility.
15. `    path(` — Part of the configuration or test; explain its responsibility.
16. `        "api/redoc/",` — Part of the configuration or test; explain its responsibility.
17. `        SpectacularRedocView.as_view(url_name="schema"),` — Connects the OpenAPI schema or rendered documentation view.
18. `        name="redoc",` — Part of the configuration or test; explain its responsibility.
19. `    ),` — Part of the configuration or test; explain its responsibility.
20. `]` — Part of the configuration or test; explain its responsibility.

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

OpenAPI is a machine-readable specification describing API paths, methods, parameters, request bodies, responses and security schemes. Swagger UI and Redoc can render an OpenAPI schema as interactive documentation. Documentation helps frontend developers and API consumers understand how to call endpoints.

## 8. Approved mini-project — Documented REST API

**Objective:** Documented REST API.

### Required tasks

1. Install drf-spectacular into the active environment.
2. Add drf_spectacular to INSTALLED_APPS.
3. Configure DEFAULT_SCHEMA_CLASS.
4. Add title, description and version metadata.
5. Add schema, Swagger UI and Redoc URL patterns.
6. Run Django system checks.
7. Open the generated schema and interactive documentation.
8. Inspect an endpoint's methods, parameters, request body and response codes.
9. Keep internal or sensitive endpoints protected from public documentation when required.

### Suggested structure

```text
projects/day_68/
├── README.md
├── postman/
│   ├── collection.json
│   └── environment.example.json
├── config/
└── application/
    └── tests/
```

### Validation checklist

- [ ] Schema endpoint loads.
- [ ] Swagger UI loads the schema.
- [ ] Redoc displays API documentation.
- [ ] API paths and methods are present.
- [ ] Request/response examples are accurate.
- [ ] No secrets or private internal details are exposed.

### Submission evidence

- API response examples.
- OpenAPI schema and documentation screenshots.
- Postman collection with test results.
- Automated test output.
- README with API base URL and endpoint details.
- No real credentials, tokens or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Documented REST API. List endpoint behavior, response examples, documentation fields and automated test cases. Do not generate a complete project."

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

**Q1. Explain api documentation using swagger and openapi.**  
**Answer:** OpenAPI is a machine-readable specification describing API paths, methods, parameters, request bodies, responses and security schemes. Swagger UI and Redoc can render an OpenAPI schema as interactive documentation. Documentation helps frontend developers and API consumers understand how to call endpoints.

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
- [ ] Complete Documented REST API.
- [ ] Run positive and negative tests.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman, documentation and automated test evidence.

**Next lesson:** Day 69.
