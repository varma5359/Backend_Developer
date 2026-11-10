# Day 60: Interview Questions — PUT, PATCH and DELETE Operations

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 60 class notes](day_60_notes.md)  
**Approved mini-project:** Complete CRUD REST API

## Core technical questions

### Q1. Explain put, patch and delete operations.
**Answer:** PUT generally replaces the target resource representation. PATCH applies a partial modification. DELETE removes a resource. API behavior should be consistent, permission-protected and explicit about success and missing records. PATCH uses partial=True in serializers so omitted fields are not treated as missing required values.

### Q2. Which DRF decorators or classes are used?
**Answer:** profiles/api_views.py. Explain how the view receives the request and constructs the response.

### Q3. What is a common mistake?
**Answer:** GET returns the selected record. Verify the exact request method, payload and response.

### Q4. How do you test the endpoint?
**Answer:** Use Postman to test valid and invalid payloads, unsupported methods and missing IDs. Inspect status codes and response bodies.

### Q5. Why are status codes important?
**Answer:** They communicate the outcome consistently to API clients and allow clients to handle success and failure.

## Scenario questions

### Q6. A client receives 400 instead of 201. What do you inspect?
**Suggested answer:** Check serializer.errors, request body, Content-Type, required fields and validation rules. Do not bypass validation just to return success.

### Q7. A client sends PATCH with only one field but the serializer complains about other required fields. What do you inspect?
**Suggested answer:** Confirm the view uses partial=True for PATCH and that the serializer instance is passed correctly.

## Project viva — Complete CRUD REST API

1. Which endpoints did you create?
2. Which methods are supported?
3. What payload is required?
4. Which status codes are returned?
5. How are invalid values handled?
6. How did you test a missing record?
7. How are write operations protected?
8. What would you improve next?

## Rapid revision

- **1.** Create a detail endpoint with an integer primary key.
- **2.** Retrieve the object using get_object_or_404().
- **3.** Implement GET to return one serialized record.
- **4.** Implement PUT using a full update payload.
- **5.** Implement PATCH using partial=True.
- **6.** Validate input before saving changes.
- **7.** Implement DELETE and return 204 No Content after success.
- **8.** Test missing IDs and invalid update data.
- **9.** Protect write operations using authentication and permissions when appropriate.

## Readiness checklist
- [ ] Explain the method semantics.
- [ ] Demonstrate each endpoint.
- [ ] Explain status codes.
- [ ] Show invalid payload handling.
- [ ] Present Complete CRUD REST API.
