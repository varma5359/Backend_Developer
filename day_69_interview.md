# Day 69: Interview Questions — API Testing Using Postman and Automated Test Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 69 class notes](day_69_notes.md)  
**Approved mini-project:** Tested Student Management API

## Core technical questions

### Q1. Explain api testing using postman and automated test basics.
**Answer:** API testing verifies endpoints independently of the frontend. Postman helps send requests, organize collections and inspect responses. DRF's APITestCase and APIClient support automated tests for status codes, response data, validation, authentication and database behavior.

### Q2. Which tools or Django components are involved?
**Answer:** profiles/tests/test_api.py, Run tests. Explain how the example is configured and verified.

### Q3. What is one common mistake?
**Answer:** Postman collection contains core endpoints. Always verify actual output rather than assuming the endpoint is correct.

### Q4. How do you test the implementation?
**Answer:** Test success, validation failure, missing resource and authorization behavior. Inspect status, response body and database state.

### Q5. What evidence should a developer provide?
**Answer:** API request/response examples, documentation, test output and a README with reproducible instructions.

## Scenario questions

### Q6. An API returns 200 but the client still shows incorrect information. What do you inspect?
**Suggested answer:** Check response body, serializer fields, database state, query conditions and automated assertions. Status alone does not prove business correctness.

### Q7. Why document an API if the frontend developer can inspect the code?
**Suggested answer:** Documentation provides a stable contract for clients, including methods, payloads, authentication and expected responses.

## Project viva — Tested Student Management API

1. What does the project verify?
2. Which endpoints are included?
3. What status codes are expected?
4. Which invalid cases are tested?
5. What is documented in OpenAPI or Postman?
6. Which automated tests were written?
7. What would you improve?

## Rapid revision

- **1.** Create a Postman collection for the API.
- **2.** Create an environment with a base URL variable.
- **3.** Add requests for GET, POST, PUT/PATCH and DELETE.
- **4.** Inspect status codes, headers and JSON response bodies.
- **5.** Add Postman test scripts for expected status and response fields.
- **6.** Create automated tests using APITestCase and APIClient.
- **7.** Create test users and sample data in setUp().
- **8.** Test successful and invalid requests.
- **9.** Run the Django test command and inspect failures.
- **10.** Keep test credentials local and fake.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the API.
- [ ] Explain error responses.
- [ ] Show documentation or test evidence.
- [ ] Present Tested Student Management API.
