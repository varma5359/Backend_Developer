# Day 32: Django Templates, Template Variables and Template Tags

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Previous Django lessons; Python, OOP, HTTP and SQL foundations  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment and Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Dynamic Employee Profile Website

> **Teaching rule:** Do not copy a command without understanding it. Use the exact file path, run one step at a time, inspect the output and explain what the framework is doing.

## 1. Learning objectives

1. Explain why templates separate presentation from Python request handling.
2. Pass data from a view to a template using context.
3. Display variables, conditions, loops and filters.
4. Handle missing templates and empty collections.

## 2. Concept introduction — start from zero

A view decides what data is needed. A template describes how that data should appear as HTML. The view passes a context dictionary; Django Template Language (DTL) reads the values and builds the final HTML. This separation means we can change page presentation without placing HTML strings throughout Python view functions.

### Why a backend developer needs this

The Student Portal is being developed as a real, growing application. The code must remain organized and the result must be repeatable. Today's lesson adds one building block to that system. A junior developer should be able to explain the purpose of the component, not only remember its syntax.

## 3. Mental model

```text
Student / Browser
       |
       v
Django project (config)
       |
       v
profiles application
       |
       v
Today's Django component
       |
       +----> optional database / template / response work
       |
       v
Visible result or persisted schema
```

## 4. File map

- `profiles/views.py`
- `profiles/urls.py`
- `profiles/templates/profiles/employee_profile.html`

Project context:

```text
student_portal/
├── .venv/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── profiles/
    └── static/
        └── profiles/
```

Files are introduced gradually. Create a file only when this lesson tells you to.

## 5. Prepare the terminal

1. Open the existing `student_portal` folder in VS Code.
2. Open Terminal → New Terminal.
3. Confirm the current directory contains `manage.py`.
4. Activate the same virtual environment created earlier.
5. Confirm the interpreter and Django version.

```powershell
Get-Location
python --version
python -m django --version
```

If the current folder does not contain manage.py, move to the project root. Do not create a second project to avoid a path mistake.

## 6. Commands — exact order

```powershell
# Create this folder if it does not exist:
# profiles/templates/profiles/

python manage.py check
python manage.py runserver
# Open http://127.0.0.1:8000/employee/
```

### Understand every command

### Step 1 — `Create the template folder`

Django's app template discovery expects the folder structure profiles/templates/profiles/. The second profiles folder namespaces the template and avoids collisions with templates in other apps.

### Step 2 — `Import render`

render is a shortcut that loads a template, renders it with context and returns an HttpResponse.

### Step 3 — `Create the employee dictionary`

This is sample Python data. Later, the same values can come from a database model.

### Step 4 — `Create context`

The dictionary key employee becomes a variable name in the template. Its value is the employee dictionary.

### Step 5 — `Call render`

The first argument is the request, the second is the template path, and the third is context. Django returns the rendered HTML as a response.

### Step 6 — `Use {{ employee.name }}`

Double curly braces output a variable value. DTL dot lookup can access dictionary keys and object attributes.

### Step 7 — `Use the if tag`

The if/else/endif tags choose which HTML fragment is rendered based on a condition.

### Step 8 — `Use the for tag`

The for/endfor tags repeat HTML for each skill. The empty branch displays a fallback when the list has no items.

### Step 9 — `Use the upper filter`

A filter transforms display output. It does not change the original Python list value.

## 7. Implementation — correct files

### Code demonstration

The code below may contain Python, HTML or CSS sections. Use the filename comments to put each section into the correct file. Never paste HTML into a .py file.

