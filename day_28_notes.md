# Day 28: Creating Django Projects and Applications, Project Structure and manage.py

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours  
**Level:** Beginner  
**Prerequisites:** Day 27 Django introduction and environment setup; Python, OOP and HTTP foundations from earlier phases  
**Tools:** Windows 10/11, Python, VS Code, PowerShell, Django 5.2.19 and browser  
**Project continuity:** `student_portal` project, `config` project package, `profiles` application  
**Approved independent mini-project:** Personal Profile Django Project

> **Teaching instruction:** Read the explanation before typing. Run commands one at a time. Use the exact filenames. Compare your result with the expected behavior. Do not move on while an earlier step is broken.

---

## 1. What you will learn

1. Create a Django project in the correct workspace.
2. Create a Django application and register its AppConfig.
3. Explain the role of the generated project and app files.
4. Run management commands and verify the initial application.

## 2. Why this topic exists

Think of a Django project as the whole website and an app as one feature area inside it. A college portal might have separate apps for profiles, courses, attendance and fees. Each app owns a related set of models, views, templates and tests. The project package owns site-wide configuration and root URL routing. A project may contain many apps; an app is not a separate server by default.

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

- `manage.py`
- `config/__init__.py`
- `config/settings.py`
- `config/urls.py`
- `config/asgi.py`
- `config/wsgi.py`
- `profiles/apps.py`
- `profiles/models.py`
- `profiles/views.py`
- `profiles/admin.py`
- `profiles/tests.py`
- `profiles/migrations/`

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
# Run these from the empty student_portal workspace
python --version
python -m pip --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "Django==5.2.19"
python -m django --version
django-admin startproject config .
python manage.py startapp profiles
python manage.py check
python manage.py help
```

### Understand every command

### Step 1 — `python -m venv .venv`

Creates an isolated Python environment in a folder named .venv. Packages installed there do not need to be installed globally.

### Step 2 — `.\.venv\Scripts\Activate.ps1`

Activates the environment in PowerShell. The prompt normally shows (.venv). If PowerShell blocks scripts, use the approved execution-policy guidance from Day 27 rather than running commands from an unknown source.

### Step 3 — `python -m pip install Django==5.2.19`

Installs the pinned Django version into the active interpreter. Pinning gives students a repeatable classroom environment.

### Step 4 — `django-admin startproject config .`

Creates the configuration package named config in the current folder. The dot means current folder; without it Django creates an extra outer directory.

### Step 5 — `python manage.py startapp profiles`

Creates a feature package named profiles with standard files. This command must run from the folder containing manage.py.

### Step 6 — `python manage.py check`

Runs Django's system checks and reports configuration issues it can detect. It does not test every user journey.

### Step 7 — `python manage.py help`

Lists management commands available in this project. Use python manage.py help migrate to inspect a specific command.

## 7. Main implementation

### Code to create or update

Use the filenames identified in Section 4. The following code is the lesson's working demonstration:

```python
# Create config project package in the current folder:
django-admin startproject config .

# Create one feature app:
python manage.py startapp profiles

# profiles/apps.py
from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

# config/settings.py — add one item to the existing list
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
]
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

### Understand the generated structure
```text
student_portal/
├── .venv/                 # local environment; do not commit
├── manage.py              # project command-line entry point
├── config/                # site-wide configuration package
│   ├── __init__.py
│   ├── settings.py        # settings
│   ├── urls.py            # root URL router
│   ├── asgi.py            # ASGI entry point
│   └── wsgi.py            # WSGI entry point
└── profiles/              # one feature application
    ├── migrations/        # database schema history
    ├── __init__.py
    ├── admin.py           # admin registration
    ├── apps.py            # application configuration
    ├── models.py          # data models
    ├── tests.py           # automated tests
    └── views.py           # request handlers
```

**manage.py:** Django generates this file. It sets the default settings module to `config.settings` and delegates the requested command to Django. Do not rewrite it.  
**settings.py:** Python configuration for the whole project: installed apps, middleware, database, templates, static files and security-related settings.  
**urls.py:** Root URL configuration. Later it will include the profiles app's routes.  
**asgi.py / wsgi.py:** Server entry points for different deployment interfaces. Students need to recognize them now; production server configuration is a later topic.  
**apps.py:** The AppConfig describes the app to Django.  
**models.py:** Holds Python classes that describe stored data.  
**views.py:** Holds callables that receive requests and return responses.  
**admin.py:** Registers models for Django's internal admin interface.  
**tests.py:** Holds automated checks of application behavior.  
**migrations/:** Holds version-controlled database schema change files.

### Project versus app — common interview distinction
A project is the website's configuration and collection of apps. An app is a feature module. For example, `config` is the project package and `profiles` is an app. The outer repository folder name does not have to match either.

### Why app registration matters
Django reads INSTALLED_APPS to discover app configuration and load app functionality. Adding the path `profiles.apps.ProfilesConfig` registers the app. The Python string must match the actual package path.

