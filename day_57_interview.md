# Day 57: Interview Questions — Serializer Fields, Validation and Custom Validation Methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 57 class notes](day_57_notes.md)  
**Approved mini-project:** Product Validation API

## Core technical questions

### Q1. Explain serializer fields, validation and custom validation methods.
**Answer:** DRF serializers validate incoming API data before saving it. Field options define required, read-only, write-only and default behavior. validate_<field>() handles one field; validate() handles rules involving multiple fields. Raise serializers.ValidationError with useful messages when data is invalid.

### Q2. Which DRF components or files are involved?
**Answer:** profiles/serializers.py, Serializer validation test. Explain their role in API data handling.

### Q3. What is one common mistake?
**Answer:** Valid SKU is normalized. Always verify the request data and serializer result.

### Q4. How do you test the implementation?
**Answer:** Use valid, invalid and missing-field payloads. Inspect serializer output, validation errors and database state.

### Q5. What should not be exposed in an API?
**Answer:** Password hashes, secret values, internal-only fields and data the client is not authorized to view.

## Scenario questions

### Q6. A client sends invalid data. What should the API do?
**Suggested answer:** Validate the payload, return a clear client error response with structured field errors and avoid saving invalid data.

### Q7. Why use a serializer instead of manually building JSON strings?
**Suggested answer:** A serializer provides structured conversion, field selection, validation and integration with Django models.

## Project viva — Product Validation API

1. Which model does the serializer represent?
2. Which fields are exposed?
3. Which fields are read-only?
4. Which validation rules are implemented?
5. What happens with invalid input?
6. How did you test the serializer?
7. What would you improve for production?

## Rapid revision

- **1.** Add a ModelSerializer for Product.
- **2.** Choose fields and read-only fields explicitly.
- **3.** Create validate_sku() for one-field normalization and checks.
- **4.** Create validate() for rules involving more than one field.
- **5.** Raise serializers.ValidationError with field-specific messages.
- **6.** Call is_valid() before accessing validated_data.
- **7.** Test valid, invalid and missing values.
- **8.** Explain the difference between serializer validation and database constraints.

## Readiness checklist
- [ ] Explain serializer responsibilities.
- [ ] Explain field selection.
- [ ] Demonstrate valid and invalid payloads.
- [ ] Explain error output.
- [ ] Present Product Validation API.
