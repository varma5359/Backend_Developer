# Day 69: API Testing Using Postman and Automated Test Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–68 — DRF endpoints, serializers, authentication, permissions and filtering  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** Tested Student Management API

> **Trainer guidance:** API correctness requires more than a 200 response. Teach the learner to verify the status code, response body, database state, authentication behavior and automated tests.

## 1. Learning objectives

- Explain api testing using postman and automated test basics.
- Implement the example step by step.
- Understand how API consumers interpret responses or documentation.
- Verify successful and unsuccessful behavior.
- Complete Tested Student Management API.

## 2. Concept introduction

API testing verifies endpoints independently of the frontend. Postman helps send requests, organize collections and inspect responses. DRF's APITestCase and APIClient support automated tests for status codes, response data, validation, authentication and database behavior.

## 3. File-by-file implementation

### profiles/tests/test_api.py

```python
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="api_tester",
            password="Local-Test-Password-123"
        )
        self.client.force_authenticate(user=self.user)

    def test_employee_list_returns_200(self):
        url = reverse("employee_collection")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_employee_payload_returns_400(self):
        url = reverse("employee-list")
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
```

### Run tests

```python
python manage.py test profiles.tests
```

## 4. Explain the important statements

### profiles/tests/test_api.py

1. `from django.urls import reverse` — Imports DRF, Django or test components.
2. `from rest_framework import status` — Imports DRF, Django or test components.
3. `from rest_framework.test import APITestCase` — Imports DRF, Django or test components.
4. `from django.contrib.auth import get_user_model` — Imports DRF, Django or test components.
5. ` ` — Part of the configuration or test; explain its responsibility.
6. `User = get_user_model()` — Part of the configuration or test; explain its responsibility.
7. ` ` — Part of the configuration or test; explain its responsibility.
8. `class EmployeeAPITests(APITestCase):` — Part of the configuration or test; explain its responsibility.
9. `    def setUp(self):` — Defines an API view, exception handler or test method.
10. `        self.user = User.objects.create_user(` — Part of the configuration or test; explain its responsibility.
11. `            username="api_tester",` — Part of the configuration or test; explain its responsibility.
12. `            password="Local-Test-Password-123"` — Part of the configuration or test; explain its responsibility.
13. `        )` — Part of the configuration or test; explain its responsibility.
14. `        self.client.force_authenticate(user=self.user)` — Part of the configuration or test; explain its responsibility.
15. ` ` — Part of the configuration or test; explain its responsibility.
16. `    def test_employee_list_returns_200(self):` — Defines an API view, exception handler or test method.
17. `        url = reverse("employee-list")` — Part of the configuration or test; explain its responsibility.
18. `        response = self.client.get(url)` — Part of the configuration or test; explain its responsibility.
19. `        self.assertEqual(response.status_code, status.HTTP_200_OK)` — Uses a named HTTP status constant.
20. ` ` — Part of the configuration or test; explain its responsibility.
21. `    def test_invalid_employee_payload_returns_400(self):` — Defines an API view, exception handler or test method.
22. `        url = reverse("employee-list")` — Part of the configuration or test; explain its responsibility.
23. `        response = self.client.post(url, data={})` — Part of the configuration or test; explain its responsibility.
24. `        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)` — Uses a named HTTP status constant.

### Run tests

1. `python manage.py test profiles.tests` — Part of the configuration or test; explain its responsibility.

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

API testing verifies endpoints independently of the frontend. Postman helps send requests, organize collections and inspect responses. DRF's APITestCase and APIClient support automated tests for status codes, response data, validation, authentication and database behavior.

## 8. Approved mini-project — Tested Student Management API

**Objective:** Tested Student Management API.

### Required tasks

1. Create a Postman collection for the API.
2. Create an environment with a base URL variable.
3. Add requests for GET, POST, PUT/PATCH and DELETE.
4. Inspect status codes, headers and JSON response bodies.
5. Add Postman test scripts for expected status and response fields.
6. Create automated tests using APITestCase and APIClient.
7. Create test users and sample data in setUp().
8. Test successful and invalid requests.
9. Run the Django test command and inspect failures.
10. Keep test credentials local and fake.

### Suggested structure

```text
projects/day_69/
├── README.md
├── postman/
│   ├── collection.json
│   └── environment.example.json
├── config/
└── application/
    └── tests/
```

### Validation checklist

- [ ] Postman collection contains core endpoints.
- [ ] Environment variable stores the base URL.
- [ ] Tests assert status codes and response data.
- [ ] Invalid payload tests verify validation errors.
- [ ] Authentication behavior is tested.
- [ ] Automated tests run repeatably without production data.

### Submission evidence

- API response examples.
- OpenAPI schema and documentation screenshots.
- Postman collection with test results.
- Automated test output.
- README with API base URL and endpoint details.
- No real credentials, tokens or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Tested Student Management API. List endpoint behavior, response examples, documentation fields and automated test cases. Do not generate a complete project."

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

**Q1. Explain api testing using postman and automated test basics.**  
**Answer:** API testing verifies endpoints independently of the frontend. Postman helps send requests, organize collections and inspect responses. DRF's APITestCase and APIClient support automated tests for status codes, response data, validation, authentication and database behavior.

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
- [ ] Complete Tested Student Management API.
- [ ] Run positive and negative tests.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman, documentation and automated test evidence.

**Next lesson:** Phase 5 complete. Next: Phase 6 — Advanced Backend Development (Day 70).
