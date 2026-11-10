# Day 34: Interview Questions — Django Models and Database Field Types

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 34 class notes](day_34_notes.md)  
**Approved mini-project:** Employee Management Model

## 1. Core technical questions

### Q1. Explain django models and database field types.
**Answer:** A Django model is a Python class that inherits from django.db.models.Model. Its fields describe data stored in a database table. Django's ORM uses model metadata to create and query database records. A normal Python class is not automatically a database table; a Django model participates in the ORM.

### Q2. Which files are involved?
**Answer:** profiles/models.py. Explain the responsibility of each file and how it connects to the rest of the Django application.

### Q3. Why is this feature important?
**Answer:** It helps keep application structure, presentation, data or schema changes understandable and maintainable.

### Q4. What is one common beginner mistake?
**Answer:** Employee inherits from models.Model. Always verify the exact file path, configuration and command output.

### Q5. How do you verify the result?
**Answer:** Run Django's system check, execute the required command, inspect the browser or migration status and test an edge case.

## 2. Scenario-based questions

### Q6. A feature is missing from the browser or database. What do you check?
**Suggested answer:**
1. Verify the current project folder and active environment.
2. Inspect the relevant Django file.
3. Check app registration and settings.
4. Read the complete terminal error.
5. Run python manage.py check.
6. Correct one issue and verify again.

### Q7. Why should the learner understand the generated files?
**Suggested answer:** Generated files are part of the application structure. Understanding them helps the developer review changes, troubleshoot errors and collaborate safely.

## 3. Practical discussion

Be prepared to:
- Identify each relevant file.
- Explain the important configuration.
- Demonstrate the expected result.
- Explain one error and its resolution.
- Describe what should be committed to Git.
- Identify one production concern.

## 4. Mini-project viva — Employee Management Model

1. What problem does the project solve?
2. Which files did you create or update?
3. Why are those files located there?
4. Which command did you run?
5. How did you verify the result?
6. What error did you encounter?
7. How did you fix it?
8. What would you improve next?
9. What should not be committed to Git?
10. How would you explain the project to a teammate?

## 5. Rapid revision

- **1.** Open profiles/models.py.
- **2.** Import django.db.models.
- **3.** Create Employee inheriting from models.Model.
- **4.** Choose field types that match the data.
- **5.** Add max_length to character fields.
- **6.** Use DecimalField for money-like values rather than float.
- **7.** Add unique constraints where business rules require unique values.
- **8.** Add __str__() for a readable object representation.
- **9.** Run python manage.py check.

## 6. Readiness checklist

- [ ] Explain the concept in simple words.
- [ ] Identify the correct files.
- [ ] Explain the command or configuration.
- [ ] Demonstrate the mini-project.
- [ ] Explain one troubleshooting case.
- [ ] Answer follow-up questions.
