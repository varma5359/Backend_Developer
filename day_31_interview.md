# Day 31: Interview Guide — Django Views: Function-Based Views and Request-Response Cycle

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 31 notes](day_31_notes.md)  
**Approved mini-project:** Dynamic Welcome Application

## 1. Core technical questions

### Q1. What is the central purpose of this lesson?
**Answer:** A view is a Python callable that receives an HttpRequest and returns an HttpResponse (or another compatible response). A function-based view is an ordinary Python function with a request parameter. Django selects the view through URL routing. The view decides what work to perform and what response to return.

**Follow-up:** Explain this using the Student Portal example.

### Q2. Which files are responsible for the implementation?
**Answer:** The files are profiles/views.py, profiles/urls.py, profiles/templates/profiles/welcome.html. Describe the responsibility of each file, rather than only listing names.

**Follow-up:** Explain this using the Student Portal example.

### Q3. How would you verify the feature?
**Answer:** Run the required commands, inspect the output, test the browser behavior and verify an edge case. Use the exact checks in Day 31 class notes.

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

## 4. Mini-project viva — Dynamic Welcome Application

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
- [ ] I can present Dynamic Welcome Application without reading the notes.

**Trainer note:** Ask the learner to predict the result of a small code or configuration change. Reward reasoning and evidence, not memorized definitions.
