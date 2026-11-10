# Day 51: Interview Questions — Custom User Models and User Profile Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 51 class notes](day_51_notes.md)  
**Approved mini-project:** Custom User Profile System

## Core technical questions

### Q1. Explain custom user models and user profile management.
**Answer:** A custom user model lets a project define its user identity fields and authentication behavior. Django recommends deciding whether to use a custom user model at the start of a project. Set AUTH_USER_MODEL before the first migrations that create user-related tables. Changing user models after a project has already migrated can require complex data and migration work.

### Q2. Which Django components are involved?
**Answer:** accounts/models.py, profiles/models.py, config/settings.py. Explain how each component contributes to the feature.

### Q3. What is one common implementation mistake?
**Answer:** Custom user class inherits from AbstractUser. Test the feature with realistic data and verify the database result.

### Q4. How do you verify the user workflow?
**Answer:** Use separate test accounts, submit valid and invalid inputs, inspect the response and verify the stored records.

### Q5. What production concern should you mention?
**Answer:** Data integrity, permissions, privacy, secure configuration and integration test coverage.

## Scenario questions

### Q6. A feature works for one user but fails for another. What do you inspect?
**Suggested answer:** Check the active user model, group membership, permissions, session, request context and database ownership rules.

### Q7. How do you prevent the browser from choosing a protected owner field?
**Suggested answer:** Exclude the field from the user-facing form and assign it server-side from request.user.

## Project viva — Custom User Profile System

1. What is the business problem?
2. Which models and relationships are used?
3. Which form fields are exposed?
4. How is authentication or ownership handled?
5. Which database constraints are important?
6. How are valid and invalid journeys tested?
7. What would you improve for production?

## Rapid revision

- **1.** Explain why a project may need a custom user model.
- **2.** Create the accounts app before the initial project migrations.
- **3.** Define User inheriting from AbstractUser.
- **4.** Set AUTH_USER_MODEL in settings.py before initial migrations.
- **5.** Use settings.AUTH_USER_MODEL in relationship fields.
- **6.** Create a separate UserProfile model for additional profile data.
- **7.** Create migrations and apply them in a fresh learning database.
- **8.** Use get_user_model() in application code.
- **9.** Explain why changing user model later is difficult.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Identify connected Django components.
- [ ] Demonstrate a complete workflow.
- [ ] Explain validation and permissions.
- [ ] Present Custom User Profile System and evidence.
