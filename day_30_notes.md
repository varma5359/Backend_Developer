# Day 30: URL Routing, Path Converters and URL Patterns

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–29 — Python, OOP, Django installation and project setup  
**Tools:** Existing Django project with profiles app, VS Code and terminal  
**Approved mini-project:** Multi-Page Routing Application

> **Trainer guidance:** Django is file-oriented. Always tell the learner which file to open, what code to add, which command to run and which URL to test. Never assume the learner knows where a file belongs.

## 1. Learning objectives

- Explain url routing, path converters and url patterns.
- Identify the Django file responsible for the behavior.
- Implement the example step by step.
- Understand how the browser request reaches the Python code.
- Verify normal and unmatched or invalid cases.
- Complete Multi-Page Routing Application.

## 2. Concept introduction

URL routing maps an incoming URL path to the view that should handle it. The project's root URL configuration can include the URL configuration of an application. Path converters capture values such as integers and strings from a URL.

## 3. Request flow

```text
Browser requests /profiles/42/ → config/urls.py → profiles/urls.py → selected view → HTTP response
```

The URL configuration and view work together. A route decides which callable should run. The view receives the request, performs the required logic and returns a response.

## 4. File-by-file implementation

Create or open the following files. Keep the folder names and Python import paths exact.

### File: `config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("profiles/", include("profiles.urls")),
]
```

### File: `profiles/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_home, name="profile_home"),
    path("<int:employee_id>/", views.employee_detail, name="employee_detail"),
]
```

### File: `profiles/views.py`

```python
from django.http import HttpResponse

def profile_home(request):
    return HttpResponse("Profiles home")

def employee_detail(request, employee_id):
    return HttpResponse(f"Employee ID: {employee_id}")
```

## 5. Understand the code

### config/urls.py

1. `from django.contrib import admin` — Imports the required Django or local module.
2. `from django.urls import path, include` — Imports the required Django or local module.
3. ` ` — Part of the example; inspect how it contributes to the complete request flow.
4. `urlpatterns = [` — Defines the list of URL patterns.
5. `    path("admin/", admin.site.urls),` — Registers a URL route and connects it to a view.
6. `    path("profiles/", include("profiles.urls")),` — Registers a URL route and connects it to a view.
7. `]` — Part of the example; inspect how it contributes to the complete request flow.

### profiles/urls.py

1. `from django.urls import path` — Imports the required Django or local module.
2. `from . import views` — Imports the required Django or local module.
3. ` ` — Part of the example; inspect how it contributes to the complete request flow.
4. `urlpatterns = [` — Defines the list of URL patterns.
5. `    path("", views.profile_home, name="profile_home"),` — Registers a URL route and connects it to a view.
6. `    path("<int:employee_id>/", views.employee_detail, name="employee_detail"),` — Registers a URL route and connects it to a view.
7. `]` — Part of the example; inspect how it contributes to the complete request flow.

### profiles/views.py

1. `from django.http import HttpResponse` — Imports the required Django or local module.
2. ` ` — Part of the example; inspect how it contributes to the complete request flow.
3. `def profile_home(request):` — Defines a view function that Django can call.
4. `    return HttpResponse("Profiles home")` — Returns a response or sends data to the next Django component.
5. ` ` — Part of the example; inspect how it contributes to the complete request flow.
6. `def employee_detail(request, employee_id):` — Defines a view function that Django can call.
7. `    return HttpResponse(f"Employee ID: {employee_id}")` — Returns a response or sends data to the next Django component.

## 6. Run and verify

1. Activate the virtual environment.
2. Change directory to the folder containing manage.py.
3. Run `python manage.py check`.
4. Start the server using `python manage.py runserver`.
5. Open the route in a browser.
6. Compare the output with the expected result.
7. Test one unmatched or invalid route.
8. Stop the server with Ctrl+C.

### Expected result

```text
/profiles/ → Profiles home\n/profiles/42/ → Employee ID: 42
```

## 7. Important Django concepts

| Concept | Explanation |
|---|---|
| URLconf | Python configuration mapping URL paths to views |
| urlpatterns | List of route definitions |
| path() | Defines a route and optional converters |
| include() | Delegates a URL prefix to another URL configuration |
| View | Callable that handles an HttpRequest and returns a response |
| HttpRequest | Object containing request information |
| HttpResponse | Object representing the response sent to the client |
| render() | Loads a template, combines it with context and returns a response |
| Context | Dictionary of values supplied to a template |
| Template tag | Django template instruction such as if or for |

## 8. Common errors and troubleshooting

| Symptom | Check |
|---|---|
| Page returns 404 | URL prefix, route spelling and include() |
| ImportError for views | Module path and function name |
| View takes unexpected arguments | Path converter name and view parameter |
| View returns None | Ensure every execution path returns a response |
| TemplateDoesNotExist | Template folder and app template path |
| Variable displays blank | Context key and template variable spelling |
| Template syntax error | Matching opening and closing template tags |

Troubleshooting sequence:
1. Confirm the server is running.
2. Check the exact URL.
3. Read the terminal traceback.
4. Check the project's root URLconf.
5. Check the application's URLconf.
6. Check the view name and function signature.
7. Check template path and context keys if rendering.
8. Run the system check again.

## 9. Industry scenario

A company employee portal needs a profile page and employee directory. URLs identify the page or employee. Views prepare the data and choose a response. Templates display the information in browser-friendly HTML.

## 10. Approved mini-project — Multi-Page Routing Application

**Objective:** Multi-Page Routing Application.

### Required features

1. Open config/urls.py and identify urlpatterns.
2. Create profiles/urls.py if it does not exist.
3. Include profiles.urls under the profiles/ prefix in the project URL file.
4. Create profile_home and employee_detail views.
5. Add a path converter for employee_id.
6. Start the server and open both URLs.
7. Try a non-integer value and observe that the int converter does not match.

### Suggested structure

```text
projects/day_30/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── urls.py
    ├── views.py
    └── templates/
        └── profiles/
