# Phase 4 — Self-Learning Revision Plan and Audit

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Scope:** Days 42–54 — Django ORM, forms and authentication  
**Goal:** A TechPhile learner should be able to understand each lesson, implement its code, verify the result, diagnose common failures and complete the project without a trainer or mentor.

## 1. Approved roadmap

The source of truth is [09_Backend_Developer.md](09_Backend_Developer.md). Keep the approved topics and mini-project titles unchanged.

| Day | Approved topic | Approved mini-project | Documentation status |
|---:|---|---|---|
| 42 | CRUD operations: Create, Read, Update and Delete | Employee CRUD Application | Revised |
| 43 | Advanced Django ORM: filter, exclude, get, order_by and values | Advanced Product Search | Revised |
| 44 | Query optimization basics: select_related and prefetch_related | Optimized Order Management System | Revised |
| 45 | Database constraints, field validation and model validation | Data Integrity Management System | Revised |
| 46 | Django authentication system and user model | User Account Management | Pending |
| 47 | User registration, login and logout | User Authentication Application | Pending |
| 48 | Password management, password reset and secure password storage | Password Recovery System | Pending |
| 49 | Django sessions, cookies and session management | Session-Based Shopping Cart | Pending |
| 50 | Authorization, permissions and role-based access | Role-Based Employee Portal | Pending |
| 51 | Custom user models and user profile management | Custom User Profile System | Pending |
| 52 | Django messages framework and application feedback | User Notification Application | Pending |
| 53 | Pagination, search and filtering in Django applications | Paginated Product Catalog | Pending |
| 54 | Complete Django application integration and validation | Job Portal Web Application | Pending |

## 2. Phase 4 continuity architecture

The lessons use one evolving Django project. The existing Phase 3 `profiles` app is preserved.

~~~text
student_portal/
├── config/
├── profiles/      # Existing Phase 3 Student and Employee features
├── catalog/       # Day 43 Product search and catalog rules
└── orders/        # Day 44 Order and OrderItem relationships
~~~

### Day 42 — Employee CRUD

Uses the existing Employee model in profiles. Adds create, read, update and delete pages. It does not introduce a second Employee model.

### Day 43 — Product search

Creates the catalog app and Product model. Teaches QuerySets, filter(), exclude(), get(), order_by(), values(), field lookups, Q objects, query-string validation and a browser search page.

### Day 44 — Order query optimization

Creates the orders app and Order / OrderItem models. OrderItem refers to Product from catalog. Learners reproduce an N+1 query pattern, then compare select_related() and prefetch_related() using query measurements and tests.

### Day 45 — Product data integrity

Extends the same Product model from Day 43. Adds field validators, model clean(), UniqueConstraint and CheckConstraint. Learners inspect existing records before applying constraints and distinguish ValidationError from IntegrityError.

## 3. Self-learning standard

Every revised lesson is expected to include:

1. Accurate day title, duration, level and prerequisites.
2. Measurable learning objectives.
3. A realistic business situation and plain-language explanation.
4. Exact starting directory and environment checks.
5. File map and exact file paths.
6. Complete code examples with required imports and context.
7. Explanations of important lines, arguments and methods.
8. Expected terminal, browser and database behavior.
9. Common errors with likely causes and practical fixes.
10. A guided implementation.
11. An independent mini-project retaining the approved title.
12. Acceptance tests and evidence to submit.
13. Knowledge check and answer key.
14. Five topic-specific MCQs with explanations.
15. A separate interview guide with model answers and scenarios.
16. A completion checklist and connection to the next day.

A long document is not automatically a good lesson. Every section must help a learner perform, understand or verify the work.

## 4. Day 43–45 revision record

### Day 43 — Advanced Django ORM

**Revised files**
- [day_43_notes.md](day_43_notes.md)
- [day_43_interview.md](day_43_interview.md)

**Included**
- QuerySet versus list and lazy evaluation.
- Separate catalog app and Product model.
- filter(), exclude(), get(), order_by() and values().
- icontains, gte, lte, in and range.
- Q objects for OR conditions.
- count(), exists(), first() and SQL inspection.
- Validated GET search form, safe sort allow-list, product list and detail pages.
- Missing-object and invalid-query handling.
- Advanced Product Search project, acceptance checks, answer key and MCQs.

### Day 44 — Query optimization

**Revised files**
- [day_44_notes.md](day_44_notes.md)
- [day_44_interview.md](day_44_interview.md)

**Included**
- N+1 query explanation.
- Order and OrderItem models related to the Day 43 Product.
- select_related() for ForeignKey / OneToOneField.
- prefetch_related() for reverse and many-to-many collections.
- Nested prefetch and Prefetch with a customized queryset.
- Query measurement and assertNumQueries().
- Order list, order detail and item report.
- Optimized Order Management System project and interview practice.

### Day 45 — Data integrity

**Revised files**
- [day_45_notes.md](day_45_notes.md)
- [day_45_interview.md](day_45_interview.md)

**Included**
- Field validation, model validation and database constraints.
- MinValueValidator and model clean().
- full_clean() stages and the important save() distinction.
- UniqueConstraint and CheckConstraint.
- Existing-data inspection before a unique constraint migration.
- Safe IntegrityError demonstration with transaction.atomic().
- ValidationError versus IntegrityError.
- Data Integrity Management System project, acceptance checks and interview practice.

## 5. Important technical boundaries

- QuerySets are lazy, but evaluation depends on the operation performed.
- get() raises DoesNotExist or MultipleObjectsReturned if the query does not match exactly one row.
- select_related() is for single-valued relations; prefetch_related() is for collections.
- A nested prefetch of `items__product` normally executes three queries: Order, OrderItem and Product. A customized Prefetch queryset that select_related()s Product can reduce this to two for the demonstrated relationship.
- Model.save() does not automatically call full_clean().
- Application validation gives useful feedback; database constraints are the final protection for the rules they enforce.
- Adding a unique constraint can fail when existing data contains duplicates. Inspect and resolve data safely before applying the migration.
- Day 42 CRUD pages are learning examples, not production-protected employee management. Authentication and authorization are later lessons.

## 6. Validation status and limitations

| Validation item | Status |
|---|---|
| Day 42–45 class-note and interview manuscripts revised | Complete |
| Day 42–45 static Markdown structure and links | Static audit added; CI result pending |
| Day 43–45 code executed in a clean Django learner project | Pending |
| Catalog and orders migration workflow executed | Pending |
| Query-count assertions executed against the documented models | Pending |
| Constraint migration tested against existing and duplicate data | Pending |
| End-to-end browser workflow tested on Windows | Pending |
| Independent beginner usability pilot | Not conducted |

A documentation-only CI pass must not be described as Django runtime validation. A plausible code sample is not proof that it runs.

## 7. Readiness decision

**Days 42–45: documentation revision complete; runtime and beginner validation pending.**

Runtime and beginner validation pending means the Day 43–45 application code still needs to be executed in a clean Django project and independently followed by beginner learners.

**Phase 4 overall: in progress.** Days 46–54 still need the same self-learning revision. Do not claim that all of Phase 4 is complete or that the pathway is mentor-free until the remaining lessons, integrated runtime checks and beginner pilot have passed.
