# Day 41: Django Application Integration and Complete Request-Response Flow

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–40 — project setup, URL routing, views, templates, models, migrations, ORM, relationships, ModelForms and validation  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Django Student Management Website

> **Self-paced method:** Follow the request from the browser to the view, form, model and database, then back to the browser. Create each file exactly where named. Run each check before continuing, and use the expected results to decide whether your implementation is correct.

## 1. Learning objectives

1. Connect root URLs, app URLs, views, forms, models and templates.
2. Build a student list and registration workflow.
3. Trace GET and POST requests from browser to database and back.
4. Test valid input, invalid input and persisted records.

## 2. Business requirement

A working Django feature is not one file. It is a connected system. The root URL configuration includes the app URL configuration. The app URL selects a view. The view queries a model or validates a form. The model communicates with the database. A template renders the data and Django returns an HTTP response. When the form is valid, the view saves and redirects.

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

- `config/urls.py`
- `profiles/urls.py`
- `profiles/views.py`
- `profiles/forms.py`
- `profiles/models.py`
- `profiles/templates/profiles/student_list.html`
- `profiles/templates/profiles/student_form.html`

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
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# Visit:
# http://127.0.0.1:8000/students/
# http://127.0.0.1:8000/students/register/
# http://127.0.0.1:8000/admin/
```

### Understand the steps

### Step 1 — `Confirm models and migrations`

Student must have student_code, full_name and email fields. Apply migrations before using the database. The form and view must use the same model fields.

### Step 2 — `Create app URL patterns`

The app router defines student_list and student_register names. Names are used by redirect() and template URL reversing.

### Step 3 — `Include app routes in the root router`

config/urls.py includes profiles.urls at the empty prefix, so /students/ reaches the app router.

### Step 4 — `Implement student_list`

The view queries Student records ordered by full_name and passes the QuerySet to the template.

### Step 5 — `Implement student_register GET`

GET creates an unbound form so the user can see the blank fields.

### Step 6 — `Implement student_register POST`

POST binds request.POST. If is_valid() returns True, the form is saved and the browser is redirected to student_list.

### Step 7 — `Create student_list.html`

The template loops through the students QuerySet and displays a fallback when there are no rows.

### Step 8 — `Create student_form.html`

The template includes the CSRF token, displays errors, renders fields and submits with POST.

### Step 9 — `Run and verify`

Open list, register a student, confirm redirect and confirm the new record appears in the list and admin.

## 7. Complete implementation

The code is split by filename. Create or update the correct file. Do not paste HTML into Python files.

**File 1 — `profiles/urls.py`**. Replace or complete the app's URL patterns with these two routes.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/register/", views.student_register, name="student_register"),
]
```

**File 2 — `profiles/views.py`**. Add or update these views. Keep any unrelated views already used in the project.

```python
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentRegistrationForm


def student_list(request):
    students = Student.objects.order_by("full_name")
    return render(
        request,
        "profiles/student_list.html",
        {"students": students},
    )


def student_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "profiles/student_form.html",
        {"form": form},
    )
```

**File 3 — `config/urls.py`**. The root URL configuration must include the app routes. Preserve the admin route.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
```

**File 4 — `profiles/templates/profiles/student_list.html`**. Create this HTML template.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Student Directory</title>
</head>
<body>
    <h1>Student Directory</h1>
    <a href="{% url 'student_register' %}">Register student</a>
    <ul>
    {% for student in students %}
        <li>{{ student.student_code }} — {{ student.full_name }} — {{ student.email }}</li>
    {% empty %}
        <li>No students registered yet.</li>
    {% endfor %}
    </ul>
</body>
</html>
```

**File 5 — `profiles/templates/profiles/student_form.html`**. Create or update this HTML template.

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
    <a href="{% url 'student_list' %}">Back to student list</a>
