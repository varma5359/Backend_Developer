# Day 48: Interview Questions — Password Management, Password Reset and Secure Password Storage

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 48 class notes](day_48_notes.md)  
**Approved mini-project:** Password Recovery System

## Core technical questions

### Q1. Explain password management, password reset and secure password storage.
**Answer:** Django stores passwords using configured password hashers, not as readable plaintext. set_password() hashes a new password and check_password() verifies a candidate. Django includes password change and reset views/forms that can be configured with templates and email delivery.

### Q2. Which Django APIs or settings are involved?
**Answer:** Password API example, config/urls.py — built-in password views. Explain their role in the workflow.

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

## Project viva — Password Recovery System

1. What problem does it solve?
2. Which Django APIs are used?
3. Which security settings matter?
4. What happens for an invalid or unauthorized request?
5. How did you test the workflow?
6. What secrets did you keep out of Git?
7. What would you improve for production?

## Rapid revision

- **1.** Explain password hashing and why plaintext storage is unsafe.
- **2.** Use set_password() when setting a password programmatically.
- **3.** Use check_password() to verify a candidate password.
- **4.** Inspect Django's password validation settings.
- **5.** Understand built-in password change and reset views.
- **6.** Configure email backend for local development and production separately.
- **7.** Use generic user-facing reset messages to avoid account enumeration.
- **8.** Test valid, invalid and expired reset workflows.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Explain the security risks.
- [ ] Demonstrate positive and negative cases.
- [ ] Explain server-side enforcement.
- [ ] Present Password Recovery System without exposing secrets.
