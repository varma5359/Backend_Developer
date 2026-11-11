# Day 40: Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–39 — project setup, URL routing, views, templates, models, migrations, ORM, relationships and ModelForms  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Secure Form Validation Application

> **Self-paced method:** Follow the request from the browser to the view, form, model and database, then back to the browser. Create each file exactly where named. Run each check before continuing, and use the expected results to decide whether your implementation is correct.

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

**File 1 — `profiles/forms.py`**. Update the existing StudentRegistrationForm from Day 39.

```python
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

        if full_name and email:
            # Compare a normalized name with the email's local part.
            # Example: "Asha Rao" becomes "asharao"; "asha.rao@example.com"
            # becomes "asharao", so the rule catches common punctuation.
            normalized_name = "".join(full_name.casefold().split())
            email_local_part = email.casefold().split("@", 1)[0]
            normalized_email = (
                email_local_part
                .replace(".", "")
                .replace("_", "")
                .replace("-", "")
            )

            if normalized_name and normalized_name in normalized_email:
                self.add_error(
                    "email",
                    "Email should not contain the full student name.",
                )
        return cleaned_data
```

**File 2 — `profiles/templates/profiles/student_form.html`**. Update the HTML template so both field errors and form-wide errors are visible.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Student Registration</title>
</head>
<body>
    <h1>Register Student</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.non_field_errors }}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
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

## 17. Independent completion test

1. Register a new record without following the exact code line by line.
2. Predict what happens for an invalid email, duplicate code, missing route or missing template.
3. Test one case at a time and compare the result with your prediction.
4. Locate the responsible component and explain the correction.
5. Confirm that invalid data was not saved and valid data appears in the student list.

**Next phase:** Phase 4 — Day 42: CRUD Operations: Create, Read, Update and Delete.

---

# Extended Beginner Lab — Validation, CSRF and Error Handling

## 19. Why validation is necessary

A browser form is not a trusted source.

A user can:
- Remove required attributes.
- Change input values.
- Submit unexpected field names.
- Send a request using a script or API client.
- Submit values that do not appear in the normal page.

The server must validate every submitted value.

## 20. Three different kinds of validation

| Validation | Purpose | Example |
|---|---|---|
| Browser validation | Convenience | required, type=email |
| Django form validation | Validate request data | EmailField rejects invalid email |
| Database constraint | Protect stored data | Unique email, non-negative stock |

Browser validation is useful but can be bypassed.

Django form validation is required for safe request processing.

Database constraints protect critical data rules across different write paths.

## 21. Field validation order

A form field normally performs:
1. Required check.
2. Input conversion.
3. Built-in field validation.
4. Configured validators.
5. Custom clean_fieldname method.

If a field fails validation, Django records an error.

The view should not save an invalid form.

## 22. clean_fieldname()

Example:

~~~python
def clean_full_name(self):
    value = self.cleaned_data["full_name"].strip()

    if len(value) < 3:
        raise forms.ValidationError(
            "Name must contain at least three characters."
        )

    return value
~~~

This method validates one field.

Return the cleaned value when valid.

## 23. Form-wide clean()

Example:

~~~python
def clean(self):
    cleaned_data = super().clean()

    start_date = cleaned_data.get("start_date")
    end_date = cleaned_data.get("end_date")

    if start_date and end_date and start_date > end_date:
        raise forms.ValidationError(
            "Start date must be before end date."
        )

    return cleaned_data
~~~

This validates a relationship between fields.

## 24. Raise ValidationError

ValidationError communicates that a value is invalid.

It can be attached to:
- A field.
- The whole form.
- A model validation method.

Do not return a plain string from a clean method when Django expects a cleaned value or ValidationError.

## 25. Display field errors

~~~django
{{ form.full_name.errors }}
~~~

This displays errors for one field.

## 26. Display non-field errors

~~~django
{{ form.non_field_errors }}
~~~

This displays form-wide errors that do not belong to one field.

## 27. Why keep the bound form?

If a submitted form is invalid, render the same bound form instance.

Correct pattern:

~~~python
if request.method == "POST":
    form = StudentForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("student_list")
else:
    form = StudentForm()

return render(
    request,
    "profiles/student_form.html",
    {"form": form},
)
~~~

If the form is invalid, it still contains the submitted values and errors.

Do not create a fresh empty form after validation fails.

## 28. What is CSRF?

CSRF means Cross-Site Request Forgery.

