# Day 46: Interview Questions — Django Authentication System and User Model

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 46 class notes](day_46_notes.md)  
**Approved mini-project:** User Account Management

## Core technical questions

### Q1. Explain django authentication system and user model.
**Answer:** Django authentication identifies users and supports password verification, sessions and permissions. The built-in user model includes fields such as username, password hash, email and staff/superuser flags. Use get_user_model() when application code needs the active user model, and settings.AUTH_USER_MODEL for model relationship declarations.

### Q2. Which Django APIs or files are involved?
**Answer:** profiles/views.py, Model relationship example. Explain the role of each API and how the feature is verified.

### Q3. What is a common mistake?
**Answer:** Authentication app is installed. Test the behavior rather than assuming the code is correct.

### Q4. How do you verify the implementation?
**Answer:** Use local test data and accounts, exercise valid and invalid cases, inspect the database/session and verify access restrictions.

### Q5. What security concern should you explain?
**Answer:** Protect credentials, validate data, enforce permissions and avoid exposing private information.

## Scenario-based questions

### Q6. A user can log in but should not be able to modify another employee's record. What is missing?
**Suggested answer:** Authorization. The application must check permissions for the requested operation and object, not merely check that the user is authenticated.

### Q7. Invalid data is being stored. What do you inspect?
**Suggested answer:** Field validation, model validation, database constraints and the exact save path. Remember that model.save() does not automatically call full_clean().

## Project viva — User Account Management

1. What problem does it solve?
2. Which validation or authentication APIs are used?
3. How are invalid values rejected?
4. How are credentials handled safely?
5. How are access restrictions verified?
6. What test cases did you run?
7. What would you improve for production?

## Rapid revision

- **1.** Inspect Django's built-in authentication app in INSTALLED_APPS.
- **2.** Understand the default User fields and password hashing.
- **3.** Use get_user_model() in application code that needs the active model class.
- **4.** Use settings.AUTH_USER_MODEL in model relationships.
- **5.** Create a user through create_user() rather than setting a raw password field.
- **6.** Distinguish regular user, staff user and superuser.
- **7.** Explain authentication versus authorization.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the security implications.
- [ ] Demonstrate valid and invalid workflows.
- [ ] Explain authentication versus authorization.
- [ ] Present User Account Management without exposing secrets.
