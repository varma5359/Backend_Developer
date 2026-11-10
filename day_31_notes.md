# Day 31: Django Views: Function-Based Views and Request-Response Cycle

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours  
**Level:** Beginner  
**Prerequisites:** Day 27 Django introduction and environment setup; Python, OOP and HTTP foundations from earlier phases  
**Tools:** Windows 10/11, Python, VS Code, PowerShell, Django 5.2.19 and browser  
**Project continuity:** `student_portal` project, `config` project package, `profiles` application  
**Approved independent mini-project:** Dynamic Welcome Application

> **Teaching instruction:** Read the explanation before typing. Run commands one at a time. Use the exact filenames. Compare your result with the expected behavior. Do not move on while an earlier step is broken.

---

## 1. What you will learn

1. Define a function-based view and explain HttpRequest and HttpResponse.
2. Read query parameters and request methods.
3. Render a template using a context dictionary.
4. Trace the request-response lifecycle through a view.

## 2. Why this topic exists

A view is a Python callable that receives an HttpRequest and returns an HttpResponse (or another compatible response). A function-based view is an ordinary Python function with a request parameter. Django selects the view through URL routing. The view decides what work to perform and what response to return.

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

- `profiles/views.py`
- `profiles/urls.py`
- `profiles/templates/profiles/welcome.html`

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
# Open:
# http://127.0.0.1:8000/welcome/
# http://127.0.0.1:8000/welcome/?name=Asha
# http://127.0.0.1:8000/request-info/
```

### Understand every command

### Step 1 — `Import HttpResponse`

It constructs a basic HTTP response whose content is sent to the browser.

### Step 2 — `Import render`

render loads a template, supplies context and returns an HttpResponse containing rendered output.

### Step 3 — `Define welcome(request)`

Django passes the current HttpRequest as the first argument when this route matches.

### Step 4 — `Read request.GET`

Query-string parameters are a QueryDict. get('name', 'Student') returns the supplied name or a default.

### Step 5 — `Build context`

A context dictionary passes Python data to the template. The key student_name becomes the template variable.

### Step 6 — `Return render(...)`

The request, template path and context are provided. The rendered HTML becomes the response.

### Step 7 — `Read request.method`

This property contains the HTTP method such as GET or POST.

### Step 8 — `Connect the URL`

A view is not reachable until a URL pattern points to it.

## 7. Main implementation

### Code to create or update

Use the filenames identified in Section 4. The following code is the lesson's working demonstration:

```python
# profiles/views.py
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    name = request.GET.get("name", "Student")
    context = {"student_name": name}
    return render(request, "profiles/welcome.html", context)

def request_info(request):
    return HttpResponse(f"HTTP method: {request.method}")

def plain_text(request):
    return HttpResponse("This text is sent to the browser.")

# profiles/urls.py — add to urlpatterns
path("welcome/", views.welcome, name="welcome"),
path("request-info/", views.request_info, name="request_info"),
path("plain-text/", views.plain_text, name="plain_text"),

<!-- profiles/templates/profiles/welcome.html -->
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Welcome</title></head>
<body>
    <h1>Welcome, {{ student_name }}</h1>
    <p>Your Django view passed this value to the template.</p>
</body>
</html>
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

### What is HttpRequest?
Django constructs an HttpRequest for each incoming request. It exposes method, path, query parameters, POST data, headers, cookies and authenticated user information. Treat user-provided values as untrusted until validated.

### What is HttpResponse?
HttpResponse represents the server's response to the browser. It includes content, a status code and headers. A normal HttpResponse defaults to status 200.

### Why does a view return a response?
Django needs a response object to send back through the middleware chain to the client. Printing text writes to the server terminal; it does not create a browser response.

### GET and POST
GET is commonly used to retrieve a page or resource. POST is commonly used to submit data that changes server state. Do not perform destructive actions in GET requests. Form handling is taught later.

### QueryDict
request.GET stores query parameters. `request.GET.get("name", "Student")` retrieves one value and uses a default if missing. The browser controls this input, so validate or normalize it before using it in business logic.

### render shortcut
`render(request, template_name, context)` is a shortcut that loads a template, renders it and returns an HttpResponse. It does not save database data.

