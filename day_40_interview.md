# Day 40: Interview Guide — Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 40 notes](day_40_notes.md)  
**Mini-project:** Secure Form Validation Application

## 1. Technical questions with model answers

### Q1. What is clean_fieldname() used for?

**Model answer:** It validates or normalizes one field after that field's built-in validation. It should return the cleaned value or raise forms.ValidationError.

### Q2. What is clean() used for?

**Model answer:** It performs validation involving multiple fields. It should call super().clean(), inspect cleaned_data safely and add field or non-field errors.

### Q3. What is cleaned_data?

**Model answer:** It is the dictionary of validated, converted form values available after validation. Only read values that survived field validation.

### Q4. What is the difference between a field error and a non-field error?

**Model answer:** A field error belongs to a specific input and can be shown beside it. A non-field error applies to the form as a whole.

### Q5. What is CSRF protection?

**Model answer:** It helps prevent cross-site request forgery by requiring a valid token for unsafe requests. It is separate from authentication and does not replace authorization.

### Q6. Why is browser-side validation insufficient?

**Model answer:** A client can bypass or alter browser validation. The server must independently validate all submitted data before saving.

## 2. Scenario-based interview question

**Scenario:** A valid form works, but a POST from a page without a CSRF token returns 403. Is that the same as form validation failing?

**Model answer:** No. CSRF middleware rejects the request before normal view/form processing because the request lacks a valid CSRF token. Include {% csrf_token %} inside the POST form and keep CSRF middleware enabled. Then test field validation separately.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Add field-specific and cross-field validation, render field and non-field errors, submit invalid and valid data, and explain the separate purpose of CSRF protection.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Secure Form Validation Application

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Secure Form Validation Application with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. Why is browser validation not enough?
**Answer:** Browser-side checks can be bypassed. Django must validate every submitted value on the server.

### Q6. What is ValidationError?
**Answer:** Django's exception used to communicate validation failures in fields, forms and models.

### Q7. What does CSRF stand for?
**Answer:** Cross-Site Request Forgery.

### Q8. What does csrf_token do?
**Answer:** It adds a token to a browser form that Django uses as part of CSRF request validation.

### Q9. Is CSRF the same as authentication?
**Answer:** No. CSRF protection helps defend against unwanted cross-site requests. Authentication verifies identity.

### Q10. Why should GET not delete a record?
**Answer:** GET should be safe and should not change server state. Use a protected POST request for deletion.

### Q11. Scenario: form POST receives 403.
**Answer:** Check the CSRF token, middleware, browser cookie and request origin. Do not disable CSRF middleware as a shortcut.

### Q12. Scenario: invalid form is saved.
**Answer:** The view is likely saving without checking form.is_valid(). Save only after successful validation.

