# Day 33: Template Inheritance, Reusable Components and Static Files

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–34 as applicable; review the previous Django lessons before continuing  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Reusable Website Layout

> **Trainer guidance:** Show the learner the exact file path before showing the code. Explain why the file exists, what each important line does, how to run the project and how to verify the result.

## 1. Learning objectives

- Explain template inheritance, reusable components and static files.
- Identify the Django files and folders used.
- Implement the example step by step.
- Explain the relationship between Django code and the browser or database.
- Verify the result and troubleshoot common errors.
- Complete Reusable Website Layout.

## 2. Concept introduction

Template inheritance lets child templates reuse a common base layout. A base template defines blocks that child templates fill. Static files are assets such as CSS, JavaScript and images; Django serves them during development when staticfiles is configured.

## 3. Why the concept matters

A Django application becomes easier to maintain when shared presentation is reused, data is represented consistently and database changes are tracked. These practices help teams review code and understand how a feature evolved.

## 4. File-by-file implementation

### File or command: `profiles/templates/profiles/base.html`

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Employee Portal{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">
</head>
<body>
    <header><h1>Employee Portal</h1></header>
    <main>{% block content %}{% endblock %}</main>
</body>
</html>
```

### File or command: `profiles/templates/profiles/home.html`

```html
{% extends "profiles/base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Welcome</h2>
    <p>Manage employee information.</p>
{% endblock %}
```

### File or command: `profiles/static/profiles/css/site.css`

```css
body {
    font-family: Arial, sans-serif;
    margin: 2rem;
}
header {
    border-bottom: 1px solid #cccccc;
}
```

### File or command: `profiles/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, "profiles/home.html")
```

## 5. Explain the important statements

### profiles/templates/profiles/base.html

1. `{% load static %}` — Uses Django template syntax to load, extend or define a template block.
2. `<!DOCTYPE html>` — Part of the file structure or configuration; understand how it supports the feature.
3. `<html>` — Part of the file structure or configuration; understand how it supports the feature.
4. `<head>` — Part of the file structure or configuration; understand how it supports the feature.
5. `    <title>{% block title %}Employee Portal{% endblock %}</title>` — Uses Django template syntax to load, extend or define a template block.
6. `    <link rel="stylesheet" href="{% static 'profiles/css/site.css' %}">` — Uses Django template syntax to load, extend or define a template block.
7. `</head>` — Part of the file structure or configuration; understand how it supports the feature.
8. `<body>` — Part of the file structure or configuration; understand how it supports the feature.
9. `    <header><h1>Employee Portal</h1></header>` — Part of the file structure or configuration; understand how it supports the feature.
10. `    <main>{% block content %}{% endblock %}</main>` — Uses Django template syntax to load, extend or define a template block.
11. `</body>` — Part of the file structure or configuration; understand how it supports the feature.
12. `</html>` — Part of the file structure or configuration; understand how it supports the feature.

### profiles/templates/profiles/home.html

1. `{% extends "profiles/base.html" %}` — Uses Django template syntax to load, extend or define a template block.
2. ` ` — Part of the file structure or configuration; understand how it supports the feature.
3. `{% block title %}Home{% endblock %}` — Uses Django template syntax to load, extend or define a template block.
4. ` ` — Part of the file structure or configuration; understand how it supports the feature.
5. `{% block content %}` — Uses Django template syntax to load, extend or define a template block.
6. `    <h2>Welcome</h2>` — Part of the file structure or configuration; understand how it supports the feature.
7. `    <p>Manage employee information.</p>` — Part of the file structure or configuration; understand how it supports the feature.
8. `{% endblock %}` — Uses Django template syntax to load, extend or define a template block.

### profiles/static/profiles/css/site.css

1. `body {` — Part of the file structure or configuration; understand how it supports the feature.
2. `    font-family: Arial, sans-serif;` — Part of the file structure or configuration; understand how it supports the feature.
3. `    margin: 2rem;` — Part of the file structure or configuration; understand how it supports the feature.
4. `}` — Part of the file structure or configuration; understand how it supports the feature.
5. `header {` — Part of the file structure or configuration; understand how it supports the feature.
6. `    border-bottom: 1px solid #cccccc;` — Part of the file structure or configuration; understand how it supports the feature.
7. `}` — Part of the file structure or configuration; understand how it supports the feature.

### profiles/views.py

1. `from django.shortcuts import render` — Imports the Django component used by this file.
2. ` ` — Part of the file structure or configuration; understand how it supports the feature.
3. `def home(request):` — Defines a method or view function.
4. `    return render(request, "profiles/home.html")` — Part of the file structure or configuration; understand how it supports the feature.

## 6. How to run and verify

1. Activate the project's virtual environment.
2. Open the terminal in the folder containing manage.py.
3. Run `python manage.py check`.
4. Execute the commands or start the development server as appropriate.
5. Open the page in a browser or inspect migration status.
6. Compare actual behavior with the expected result.
7. Record any warning and explain whether it is expected.

## 7. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Template block is not rendered | extends path and matching block names |
| CSS is missing | static directory, STATIC_URL, {% load static %} and URL |
| Model is not detected | app in INSTALLED_APPS and model import |
| Field configuration error | Field type and required field arguments |
| No migration is generated | Check whether model changes exist and the correct app is selected |
| Migration fails | Read the full database error and inspect migration dependencies |
| Database does not reflect model change | Run makemigrations and then migrate |

## 8. Industry scenario

A staff management website needs a consistent page header and styling, an employee data model and a repeatable way to update its database structure. Django's template inheritance, static files, model fields and migrations support these needs.

## 9. Approved mini-project — Reusable Website Layout

**Objective:** Reusable Website Layout.

### Functional requirements

1. Create base.html with common HTML structure.
2. Define title and content blocks in base.html.
3. Create home.html and extend the base template.
4. Override the title and content blocks.
5. Create the app static folder and CSS file.
6. Load static and use the static template tag for the CSS link.
7. Open the page and verify that the shared layout and stylesheet load.

### Suggested structure

```text
projects/day_33/
├── manage.py
├── config/
└── profiles/
    ├── models.py
    ├── migrations/
    ├── templates/
    └── static/
```

### Validation checklist

- [ ] The child template extends the correct base template.
- [ ] The required blocks appear in the base template.
- [ ] The child overrides the blocks.
- [ ] The static folder uses app/static/app_name/ convention.
- [ ] The browser loads the CSS file without a 404.

### Submission evidence

- Updated source files.
- Commands executed and terminal output.
- Browser screenshot or migration status.
- README with exact file paths and setup instructions.
- Explanation of one design decision and one error handled.

## 10. AI-assisted implementation guide

**Planning prompt:** "Help me plan Reusable Website Layout. List the files, ordered tasks, commands and verification checks. Do not write the complete solution."

**Guided prompt:** "Guide me through one file at a time. Explain why the file is needed, show only the next change and wait for my output."

**Debugging prompt:** "Inspect my exact Django error, file path and command. Explain the likely cause and how to verify the fix."

**Review prompt:** "Review my implementation against the approved requirements. Identify missing validation, naming issues and maintainability concerns."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Organize Django presentation, data or database structure changes in a maintainable way.  
B. Replace Python.  
C. Disable validation.  
D. Remove all configuration.  
**Answer: A.** The concept supports a maintainable Django application.

**Q2. What should you inspect when the result is missing?**  
A. Only the browser theme.  
B. The relevant file path, setting and Django output.  
C. Delete the project.  
D. Ignore the warning.  
**Answer: B.** File paths and configuration commonly determine whether Django discovers the component.

**Q3. Which practice is safest?**  
A. Edit generated files without understanding them.  
B. Ignore migrations.  
C. Follow the correct workflow and verify each change.  
D. Commit local secrets.  
**Answer: C.** Use a repeatable workflow and inspect the result.

**Q4. What is the best evidence of completion?**  
A. A file exists.  
B. The code is long.  
C. The learner watched a video.  
D. The feature works and its behavior is verified.  
**Answer: D.** Evidence should show the required behavior.

**Q5. What should the README contain?**  
A. Setup, file paths, commands and validation results.  
B. Only a title.  
C. A private password.  
D. No instructions.  
**Answer: A.** Clear instructions make the project reproducible.

## 12. Interview preparation

**Q1. Explain template inheritance, reusable components and static files.**  
**Answer:** Template inheritance lets child templates reuse a common base layout. A base template defines blocks that child templates fill. Static files are assets such as CSS, JavaScript and images; Django serves them during development when staticfiles is configured.

**Q2. Which files or commands are important?**  
**Answer:** Explain each file or command from the demonstration and its responsibility.

**Q3. How would you troubleshoot a failure?**  
**Answer:** Read the full traceback, confirm file paths and configuration, run Django system checks and verify the result after one focused correction.

**Follow-up:** What evidence would you show another developer?  
**Answer:** The source change, command output, browser behavior or migration status and a concise README.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Identify the relevant file paths.
- [ ] Implement the example.
- [ ] Run the required checks or commands.
- [ ] Verify the expected result.
- [ ] Complete Reusable Website Layout.
- [ ] Test normal and error cases.
- [ ] Complete all five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 34.
