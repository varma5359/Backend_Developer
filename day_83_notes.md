# Day 83: pytest Fundamentals, Fixtures and API Testing

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–83 — Django fundamentals, APIs, security and advanced backend concepts  
**Tools:** Python, Django, pytest where applicable, VS Code and terminal  
**Approved mini-project:** Automated API Test Suite

> **Trainer guidance:** Tests and configuration are part of application quality. Do not use production data or secrets in a learning environment. Ask the learner to show repeatable evidence rather than only saying "it works".

## 1. Learning objectives

- Explain pytest fundamentals, fixtures and api testing.
- Identify the files and tools involved.
- Implement the example step by step.
- Verify expected and failure behavior.
- Explain how the practice supports production readiness.
- Complete Automated API Test Suite.

## 2. Concept introduction

pytest is a Python testing framework with concise assertions and fixtures for reusable test setup. pytest-django integrates pytest with Django's test database and settings. DRF's APIClient helps test API requests, authentication, response data and status codes without using a live external server.

## 3. File-by-file implementation

### Install test tools

```python
python -m pip install pytest pytest-django
```

### pytest.ini

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = tests.py test_*.py *_tests.py
```

### profiles/tests/test_api.py

```python
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_employee_collection_returns_success(api_client):
    response = api_client.get(reverse("employee_collection"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_invalid_employee_payload_returns_400(api_client):
    response = api_client.post(
        reverse("employee_collection"),
        data={},
        format="json",
    )
    assert response.status_code == 400
```

## 4. Explain the important statements

### Install test tools

1. `python -m pip install pytest pytest-django` — Part of the configuration; explain how it affects repeatability or safety.

### pytest.ini

1. `[pytest]` — Part of the configuration; explain how it affects repeatability or safety.
2. `DJANGO_SETTINGS_MODULE = config.settings` — Tells pytest-django which Django settings module to load.
3. `python_files = tests.py test_*.py *_tests.py` — Part of the configuration; explain how it affects repeatability or safety.

### profiles/tests/test_api.py

1. `import pytest` — Part of the configuration; explain how it affects repeatability or safety.
2. `from django.urls import reverse` — Imports testing, configuration or application components.
3. `from rest_framework.test import APIClient` — Imports testing, configuration or application components.
4. ` ` — Part of the configuration; explain how it affects repeatability or safety.
5. `@pytest.fixture` — Defines reusable test setup.
6. `def api_client():` — Part of the configuration; explain how it affects repeatability or safety.
7. `    return APIClient()` — Part of the configuration; explain how it affects repeatability or safety.
8. ` ` — Part of the configuration; explain how it affects repeatability or safety.
9. `@pytest.mark.django_db` — Part of the configuration; explain how it affects repeatability or safety.
10. `def test_employee_collection_returns_success(api_client):` — Defines one independently executable test.
11. `    response = api_client.get(reverse("employee_collection"))` — Part of the configuration; explain how it affects repeatability or safety.
12. `    assert response.status_code == 200` — Checks actual behavior against an expected result.
13. ` ` — Part of the configuration; explain how it affects repeatability or safety.
14. `@pytest.mark.django_db` — Part of the configuration; explain how it affects repeatability or safety.
15. `def test_invalid_employee_payload_returns_400(api_client):` — Defines one independently executable test.
16. `    response = api_client.post(` — Part of the configuration; explain how it affects repeatability or safety.
17. `        reverse("employee_collection"),` — Part of the configuration; explain how it affects repeatability or safety.
18. `        data={},` — Part of the configuration; explain how it affects repeatability or safety.
19. `        format="json",` — Part of the configuration; explain how it affects repeatability or safety.
20. `    )` — Part of the configuration; explain how it affects repeatability or safety.
21. `    assert response.status_code == 400` — Checks actual behavior against an expected result.

## 5. Important terminology

| Term | Meaning |
|---|---|
| Unit test | Tests one small unit of behavior |
| Integration test | Tests multiple components working together |
| Fixture | Reusable test setup or data |
| Test client | Simulates requests to a Django application |
| APIClient | DRF test client for API requests |
| Environment variable | Configuration value supplied to the process |
| Secret | Sensitive configuration that must remain protected |
| Deployment check | Django check for production configuration issues |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Test not discovered | Filename and test function naming |
| Database access denied | Test database setup and markers |
| Wrong URL reverse name | URL pattern name |
| Test depends on prior test | Missing setup/cleanup and shared state |
| Secret missing | Environment variable configuration |
| DEBUG accidentally enabled | Production settings source |
| .env appears in Git | .gitignore and tracked-file status |

## 7. Industry scenario

pytest is a Python testing framework with concise assertions and fixtures for reusable test setup. pytest-django integrates pytest with Django's test database and settings. DRF's APIClient helps test API requests, authentication, response data and status codes without using a live external server.

## 8. Approved mini-project — Automated API Test Suite

**Objective:** Automated API Test Suite.

### Required tasks

1. Install pytest and pytest-django in the virtual environment.
2. Create pytest.ini with the Django settings module.
3. Create a test file matching pytest naming rules.
4. Create a fixture that returns APIClient.
5. Mark tests that need database access with django_db.
6. Test a successful API request.
7. Test invalid JSON payload and expected 400 response.
8. Run pytest and inspect the report.
9. Use fixtures to share setup rather than duplicate it.

### Suggested structure

```text
projects/day_83/
├── README.md
├── pytest.ini
├── .env.example
└── application/
    └── tests/
```

### Validation checklist

- [ ] pytest discovers the tests.
- [ ] Django settings are loaded.
- [ ] APIClient sends requests.
- [ ] Database marker is used where required.
- [ ] Success and validation failure are tested.
- [ ] Test output is repeatable.

### Submission evidence

- Test files and test output.
- Screenshots or terminal report.
- Example configuration file.
- README with commands and setup.
- No production secrets or real user data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Automated API Test Suite. List test cases or configuration values, files, commands and expected results. Do not write the complete test suite."

**Guided prompt:** "Help me write one test or setting at a time. Explain what it proves and wait for the test result."

**Debugging prompt:** "Here is my test failure or sanitized configuration. Identify the root cause and the smallest safe fix."

**Review prompt:** "Review the tests or settings for coverage, repeatability, secret safety and production readiness."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Make behavior repeatable and configuration safe.  
B. Replace Python.  
C. Disable errors.  
D. Commit secrets.  
**Answer: A.** Testing and configuration support reliable applications.

**Q2. What should a test verify?**  
A. Only that a file exists.  
B. Expected behavior and important failure cases.  
C. Only the editor theme.  
D. Nothing.  
**Answer: B.** Tests should verify observable behavior.

**Q3. What is a fixture used for?**  
A. Styling templates.  
B. Creating a Git tag.  
C. Reusable test setup.  
D. Replacing Django settings.  
**Answer: C.** Fixtures provide shared setup or test data.

**Q4. Should a real .env file be committed?**  
A. Always.  
B. Only if it contains a password.  
C. If it is renamed.  
D. No. Keep it ignored and provide a placeholder example.  
**Answer: D.** Do not commit private configuration.

**Q5. What is the strongest evidence of completion?**  
A. Repeatable tests pass and invalid cases are covered.  
B. A project folder exists.  
C. A code screenshot only.  
D. A planned test list only.  
**Answer: A.** Execution and results are required.

## 11. Interview preparation

**Q1. Explain pytest fundamentals, fixtures and api testing.**  
**Answer:** pytest is a Python testing framework with concise assertions and fixtures for reusable test setup. pytest-django integrates pytest with Django's test database and settings. DRF's APIClient helps test API requests, authentication, response data and status codes without using a live external server.

**Q2. What is one common failure?**  
**Answer:** pytest discovers the tests. Explain how to reproduce and fix it.

**Q3. How do you verify the implementation?**  
**Answer:** Run the test or deployment check, inspect output and confirm both expected and failure behavior.

**Follow-up:** Why should tests be isolated?  
**Answer:** Tests should not depend on previous tests or real external state, so they remain repeatable.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run tests or checks.
- [ ] Verify expected and failure behavior.
- [ ] Complete Automated API Test Suite.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence.

**Next lesson:** Day 84.