It is an attack where a browser that is authenticated to a site can be tricked into sending an unwanted request to that site.

Django provides CSRF protection for unsafe browser requests.

## 29. How CSRF protection works at a high level

~~~text
Browser requests form page
        |
        v
Django provides CSRF token
        |
        v
Template includes token in form
        |
        v
Browser submits POST with token
        |
        v
Django CSRF middleware validates request
        |
        +---- Invalid/missing ----> Reject request
        |
        +---- Valid -------------> Continue to view
~~~

This is a simplified description. Django also uses cookie and origin/referrer checks according to its CSRF configuration.

## 30. CSRF token in template

~~~django
<form method="post">
    {% csrf_token %}
    ...
</form>
~~~

The tag generates the hidden token input.

Place it inside the form.

## 31. CSRF middleware

Check config/settings.py for CsrfViewMiddleware.

Do not remove it to solve a form submission problem.

If a POST request fails CSRF validation:
- Check the token tag.
- Check middleware.
- Check cookies.
- Check the request origin.
- Check whether the form is submitted through the expected browser page.

## 32. GET versus POST and CSRF

GET should not change application state.

POST is commonly used for:
- Creating a record.
- Updating a record.
- Deleting a record.
- Applying for a job.
- Adding to a cart.

CSRF protection is important for unsafe methods such as POST.

Do not use GET for a destructive action.

## 33. What is a 403 response?

403 Forbidden means the server refuses the request.

CSRF verification failure commonly results in a forbidden response.

A permission failure can also result in 403.

The reason must be diagnosed from the server logs and request context, not guessed from the status code alone.

## 34. CSRF and API requests

Traditional HTML form submissions include the token through the template tag.

JavaScript requests may need to send the CSRF token in the appropriate header when using session-based authentication.

Django REST Framework has its own authentication and CSRF considerations, which are covered in the API phase.

Do not disable CSRF globally because one JavaScript request is not configured correctly.

## 35. User-facing error messages

Good error:
- Please correct the highlighted fields.
- This email address is already registered.
- The requested record could not be found.

Avoid exposing:
- Database SQL.
- Stack traces.
- Internal paths.
- Secret values.
- Session cookies.
- Password hashes.

## 36. Logging versus displaying errors

A user-facing message should be understandable and safe.

A server log can contain technical details useful to developers, but it must not contain passwords, reset tokens or session secrets.

Use logging with appropriate levels and access controls.

## 37. Common validation and CSRF problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Form accepts invalid value | Missing server-side validator | Add field/form validation |
| Form errors not visible | Template does not render errors | Display field and non-field errors |
| Invalid form becomes blank | New unbound form rendered | Reuse bound form |
| CSRF verification failed | Missing token or middleware/cookie issue | Check token, middleware and request origin |
| POST action triggered by link | State-changing action uses GET | Use POST form |
| Database rejects value | Constraint violated | Validate in form and handle constraint safely |
| Internal error exposed | Exception text displayed | Show safe message and log securely |

## 38. Guided validation exercise

Use a Student form.

Test:
1. Empty required name.
2. Invalid email.
3. Duplicate email.
4. Name with only spaces.
5. Valid submission.
6. Invalid update.
7. POST without CSRF token in a controlled test.
8. POST with valid CSRF token.

For each test, record:
- Submitted value.
- Validation stage.
- Expected message.
- Whether a database write should occur.

## 39. Self-check questions

1. Why is browser validation not enough?
2. What is field-level validation?
3. What does clean_fieldname() do?
4. When should clean() be used?
5. What is ValidationError?
6. Why should a bound form be rendered after invalid POST?
7. What does CSRF stand for?
8. What is the purpose of csrf_token?
9. Why should CSRF middleware not be disabled?
10. Why should GET not delete records?
11. What is the difference between 400 and 403?
12. Why should technical exceptions not be displayed to users?

## 40. Answers

1. Browser checks can be bypassed.
2. Validates one field.
3. Performs custom validation for one field.
4. For cross-field rules.
5. Django's validation exception.
6. It contains submitted values and validation errors.
7. Cross-Site Request Forgery.
8. Adds a token used by Django's CSRF protection.
9. It protects state-changing browser requests.
10. GET should be safe and not mutate application state.
11. 400 means bad request; 403 means access is forbidden.
12. They may reveal internal details or secrets.

## 41. Independent challenge — Safe Student Form

