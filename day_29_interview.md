# Day 29: Interview Guide — Django Development Server, settings.py and Installed Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 29 notes](day_29_notes.md)  
**Mini-project:** Django Configuration Explorer

## 1. Technical questions with model answers

### Q1. What is settings.py?

**Model answer:** It is the project's configuration module. It defines installed apps, middleware, URL configuration, templates, database, static files, security settings and other project-wide options.

### Q2. What does INSTALLED_APPS control?

**Model answer:** It lists Django and third-party/local apps that Django should load. App registration enables features such as model discovery and migrations.

### Q3. What is middleware?

**Model answer:** Middleware is a request/response processing layer. Middleware components can inspect or modify requests before the view and responses after the view.

### Q4. What does DEBUG=True mean?

**Model answer:** It enables detailed development diagnostics. It must not be enabled in production because error pages can reveal sensitive implementation details.

### Q5. What is ALLOWED_HOSTS?

**Model answer:** It lists host/domain values that Django accepts for the Host header when DEBUG is False. It is not a substitute for network security.

### Q6. How do you run the development server on another port?

**Model answer:** Use python manage.py runserver 8001. The server listens on the selected local development port until stopped with Ctrl+C.

## 2. Scenario-based interview question

**Scenario:** The project runs locally but a developer wants to deploy it with DEBUG=True and ALLOWED_HOSTS=['*']. Explain the risk and safer approach.

**Model answer:** DEBUG can expose detailed tracebacks and configuration information. A wildcard host setting is overly broad. Use environment-specific settings, DEBUG=False in production, an explicit host list, protected SECRET_KEY and production server configuration.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Inspect each required setting, run check, start the server, open the local page, test a second port, stop with Ctrl+C and explain which settings must change before deployment.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Django Configuration Explorer

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
- [ ] I can present Django Configuration Explorer with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding section in [Day 29 class notes](day_29_notes.md), repeat the steps and record the output.