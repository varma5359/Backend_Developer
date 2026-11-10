# Day 59: Interview Questions — GET and POST Requests Using Django REST Framework

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 59 class notes](day_59_notes.md)  
**Approved mini-project:** Student Registration API

## Core technical questions

### Q1. Explain get and post requests using django rest framework.
**Answer:** GET retrieves a representation of a resource. POST submits data, commonly to create a new resource. In DRF, request.data parses supported request bodies, serializers validate the payload and Response returns structured data with an appropriate HTTP status code.

### Q2. Which DRF decorators or classes are used?
**Answer:** profiles/api_views.py, profiles/api_urls.py. Explain how the view receives the request and constructs the response.

### Q3. What is a common mistake?
**Answer:** GET returns a JSON list. Verify the exact request method, payload and response.

### Q4. How do you test the endpoint?
**Answer:** Use Postman to test valid and invalid payloads, unsupported methods and missing IDs. Inspect status codes and response bodies.

### Q5. Why are status codes important?
**Answer:** They communicate the outcome consistently to API clients and allow clients to handle success and failure.

## Scenario questions

### Q6. A client receives 400 instead of 201. What do you inspect?
**Suggested answer:** Check serializer.errors, request body, Content-Type, required fields and validation rules. Do not bypass validation just to return success.

### Q7. A client sends PATCH with only one field but the serializer complains about other required fields. What do you inspect?
**Suggested answer:** Confirm the view uses partial=True for PATCH and that the serializer instance is passed correctly.

## Project viva — Student Registration API

1. Which endpoints did you create?
2. Which methods are supported?
3. What payload is required?
4. Which status codes are returned?
5. How are invalid values handled?
6. How did you test a missing record?
7. How are write operations protected?
8. What would you improve next?

## Rapid revision

- **1.** Create a collection endpoint for employees.
- **2.** Implement GET to retrieve all employee records.
- **3.** Serialize the queryset using many=True.
- **4.** Implement POST to read request.data.
- **5.** Pass the payload to EmployeeSerializer(data=...).
- **6.** Call is_valid() before save().
- **7.** Return 201 Created after successful creation.
- **8.** Return 400 Bad Request with serializer.errors for invalid data.
- **9.** Test both methods using Postman.

## Readiness checklist
- [ ] Explain the method semantics.
- [ ] Demonstrate each endpoint.
- [ ] Explain status codes.
- [ ] Show invalid payload handling.
- [ ] Present Student Registration API.
