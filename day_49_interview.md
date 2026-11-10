# Day 49: Interview Questions — Django Sessions, Cookies and Session Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 49 class notes](day_49_notes.md)  
**Approved mini-project:** Session-Based Shopping Cart

## Core technical questions

### Q1. Explain django sessions, cookies and session management.
**Answer:** A cookie is small data stored by the browser and sent with matching requests. Django sessions store user-specific state on the server or configured session backend; the browser usually holds a session identifier cookie. Session data can support a shopping cart, but important business data should be persisted appropriately.

### Q2. Which Django APIs or settings are involved?
**Answer:** profiles/views.py, settings.py — security-oriented cookie settings. Explain their role in the workflow.

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

## Project viva — Session-Based Shopping Cart

1. What problem does it solve?
2. Which Django APIs are used?
3. Which security settings matter?
4. What happens for an invalid or unauthorized request?
5. How did you test the workflow?
6. What secrets did you keep out of Git?
7. What would you improve for production?

## Rapid revision

- **1.** Explain the difference between a browser cookie and server-side session data.
- **2.** Inspect SESSION_ENGINE and session middleware settings.
- **3.** Read a cart dictionary from request.session.
- **4.** Update session data after a POST action.
- **5.** Use a POST form with CSRF token for add and clear operations.
- **6.** Set appropriate session expiry when the use case requires it.
- **7.** Explain secure cookie settings and HTTPS requirements.
- **8.** Test the cart across page requests and after logout/session expiry.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Explain the security risks.
- [ ] Demonstrate positive and negative cases.
- [ ] Explain server-side enforcement.
- [ ] Present Session-Based Shopping Cart without exposing secrets.
