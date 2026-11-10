# Day 47: User Registration, Login and Logout

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–46 — Django fundamentals, ORM, forms and user concepts  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** User Authentication Application

> **Trainer guidance:** Authentication and data integrity are important backend responsibilities. Use local test users and sample records. Never ask learners to paste real passwords, tokens or secret keys into code or shared screenshots.

## 1. Learning objectives

- Explain user registration, login and logout.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Test valid and invalid cases.
- Explain the security and data-integrity implications.
- Complete User Authentication Application.

## 2. Concept introduction

Registration creates an account after validating the submitted details. Login verifies credentials and creates an authenticated session. Logout ends the current authenticated session. Django provides UserCreationForm, authenticate(), login(), logout() and login_required for common workflows.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registration/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "registration/login.html")

@login_required
def dashboard(request):
    return render(request, "registration/dashboard.html")

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("dashboard")
```

### Login form template

```python
<form method="post">
    {% csrf_token %}
    <label>Username</label>
    <input name="username" required>
    <label>Password</label>
    <input type="password" name="password" required>
    <button type="submit">Login</button>
</form>
```

### Logout form template

```python
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Logout</button>
</form>
```

## 4. Explain the important statements

### profiles/views.py

1. `from django.contrib.auth import authenticate, login, logout` — Imports Django authentication, model or validation components.
2. `from django.contrib.auth.forms import UserCreationForm` — Imports Django authentication, model or validation components.
3. `from django.contrib.auth.decorators import login_required` — Imports Django authentication, model or validation components.
4. `from django.shortcuts import render, redirect` — Imports Django authentication, model or validation components.
5. ` ` — Part of the example; explain its role in the complete workflow.
6. `def register(request):` — Defines a view or validation method.
7. `    form = UserCreationForm(request.POST or None)` — Part of the example; explain its role in the complete workflow.
8. `    if request.method == "POST" and form.is_valid():` — Part of the example; explain its role in the complete workflow.
9. `        form.save()` — Part of the example; explain its role in the complete workflow.
10. `        return redirect("login")` — Part of the example; explain its role in the complete workflow.
11. `    return render(request, "registration/register.html", {"form": form})` — Part of the example; explain its role in the complete workflow.
12. ` ` — Part of the example; explain its role in the complete workflow.
13. `def user_login(request):` — Defines a view or validation method.
14. `    if request.method == "POST":` — Part of the example; explain its role in the complete workflow.
15. `        username = request.POST.get("username")` — Part of the example; explain its role in the complete workflow.
16. `        password = request.POST.get("password")` — Part of the example; explain its role in the complete workflow.
17. `        user = authenticate(request, username=username, password=password)` — Verifies credentials and returns a user or None.
18. `        if user is not None:` — Part of the example; explain its role in the complete workflow.
19. `            login(request, user)` — Associates the authenticated user with the current session.
20. `            return redirect("dashboard")` — Part of the example; explain its role in the complete workflow.
21. `    return render(request, "registration/login.html")` — Part of the example; explain its role in the complete workflow.
22. ` ` — Part of the example; explain its role in the complete workflow.
23. `@login_required` — Part of the example; explain its role in the complete workflow.
24. `def dashboard(request):` — Defines a view or validation method.
25. `    return render(request, "registration/dashboard.html")` — Part of the example; explain its role in the complete workflow.
26. ` ` — Part of the example; explain its role in the complete workflow.
27. `def user_logout(request):` — Defines a view or validation method.
28. `    if request.method == "POST":` — Part of the example; explain its role in the complete workflow.
29. `        logout(request)` — Ends the current authenticated session.
30. `        return redirect("login")` — Part of the example; explain its role in the complete workflow.
31. `    return redirect("dashboard")` — Part of the example; explain its role in the complete workflow.

### Login form template

1. `<form method="post">` — Part of the example; explain its role in the complete workflow.
2. `    {% csrf_token %}` — Part of the example; explain its role in the complete workflow.
3. `    <label>Username</label>` — Part of the example; explain its role in the complete workflow.
4. `    <input name="username" required>` — Part of the example; explain its role in the complete workflow.
5. `    <label>Password</label>` — Part of the example; explain its role in the complete workflow.
6. `    <input type="password" name="password" required>` — Part of the example; explain its role in the complete workflow.
7. `    <button type="submit">Login</button>` — Part of the example; explain its role in the complete workflow.
8. `</form>` — Part of the example; explain its role in the complete workflow.

### Logout form template

1. `<form method="post" action="{% url 'logout' %}">` — Part of the example; explain its role in the complete workflow.
2. `    {% csrf_token %}` — Part of the example; explain its role in the complete workflow.
3. `    <button type="submit">Logout</button>` — Part of the example; explain its role in the complete workflow.
4. `</form>` — Part of the example; explain its role in the complete workflow.

## 5. Important concepts and distinctions

| Concept | Meaning |
|---|---|
| Validation | Checks whether supplied data satisfies rules |
| Constraint | Database rule protecting stored data |
| Authentication | Verifies who the user is |
| Authorization | Determines what the user is allowed to do |
| Password hash | One-way derived representation used for password verification |
| Session | Server-managed state associated with a browser session |
| Anonymous user | Request that is not authenticated |
| Superuser | User with broad administrative permissions |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Duplicate value saved | Unique constraint and validation |
| Invalid value accepted | Field validator, full_clean and database constraint |
| Password stored incorrectly | Use create_user() or set_password() |
| Login always fails | Username, password, authentication backend and user state |
| Protected page accessible | login_required and view authorization |
| Logout does not work | POST method, URL and session configuration |
| User model import mismatch | get_user_model() and AUTH_USER_MODEL |

## 7. Security and reliability notes

- Never store raw passwords.
- Use Django's password management APIs.
- Keep CSRF protection enabled for browser POST forms.
- Protect views that contain private data.
- Authentication does not automatically grant permission to every record.
- Do not expose account existence or sensitive authentication details unnecessarily.
- Keep secret keys and database credentials outside source control.
- Use HTTPS in production.

## 8. Industry scenario

Registration creates an account after validating the submitted details. Login verifies credentials and creates an authenticated session. Logout ends the current authenticated session. Django provides UserCreationForm, authenticate(), login(), logout() and login_required for common workflows.

## 9. Approved mini-project — User Authentication Application

**Objective:** User Authentication Application.

### Required tasks

1. Use UserCreationForm for account registration.
2. Display the form on GET and bind POST data on submission.
3. Save the user only after form validation.
4. Use authenticate() to verify submitted credentials.
5. Call login() only when authenticate() returns a user.
6. Protect a dashboard using login_required.
7. Use POST for logout and include CSRF token.
8. Test valid, invalid and unauthenticated access.

### Suggested structure

```text
projects/day_47/
├── README.md
├── config/
└── profiles/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
```

### Validation checklist

- [ ] Valid registration creates a user.
- [ ] Duplicate or invalid registration displays form errors.
- [ ] Valid login creates an authenticated session.
- [ ] Invalid login does not authenticate the user.
- [ ] Anonymous users are redirected from the protected dashboard.
- [ ] Logout ends the session using POST.

### Submission evidence

- Source code and URL patterns.
- Registration and login screenshots using test accounts.
- Valid and invalid test results.
- Database evidence showing safe user creation.
- README with setup instructions and security notes.
- No passwords, access tokens or private data in the repository.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan User Authentication Application. List the forms, views, URLs, templates, validation rules and test cases. Do not provide a complete solution."

**Guided prompt:** "Guide me through one authentication or validation step at a time. Explain the security implications and wait for my test result."

**Debugging prompt:** "Here are my exact view, form, settings and error. Identify the cause without asking me to share any real password or secret."

**Review prompt:** "Review this local test implementation for validation, authentication, authorization, CSRF and secret handling."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Protect data integrity or manage user identity securely.  
B. Replace HTTP.  
C. Store passwords as plaintext.  
D. Disable database constraints.  
**Answer: A.** The feature protects application data and user workflows.

**Q2. What should be used for password creation?**  
A. Store raw password in a text field.  
B. Django's create_user() or set_password() API.  
C. Put the password in settings.py.  
D. Commit the password to Git.  
**Answer: B.** Django provides password hashing APIs.

**Q3. What is the difference between authentication and authorization?**  
A. They mean the same thing.  
B. Authentication is database sorting.  
C. Authentication verifies identity; authorization checks permissions.  
D. Authorization creates passwords.  
**Answer: C.** They are separate security decisions.

**Q4. What should happen before data is saved?**  
A. Ignore all validation.  
B. Disable constraints.  
C. Trust the browser.  
D. Validate the data and enforce important integrity rules.  
**Answer: D.** Validation and constraints protect data.

**Q5. What is the strongest evidence of completion?**  
A. Valid and invalid workflows are tested and security rules are explained.  
B. A project title only.  
C. A long code file.  
D. A screenshot of the login button.  
**Answer: A.** Test behavior and explain security choices.

## 12. Interview preparation

**Q1. Explain user registration, login and logout.**  
**Answer:** Registration creates an account after validating the submitted details. Login verifies credentials and creates an authenticated session. Logout ends the current authenticated session. Django provides UserCreationForm, authenticate(), login(), logout() and login_required for common workflows.

**Q2. What is one security risk?**  
**Answer:** Explain the relevant risk such as unsafe password handling, missing authorization, missing CSRF protection or invalid data reaching the database.

**Q3. How do you verify the workflow?**  
**Answer:** Use test accounts and test records. Exercise valid and invalid cases, inspect the session or database result and verify access restrictions.

**Follow-up:** Why is a successful login not proof of authorization?  
**Answer:** Authentication proves identity; authorization must still check whether that user has permission for the requested operation or record.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid cases.
- [ ] Verify data or session behavior.
- [ ] Complete User Authentication Application.
- [ ] Review security notes.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and evidence without secrets.

**Next lesson:** Day 48.
