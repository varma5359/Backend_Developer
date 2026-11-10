# Day 41: Interview Questions — Django Application Integration and Complete Request-Response Flow

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 41 class notes](day_41_notes.md)  
**Approved mini-project:** Django Student Management Website

## 1. Core technical questions

### Q1. Explain django application integration and complete request-response flow.
**Answer:** A complete Django feature connects URL routing, views, models, forms, templates and database operations. Each component has a responsibility. The URL selects a view, the view coordinates work, the form validates input, the model represents stored data and the template renders the response.

### Q2. What is the responsibility of each component?
**Answer:** profiles/urls.py, profiles/views.py, config/urls.py. Explain how the files cooperate to process the request and return a response.

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

## 4. Mini-project viva — Django Student Management Website

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

- **1.** Confirm the profiles app is installed.
- **2.** Confirm Employee model and migrations are ready.
- **3.** Confirm EmployeeForm validates and saves data.
- **4.** Create a list view that queries employees.
- **5.** Create a create view that handles GET and POST.
- **6.** Connect both views using profiles/urls.py.
- **7.** Include profiles.urls in the root URLconf.
- **8.** Create list and form templates.
- **9.** Run system checks and the development server.
- **10.** Create a record, view the list and verify the database/admin result.

## 6. Readiness checklist

- [ ] Explain the form workflow.
- [ ] Explain validation and CSRF.
- [ ] Identify all related files.
- [ ] Demonstrate valid and invalid submissions.
- [ ] Explain how the record is saved.
- [ ] Present Django Student Management Website.