```python
# profiles/views.py
from django.shortcuts import render

def employee_profile(request):
    employee = {
        "name": "Asha",
        "department": "Data Science",
        "active": True,
        "skills": ["Python", "Django", "SQL"],
    }
    context = {"employee": employee}
    return render(request, "profiles/employee_profile.html", context)

# Add to profiles/urls.py urlpatterns:
path("employee/", views.employee_profile, name="employee_profile")

<!-- profiles/templates/profiles/employee_profile.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Employee Profile</title>
</head>
<body>
    <h1>{{ employee.name }}</h1>
    <p>Department: {{ employee.department }}</p>
    {% if employee.active %}
        <p>Status: Active</p>
    {% else %}
        <p>Status: Inactive</p>
    {% endif %}
    <h2>Skills</h2>
    <ul>
    {% for skill in employee.skills %}
        <li>{{ skill|upper }}</li>
    {% empty %}
        <li>No skills recorded.</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### Before saving

1. Read the existing file.
2. Preserve working code from earlier days.
3. Add the new code at the correct location.
4. Check spelling and indentation.
5. Save the file.
6. Run the relevant Django command.
7. Inspect terminal output before opening the browser.

## 8. Detailed explanation

### What is a template?
A template is usually an HTML file containing HTML plus Django Template Language. It controls presentation, not the database schema or request routing.

### Context dictionary
The view creates a dictionary and passes it to render. If the context is `{"employee": employee}`, the template can access `employee`. If the key is misspelled, the expected value will not appear.

### Variable syntax
`{{ employee.name }}` asks DTL to resolve the name value from employee. DTL dot lookup works with dictionary keys, object attributes and list indices in its supported lookup rules.

### Template tags
Tags use `{% ... %}`. Common tags include if, for, url, extends, include, csrf_token and load. Tags control template behavior rather than simply outputting a value.

### Filters
Filters use the pipe syntax, for example `{{ employee.name|upper }}`. Filters transform the displayed value. Common filters include lower, title, date, default and length.

### Empty loops
`{% empty %}` runs when a for-loop collection has no items. It is useful for empty search results and new applications.

### Autoescaping and security
Django autoescapes ordinary variable output by default. Do not apply the safe filter to untrusted user content. Template escaping helps prevent HTML injection, but it is not a replacement for validation, authorization or safe JavaScript handling.

### Keep logic in the right place
Use Python views and model/service code for business rules. Use templates for presentation and simple display decisions. Avoid complex calculations and database queries inside templates.

### TemplateDoesNotExist
Check spelling, folder names, file extension, app registration and TEMPLATES APP_DIRS setting. The correct path for this example is profiles/templates/profiles/employee_profile.html.

### Templates are not static files
A template is processed by Django and can contain context variables. A static HTML file is served as-is and does not automatically receive Django context.

## 9. Execution trace

Explain these questions aloud:
1. What is the input or requested operation?
2. Which file or command handles it?
3. What does Django do automatically?
4. What did the developer implement?
5. What result should be produced?
6. How do we prove that result is correct?

## 10. Verification checklist

- [ ] Template loads without TemplateDoesNotExist.
- [ ] Asha and Data Science appear.
- [ ] The active branch appears for True and inactive branch for False.
- [ ] Each skill is rendered as an uppercase list item.
- [ ] The empty message appears for an empty list.
- [ ] The learner explains the view-to-context-to-template flow.

Run the general project check:

```powershell
python manage.py check
```

Expected when project configuration is valid:

```text
System check identified no issues (0 silenced).
```

The system check does not prove every browser interaction or database operation. Perform the specific checks above.

## 11. Troubleshooting

| Symptom | Likely cause | Diagnostic |
|---|---|---|
| manage.py not found | Wrong directory | Get-Location and locate manage.py |
| No module named django | Wrong environment | Check sys.executable and Django version |
| App not loaded | Missing app registration | Inspect INSTALLED_APPS |
| Template not found | Incorrect folder/file path | Check app/templates/app_name/ |
| Route returns 404 | URL pattern missing or order issue | Inspect root and app URLconf |
| Database table missing | Migration not applied | Run showmigrations and migrate |
| CSS missing | Incorrect static path | Inspect browser Network tab |
| SyntaxError | Incorrect Python syntax | Read traceback file and line |

### Safe debugging process
1. Reproduce the problem.
2. Read the complete error.
3. Locate the first relevant line in your own code.
4. Confirm the correct Python environment and project folder.
5. Check the filename, imports, spelling and configuration.
6. Change one thing at a time.
7. Rerun the appropriate check.
8. Verify the actual behavior again.

## 12. Industry scenario

A training institute needs to maintain a Student Portal. A backend developer must make the application easy to extend and debug. Today's concept is useful because it gives a predictable way to organize or operate one part of the system.

Discuss:
- What problem does the user face?
- Which component is responsible?
- What information enters the feature?
- What result should the user or developer observe?
- What failure case should be tested?

## 13. Approved mini-project — Dynamic Employee Profile Website

### Objective
Build a working demonstration of today's approved concept in the existing Student Portal.

### Ordered tasks

1. Create the view and route.
2. Create the template at the exact path.
3. Open /employee/ and confirm the name, department and status.
4. Change active to False and observe the conditional branch.
5. Change skills to an empty list and observe the empty message.
6. Add a new skill and confirm the loop displays it.

### Acceptance checks

- [ ] Template loads without TemplateDoesNotExist.
- [ ] Asha and Data Science appear.
- [ ] The active branch appears for True and inactive branch for False.
- [ ] Each skill is rendered as an uppercase list item.
- [ ] The empty message appears for an empty list.
- [ ] The learner explains the view-to-context-to-template flow.

### Submission evidence
- Relevant source files.
- Terminal output from checks and commands.
- Browser screenshot or database evidence, where relevant.
- README with setup and verification steps.
- Short explanation of one error and its correction.

### Optional extension
Make one small change, predict its result, run it and explain the difference.

## 14. AI-assisted implementation

First attempt each step using the lesson. If you are still stuck, use an optional AI learning assistant for hints and explanations; do not ask it to hide the implementation from you.

**Planning prompt**
```text
I am a beginner. Help me plan Dynamic Employee Profile Website.
Give me ordered tasks and checkpoints. Do not give me the complete solution.
```

**Guided implementation prompt**
```text
Guide me one file and one step at a time. Explain the command,
the code and the expected output. Wait for my result before continuing.
```

**Debugging prompt**
```text
Here is my exact command, current directory, relevant file and full error.
Explain the likely cause and the smallest safe fix. Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Q1. What does render() return?

