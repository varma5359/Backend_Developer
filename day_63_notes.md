# Day 63: API Authentication and Permission Classes

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–62 — DRF installation, serializers and API views  
**Tools:** Python, Django, DRF, VS Code, terminal and Postman  
**Approved mini-project:** Protected Employee API

> **Trainer guidance:** Compare the different DRF view styles using the same resource. Explain what code the framework provides automatically and what the developer still needs to configure.

## 1. Learning objectives

- Explain api authentication and permission classes.
- Identify the DRF class, mixin, router or permission involved.
- Implement the example step by step.
- Connect URL patterns to API behavior.
- Test valid and denied requests.
- Complete Protected Employee API.

## 2. Concept introduction

Authentication identifies the API client or user. Permission classes decide whether the request is allowed to proceed. DRF supports permissions such as AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly. Authentication and permissions are separate: successful authentication does not automatically grant access.

## 3. File-by-file implementation

### profiles/api_views.py

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
```

### settings.py — default API permission

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
```

### Custom permission example

```python
from rest_framework.permissions import BasePermission

class IsHRUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="HR").exists()
        )
```

## 4. Explain the important statements

### profiles/api_views.py

1. `from rest_framework.permissions import IsAuthenticated` — Imports DRF components or models.
2. `from rest_framework.viewsets import ModelViewSet` — Imports DRF components or models.
3. `from .models import Employee` — Imports DRF components or models.
4. `from .serializers import EmployeeSerializer` — Imports DRF components or models.
5. ` ` — Part of the API configuration; explain its effect.
6. `class EmployeeViewSet(ModelViewSet):` — Defines a view, ViewSet or permission class.
7. `    queryset = Employee.objects.all()` — Part of the API configuration; explain its effect.
8. `    serializer_class = EmployeeSerializer` — Defines a view, ViewSet or permission class.
9. `    permission_classes = [IsAuthenticated]` — Specifies which permission checks must pass.

### settings.py — default API permission

1. `REST_FRAMEWORK = {` — Part of the API configuration; explain its effect.
2. `    "DEFAULT_PERMISSION_CLASSES": [` — Part of the API configuration; explain its effect.
3. `        "rest_framework.permissions.IsAuthenticated",` — Part of the API configuration; explain its effect.
4. `    ],` — Part of the API configuration; explain its effect.
5. `}` — Part of the API configuration; explain its effect.

### Custom permission example

1. `from rest_framework.permissions import BasePermission` — Imports DRF components or models.
2. ` ` — Part of the API configuration; explain its effect.
3. `class IsHRUser(BasePermission):` — Defines a view, ViewSet or permission class.
4. `    def has_permission(self, request, view):` — Defines a custom request-level permission decision.
5. `        return (` — Part of the API configuration; explain its effect.
6. `            request.user` — Part of the API configuration; explain its effect.
7. `            and request.user.is_authenticated` — Part of the API configuration; explain its effect.
8. `            and request.user.groups.filter(name="HR").exists()` — Part of the API configuration; explain its effect.
9. `        )` — Part of the API configuration; explain its effect.

## 5. Compare the DRF approaches

| Approach | Best use |
|---|---|
| Function-based API view | Small endpoint with explicit control |
| APIView | Class-based endpoint with explicit HTTP method handlers |
| Generic views | Common list/create/retrieve/update/delete patterns |
| Mixins | Reuse specific operations in custom combinations |
| ViewSet | Group related resource actions in one class |
| Router | Generate URL patterns for registered ViewSets |

More abstraction is not automatically better. Choose the clearest structure for the endpoint.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Method not allowed | View class or ViewSet actions |
| Router URL missing | Router registration and included router.urls |
| 401/403 response | Authentication and permission configuration |
| Queryset exposes too many records | get_queryset() and user scoping |
| Serializer mismatch | serializer_class and model |
| Custom permission always denies | User authentication, group name and permission method |

## 7. Industry scenario

