# Day 41: Django Application Integration and Complete Request-Response Flow

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–40 — Django setup, URLs, views, templates and models  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Django Student Management Website

> **Trainer guidance:** Explain the browser request first, then show the file that handles it. Make students test GET and POST separately. A form should never save data before validation.

## 1. Learning objectives

- Explain django application integration and complete request-response flow.
- Identify the file responsible for each part of the workflow.
- Implement the example step by step.
- Explain the difference between GET and POST handling.
- Validate normal and invalid input.
- Complete Django Student Management Website.

## 2. Concept introduction

A complete Django feature connects URL routing, views, models, forms, templates and database operations. Each component has a responsibility. The URL selects a view, the view coordinates work, the form validates input, the model represents stored data and the template renders the response.

## 3. End-to-end flow

```text
Browser form
   ↓ POST request
Application URL pattern
   ↓
View receives HttpRequest
   ↓
Form binds request.POST
   ↓
form.is_valid()
   ↓
cleaned_data / validation errors
   ↓
ModelForm.save()
   ↓
Database
   ↓
Redirect or rendered response
```

## 4. File-by-file implementation

### File: `profiles/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_create, name="employee_create"),
]
```

### File: `profiles/views.py`

```python
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all().order_by("full_name")
    return render(
        request,
        "profiles/employee_list.html",
        {"employees": employees}
    )

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()

    return render(request, "profiles/employee_form.html", {"form": form})
```

### File: `config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
```

## 5. Understand the important statements

### profiles/urls.py

1. `from django.urls import path` — Imports a Django component or local module.
2. `from . import views` — Imports a Django component or local module.
3. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
4. `urlpatterns = [` — Part of the workflow; explain how it contributes to validation or response rendering.
5. `    path("employees/", views.employee_list, name="employee_list"),` — Connects a URL to a view.
6. `    path("employees/add/", views.employee_create, name="employee_create"),` — Connects a URL to a view.
7. `]` — Part of the workflow; explain how it contributes to validation or response rendering.

### profiles/views.py

1. `from django.shortcuts import render, redirect` — Imports a Django component or local module.
2. `from .models import Employee` — Imports a Django component or local module.
3. `from .forms import EmployeeForm` — Imports a Django component or local module.
4. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
5. `def employee_list(request):` — Defines a view or validation method.
6. `    employees = Employee.objects.all().order_by("full_name")` — Part of the workflow; explain how it contributes to validation or response rendering.
7. `    return render(` — Part of the workflow; explain how it contributes to validation or response rendering.
8. `        request,` — Part of the workflow; explain how it contributes to validation or response rendering.
9. `        "profiles/employee_list.html",` — Part of the workflow; explain how it contributes to validation or response rendering.
10. `        {"employees": employees}` — Part of the workflow; explain how it contributes to validation or response rendering.
11. `    )` — Part of the workflow; explain how it contributes to validation or response rendering.
12. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
13. `def employee_create(request):` — Defines a view or validation method.
14. `    if request.method == "POST":` — Part of the workflow; explain how it contributes to validation or response rendering.
15. `        form = EmployeeForm(request.POST)` — Part of the workflow; explain how it contributes to validation or response rendering.
16. `        if form.is_valid():` — Runs form validation before saving.
17. `            form.save()` — Persists the validated model form.
18. `            return redirect("employee_list")` — Part of the workflow; explain how it contributes to validation or response rendering.
19. `    else:` — Part of the workflow; explain how it contributes to validation or response rendering.
20. `        form = EmployeeForm()` — Part of the workflow; explain how it contributes to validation or response rendering.
21. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
22. `    return render(request, "profiles/employee_form.html", {"form": form})` — Part of the workflow; explain how it contributes to validation or response rendering.

### config/urls.py

1. `from django.contrib import admin` — Imports a Django component or local module.
2. `from django.urls import path, include` — Imports a Django component or local module.
3. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
4. `urlpatterns = [` — Part of the workflow; explain how it contributes to validation or response rendering.
5. `    path("admin/", admin.site.urls),` — Connects a URL to a view.
6. `    path("", include("profiles.urls")),` — Connects a URL to a view.
7. `]` — Part of the workflow; explain how it contributes to validation or response rendering.

## 6. GET and POST

| Method | Typical form behavior |
|---|---|
| GET | Display an empty form or retrieve the page |
| POST | Receive submitted values, validate and save when valid |

Do not use GET to change application state. A successful POST often redirects to a page that displays the saved record. This pattern is known as Post/Redirect/Get.

## 7. Validation and security rules

- Always call form.is_valid() before using cleaned_data or saving a ModelForm.
- Display field errors and non-field errors.
- Keep CSRF protection enabled for internal browser forms.
- Do not trust browser-side validation alone; server-side validation is required.
- Never place passwords or secret keys in form HTML or source code.
- Validate permissions before allowing a user to create or modify protected records.

## 8. Common errors

| Symptom | What to inspect |
|---|---|
| Form does not save | is_valid(), model constraints and database errors |
| CSRF verification failed | csrf_token in the form and CSRF middleware |
| Field not found | ModelForm Meta.fields and model field names |
| Form always invalid | Display form.errors and inspect field validation |
| Duplicate email/code | Unique model constraints and validation feedback |
| View handles only GET | Add correct POST branch |
| Redirect name does not resolve | URL pattern name and namespace |

## 9. Industry scenario

A complete Django feature connects URL routing, views, models, forms, templates and database operations. Each component has a responsibility. The URL selects a view, the view coordinates work, the form validates input, the model represents stored data and the template renders the response.

## 10. Approved mini-project — Django Student Management Website

**Objective:** Django Student Management Website.

### Required tasks

1. Confirm the profiles app is installed.
2. Confirm Employee model and migrations are ready.
3. Confirm EmployeeForm validates and saves data.
4. Create a list view that queries employees.
5. Create a create view that handles GET and POST.
6. Connect both views using profiles/urls.py.
7. Include profiles.urls in the root URLconf.
8. Create list and form templates.
9. Run system checks and the development server.
10. Create a record, view the list and verify the database/admin result.

### Suggested structure

```text
projects/day_41/
├── manage.py
├── config/
└── profiles/
    ├── models.py
    ├── forms.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── profiles/
