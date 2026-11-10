# Day 91: Capstone: Application Development and Business Logic

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 1–88 — Python, OOP, Django, SQL, APIs, security, testing and deployment  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Core Backend Application

> **Capstone rule:** Keep the approved project scope. Do not add features before the required workflow works. Document what is implemented, what is tested and what remains incomplete.

## 1. Learning objectives

- Explain capstone: application development and business logic.
- Produce the approved project artifact.
- Connect the artifact to the business requirements.
- Explain design decisions and trade-offs.
- Validate the work using acceptance criteria.
- Complete Core Backend Application.

## 2. Capstone business context

The core application implements business workflows using Django models, forms or serializers, views and reusable services. Keep HTTP request handling separate from business rules. Validate state transitions, check user permissions and group related database writes in transactions when partial updates would be unsafe.

## 3. Project scope

### Core modules
1. User accounts and role-based access.
2. Department management.
3. Employee management.
4. Project management.
5. Task assignment and status tracking.
6. Notifications.
7. REST API access for frontend/mobile clients.
8. Automated tests and deployment.

### Main user roles

| Role | Responsibility |
|---|---|
| Administrator | Manages system configuration and user access |
| HR | Manages employee and department information |
| Project manager | Creates projects and assigns tasks |
| Employee | Views assigned work and updates permitted task status |

## 4. Required work for today

1. Create the Django apps and register them.
2. Implement employee and department management workflows.
3. Implement project creation and manager assignment.
4. Implement task creation, assignment and status transitions.
5. Move reusable business rules into service functions.
6. Move reusable read queries into selectors where useful.
7. Use transactions for related database writes.
8. Validate task states and assignment rules.
9. Add notifications for important events where required.
10. Write a short README for each main workflow.

## 5. File-by-file implementation

### core/services.py

```python
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import Task

@transaction.atomic
def assign_task(task_id, employee):
    task = Task.objects.select_for_update().get(pk=task_id)

    if not employee.user.is_active:
        raise ValidationError("Employee account is inactive.")

    task.assigned_employee = employee
    task.save(update_fields=["assigned_employee"])
    return task

@transaction.atomic
def update_task_status(task, new_status):
    allowed = {"TODO", "IN_PROGRESS", "BLOCKED", "DONE"}
    if new_status not in allowed:
        raise ValidationError("Unsupported task status.")

    task.status = new_status
    task.save(update_fields=["status"])
    return task
```

### core/selectors.py

```python
from .models import Project, Task

def get_active_projects():
    return (
        Project.objects
        .filter(status__in=["PLANNED", "ACTIVE"])
        .select_related("manager__user")
        .order_by("name")
    )

def get_employee_tasks(employee):
    return (
        Task.objects
        .filter(assigned_employee=employee)
        .select_related("project")
        .order_by("due_date")
    )
```

## 6. Explain the design or implementation

### core/services.py

1. `from django.core.exceptions import ValidationError` — Reports a business rule violation.
2. `from django.db import transaction` — Part of the capstone design; explain how it supports the requirement.
3. `from .models import Task` — Part of the capstone design; explain how it supports the requirement.
4. ` ` — Part of the capstone design; explain how it supports the requirement.
5. `@transaction.atomic` — Protects related database operations as one transaction.
6. `def assign_task(task_id, employee):` — Part of the capstone design; explain how it supports the requirement.
7. `    task = Task.objects.select_for_update().get(pk=task_id)` — Part of the capstone design; explain how it supports the requirement.
8. ` ` — Part of the capstone design; explain how it supports the requirement.
9. `    if not employee.user.is_active:` — Part of the capstone design; explain how it supports the requirement.
10. `        raise ValidationError("Employee account is inactive.")` — Reports a business rule violation.
11. ` ` — Part of the capstone design; explain how it supports the requirement.
12. `    task.assigned_employee = employee` — Part of the capstone design; explain how it supports the requirement.
13. `    task.save(update_fields=["assigned_employee"])` — Part of the capstone design; explain how it supports the requirement.
14. `    return task` — Part of the capstone design; explain how it supports the requirement.
15. ` ` — Part of the capstone design; explain how it supports the requirement.
16. `@transaction.atomic` — Protects related database operations as one transaction.
17. `def update_task_status(task, new_status):` — Part of the capstone design; explain how it supports the requirement.
18. `    allowed = {"TODO", "IN_PROGRESS", "BLOCKED", "DONE"}` — Part of the capstone design; explain how it supports the requirement.
19. `    if new_status not in allowed:` — Part of the capstone design; explain how it supports the requirement.
20. `        raise ValidationError("Unsupported task status.")` — Reports a business rule violation.
21. ` ` — Part of the capstone design; explain how it supports the requirement.
22. `    task.status = new_status` — Part of the capstone design; explain how it supports the requirement.
23. `    task.save(update_fields=["status"])` — Part of the capstone design; explain how it supports the requirement.
24. `    return task` — Part of the capstone design; explain how it supports the requirement.

### core/selectors.py

