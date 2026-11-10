# Day 40: Interview Questions — Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 40 class notes](day_40_notes.md)  
**Approved mini-project:** Secure Form Validation Application

## 1. Core technical questions

### Q1. Explain form validation, csrf protection and error messages.
**Answer:** Validation checks whether submitted data satisfies expected rules before it is accepted. Django forms provide field validation, clean_<field>() methods and a form-wide clean() method. CSRF protection helps prevent an attacker from causing a browser to submit an unwanted request using a user's authenticated session.

### Q2. What is the responsibility of each component?
**Answer:** profiles/forms.py, profiles/templates/profiles/employee_form.html. Explain how the files cooperate to process the request and return a response.

### Q3. Why must a form be validated before saving?
**Answer:** Validation checks submitted values against required field and business rules. Saving invalid data can create incorrect or inconsistent records.

### Q4. What is CSRF protection?
**Answer:** It helps prevent an attacker from causing a browser to submit an unwanted request using a user's authenticated session. Django provides CSRF middleware and template support.

### Q5. How do you verify the feature?
**Answer:** Test GET, invalid POST and valid POST. Inspect errors, redirects and the saved record.

## 2. Scenario-based questions

### Q6. A user submits a form but no record appears. What do you inspect?
**Suggested answer:** Confirm the URL and view, inspect request.method, check form.is_valid(), display form.errors, inspect model constraints and database errors, and verify the redirect.

### Q7. A form works in one browser but fails with CSRF verification. What do you inspect?
**Suggested answer:** Check that the POST form includes {% csrf_token %}, CSRF middleware is enabled and the request is using the expected session/cookie flow.

## 3. Practical discussion

Be prepared to:
- Explain GET versus POST.
- Explain a bound and unbound form.
- Explain cleaned_data and form.errors.
- Explain field-specific and form-wide validation.
- Explain CSRF protection.
- Demonstrate the saved record.

## 4. Mini-project viva — Secure Form Validation Application

1. What is the objective?
2. Which model and form are used?
3. How does the view handle GET?
4. How does the view handle POST?
5. What happens when is_valid() returns False?
6. How are errors displayed?
7. How is CSRF protection included?
8. How do you verify the saved record?
9. What test cases did you run?
10. What would you improve next?

## 5. Rapid revision

- **1.** Add a field-specific clean_employee_code() method.
- **2.** Read the field value from cleaned_data.
- **3.** Normalize the value and check the business rule.
- **4.** Raise forms.ValidationError when the field value is invalid.
- **5.** Use clean() for rules that involve multiple fields.
- **6.** Call super().clean() and return cleaned_data.
- **7.** Keep {% csrf_token %} inside every internal POST form.
- **8.** Submit valid and invalid values and inspect displayed errors.

## 6. Readiness checklist

- [ ] Explain the form workflow.
- [ ] Explain validation and CSRF.
- [ ] Identify all related files.
- [ ] Demonstrate valid and invalid submissions.
- [ ] Explain how the record is saved.
- [ ] Present Secure Form Validation Application.
