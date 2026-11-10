# Day 38: Interview Guide — Model Relationships: One-to-One, One-to-Many and Many-to-Many

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 38 notes](day_38_notes.md)  
**Approved mini-project:** College Relationship Manager

## 1. Core questions

### Q1. Explain today's topic.
**Answer:** Real applications connect records. A student belongs to a department, a student may have one profile, and students can enroll in multiple courses while each course can have many students. Django models these patterns with ForeignKey, OneToOneField and ManyToManyField. Relationship design protects data integrity and makes ORM navigation possible.

**Follow-up:** Give one example from the Student Portal.

### Q2. Which files or commands are involved?
**Answer:** `profiles/models.py`, `profiles/migrations/`. Explain what each does and how the components connect.

**Follow-up:** What would you inspect if the feature is missing or fails?

### Q3. What does Django do automatically?
**Answer:** Django supplies the framework mechanisms, ORM/admin integration and command behavior. Developers still define business rules, choose field relationships, configure the app and verify results.

### Q4. How do you verify the feature?
**Answer:** Run `python manage.py check`, execute the relevant commands and inspect the real admin/database/shell result. Test an edge case.

## 2. Scenario-based questions

### Q5. The command succeeds but the expected record or behavior is missing. What do you inspect?
**Suggested answer:** Confirm the correct project and database, inspect the model/registration/query, check migration state, review constraints and reproduce the operation in shell or browser.

### Q6. Why is it risky to change or delete migration files without a plan?
**Suggested answer:** Migration files are shared schema history. Other developers and deployed databases may already have applied them. Deleting or rewriting history can make database state inconsistent.

### Q7. A user requests access to an admin function they do not need. What should the developer do?
**Suggested answer:** Apply least privilege. Grant only the permissions needed for the user's role; do not make every staff user a superuser.

## 3. Practical coding discussion

Be ready to:
- Identify the correct file.
- Explain the important field/query/admin setting.
- Run the management command.
- Demonstrate the actual result.
- Explain a constraint or exception.
- Test a missing/duplicate/invalid case.
- Explain a safe correction.

## 4. Mini-project viva — College Relationship Manager

1. What problem does it solve?
2. What is the data requirement?
3. Which models or admin classes are involved?
4. Which commands or queries did you execute?
5. What output did you verify?
6. What happens for invalid or duplicate data?
7. Which test cases did you perform?
8. What error did you encounter?
9. How did you fix it?
10. What would you improve?

## 5. Rapid revision

- Explain the topic in simple language.
- Identify the model, command or query.
- Explain the database effect.
- Demonstrate the project.
- Test one edge case.
- Explain a common exception or integrity concern.

## 6. Interview readiness

- [ ] I can define the concept.
- [ ] I can explain the file and code.
- [ ] I can run the commands.
- [ ] I can show real database behavior.
- [ ] I can explain an edge case.
- [ ] I can present College Relationship Manager.

**Trainer note:** Ask the learner to predict the database result before executing a query or changing a relationship. The aim is to assess reasoning, not syntax memorization.
