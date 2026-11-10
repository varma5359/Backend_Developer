# Day 50: Authorization, Permissions and Role-Based Access

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–49 — Django fundamentals, models, forms and authentication basics  
**Tools:** Python, Django, VS Code, terminal, browser and local test accounts  
**Approved mini-project:** Role-Based Employee Portal

> **Security reminder:** Use fake users and test data. Never paste real passwords, reset tokens, session cookies or private credentials into source control or shared messages.

## 1. Learning objectives

- Explain authorization, permissions and role-based access.
- Identify the Django APIs and settings involved.
- Implement the example step by step.
- Explain the security implications.
- Test both permitted and denied workflows.
- Complete Role-Based Employee Portal.

## 2. Concept introduction

Authentication confirms a user's identity. Authorization determines whether that user can perform an action. Django includes model permissions, groups, permission decorators and user permission methods. A role can be represented using groups and assigned permissions; sensitive object-level decisions may require explicit checks or a dedicated permission system.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render
from .models import Employee

@login_required
@permission_required("profiles.view_employee", raise_exception=True)
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "profiles/employee_list.html", {"employees": employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if not request.user.has_perm("profiles.view_employee"):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    return render(request, "profiles/employee_detail.html", {"employee": employee})
```

### Django shell — inspect permissions

```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from profiles.models import Employee

content_type = ContentType.objects.get_for_model(Employee)
view_permission = Permission.objects.get(
    codename="view_employee",
    content_type=content_type
)

hr_group, created = Group.objects.get_or_create(name="HR")
hr_group.permissions.add(view_permission)
```

## 4. Explain the important statements

### profiles/views.py

1. `from django.contrib.auth.decorators import login_required, permission_required` — Imports Django authentication, session or model utilities.
2. `from django.shortcuts import get_object_or_404, render` — Imports Django authentication, session or model utilities.
3. `from .models import Employee` — Imports Django authentication, session or model utilities.
4. ` ` — Part of the example; explain its role in the security workflow.
5. `@login_required` — Part of the example; explain its role in the security workflow.
6. `@permission_required("profiles.view_employee", raise_exception=True)` — Restricts a view to users with the named permission.
7. `def employee_list(request):` — Defines a view function.
8. `    employees = Employee.objects.all()` — Part of the example; explain its role in the security workflow.
9. `    return render(request, "profiles/employee_list.html", {"employees": employees})` — Part of the example; explain its role in the security workflow.
10. ` ` — Part of the example; explain its role in the security workflow.
11. `@login_required` — Part of the example; explain its role in the security workflow.
12. `def employee_detail(request, pk):` — Defines a view function.
13. `    employee = get_object_or_404(Employee, pk=pk)` — Part of the example; explain its role in the security workflow.
14. ` ` — Part of the example; explain its role in the security workflow.
15. `    if not request.user.has_perm("profiles.view_employee"):` — Checks whether the current user has a permission.
16. `        from django.core.exceptions import PermissionDenied` — Imports Django authentication, session or model utilities.
17. `        raise PermissionDenied` — Part of the example; explain its role in the security workflow.
18. ` ` — Part of the example; explain its role in the security workflow.
19. `    return render(request, "profiles/employee_detail.html", {"employee": employee})` — Part of the example; explain its role in the security workflow.

### Django shell — inspect permissions

1. `from django.contrib.auth.models import Group, Permission` — Imports Django authentication, session or model utilities.
2. `from django.contrib.contenttypes.models import ContentType` — Imports Django authentication, session or model utilities.
3. `from profiles.models import Employee` — Imports Django authentication, session or model utilities.
4. ` ` — Part of the example; explain its role in the security workflow.
5. `content_type = ContentType.objects.get_for_model(Employee)` — Part of the example; explain its role in the security workflow.
6. `view_permission = Permission.objects.get(` — Part of the example; explain its role in the security workflow.
7. `    codename="view_employee",` — Part of the example; explain its role in the security workflow.
8. `    content_type=content_type` — Part of the example; explain its role in the security workflow.
9. `)` — Part of the example; explain its role in the security workflow.
10. ` ` — Part of the example; explain its role in the security workflow.
11. `hr_group, created = Group.objects.get_or_create(name="HR")` — Part of the example; explain its role in the security workflow.
12. `hr_group.permissions.add(view_permission)` — Part of the example; explain its role in the security workflow.

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

Authentication confirms a user's identity. Authorization determines whether that user can perform an action. Django includes model permissions, groups, permission decorators and user permission methods. A role can be represented using groups and assigned permissions; sensitive object-level decisions may require explicit checks or a dedicated permission system.

## 8. Approved mini-project — Role-Based Employee Portal

**Objective:** Role-Based Employee Portal.

### Required tasks

1. Explain authentication versus authorization.
2. Inspect default model permissions created by Django.
3. Create groups such as HR and Manager.
4. Assign appropriate model permissions to groups.
5. Check user.has_perm() before protected operations.
6. Use login_required to require authentication.
7. Use permission_required for a model permission.
8. Test access as anonymous, normal and permitted users.
9. Explain why hiding a button in HTML is not sufficient authorization.

### Suggested structure

```text
projects/day_50/
├── README.md
├── config/
└── application/
    ├── views.py
    ├── urls.py
    ├── templates/
    └── tests/
```

### Validation checklist

- [ ] Anonymous users cannot access protected views.
- [ ] Authenticated users without permission are denied.
- [ ] Users with the correct permission can access the feature.
- [ ] Groups receive only required permissions.
- [ ] Object-specific access rules are checked where necessary.
- [ ] The learner understands that UI hiding is not security.

### Submission evidence

- Source files and settings relevant to the task.
- Screenshots from local test accounts.
- Valid and denied access test results.
- README with setup and security decisions.
- No passwords, reset tokens or session cookies in evidence.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Role-Based Employee Portal. Identify views, settings, URL patterns, templates, security controls and test cases. Do not provide the complete implementation."

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

**Q1. Explain authorization, permissions and role-based access.**  
**Answer:** Authentication confirms a user's identity. Authorization determines whether that user can perform an action. Django includes model permissions, groups, permission decorators and user permission methods. A role can be represented using groups and assigned permissions; sensitive object-level decisions may require explicit checks or a dedicated permission system.

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
- [ ] Complete Role-Based Employee Portal.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 51.
