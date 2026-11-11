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

---

# Extended Beginner Lab — Template Inheritance and Static Files

## 19. Why template inheritance exists

Imagine a portal with a home page, student list, student detail, course list and attendance page.

All pages need the same header, navigation, footer, CSS references and message area.

Copying the same HTML into every file creates maintenance problems.

Template inheritance provides a shared layout.

## 20. Base template

A base template contains the shared page structure.

~~~django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Student Portal{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">
</head>
<body>
    <header>
        <h1>Student Portal</h1>
    </header>

    <nav>
        <a href="{% url 'home' %}">Home</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>Student Portal</footer>
</body>
</html>
~~~

## 21. What is a block?

A block defines a section that a child template can override.

The base template provides default content.

A child template supplies its own content for the same block name.

## 22. Child template

~~~django
{% extends "profiles/base.html" %}

{% block title %}Student List{% endblock %}

{% block content %}
    <h2>Students</h2>
    <p>Student list content appears here.</p>
{% endblock %}
~~~

extends should appear at the beginning of the child template before ordinary page content.

## 23. Block names must match

If the base template defines content but the child defines body, the child block will not replace content.

Check exact spelling and capitalization.

## 24. Preserve parent block content

Django provides block.super when a child needs to include the parent's block content.

Example:

~~~django
{% block content %}
    {{ block.super }}
    <p>Additional child content</p>
{% endblock %}
~~~

Use this only when parent content should remain.

## 25. Include tag

An include renders a separate reusable fragment.

Example:

~~~django
{% include "profiles/_navigation.html" %}
~~~

This can be useful for a navigation bar or reusable card.

Inheritance shares the page structure. Include shares a smaller fragment.

## 26. Inheritance versus include

| Inheritance | Include |
|---|---|
| Child extends a base | Template inserts another template |
| Uses blocks | Reuses a fragment |
| Defines page layout | Defines reusable partial UI |
| Usually one base hierarchy | Can include multiple fragments |

## 27. Static files

Static files are assets that belong to the application code.

Examples:
- CSS.
- JavaScript.
- Logo.
- Icons.
- Background images.

They are different from media files uploaded by users.

## 28. Create a static folder

Inside the profiles app, create:

~~~text
profiles/
└── static/
    └── profiles/
        ├── css/
        │   └── site.css
        └── images/
            └── logo.png
~~~

The app namespace inside static prevents name collisions with other apps.

## 29. Load a CSS file

At the top of the template:

~~~django
{% load static %}
~~~

Then:

~~~django
<link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">
~~~

Django's static tag generates the URL based on static-file settings.

## 30. Example CSS

~~~css
body {
    font-family: Arial, sans-serif;
    margin: 0;
}

header,
footer {
    padding: 1rem;
}

main {
    max-width: 960px;
    margin: 0 auto;
    padding: 1rem;
}

nav a {
    margin-right: 1rem;
}
~~~

The CSS is stored in site.css, not in a Python view.

## 31. Verify static file discovery

Run:

~~~powershell
python manage.py findstatic profiles/css/site.css
~~~

Django should report the location of the file if it is discoverable.

If it cannot find the file:
- Check folder nesting.
- Check app registration.
- Check spelling.
- Check STATICFILES_DIRS if using a project-level static folder.

## 32. Understand STATIC_ROOT and STATICFILES_DIRS

STATIC_ROOT:
- Destination directory for collected static files.
- Used by collectstatic in deployment workflows.

STATICFILES_DIRS:
- Additional directories where Django looks for project-level static files.

App-level static folders can be discovered through installed apps.

Do not set STATIC_ROOT to the same folder used as a source directory for static development assets.

## 33. Development static files versus production

During development, Django can serve static files through the development setup when DEBUG is enabled.

Production uses a separate static-file collection and serving strategy.

The collectstatic command is used later in deployment preparation.

Do not assume that because CSS loads through runserver, production static files are configured.

## 34. Static file caching

Browsers may cache CSS and JavaScript.

If a change does not appear:
1. Confirm the file was saved.
2. Confirm the correct static URL.
3. Open the URL directly.
4. Refresh with cache disabled.
5. Inspect browser developer tools.

Do not randomly rename files before checking the path.

## 35. Common inheritance errors

| Symptom | Cause | Fix |
|---|---|---|
| Child content not visible | Block names differ | Match block names |
| Base template not found | Wrong extends path | Check template namespace |
| Duplicate page header | Child repeats parent layout | Keep shared structure in base |
| Include missing | Wrong include path | Check app template folder |
| Child extends after HTML | extends is not at top | Move extends to beginning |

## 36. Common static-file errors

| Symptom | Cause | Fix |
|---|---|---|
| CSS 404 | Wrong static path | Check static folder and tag |
| CSS not applied | Link tag missing or cached | Inspect network and refresh |
| findstatic cannot locate file | App not installed or wrong path | Check INSTALLED_APPS and folder nesting |
| Static works locally but not production | Production collection/serving not configured | Review collectstatic and deployment config |

## 37. Guided exercise — Shared Institute Layout

Create:
1. One base template.
2. One navigation include.
3. One student list child.
4. One student detail child.
5. One shared CSS file.

Change the header once in the base template and verify that both child pages update.

## 38. Self-check questions

1. What problem does template inheritance solve?
2. What is a block?
3. Why must child block names match?
4. What does block.super do?
5. What is the difference between extends and include?
6. What are static files?
7. What does load static do?
8. What is the purpose of findstatic?
9. What is STATIC_ROOT?
10. Why does production need a static-file strategy?

## 39. Answers

1. It avoids repeated page structure.
2. A replaceable section in a base template.
3. Django uses the block name to match child content.
4. Includes parent block content.
5. extends inherits a layout; include inserts a fragment.
6. Application assets such as CSS, JavaScript and logos.
7. Loads the static template tag library.
8. Helps locate a static asset.
9. Destination for collected static files.
10. Production serving differs from the development server.

## 40. Independent challenge — Multi-Page Institute Theme

Build two child pages using one base template and one CSS file.

Evidence:
- Screenshot of page one.
- Screenshot of page two.
- Browser network result for the CSS file.
- Output from findstatic.
- Explanation of inheritance and static-file discovery.

---

# Deep Practice Workbook — Static Assets and Shared Layout

## 41. Static asset versus uploaded media

Static asset:
- Belongs to the application source.
- Example: site.css, logo.svg, navigation.js.

Uploaded media:
- Submitted by a user.
- Example: profile photo, resume, attachment.

They have different storage, validation and security requirements.

## 42. Static directory structure

~~~text
profiles/
└── static/
    └── profiles/
        ├── css/
        │   ├── site.css
        │   └── forms.css
        ├── js/
        │   └── navigation.js
        └── images/
            └── institute-logo.svg
~~~

The repeated app name creates a namespace and reduces filename collisions.

## 43. Load multiple assets

~~~django
{% load static %}

<link rel="stylesheet"
      href="{% static 'profiles/css/site.css' %}">

<script src="{% static 'profiles/js/navigation.js' %}"
        defer></script>
~~~

The defer attribute allows the browser to download the script without blocking HTML parsing and execute it after parsing.

## 44. Static file verification checklist

1. File exists.
2. Folder path is correct.
3. App is installed.
4. Static tag library is loaded.
5. Template path is correct.
6. Browser URL matches expected static URL.
7. Network response is successful.
8. CSS selector matches the HTML.
9. Browser cache is refreshed if necessary.

## 45. What collectstatic does

In deployment workflows, collectstatic gathers static files from configured locations into STATIC_ROOT.

It does not:
- Create your CSS.
- Fix wrong paths.
- Replace static-file configuration.
- Upload user media automatically.

It is a collection step used before production static serving.

## 46. Why not use STATIC_ROOT as the source folder?

STATIC_ROOT is the collection destination.

STATICFILES_DIRS and app static directories are source locations.

Keep source and collection destinations separate to avoid confusing discovery and collection behavior.

## 47. Shared layout exercise

Create a base template with:
- HTML document structure.
- Header.
- Navigation.
- Main content block.
- Footer.
- Static CSS reference.

Create two child templates:
- Student list.
- Course list.

Change the header once and verify both pages update.

## 48. Include exercise

Create a navigation fragment and include it in the base template.

Then change one navigation label.

Verify that all pages using the base template show the change.

## 49. Common browser inspection steps

Open browser developer tools.

Use the Network tab:
1. Reload the page.
2. Find the CSS request.
3. Check the request URL.
4. Check status code.
5. Inspect response content.
6. Check whether the browser loaded the latest version.

Use the Elements/Inspector tab:
- Confirm the link element exists.
- Confirm the CSS selector matches.
- Confirm no later rule overrides the style.

## 50. Production warning

The Django development server's static handling is not a production architecture.

Production requires a deliberate static-file serving strategy such as a web server, object storage or a suitable static-file service.

This lesson only teaches source layout and discovery. Deployment configuration belongs to the deployment phase.

## 51. Knowledge check

1. What is a static file?
2. What is uploaded media?
3. Why use an app namespace in the static folder?
4. What does collectstatic do?
5. What is STATIC_ROOT?
6. What is STATICFILES_DIRS?
7. Why does a CSS file return 404?
8. Why might the browser show old CSS?
9. What is the benefit of a shared base template?
10. What is the difference between extends and include?

## 52. Answers

1. An application asset such as CSS, JavaScript or a logo.
2. A file uploaded by a user.
3. To avoid naming collisions between apps.
4. Collects static assets into the configured destination.
5. Destination for collected files.
6. Additional source directories for static assets.
7. Wrong path, app discovery or static configuration.
8. Browser cache.
9. It avoids repeating shared page structure.
10. extends inherits a layout; include inserts a fragment.

## 53. Final asset audit

Before completing:
- Confirm all child templates extend the correct base.
- Confirm block names match.
- Confirm include paths.
- Confirm static files use the static tag.
- Confirm findstatic locates the assets.
- Confirm the browser loads the CSS.
- Explain what additional work is required in production.

## 54. Final independent static-file assessment

Create a shared base template and two child templates.

Use one stylesheet and one navigation include.

Test the following:
1. Both child templates inherit the same header.
2. Both pages load the same CSS.
3. A change to the base header appears on both pages.
4. A change to the navigation include appears on both pages.
5. findstatic locates the CSS file.
6. The browser network panel returns the stylesheet successfully.

Write a short explanation of the difference between source static folders and STATIC_ROOT.


## 55. Static-file deployment questions

Explain:
1. Why does production not normally use runserver to serve static assets?
2. What does collectstatic collect?
3. Where are collected files written?
4. Who serves those files in production?
5. Why should uploaded media be handled separately?
6. Why should a browser cache be checked before changing file paths?

Write a short deployment handover that identifies the static source folders and the collection destination without exposing secrets.

