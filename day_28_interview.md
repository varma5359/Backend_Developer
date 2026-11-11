# Day 28: Interview Guide — Creating Django Projects and Applications, Project Structure and manage.py

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 28 notes](day_28_notes.md)  
**Mini-project:** Personal Profile Django Project

## 1. Technical questions with model answers

### Q1. What does startproject create?

**Model answer:** It creates the project package and manage.py. The package includes settings, root URLs, ASGI and WSGI entry points.

### Q2. What does startapp create?

**Model answer:** It creates an app package with files such as models.py, views.py, admin.py, apps.py, tests.py and migrations/.

### Q3. Why use django-admin startproject config .?

**Model answer:** The dot tells Django to create the project package in the current directory instead of nesting another project folder.

### Q4. Why add profiles to INSTALLED_APPS?

**Model answer:** Django must load the app so it can discover its models, admin integration, migrations and app configuration.

### Q5. What is the role of apps.py?

**Model answer:** It contains the AppConfig class, which describes the app and can define startup configuration.

### Q6. Why should .venv and secrets not be committed?

**Model answer:** The virtual environment is machine-specific generated dependency state. Secrets such as passwords and API keys must remain private; commit a safe example configuration instead.

## 2. Scenario-based interview question

**Scenario:** The runserver command says no module named profiles after the app folder was created. What do you check?

**Model answer:** Confirm the app folder is beside manage.py, the package contains apps.py and __init__.py, the app name is correctly listed in INSTALLED_APPS, and the command is being run from the project root with the correct environment.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Create the project in the intended workspace, create profiles, inspect the file tree, register the app, run check, and explain the purpose of manage.py and the config package.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Personal Profile Django Project

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
- [ ] I can present Personal Profile Django Project with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding section in [Day 28 class notes](day_28_notes.md), repeat the steps and record the output.