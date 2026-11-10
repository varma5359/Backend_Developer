# Day 65: Interview Questions — Role-Based API Permissions and Object-Level Permissions

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 65 class notes](day_65_notes.md)  
**Approved mini-project:** Role-Based Access API

## Core technical questions

### Q1. Explain role-based api permissions and object-level permissions.
**Answer:** Role-based access assigns permissions according to a user's role, often represented by Django groups. Object-level permissions decide whether the user may access a specific record. A user may have permission to view employees generally but still be restricted from viewing or editing another employee's private record.

### Q2. Which DRF classes or settings are involved?
**Answer:** profiles/permissions.py, profiles/api_views.py. Explain how the configuration affects incoming requests.

### Q3. What is one common security mistake?
**Answer:** Exposing tokens, failing to scope querysets or relying only on frontend access controls. Explain the specific risk.

### Q4. How do you verify the implementation?
**Answer:** Test with local accounts and safe test tokens, then exercise valid, invalid and unauthorized requests. Inspect status codes and result records.

### Q5. What should not be included in a public repository?
**Answer:** Passwords, API tokens, JWTs, session cookies, private keys and real personal data.

## Scenario questions

### Q6. A user can retrieve another user's record. What do you inspect?
**Suggested answer:** Queryset scoping, object-level permission checks and ownership relationships. Test direct API requests as different users.

### Q7. An API returns too many records. What do you add?
**Suggested answer:** Appropriate filters and pagination, with explicit searchable and orderable fields.

## Project viva — Role-Based Access API

1. What is the purpose?
2. Which authentication/permission/filter components are used?
3. How are credentials supplied?
4. How are unauthorized requests handled?
5. How are result sets restricted?
6. How did you test the behavior?
7. What would you improve?

## Rapid revision

- **1.** Define the roles required by the business scenario.
- **2.** Create Django groups such as HR and Employee.
- **3.** Assign only the required model permissions to each group.
- **4.** Create a custom BasePermission class.
- **5.** Implement has_object_permission() for record-level checks.
- **6.** Filter get_queryset() so users cannot list records they do not own.
- **7.** Test own record, another user's record and HR access.
- **8.** Test write operations separately from safe read methods.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the configuration.
- [ ] Demonstrate valid and invalid requests.
- [ ] Explain the security boundary.
- [ ] Present Role-Based Access API with safe evidence.
