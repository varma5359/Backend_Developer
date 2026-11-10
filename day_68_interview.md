# Day 68: Interview Questions — API Documentation Using Swagger and OpenAPI

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 68 class notes](day_68_notes.md)  
**Approved mini-project:** Documented REST API

## Core technical questions

### Q1. Explain api documentation using swagger and openapi.
**Answer:** OpenAPI is a machine-readable specification describing API paths, methods, parameters, request bodies, responses and security schemes. Swagger UI and Redoc can render an OpenAPI schema as interactive documentation. Documentation helps frontend developers and API consumers understand how to call endpoints.

### Q2. Which tools or Django components are involved?
**Answer:** Install package, config/settings.py, config/urls.py. Explain how the example is configured and verified.

### Q3. What is one common mistake?
**Answer:** Schema endpoint loads. Always verify actual output rather than assuming the endpoint is correct.

### Q4. How do you test the implementation?
**Answer:** Test success, validation failure, missing resource and authorization behavior. Inspect status, response body and database state.

### Q5. What evidence should a developer provide?
**Answer:** API request/response examples, documentation, test output and a README with reproducible instructions.

## Scenario questions

### Q6. An API returns 200 but the client still shows incorrect information. What do you inspect?
**Suggested answer:** Check response body, serializer fields, database state, query conditions and automated assertions. Status alone does not prove business correctness.

### Q7. Why document an API if the frontend developer can inspect the code?
**Suggested answer:** Documentation provides a stable contract for clients, including methods, payloads, authentication and expected responses.

## Project viva — Documented REST API

1. What does the project verify?
2. Which endpoints are included?
3. What status codes are expected?
4. Which invalid cases are tested?
5. What is documented in OpenAPI or Postman?
6. Which automated tests were written?
7. What would you improve?

## Rapid revision

- **1.** Install drf-spectacular into the active environment.
- **2.** Add drf_spectacular to INSTALLED_APPS.
- **3.** Configure DEFAULT_SCHEMA_CLASS.
- **4.** Add title, description and version metadata.
- **5.** Add schema, Swagger UI and Redoc URL patterns.
- **6.** Run Django system checks.
- **7.** Open the generated schema and interactive documentation.
- **8.** Inspect an endpoint's methods, parameters, request body and response codes.
- **9.** Keep internal or sensitive endpoints protected from public documentation when required.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the API.
- [ ] Explain error responses.
- [ ] Show documentation or test evidence.
- [ ] Present Documented REST API.
