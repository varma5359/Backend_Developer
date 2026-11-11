# Day 33: Interview Guide — Template Inheritance, Reusable Components and Static Files

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 33 notes](day_33_notes.md)  
**Mini-project:** Reusable Website Layout

## 1. Technical questions with model answers

### Q1. Why use template inheritance?

**Model answer:** It lets child templates reuse a shared base layout. The base defines blocks, and child templates override those blocks instead of duplicating the whole HTML page.

### Q2. What does extends do?

**Model answer:** It declares the parent template that a child template inherits from. It should appear before other template content in the child.

### Q3. What does block do?

**Model answer:** It marks a named region in the base template that a child template can replace or extend.

### Q4. What is the difference between include and extends?

**Model answer:** extends reuses a page layout through inheritance. include inserts a reusable template fragment, such as a navigation component.

### Q5. How does Django serve static files during development?

**Model answer:** The template loads the static tag library and references a static asset with {% static '...' %}. STATIC_URL defines the URL prefix. Production static files require a separate collection/serving strategy.

### Q6. How do you debug CSS that is not loading?

**Model answer:** Inspect the rendered link URL, confirm the file path and static directory, check STATIC_URL and browser Network tab status, and read the runserver output.

## 2. Scenario-based interview question

**Scenario:** The HTML page loads but has no styling. What is the most reliable debugging sequence?

**Model answer:** Inspect the browser Network tab for the CSS request and status code, copy the requested path, verify the file exists in the configured static directory, confirm {% load static %} and the static tag path, then check settings. Do not assume a CSS problem is caused by the template layout.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Create a base template, define navigation and content blocks, extend it from two child pages, include a reusable component, add a CSS file and verify both pages plus the CSS request.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Reusable Website Layout

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
- [ ] I can present Reusable Website Layout with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is template inheritance?
**Answer:** It lets child templates reuse a base layout and override named blocks.

### Q6. What is the difference between extends and include?
**Answer:** extends inherits a page layout. include inserts a reusable template fragment.

### Q7. What does block.super do?
**Answer:** It includes the parent block content inside an overridden child block.

### Q8. What are static files?
**Answer:** Application assets such as CSS, JavaScript, logos and icons.

### Q9. What does collectstatic do?
**Answer:** It gathers static files into STATIC_ROOT for a deployment workflow.

### Q10. What is the difference between static and media?
**Answer:** Static files belong to the application. Media files are uploaded by users.

### Q11. Scenario: CSS returns 404.
**Answer:** Check static folder nesting, app registration, static tag path and browser network request.

### Q12. Scenario: CSS works locally but not after deployment.
**Answer:** Check collectstatic, STATIC_ROOT and the production static-file serving configuration.