Authentication identifies the API client or user. Permission classes decide whether the request is allowed to proceed. DRF supports permissions such as AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly. Authentication and permissions are separate: successful authentication does not automatically grant access.

## 8. Approved mini-project — Protected Employee API

**Objective:** Protected Employee API.

### Required tasks

1. Explain authentication versus permission checks.
2. Protect an API view with IsAuthenticated.
3. Compare AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly.
4. Configure a default permission class where appropriate.
5. Create a custom permission based on group membership.
6. Test anonymous, authenticated normal and HR users.
7. Verify that the API denies direct requests without permission.
8. Explain why hiding frontend buttons is not sufficient security.

### Suggested structure

```text
projects/day_63/
├── README.md
├── config/
└── profiles/
    ├── api_views.py
    ├── api_urls.py
    ├── serializers.py
    ├── permissions.py
    └── tests/
```

### Validation checklist

- [ ] Anonymous request is denied where authentication is required.
- [ ] Authenticated user receives only permitted access.
- [ ] Admin/HR behavior matches configured rules.
- [ ] Custom permission is tested.
- [ ] Direct API URL access is protected.
- [ ] The learner distinguishes authentication and authorization.

### Postman evidence

- Successful list and detail request.
- Successful create/update request where applicable.
- Invalid request response.
- Anonymous request response.
- Authenticated user response.
- Custom permission test if applicable.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Protected Employee API. Compare the suitable DRF view styles, list routes, permissions and test cases. Do not generate the entire API."

**Guided prompt:** "Help me implement one view or permission class at a time. Explain what DRF provides automatically."

**Debugging prompt:** "Here is my view, URL configuration and status code. Trace the routing, authentication and permission flow."

**Review prompt:** "Review the API for overbroad querysets, missing permissions, duplicated code and incorrect route behavior."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Reuse common API operations or enforce access rules.  
B. Replace JSON.  
C. Disable URL routing.  
D. Remove serializers.  
**Answer: A.** DRF abstractions reduce repeated code or enforce permissions.

**Q2. What does a router do with a ViewSet?**  
A. Creates a database.  
B. Generates URL patterns for registered actions.  
C. Hashes passwords.  
D. Installs Django.  
**Answer: B.** Routers connect ViewSets to URL patterns.

**Q3. What is the purpose of IsAuthenticated?**  
A. Allow anonymous requests.  
B. Sort the queryset.  
C. Require an authenticated user.  
D. Delete a record.  
**Answer: C.** IsAuthenticated denies anonymous requests.

**Q4. Does authentication automatically grant every permission?**  
A. Yes.  
B. Only on GET.  
C. Only in Postman.  
D. No. Permission checks are separate.  
**Answer: D.** Authentication and authorization are separate.

**Q5. What is the strongest evidence of a protected API?**  
A. Anonymous and permitted user requests return the expected different results.  
B. A button is hidden in HTML.  
C. The route is not documented.  
D. The API returns 200 for every request.  
**Answer: A.** Test access directly at the API.

## 11. Interview preparation

**Q1. Explain api authentication and permission classes.**  
**Answer:** Authentication identifies the API client or user. Permission classes decide whether the request is allowed to proceed. DRF supports permissions such as AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly. Authentication and permissions are separate: successful authentication does not automatically grant access.

**Q2. What is the difference between generic views and ViewSets?**  
**Answer:** Generic views represent common API patterns through individual view classes. ViewSets group related resource actions, often with router-generated URLs.

**Q3. Why are permission classes needed?**  
**Answer:** They enforce access rules on the server for every request.

**Follow-up:** Why is frontend-only permission hiding unsafe?  
**Answer:** A client can call the API URL directly, so the server must enforce permissions.

## 12. Completion checklist

- [ ] Explain the DRF approach.
- [ ] Implement and connect the view.
- [ ] Test the routes.
- [ ] Verify permissions.
- [ ] Complete Protected Employee API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and Postman evidence.

**Next lesson:** Day 64.