1. `from .models import Project, Task` — Part of the capstone design; explain how it supports the requirement.
2. ` ` — Part of the capstone design; explain how it supports the requirement.
3. `def get_active_projects():` — Part of the capstone design; explain how it supports the requirement.
4. `    return (` — Part of the capstone design; explain how it supports the requirement.
5. `        Project.objects` — Part of the capstone design; explain how it supports the requirement.
6. `        .filter(status__in=["PLANNED", "ACTIVE"])` — Part of the capstone design; explain how it supports the requirement.
7. `        .select_related("manager__user")` — Part of the capstone design; explain how it supports the requirement.
8. `        .order_by("name")` — Part of the capstone design; explain how it supports the requirement.
9. `    )` — Part of the capstone design; explain how it supports the requirement.
10. ` ` — Part of the capstone design; explain how it supports the requirement.
11. `def get_employee_tasks(employee):` — Part of the capstone design; explain how it supports the requirement.
12. `    return (` — Part of the capstone design; explain how it supports the requirement.
13. `        Task.objects` — Part of the capstone design; explain how it supports the requirement.
14. `        .filter(assigned_employee=employee)` — Part of the capstone design; explain how it supports the requirement.
15. `        .select_related("project")` — Part of the capstone design; explain how it supports the requirement.
16. `        .order_by("due_date")` — Part of the capstone design; explain how it supports the requirement.
17. `    )` — Part of the capstone design; explain how it supports the requirement.

## 7. Architecture flow

```text
Frontend / API client
      ↓ HTTPS / REST
Django URL routing
      ↓
Authentication and permissions
      ↓
Serializer / validation
      ↓
View / service layer
      ↓
Django ORM
      ↓
PostgreSQL
      ↓
Response / notification
```

## 8. Validation and review

- [ ] Core CRUD workflows work.
- [ ] Business rules are enforced server-side.
- [ ] Invalid task status is rejected.
- [ ] Task assignment validates employee state.
- [ ] Related writes use transactions where needed.
- [ ] Views remain focused on HTTP handling.
- [ ] Queries retrieve the intended records.

## 9. Suggested project structure

```text
employee_project_management/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
├── departments/
├── employees/
├── projects/
├── tasks/
├── notifications/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

Adapt app boundaries if there is a clear reason, but keep responsibilities easy to locate.

## 10. AI-assisted capstone workflow

**Planning prompt:** "Help me plan Core Backend Application for the Employee and Project Management System. Use the approved scope and list deliverables, dependencies, acceptance criteria and risks. Do not generate the entire project."

**Implementation prompt:** "Guide me through one component at a time. Explain the file path, code and test. Wait for my output before continuing."

**Debugging prompt:** "Here is my code, request, response and traceback. Trace the failure from URL to view to service to database."

**Review prompt:** "Review this deliverable against the approved requirements. Identify missing behavior, security risks, test gaps and documentation gaps."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's capstone deliverable?**  
A. Produce a verified part of the final backend system.  
B. Add unrelated features.  
C. Replace the approved project.  
D. Skip requirements.  
**Answer: A.** Each capstone day contributes a defined deliverable.

**Q2. What should be used to verify a requirement?**  
A. A feature name only.  
B. An acceptance criterion and test evidence.  
C. A code screenshot only.  
D. A verbal assumption.  
**Answer: B.** Requirements need observable acceptance criteria.

**Q3. Why separate business logic from views?**  
A. To increase file count.  
B. To avoid tests.  
C. To make reusable behavior easier to test and maintain.  
D. To disable validation.  
**Answer: C.** Clear responsibilities support maintainability.

**Q4. What should be documented?**  
A. Only successful features.  
B. Only planned features.  
C. No limitations.  
D. Implemented scope, tests, limitations and known issues.  
**Answer: D.** Honest documentation is part of a professional deliverable.

**Q5. What is the strongest evidence of completion?**  
A. Deliverable, validation results and explanation.  
B. A long code file.  
C. A project title.  
D. A screenshot of VS Code.  
**Answer: A.** Show working evidence and explain the result.

## 12. Interview preparation

**Q1. Explain capstone: application development and business logic.**  
**Answer:** The core application implements business workflows using Django models, forms or serializers, views and reusable services. Keep HTTP request handling separate from business rules. Validate state transitions, check user permissions and group related database writes in transactions when partial updates would be unsafe.

**Q2. What design decision did you make?**  
**Answer:** Identify one decision, explain alternatives and why your choice meets the requirement.

**Q3. How do you verify the deliverable?**  
**Answer:** Compare it with acceptance criteria, run the relevant tests and capture evidence.

**Follow-up:** What remains outside the scope?  
**Answer:** State the known limitations honestly and explain what would be needed to implement them.

## 13. Submission requirements

- [ ] Source files or design artifacts.
- [ ] README with setup and explanation.
- [ ] Test cases and evidence.
- [ ] Known limitations.
- [ ] Security and privacy considerations.
- [ ] Clear link to the approved capstone requirements.

**Next lesson:** Day 92.
