# Day 92: Capstone: REST API Development and Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 89–93 and relevant Django/DRF lessons  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Complete REST API

> **Capstone rule:** Every API and security decision must match the approved requirements. Test with fake accounts and sample records. Do not expose real user data, passwords or tokens.

## 1. Learning objectives

- Explain capstone: rest api development and validation.
- Implement the approved capstone deliverable.
- Connect the feature to the system architecture.
- Validate successful, invalid and unauthorized requests.
- Explain design and security trade-offs.
- Complete Complete REST API.

## 2. Concept introduction

The capstone API exposes department, employee, project and task resources. Each endpoint should have a clear method, serializer, validation rule and response contract. Clients should not be allowed to set protected ownership fields or fields that should be controlled by server-side business logic.

## 3. File-by-file implementation

### projects/serializers.py

```python
from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "name", "description", "manager",
            "start_date", "end_date", "status"
        ]
        read_only_fields = ["id"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id", "project", "assigned_employee",
            "title", "description", "status", "due_date"
        ]
        read_only_fields = ["id"]

    def validate_status(self, value):
        allowed = {"TODO", "IN_PROGRESS", "BLOCKED", "DONE"}
        if value not in allowed:
            raise serializers.ValidationError("Invalid task status.")
        return value
```

### projects/api_views.py

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.select_related("manager__user")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.select_related("project", "assigned_employee")
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
```

## 4. Explain the important code

### projects/serializers.py

1. `from rest_framework import serializers` — Part of the capstone implementation; explain how it supports the API contract.
2. `from .models import Project, Task` — Part of the capstone implementation; explain how it supports the API contract.
3. ` ` — Part of the capstone implementation; explain how it supports the API contract.
4. `class ProjectSerializer(serializers.ModelSerializer):` — Defines a serializer, viewset or permission class.
5. `    class Meta:` — Defines a serializer, viewset or permission class.
6. `        model = Project` — Part of the capstone implementation; explain how it supports the API contract.
7. `        fields = [` — Part of the capstone implementation; explain how it supports the API contract.
8. `            "id", "name", "description", "manager",` — Part of the capstone implementation; explain how it supports the API contract.
9. `            "start_date", "end_date", "status"` — Part of the capstone implementation; explain how it supports the API contract.
10. `        ]` — Part of the capstone implementation; explain how it supports the API contract.
11. `        read_only_fields = ["id"]` — Part of the capstone implementation; explain how it supports the API contract.
12. ` ` — Part of the capstone implementation; explain how it supports the API contract.
13. `class TaskSerializer(serializers.ModelSerializer):` — Defines a serializer, viewset or permission class.
14. `    class Meta:` — Defines a serializer, viewset or permission class.
15. `        model = Task` — Part of the capstone implementation; explain how it supports the API contract.
16. `        fields = [` — Part of the capstone implementation; explain how it supports the API contract.
17. `            "id", "project", "assigned_employee",` — Part of the capstone implementation; explain how it supports the API contract.
18. `            "title", "description", "status", "due_date"` — Part of the capstone implementation; explain how it supports the API contract.
19. `        ]` — Part of the capstone implementation; explain how it supports the API contract.
20. `        read_only_fields = ["id"]` — Part of the capstone implementation; explain how it supports the API contract.
21. ` ` — Part of the capstone implementation; explain how it supports the API contract.
22. `    def validate_status(self, value):` — Validates one serializer field.
23. `        allowed = {"TODO", "IN_PROGRESS", "BLOCKED", "DONE"}` — Part of the capstone implementation; explain how it supports the API contract.
24. `        if value not in allowed:` — Part of the capstone implementation; explain how it supports the API contract.
25. `            raise serializers.ValidationError("Invalid task status.")` — Part of the capstone implementation; explain how it supports the API contract.
26. `        return value` — Part of the capstone implementation; explain how it supports the API contract.

### projects/api_views.py

1. `from rest_framework.viewsets import ModelViewSet` — Provides common CRUD actions for a model resource.
2. `from rest_framework.permissions import IsAuthenticated` — Part of the capstone implementation; explain how it supports the API contract.
3. `from .models import Project, Task` — Part of the capstone implementation; explain how it supports the API contract.
4. `from .serializers import ProjectSerializer, TaskSerializer` — Part of the capstone implementation; explain how it supports the API contract.
5. ` ` — Part of the capstone implementation; explain how it supports the API contract.
6. `class ProjectViewSet(ModelViewSet):` — Defines a serializer, viewset or permission class.
7. `    queryset = Project.objects.select_related("manager__user")` — Fetches related single-valued objects efficiently.
8. `    serializer_class = ProjectSerializer` — Defines a serializer, viewset or permission class.
9. `    permission_classes = [IsAuthenticated]` — Applies server-side access rules.
10. ` ` — Part of the capstone implementation; explain how it supports the API contract.
11. `class TaskViewSet(ModelViewSet):` — Defines a serializer, viewset or permission class.
12. `    queryset = Task.objects.select_related("project", "assigned_employee")` — Fetches related single-valued objects efficiently.
13. `    serializer_class = TaskSerializer` — Defines a serializer, viewset or permission class.
14. `    permission_classes = [IsAuthenticated]` — Applies server-side access rules.

## 5. API contract checklist

| Item | Requirement |
|---|---|
| Resource | Department, Employee, Project, Task or Notification |
| Method | GET, POST, PUT, PATCH or DELETE as appropriate |
| Validation | Serializer and business rules |
| Authentication | Required for private resources |
| Authorization | Role and object-level rules |
| Status | Correct HTTP status code |
| Response | Documented JSON representation |
| Tests | Success, invalid, missing and unauthorized cases |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Field exposed unexpectedly | Serializer fields and read-only fields |
| User can change owner ID | Server-side assignment and serializer configuration |
| User sees another employee's data | get_queryset() and object permission |
| API returns 500 for invalid input | Serializer validation and exception handling |
| List endpoint is slow | Query count, select_related and pagination |
| Test fails due to URL name | Router basename and reverse() name |
| Error exposes traceback | Production DEBUG and exception handling |

## 7. Industry scenario

The capstone API exposes department, employee, project and task resources. Each endpoint should have a clear method, serializer, validation rule and response contract. Clients should not be allowed to set protected ownership fields or fields that should be controlled by server-side business logic.

## 8. Approved mini-project — Complete REST API

**Objective:** Complete REST API.

### Required tasks

1. Identify API resources and operations from Day 89 requirements.
2. Create serializers for projects and tasks.
3. Select exposed fields explicitly.
4. Add validation for task state and required values.
5. Create ViewSets for resource CRUD operations.
6. Register routes using a router.
7. Set server-controlled fields in perform_create() where needed.
8. Test list, detail, create, update, partial update and delete.
9. Document request and response examples.

### Suggested structure

```text
employee_project_management/
├── accounts/
├── employees/
├── projects/
│   ├── models.py
│   ├── serializers.py
│   ├── api_views.py
│   ├── permissions.py
│   └── tests/
├── tasks/
└── README.md
```

### Validation checklist

- [ ] Each resource has clear endpoints.
- [ ] Serializers expose only intended fields.
- [ ] Invalid task status is rejected.
- [ ] Protected fields are controlled by the server.
- [ ] CRUD methods return expected status codes.
- [ ] API documentation matches actual behavior.

## 9. AI-assisted capstone workflow

**Planning prompt:** "Help me plan Complete REST API. Use the approved capstone requirements. List API resources, security rules, tests and acceptance criteria."

**Implementation prompt:** "Guide me through one serializer, view or permission at a time. Explain why each field or rule exists."

**Debugging prompt:** "Here is my sanitized request, response status, serializer and permission code. Trace the failure and propose a small correction."

**Review prompt:** "Review the API contract, access control, query scope, validation, error handling and test evidence."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's deliverable?**  
A. Implement a verified part of the final backend.  
B. Add unrelated features.  
C. Remove security.  
D. Skip testing.  
**Answer: A.** The capstone is built through verifiable deliverables.

**Q2. Where should the server obtain the current user's identity?**  
A. A hidden form field.  
B. request.user.  
C. A query parameter.  
D. A URL slug supplied by the client.  
**Answer: B.** Use the authenticated request user.

**Q3. Why scope a queryset?**  
A. To style HTML.  
B. To increase response size.  
C. To restrict records available to the current user.  
D. To disable permissions.  
**Answer: C.** Queryset scoping protects record visibility.

**Q4. What should an API test verify?**  
A. Only that the endpoint exists.  
B. Only the editor theme.  
C. Only the response length.  
D. Status, response data, permissions and database effects.  
**Answer: D.** Tests must verify actual behavior.

**Q5. What is the strongest evidence of completion?**  
A. Passing tests and verified API behavior.  
B. A project folder only.  
C. A planned feature list.  
D. A screenshot of a code editor.  
**Answer: A.** Demonstrate working and tested behavior.

## 11. Interview preparation

**Q1. Explain capstone: rest api development and validation.**  
**Answer:** The capstone API exposes department, employee, project and task resources. Each endpoint should have a clear method, serializer, validation rule and response contract. Clients should not be allowed to set protected ownership fields or fields that should be controlled by server-side business logic.

**Q2. What is one important design decision?**  
**Answer:** Explain the API field, permission, queryset or test choice and why it matches the business requirement.

**Q3. How do you verify the deliverable?**  
**Answer:** Test successful, invalid, missing and unauthorized requests. Inspect the response and database state.

**Follow-up:** What would you improve before production?  
**Answer:** Identify additional monitoring, rate limiting, audit logging, security review, load testing or operational controls as appropriate.

## 12. Submission requirements

- [ ] Source code and migrations.
- [ ] API endpoint list and payload examples.
- [ ] Test cases and test output.
- [ ] Permission test evidence.
- [ ] Query/performance evidence where applicable.
- [ ] README and known limitations.
- [ ] No secrets or real personal data.

**Next lesson:** Day 93.