### What the dot means in startproject
`django-admin startproject config .` means: create the config package in the current working directory. It is useful when the current folder is already the repository root. Check the folder tree immediately after running it.

### Virtual environment and version pin
The virtual environment isolates project dependencies. A pinned version makes the classroom instructions reproducible. The class should use the same Python/Django version for the phase; don't randomly upgrade midway.

### Common errors
- `django-admin is not recognized`: activate .venv or use `python -m django startproject config .`.
- `No module named django`: the active interpreter does not have Django installed.
- `manage.py not found`: terminal is not in the project root.
- App does not load: check spelling and INSTALLED_APPS.
- Port already in use: use `python manage.py runserver 8001` or stop the other local server.

### What is not done yet?
We have not created a profile page, model or database table. We have created the project structure and registered the app. The next lessons progressively add routes, views, templates and models.

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

- [ ] The command prompt shows the virtual environment is active.
- [ ] python -m django --version prints the pinned version.
- [ ] manage.py, config/ and profiles/ are siblings.
- [ ] profiles.apps.ProfilesConfig is present in INSTALLED_APPS.
- [ ] python manage.py check reports no issues.

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

## 13. Approved mini-project — Personal Profile Django Project

### Problem statement

Build a small practical demonstration of today's topic inside the Student Portal workspace. The objective is not to copy a tutorial. The learner must be able to explain and reproduce the implementation.

### Functional requirements

1. Create a new empty folder called student_portal and open it in VS Code.
2. Create and activate .venv. Confirm the interpreter path using python -c "import sys; print(sys.executable)".
3. Install the pinned Django version and record python -m django --version.
4. Create the config project and profiles app.
5. Register profiles in INSTALLED_APPS.
6. Run check and inspect each generated file.

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

- [ ] The command prompt shows the virtual environment is active.
- [ ] python -m django --version prints the pinned version.
- [ ] manage.py, config/ and profiles/ are siblings.
- [ ] profiles.apps.ProfilesConfig is present in INSTALLED_APPS.
- [ ] python manage.py check reports no issues.

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
I am a beginner learning Django. Help me plan Personal Profile Django Project.
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
I am working on Personal Profile Django Project.
My current directory is: [paste path]
My command is: [paste exact command]
My file contents are: [paste relevant file]
My complete error is: [paste traceback]
Explain the likely cause and the smallest safe correction.
Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Question 1

What is a Django project?

- A. The overall site configuration and collection of apps
- B. A database table
- C. A single HTML page
- D. A Python variable

**Correct answer: A** — The project contains site-wide configuration and coordinates the installed apps.

### Question 2

What does the final dot in startproject config . mean?

- A. Delete the folder
- B. Create the project in the current directory
- C. Install Django globally
- D. Create a database row

**Correct answer: B** — The dot is the current working directory; it avoids an extra nested folder.

### Question 3

Which file is the project-specific command entry point?

- A. models.py
- B. admin.py
- C. manage.py
- D. apps.py

**Correct answer: C** — manage.py loads project settings and exposes Django management commands.

### Question 4

Where do you register a new app?

- A. INSTALLED_APPS in settings.py
- B. In README only
- C. In templates
- D. In migrations only

**Correct answer: A** — Django loads configured applications through INSTALLED_APPS.

### Question 5

Does creating an app automatically create a database table?

- A. Yes, always
- B. Only on Windows
- C. Only when runserver starts
- D. No; define models and apply migrations

**Correct answer: D** — An app folder is not a database schema. Models and migrations are needed.

## 16. Interview preparation

### Question 1 — Explain today's topic
**Answer:** Think of a Django project as the whole website and an app as one feature area inside it. A college portal might have separate apps for profiles, courses, attendance and fees. Each app owns a related set of models, views, templates and tests. The project package owns site-wide configuration and root URL routing. A project may contain many apps; an app is not a separate server by default.

**Follow-up:** Explain the same concept using the Student Portal project.

### Question 2 — Which files are involved?
**Answer:** `manage.py`, `config/__init__.py`, `config/settings.py`, `config/urls.py`, `config/asgi.py`, `config/wsgi.py`, `profiles/apps.py`, `profiles/models.py`, `profiles/views.py`, `profiles/admin.py`, `profiles/tests.py`, `profiles/migrations/`. Explain what each file owns and how the files connect.

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
- [ ] I completed **Personal Profile Django Project**.
- [ ] I submitted source files and evidence.
- [ ] I answered the interview questions and reviewed the MCQs.

## 18. Trainer validation

Do not mark the day complete just because code exists. Ask the student to:
1. Demonstrate the feature.
2. Explain the flow.
3. Change one small part independently.
4. Predict the result before running.
5. Diagnose one controlled mistake.

**Next lesson:** Day 29 — Django Development Server, settings.py and Installed Applications
