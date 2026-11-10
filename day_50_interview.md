# Day 50: Interview Questions — Authorization, Permissions and Role-Based Access

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 50 class notes](day_50_notes.md)  
**Approved mini-project:** Role-Based Employee Portal

## Core technical questions

### Q1. Explain authorization, permissions and role-based access.
**Answer:** Authentication confirms a user's identity. Authorization determines whether that user can perform an action. Django includes model permissions, groups, permission decorators and user permission methods. A role can be represented using groups and assigned permissions; sensitive object-level decisions may require explicit checks or a dedicated permission system.

### Q2. Which Django APIs or settings are involved?
**Answer:** profiles/views.py, Django shell — inspect permissions. Explain their role in the workflow.

### Q3. What is a common security mistake?
**Answer:** Trusting client-side checks, exposing credentials or failing to enforce server-side permissions. Explain the exact risk for this topic.

### Q4. How do you verify the implementation?
**Answer:** Use local test accounts and data. Test both valid and denied cases and inspect the server-side response.

### Q5. Why is security configuration environment-specific?
**Answer:** Local development and production have different network and secret-management requirements. Production must use secure transport and protected configuration.

## Scenario questions

### Q6. A user can perform an action that should be restricted. What do you inspect?
**Suggested answer:** Confirm the view has server-side authentication and authorization checks, inspect the user's permissions/group membership and test direct URL access.

### Q7. How do you test safely?
**Suggested answer:** Use fake users, local test data and test credentials. Never share a real password, reset token or session cookie.

## Project viva — Role-Based Employee Portal

1. What problem does it solve?
2. Which Django APIs are used?
3. Which security settings matter?
4. What happens for an invalid or unauthorized request?
5. How did you test the workflow?
6. What secrets did you keep out of Git?
7. What would you improve for production?

## Rapid revision

- **1.** Explain authentication versus authorization.
- **2.** Inspect default model permissions created by Django.
- **3.** Create groups such as HR and Manager.
- **4.** Assign appropriate model permissions to groups.
- **5.** Check user.has_perm() before protected operations.
- **6.** Use login_required to require authentication.
- **7.** Use permission_required for a model permission.
- **8.** Test access as anonymous, normal and permitted users.
- **9.** Explain why hiding a button in HTML is not sufficient authorization.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Explain the security risks.
- [ ] Demonstrate positive and negative cases.
- [ ] Explain server-side enforcement.
- [ ] Present Role-Based Employee Portal without exposing secrets.
