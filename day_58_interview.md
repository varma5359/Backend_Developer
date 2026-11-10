# Day 58: Interview Questions — Function-Based API Views and APIView

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 58 class notes](day_58_notes.md)  
**Approved mini-project:** Employee REST API

## Core technical questions

### Q1. Explain function-based api views and apiview.
**Answer:** DRF supports function-based API views using @api_view and class-based API views using APIView. These abstractions provide request parsing, response rendering, authentication and permission integration. Choose a style that fits the endpoint and keep business logic understandable.

### Q2. Which DRF decorators or classes are used?
**Answer:** profiles/api_views.py, APIView example, profiles/api_urls.py. Explain how the view receives the request and constructs the response.

### Q3. What is a common mistake?
**Answer:** Endpoint returns JSON. Verify the exact request method, payload and response.

### Q4. How do you test the endpoint?
**Answer:** Use Postman to test valid and invalid payloads, unsupported methods and missing IDs. Inspect status codes and response bodies.

### Q5. Why are status codes important?
**Answer:** They communicate the outcome consistently to API clients and allow clients to handle success and failure.

## Scenario questions

### Q6. A client receives 400 instead of 201. What do you inspect?
**Suggested answer:** Check serializer.errors, request body, Content-Type, required fields and validation rules. Do not bypass validation just to return success.

### Q7. A client sends PATCH with only one field but the serializer complains about other required fields. What do you inspect?
**Suggested answer:** Confirm the view uses partial=True for PATCH and that the serializer instance is passed correctly.

## Project viva — Employee REST API

1. Which endpoints did you create?
2. Which methods are supported?
3. What payload is required?
4. Which status codes are returned?
5. How are invalid values handled?
6. How did you test a missing record?
7. How are write operations protected?
8. What would you improve next?

## Rapid revision

- **1.** Create a separate api_views.py file or organize API views clearly.
- **2.** Create a simple function-based endpoint using @api_view.
- **3.** Return a DRF Response object.
- **4.** Restrict allowed HTTP methods in the decorator.
- **5.** Create a small APIView class with a get() method.
- **6.** Connect the view through an API URL configuration.
- **7.** Open the endpoint in a browser or Postman.
- **8.** Compare the structure of function-based and class-based API views.

## Readiness checklist
- [ ] Explain the method semantics.
- [ ] Demonstrate each endpoint.
- [ ] Explain status codes.
- [ ] Show invalid payload handling.
- [ ] Present Employee REST API.
