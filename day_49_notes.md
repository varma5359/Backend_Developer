# Day 49: Django Sessions, Cookies and Session Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–49 — Django fundamentals, models, forms and authentication basics  
**Tools:** Python, Django, VS Code, terminal, browser and local test accounts  
**Approved mini-project:** Session-Based Shopping Cart

> **Security reminder:** Use fake users and test data. Never paste real passwords, reset tokens, session cookies or private credentials into source control or shared messages.

## 1. Learning objectives

- Explain django sessions, cookies and session management.
- Identify the Django APIs and settings involved.
- Implement the example step by step.
- Explain the security implications.
- Test both permitted and denied workflows.
- Complete Session-Based Shopping Cart.

## 2. Concept introduction

A cookie is small data stored by the browser and sent with matching requests. Django sessions store user-specific state on the server or configured session backend; the browser usually holds a session identifier cookie. Session data can support a shopping cart, but important business data should be persisted appropriately.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.shortcuts import render, redirect

def cart_view(request):
    cart = request.session.get("cart", {})
    return render(request, "store/cart.html", {"cart": cart})

def add_to_cart(request, product_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        key = str(product_id)
        cart[key] = cart.get(key, 0) + 1
        request.session["cart"] = cart
        request.session.modified = True
    return redirect("cart_view")

def clear_cart(request):
    if request.method == "POST":
        request.session.pop("cart", None)
    return redirect("cart_view")
```

### settings.py — security-oriented cookie settings

```python
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True  # Use HTTPS in production
CSRF_COOKIE_SECURE = True     # Use HTTPS in production
```

## 4. Explain the important statements

### profiles/views.py

1. `from django.shortcuts import render, redirect` — Imports Django authentication, session or model utilities.
2. ` ` — Part of the example; explain its role in the security workflow.
3. `def cart_view(request):` — Defines a view function.
4. `    cart = request.session.get("cart", {})` — Reads or updates server-side session data.
5. `    return render(request, "store/cart.html", {"cart": cart})` — Part of the example; explain its role in the security workflow.
6. ` ` — Part of the example; explain its role in the security workflow.
7. `def add_to_cart(request, product_id):` — Defines a view function.
8. `    if request.method == "POST":` — Part of the example; explain its role in the security workflow.
9. `        cart = request.session.get("cart", {})` — Reads or updates server-side session data.
10. `        key = str(product_id)` — Part of the example; explain its role in the security workflow.
11. `        cart[key] = cart.get(key, 0) + 1` — Part of the example; explain its role in the security workflow.
12. `        request.session["cart"] = cart` — Reads or updates server-side session data.
13. `        request.session.modified = True` — Reads or updates server-side session data.
14. `    return redirect("cart_view")` — Part of the example; explain its role in the security workflow.
15. ` ` — Part of the example; explain its role in the security workflow.
16. `def clear_cart(request):` — Defines a view function.
17. `    if request.method == "POST":` — Part of the example; explain its role in the security workflow.
18. `        request.session.pop("cart", None)` — Reads or updates server-side session data.
19. `    return redirect("cart_view")` — Part of the example; explain its role in the security workflow.

### settings.py — security-oriented cookie settings

1. `SESSION_COOKIE_HTTPONLY = True` — Configures browser session cookie behavior.
2. `SESSION_COOKIE_SECURE = True  # Use HTTPS in production` — Configures browser session cookie behavior.
3. `CSRF_COOKIE_SECURE = True     # Use HTTPS in production` — Part of the example; explain its role in the security workflow.

## 5. Important security concepts

| Concept | What it protects |
|---|---|
| Password hashing | Avoids storing readable passwords |
| Password validation | Rejects weak or unsuitable passwords |
| Reset token | Provides a controlled password reset workflow |
| Session | Associates requests with server-side user state |
| HttpOnly cookie | Prevents ordinary client-side scripts from reading the cookie |
| Secure cookie | Restricts cookie transmission to HTTPS |
| CSRF token | Helps protect browser POST requests |
| Permission | Defines an allowed action |
| Group | Collects users and permissions into a role-like set |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Password check fails | Confirm set_password() was used and the saved user was refreshed |
| Reset email not sent | Email backend and environment settings |
| Session data disappears | Session middleware, cookie and session backend |
| Cart does not update | POST method, session assignment and modified flag |
| User can access restricted page | View decorator and permission check |
| User sees 403 unexpectedly | Group membership and assigned permission |
| Secure cookie missing in local HTTP | Secure flag requires HTTPS; configure by environment |

## 7. Industry scenario

A cookie is small data stored by the browser and sent with matching requests. Django sessions store user-specific state on the server or configured session backend; the browser usually holds a session identifier cookie. Session data can support a shopping cart, but important business data should be persisted appropriately.

## 8. Approved mini-project — Session-Based Shopping Cart

**Objective:** Session-Based Shopping Cart.

### Required tasks

1. Explain the difference between a browser cookie and server-side session data.
2. Inspect SESSION_ENGINE and session middleware settings.
3. Read a cart dictionary from request.session.
4. Update session data after a POST action.
5. Use a POST form with CSRF token for add and clear operations.
6. Set appropriate session expiry when the use case requires it.
7. Explain secure cookie settings and HTTPS requirements.
8. Test the cart across page requests and after logout/session expiry.

### Suggested structure

```text
projects/day_49/
├── README.md
├── config/
└── application/
    ├── views.py
    ├── urls.py
    ├── templates/
    └── tests/
```

### Validation checklist

- [ ] Cart data persists across requests for the same session.
- [ ] Adding a product increments its quantity.
- [ ] Clear cart uses POST.
- [ ] CSRF token is included.
- [ ] Sensitive values are not stored in client-readable cookies.
- [ ] Cookie security settings are appropriate for the environment.

### Submission evidence

- Source files and settings relevant to the task.
- Screenshots from local test accounts.
- Valid and denied access test results.
- README with setup and security decisions.
- No passwords, reset tokens or session cookies in evidence.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Session-Based Shopping Cart. Identify views, settings, URL patterns, templates, security controls and test cases. Do not provide the complete implementation."

**Guided prompt:** "Help me implement one safe workflow at a time. Explain the security setting and wait for my test result."

**Debugging prompt:** "Here is my local test configuration and error. Diagnose the issue without asking me to share real credentials, tokens or cookies."

**Review prompt:** "Review the feature for password handling, session security, authorization and negative test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Securely manage credentials, sessions or access rights.  
B. Replace HTTP.  
C. Store secrets in HTML.  
D. Disable authentication.  
**Answer: A.** These controls protect user identity and application data.

**Q2. What should never be committed to Git?**  
A. A README.  
B. A real password, reset token or session cookie.  
C. A test case.  
D. A public CSS file.  
**Answer: B.** Credentials and session secrets must remain private.

**Q3. Which check should protect a sensitive operation?**  
A. Hiding the button only.  
B. A CSS class.  
C. Server-side authentication and authorization.  
D. A comment in the code.  
**Answer: C.** Security decisions must be enforced on the server.

**Q4. What is a safe way to test access?**  
A. Use a real customer's account.  
B. Share a session cookie.  
C. Disable all permissions.  
D. Use separate local test users with different permissions.  
**Answer: D.** Test accounts allow controlled positive and negative tests.

**Q5. What is the best evidence of completion?**  
A. Verified permitted and denied workflows.  
B. A login page screenshot only.  
C. A project folder only.  
D. A code snippet with no test.  
**Answer: A.** Security behavior requires both positive and negative testing.

## 11. Interview preparation

**Q1. Explain django sessions, cookies and session management.**  
**Answer:** A cookie is small data stored by the browser and sent with matching requests. Django sessions store user-specific state on the server or configured session backend; the browser usually holds a session identifier cookie. Session data can support a shopping cart, but important business data should be persisted appropriately.

**Q2. What is one security mistake to avoid?**  
**Answer:** Do not expose passwords, tokens or session identifiers. Do not rely on frontend-only checks for access control.

**Q3. How do you verify the feature?**  
**Answer:** Use local test accounts with different states and permissions. Test allowed and denied requests and inspect the server-side result.

**Follow-up:** Why is hiding a link not sufficient authorization?  
**Answer:** A user can send a direct request to the URL. The view must enforce the permission on the server.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid workflows.
- [ ] Verify security settings and access checks.
- [ ] Complete Session-Based Shopping Cart.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 50.