### Request-response lifecycle
Browser → middleware request processing → URL resolver → view → optional model/form/template work → response → middleware response processing → browser. The exact components depend on the request.

### Status codes
A view may return a normal 200 response, a redirect, a 404 response or another status. Use meaningful HTTP status codes rather than always returning a generic message.

### View design
A view coordinates one request. Keep it readable. Avoid putting unrelated workflows and all business rules into one enormous function. Reusable business operations can be moved into dedicated functions or service modules when complexity grows.

### Troubleshooting
- View returns nothing: ensure every execution path returns an HttpResponse.
- Template missing: check exact template path and app registration.
- Query value missing: inspect URL and request.GET.
- Route not found: check app urls and root include.
- Import error: check function spelling and relative imports.

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

- [ ] Each view returns a response.
- [ ] Missing name uses the default value.
- [ ] Supplied name appears in the rendered page.
- [ ] request.method displays GET for normal browser navigation.
- [ ] The learner explains print versus HttpResponse.
- [ ] The learner traces the full request-response path.

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

## 13. Approved mini-project — Dynamic Welcome Application

### Problem statement

Build a small practical demonstration of today's topic inside the Student Portal workspace. The objective is not to copy a tutorial. The learner must be able to explain and reproduce the implementation.

### Functional requirements

1. Create welcome, request_info and plain_text views.
2. Add the URL patterns.
3. Create welcome.html at the exact path.
4. Open the welcome page without a name and confirm Student appears.
5. Add ?name=Asha and confirm Asha appears.
6. Open request-info and explain why the browser request is GET.

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

- [ ] Each view returns a response.
- [ ] Missing name uses the default value.
- [ ] Supplied name appears in the rendered page.
- [ ] request.method displays GET for normal browser navigation.
- [ ] The learner explains print versus HttpResponse.
- [ ] The learner traces the full request-response path.

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
I am a beginner learning Django. Help me plan Dynamic Welcome Application.
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
I am working on Dynamic Welcome Application.
My current directory is: [paste path]
My command is: [paste exact command]
My file contents are: [paste relevant file]
My complete error is: [paste traceback]
Explain the likely cause and the smallest safe correction.
Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Question 1

What must a Django view normally return?

- A. A database model class
- B. An HttpResponse or compatible response
- C. A print statement
- D. A URL pattern list

**Correct answer: B** — The view must return a response object for Django to send to the client.

### Question 2

Where does a query parameter such as ?name=Asha appear?

- A. request.GET
- B. request.POST
- C. request.user
- D. settings.py

**Correct answer: A** — Query-string values are read through request.GET.

### Question 3

What does render() do?

- A. Creates a database table
- B. Loads a template, supplies context and returns a response
- C. Starts a server
- D. Registers a model

**Correct answer: B** — render combines a template with context and returns an HttpResponse.

### Question 4

Why does print('Hello') not display the text in the browser?

- A. Python cannot print strings
- B. print sends output to the database
- C. print writes to the server terminal, not the HTTP response
- D. Django disables print

**Correct answer: C** — Browser output must be included in a returned HTTP response.

### Question 5

What does request.method contain?

- A. The URL route name
- B. The current HTTP method
- C. The database engine
- D. The logged-in user's password

**Correct answer: B** — It indicates methods such as GET or POST.

## 16. Interview preparation

### Question 1 — Explain today's topic
**Answer:** A view is a Python callable that receives an HttpRequest and returns an HttpResponse (or another compatible response). A function-based view is an ordinary Python function with a request parameter. Django selects the view through URL routing. The view decides what work to perform and what response to return.

**Follow-up:** Explain the same concept using the Student Portal project.

### Question 2 — Which files are involved?
**Answer:** `profiles/views.py`, `profiles/urls.py`, `profiles/templates/profiles/welcome.html`. Explain what each file owns and how the files connect.

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
- [ ] I completed **Dynamic Welcome Application**.
- [ ] I submitted source files and evidence.
- [ ] I answered the interview questions and reviewed the MCQs.

## 18. Trainer validation

Do not mark the day complete just because code exists. Ask the student to:
1. Demonstrate the feature.
2. Explain the flow.
3. Change one small part independently.
4. Predict the result before running.
5. Diagnose one controlled mistake.

**Next lesson:** Day 32 — Django Templates, Template Variables and Template Tags