```

### Validation checklist

- [ ] All components are connected through the correct imports and URLs.
- [ ] GET form displays correctly.
- [ ] Invalid POST displays validation errors.
- [ ] Valid POST saves one record.
- [ ] Successful save redirects to the employee list.
- [ ] The list view displays the saved record.
- [ ] The learner can trace the complete request-response flow.

### Test scenarios

| Scenario | Expected behavior |
|---|---|
| GET form page | Empty form is displayed |
| POST missing required field | Validation error is displayed |
| POST invalid field value | Field-specific error is displayed |
| POST valid values | Record is saved and user is redirected |
| Open list page | Saved record is visible |
| POST without CSRF token | Request is rejected when CSRF protection is enabled |

### Submission evidence

- Source files.
- Browser screenshots of GET and POST behavior.
- Database/admin evidence for a valid saved record.
- Invalid form submission evidence.
- README with exact commands and file paths.
- Short explanation of the request-response flow.

## 11. AI-assisted implementation

**Planning prompt:** "Help me plan Django Student Management Website. Identify the model, form, view, URL and template responsibilities. Give an ordered implementation plan, not the complete code."

**Guided prompt:** "Help me implement the form GET branch first. Explain the code and wait for my browser result before showing the POST branch."

**Debugging prompt:** "Here are my form class, view, template and form.errors output. Find the validation or request handling issue and explain the smallest fix."

**Review prompt:** "Review the workflow for server-side validation, CSRF, redirects, data persistence and clear user feedback."

## 12. Five daily MCQs

**Q1. What should happen before a ModelForm is saved?**  
A. Call form.is_valid().  
B. Delete the model.  
C. Disable CSRF.  
D. Ignore the submitted values.  
**Answer: A.** Validate the bound form before saving.

**Q2. Which method normally displays a blank form?**  
A. DELETE  
B. GET  
C. PATCH  
D. MERGE  
**Answer: B.** GET retrieves the page and displays the form.

**Q3. What does {% csrf_token %} provide?**  
A. A database primary key.  
B. A CSS file.  
C. A CSRF token for a protected form submission.  
D. A URL converter.  
**Answer: C.** It helps Django verify that the POST submission includes the expected token.

**Q4. Where should important server-side validation happen?**  
A. Only in browser JavaScript.  
B. Only in a README.  
C. In a screenshot.  
D. In Django form/model validation.  
**Answer: D.** Client-side checks can be bypassed; validate on the server.

**Q5. Why redirect after a successful POST?**  
A. To avoid accidental duplicate form submission on refresh and show the resulting page.  
B. To disable the database.  
C. To remove validation.  
D. To bypass URL routing.  
**Answer: A.** Post/Redirect/Get is a common browser workflow.

## 13. Interview preparation

**Q1. Explain django application integration and complete request-response flow.**  
**Answer:** A complete Django feature connects URL routing, views, models, forms, templates and database operations. Each component has a responsibility. The URL selects a view, the view coordinates work, the form validates input, the model represents stored data and the template renders the response.

**Q2. Why is is_valid() important?**  
**Answer:** It runs validation and populates cleaned_data or errors. Saving should happen only after the form is valid.

**Q3. What is CSRF protection?**  
**Answer:** It helps protect authenticated browser sessions from unwanted cross-site form submissions.

**Follow-up:** How do you verify a successful submission?  
**Answer:** Check the redirect, displayed list and actual saved database record.

## 14. Completion checklist

- [ ] Explain the form workflow.
- [ ] Identify model, form, view, URL and template files.
- [ ] Test GET and POST.
- [ ] Test invalid and valid data.
- [ ] Verify CSRF behavior.
- [ ] Complete Django Student Management Website.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Phase 3 complete. Next: Phase 4 — Django ORM, Forms and Authentication (Day 42).
