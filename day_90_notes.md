# Day 90: Capstone: Database Design, Relationships and Django Models

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 1–88 — Python, OOP, Django, SQL, APIs, security, testing and deployment  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Database and Model Design

> **Capstone rule:** Keep the approved project scope. Do not add features before the required workflow works. Document what is implemented, what is tested and what remains incomplete.

## 1. Learning objectives

- Explain capstone: database design, relationships and django models.
- Produce the approved project artifact.
- Connect the artifact to the business requirements.
- Explain design decisions and trade-offs.
- Validate the work using acceptance criteria.
- Complete Database and Model Design.

## 2. Capstone business context

The capstone database represents users, departments, employees, projects, tasks and notifications. Use primary keys, foreign keys, one-to-one and one-to-many relationships deliberately. Model constraints should protect important business rules, and indexes should be added only where query patterns justify them.

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

1. Translate the Day 89 entities into database tables.
2. Define primary keys and field types.
3. Create Department and Employee models.
4. Create Project with a manager relationship.
5. Create Task with project and assigned employee relationships.
6. Create Notification linked to a user.
7. Choose on_delete behavior based on business meaning.
8. Add constraints for unique values and valid states where needed.
9. Generate and inspect migrations.
10. Apply migrations to a clean development database.
11. Create sample data and verify relationships using the ORM.

## 5. File-by-file implementation

### core/models.py

