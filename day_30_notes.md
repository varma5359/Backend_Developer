# Day 30: URL Routing, Path Converters and URL Patterns

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours  
**Level:** Beginner  
**Prerequisites:** Day 27 Django introduction and environment setup; Python, OOP and HTTP foundations from earlier phases  
**Tools:** Windows 10/11, Python, VS Code, PowerShell, Django 5.2.19 and browser  
**Project continuity:** `student_portal` project, `config` project package, `profiles` application  
**Approved independent mini-project:** Multi-Page Routing Application

> **Teaching instruction:** Read the explanation before typing. Run commands one at a time. Use the exact filenames. Compare your result with the expected behavior. Do not move on while an earlier step is broken.

---

## 1. What you will learn

1. Explain how Django resolves a requested URL.
2. Create app-level URL patterns and include them in the project router.
3. Use path converters to capture values.
4. Use route names to reverse URLs safely.

## 2. Why this topic exists

A URL is an address requested by the browser. Django's URL dispatcher checks configured patterns in order. When a pattern matches, Django calls its view and passes captured path values as arguments. The project URL file is the main entry point; an app can own its own routes so the project does not become one huge file.

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

- `config/urls.py`
- `profiles/urls.py (create this file)`
- `profiles/views.py`

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
# Test:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about/
# http://127.0.0.1:8000/profile/25/
# http://127.0.0.1:8000/member/asha/
```

### Understand every command

### Step 1 — `Create profiles/urls.py`

Django creates views.py but does not create app-level urls.py automatically. Create the file beside views.py.

### Step 2 — `Import path and views`

path creates a route. The relative import . means import from the current profiles package.

### Step 3 — `Create urlpatterns`

Django expects the conventional variable urlpatterns to be a list of URL patterns.

### Step 4 — `Add the integer converter`

<int:profile_id> captures a positive integer from the URL and passes it to the view using the keyword profile_id.

### Step 5 — `Add the string converter`

<str:username> captures a non-empty path segment that does not contain a slash.

### Step 6 — `Include app routes in config/urls.py`

include delegates the remaining URL path to profiles.urls. The app owns its feature routes.

### Step 7 — `Run the server and test paths`

The browser path is matched by Django; the selected view returns the response.

## 7. Main implementation

### Code to create or update

Use the filenames identified in Section 4. The following code is the lesson's working demonstration:

```python
# profiles/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def about(request):
    return HttpResponse("About page")

def profile_detail(request, profile_id):
    return HttpResponse(f"Profile ID: {profile_id}")

def member_detail(request, username):
    return HttpResponse(f"Member: {username}")

# profiles/urls.py — create this file
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/<int:profile_id>/", views.profile_detail, name="profile_detail"),
    path("member/<str:username>/", views.member_detail, name="member_detail"),
]

# config/urls.py — root URL configuration
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
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

### Trace one request
When the browser requests `/profile/25/`:
1. Django receives the HTTP request.
2. The root URL configuration checks its patterns.
3. The empty prefix includes profiles.urls.
4. Django checks app patterns.
5. The int converter captures 25 and converts it to an integer.
6. Django calls profile_detail(request, profile_id=25).
7. The view returns an HttpResponse.
8. The browser displays the response content.

### Path converters
- `str`: non-empty segment excluding slash; default converter when no converter is supplied.
- `int`: positive integer.
- `slug`: letters, numbers, hyphens and underscores.
- `uuid`: UUID formatted value.
- `path`: captures a path including slash characters.

### Path versus query string
In `/search/?q=django`, `/search/` is the path. `q=django` is query-string data. Path converters capture values in the path; query parameters are read from `request.GET`.

### Route ordering
Django checks patterns in order and selects the first match. Put specific patterns before broad catch-all patterns where they could overlap. A broad string or path converter placed too early may capture a route intended for a more specific view.

### Route names and reverse lookup
A route name such as `home` lets templates use `{% url 'home' %}` and Python use `reverse("home")`. If the literal path changes but the route name remains, links generated through reverse lookup can still work.

### Trailing slash
Django projects commonly use trailing slashes in routes. Be consistent. CommonMiddleware may redirect in some configurations, but do not rely on automatic redirects as a substitute for defining the intended route.

### 404 is not a crash
If no URL pattern matches, Django returns a 404 response. A missing route is different from an import error, syntax error or database failure.

