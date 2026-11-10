# Day 89: Capstone: Business Problem, Requirements and System Design

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 1–88 — Python, OOP, Django, SQL, APIs, security, testing and deployment  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Backend Project Requirements

> **Capstone rule:** Keep the approved project scope. Do not add features before the required workflow works. Document what is implemented, what is tested and what remains incomplete.

## 1. Learning objectives

- Explain capstone: business problem, requirements and system design.
- Produce the approved project artifact.
- Connect the artifact to the business requirements.
- Explain design decisions and trade-offs.
- Validate the work using acceptance criteria.
- Complete Backend Project Requirements.

## 2. Capstone business context

The capstone is an Employee and Project Management System. An organization currently tracks employees, departments, projects and tasks in spreadsheets. The backend should centralize these records, support controlled access, expose REST APIs and provide an auditable workflow. Day 89 turns the business need into clear requirements and a system design before implementation begins.

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

1. Write the business problem and target users.
2. Identify roles: administrator, HR, project manager and employee.
3. Define functional requirements for employees, departments, projects, tasks and notifications.
4. Define non-functional requirements for security, reliability, maintainability and performance.
5. Write user stories and acceptance criteria.
6. Identify core entities and relationships.
7. Draw the high-level architecture and request flow.
8. List API resources and likely operations.
9. Record assumptions, constraints, risks and out-of-scope features.
10. Create a day-by-day implementation plan for Days 90–96.

## 5. File-by-file implementation



## 6. Explain the design or implementation

For the requirements document, explain each user role, functional requirement, non-functional requirement, entity and acceptance criterion. For system design, trace a client request through the API, business logic and database.

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

- [ ] Problem statement is clear and business-focused.
- [ ] Roles and responsibilities are defined.
- [ ] Functional requirements are testable.
- [ ] Non-functional requirements are measurable where possible.
- [ ] Core entities and relationships are identified.
- [ ] Architecture and API boundaries are documented.
- [ ] Risks and assumptions are recorded.
- [ ] Acceptance criteria are agreed before coding.

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

**Planning prompt:** "Help me plan Backend Project Requirements for the Employee and Project Management System. Use the approved scope and list deliverables, dependencies, acceptance criteria and risks. Do not generate the entire project."

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

**Q1. Explain capstone: business problem, requirements and system design.**  
**Answer:** The capstone is an Employee and Project Management System. An organization currently tracks employees, departments, projects and tasks in spreadsheets. The backend should centralize these records, support controlled access, expose REST APIs and provide an auditable workflow. Day 89 turns the business need into clear requirements and a system design before implementation begins.

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

**Next lesson:** Day 90.
