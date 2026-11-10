# Day 29: Django Development Server, settings.py and Installed Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours  
**Level:** Beginner  
**Prerequisites:** Day 27 Django introduction and environment setup; Python, OOP and HTTP foundations from earlier phases  
**Tools:** Windows 10/11, Python, VS Code, PowerShell, Django 5.2.19 and browser  
**Project continuity:** `student_portal` project, `config` project package, `profiles` application  
**Approved independent mini-project:** Django Configuration Explorer

> **Teaching instruction:** Read the explanation before typing. Run commands one at a time. Use the exact filenames. Compare your result with the expected behavior. Do not move on while an earlier step is broken.

---

## 1. What you will learn

1. Explain the role of settings.py and key settings.
2. Register an application correctly.
3. Start and stop Django's local development server.
4. Distinguish development settings from production requirements.

## 2. Why this topic exists

Django needs configuration before it can load apps, middleware, databases and templates. The settings module tells Django which applications are active and how the project should behave. The development server is a local testing tool. It is deliberately not a production server.

### Connect it to a real application

Imagine the institute is building its Student Portal. The user opens a browser and requests a page. Django must know which project settings to load, which app owns the feature, which component should handle the request and how the response should be returned. Today's topic is one part of that process.

## 3. Mental model — understand before coding

```text
Browser / Student
       |
       | HTTP request
       v
Django project package: config
       |
       v
profiles application
       |
       v
Today's Django feature
       |
       v
HTTP response / visible result
```

The diagram is intentionally simplified. Some features also use a database, form, template, middleware or authentication component. We will add those in the relevant days.

## 4. Locate the files

The exact files for today are:

- `config/settings.py`
- `config/urls.py`
- `profiles/apps.py`

The overall project is growing in this structure:

```text
student_portal/
├── .venv/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── profiles/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── profiles/
```

**Important:** Some files are created by Django and some are created by us. Do not create duplicate project folders. Keep the existing project from Day 28.

## 5. Prepare the terminal

1. Open VS Code.
2. Open the `student_portal` folder.
3. Select Terminal → New Terminal.
4. Confirm the current directory contains `manage.py`.
5. Activate the same `.venv` created in Day 27.
6. Verify the Python and Django versions.

```powershell
Get-Location
python --version
python -m django --version
```

If `manage.py` is not in the current directory, change to the correct project folder. If Django is not found, check the active interpreter before reinstalling packages.

## 6. Commands — exact order

```powershell
python manage.py check
python manage.py runserver
# Browser: http://127.0.0.1:8000/
# Alternate port:
python manage.py runserver 8001
# Stop the server in its terminal:
# Ctrl+C
```

### Understand every command

### Step 1 — `python manage.py check`

Checks the configuration that Django can inspect at startup. Read warnings as well as errors.

### Step 2 — `python manage.py runserver`

Starts the local server, normally at 127.0.0.1:8000. The process keeps running in that terminal.

### Step 3 — `python manage.py runserver 8001`

Starts the same local project on port 8001 if that port is free.

### Step 4 — `Ctrl+C`

Stops the server. Editing files may trigger automatic reload, but you still need to inspect the terminal for errors.

## 7. Main implementation

### Code to create or update

Use the filenames identified in Section 4. The following code is the lesson's working demonstration:

```python
# config/settings.py — understand these existing settings

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
```

If the code block contains HTML or CSS, put that section in the corresponding HTML or CSS file. Do not paste HTML into `views.py`.

### How to type safely

1. Open the named file.
2. Read the existing contents.
3. Add or replace only the section relevant to today's lesson.
4. Preserve earlier working code.
5. Check indentation and spelling.
6. Save the file.
7. Run `python manage.py check`.
8. Test the browser path or command.
9. Read the terminal output if the page fails.

## 8. Line-by-line and concept walkthrough

### settings.py is executable Python
It is not JSON or a special settings language. It is a Python module containing variables and values that Django imports when it starts.

### DEBUG
With DEBUG=True, Django can show detailed error pages useful during local development. These pages can reveal paths, settings and diagnostic information. Never expose DEBUG=True on a public production site.

### ALLOWED_HOSTS
This setting lists host names that Django accepts in the HTTP Host header when DEBUG=False. Local development has special behavior. For deployment, set the actual host names, not a random wildcard copied from a tutorial.

### INSTALLED_APPS
This is a Python list of app configurations. The default entries enable Django's admin, authentication, content types, sessions, messages and static files. Add the profiles AppConfig as one list item. A missing comma can cause a Python syntax error.

### MIDDLEWARE
Middleware is a chain around request/response processing. SecurityMiddleware, SessionMiddleware, CsrfViewMiddleware and AuthenticationMiddleware each have responsibilities. Removing middleware to silence an error can break security or framework behavior.

