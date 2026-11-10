# Day 56: Interview Questions — Serializers and Converting Django Models into JSON

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 56 class notes](day_56_notes.md)  
**Approved mini-project:** Employee Data Serializer

## Core technical questions

### Q1. Explain serializers and converting django models into json.
**Answer:** A serializer converts complex Python objects such as Django model instances into primitive data types that can be rendered as JSON. It can also deserialize incoming data and validate it before creating or updating model instances. ModelSerializer can derive fields and default validation from a Django model.

### Q2. Which DRF components or files are involved?
**Answer:** profiles/serializers.py, Django shell, Serializer usage. Explain their role in API data handling.

### Q3. What is one common mistake?
**Answer:** Serializer imports successfully. Always verify the request data and serializer result.

### Q4. How do you test the implementation?
**Answer:** Use valid, invalid and missing-field payloads. Inspect serializer output, validation errors and database state.

### Q5. What should not be exposed in an API?
**Answer:** Password hashes, secret values, internal-only fields and data the client is not authorized to view.

## Scenario questions

### Q6. A client sends invalid data. What should the API do?
**Suggested answer:** Validate the payload, return a clear client error response with structured field errors and avoid saving invalid data.

### Q7. Why use a serializer instead of manually building JSON strings?
**Suggested answer:** A serializer provides structured conversion, field selection, validation and integration with Django models.

## Project viva — Employee Data Serializer

1. Which model does the serializer represent?
2. Which fields are exposed?
3. Which fields are read-only?
4. Which validation rules are implemented?
5. What happens with invalid input?
6. How did you test the serializer?
7. What would you improve for production?

## Rapid revision

- **1.** Create profiles/serializers.py.
- **2.** Import serializers and the Employee model.
- **3.** Create EmployeeSerializer inheriting from ModelSerializer.
- **4.** Set Meta.model to Employee.
- **5.** Select the API fields explicitly.
- **6.** Mark database-generated ID as read-only.
- **7.** Serialize one model instance and inspect serializer.data.
- **8.** Serialize a queryset using many=True.
- **9.** Explain that serializer.data contains primitive values, not a raw database connection.

## Readiness checklist
- [ ] Explain serializer responsibilities.
- [ ] Explain field selection.
- [ ] Demonstrate valid and invalid payloads.
- [ ] Explain error output.
- [ ] Present Employee Data Serializer.