A. A database table
B. A rendered HTTP response
C. A URL pattern
D. A Python list

**Answer: B.** render combines a template and context and returns an HttpResponse.

### Q2. Which syntax outputs a context variable?

A. {% employee %}
B. [[employee]]
C. {{ employee }}
D. (employee)

**Answer: C.** Double curly braces are used to output template variables.

### Q3. Which tag repeats markup for each item?

A. {% for %}
B. {% csrf_token %}
C. {% extends %}
D. {% load %}

**Answer: A.** for/endfor iterates over a collection.

### Q4. What does the upper filter do?

A. Changes the database field
B. Converts displayed text to uppercase
C. Creates a new model
D. Validates a password

**Answer: B.** The filter transforms the display value in the rendered template.

### Q5. What should you do if TemplateDoesNotExist occurs?

A. Disable template loading
B. Check app registration and exact template path
C. Delete settings.py
D. Use print instead of render

**Answer: B.** Django must be able to discover the template in the configured template directories.

## 16. Interview preparation

### Q1. Explain today's topic in simple words.
**Answer:** A view decides what data is needed. A template describes how that data should appear as HTML. The view passes a context dictionary; Django Template Language (DTL) reads the values and builds the final HTML. This separation means we can change page presentation without placing HTML strings throughout Python view functions.

**Follow-up:** Give an example from the Student Portal.

### Q2. Which files or commands are important?
**Answer:** `profiles/views.py`, `profiles/urls.py`, `profiles/templates/profiles/employee_profile.html`. Explain the responsibility of each.

**Follow-up:** What would you inspect if the expected behavior did not appear?

### Q3. How do you verify the implementation?
**Answer:** Run the commands, inspect output and verify the browser or database behavior. Explain the edge case you tested.

**Follow-up:** Does a successful system check guarantee that every feature works?

**Answer:** No. It checks selected project configuration and framework conditions. Feature behavior needs direct testing.

### Q4. What is a common beginner mistake?
**Answer:** Running commands from the wrong folder, editing the wrong file or assuming code works without verification. Read the error and isolate the cause.

## 17. Completion checklist

- [ ] I can explain today's concept without reading.
- [ ] I know the exact file paths.
- [ ] I can explain the important code.
- [ ] I ran the required commands.
- [ ] The Django system check passes.
- [ ] I verified the expected behavior.
- [ ] I tested an edge case.
- [ ] I completed Dynamic Employee Profile Website.
- [ ] I submitted reproducible evidence.
- [ ] I can answer the interview questions.

