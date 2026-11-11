# Day 33: Interview Guide — Template Inheritance, Reusable Components and Static Files

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 33 notes](day_33_notes.md)  
**Approved mini-project:** Reusable Website Layout

## 1. Core technical questions

### Q1. Explain today's concept.
**Answer:** Most pages on a website share a header, navigation, footer and overall layout. Copying the same HTML into every page creates duplication. Template inheritance lets one base template define the shared layout while child templates provide page-specific content. Static files such as CSS, JavaScript and logos are application assets served separately from templates.

**Follow-up:** Explain how this concept appears in the Student Portal.

### Q2. Which files or commands are involved?
**Answer:** `profiles/templates/profiles/base.html`, `profiles/templates/profiles/home.html`, `profiles/templates/profiles/about.html`, `profiles/static/profiles/css/site.css`, `profiles/views.py`, `profiles/urls.py`. Explain what each one is responsible for and how they connect.

**Follow-up:** What error might occur if a file is missing or incorrectly configured?

### Q3. What does Django do automatically, and what must the developer write?
**Answer:** Django supplies framework mechanisms and conventions. The developer defines the application's requirements, configuration, business rules, correct file connections and tests.

### Q4. How do you verify your work?
**Answer:** Run `python manage.py check`, execute the relevant commands, inspect the output and test the actual browser/database behavior. Include an edge case.

## 2. Scenario-based questions

### Q5. The feature does not work even though the code is present. What do you inspect?
**Suggested answer:**
1. Reproduce the problem.
2. Read the complete error.
3. Check the current folder and Python environment.
4. Inspect the named file and nearby lines.
5. Check imports, app registration, URL patterns and file paths.
6. Run Django checks.
7. Repeat the actual test.

### Q6. A learner says the command succeeded, so the task is complete. Is that enough?
**Suggested answer:** No. A command may create a file or run a server without proving the expected feature works. Demonstrate the result, test an edge case and explain the implementation.

### Q7. How would you explain this work to a teammate?
**Suggested answer:** Describe the requirement, relevant files, command sequence, execution flow, expected output, tests and one error/fix.

## 3. Practical discussion

Be prepared to:
- Identify the exact file path.
- Explain important code statements.
- Demonstrate the required commands.
- Explain the observed result.
- Modify one small part and predict the effect.
- Test a normal and edge case.
- Describe a safe debugging method.

## 4. Mini-project viva — Reusable Website Layout

1. What problem does the project solve?
2. What are the functional requirements?
3. Which files did you create or update?
4. Which commands did you run?
5. What does the important code do?
6. How did you verify the normal case?
7. Which edge case did you test?
8. What error did you encounter?
9. How did you fix it?
10. What would you improve next?

## 5. Rapid revision

- Define the concept.
- Name the important files.
- Explain the execution flow.
- Demonstrate the project.
- Run checks.
- Explain one failure and its fix.

## 6. Readiness checklist

- [ ] I can explain the concept clearly.
- [ ] I can identify the relevant files.
- [ ] I can reproduce the example.
- [ ] I can explain the important code.
- [ ] I can verify the result.
- [ ] I can answer a scenario question.
- [ ] I can present Reusable Website Layout independently.

**Self-practice:** Explain why a step is needed and predict what changes when one value or setting is modified.
