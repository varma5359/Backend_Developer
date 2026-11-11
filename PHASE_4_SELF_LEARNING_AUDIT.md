# Phase 4 — Self-Learning Revision Plan and Audit

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Scope:** Days 42–54 — Django ORM, Forms and Authentication  
**Goal:** TechPhile learners should learn concepts, build projects and verify their own work without a trainer or mentor.

## 1. Approved scope

The authoritative roadmap is [09_Backend_Developer.md](09_Backend_Developer.md). The approved sequence and mini-project titles must not be silently changed.

| Day | Approved topic | Approved mini-project | Revision status |
|---:|---|---|---|
| 42 | CRUD operations: Create, Read, Update and Delete | Employee CRUD Application | Rewritten self-learning lesson and interview guide |
| 43 | Advanced Django ORM: filter, exclude, get, order_by and values | Advanced Product Search | Pending |
| 44 | Query optimization basics: select_related and prefetch_related | Optimized Order Management System | Pending |
| 45 | Database constraints, field validation and model validation | Data Integrity Management System | Pending |
| 46 | Django authentication system and user model | User Account Management | Pending |
| 47 | User registration, login and logout | User Authentication Application | Pending |
| 48 | Password management, password reset and secure password storage | Password Recovery System | Pending |
| 49 | Django sessions, cookies and session management | Session-Based Shopping Cart | Pending |
| 50 | Authorization, permissions and role-based access | Role-Based Employee Portal | Pending |
| 51 | Custom user models and user profile management | Custom User Profile System | Pending |
| 52 | Django messages framework and application feedback | User Notification Application | Pending |
| 53 | Pagination, search and filtering in Django applications | Paginated Product Catalog | Pending |
| 54 | Complete Django application integration and validation | Job Portal Web Application | Pending |

## 2. Initial repository findings

The existing Phase 4 manuscripts were present, but they were not ready to be described as mentor-free.

The initial inspection found recurring quality problems:

- Trainer-dependent instructions remained in the notes.
- Prerequisite ranges sometimes included the current day or future days.
- Some code walkthroughs contained placeholder explanations instead of explaining the actual line.
- Some examples did not provide a complete file-by-file path.
- Expected terminal, browser and database results were often too general.
- Some lessons used app files without explaining how they connect to the Phase 3 project.
- Interview guides often used generic answers instead of day-specific model answers.

## 3. Continuity decisions

### Existing Phase 3 project

The continuous project is the learner's student_portal project with the config project package and profiles app.

The Employee model introduced in Phase 3 contains employee_code (unique), full_name, email (unique), salary, joining_date, is_active and created_at.

The Phase 3 forms file also contains StudentRegistrationForm. Phase 4 lessons must preserve that form and add new form classes without silently replacing earlier work.

### Day 42 implementation boundary

Day 42 adds Employee CRUD pages around the existing Employee model. It does not require a new Employee model or a schema migration.

EmployeeForm must use an explicit field allow-list and exclude the automatically populated created_at field. Update must pass the existing instance. Delete must use a confirmation page and POST, not a destructive GET.

### Authentication boundary

Days 42–45 teach CRUD, ORM querying, optimization and data integrity. User authentication begins on Day 46. Do not claim that Day 42 employee pages are production-protected. Explain this limitation clearly.

## 4. Self-learning acceptance standard

A revised daily lesson must provide:

1. Day title, approved topic, duration, level and accurate prerequisites.
2. Measurable learning objectives.
3. A business problem and plain-language mental model.
4. Exact starting folder and environment checks.
5. A file map and exact file paths.
6. Complete runnable examples with imports and context.
7. Explanation of important code lines and parameters.
8. Multiple meaningful examples for important concepts.
9. Expected terminal, browser or database behavior.
10. Common errors with likely causes and actionable fixes.
11. A guided implementation.
12. An independent mini-project using the approved title.
13. Acceptance tests and evidence to submit.
14. A knowledge check with answer key.
15. Five day-specific MCQs with explanations.
16. A separate interview guide with model answers and scenarios.
17. A completion checklist and connection to the next day.

Do not add length by repeating generic explanations. Every section must help the learner perform, understand or verify the work.

## 5. Validation policy

- Static Markdown review is not runtime validation.
- A code sample is not proven to work merely because it looks plausible.
- Runtime validation requires executing the relevant Django checks and tests in a known environment.
- A mentor-free claim requires an actual beginner pilot in addition to static and runtime checks.
- Do not delete or reset learner databases to make examples repeatable.
- Use unique sample values and explain how to avoid duplicate unique values.
- Use a dedicated test record for destructive operations.
- Preserve prior project files and earlier lesson functionality.

## 6. Current revision status

| Deliverable | Status |
|---|---|
| Day 42 class notes | Rewritten with self-paced instructions and complete CRUD walkthrough |
| Day 42 interview guide | Rewritten with technical model answers, code-reading, scenarios and project viva |
| Days 43–54 class notes | Pending revision |
| Days 43–54 interview guides | Pending revision |
| Phase 4 integrated reference application | Not yet created or runtime-validated |
| Phase 4 beginner usability pilot | Not yet conducted |

## 7. Final readiness decision

**Phase 4 is in progress.** Day 42 has received a self-learning rewrite. The remaining twelve days still require revision and validation. Do not label Phase 4 mentor-free until all thirteen days have passed content review, integrated examples have been runtime-tested, and beginner usability evidence has been collected.
