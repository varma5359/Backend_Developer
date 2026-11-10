# Day 30: Interview Questions — URL Routing, Path Converters and URL Patterns

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 30 class notes](day_30_notes.md)  
**Approved mini-project:** Multi-Page Routing Application

## 1. Core technical questions

### Q1. Explain url routing, path converters and url patterns.
**Answer:** URL routing maps an incoming URL path to the view that should handle it. The project's root URL configuration can include the URL configuration of an application. Path converters capture values such as integers and strings from a URL.

### Q2. Describe the request flow.
**Answer:** Browser requests /profiles/42/ → config/urls.py → profiles/urls.py → selected view → HTTP response

### Q3. Which files are involved?
**Answer:** config/urls.py, profiles/urls.py, profiles/views.py. Explain the responsibility of each file and how the files connect.

### Q4. What is a common beginner error?
**Answer:** Root URL configuration includes the application URL file. If the result differs, inspect the exact URL, file path, import, function name and server traceback.

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

## 4. Mini-project viva — Multi-Page Routing Application

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

- **1.** Open config/urls.py and identify urlpatterns.
- **2.** Create profiles/urls.py if it does not exist.
- **3.** Include profiles.urls under the profiles/ prefix in the project URL file.
- **4.** Create profile_home and employee_detail views.
- **5.** Add a path converter for employee_id.
- **6.** Start the server and open both URLs.
- **7.** Try a non-integer value and observe that the int converter does not match.

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
