# Day 39: Django Forms and ModelForms

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–38 — project setup, URL routing, views, templates, models, migrations, admin, ORM and model relationships  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Student Registration Form

> **Self-paced method:** Follow the request from the browser to the view, form, model and database, then back to the browser. Create each file exactly where named. Run each check before continuing, and use the expected results to decide whether your implementation is correct.

## 1. Learning objectives

1. Explain why browser input must be validated on the server.
2. Distinguish forms.Form from forms.ModelForm.
3. Handle GET and POST requests separately.
4. Bind submitted data, inspect errors and save only valid data.

## 2. Business requirement

A form is not just HTML. A Django form knows which fields are expected, converts submitted strings into Python values and validates those values. A ModelForm connects form fields to a model and can create or update a model instance. The browser displays the form, but the server is responsible for validation and persistence.

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

- `profiles/forms.py (create)`
- `profiles/views.py`
- `profiles/urls.py`
- `profiles/templates/profiles/student_form.html (create)`

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
# Open http://127.0.0.1:8000/students/register/
# GET displays the empty form.
# POST occurs when the form is submitted.
```

### Understand the steps

### Step 1 — `Create profiles/forms.py`

A Django app does not automatically receive a forms.py file. Create it beside models.py and views.py.

### Step 2 — `Import forms and Student`

forms contains Django form classes. Student is the model whose fields will be used by the ModelForm.

### Step 3 — `Create StudentRegistrationForm`

Inheriting from forms.ModelForm tells Django to derive form fields and save behavior from a model.

### Step 4 — `Define the Meta class`

Meta is configuration for this ModelForm. model selects the model; fields is an allowlist of fields that users may submit.

### Step 5 — `Handle GET`

GET displays an unbound empty form. The browser requests the page without submitting form data.

### Step 6 — `Handle POST`

POST binds request.POST to the form. The form now contains submitted data and can validate it.

### Step 7 — `Call is_valid()`

Django runs field cleaning and validation. Only if it returns True should the view call save() or read cleaned_data.

### Step 8 — `Call form.save()`

For this ModelForm, save creates and persists a Student instance, then returns it.

### Step 9 — `Redirect after success`

Post/Redirect/Get avoids resubmitting the same POST if the user refreshes the success page. Redirecting to the same form is a simple checkpoint for this lesson; Day 41 will redirect to the student list.

### Step 10 — `Render the form`

If the form is invalid, the bound form is rendered again and its validation errors are displayed.

## 7. Complete implementation

The code is split by filename. Create or update the correct file. Do not paste HTML into Python files.

**File 1 — `profiles/forms.py`**. Create this Python file beside `models.py` and `views.py`.

```python
from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["student_code", "full_name", "email"]
```

**File 2 — `profiles/views.py`**. Add this view. Keep other views already used by earlier lessons.

```python
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm


def student_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_register")
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "profiles/student_form.html",
        {"form": form},
    )
