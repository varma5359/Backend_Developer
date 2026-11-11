# Day 27: Interview Guide — Introduction to Django, Features, Architecture and Installation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 27 notes](day_27_notes.md)  
**Mini-project:** Django Environment Setup

## 1. Technical questions with model answers

### Q1. What is Django?

**Model answer:** Django is a high-level Python web framework. It supplies common web-application components such as URL routing, views, templates, ORM, forms, authentication and security protections. It does not remove the need to understand HTTP, databases or Python.

### Q2. Explain Django's request-response flow.

**Model answer:** A browser sends an HTTP request. Django middleware processes it. The URL resolver selects a view. The view runs application logic and may query the ORM or render a template. Django returns an HTTP response to the browser.

### Q3. What is the difference between a project and an app?

**Model answer:** A project contains site-wide configuration and URL entry points. An app groups a feature or domain, such as profiles or billing. One project can contain multiple apps.

### Q4. Why use a virtual environment?

**Model answer:** It isolates project dependencies from other Python projects. This makes versions reproducible and reduces conflicts.

### Q5. What is the purpose of manage.py?

**Model answer:** It is the project's command-line utility. It sets the Django settings module and exposes management commands such as check, runserver, migrate and createsuperuser.

### Q6. Why is runserver not a production server?

**Model answer:** It is intended for local development and debugging. Production needs a suitable WSGI or ASGI server, secure settings, static-file handling, monitoring and deployment configuration.

## 2. Scenario-based interview question

**Scenario:** A beginner installs Django globally, then the project cannot import it in VS Code. Explain how you would debug it.

**Model answer:** Check which interpreter VS Code selected, activate the project's virtual environment, run python -m pip show django and python -c "import sys; print(sys.executable)" in the same terminal. Install the required version using that interpreter, then rerun the import and manage.py check.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Explain the purpose of the framework, draw the request flow, create and activate .venv, install the pinned Django version, verify the interpreter and Django version, and write reproducible setup commands in README.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Django Environment Setup

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Django Environment Setup with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding section in [Day 27 class notes](day_27_notes.md), repeat the steps and record the output.
## Additional technical and scenario questions

### Q7. What problem does a web framework solve?
**Answer:** A framework provides reusable structure and common capabilities so developers do not need to build routing, request handling, configuration and other repeated web concerns from scratch.

### Q8. What is Django's MVT pattern?
**Answer:** Model represents data, View handles request logic, and Template presents the response. The URL dispatcher connects a requested path to a view.

### Q9. What happens during a Django request?
**Answer:** The request passes through middleware, URL resolution selects a view, the view performs required work, a response is created and response middleware runs before the browser receives it.

### Q10. Why use a virtual environment?
**Answer:** It isolates project dependencies so one project's Django version and packages do not interfere with another project's environment.

### Q11. Why pin the Django version?
**Answer:** A pinned version makes the learning environment reproducible. All learners can follow the same commands and examples.

### Q12. Is runserver suitable for production?
**Answer:** No. It is a development server. Production requires a properly configured application server, web server or hosting platform and production security settings.

### Q13. Scenario: Django installs globally but not inside VS Code.
**Answer:** Check which Python interpreter VS Code uses, activate the project virtual environment and run python -m django --version from the same terminal.

### Q14. Scenario: a beginner says Django is a programming language.
**Answer:** Django is a Python web framework. Python is the programming language; Django provides reusable web application structure and tools.