## 18. Independent completion test

Do not mark the day complete merely because a file contains code. Complete every check yourself:
1. Demonstrate the result in the browser or terminal.
2. Explain the execution flow without reading the notes.
3. Modify one small part independently and predict the result before running it.
4. Compare the actual result with your prediction.
5. Diagnose and fix one controlled mistake, such as a misspelled variable, template path or setting.

**Next lesson:** Day 33 — Template Inheritance, Reusable Components and Static Files

---

# Extended Beginner Lab — Templates, Context and Safe Rendering

## 19. What is a template?

A Django template is a text file that describes the structure of a response, commonly HTML.

The view prepares data. The template decides how to display that data.

This separation helps keep request handling in views, data structure in models and presentation in templates.

## 20. Understand template variables

Example:

~~~django
<h1>Welcome, {{ student_name }}</h1>
~~~

The double curly braces display a value from template context.

If the view passes student_name with the value Asha, the browser receives HTML containing the rendered name.

If the context key is missing, Django normally renders an empty value rather than raising a Python NameError.

## 21. Understand template filters

A filter transforms a value for display.

Example:

~~~django
{{ student_name|upper }}
~~~

This displays the value in uppercase.

Other useful filters:
- lower.
- title.
- length.
- default.
- date.
- truncatewords.
- join.
- floatformat.

A filter changes presentation. It does not normally update the database value.

## 22. Understand the default filter

~~~django
{{ student_name|default:"Guest" }}
~~~

If the value is empty or false-like, the template displays Guest.

Use a default when an optional value may be absent.

Do not use a default to hide a missing required database value without understanding why it is missing.

## 23. Understand loops

~~~django
{% for student in students %}
    <p>{{ student.name }}</p>
{% empty %}
    <p>No students found.</p>
{% endfor %}
~~~

for repeats the block for each item.

empty displays when the collection has no items.

This is useful for lists from a QuerySet.

## 24. Understand conditions

~~~django
{% if student.is_active %}
    <span>Active</span>
{% else %}
    <span>Inactive</span>
{% endif %}
~~~

A template condition controls display.

It is not a replacement for backend authorization. Hiding a button does not protect the view.

## 25. Understand the with tag

The with tag assigns a value to a temporary template variable.

~~~django
{% with full_name=student.first_name|add:" "|add:student.last_name %}
    <p>{{ full_name }}</p>
{% endwith %}
~~~

Use it for a small presentation expression. Complex business logic belongs in Python.

## 26. Understand URL tag

~~~django
<a href="{% url 'student_detail' student.id %}">
    View student
</a>
~~~

The url tag reverses a named URL.

If the route name or required argument is wrong, Django raises NoReverseMatch during rendering.

## 27. Understand static tag

~~~django
{% load static %}
<link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">
~~~

The static tag generates the correct URL for a static file.

The path is relative to configured static-file locations.

## 28. Understand CSRF tag

~~~django
<form method="post">
    {% csrf_token %}
    ...
</form>
~~~

The CSRF tag inserts a hidden token used by Django's CSRF protection.

Use it in internal POST forms.

## 29. Autoescaping

Django templates automatically escape many variable values in HTML contexts.

This helps prevent untrusted text from being interpreted as HTML or script.

If a user submits a name containing HTML tags, Django generally renders the characters safely rather than executing them as markup.

Do not disable autoescaping casually.

## 30. The safe filter

~~~django
{{ trusted_html|safe }}
~~~

The safe filter marks a value as safe HTML.

Use it only when the HTML is trusted and has been safely prepared.

Never apply safe to arbitrary user-submitted text. It can create cross-site scripting vulnerabilities.

## 31. Template inheritance

A base template can define reusable layout blocks.

A child template uses extends and fills the blocks.

This avoids copying the same header, navigation and footer into every page.

## 32. Include reusable template fragments

The include tag renders another template fragment.

Example:

~~~django
{% include "profiles/_student_card.html" %}
~~~

Use includes for reusable presentation fragments.

Do not use template includes as a substitute for Python function reuse.

## 33. Context data versus template logic

