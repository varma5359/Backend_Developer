# Day 40: Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–40 as relevant; project setup, URL routing, views, templates, models, migrations and forms  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Secure Form Validation Application

> **Trainer standard:** This is an integration lesson. Students must understand the journey from the browser request to the database and back to the browser. Do not let them copy the complete files without tracing each step.

## 1. Learning objectives

1. Write field-specific clean_<field>() validation.
2. Write form-wide clean() validation for related fields.
3. Display field and non-field errors.
4. Explain CSRF protection and preserve secure POST handling.

## 2. Business requirement

Validation checks whether submitted data is acceptable before it is saved. Django performs built-in field validation and lets developers add field-specific and form-wide rules. Error messages should help users correct mistakes. CSRF protection solves a separate security problem: it helps stop an attacker from causing a user's browser to submit an unwanted request using that user's session.

The goal is to make the student registration workflow understandable and reproducible. A junior developer should be able to identify the file responsible for a behavior and debug the flow when it fails.

## 3. Mental model

```text
Browser
  |
  | HTTP request
  v
config/urls.py
  |
  | include()
  v
profiles/urls.py
  |
  | selects a view
  v
profiles/views.py
  |
  +----> profiles/forms.py (bind and validate POST)
  |
  +----> profiles/models.py (ORM)
  |              |
  |              v
  |          Database
  |
  +----> templates (render HTML)
  |
  v
HTTP response / redirect
  |
  v
Browser
```

## 4. Files involved

- `profiles/forms.py`
- `profiles/views.py`
- `profiles/templates/profiles/student_form.html`
- `config/settings.py`

Project structure:

```text
student_portal/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── profiles/
            ├── student_list.html
            └── student_form.html
```

## 5. Prepare the terminal

1. Open the existing Student Portal project.
2. Open VS Code terminal.
3. Activate the .venv environment.
4. Confirm the current directory contains manage.py.
5. Confirm the Django version.

```powershell
Get-Location
python --version
python -m django --version
```

## 6. Commands — run in order

```powershell
python manage.py check
python manage.py runserver
# Submit invalid and valid student registration values.
# Confirm invalid data is not saved.
```

### Understand the steps

### Step 1 — `Add clean_student_code`

Django calls a clean_<fieldname>() method as part of form validation for that field. The method should return the cleaned value or raise ValidationError.

### Step 2 — `Read cleaned_data`

cleaned_data contains values after earlier field-level cleaning. It is not the raw request.POST dictionary.

### Step 3 — `Normalize the code`

strip removes surrounding whitespace. upper converts letters to uppercase. Returning the normalized value means the validated value is used by later form processing.

### Step 4 — `Raise ValidationError`

This tells Django the field is invalid and attaches the message to that field.

### Step 5 — `Add clean()`

clean handles rules that involve more than one field. Call super().clean() to retain the parent form's cleaning behavior.

### Step 6 — `Read values safely`

Use cleaned_data.get because a field may be absent if its own validation failed.

### Step 7 — `Add a field error`

add_error('email', message) associates a cross-field validation error with the email field.

### Step 8 — `Render errors`

form.as_p renders field errors. non_field_errors displays errors that are not attached to one particular field.

### Step 9 — `Keep CSRF protection enabled`

The template token works with CsrfViewMiddleware. Do not remove middleware or turn off CSRF to make a broken form submit.

## 7. Complete implementation

The code is split by filename. Create or update the correct file. Do not paste HTML into Python files.

```python
# profiles/forms.py
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["student_code", "full_name", "email"]

    def clean_student_code(self):
        code = self.cleaned_data["student_code"].strip().upper()
        if not code.startswith("STU"):
            raise forms.ValidationError(
                "Student code must start with STU."
            )
        return code

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name")
        email = cleaned_data.get("email")

        if full_name and email and full_name.casefold() in email.casefold():
            self.add_error(
                "email",
                "Email should not contain the full student name.",
            )
        return cleaned_data

<!-- profiles/templates/profiles/student_form.html -->
<h1>Register Student</h1>
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```

### Read before typing

- Confirm the Student model exists and the database has its migration applied.
- Confirm the form uses exactly the same field names as the model.
- Confirm both URL names are spelled consistently in urls.py, redirect() and template links.
- Preserve existing admin and model code from earlier lessons.

## 8. Detailed request-response explanation