```

### Validation checklist

- [ ] Root URL configuration includes the application URL file.
- [ ] The home route resolves correctly.
- [ ] The integer path converter passes employee_id to the view.
- [ ] URL names are unique and meaningful.
- [ ] An unmatched path produces the expected 404 response.

### Submission evidence

- Updated Django files.
- Terminal output from python manage.py check.
- Browser screenshots for each route.
- README with file paths and run commands.
- Explanation of the request flow.
- One documented troubleshooting case.

## 11. AI-assisted implementation

**Planning prompt:** "Help me plan Multi-Page Routing Application. List the exact files, URLs, view functions, template files and test cases. Do not write the complete application."

**Guided prompt:** "Help me update only the next file. Explain the path and code, then wait for me to run the server."

**Debugging prompt:** "Here are my URLconf, view, template path and traceback. Trace the request flow and identify the first incorrect link."

**Review prompt:** "Review my routes, view return values and template context. Identify missing cases without rewriting the project."

## 12. Five daily MCQs

**Q1. Which Django component maps a URL to a view?**  
A. URLconf  
B. Database row  
C. Static image  
D. Git branch  
**Answer: A.** URLconf contains URL patterns that select views.

**Q2. What should a view return?**  
A. Any Python variable  
B. An HttpResponse-compatible response  
C. A database table name  
D. A template folder path only  
**Answer: B.** A view must return a response object.

**Q3. What does render() do?**  
A. Deletes the database  
B. Creates a Git commit  
C. Renders a template with context and returns a response  
D. Installs Django  
**Answer: C.** render() combines template and context.

**Q4. What commonly causes TemplateDoesNotExist?**  
A. A wrong template path or missing template file  
B. A Git branch  
C. A browser bookmark  
D. An unused Python variable  
**Answer: A.** Verify the template folder structure and name.

**Q5. Why test an unmatched URL?**  
A. To change the database  
B. To test a missing route and expected 404 behavior  
C. To install a package  
D. To create a model  
**Answer: B.** Unmatched paths should not silently resolve to the wrong page.

## 13. Interview preparation

**Q1. Explain url routing, path converters and url patterns.**  
**Answer:** URL routing maps an incoming URL path to the view that should handle it. The project's root URL configuration can include the URL configuration of an application. Path converters capture values such as integers and strings from a URL.

**Q2. Describe the request flow for this lesson.**  
**Answer:** Browser requests /profiles/42/ → config/urls.py → profiles/urls.py → selected view → HTTP response

**Q3. What is one common error and how would you debug it?**  
**Answer:** Check the URLconf, view, function signature, response or template path according to the error. Read the traceback and verify one link at a time.

**Follow-up:** How would you prove the fix works?  
**Answer:** Run Django's system check, start the server and test both expected and invalid URLs.

## 14. Completion checklist

- [ ] Explain the concept in simple language.
- [ ] Identify every file used in the demonstration.
- [ ] Run the system check.
- [ ] Start the development server.
- [ ] Verify the expected browser output.
- [ ] Complete Multi-Page Routing Application.
- [ ] Test normal and invalid cases.
- [ ] Complete the five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit code, README and evidence.

**Next lesson:** Day 31.
