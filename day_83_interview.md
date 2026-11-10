# Day 83: Interview Questions — pytest Fundamentals, Fixtures and API Testing

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 83 class notes](day_83_notes.md)  
**Approved mini-project:** Automated API Test Suite

## Core technical questions

### Q1. Explain pytest fundamentals, fixtures and api testing.
**Answer:** pytest is a Python testing framework with concise assertions and fixtures for reusable test setup. pytest-django integrates pytest with Django's test database and settings. DRF's APIClient helps test API requests, authentication, response data and status codes without using a live external server.

### Q2. Which tools or files are involved?
**Answer:** Install test tools, pytest.ini, profiles/tests/test_api.py. Explain how they are used.

### Q3. What is one common mistake?
**Answer:** pytest discovers the tests. Explain how it affects repeatability or production safety.

### Q4. How do you verify the result?
**Answer:** Run the tests or checks and inspect the output. Include both successful and failure scenarios.

### Q5. What is one production consideration?
**Answer:** Repeatability, secret management, access control, logging and environment separation are important.

## Scenario questions

### Q6. A test passes locally but fails in another environment. What do you inspect?
**Suggested answer:** Dependency versions, settings module, environment variables, test database, test isolation and external service assumptions.

### Q7. How do you prove that configuration is safe?
**Suggested answer:** Verify secrets are loaded from protected environment settings, .env is ignored, DEBUG is disabled in production and allowed hosts are explicit.

## Project viva — Automated API Test Suite

1. What does the project verify?
2. Which tests or settings did you create?
3. How do you run them?
4. What failure case did you test?
5. How do you avoid relying on production data?
6. What would you improve?

## Rapid revision

- **1.** Install pytest and pytest-django in the virtual environment.
- **2.** Create pytest.ini with the Django settings module.
- **3.** Create a test file matching pytest naming rules.
- **4.** Create a fixture that returns APIClient.
- **5.** Mark tests that need database access with django_db.
- **6.** Test a successful API request.
- **7.** Test invalid JSON payload and expected 400 response.
- **8.** Run pytest and inspect the report.
- **9.** Use fixtures to share setup rather than duplicate it.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the command or configuration.
- [ ] Show test/check output.
- [ ] Explain one failure case.
- [ ] Present Automated API Test Suite.
