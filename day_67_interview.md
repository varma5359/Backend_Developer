# Day 67: Interview Questions — API Error Handling, Status Codes and Response Structure

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 67 class notes](day_67_notes.md)  
**Approved mini-project:** Standardized API Response System

## Core technical questions

### Q1. Explain api error handling, status codes and response structure.
**Answer:** An API should communicate success and failure consistently. HTTP status codes indicate the outcome, while the response body provides machine-readable details. DRF handles common exceptions, and a project can customize exception formatting carefully without hiding unexpected server failures.

### Q2. Which tools or Django components are involved?
**Answer:** profiles/api_views.py, config/settings.py — custom exception handler, config/api_exceptions.py. Explain how the example is configured and verified.

### Q3. What is one common mistake?
**Answer:** Successful create returns 201. Always verify actual output rather than assuming the endpoint is correct.

### Q4. How do you test the implementation?
**Answer:** Test success, validation failure, missing resource and authorization behavior. Inspect status, response body and database state.

### Q5. What evidence should a developer provide?
**Answer:** API request/response examples, documentation, test output and a README with reproducible instructions.

## Scenario questions

### Q6. An API returns 200 but the client still shows incorrect information. What do you inspect?
**Suggested answer:** Check response body, serializer fields, database state, query conditions and automated assertions. Status alone does not prove business correctness.

### Q7. Why document an API if the frontend developer can inspect the code?
**Suggested answer:** Documentation provides a stable contract for clients, including methods, payloads, authentication and expected responses.

## Project viva — Standardized API Response System

1. What does the project verify?
2. Which endpoints are included?
3. What status codes are expected?
4. Which invalid cases are tested?
5. What is documented in OpenAPI or Postman?
6. Which automated tests were written?
7. What would you improve?

## Rapid revision

- **1.** Review common HTTP status codes used by APIs.
- **2.** Create a consistent success response structure.
- **3.** Return 400 for invalid request data.
- **4.** Return 201 after successful resource creation.
- **5.** Use 404 for missing resources and 401/403 for authentication/permission outcomes.
- **6.** Understand DRF's default exception handling.
- **7.** Add a custom exception handler only when the project needs a consistent format.
- **8.** Test validation, missing resource and unexpected server errors separately.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the API.
- [ ] Explain error responses.
- [ ] Show documentation or test evidence.
- [ ] Present Standardized API Response System.
