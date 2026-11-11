# Day 40: Interview Guide — Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 40 notes](day_40_notes.md)  
**Approved mini-project:** Secure Form Validation Application

## 1. Core technical questions

### Q1. Explain today's topic.
**Answer:** Validation checks whether submitted data is acceptable before it is saved. Django performs built-in field validation and lets developers add field-specific and form-wide rules. Error messages should help users correct mistakes. CSRF protection solves a separate security problem: it helps stop an attacker from causing a user's browser to submit an unwanted request using that user's session.

**Follow-up:** Explain it using the Student Portal.

### Q2. Which files are involved?
**Answer:** `profiles/forms.py`, `profiles/views.py`, `profiles/templates/profiles/student_form.html`, `config/settings.py`. Explain the responsibility of each and how they connect.

**Follow-up:** What happens if one of these components is missing or incorrectly configured?

### Q3. What does Django do automatically, and what does the developer implement?
**Answer:** Django provides URL resolution, request objects, middleware processing, ORM mechanisms, template rendering and response construction. The developer defines the application routes, models, views, form rules, templates and business behavior.

### Q4. How do you verify this feature?
**Answer:** Run the system check, test the browser flow, submit invalid and valid values, inspect the database record and verify the redirect.

## 2. Scenario-based questions

### Q5. The registration form is displayed, but the record is not saved. What do you inspect?
**Suggested answer:** Confirm the request is POST, inspect form.errors, check is_valid(), ensure save() is inside the valid branch, inspect model constraints and database migration state.

### Q6. The save succeeds, but the redirect fails. What do you inspect?
**Suggested answer:** Check that the named route exists, that its name is spelled correctly and that the root URLconf includes the app URLconf.

### Q7. Why should the form not save invalid data?
**Suggested answer:** Invalid data can violate business rules and database constraints. Server-side validation must succeed before persistence.

## 3. Practical coding discussion

Be ready to:
- Trace a GET request to the list view.
- Trace a GET request to the registration form.
- Trace a valid POST request to the database and redirect.
- Trace an invalid POST request to the error display.
- Identify the files involved.
- Verify the saved record in the admin.
- Explain the boundary between this lesson and full CRUD.

## 4. Mini-project viva — Secure Form Validation Application

1. What business problem does it solve?
2. Which routes are implemented?
3. Which view handles each route?
4. Which model and form are used?
5. How does GET differ from POST?
6. How are invalid errors displayed?
7. How is a valid record saved?
8. Why is a redirect used after saving?
9. How did you verify the database record?
10. Which feature is deferred to Day 42?

## 5. Rapid revision

- Browser request enters the root URLconf.
- Root URLconf includes the app URLconf.
- App URL selects the view.
- View uses the form and model.
- ORM interacts with the database.
- Template renders the response.
- Valid POST redirects to the list.
- Invalid POST redisplays the form with errors.

## 6. Interview readiness checklist

- [ ] I can explain the complete request-response lifecycle.
- [ ] I can identify all involved files.
- [ ] I can explain GET and POST separately.
- [ ] I can explain validation before saving.
- [ ] I can verify the database record.
- [ ] I can explain the Post/Redirect/Get pattern.
- [ ] I can present Secure Form Validation Application independently.

**Self-practice:** Ask yourself to trace an actual browser request and locate the exact file for each step. Do not accept a vague answer such as "Django handles it" without explaining which component does what.