### DATABASES
The generated project uses SQLite for local development. The ENGINE names the Django database backend and NAME identifies the database file. PostgreSQL is part of the overall pathway; this lesson does not require installing or configuring a PostgreSQL server.

### STATIC_URL
This is the URL prefix for static assets such as CSS and JavaScript. Static file discovery and production collection are discussed when we build templates and deployment.

### Development server lifecycle
Start it from the directory containing manage.py. Keep the terminal open. Open the printed local address in the browser. Stop it with Ctrl+C. If you close the terminal, the local server stops.

### Configuration versus application code
Do not put a business rule such as employee eligibility into settings.py. Settings configure Django; models represent data; views coordinate requests; business logic belongs in the relevant application layer.

### Production warning
runserver is not designed for production traffic, security hardening or performance. Production uses an appropriate WSGI/ASGI server and deployment configuration. The local DEBUG setting and production host settings must be treated separately.

### Troubleshooting
- Port conflict: run on 8001.
- Server starts but page errors: inspect terminal traceback and URL config.
- App missing: inspect INSTALLED_APPS and app path.
- Settings import error: read the Python traceback and fix the exact syntax or import problem.
- Browser cannot connect: verify server is still running and port matches printed URL.

## 9. Trace the execution

Use the following questions while demonstrating:
1. What did the browser or developer request?
2. Which project file receives the request first?
3. Which app or feature owns the route?
4. Which function or component is selected?
5. What input does it receive?
6. What work does it perform?
7. What result is returned?
8. How can we verify the result?

Ask the learner to explain the flow without looking at the code.

## 10. Expected result and verification

- [ ] The project check passes.
- [ ] The development server starts and displays the local URL.
- [ ] The browser loads the Django welcome page.
- [ ] The server can run on port 8001 when available.
- [ ] The learner explains why DEBUG must be False in production.
- [ ] The learner explains why runserver is not a production server.

Run the system check:

```powershell
python manage.py check
```

Expected output when configuration is valid:

```text
System check identified no issues (0 silenced).
```

This check is not a replacement for browser testing. Visit every required URL and verify the actual behavior.

## 11. Common beginner mistakes and debugging

| Symptom | Likely cause | What to inspect |
|---|---|---|
| `manage.py` not found | Terminal is in the wrong directory | Run Get-Location and locate manage.py |
| `No module named django` | Wrong Python environment | Check python -c "import sys; print(sys.executable)" |
| App not discovered | App missing from settings | Inspect INSTALLED_APPS |
| ImportError | Wrong name or import path | Check package and function spelling |
| 404 response | No matching route | Inspect config/urls.py and profiles/urls.py |
| TemplateDoesNotExist | Incorrect template location | Check profiles/templates/profiles/ |
| Browser cannot connect | Server stopped or wrong port | Inspect terminal and printed URL |
| SyntaxError | Incorrect Python syntax | Read the exact file and line in traceback |

### Debugging routine

1. Reproduce the error.
2. Read the full traceback, not only the last line.
3. Locate the first relevant line in your own project.
4. Confirm the active interpreter and current directory.
5. Check names, imports, indentation and file paths.
6. Change one thing at a time.
7. Run `python manage.py check` again.
8. Repeat the browser test.

## 12. Industry scenario

A training institute needs a Student Portal. The backend developer must make the application understandable to teammates. The feature should have a clear location, a predictable execution path and a testable result.

**Discuss:**
- What does the student need?
- What does the browser send?
- Which component owns the behavior?
- What should happen for missing or invalid input?
- What evidence proves the feature works?

## 13. Approved mini-project — Django Configuration Explorer

### Problem statement

Build a small practical demonstration of today's topic inside the Student Portal workspace. The objective is not to copy a tutorial. The learner must be able to explain and reproduce the implementation.

### Functional requirements

1. Open settings.py and identify BASE_DIR, SECRET_KEY, DEBUG, ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE, DATABASES and STATIC_URL.
2. Explain each setting in one sentence before changing anything.
3. Confirm profiles is registered.
4. Run check, start runserver and inspect the browser.
5. Start on port 8001 and explain why the URL changes.
6. Stop the server cleanly.

### Suggested implementation sequence

1. Inspect the current project.
2. Identify the feature requirement.
3. List the files that will change.
4. Implement one small component.
5. Run a system check.
6. Verify the normal use case.
7. Test an invalid or unexpected case.
8. Fix any error.
9. Record evidence.
10. Explain the code and result to the trainer.

### Acceptance criteria

- [ ] The project check passes.
- [ ] The development server starts and displays the local URL.
- [ ] The browser loads the Django welcome page.
- [ ] The server can run on port 8001 when available.
- [ ] The learner explains why DEBUG must be False in production.
- [ ] The learner explains why runserver is not a production server.

### Submission evidence

