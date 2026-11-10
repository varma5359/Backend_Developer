# Day 27: Introduction to Django, Features, Architecture and Installation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–26 — Python, OOP, web fundamentals, SQL and Git  
**Tools:** Python 3, VS Code, terminal, pip and Django  
**Approved mini-project:** Django Environment Setup

> **Trainer guidance:** Treat Django as a new framework, not as magic. Run every command from the correct folder, inspect the generated files and understand what each component does. Do not move to the next step until the current step works.

## 1. Learning objectives

By the end of this lesson, you should be able to:
- Explain introduction to django, features, architecture and installation.
- Identify the role of the main Django components introduced today.
- Run the commands in the correct order.
- Interpret the expected output.
- Troubleshoot a common setup or configuration error.
- Complete Django Environment Setup and explain the result.

## 2. Concept introduction

Django is a high-level Python web framework. It provides URL routing, views, templates, an ORM, forms, authentication and security features. It helps developers build web applications without writing every common web feature from scratch.

### Why backend developers use Django

- It provides a structured way to build web applications.
- It includes URL routing and request/response handling.
- It provides an ORM to work with relational databases through Python objects.
- It includes a template system for server-rendered HTML.
- It provides forms, authentication, sessions and security protections.
- It encourages reusable applications and clear project structure.

Django does not remove the need to understand Python, HTTP, SQL, security or testing. It gives you a framework in which to apply those skills.

## 3. Understand the request-response architecture

```text
Browser → HTTP request → URL dispatcher → view → optional model/database → response or rendered template → browser
```

A browser sends an HTTP request. Django uses URL configuration to locate the view that should handle the request. The view performs the required work and returns an HTTP response. It may use a model/database or render a template.

## 4. Prepare your workspace

1. Open VS Code.
2. Open the project folder, not an unrelated parent folder.
3. Open Terminal → New Terminal.
4. Confirm your current folder with `pwd` in Git Bash or `Get-Location` in PowerShell.
5. Activate the intended virtual environment.
6. Run `python --version`.
7. Run the Django command shown below.

**Important:** If your terminal uses Windows PowerShell, activation normally uses `.venv\Scripts\Activate.ps1`. If PowerShell blocks script execution, follow your machine's approved policy rather than running unknown scripts.

## 5. Main demonstration

Save the relevant commands or code in your project notes. Execute the following commands one at a time:

```bash
# Create a virtual environment (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install Django
python -m pip install django

# Verify installation
python -m django --version
```

### Expected result

A Django version number is displayed after installation.

### Line-by-line explanation

1. python -m venv .venv creates an isolated Python environment in the project folder.
2. The PowerShell activation command activates that environment for the current terminal session.
3. python -m pip install django installs Django into the active environment.
4. python -m django --version confirms that the Django package can be imported and reports its version.

## 6. Important terminology

| Term | Meaning |
|---|---|
| Django project | Overall website configuration and collection of applications |
| Django application | Reusable component that provides a feature |
| Virtual environment | Isolated Python package environment |
| manage.py | Project-specific command-line utility |
| settings.py | Project configuration module |
| urls.py | URL routing configuration |
| View | Python code that handles a request and returns a response |
| Development server | Local server used during development |

## 7. Verify your environment or application

Use the following verification sequence:
1. Confirm the command runs from the intended project folder.
2. Confirm the virtual environment is active.
3. Confirm Django is installed in that environment.
4. Run the relevant Django system check.
5. Start the development server when applicable.
6. Open the local URL in a browser.
7. Record the exact output and any warnings.
8. Stop the development server with Ctrl+C when finished.

Do not report a feature as working just because a command was accepted. Verify the browser response or actual application behavior.

## 8. Common errors and troubleshooting

| Error or symptom | What to check |
|---|---|
| django-admin is not recognized | Activate the virtual environment and try python -m django |
| No module named django | Install Django into the active environment |
| No such file manage.py | Change to the Django project folder |
| Port already in use | Stop the other process or use another local port |
| App not found | Check app folder name and INSTALLED_APPS |
| System check reports an issue | Read the complete message and correct the named setting |
| Browser cannot connect | Confirm runserver is active and URL/port are correct |

### Debugging method

1. Read the final error message.
2. Identify the file and line number.
3. Check spelling and indentation.
4. Confirm the active Python interpreter.
5. Confirm the current working directory.
6. Correct one issue at a time.
7. Rerun the check and verify again.

## 9. Industry scenario

