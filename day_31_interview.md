# Day 31: Interview Questions — Django Views: Function-Based Views and Request-Response Cycle

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 31 class notes](day_31_notes.md)  
**Approved mini-project:** Dynamic Welcome Application

## 1. Core technical questions

### Q1. Explain django views: function-based views and request-response cycle.
**Answer:** A view is a Python callable that receives an HttpRequest object and returns an HttpResponse. Function-based views are ordinary Python functions with a request parameter. They contain request-specific application logic and decide what response to return.

### Q2. Describe the request flow.
**Answer:** HTTP request → URL pattern → view(request) → application logic → HttpResponse / rendered template → browser

### Q3. Which files are involved?
**Answer:** profiles/views.py, profiles/urls.py. Explain the responsibility of each file and how the files connect.

### Q4. What is a common beginner error?
**Answer:** Each view accepts request as its first parameter. If the result differs, inspect the exact URL, file path, import, function name and server traceback.

### Q5. How do you verify the implementation?
**Answer:** Run python manage.py check, start the development server, open the expected route and test at least one invalid or unmatched case.

## 2. Scenario-based questions

### Q6. A browser request does not show the expected page. What do you inspect?
**Suggested answer:**
1. Confirm the development server is running.
2. Verify the exact URL path.
3. Inspect the project URLconf.
4. Inspect the application URLconf.
5. Confirm the view function exists and returns a response.
6. If a template is used, verify its path and context values.
7. Read the traceback and test again.

### Q7. Why should URL routing, views and templates have separate responsibilities?
**Suggested answer:** URL routing selects the handler, the view implements request-specific logic and prepares data, and the template controls HTML presentation. Separating them makes the application easier to maintain.

## 3. Practical coding discussion

Be ready to:
- Identify the exact file path.
- Explain each important import.
- Explain the route and view connection.
- Demonstrate the browser output.
- Explain how invalid routes or missing templates are handled.
- Describe how you would test the implementation.

## 4. Mini-project viva — Dynamic Welcome Application

1. What problem does the project solve?
2. Which URL paths did you create?
3. Which view handles each route?
4. What data is passed to the view?
5. What response does the view return?
6. What did you verify in the browser?
7. What error did you encounter?
8. How did you fix it?
9. Which test would you automate?
10. What would you improve next?

## 5. Rapid revision

- **1.** Create a simple function-based view.
- **2.** Import HttpResponse from django.http.
- **3.** Return an HttpResponse from the view.
- **4.** Connect the view to a URL pattern.
- **5.** Add a second view that accepts a URL parameter.
- **6.** Inspect request.method and request.path in a safe demonstration.
- **7.** Explain that a view must return an HttpResponse-compatible response.

## 6. Common incorrect answers

| Incorrect answer | Better answer |
|---|---|
| URLconf contains all business logic | URLconf maps paths to views |
| A view can return any object | A view should return an HttpResponse-compatible response |
| A template runs Python code | Django templates use a restricted template language |
| A 404 always means the server is stopped | It may mean no URL pattern matched |
| The file path is unimportant | Django file and template paths must be correct |

## 7. Readiness checklist

- [ ] Explain the concept.
- [ ] Explain the file structure.
- [ ] Trace the request to the response.
- [ ] Demonstrate the mini-project.
- [ ] Explain one error and its resolution.
- [ ] Answer follow-up questions.
