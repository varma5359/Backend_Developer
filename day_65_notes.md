# Day 65: Role-Based API Permissions and Object-Level Permissions

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–65 — DRF serializers, views, routers and permissions  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** Role-Based Access API

> **Security reminder:** Use test accounts and fake tokens. Never paste real API tokens, JWTs, passwords or session cookies into a public repository or screenshot.

## 1. Learning objectives

- Explain role-based api permissions and object-level permissions.
- Configure the relevant DRF component.
- Implement the example step by step.
- Test valid and invalid requests.
- Explain security, privacy and API behavior.
- Complete Role-Based Access API.

## 2. Concept introduction

Role-based access assigns permissions according to a user's role, often represented by Django groups. Object-level permissions decide whether the user may access a specific record. A user may have permission to view employees generally but still be restricted from viewing or editing another employee's private record.

## 3. File-by-file implementation

### profiles/permissions.py

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrHR(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return (
                obj.user_id == request.user.id
                or request.user.groups.filter(name="HR").exists()
            )

        return request.user.groups.filter(name="HR").exists()
```

### profiles/api_views.py

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import EmployeeProfile
from .serializers import EmployeeProfileSerializer
from .permissions import IsOwnerOrHR

class EmployeeProfileViewSet(ModelViewSet):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrHR]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="HR").exists():
            return EmployeeProfile.objects.all()
        return EmployeeProfile.objects.filter(user=user)
```

## 4. Explain the important statements

### profiles/permissions.py

1. `from rest_framework.permissions import BasePermission, SAFE_METHODS` — Imports DRF, Django or model components.
2. ` ` — Part of the API configuration; explain its effect on the request.
3. `class IsOwnerOrHR(BasePermission):` — Defines an authentication, permission or API view class.
4. `    def has_object_permission(self, request, view, obj):` — Defines record-level access rules.
5. `        if request.method in SAFE_METHODS:` — Part of the API configuration; explain its effect on the request.
6. `            return (` — Part of the API configuration; explain its effect on the request.
7. `                obj.user_id == request.user.id` — Part of the API configuration; explain its effect on the request.
8. `                or request.user.groups.filter(name="HR").exists()` — Part of the API configuration; explain its effect on the request.
9. `            )` — Part of the API configuration; explain its effect on the request.
10. ` ` — Part of the API configuration; explain its effect on the request.
11. `        return request.user.groups.filter(name="HR").exists()` — Part of the API configuration; explain its effect on the request.

### profiles/api_views.py

1. `from rest_framework.viewsets import ModelViewSet` — Imports DRF, Django or model components.
2. `from rest_framework.permissions import IsAuthenticated` — Imports DRF, Django or model components.
3. `from .models import EmployeeProfile` — Imports DRF, Django or model components.
4. `from .serializers import EmployeeProfileSerializer` — Imports DRF, Django or model components.
5. `from .permissions import IsOwnerOrHR` — Imports DRF, Django or model components.
6. ` ` — Part of the API configuration; explain its effect on the request.
7. `class EmployeeProfileViewSet(ModelViewSet):` — Defines an authentication, permission or API view class.
8. `    serializer_class = EmployeeProfileSerializer` — Defines an authentication, permission or API view class.
9. `    permission_classes = [IsAuthenticated, IsOwnerOrHR]` — Part of the API configuration; explain its effect on the request.
10. ` ` — Part of the API configuration; explain its effect on the request.
11. `    def get_queryset(self):` — Restricts the records available to the current request.
12. `        user = self.request.user` — Part of the API configuration; explain its effect on the request.
13. `        if user.groups.filter(name="HR").exists():` — Part of the API configuration; explain its effect on the request.
14. `            return EmployeeProfile.objects.all()` — Part of the API configuration; explain its effect on the request.
15. `        return EmployeeProfile.objects.filter(user=user)` — Part of the API configuration; explain its effect on the request.

## 5. Important distinctions

| Concept | Meaning |
|---|---|
| Authentication | Establishes who is making the request |
| Token | Credential sent by the client to authenticate |
| JWT | Signed token format with claims and expiry |
| Role | User grouping that represents a set of responsibilities |
| Model permission | Permission for an action on a model |
| Object permission | Permission decision for a specific object |
| Filtering | Restricts records using structured conditions |
| Searching | Matches text across configured fields |
| Ordering | Sorts results |
| Pagination | Splits results into pages |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| 401 Unauthorized | Authentication class and Authorization header |
| 403 Forbidden | Permission class, user role and object ownership |
| User sees too many records | get_queryset() scoping |
| Search returns unexpected values | search_fields and query parameter |
| Ordering rejected | ordering_fields allowlist |
| Pagination missing | DEFAULT_PAGINATION_CLASS and page size |
| Token leaked | Revoke/rotate token and remove secret from future exposure |

## 7. Industry scenario

Role-based access assigns permissions according to a user's role, often represented by Django groups. Object-level permissions decide whether the user may access a specific record. A user may have permission to view employees generally but still be restricted from viewing or editing another employee's private record.

## 8. Approved mini-project — Role-Based Access API

**Objective:** Role-Based Access API.

### Required tasks

1. Define the roles required by the business scenario.
2. Create Django groups such as HR and Employee.
3. Assign only the required model permissions to each group.
4. Create a custom BasePermission class.
5. Implement has_object_permission() for record-level checks.
6. Filter get_queryset() so users cannot list records they do not own.
7. Test own record, another user's record and HR access.
8. Test write operations separately from safe read methods.

### Suggested structure

```text
projects/day_65/
├── README.md
├── config/
└── application/
    ├── permissions.py
    ├── api_views.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] Normal employee sees only own records.
- [ ] HR role sees the intended employee records.
- [ ] Non-HR user cannot modify another employee's profile.
- [ ] Anonymous user is denied.
- [ ] Queryset is scoped as well as object permissions.
- [ ] Direct API URL access cannot bypass the rules.

### Postman test matrix

| Request | Expected result |
|---|---|
| Missing/invalid credentials | 401 or configured authentication error |
| Authenticated but no permission | 403 |
| Authorized user | 200/201 as appropriate |
| Search/filter query | Only matching results |
| Unsupported order field | Rejected or ignored according to configuration |
| Page navigation | Correct page metadata and result count |

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Role-Based Access API. Identify authentication, permission, filtering and test cases. Do not provide real credentials or tokens."

**Guided prompt:** "Guide me through one configuration or permission step. Explain the security effect and wait for my test result."

**Debugging prompt:** "Here is the request method, URL, headers without secrets, response status and relevant code. Diagnose the authentication or permission issue."

**Review prompt:** "Review the API for token handling, queryset scoping, object-level permissions and safe filtering/order fields."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Secure API access or control which records are returned.  
B. Replace Django.  
C. Disable HTTP.  
D. Store tokens in source code.  
**Answer: A.** These features control identity, access and API result size.

**Q2. What should never be committed?**  
A. Public serializer code.  
B. Real access tokens or JWTs.  
C. A test fixture with fake data.  
D. A README.  
**Answer: B.** Tokens are credentials and must be protected.

**Q3. What is object-level permission?**  
A. Sorting all records.  
B. Installing DRF.  
C. Deciding whether a user can access a specific record.  
D. Changing a template.  
**Answer: C.** It evaluates access for an individual object.

**Q4. Why use pagination?**  
A. To return every record at once.  
B. To disable search.  
C. To remove filters.  
D. To limit result size and support page navigation.  
**Answer: D.** Pagination improves usability and resource control.

**Q5. Why explicitly configure ordering_fields?**  
A. To allow only intended sort fields.  
B. To expose every model field.  
C. To remove authentication.  
D. To change database schema.  
**Answer: A.** An allowlist gives predictable API behavior.

## 11. Interview preparation

**Q1. Explain role-based api permissions and object-level permissions.**  
**Answer:** Role-based access assigns permissions according to a user's role, often represented by Django groups. Object-level permissions decide whether the user may access a specific record. A user may have permission to view employees generally but still be restricted from viewing or editing another employee's private record.

**Q2. What is one security risk?**  
**Answer:** Explain the risk of leaked tokens, overbroad querysets or missing object-level permissions.

**Q3. How do you verify the implementation?**  
**Answer:** Use test accounts and requests with valid, missing and invalid credentials. Test own and other users' records and verify filter/search/order/page results.

**Follow-up:** Why is queryset scoping important even when object permissions exist?  
**Answer:** Queryset scoping limits which records can be listed or retrieved and reduces the chance of exposing unauthorized objects.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Configure the relevant DRF components.
- [ ] Test valid and invalid requests.
- [ ] Verify access and result boundaries.
- [ ] Complete Role-Based Access API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 66.
