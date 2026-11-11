# Day 33: Template Inheritance, Reusable Components and Static Files

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Previous Django lessons; Python, OOP, HTTP and SQL foundations  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment and Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Reusable Website Layout

> **Teaching rule:** Do not copy a command without understanding it. Use the exact file path, run one step at a time, inspect the output and explain what the framework is doing.

## 1. Learning objectives

1. Explain why websites use shared base templates.
2. Create a parent template with named blocks and child templates.
3. Use URL reversing in navigation links.
4. Add static CSS and distinguish static assets from uploaded media.

## 2. Concept introduction — start from zero

Most pages on a website share a header, navigation, footer and overall layout. Copying the same HTML into every page creates duplication. Template inheritance lets one base template define the shared layout while child templates provide page-specific content. Static files such as CSS, JavaScript and logos are application assets served separately from templates.

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

- `profiles/templates/profiles/base.html`
- `profiles/templates/profiles/home.html`
- `profiles/templates/profiles/about.html`
- `profiles/static/profiles/css/site.css`
- `profiles/views.py`
- `profiles/urls.py`

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
python manage.py check
python manage.py runserver
# Open / and /about/
# Browser devtools -> Network -> filter CSS
```

### Understand every command

### Step 1 — `Create base.html`

This is the parent template. It contains shared HTML such as document structure, header, navigation, main content region and footer.

### Step 2 — `Load static tags`

{% load static %} enables the static template tag library in this template.

### Step 3 — `Define blocks`

block title and block content are named regions that child templates may override. Default content appears if a child does not override a block.

### Step 4 — `Use the static tag`

{% static 'profiles/css/site.css' %} builds the static asset URL using STATIC_URL and configured static-file finders.

### Step 5 — `Use named URLs`

{% url 'home' %} reverses a named URL pattern. If the path changes but the name remains, the generated link can still point to the right route.

### Step 6 — `Create child templates`

A child begins with {% extends 'profiles/base.html' %}. It inherits the parent layout and supplies content for the blocks.

### Step 7 — `Create static folder`

Store the CSS at profiles/static/profiles/css/site.css. App-namespaced static paths avoid collisions between apps.

### Step 8 — `Verify in browser tools`

Open the page and inspect the CSS request in the Network tab. A missing or 404 stylesheet usually means a path or static-file configuration problem.

## 7. Implementation — correct files

### Code demonstration

The code below may contain Python, HTML or CSS sections. Use the filename comments to put each section into the correct file. Never paste HTML into a .py file.

```python
<!-- profiles/templates/profiles/base.html -->
{% load static %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{% block title %}Student Portal{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">
</head>
<body>
    <header><a href="{% url 'home' %}">Student Portal</a></header>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
    </nav>
    <main>{% block content %}{% endblock %}</main>
    <footer>Learning Django</footer>
</body>
</html>

<!-- profiles/templates/profiles/home.html -->
{% extends "profiles/base.html" %}
{% block title %}Home | Student Portal{% endblock %}
{% block content %}
<h1>Student Portal</h1>
<p>Welcome to the student portal.</p>
{% endblock %}

<!-- profiles/templates/profiles/about.html -->
{% extends "profiles/base.html" %}
{% block title %}About | Student Portal{% endblock %}
{% block content %}
<h1>About</h1>
<p>This is a Django learning application.</p>
{% endblock %}

/* profiles/static/profiles/css/site.css */
body { font-family: Arial, sans-serif; margin: 2rem; }
header, footer { padding: 1rem; background: #eeeeee; }
main { margin-top: 1.5rem; }
```

### Before saving

1. Read the existing file.
2. Preserve working code from earlier days.
3. Add the new code at the correct location.
4. Check spelling and indentation.
5. Save the file.
6. Run the relevant Django command.
7. Inspect terminal output before opening the browser.

## 7A. Connect the child templates to views and routes

The templates do not open by themselves. The browser requests a URL, a view renders the child template, and the root URLconf must include the app routes.

**File: profiles/views.py**

```python
from django.shortcuts import render

def home(request):
    return render(request, "profiles/home.html")

def about(request):
    return render(request, "profiles/about.html")
```

**File: profiles/urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

**File: config/urls.py**

Confirm the project URLconf includes the app URLconf:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
```

**Why these lines matter**

- `render` loads the child template and returns the HTTP response.
- `home` renders the home child template.
- `about` renders the about child template.
- The app URLconf maps each browser path to the corresponding view.
- The root URLconf includes the app URLconf, so the routes are reachable.
- The route names home and about match the names used by the navigation links in base.html.

## 8. Detailed explanation

### Template inheritance
A parent template defines the shared layout. A child template uses extends and overrides named blocks. The child template should put extends first, apart from template comments.

### Blocks
A block is a named insertion point. The parent defines it; a child can replace its content. Use meaningful names such as title, content and extra_js.

### include versus extends
extends inherits a page layout. include renders a reusable partial inside another template, such as a small navigation component. Use each for its intended purpose.

### Why namespaced template paths?
If two apps both contain home.html, the namespaced paths profiles/home.html and courses/home.html avoid ambiguity.

### Static files
Static files are assets shipped with the application: CSS, JavaScript, icons and logos. Uploaded user files are media, which need upload validation, storage and access controls.

### STATIC_URL and static tag
STATIC_URL is the URL prefix. The static template tag asks Django's static-file machinery to build the correct URL. Do not hardcode a localhost URL in the template.

### Development versus production
During development, Django's staticfiles support can serve static files. In production, collectstatic gathers assets into STATIC_ROOT and a web server or storage service serves them. Never assume runserver's static handling is a production strategy.

### Static files troubleshooting
- Confirm django.contrib.staticfiles is in INSTALLED_APPS.
- Check spelling and case of folder/file names.
- Inspect the generated CSS URL in the page source.
- Check browser Network status and server output.
- Remember CSS changes may require a browser refresh; cache may need clearing.

## 9. Execution trace

Explain these questions aloud:
1. What is the input or requested operation?
2. Which file or command handles it?
3. What does Django do automatically?
4. What did the developer implement?
5. What result should be produced?
6. How do we prove that result is correct?

## 10. Verification checklist

- [ ] Both pages render using base.html.
- [ ] Both pages share header, navigation and footer.
- [ ] Each child page displays its own title and content.
- [ ] Navigation links resolve using URL names.
- [ ] CSS loads with a successful network response.
- [ ] The learner explains static assets versus uploaded media.

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

## 13. Approved mini-project — Reusable Website Layout

### Objective
Build a working demonstration of today's approved concept in the existing Student Portal.

### Ordered tasks

1. Create base.html with shared header, navigation, content block and footer.
2. Create home.html and about.html as child templates.
3. Create the CSS file at the exact namespaced path.
4. Create views and routes for home and about if not already present.
5. Open both pages and confirm shared layout.
6. Inspect the CSS network request and change one CSS rule to verify it is loaded.

### Acceptance checks

- [ ] Both pages render using base.html.
- [ ] Both pages share header, navigation and footer.
- [ ] Each child page displays its own title and content.
- [ ] Navigation links resolve using URL names.
- [ ] CSS loads with a successful network response.
- [ ] The learner explains static assets versus uploaded media.

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
I am a beginner. Help me plan Reusable Website Layout.
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

### Q1. Which tag creates a child template?

A. {% extends %}
B. {% csrf_token %}
C. {% for %}
D. {% debug %}

**Answer: A.** extends inherits the parent template layout.

### Q2. What is the main use of a template block?

A. Create a database index
B. Define a region that a child template can override
C. Register a Django app
D. Validate a form

**Answer: B.** Blocks allow child templates to provide page-specific content.

### Q3. What is a static file?

A. A model row
B. A user password
C. An application asset such as CSS or JavaScript
D. A URL parameter

**Answer: C.** Static assets are served separately from rendered templates.

### Q4. Why use {% url 'home' %}?

A. It reverses a named URL pattern
B. It executes SQL
C. It creates a user
D. It loads a CSS file

**Answer: A.** URL reversing avoids hardcoding route paths.

### Q5. Which statement is correct for production static files?

A. runserver is always the production static host
B. Collect static assets and serve them with suitable production infrastructure
C. Put CSS in settings.py
D. Disable staticfiles

**Answer: B.** Production deployments collect and serve static assets using a web server or storage backend.

## 16. Interview preparation

### Q1. Explain today's topic in simple words.
**Answer:** Most pages on a website share a header, navigation, footer and overall layout. Copying the same HTML into every page creates duplication. Template inheritance lets one base template define the shared layout while child templates provide page-specific content. Static files such as CSS, JavaScript and logos are application assets served separately from templates.

**Follow-up:** Give an example from the Student Portal.

### Q2. Which files or commands are important?
**Answer:** `profiles/templates/profiles/base.html`, `profiles/templates/profiles/home.html`, `profiles/templates/profiles/about.html`, `profiles/static/profiles/css/site.css`, `profiles/views.py`, `profiles/urls.py`. Explain the responsibility of each.

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
- [ ] I completed Reusable Website Layout.
- [ ] I submitted reproducible evidence.
- [ ] I can answer the interview questions.

## 18. Independent completion test

Do not mark the day complete merely because a file contains code. Complete every check yourself:
1. Demonstrate the result in the browser or terminal.
2. Explain the execution flow without reading the notes.
3. Modify one small part independently and predict the result before running it.
4. Compare the actual result with your prediction.
5. Diagnose and fix one controlled mistake, such as a misspelled variable, template path or setting.

**Next lesson:** Day 34 — Django Models and Database Field Types