- Source files changed for this project.
- Terminal output from checks and commands.
- Browser screenshots or observed URLs, where applicable.
- A short README containing setup and verification steps.
- A short explanation of one error and its resolution.

### Optional extension

Change one small behavior and predict the result before running it. Do not introduce concepts that belong to later lessons.

## 14. AI-assisted implementation guide

Use the AI mentor as a teaching assistant, not as a code generator that hides the learning.

| Level | What to ask | What the learner must do |
|---|---|---|
| 1. Hint | "Give me one hint for the next step." | Attempt the step independently. |
| 2. Plan | "Break this project into small ordered tasks." | Explain the plan before coding. |
| 3. Example | "Show a tiny example of this one concept." | Reproduce and modify it. |
| 4. Guided implementation | "Guide me through one file at a time; wait after each step." | Run each step and share output. |
| 5. Explanation | "Explain every important line and why it is required." | Explain the code back in own words. |
| 6. Debugging | "Here is my exact command, file and traceback. Help isolate the smallest fix." | Apply one fix and retest. |
| 7. Review | "Review my implementation against the requirements and tests." | Correct issues and submit evidence. |

**Planning prompt**

```text
I am a beginner learning Django. Help me plan Django Configuration Explorer.
Do not provide the complete solution. Give me the ordered tasks,
the files I need to inspect, and the verification checkpoints.
```

**Guided implementation prompt**

```text
Guide me through this Django task one step at a time.
Explain the purpose of the command or code, tell me the exact file,
and wait for my terminal output before giving the next step.
Do not skip explanations or write the whole project at once.
```

**Debugging prompt**

```text
I am working on Django Configuration Explorer.
My current directory is: [paste path]
My command is: [paste exact command]
My file contents are: [paste relevant file]
My complete error is: [paste traceback]
Explain the likely cause and the smallest safe correction.
Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Question 1

What is settings.py?

- A. A database table
- B. A Python module containing project configuration
- C. An HTML template
- D. A URL converter

**Correct answer: B** — Django imports this Python module to load project settings.

### Question 2

Why must DEBUG be False in production?

- A. It makes pages slower only
- B. It disables CSS
- C. Detailed debug pages can expose sensitive diagnostic information
- D. It removes all apps

**Correct answer: C** — Debug pages can reveal implementation details and sensitive configuration.

### Question 3

What does INSTALLED_APPS do?

- A. Lists applications Django should load
- B. Stores user passwords
- C. Defines browser routes
- D. Starts the server

**Correct answer: A** — Django loads configured app packages and contrib apps from this setting.

### Question 4

What should you do if port 8000 is occupied?

- A. Delete manage.py
- B. Use another port such as 8001
- C. Remove middleware
- D. Change the database engine

**Correct answer: B** — runserver accepts a port argument.

### Question 5

Which statement about runserver is correct?

- A. It is the production server
- B. It automatically deploys to cloud
- C. It replaces Gunicorn
- D. It is intended for local development

**Correct answer: D** — Use a suitable production server and deployment configuration outside development.

## 16. Interview preparation

### Question 1 — Explain today's topic
**Answer:** Django needs configuration before it can load apps, middleware, databases and templates. The settings module tells Django which applications are active and how the project should behave. The development server is a local testing tool. It is deliberately not a production server.

**Follow-up:** Explain the same concept using the Student Portal project.

### Question 2 — Which files are involved?
**Answer:** `config/settings.py`, `config/urls.py`, `profiles/apps.py`. Explain what each file owns and how the files connect.

**Follow-up:** What would you inspect if the feature does not work?

### Question 3 — How do you verify your implementation?
**Answer:** Run the relevant management command, inspect the output, open the expected browser path and test an edge case. A successful system check alone does not prove every user journey.

**Follow-up:** What evidence would you submit to a reviewer?

### Question 4 — A teammate copied code but cannot explain it. Is the task complete?
**Answer:** No. The learner must explain the responsibility of each component, reproduce the behavior, test a normal and invalid case and document the setup.

## 17. Completion checklist

- [ ] I can explain today's topic in simple language.
- [ ] I can identify the exact files.
- [ ] I can explain the important code statements.
- [ ] I ran the required commands.
- [ ] `python manage.py check` passes.
- [ ] I verified the expected behavior.
- [ ] I tested an edge case.
- [ ] I completed **Django Configuration Explorer**.
- [ ] I submitted source files and evidence.
- [ ] I answered the interview questions and reviewed the MCQs.

## 18. Trainer validation

Do not mark the day complete just because code exists. Ask the student to:
1. Demonstrate the feature.
2. Explain the flow.
3. Change one small part independently.
4. Predict the result before running.
5. Diagnose one controlled mistake.

**Next lesson:** Day 30 — URL Routing, Path Converters and URL Patterns
