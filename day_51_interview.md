# Day 51: Interview Guide — Custom User Models and User Profile Management

**Related class notes:** [Day 51 notes](day_51_notes.md)  
**Approved mini-project:** Custom User Profile System  
**Level:** Intermediate

## 1. Core technical questions

### Q1. What is a custom user model?
**Answer:** It is a project-defined Django model used for authentication. It is useful when the application's account identity or account-level fields differ from the default user model.

### Q2. What is AbstractUser?
**Answer:** AbstractUser is a Django abstract base model containing common user fields and behavior. A project can inherit from it and add fields while retaining much of Django's standard authentication functionality.

### Q3. What is AbstractBaseUser?
**Answer:** It is a more minimal base for custom authentication models. The developer must implement more of the user model behavior, manager configuration and permission integration. It is more flexible but requires more care.

### Q4. Which base class is suitable for adding one or two fields?
**Answer:** AbstractUser is usually the simpler choice when the project wants to keep standard Django authentication and add fields.

### Q5. What does AUTH_USER_MODEL do?
**Answer:** It identifies the model used by Django as the project's user model, for example accounts.User.

### Q6. When should AUTH_USER_MODEL be configured?
**Answer:** Before the first migrations that create user-related tables. Other models and authentication tables depend on the configured user model.

### Q7. Why is changing the user model after migrations difficult?
**Answer:** Existing database tables, foreign keys, migration dependencies and account data may reference the previous model. A later change can require complex schema and data migrations.

### Q8. What is the purpose of get_user_model()?
**Answer:** It returns the configured user model class at runtime. It is useful in views, forms and other Python code that needs to query users.

### Q9. What should a model use for a relationship to the configured user model?
**Answer:** Use settings.AUTH_USER_MODEL as the ForeignKey or OneToOneField target.

### Q10. What is the difference between a custom user model and a profile model?
**Answer:** A custom user model changes the model representing the account. A profile model stores additional information in a separate model linked to the user, often through OneToOneField.

### Q11. Can an existing project use the default user model and add profile information?
**Answer:** Yes. A separate profile model is often appropriate when the existing authentication identity is sufficient and the additional fields are optional user details.

### Q12. What does OneToOneField enforce?
**Answer:** It connects one row to one related row and enforces uniqueness on the relationship. It is suitable for one profile per account.

## 2. Migration and design questions

### Q13. Why does this lesson use a separate fresh project?
**Answer:** The main student_portal already has migrations and a StudentProfile model connected to the Student domain model. Changing AUTH_USER_MODEL or repurposing that model would risk breaking existing work. A separate fresh project safely demonstrates custom user configuration.

### Q14. Why should the profile form not expose the user field?
**Answer:** The browser must not choose which user's profile it edits. The view should assign the authenticated request.user.

### Q15. Why might phone number be stored as a CharField?
**Answer:** A phone number is an identifier, not a quantity. It can contain leading zeros, country prefixes and formatting characters.

## 3. Scenario questions

### Q16. A developer wants to add a phone field to an already migrated project. Must they change AUTH_USER_MODEL?
**Answer:** No. If it is optional profile information, add it to an appropriate existing profile model or create a separate profile model. Do not change the user model just to add one field.

### Q17. A custom user model is configured after the project has many migrations. What should the developer do?
**Answer:** Stop and plan the migration carefully. Back up the database, map existing relations and account data, create a tested migration strategy and validate it in a copy of the environment. Do not simply change the setting and run migrate.

### Q18. One student can edit another student's profile.
**Answer:** The view is trusting submitted ownership data. Use request.user to retrieve the current user's profile and do not expose the user relationship in the form.

## 4. Mini-project discussion — Custom User Profile System

Demonstrate:
1. Fresh custom_user_demo project.
2. AbstractUser extension.
3. AUTH_USER_MODEL before migrations.
4. Custom admin configuration.
5. get_user_model().
6. Existing student_portal user model remains unchanged.
7. Separate UserProfile linked to the configured user.
8. Ownership-safe profile edit view.

## 5. Readiness checklist

- [ ] I can compare AbstractUser and AbstractBaseUser.
- [ ] I know when AUTH_USER_MODEL must be set.
- [ ] I can explain get_user_model() and settings.AUTH_USER_MODEL.
- [ ] I can distinguish user model and profile model.
- [ ] I can explain the migration warning.
- [ ] I can explain profile ownership.
- [ ] I can demonstrate Custom User Profile System.

**Related notes:** [Day 51 class notes](day_51_notes.md)
