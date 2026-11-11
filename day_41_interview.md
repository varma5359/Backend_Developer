# Day 41: Interview Guide — Django Application Integration and Complete Request-Response Flow

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 41 notes](day_41_notes.md)  
**Mini-project:** Django Student Management Website

## 1. Technical questions with model answers

### Q1. Trace a GET request to the student list.

**Model answer:** The browser requests /students/. The root URLconf includes profiles.urls. The app route selects student_list. The view queries Student records, passes them in context to student_list.html and returns the rendered HTTP response.

### Q2. Trace a valid registration POST.

**Model answer:** The browser posts form data and CSRF token. The URL selects student_register. The view binds StudentRegistrationForm(request.POST), is_valid() runs validation, save() writes the record, and redirect sends the browser to the named student list route.

### Q3. What happens on an invalid POST?

**Model answer:** The form remains bound, is_valid() returns False, the view does not save and re-renders the form with errors and submitted values.

### Q4. Why should the template not query the database directly?

**Model answer:** The view should prepare data and pass it through context. This keeps database/business logic in Python and presentation in templates.

### Q5. Why use named URL reversing?

**Model answer:** It avoids hardcoding route strings in redirects and templates. Renaming a route path does not require changing every reference when its name remains stable.

### Q6. What does the final capstone need to prove?

**Model answer:** That models, migrations, URL routing, views, forms, validation, templates and database persistence work together, and that the learner can explain and verify the complete flow.

## 2. Scenario-based interview question

**Scenario:** The registration form displays a success message but the student is missing from the list. How do you debug the complete path?

**Model answer:** Check the POST status and form.is_valid(), confirm save() is reached, inspect the returned model instance and query the same configured database. Verify the redirect route and list view queryset. Check that the list template iterates the same context key passed by the view.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Run the Student Management Website, verify list and registration routes, submit valid and invalid records, inspect the database/admin and demonstrate the request-response path without reading the notes.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Django Student Management Website

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
- [ ] I can present Django Student Management Website with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is integration testing?
**Answer:** It checks multiple components working together, such as a URL, view, form, model, database and template during one request.

### Q6. What does manage.py check prove?
**Answer:** It detects certain configuration problems. It does not prove every browser workflow or permission rule works.

### Q7. Why run the full test suite?
**Answer:** A new feature can break existing behavior in another app. The full suite helps detect regressions.

### Q8. What does the Django test client do?
**Answer:** It simulates HTTP requests to the application without requiring a real browser.

### Q9. Why test as an ordinary user?
**Answer:** Superusers bypass many permission restrictions and can hide access-control bugs.

### Q10. What should a debugging record contain?
**Answer:** Exact URL/command, active environment, traceback, relevant code, expected behavior, actual behavior and the smallest fix.

### Q11. Scenario: page works for admin but not student.
**Answer:** Check authentication, permissions, ownership, context assumptions and the data available to an ordinary user.

### Q12. Scenario: system check passes but form submission fails.
**Answer:** Run a functional test and inspect CSRF, form validation, database migration state and view behavior. System checks do not simulate every request.
