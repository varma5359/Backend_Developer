# Day 55: Interview Questions — Introduction to REST APIs and Django REST Framework Installation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 55 class notes](day_55_notes.md)  
**Approved mini-project:** REST API Environment Setup

## Core technical questions

### Q1. Explain introduction to rest apis and django rest framework installation.
**Answer:** A REST API exposes resources and operations over HTTP so clients such as browsers, mobile applications and other services can exchange data. Django REST Framework (DRF) adds serializers, API views, authentication, permissions, pagination and browsable API support to Django.

### Q2. Which DRF components or files are involved?
**Answer:** Terminal commands, config/settings.py. Explain their role in API data handling.

### Q3. What is one common mistake?
**Answer:** DRF is installed in the active environment. Always verify the request data and serializer result.

### Q4. How do you test the implementation?
**Answer:** Use valid, invalid and missing-field payloads. Inspect serializer output, validation errors and database state.

### Q5. What should not be exposed in an API?
**Answer:** Password hashes, secret values, internal-only fields and data the client is not authorized to view.

## Scenario questions

### Q6. A client sends invalid data. What should the API do?
**Suggested answer:** Validate the payload, return a clear client error response with structured field errors and avoid saving invalid data.

### Q7. Why use a serializer instead of manually building JSON strings?
**Suggested answer:** A serializer provides structured conversion, field selection, validation and integration with Django models.

## Project viva — REST API Environment Setup

1. Which model does the serializer represent?
2. Which fields are exposed?
3. Which fields are read-only?
4. Which validation rules are implemented?
5. What happens with invalid input?
6. How did you test the serializer?
7. What would you improve for production?

## Rapid revision

- **1.** Explain resource-based API design using an Employee resource.
- **2.** Install djangorestframework into the active virtual environment.
- **3.** Add rest_framework to INSTALLED_APPS.
- **4.** Run python manage.py check.
- **5.** Understand JSON request and response representations.
- **6.** Compare a server-rendered Django page with an API endpoint.
- **7.** Create a short API environment README with package version and setup steps.

## Readiness checklist
- [ ] Explain serializer responsibilities.
- [ ] Explain field selection.
- [ ] Demonstrate valid and invalid payloads.
- [ ] Explain error output.
- [ ] Present REST API Environment Setup.