```

**File 3 — `profiles/urls.py`**. Add this route inside the existing `urlpatterns` list. Do not create a second `urlpatterns` variable.

```python
path("students/register/", views.student_register, name="student_register"),
```

The file must already import `path` and `views`, as shown in the earlier URL-routing lesson.

**File 4 — `profiles/templates/profiles/student_form.html`**. This is an HTML template, not Python. Create the folders if they do not exist.

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

### HTML form versus Django form
HTML provides the browser controls. Django forms provide server-side field definitions, data binding, conversion and validation. A browser can be bypassed, so server-side validation is essential.

### Form versus ModelForm
- `forms.Form`: define form fields manually; use it when the form does not directly map to one model.
- `forms.ModelForm`: derives fields from a model; use it when creating or editing a model record.
Both support validation and cleaned_data.

### Bound and unbound forms
An unbound form has no submitted data and is commonly used for GET. A bound form has submitted data such as request.POST. It can be valid or invalid.

### Meta.model and Meta.fields
model identifies the Django model. fields is an explicit allowlist. Avoid fields="__all__" for public-facing forms because a future model field might become editable unintentionally.

### Why validate before saving?
is_valid() performs field and form validation. Saving before validation can persist incomplete or incorrect information. Use cleaned_data only after the form has validated.

### What does form.as_p do?
It renders each field and associated errors wrapped in paragraph elements. It is a convenient teaching shortcut, not a complete custom design system.

### GET and POST
GET displays the blank form. POST submits the data. A successful POST should usually redirect to avoid browser resubmission. Do not use GET for actions that change data.

### CSRF token
A normal internal POST form includes {% csrf_token %}. This works with Django's CSRF middleware. CSRF is explained in detail on Day 40.

### Duplicate values
If student_code or email is unique, the database prevents duplicate values. The form may also provide helpful validation messages. The database constraint remains the final integrity protection.

### Troubleshooting
- No module named forms: create forms.py in the correct app.
- FieldError: a field listed in Meta.fields does not exist on the model.
- Form invalid: display form.errors and inspect each field.
- Reverse for student_register not found: check URL name and root include.
- IntegrityError: check duplicate unique values and required model fields.

## 9. Verify the application

- [ ] GET displays an empty form.
- [ ] POST binds submitted values.
- [ ] Invalid form does not save a record.
- [ ] Valid form saves a Student row.
- [ ] CSRF token is included in the HTML form.
- [ ] Duplicate unique values are rejected.
- [ ] Successful POST redirects rather than leaving the browser on the POST response.

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

## 12. Approved mini-project — Student Registration Form

### Objective
Build the integrated student listing and registration workflow using Django URLs, views, forms, models, templates and the database.

### Ordered tasks

1. Confirm a Student model exists with student_code, full_name and email fields and that migrations are applied.
2. Create profiles/forms.py and StudentRegistrationForm.
3. Create the student_register view with separate GET and POST branches.
4. Add the URL route and template.
5. Open the registration URL and submit an empty form.
6. Submit valid details and confirm the database row is created.
7. Submit a duplicate student_code or email and inspect the validation behavior.

### Acceptance criteria

- [ ] GET displays an empty form.
- [ ] POST binds submitted values.
- [ ] Invalid form does not save a record.
- [ ] Valid form saves a Student row.
- [ ] CSRF token is included in the HTML form.
- [ ] Duplicate unique values are rejected.
- [ ] Successful POST redirects rather than leaving the browser on the POST response.

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
Help me plan Student Registration Form. Break the work into URLs, views, forms,
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

### Q1. What is a ModelForm?

A. A CSS template
B. A Django form connected to a model
C. A database server
D. A URL converter

**Answer: B.** ModelForm derives fields from a model and can save a model instance.

### Q2. What does a bound form contain?

A. Only default settings
B. Submitted data
C. A database migration
D. A URL pattern

**Answer: B.** A bound form is associated with submitted data such as request.POST.

### Q3. When should form.save() be called?

A. Before validation
B. Only after form.is_valid() returns True
C. On every GET
D. When CSRF is disabled

**Answer: B.** Validation must succeed before saving a ModelForm.

### Q4. What is the common purpose of GET for a registration form?

A. Delete the student
B. Display the blank form
C. Save the record
D. Reset the database

**Answer: B.** GET normally retrieves and displays the form page.

### Q5. Why specify Meta.fields explicitly?

A. To hide every field
B. To control which model fields users can submit
C. To start the server
D. To generate URL routes

**Answer: B.** An explicit allowlist prevents unintended model fields from becoming editable.

## 15. Interview preparation

### Q1. Explain the complete request-response flow.
**Answer:** A form is not just HTML. A Django form knows which fields are expected, converts submitted strings into Python values and validates those values. A ModelForm connects form fields to a model and can create or update a model instance. The browser displays the form, but the server is responsible for validation and persistence.

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
- [ ] I completed Student Registration Form.
- [ ] I can explain the application without reading the notes.

## 17. Trainer validation

Ask the student to register a new record without following the exact code line by line. Ask them to predict what happens for an invalid email, duplicate code, missing route or missing template. They should locate the relevant component and explain the fix.

**Next phase:** Phase 4 — Day 42: CRUD Operations: Create, Read, Update and Delete.