### Namespaces (preview)
Larger projects can use app_name and include namespaces to avoid route-name collisions. We will introduce namespaces when the project has enough apps to need them.

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

- [ ] Root path returns Home page.
- [ ] /about/ returns About page.
- [ ] /profile/25/ passes integer 25.
- [ ] /member/asha/ passes string asha.
- [ ] An unknown path returns 404.
- [ ] The learner explains the root-to-app URL routing chain.

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

## 13. Approved mini-project — Multi-Page Routing Application

### Problem statement

Build a small practical demonstration of today's topic inside the Student Portal workspace. The objective is not to copy a tutorial. The learner must be able to explain and reproduce the implementation.

### Functional requirements

1. Create the four view functions shown.
2. Create profiles/urls.py and connect each route to its view.
3. Include profiles.urls in config/urls.py.
4. Visit each URL and record the returned text.
5. Change /profile/25/ to /profile/abc/ and observe that the int converter does not match.
6. Add one unknown URL and observe the 404 response.

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
10. Write a short explanation of the code and result in your own words. Compare it with the expected behavior in this lesson.

### Acceptance criteria

- [ ] Root path returns Home page.
- [ ] /about/ returns About page.
- [ ] /profile/25/ passes integer 25.
- [ ] /member/asha/ passes string asha.
- [ ] An unknown path returns 404.
- [ ] The learner explains the root-to-app URL routing chain.

### Submission evidence

- Source files changed for this project.
- Terminal output from checks and commands.
- Browser screenshots or observed URLs, where applicable.
- A short README containing setup and verification steps.
- A short explanation of one error and its resolution.

### Optional extension

Change one small behavior and predict the result before running it. Do not introduce concepts that belong to later lessons.

## 14. AI-assisted implementation guide

First attempt each step using the lesson. If you are still stuck, an optional AI learning assistant can give hints; it must not replace your own implementation and verification.

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
I am a beginner learning Django. Help me plan Multi-Page Routing Application.
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
I am working on Multi-Page Routing Application.
My current directory is: [paste path]
My command is: [paste exact command]
My file contents are: [paste relevant file]
My complete error is: [paste traceback]
Explain the likely cause and the smallest safe correction.
Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Question 1

Which variable does Django inspect for URL patterns?

- A. routes
- B. urlpatterns
- C. url_list
- D. views

**Correct answer: B** — Django uses the conventional urlpatterns variable in a URLconf.

### Question 2

What does <int:student_id> do?

- A. Captures and converts a path segment to an integer
- B. Reads a query string
- C. Creates a database primary key
- D. Validates an email

**Correct answer: A** — The converter matches an integer path segment and passes it as a keyword argument.

### Question 3

What does include('profiles.urls') do?

- A. Copies all views into settings
- B. Delegates route matching to the app URLconf
- C. Creates a template
- D. Starts runserver

**Correct answer: B** — The project URLconf includes the app URLconf under its prefix.

### Question 4

In /search/?q=django, where is q stored?

- A. request.path
- B. request.POST
- C. request.GET
- D. request.user

**Correct answer: C** — Query-string parameters are available through request.GET.

### Question 5

What does an unmatched URL normally produce?

- A. A 404 response
- B. A successful database insert
- C. A 500 always
- D. A new app

**Correct answer: A** — No configured URL pattern matched the requested path.

## 16. Interview preparation

### Question 1 — Explain today's topic
**Answer:** A URL is an address requested by the browser. Django's URL dispatcher checks configured patterns in order. When a pattern matches, Django calls its view and passes captured path values as arguments. The project URL file is the main entry point; an app can own its own routes so the project does not become one huge file.

**Follow-up:** Explain the same concept using the Student Portal project.

### Question 2 — Which files are involved?
**Answer:** `config/urls.py`, `profiles/urls.py (create this file)`, `profiles/views.py`. Explain what each file owns and how the files connect.

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
- [ ] I completed **Multi-Page Routing Application**.
- [ ] I submitted source files and evidence.
- [ ] I answered the interview questions and reviewed the MCQs.

## 18. Independent completion test

Do not mark the day complete just because code exists. Complete every check yourself:
1. Demonstrate the feature in the browser or terminal.
2. Explain the request or execution flow without reading the notes.
3. Change one small part independently.
4. Predict the result before running the change, then compare your prediction.
5. Diagnose and fix one controlled mistake, such as a misspelled URL, setting or file path.

**Next lesson:** Day 31 — Django Views: Function-Based Views and Request-Response Cycle
