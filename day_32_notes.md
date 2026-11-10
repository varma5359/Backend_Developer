# Day 32: Django Templates, Template Variables and Template Tags

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–29 — Python, OOP, Django installation and project setup  
**Tools:** Existing Django project, profiles app, VS Code and browser  
**Approved mini-project:** Dynamic Employee Profile Website

> **Trainer guidance:** Django is file-oriented. Always tell the learner which file to open, what code to add, which command to run and which URL to test. Never assume the learner knows where a file belongs.

## 1. Learning objectives

- Explain django templates, template variables and template tags.
- Identify the Django file responsible for the behavior.
- Implement the example step by step.
- Understand how the browser request reaches the Python code.
- Verify normal and unmatched or invalid cases.
- Complete Dynamic Employee Profile Website.

## 2. Concept introduction

Templates separate presentation from Python view logic. A view sends a context dictionary to render(). The template reads context values using {{ variable }} and uses template tags such as {% if %} and {% for %} to control presentation.

## 3. Request flow

```text
View prepares context dictionary → render(request, template_path, context) → Django template engine → HTML response → browser
```

The URL configuration and view work together. A route decides which callable should run. The view receives the request, performs the required logic and returns a response.

## 4. File-by-file implementation

Create or open the following files. Keep the folder names and Python import paths exact.

### File: `profiles/views.py`

```python
from django.shortcuts import render

def employee_list(request):
    employees = [
        {"name": "Asha", "department": "Engineering"},
        {"name": "Ravi", "department": "Finance"},
    ]
    return render(
        request,
        "profiles/employee_list.html",
        {"employees": employees}
    )
```

### File: `profiles/templates/profiles/employee_list.html`

```python
<h1>Employee Directory</h1>
<ul>
{% for employee in employees %}
    <li>
        {{ employee.name }} — {{ employee.department }}
    </li>
{% empty %}
    <li>No employees available</li>
{% endfor %}
</ul>
```

## 5. Understand the code

### profiles/views.py

1. `from django.shortcuts import render` — Imports the required Django or local module.
2. ` ` — Part of the example; inspect how it contributes to the complete request flow.
3. `def employee_list(request):` — Defines a view function that Django can call.
4. `    employees = [` — Part of the example; inspect how it contributes to the complete request flow.
5. `        {"name": "Asha", "department": "Engineering"},` — Part of the example; inspect how it contributes to the complete request flow.
6. `        {"name": "Ravi", "department": "Finance"},` — Part of the example; inspect how it contributes to the complete request flow.
7. `    ]` — Part of the example; inspect how it contributes to the complete request flow.
8. `    return render(` — Returns a response or sends data to the next Django component.
9. `        request,` — Part of the example; inspect how it contributes to the complete request flow.
10. `        "profiles/employee_list.html",` — Part of the example; inspect how it contributes to the complete request flow.
11. `        {"employees": employees}` — Part of the example; inspect how it contributes to the complete request flow.
12. `    )` — Part of the example; inspect how it contributes to the complete request flow.

### profiles/templates/profiles/employee_list.html

1. `<h1>Employee Directory</h1>` — Part of the example; inspect how it contributes to the complete request flow.
2. `<ul>` — Part of the example; inspect how it contributes to the complete request flow.
3. `{% for employee in employees %}` — Part of the example; inspect how it contributes to the complete request flow.
4. `    <li>` — Part of the example; inspect how it contributes to the complete request flow.
5. `        {{ employee.name }} — {{ employee.department }}` — Part of the example; inspect how it contributes to the complete request flow.
6. `    </li>` — Part of the example; inspect how it contributes to the complete request flow.
7. `{% empty %}` — Part of the example; inspect how it contributes to the complete request flow.
8. `    <li>No employees available</li>` — Part of the example; inspect how it contributes to the complete request flow.
9. `{% endfor %}` — Part of the example; inspect how it contributes to the complete request flow.
10. `</ul>` — Part of the example; inspect how it contributes to the complete request flow.

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
Employee Directory\nAsha — Engineering\nRavi — Finance
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

## 10. Approved mini-project — Dynamic Employee Profile Website

**Objective:** Dynamic Employee Profile Website.

### Required features

1. Create the template folder inside the profiles app.
2. Create profiles/templates/profiles/employee_list.html.
3. Prepare a list of employee dictionaries in the view.
4. Pass the list through a context dictionary to render().
5. Use {{ }} to display a value.
6. Use {% for %} to loop and {% empty %} for an empty list.
7. Open the route and inspect the rendered HTML in the browser.

### Suggested structure

```text
projects/day_32/
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

- [ ] Template path follows app/templates/app_name/file.html convention.
- [ ] The view passes the expected context key.
- [ ] Template variables display the correct values.
- [ ] The for loop renders every record.
- [ ] The empty branch works when the list has no records.

### Submission evidence

- Updated Django files.
- Terminal output from python manage.py check.
- Browser screenshots for each route.
- README with file paths and run commands.
- Explanation of the request flow.
- One documented troubleshooting case.

## 11. AI-assisted implementation

**Planning prompt:** "Help me plan Dynamic Employee Profile Website. List the exact files, URLs, view functions, template files and test cases. Do not write the complete application."

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

**Q1. Explain django templates, template variables and template tags.**  
**Answer:** Templates separate presentation from Python view logic. A view sends a context dictionary to render(). The template reads context values using {{ variable }} and uses template tags such as {% if %} and {% for %} to control presentation.

**Q2. Describe the request flow for this lesson.**  
**Answer:** View prepares context dictionary → render(request, template_path, context) → Django template engine → HTML response → browser

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
- [ ] Complete Dynamic Employee Profile Website.
- [ ] Test normal and invalid cases.
- [ ] Complete the five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit code, README and evidence.

**Next lesson:** Day 33.
