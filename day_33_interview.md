# Day 33: Interview Questions — Template Inheritance, Reusable Components and Static Files

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 33 class notes](day_33_notes.md)  
**Approved mini-project:** Reusable Website Layout

## 1. Core technical questions

### Q1. Explain template inheritance, reusable components and static files.
**Answer:** Template inheritance lets child templates reuse a common base layout. A base template defines blocks that child templates fill. Static files are assets such as CSS, JavaScript and images; Django serves them during development when staticfiles is configured.

### Q2. Which files are involved?
**Answer:** profiles/templates/profiles/base.html, profiles/templates/profiles/home.html, profiles/static/profiles/css/site.css, profiles/views.py. Explain the responsibility of each file and how it connects to the rest of the Django application.

### Q3. Why is this feature important?
**Answer:** It helps keep application structure, presentation, data or schema changes understandable and maintainable.

### Q4. What is one common beginner mistake?
**Answer:** The child template extends the correct base template. Always verify the exact file path, configuration and command output.

### Q5. How do you verify the result?
**Answer:** Run Django's system check, execute the required command, inspect the browser or migration status and test an edge case.

## 2. Scenario-based questions

### Q6. A feature is missing from the browser or database. What do you check?
**Suggested answer:**
1. Verify the current project folder and active environment.
2. Inspect the relevant Django file.
3. Check app registration and settings.
4. Read the complete terminal error.
5. Run python manage.py check.
6. Correct one issue and verify again.

### Q7. Why should the learner understand the generated files?
**Suggested answer:** Generated files are part of the application structure. Understanding them helps the developer review changes, troubleshoot errors and collaborate safely.

## 3. Practical discussion

Be prepared to:
- Identify each relevant file.
- Explain the important configuration.
- Demonstrate the expected result.
- Explain one error and its resolution.
- Describe what should be committed to Git.
- Identify one production concern.

## 4. Mini-project viva — Reusable Website Layout

1. What problem does the project solve?
2. Which files did you create or update?
3. Why are those files located there?
4. Which command did you run?
5. How did you verify the result?
6. What error did you encounter?
7. How did you fix it?
8. What would you improve next?
9. What should not be committed to Git?
10. How would you explain the project to a teammate?

## 5. Rapid revision

- **1.** Create base.html with common HTML structure.
- **2.** Define title and content blocks in base.html.
- **3.** Create home.html and extend the base template.
- **4.** Override the title and content blocks.
- **5.** Create the app static folder and CSS file.
- **6.** Load static and use the static template tag for the CSS link.
- **7.** Open the page and verify that the shared layout and stylesheet load.

## 6. Readiness checklist

- [ ] Explain the concept in simple words.
- [ ] Identify the correct files.
- [ ] Explain the command or configuration.
- [ ] Demonstrate the mini-project.
- [ ] Explain one troubleshooting case.
- [ ] Answer follow-up questions.
