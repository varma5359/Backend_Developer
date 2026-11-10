# Day 82: Unit Testing, Integration Testing and Django TestCase

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–83 — Django fundamentals, APIs, security and advanced backend concepts  
**Tools:** Python, Django, pytest where applicable, VS Code and terminal  
**Approved mini-project:** Django Application Test Suite

> **Trainer guidance:** Tests and configuration are part of application quality. Do not use production data or secrets in a learning environment. Ask the learner to show repeatable evidence rather than only saying "it works".

## 1. Learning objectives

- Explain unit testing, integration testing and django testcase.
- Identify the files and tools involved.
- Implement the example step by step.
- Verify expected and failure behavior.
- Explain how the practice supports production readiness.
- Complete Django Application Test Suite.

## 2. Concept introduction

Unit tests verify a small unit of behavior; integration tests verify connected components work together. Django TestCase provides an isolated test database, request client and assertions for models, views and responses. Tests should cover expected behavior and important failure cases.

## 3. File-by-file implementation

### profiles/tests.py

```python
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from profiles.models import Employee

User = get_user_model()

class EmployeeModelTests(TestCase):
    def test_employee_string_representation(self):
        employee = Employee.objects.create(
            employee_code="EMP101",
            full_name="Asha Rao",
            email="asha@example.test",
            department="ENG",
            salary="45000.00",
            joining_date="2025-01-10",
        )
        self.assertIn("EMP101", str(employee))

class EmployeeViewTests(TestCase):
    def test_employee_list_returns_200(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 200)
```

### Run tests

```python
python manage.py test profiles
```

## 4. Explain the important statements

### profiles/tests.py

1. `from django.test import TestCase` — Imports testing, configuration or application components.
2. `from django.urls import reverse` — Imports testing, configuration or application components.
3. `from django.contrib.auth import get_user_model` — Imports testing, configuration or application components.
4. `from profiles.models import Employee` — Imports testing, configuration or application components.
5. ` ` — Part of the configuration; explain how it affects repeatability or safety.
6. `User = get_user_model()` — Part of the configuration; explain how it affects repeatability or safety.
7. ` ` — Part of the configuration; explain how it affects repeatability or safety.
8. `class EmployeeModelTests(TestCase):` — Defines a test class.
9. `    def test_employee_string_representation(self):` — Defines one independently executable test.
10. `        employee = Employee.objects.create(` — Part of the configuration; explain how it affects repeatability or safety.
11. `            employee_code="EMP101",` — Part of the configuration; explain how it affects repeatability or safety.
12. `            full_name="Asha Rao",` — Part of the configuration; explain how it affects repeatability or safety.
13. `            email="asha@example.test",` — Part of the configuration; explain how it affects repeatability or safety.
14. `            department="ENG",` — Part of the configuration; explain how it affects repeatability or safety.
15. `            salary="45000.00",` — Part of the configuration; explain how it affects repeatability or safety.
16. `            joining_date="2025-01-10",` — Part of the configuration; explain how it affects repeatability or safety.
17. `        )` — Part of the configuration; explain how it affects repeatability or safety.
18. `        self.assertIn("EMP101", str(employee))` — Checks actual behavior against an expected result.
19. ` ` — Part of the configuration; explain how it affects repeatability or safety.
20. `class EmployeeViewTests(TestCase):` — Defines a test class.
21. `    def test_employee_list_returns_200(self):` — Defines one independently executable test.
22. `        response = self.client.get(reverse("employee_list"))` — Part of the configuration; explain how it affects repeatability or safety.
23. `        self.assertEqual(response.status_code, 200)` — Checks actual behavior against an expected result.

### Run tests

1. `python manage.py test profiles` — Part of the configuration; explain how it affects repeatability or safety.

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

Unit tests verify a small unit of behavior; integration tests verify connected components work together. Django TestCase provides an isolated test database, request client and assertions for models, views and responses. Tests should cover expected behavior and important failure cases.

## 8. Approved mini-project — Django Application Test Suite

**Objective:** Django Application Test Suite.

### Required tasks

1. Explain why tests are written before deployment.
2. Create a tests module for the app.
3. Write a model test for __str__ or a business method.
4. Write a view test using Django's test client.
5. Use setUp() when multiple tests need common test data.
6. Use assertions for status, content and database state.
7. Run tests using python manage.py test.
8. Test both expected and failure behavior.
9. Explain the difference between unit and integration tests.

### Suggested structure

```text
projects/day_82/
├── README.md
├── pytest.ini
├── .env.example
└── application/
    └── tests/
```

### Validation checklist

- [ ] Tests run using Django's test command.
- [ ] Model behavior is tested.
- [ ] A view response is tested.
- [ ] Tests use isolated test data.
- [ ] At least one invalid or missing-data case is tested.
- [ ] Test names explain the behavior.

### Submission evidence

- Test files and test output.
- Screenshots or terminal report.
- Example configuration file.
- README with commands and setup.
- No production secrets or real user data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Django Application Test Suite. List test cases or configuration values, files, commands and expected results. Do not write the complete test suite."

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

**Q1. Explain unit testing, integration testing and django testcase.**  
**Answer:** Unit tests verify a small unit of behavior; integration tests verify connected components work together. Django TestCase provides an isolated test database, request client and assertions for models, views and responses. Tests should cover expected behavior and important failure cases.

**Q2. What is one common failure?**  
**Answer:** Tests run using Django's test command. Explain how to reproduce and fix it.

**Q3. How do you verify the implementation?**  
**Answer:** Run the test or deployment check, inspect output and confirm both expected and failure behavior.

**Follow-up:** Why should tests be isolated?  
**Answer:** Tests should not depend on previous tests or real external state, so they remain repeatable.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run tests or checks.
- [ ] Verify expected and failure behavior.
- [ ] Complete Django Application Test Suite.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence.

**Next lesson:** Day 83.
