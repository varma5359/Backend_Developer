# Day 82: Interview Questions — Unit Testing, Integration Testing and Django TestCase

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 82 class notes](day_82_notes.md)  
**Approved mini-project:** Django Application Test Suite

## Core technical questions

### Q1. Explain unit testing, integration testing and django testcase.
**Answer:** Unit tests verify a small unit of behavior; integration tests verify connected components work together. Django TestCase provides an isolated test database, request client and assertions for models, views and responses. Tests should cover expected behavior and important failure cases.

### Q2. Which tools or files are involved?
**Answer:** profiles/tests.py, Run tests. Explain how they are used.

### Q3. What is one common mistake?
**Answer:** Tests run using Django's test command. Explain how it affects repeatability or production safety.

### Q4. How do you verify the result?
**Answer:** Run the tests or checks and inspect the output. Include both successful and failure scenarios.

### Q5. What is one production consideration?
**Answer:** Repeatability, secret management, access control, logging and environment separation are important.

## Scenario questions

### Q6. A test passes locally but fails in another environment. What do you inspect?
**Suggested answer:** Dependency versions, settings module, environment variables, test database, test isolation and external service assumptions.

### Q7. How do you prove that configuration is safe?
**Suggested answer:** Verify secrets are loaded from protected environment settings, .env is ignored, DEBUG is disabled in production and allowed hosts are explicit.

## Project viva — Django Application Test Suite

1. What does the project verify?
2. Which tests or settings did you create?
3. How do you run them?
4. What failure case did you test?
5. How do you avoid relying on production data?
6. What would you improve?

## Rapid revision

- **1.** Explain why tests are written before deployment.
- **2.** Create a tests module for the app.
- **3.** Write a model test for __str__ or a business method.
- **4.** Write a view test using Django's test client.
- **5.** Use setUp() when multiple tests need common test data.
- **6.** Use assertions for status, content and database state.
- **7.** Run tests using python manage.py test.
- **8.** Test both expected and failure behavior.
- **9.** Explain the difference between unit and integration tests.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the command or configuration.
- [ ] Show test/check output.
- [ ] Explain one failure case.
- [ ] Present Django Application Test Suite.