Good template responsibilities:
- Display a name.
- Loop over records.
- Show an empty-state message.
- Display a link.
- Show a simple condition.

Responsibilities better kept in the view/model:
- Complex database queries.
- Permission calculations.
- Financial totals.
- Multi-step business rules.
- Data transformations that need unit tests.

## 34. Common template mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Variable appears blank | Context key missing or misspelled | Inspect view context |
| NoReverseMatch | URL name or argument incorrect | Check URLconf |
| TemplateDoesNotExist | Wrong template path | Check app/templates/app |
| CSS not loaded | Static path or static tag wrong | Inspect static file URL |
| User text becomes HTML | Unsafe rendering | Keep autoescaping enabled |
| Loop displays nothing | QuerySet is empty or wrong context | Inspect view result |
| Include fails | Wrong include path | Check app template namespace |
| Block does not render | Child block name differs | Compare base and child block names |

## 35. Guided template exercise

Create a student list template that:
1. Displays a heading.
2. Shows each student's name.
3. Shows a link to the detail route.
4. Displays Active or Inactive.
5. Shows an empty message.
6. Uses a shared base template.
7. Loads a CSS file through the static tag.

Explain every template tag used.

## 36. Self-check questions

1. What does a template variable do?
2. What does a template filter do?
3. What is the purpose of empty?
4. What does extends do?
5. What does include do?
6. Why use the url tag?
7. Why use the static tag?
8. What does csrf_token do?
9. What is autoescaping?
10. Why is safe dangerous for user input?

## 37. Answers

1. Displays a context value.
2. Transforms a value for presentation.
3. Displays content when a loop has no items.
4. Inherits a base template.
5. Renders another template fragment.
6. Generates a URL from a route name.
7. Generates a URL for a static asset.
8. Adds a CSRF token to a form.
9. Escapes unsafe characters in HTML output.
10. It can cause untrusted content to be interpreted as HTML or script.

## 38. Independent challenge — Student Directory Page

Build a directory page with:
- Base layout.
- Student heading.
- Student loop.
- Empty state.
- Detail links.
- Active status.
- CSS file.
- Safe rendering of student-entered text.

Test with at least two records, no records, and a student name containing characters such as angle brackets.

Record what the browser displays and explain why autoescaping matters.

---

# Deep Practice Workbook — Build and Review a Template Page

## 39. Start with a user story

A student opens the institute portal and wants to see:
- A page title.
- A welcome message.
- A list of courses.
- A link to each course.
- A message when no courses are available.

The view should retrieve the data. The template should display it.

## 40. Example view

~~~python
from django.shortcuts import render
from .models import Course


def course_list(request):
    courses = Course.objects.filter(
        is_active=True
    ).order_by("title")

    context = {
        "page_title": "Available Courses",
        "courses": courses,
    }

    return render(
        request,
        "profiles/course_list.html",
        context,
    )
~~~

This example assumes the Course model has title and is_active fields. Confirm the actual model field names before using it.

## 41. Example template

