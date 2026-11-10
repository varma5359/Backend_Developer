# Day 47: Interview Questions — User Registration, Login and Logout

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 47 class notes](day_47_notes.md)  
**Approved mini-project:** User Authentication Application

## Core technical questions

### Q1. Explain user registration, login and logout.
**Answer:** Registration creates an account after validating the submitted details. Login verifies credentials and creates an authenticated session. Logout ends the current authenticated session. Django provides UserCreationForm, authenticate(), login(), logout() and login_required for common workflows.

### Q2. Which Django APIs or files are involved?
**Answer:** profiles/views.py, Login form template, Logout form template. Explain the role of each API and how the feature is verified.

### Q3. What is a common mistake?
**Answer:** Valid registration creates a user. Test the behavior rather than assuming the code is correct.

### Q4. How do you verify the implementation?
**Answer:** Use local test data and accounts, exercise valid and invalid cases, inspect the database/session and verify access restrictions.

### Q5. What security concern should you explain?
**Answer:** Protect credentials, validate data, enforce permissions and avoid exposing private information.

## Scenario-based questions

### Q6. A user can log in but should not be able to modify another employee's record. What is missing?
**Suggested answer:** Authorization. The application must check permissions for the requested operation and object, not merely check that the user is authenticated.

### Q7. Invalid data is being stored. What do you inspect?
**Suggested answer:** Field validation, model validation, database constraints and the exact save path. Remember that model.save() does not automatically call full_clean().

## Project viva — User Authentication Application

1. What problem does it solve?
2. Which validation or authentication APIs are used?
3. How are invalid values rejected?
4. How are credentials handled safely?
5. How are access restrictions verified?
6. What test cases did you run?
7. What would you improve for production?

## Rapid revision

- **1.** Use UserCreationForm for account registration.
- **2.** Display the form on GET and bind POST data on submission.
- **3.** Save the user only after form validation.
- **4.** Use authenticate() to verify submitted credentials.
- **5.** Call login() only when authenticate() returns a user.
- **6.** Protect a dashboard using login_required.
- **7.** Use POST for logout and include CSRF token.
- **8.** Test valid, invalid and unauthenticated access.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the security implications.
- [ ] Demonstrate valid and invalid workflows.
- [ ] Explain authentication versus authorization.
- [ ] Present User Authentication Application without exposing secrets.