### Field validation order
Django first performs field-level cleaning and built-in validation. If the field is valid, it can call clean_<fieldname>(). It then calls the form-wide clean() method. Invalid fields may be absent from cleaned_data.

### clean_<fieldname>()
The method name must exactly match the field. clean_student_code validates student_code. It should return the normalized value. Raising forms.ValidationError marks the field invalid.

### clean()
Use clean() when a rule depends on more than one field. Always call super().clean() and return cleaned_data. Use .get() because another field may have failed validation.

### ValidationError
ValidationError is a structured Django validation failure. It is different from an unhandled Python exception. Django catches it during form validation and makes the message available to the form.

### Field errors versus non-field errors
Field errors relate to one input. Non-field errors relate to the form as a whole. The template should display both.

### CSRF — what threat is addressed?
A browser may automatically send session cookies to a website. An attacker can try to trick a logged-in browser into submitting an unwanted state-changing request. CSRF tokens help Django verify that a POST form submission originated from a page that received the expected token.

### CSRF is not the same as authentication
- Authentication asks: who is the user?
- Authorization asks: what may this user do?
- CSRF protection asks: is this browser request protected against cross-site request forgery?
- Validation asks: is the submitted data acceptable?
These protections solve different problems and should be used together.

### CSRF configuration
The generated Django project includes CsrfViewMiddleware. Internal POST forms should include {% csrf_token %}. For API clients, CSRF behavior depends on the authentication mechanism; do not blindly disable CSRF for browser/session-authenticated APIs.

### Never trust client-side validation alone
HTML required attributes and JavaScript checks improve user experience but can be bypassed. Repeat validation on the server.

### Troubleshooting
- clean method not called: check method spelling and that form.is_valid() is executed.
- cleaned_data KeyError: use .get() when another field may be invalid.
- CSRF verification failed: check middleware, template token, cookies and request origin.
- Error not visible: render form.as_p and non_field_errors.
- Data saved despite error: check whether save() is called outside the is_valid() branch.

## 9. Verify the application

- [ ] Invalid student code is rejected.
- [ ] Valid code is normalized to uppercase.
- [ ] Cross-field validation attaches the message to email.
- [ ] Invalid form does not save a record.
- [ ] Field errors are visible.
- [ ] CSRF token is included in the POST form.
- [ ] CSRF middleware remains enabled.

Run:

```powershell
python manage.py check
```

Expected output when project configuration is valid:

```text
System check identified no issues (0 silenced).
```

Then test the complete browser flow. A system check does not create student records or prove the form works.

## 10. Common errors and fixes

| Symptom | Likely cause | What to inspect |
|---|---|---|
| NoReverseMatch | URL name mismatch | urlpatterns, redirect name and template url tag |
| TemplateDoesNotExist | Wrong template location | profiles/templates/profiles/ |
| no such table | Migration not applied | showmigrations and migrate |
| Form invalid | Model field validation failed | form.errors and model constraints |
| CSRF verification failed | Token missing or middleware/cookie issue | csrf_token and CSRF middleware |
| Duplicate student code/email | Unique constraint | Existing records and validation messages |
| App route returns 404 | Root include or app pattern missing | config/urls.py and profiles/urls.py |
| Student not shown | Wrong database/query/context | QuerySet, context key and database settings |

### Debugging process

1. Reproduce the issue with a known input.
2. Identify whether it is a URL, view, form, model, template or database problem.
3. Read the traceback or form errors.
4. Check the exact file path and spelling.
5. Run Django checks.
6. Correct one issue at a time.
7. Retest both normal and invalid flows.
8. Verify the saved record in the admin or shell.

## 11. Industry scenario

A training institute registers students through a portal. The office staff need a list of students and a registration form. Invalid information should not be saved. A successful registration should appear in the student directory.

Discuss:
- How does the browser request the list?
- Which view queries the database?
- How does the form validate submitted values?
- What happens if the email is invalid?
- Why is the user redirected after successful registration?
- How can staff verify the record?

## 12. Approved mini-project — Secure Form Validation Application

### Objective
Build the integrated student listing and registration workflow using Django URLs, views, forms, models, templates and the database.

### Ordered tasks

1. Add the field-specific clean_student_code method.
2. Add a form-wide clean method that compares full_name and email.
3. Render both field and non-field errors.
4. Submit a code without STU prefix and observe the field error.
5. Submit a name embedded in the email and observe the cross-field error.
6. Submit a valid student and verify the saved row.
7. Remove the CSRF token only in a local controlled test, observe failure, then restore it immediately.