A company needs a backend website for employee information. Django provides a project structure and reusable applications. Developers can separate employee profiles, departments and authentication into different applications while sharing one project configuration.

## 10. When to use Django and what not to assume

- Use Django when you need a structured Python web application with database-backed features.
- Use Django applications to group related features.
- Use the development server only for local development.
- Do not expose DEBUG mode on production.
- Do not commit secret keys, database passwords or API tokens.
- Do not assume a generated project is already a complete business application.

## 11. Approved mini-project — Django Environment Setup

**Objective:** Django Environment Setup.

### Functional requirements

1. Check Python is installed with python --version.
2. Create a new project folder and open it in VS Code.
3. Create and activate a virtual environment.
4. Install Django using python -m pip install django.
5. Verify installation and record the installed version.
6. Create a short README with setup commands and troubleshooting notes.

### Suggested folder structure

```text
projects/day_27/
├── README.md
├── screenshots/
└── commands.txt
```

### Validation checklist

- [ ] python --version displays a supported Python version.
- [ ] The virtual environment is active in the terminal.
- [ ] python -m django --version works.
- [ ] Django is installed in the intended environment.
- [ ] The README contains repeatable setup instructions.

### Submission evidence

- Project folder or configuration files.
- Terminal output for each required command.
- Browser screenshot where a server is started.
- README with setup and verification steps.
- Short explanation of what each generated file or setting does.
- A troubleshooting note describing one issue and its resolution.

## 12. AI-assisted implementation guide

Use the AI mentor in small steps:
1. Ask for a plan, not a complete project.
2. Ask for the first command only.
3. Run the command and share the output.
4. Ask what the generated files mean.
5. Continue only after understanding the result.
6. Share exact errors when debugging.
7. Ask for a review against the validation checklist.

**Planning prompt:** "Help me plan Django Environment Setup. List the prerequisites, ordered tasks, files, commands and verification checks. Do not write the complete solution."

**Implementation prompt:** "Guide me one step at a time. Explain the purpose of the command or file and wait for my terminal output before continuing."

**Debugging prompt:** "Here is my exact command, folder structure and error. Identify the likely cause and the smallest safe correction."

## 13. Daily MCQs

**Q1. What is the main purpose of Django?**  
A. It is a Python web framework.  
B. It is a database engine only.  
C. It replaces Python.  
D. It is a browser.  
**Answer: A.** Django is a Python web framework.

**Q2. Why should a developer use a virtual environment?**  
A. To replace Git.  
B. To isolate project dependencies.  
C. To host a website publicly.  
D. To remove Python.  
**Answer: B.** It isolates installed packages for the project.

**Q3. What should you do if a Django command cannot import Django?**  
A. Delete Python.  
B. Ignore the message.  
C. Check the active environment and install Django there.  
D. Change the browser.  
**Answer: C.** The package must be installed in the environment used by the command.

**Q4. Is Django runserver the recommended production server?**  
A. Yes, for all workloads.  
B. Yes, if DEBUG is True.  
C. Only for database migrations.  
D. No, it is a development server.  
**Answer: D.** Use an appropriate production deployment stack.

**Q5. What is the best evidence that the setup task is complete?**  
A. Commands run successfully and the application or version is verified.  
B. A folder name only.  
C. A screenshot of an empty editor.  
D. A copied command list without execution.  
**Answer: A.** Completion requires observed and documented verification.

## 14. Interview preparation

**Q1. Explain introduction to django, features, architecture and installation.**  
**Answer:** Django is a high-level Python web framework. It provides URL routing, views, templates, an ORM, forms, authentication and security features. It helps developers build web applications without writing every common web feature from scratch.

**Q2. What is one important command or configuration introduced today?**  
**Answer:** Explain the command/configuration from the demonstration, its purpose and the expected result.

**Q3. What would you check if the setup did not work?**  
**Answer:** Check the active virtual environment, Python interpreter, current directory, installed packages, command spelling and complete error message.

**Follow-up:** Why is it important to understand the generated files rather than simply run commands?  
**Answer:** Backend developers must know where configuration and application behavior live so they can debug, extend and deploy the project safely.

## 15. Completion checklist

- [ ] Explain the main concepts without reading.
- [ ] Run all required commands.
- [ ] Verify the expected result.
- [ ] Explain the important files and settings.
- [ ] Complete Django Environment Setup.
- [ ] Test at least three relevant cases or checks.
- [ ] Complete all five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 28.
