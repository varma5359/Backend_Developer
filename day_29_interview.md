# Day 29: Interview Guide — Django Development Server, settings.py and Installed Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 29 notes](day_29_notes.md)  
**Approved mini-project:** Django Configuration Explorer

## 1. Core technical questions

### Q1. What is the central purpose of this lesson?
**Answer:** Django needs configuration before it can load apps, middleware, databases and templates. The settings module tells Django which applications are active and how the project should behave. The development server is a local testing tool. It is deliberately not a production server.

**Follow-up:** Explain this using the Student Portal example.

### Q2. Which files are responsible for the implementation?
**Answer:** The files are config/settings.py, config/urls.py, profiles/apps.py. Describe the responsibility of each file, rather than only listing names.

**Follow-up:** Explain this using the Student Portal example.

### Q3. How would you verify the feature?
**Answer:** Run the required commands, inspect the output, test the browser behavior and verify an edge case. Use the exact checks in Day 29 class notes.

**Follow-up:** Explain this using the Student Portal example.

### Q4. What mistakes commonly affect beginners?
**Answer:** Common causes include an incorrect working directory, wrong Python environment, spelling errors, incorrect imports, a missing app registration or a route/file path mismatch. Read the traceback and correct one cause at a time.

**Follow-up:** Explain this using the Student Portal example.

## 2. Scenario-based questions

### Q5. The code exists, but the expected behavior is not visible. How do you debug it?
**Suggested answer:**
1. Reproduce the problem.
2. Read the complete error or terminal output.
3. Confirm the current directory and active virtual environment.
4. Inspect the file and line mentioned in the traceback.
5. Check imports, names, configuration and route connections.
6. Run `python manage.py check`.
7. Test the browser behavior again.

### Q6. A student says, "The command completed, so the feature is done." Is that enough?
**Suggested answer:** No. A command may create a file or start a server without proving the required user behavior. Demonstrate the result, test an edge case and explain the implementation.

### Q7. How would you explain your implementation to another developer?
**Suggested answer:** State the requirement, name the files, explain the data or request flow, demonstrate the commands, show expected output and describe one failure and its fix.

## 3. Practical coding discussion

Be ready to:
- Identify the exact file path.
- Explain the important imports and statements.
- Run the relevant management command.
- Demonstrate the browser or terminal result.
- Modify one small part and predict the outcome.
- Test one invalid or unexpected case.
- Diagnose one common error.

## 4. Mini-project viva — Django Configuration Explorer

1. What problem does the project solve?
2. What are the functional requirements?
3. Which files did you create or update?
4. What commands did you execute?
5. What does the main code do?
6. How did you test the normal case?
7. Which edge case did you test?
8. What error did you encounter?
9. How did you resolve it?
10. What would you improve next?

## 5. Rapid revision

- Explain the concept in one minute.
- Identify the exact files and their responsibilities.
- Trace the relevant execution flow.
- Demonstrate the mini-project.
- Run the required checks.
- Explain an edge case.
- Describe a safe debugging process.

## 6. Readiness checklist

- [ ] I can define the topic.
- [ ] I can explain the relevant files.
- [ ] I can reproduce the implementation.
- [ ] I can explain the important code.
- [ ] I can verify the expected behavior.
- [ ] I can explain an edge case.
- [ ] I can present Django Configuration Explorer without reading the notes.

**Self-practice:** Predict the result of a small code or configuration change. Check your reasoning against the code and observed result, not memorized definitions.