</body>
</html>
```

### Read before typing

- Confirm the Student model exists and the database has its migration applied.
- Confirm the form uses exactly the same field names as the model.
- Confirm both URL names are spelled consistently in urls.py, redirect() and template links.
- Preserve existing admin and model code from earlier lessons.

## 8. Detailed request-response explanation

### Complete request lifecycle
When the student opens /students/:
1. Browser sends a GET request.
2. Django applies request middleware.
3. config/urls.py receives URL resolution.
4. include() delegates to profiles.urls.
5. The student_list route selects student_list(request).
6. The view builds a QuerySet from Student.objects.
7. render() loads student_list.html with context.
8. Django returns an HTML HttpResponse.
9. Browser displays the student directory.

### Registration GET lifecycle
1. Browser requests /students/register/.
2. URL resolver selects student_register.
3. request.method is GET.
4. The view creates an unbound StudentRegistrationForm.
5. The template renders the blank form and CSRF token.
6. The browser displays the fields.

### Registration POST lifecycle
1. Browser submits form fields using POST.
2. Django CSRF middleware checks the request.
3. The view creates a bound form from request.POST.
4. is_valid() runs validation.
5. If invalid, the same form is rendered with errors and nothing is saved.
6. If valid, form.save() creates the Student record.
7. redirect("student_list") returns a redirect response.
8. Browser makes a new GET request to /students/.
9. The list view queries the database and displays the new student.

### Why redirect after POST?
This is the Post/Redirect/Get pattern. Refreshing the list page repeats a GET, not the original form POST, reducing accidental duplicate submissions.

### Why not query the database inside the template?
The view should prepare data. The template should render it. Keeping database work out of templates makes responsibilities clearer and testing easier.

### What does Django do automatically?
Django resolves URLs, constructs HttpRequest, runs middleware, loads configured templates, renders template tags, manages ORM queries and creates responses. The developer still defines routes, views, models, form rules, templates and business behavior.

### Scope of this phase assessment
This project demonstrates listing and registering students. Full update and delete operations are Day 42 in Phase 4. Do not add unfinished CRUD actions and claim they are covered by this lesson.

### Data integrity and security
- Keep CSRF middleware enabled and include the token in internal POST forms.
- Validate all data on the server.
- Use model/database unique constraints for identifiers and email.
- Restrict admin and sensitive operations with authentication and permissions.
- Do not expose DEBUG mode or secrets in production.

### Troubleshooting
- NoReverseMatch: check exact URL names student_list and student_register.
- TemplateDoesNotExist: check profiles/templates/profiles/ and spelling.
- Table missing: run migrations and verify database settings.
- Form invalid: display errors and compare form fields with model fields.
- CSRF failure: check token, middleware and browser cookies.
- Duplicate code/email: handle uniqueness validation and database IntegrityError appropriately.

## 9. Verify the application

- [ ] /students/ returns the student directory.
- [ ] Empty database displays the empty-state message.
- [ ] Registration GET displays the form.
- [ ] Invalid POST redisplays errors and does not save.
- [ ] Valid POST saves one Student record.
- [ ] Successful POST redirects to the student list.
- [ ] The new student appears in the list and admin.
- [ ] The learner can trace the complete GET and POST flows.

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

## 12. Approved mini-project — Django Student Management Website

### Objective
Build the integrated student listing and registration workflow using Django URLs, views, forms, models, templates and the database.

### Ordered tasks

1. Confirm Student model has student_code, full_name and email fields; ensure migration is applied.
2. Create or verify StudentRegistrationForm from Day 39 and validation from Day 40.
3. Create student_list view and student_register view.
4. Create profiles/urls.py routes and include them in config/urls.py.
5. Create the student list and form templates.
6. Run check and migrations.
7. Open the empty student list.
8. Open registration, submit invalid values and verify no record is saved.
9. Submit a valid student and verify redirect to list.
10. Verify the same record through Django admin.

### Acceptance criteria

- [ ] /students/ returns the student directory.
- [ ] Empty database displays the empty-state message.
- [ ] Registration GET displays the form.
- [ ] Invalid POST redisplays errors and does not save.
- [ ] Valid POST saves one Student record.
- [ ] Successful POST redirects to the student list.
- [ ] The new student appears in the list and admin.
- [ ] The learner can trace the complete GET and POST flows.

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
Help me plan Django Student Management Website. Break the work into URLs, views, forms,
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

### Q1. What does the root URLconf do in this application?

A. Stores student records
B. Includes the app URLconf and routes admin
C. Renders CSS
D. Validates form fields

**Answer: B.** The root URLconf delegates feature routes to profiles.urls and exposes admin.

### Q2. What happens when a valid registration POST is submitted?

A. The form is ignored
B. The view validates, saves and redirects
C. The database is deleted
D. The browser receives only a print statement

**Answer: B.** A valid ModelForm is saved and the browser is redirected to the list page.

### Q3. What happens when form.is_valid() returns False?

A. The form is saved anyway
B. The view renders the bound form with errors
C. The route is deleted
D. The server restarts

**Answer: B.** Invalid form data is redisplayed so the user can correct it.

### Q4. Why is redirect after successful POST useful?

A. It removes the database
B. It implements Post/Redirect/Get and reduces accidental resubmission
C. It disables validation
D. It hides the model

**Answer: B.** The browser makes a fresh GET after the POST, so refreshing the result page does not repeat the POST.

### Q5. Which topic is explicitly deferred to Phase 4 Day 42?

A. Creating and listing students
B. Full CRUD including update and delete
C. Django URL routing
D. Template variables

**Answer: B.** Day 41 integrates list and create; Day 42 covers complete CRUD operations.

## 15. Interview preparation

### Q1. Explain the complete request-response flow.
**Answer:** A working Django feature is not one file. It is a connected system. The root URL configuration includes the app URL configuration. The app URL selects a view. The view queries a model or validates a form. The model communicates with the database. A template renders the data and Django returns an HTTP response. When the form is valid, the view saves and redirects.

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
- [ ] I completed Django Student Management Website.
- [ ] I can explain the application without reading the notes.

## 17. Independent completion test

1. Register a new record without following the exact code line by line.
2. Predict what happens for an invalid email, duplicate code, missing route or missing template.
3. Test one case at a time and compare the result with your prediction.
4. Locate the responsible component and explain the correction.
5. Confirm that invalid data was not saved and valid data appears in the student list.

**Next phase:** Phase 4 — Day 42: CRUD Operations: Create, Read, Update and Delete.


## 18. Phase 3 cumulative assessment — Django Student Management Website

**Approved assessment:** Django Student Management Website  
**Suggested duration:** 2–3 hours  
**Total:** 100 marks

### Business requirement
A training institute needs a simple website to register students and display a student directory. The application must reject invalid submissions and persist valid student records.

### Required tasks
1. Create the Django project and profiles app using the structure taught in Days 27–28.
2. Configure the app and development settings.
3. Create root and app URL patterns.
4. Implement function-based views for listing and registration.
5. Confirm the Student model introduced on Day 38 and its migration exist; do not create a duplicate model. Apply any new migration only if you intentionally changed the schema.
6. Register the model in Django admin.
7. Use ORM queries to retrieve and order students.
8. Build a ModelForm and server-side validation.
9. Create templates using inheritance and static CSS.
10. Demonstrate GET, invalid POST and valid POST behavior.
11. Verify the saved student in the list and admin.
12. Explain the complete request-response flow.

### Constraints
- Use only concepts introduced by Day 41.
- Keep CSRF protection enabled.
- Do not expose DEBUG=True on a public server.
- Do not hardcode credentials or secrets.
- Full update/delete CRUD belongs to Phase 4 Day 42 and is not required here.

### Evaluation rubric

| Dimension | Marks | Evidence |
|---|---:|---|
| Conceptual understanding | 20 | Explain project/app, routing, views, templates, models, forms and request lifecycle |
| Practical correctness | 30 | Working list and registration workflow; valid record persisted |
| Problem-solving | 20 | Diagnose one controlled URL, template, validation or migration error |
| Code organization | 15 | Correct file responsibilities, readable names and reusable templates |
| Testing and validation | 10 | System check, invalid POST and valid POST evidence |
| Communication and evidence | 5 | README, screenshots/terminal output and clear explanation |
| **Total** | **100** | |

### Phase pass criteria
A learner should not pass only because the project starts. The learner must demonstrate a valid registration, show that invalid input is not saved, locate the files responsible for the workflow and explain the GET and POST lifecycles.

### Interview questions
1. Trace a GET request from the browser to a Django template.
2. Trace a POST request through CSRF middleware, form validation and model save.
3. Explain why migrations are separate from model definitions.
4. Explain ForeignKey, OneToOneField and ManyToManyField with the college example.
5. Explain the difference between authentication, authorization, CSRF and validation.

**Phase 3 completion outcome:** The learner can create a basic Django project, configure an app, route requests, write views, render templates, define models, apply migrations, use the ORM, connect model relationships, validate forms and integrate a basic server-rendered student management workflow.

---

# Extended Beginner Lab — Trace and Validate the Complete Django Request

## 19. Why integration matters

A feature can have a correct model and still fail as a complete user journey.

Examples:
- The model exists but the URL is missing.
- The URL exists but points to the wrong view.
- The view passes the wrong context key.
- The template uses a different field name.
- The form saves but does not redirect.
- The database migration was not applied.
- The page works for an administrator but fails for an ordinary user.

Integration checks the components together.

## 20. The full request-response lifecycle

~~~text
Browser
  |
  | HTTP request
  v
Middleware
  |
  v
URL resolver
  |
  v
View
  |
  +---- Read request values
  |
  +---- Authenticate user
  |
  +---- Check permission/ownership
  |
  +---- Validate form
  |
  v
ORM operation
  |
  v
Database
  |
  v
View prepares context
  |
  v
Template rendering
  |
  v
Middleware response processing
  |
  v
HTTP response
  |
  v
Browser
~~~

This flow is simplified, but it provides a useful mental model for debugging.

## 21. Trace the request URL

For every page, write:
- Browser URL.
- HTTP method.
- Root URL pattern.
- Included app URL pattern.
- View function.
- View parameters.
- Template.
- Expected status code.

This makes it easier to locate a broken connection.

## 22. Trace a GET request

Example: open the student list.

1. Browser sends GET.
2. Django middleware processes the request.
3. URL resolver selects the student-list route.
4. View builds a QuerySet.
5. View passes the QuerySet to the template.
6. Template loops through students.
7. Django returns HTML.
8. Browser displays the page.

No database write should occur during a normal list GET.

## 23. Trace a POST request

Example: create a student.

1. Browser submits the form using POST.
2. CSRF middleware validates the token.
3. URL resolver selects the create view.
4. View binds the form to request.POST.
5. Form validates values.
6. Invalid form is rendered with errors.
7. Valid form is saved.
8. View adds a success message if configured.
9. View redirects to the list or detail page.
10. Browser requests the destination using GET.
11. Template displays the updated result.

## 24. Trace an invalid POST

1. Browser submits invalid data.
2. CSRF validation passes.
3. View binds the form.
4. form.is_valid() returns False.
5. The form contains errors.
6. View renders the same bound form.
7. Template displays the errors.
8. No database write should occur.

This is a successful validation response, not necessarily a server failure.

## 25. Identify which layer owns the bug

| Symptom | First layer to inspect |
|---|---|
| URL returns 404 | URLconf or object lookup |
| NoReverseMatch | URL name and arguments |
| View receives wrong parameter | Path converter and view signature |
| TemplateDoesNotExist | Template path and app registration |
| Variable is blank | View context and template variable |
| Form is invalid | Field names and validation errors |
| CSRF 403 | Token, middleware, cookie and origin |
| Database table missing | Migrations and database configuration |
| Permission denied | User permissions and ownership |
| Page has repeated queries | QuerySet and related-object access |

## 26. System check versus functional test

python manage.py check:
- Checks configuration.
- Finds certain model, URL and settings problems.
- Does not simulate every user journey.

A functional test:
- Sends a request.
- Executes the view.
- Checks response status and content.
- Can verify database changes.

You need both.

## 27. Run the project checks

~~~powershell
python manage.py check
python manage.py showmigrations
python manage.py makemigrations --check --dry-run
~~~

Read each result.

Do not ignore warnings or errors.

## 28. Run app tests

~~~powershell
python manage.py test profiles
~~~

This runs tests in the profiles app.

Run the complete suite:

~~~powershell
python manage.py test
~~~

A test suite should include both successful and failing scenarios.

## 29. Use the Django test client

The Django test client simulates browser requests without starting a real browser.

Example:

~~~python
from django.test import TestCase
from django.urls import reverse

class StudentListTests(TestCase):
    def test_student_list_returns_success(self):
        response = self.client.get(
            reverse("student_list")
        )

        self.assertEqual(response.status_code, 200)
~~~

This assumes the route name exists.

## 30. Test response content

~~~python
self.assertContains(response, "Students")
~~~

This checks that the response includes the expected text.

Use assertions that verify meaningful behavior, not only that a response object exists.

## 31. Test redirects

~~~python
self.assertRedirects(
    response,
    reverse("student_list"),
)
~~~

This checks the redirect destination.

The expected URL must match the actual application flow.

## 32. Test database effects

Before a create request:

~~~python
self.assertEqual(Student.objects.count(), 0)
~~~

After a valid create request:

~~~python
self.assertEqual(Student.objects.count(), 1)
~~~

For invalid form submission, assert that the count remains unchanged.

## 33. Test access control

Test:
- Anonymous visitor.
- Authenticated user.
- User with permission.
- User without permission.
- User accessing their own object.
- User attempting another user's object.

A page that works for a superuser may still be incorrectly configured for ordinary users.

## 34. Test edge cases

Examples:
- Empty database.
- Missing primary key.
- Duplicate unique value.
- Invalid form.
- Unsupported HTTP method.
- Missing optional relationship.
- Empty search result.
- Unauthorized object.
- Invalid page number.

Normal-path-only testing is incomplete.

## 35. Read a traceback

When an error occurs:
1. Read the final exception type and message.
2. Read the traceback from bottom to top.
3. Find the first line in your own project.
4. Open the file and line number.
5. Check imports, names and indentation.
6. Confirm the active environment and current directory.
7. Make one small correction.
8. Run the same failing test again.

Do not randomly rewrite unrelated files.

## 36. Common integration errors

| Error | Likely cause | First check |
|---|---|---|
| NoReverseMatch | Missing/wrong route name | URLconf |
| TemplateDoesNotExist | Incorrect template path | Template folders |
| FieldError | Wrong model field name | Model definition |
| OperationalError: no such table | Migration not applied or wrong DB | showmigrations and settings |
| IntegrityError | Constraint violation | Submitted data and database rule |
| PermissionDenied | Required permission missing | User/group permission |
| CSRF failure | Missing/invalid token | Form and middleware |
| ImportError | Wrong module/class name | Import path |
| AttributeError | Object does not have expected attribute | Model/view context |
| TypeError | Wrong argument or data type | Function signature and submitted values |

## 37. Keep a reproducible debugging record

For every error, record:
- Exact command or URL.
- Current project folder.
- Active Python interpreter.
- Complete traceback.
- Relevant file and code.
- What you expected.
- What happened.
- The smallest change made.
- Result after retesting.

This helps another developer reproduce the issue.

## 38. Final integration exercise

Choose one feature from the Student Portal.

Trace:
1. Model.
2. Migration.
3. URL.
4. View.
5. Form.
6. Template.
7. Database operation.
8. Authentication/permission rule.
9. Expected response.
10. Automated test.

Then intentionally break one small connection in a practice copy and diagnose it.

## 39. Self-check questions

1. What does integration mean?
2. What happens before a view runs?
3. What does the URL resolver do?
4. What does middleware do?
5. What is the difference between GET and POST flow?
6. What should happen after invalid form validation?
7. What does manage.py check prove?
8. Why run tests as well?
9. What does the Django test client do?
10. Why test with ordinary users?
11. How should a traceback be investigated?
12. What is a regression test?

## 40. Answers

1. Connecting all application components into a complete workflow.
2. Middleware processes the request and URL resolution selects a view.
3. It matches a URL pattern to a view.
4. It processes requests and responses around views.
5. GET normally reads; POST submits state-changing data.
6. Render the bound form with errors and do not save.
7. It checks certain configuration issues, not every user journey.
8. Tests verify actual behavior.
9. It simulates HTTP requests to the application.
10. Superusers bypass normal permission restrictions.
11. Read the exception, locate the project line and fix one cause at a time.
12. A test ensuring existing behavior still works after changes.

## 41. Independent challenge — Student Portal Integration Report

Choose one workflow and write a report with:
- User story.
- URL and HTTP method.
- Model fields used.
- Form validation.
- View logic.
- Template output.
- Database effect.
- Security/access rule.
- Test cases.
- Known limitations.

The report must be understandable to a developer who has not seen your code before.

## 42. Final integration handover

Write a handover note for another developer.

Include:
- How to create the environment.
- Which settings must be checked.
- How to run migrations.
- How to start the server.
- Which URL demonstrates the feature.
- How to run tests.
- Which known limitations remain.

A feature is not ready for handover if another developer must guess the setup or expected behavior.


## 43. Final release checklist

- [ ] Setup instructions are complete.
- [ ] Dependencies are pinned.
- [ ] Environment settings are understood.
- [ ] Migrations are committed.
- [ ] System checks pass.
- [ ] Tests pass.
- [ ] Normal workflow is demonstrated.
- [ ] Invalid workflow is demonstrated.
- [ ] Unauthorized workflow is denied.
- [ ] Expected browser result is documented.
- [ ] Known limitations are recorded.
- [ ] Another developer can reproduce the feature.