~~~django
{% extends "profiles/base.html" %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
    <h2>{{ page_title }}</h2>

    <p>Choose a course to view its details.</p>

    {% for course in courses %}
        <article>
            <h3>{{ course.title }}</h3>
        </article>
    {% empty %}
        <p>No active courses are available.</p>
    {% endfor %}
{% endblock %}
~~~

## 42. Trace the data

- Course.objects.filter() builds the QuerySet.
- order_by() defines the display order.
- context connects the Python variable to the template variable.
- render() loads the template and returns an HttpResponse.
- The for tag iterates through the courses.
- empty displays when the QuerySet has no rows.

## 43. Template variable practice

For each context dictionary, write the template expression.

| Context key | Value | Template expression |
|---|---|---|
| student_name | Asha |  |
| total_students | 25 |  |
| course_title | Django |  |
| is_active | True |  |

Expected expressions:
- student_name.
- total_students.
- course_title.
- is_active.

## 44. Filter practice

Predict the result:

~~~django
{{ "django"|upper }}
{{ "DJANGO"|lower }}
{{ student_name|default:"Guest" }}
{{ description|truncatewords:5 }}
~~~

Explain:
- Which filter changes case?
- Which filter supplies a fallback?
- Which filter shortens displayed text?

## 45. Loop practice

Given three course records, write a loop that displays:
- Course title.
- Course duration.
- Course detail link.

Then write an empty block.

Test the template with:
- Three courses.
- One course.
- No courses.

## 46. Condition practice

Display Active when course.is_active is true.

Display Inactive otherwise.

Explain why this is a presentation decision and not a permission check.

## 47. URL tag practice

Create a detail link using the named route.

The route should accept a course identifier.

Confirm:
- The route name exists.
- The view parameter name matches the converter.
- The template supplies the required value.

If the URL tag raises NoReverseMatch, inspect the URL configuration before changing the template.

## 48. Static tag practice

Add a CSS file using the static tag.

Verify:
1. The static folder is inside the app.
2. The path contains the app namespace.
3. The static library is loaded.
4. The browser requests the expected URL.
5. The response is successful.

## 49. Security review

For every user-provided value displayed in the template:
- Keep autoescaping enabled.
- Do not apply safe to untrusted content.
- Do not display passwords.
- Do not display session identifiers.
- Do not display secret values.
- Avoid exposing private information unnecessarily.

## 50. Accessibility review

A usable template should:
- Use semantic headings in order.
- Use labels for form inputs.
- Use meaningful link text.
- Provide visible error messages.
- Not rely on color alone.
- Provide alternative text for meaningful images.

## 51. Template debugging exercise

Break one item at a time in a practice copy:
1. Misspell a context variable.
2. Misspell a route name.
3. Change a block name.
4. Change the template path.
5. Remove the static library load tag.
6. Remove a required template include.

For each error:
- Record the symptom.
- Identify the file.
- Explain the cause.
- Apply the smallest correction.
- Test again.

## 52. Knowledge check

1. Why does a view pass context?
2. What is the difference between a variable and a filter?
3. Why use empty in a loop?
4. What does extends do?
5. What does include do?
6. What is the purpose of autoescaping?
7. Why should safe be used cautiously?
8. Why use named URLs?
9. Why use the static tag?
10. Why should a template not decide authorization?

## 53. Answers

1. To make Python values available to the template.
2. A variable displays data; a filter transforms it for presentation.
3. To show a message when the collection has no items.
4. To inherit a base template.
5. To render a reusable fragment.
6. To prevent untrusted text being interpreted as HTML.
7. It marks content as safe and can allow script injection.
8. To avoid hard-coded paths and support route changes.
9. To generate a static asset URL.
10. Because users can request backend URLs directly.

## 54. Final template review

Before marking the lesson complete:
- Confirm the view returns render().
- Confirm the template path.
- Confirm context names.
- Confirm loop and empty behavior.
- Confirm named routes.
- Confirm static files.
- Confirm autoescaping.
- Confirm the page works with zero records.
- Confirm no sensitive data is exposed.

## 55. Final independent template assessment

Build a template with one heading, one paragraph, one list, one empty state and one named link.

Explain the data flow from view context to rendered HTML.

Test:
1. Missing optional value.
2. Empty QuerySet.
3. Text containing angle brackets.
4. Incorrect route name.
5. Missing static file.

For each case, record the visible result and the file that needs correction.

Do not solve a template error by moving complex database logic into HTML.


## 56. Template review rubric

Rate the page against these checks:
- Correct base template.
- Correct child block names.
- Correct context variable names.
- Correct empty-state behavior.
- Correct route names.
- Correct static paths.
- Safe rendering of user text.
- Useful heading structure.
- Accessible form labels.
- Clear error presentation.
- No passwords or tokens in the HTML.
- No complex database queries in the template.

Fix every failed check before submission.


## 57. Explain-back assessment

Without reading the notes, explain:
1. How a view passes data to a template.
2. How a template variable is rendered.
3. How filters transform display values.
4. How loops display QuerySet results.
5. How empty handles zero records.
6. How conditions change presentation.
7. How extends reuses a base layout.
8. How include reuses a fragment.
9. How url generates a named route.
10. How static generates an asset URL.
11. Why autoescaping matters.
12. Why safe must not be used on untrusted input.

## 58. Submission reflection

Write one example where a template variable was missing, explain how you found the missing context key, and show the corrected view/template pair. Include the expected rendered result.