### Acceptance criteria

- [ ] Invalid student code is rejected.
- [ ] Valid code is normalized to uppercase.
- [ ] Cross-field validation attaches the message to email.
- [ ] Invalid form does not save a record.
- [ ] Field errors are visible.
- [ ] CSRF token is included in the POST form.
- [ ] CSRF middleware remains enabled.

### Submission evidence
- Complete relevant source files.
- Migration status and system check output.
- Screenshot of student list and registration form.
- Evidence of one invalid submission and one valid submission.
- Evidence that the new record exists in the database/admin.
- README with setup and verification steps.
- Short explanation of the GET and POST lifecycles.

### Scope boundary
This lesson integrates list and create behavior. Full update and delete CRUD is taught on Day 42. Do not claim that CRUD is complete here.

## 13. AI-assisted implementation guide

**Planning prompt**
```text
Help me plan Secure Form Validation Application. Break the work into URLs, views, forms,
models and templates. Do not provide the full solution.
```

**Guided implementation prompt**
```text
Guide me through the Student Portal integration one file at a time.
Explain the request flow and wait for my test result after each step.
```

**Debugging prompt**
```text
Here are my URLs, view, form, model fields, browser URL and complete error.
Trace the request flow and identify the smallest broken connection.
Do not rewrite unrelated files.
```

## 14. Daily MCQs

### Q1. Which method validates one specific form field?

A. clean()
B. clean_student_code()
C. save()
D. get_context_data()

**Answer: B.** clean_<fieldname>() is the field-specific validation hook.

### Q2. Why call super().clean()?

A. To start the server
B. To preserve parent form cleaning behavior
C. To disable validation
D. To create a database

**Answer: B.** The parent clean method may contribute cleaned data and should normally be called.

### Q3. What does CSRF protection help prevent?

A. Duplicate database rows
B. Cross-site request forgery
C. Invalid email formats
D. Missing templates

**Answer: B.** CSRF protection helps stop unwanted cross-site state-changing requests made through a user's browser.

### Q4. Where should server-side validation occur?

A. Only in JavaScript
B. In the Django form/model validation on the server
C. Only in CSS
D. Only after saving

**Answer: B.** Client-side checks can be bypassed, so the server must validate submitted data.

### Q5. What should happen if form.is_valid() is False?

A. Save anyway
B. Delete the model
C. Redisplay the bound form with errors
D. Disable CSRF

**Answer: C.** The invalid bound form should be rendered so the user can correct the input.

## 15. Interview preparation

### Q1. Explain the complete request-response flow.
**Answer:** Validation checks whether submitted data is acceptable before it is saved. Django performs built-in field validation and lets developers add field-specific and form-wide rules. Error messages should help users correct mistakes. CSRF protection solves a separate security problem: it helps stop an attacker from causing a user's browser to submit an unwanted request using that user's session.

**Follow-up:** Trace GET /students/ and POST /students/register/ separately.

### Q2. Why separate URLs, views, forms, models and templates?
**Answer:** Each component has a distinct responsibility. URLs select the view, the view coordinates request work, forms validate input, models represent persisted data and templates render the response.

**Follow-up:** Which component would you inspect if a validation error is not displayed?

### Q3. Why redirect after a successful form save?
**Answer:** The Post/Redirect/Get pattern makes the browser issue a fresh GET after the POST and reduces accidental form resubmission on refresh.

**Follow-up:** Does redirect replace server-side validation?

**Answer:** No. Validation must happen before saving. Redirect is a navigation pattern after success.

### Q4. What is not included in this day's project?
**Answer:** Full update and delete CRUD are not included. They are the focus of Day 42.

## 16. Completion checklist

- [ ] I can trace a GET request.
- [ ] I can trace a POST request.
- [ ] I know the responsibility of every involved file.
- [ ] I can explain form validation and saving.
- [ ] I can explain the database query and template context.
- [ ] I tested invalid and valid data.
- [ ] I verified the record in the list and admin.
- [ ] I completed Secure Form Validation Application.
- [ ] I can explain the application without reading the notes.

## 17. Trainer validation

Ask the student to register a new record without following the exact code line by line. Ask them to predict what happens for an invalid email, duplicate code, missing route or missing template. They should locate the relevant component and explain the fix.

**Next phase:** Phase 4 — Day 42: CRUD Operations: Create, Read, Update and Delete.
