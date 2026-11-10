# Day 29: Interview Questions — Django Development Server, settings.py and Installed Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 29 notes](day_29_notes.md)  
**Approved mini-project:** Django Configuration Explorer

## 1. Core technical questions

### Q1. Explain django development server, settings.py and installed applications.
**Answer:** Django settings configure installed apps, middleware, database connections, templates, static files, security and other project behavior. Configuration should be environment-aware and secrets should not be committed to Git.

**Follow-up:** Give one example from a Django project.

### Q2. Why is this concept important for a backend developer?
**Answer:** It helps a developer build, configure, understand or troubleshoot a Django application. Explain the practical example from the class notes rather than giving only a definition.

### Q3. Which command or file is important in this lesson?
**Answer:** Identify the relevant command or file from the lesson. Explain where it belongs, what it does and how you verified it.

### Q4. What is one common beginner mistake?
**Answer:** A common mistake is skipping environment, folder or configuration checks. Read the complete error and verify one step at a time.

### Q5. How would you verify the result?
**Answer:** Run the command, check Django's system output and verify the browser or application behavior. Capture reproducible evidence.

## 2. Scenario-based question

**Scenario:** A junior developer is completing Django Configuration Explorer. The command appears to work, but the expected application result is not visible.

**Suggested answer:**
1. Confirm the active virtual environment.
2. Confirm the current project directory.
3. Check the command and file names.
4. Read the full error or server output.
5. Verify the expected file or setting.
6. Rerun the system check.
7. Verify the result in the browser or terminal.

**Follow-up:** What evidence would you provide to another developer?

## 3. Practical discussion

Be prepared to:
- Explain the purpose of each command.
- Identify the relevant Django file.
- Explain why the configuration is needed.
- Demonstrate a successful run.
- Describe one error and its fix.
- Explain one production consideration.

## 4. Mini-project viva — Django Configuration Explorer

1. What was the objective?
2. What prerequisites did you need?
3. Which commands did you execute?
4. Which files did Django create or use?
5. How did you verify the result?
6. What error did you encounter, if any?
7. How did you solve it?
8. What is not included in this learning exercise?
9. What would you improve next?
10. How would you explain the project to a teammate?

## 5. Common incorrect answers

| Incorrect statement | Better answer |
|---|---|
| Django is a database | Django is a Python web framework |
| A successful command proves the full feature works | Verify the browser, configuration or application behavior |
| The development server is production-ready | Use a production deployment stack |
| All project settings are safe to publish | Keep secrets and environment-specific configuration protected |
| A Django project and app are identical | A project is the overall configuration; apps group features |

## 6. Rapid revision

- **Step 1:** Open config/settings.py.
- **Step 2:** Find INSTALLED_APPS and identify the built-in Django applications.
- **Step 3:** Add the profiles app created on Day 28.
- **Step 4:** Read DEBUG and ALLOWED_HOSTS and explain their development purpose.
- **Step 5:** Run python manage.py check.
- **Step 6:** Start the server and observe the result.
- **Step 7:** Record which settings should be changed for production.

## 7. Interview readiness checklist

- [ ] Explain the topic in simple language.
- [ ] Explain the main command and its output.
- [ ] Identify the relevant file or folder.
- [ ] Describe a common failure and how to debug it.
- [ ] Present Django Configuration Explorer and its evidence.
- [ ] Explain one production consideration.

**Trainer note:** Ask the learner to explain the command and file locations without looking at the notes. If they cannot, ask them to rerun the demonstration and explain each step.