```python
from django.conf import settings
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees"
    )
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="managed_projects"
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default="PLANNED")

class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assigned_employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="assigned_tasks"
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default="TODO")
    due_date = models.DateField(null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

## 6. Explain the design or implementation

### core/models.py

1. `from django.conf import settings` — Part of the capstone design; explain how it supports the requirement.
2. `from django.db import models` — Part of the capstone design; explain how it supports the requirement.
3. ` ` — Part of the capstone design; explain how it supports the requirement.
4. `class Department(models.Model):` — Defines a model or business component.
5. `    name = models.CharField(max_length=100, unique=True)` — Part of the capstone design; explain how it supports the requirement.
6. `    description = models.TextField(blank=True)` — Part of the capstone design; explain how it supports the requirement.
7. ` ` — Part of the capstone design; explain how it supports the requirement.
8. `    def __str__(self):` — Part of the capstone design; explain how it supports the requirement.
9. `        return self.name` — Part of the capstone design; explain how it supports the requirement.
10. ` ` — Part of the capstone design; explain how it supports the requirement.
11. `class Employee(models.Model):` — Defines a model or business component.
12. `    user = models.OneToOneField(` — Defines a one-to-one relationship.
13. `        settings.AUTH_USER_MODEL,` — Part of the capstone design; explain how it supports the requirement.
14. `        on_delete=models.CASCADE,` — Part of the capstone design; explain how it supports the requirement.
15. `        related_name="employee"` — Part of the capstone design; explain how it supports the requirement.
16. `    )` — Part of the capstone design; explain how it supports the requirement.
17. `    department = models.ForeignKey(` — Defines a many-to-one relationship.
18. `        Department,` — Part of the capstone design; explain how it supports the requirement.
19. `        on_delete=models.PROTECT,` — Part of the capstone design; explain how it supports the requirement.
20. `        related_name="employees"` — Part of the capstone design; explain how it supports the requirement.
21. `    )` — Part of the capstone design; explain how it supports the requirement.
22. `    designation = models.CharField(max_length=100)` — Part of the capstone design; explain how it supports the requirement.
23. `    joining_date = models.DateField()` — Part of the capstone design; explain how it supports the requirement.
24. ` ` — Part of the capstone design; explain how it supports the requirement.
25. `    def __str__(self):` — Part of the capstone design; explain how it supports the requirement.
26. `        return self.user.get_full_name() or self.user.username` — Part of the capstone design; explain how it supports the requirement.
27. ` ` — Part of the capstone design; explain how it supports the requirement.
28. `class Project(models.Model):` — Defines a model or business component.
29. `    name = models.CharField(max_length=150)` — Part of the capstone design; explain how it supports the requirement.
30. `    description = models.TextField(blank=True)` — Part of the capstone design; explain how it supports the requirement.
31. `    manager = models.ForeignKey(` — Defines a many-to-one relationship.
32. `        Employee,` — Part of the capstone design; explain how it supports the requirement.
33. `        on_delete=models.PROTECT,` — Part of the capstone design; explain how it supports the requirement.
34. `        related_name="managed_projects"` — Part of the capstone design; explain how it supports the requirement.
35. `    )` — Part of the capstone design; explain how it supports the requirement.
36. `    start_date = models.DateField()` — Part of the capstone design; explain how it supports the requirement.
37. `    end_date = models.DateField(null=True, blank=True)` — Part of the capstone design; explain how it supports the requirement.
38. `    status = models.CharField(max_length=20, default="PLANNED")` — Part of the capstone design; explain how it supports the requirement.
39. ` ` — Part of the capstone design; explain how it supports the requirement.
40. `class Task(models.Model):` — Defines a model or business component.
41. `    project = models.ForeignKey(` — Defines a many-to-one relationship.
42. `        Project,` — Part of the capstone design; explain how it supports the requirement.
43. `        on_delete=models.CASCADE,` — Part of the capstone design; explain how it supports the requirement.
44. `        related_name="tasks"` — Part of the capstone design; explain how it supports the requirement.
45. `    )` — Part of the capstone design; explain how it supports the requirement.
46. `    assigned_employee = models.ForeignKey(` — Defines a many-to-one relationship.
47. `        Employee,` — Part of the capstone design; explain how it supports the requirement.
48. `        on_delete=models.PROTECT,` — Part of the capstone design; explain how it supports the requirement.
49. `        related_name="assigned_tasks"` — Part of the capstone design; explain how it supports the requirement.
50. `    )` — Part of the capstone design; explain how it supports the requirement.
51. `    title = models.CharField(max_length=150)` — Part of the capstone design; explain how it supports the requirement.
52. `    description = models.TextField(blank=True)` — Part of the capstone design; explain how it supports the requirement.
53. `    status = models.CharField(max_length=20, default="TODO")` — Part of the capstone design; explain how it supports the requirement.
54. `    due_date = models.DateField(null=True, blank=True)` — Part of the capstone design; explain how it supports the requirement.
55. ` ` — Part of the capstone design; explain how it supports the requirement.
56. `class Notification(models.Model):` — Defines a model or business component.
57. `    user = models.ForeignKey(` — Defines a many-to-one relationship.
58. `        settings.AUTH_USER_MODEL,` — Part of the capstone design; explain how it supports the requirement.
59. `        on_delete=models.CASCADE,` — Part of the capstone design; explain how it supports the requirement.
60. `        related_name="notifications"` — Part of the capstone design; explain how it supports the requirement.
61. `    )` — Part of the capstone design; explain how it supports the requirement.
62. `    message = models.TextField()` — Part of the capstone design; explain how it supports the requirement.
63. `    is_read = models.BooleanField(default=False)` — Part of the capstone design; explain how it supports the requirement.
64. `    created_at = models.DateTimeField(auto_now_add=True)` — Part of the capstone design; explain how it supports the requirement.

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

- [ ] All required entities are represented.
- [ ] ForeignKey and OneToOneField relationships match the design.
- [ ] on_delete behavior is deliberate.
- [ ] Required fields and nullability are appropriate.
- [ ] Constraints protect key business rules.
- [ ] Migrations apply successfully.
- [ ] Sample records can be created and related correctly.

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

**Planning prompt:** "Help me plan Database and Model Design for the Employee and Project Management System. Use the approved scope and list deliverables, dependencies, acceptance criteria and risks. Do not generate the entire project."

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

**Q1. Explain capstone: database design, relationships and django models.**  
**Answer:** The capstone database represents users, departments, employees, projects, tasks and notifications. Use primary keys, foreign keys, one-to-one and one-to-many relationships deliberately. Model constraints should protect important business rules, and indexes should be added only where query patterns justify them.

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

**Next lesson:** Day 91.