Build a student create/update form that:
- Validates all required fields.
- Checks an email format.
- Displays field errors.
- Uses CSRF token.
- Saves only after is_valid().
- Redirects after success.
- Does not display internal exceptions.

Test both normal and invalid submissions and submit the evidence.

---

# Practice Workbook — Validate and Protect a Student Form

## 42. Build a validation table

Create a table for each form field:

| Field | Required? | Input type | Validation | Error message |
|---|---|---|---|---|
| Full name | Yes | Text | Not only spaces | Enter a valid name |
| Email | Yes | Email | Valid email format | Enter a valid email |
| Phone | Optional | Text | Business-specific | Check phone number |
| Joining date | Yes | Date | Valid date | Enter joining date |

The exact fields depend on the approved Student model.

## 43. Test field validation

For every field, test:
- Missing value.
- Empty string.
- Whitespace-only value.
- Valid value.
- Too-short value.
- Too-long value.
- Incorrect type or format.

Record whether the failure comes from the field definition, validator or custom clean method.

## 44. Test cross-field validation

Example business rule:
- start_date must be before end_date.

Test:
1. Both values missing.
2. Only start_date.
3. Only end_date.
4. Start date earlier.
5. Same date.
6. Start date later.

Decide whether equal dates are allowed and encode that rule deliberately.

## 45. CSRF request flow

A browser form normally receives a CSRF token when the page is rendered.

The POST request must include the expected token and cookie/context.

The CSRF middleware checks the request before the view processes the unsafe operation.

If the check fails, the view should not save the form.

## 46. Test CSRF with Django's test client

Django's test client does not enforce CSRF checks by default in every ordinary test setup.

To test CSRF enforcement, use a client configured with enforce_csrf_checks=True.

Example:

~~~python
from django.test import Client, TestCase


class CsrfProtectionTests(TestCase):
    def test_post_without_csrf_token_is_rejected(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            "/feedback/",
            {"message": "Test message"},
        )

        self.assertEqual(response.status_code, 403)
~~~

The exact URL and payload must match the application.

A second test should load the form page, obtain the CSRF cookie/token through the normal browser flow and submit a valid POST.

## 47. Why CSRF is not authentication

A CSRF token helps protect a browser from unwanted cross-site state-changing requests.

It does not prove that the user has permission to update a record.

The application still needs:
- Authentication.
- Authorization.
- Ownership checks.
- Form validation.

## 48. Why CSRF is not input validation

A valid CSRF token does not make submitted values trustworthy.

A request with a valid token can still contain:
- Invalid email.
- Negative stock.
- Unexpected field values.
- Another user's object ID.

Validate all data on the server.

## 49. Error response decision

Choose the response:
- Invalid form: render form with errors.
- Missing object: 404.
- Authenticated user lacks permission: 403.
- Unsupported HTTP method: 405.
- Unexpected server exception: safe 500 response.

Do not use one generic status code for every failure.

## 50. Security debugging scenario

A learner disables CsrfViewMiddleware because the form receives 403.

This is not a safe fix.

Instead:
1. Confirm the form uses POST.
2. Confirm csrf_token is inside the form.
3. Confirm middleware remains enabled.
4. Confirm browser cookies are accepted.
5. Confirm the form is loaded from the expected host.
6. Inspect the CSRF failure reason in the server log.
7. Fix the actual token/origin issue.

## 51. Validation and CSRF checklist

- [ ] Server-side form validation exists.
- [ ] Cross-field rules are tested.
- [ ] Invalid forms are not saved.
- [ ] Bound form is rendered after failure.
- [ ] POST forms include CSRF token.
- [ ] CsrfViewMiddleware remains enabled.
- [ ] State-changing actions do not use GET.
- [ ] Permission checks remain separate from CSRF.
- [ ] Safe user-facing errors are displayed.
- [ ] Technical details are logged securely.

## 52. Final workbook submission

Submit:
- Field validation table.
- Cross-field test cases.
- CSRF flow diagram.
- CSRF test code.
- Invalid form screenshot.
- Explanation of CSRF versus authentication.
- Explanation of why disabling CSRF is unsafe.

## 53. Final security assessment

Explain why each control is separate:
- CSRF token.
- Authentication.
- Authorization.
- Form validation.
- Database constraints.

For one POST endpoint, demonstrate that a valid CSRF token does not permit an unauthenticated or unauthorized user to perform an action.

The endpoint must still enforce its own authentication, permission and validation rules.

