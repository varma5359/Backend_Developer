# Day 35: Interview Questions — Django Migrations: makemigrations and migrate

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 35 class notes](day_35_notes.md)  
**Approved mini-project:** Database Migration Practice

## 1. Core technical questions

### Q1. Explain django migrations: makemigrations and migrate.
**Answer:** Migrations are version-controlled instructions that describe changes to the database schema. makemigrations detects model changes and creates migration files. migrate applies unapplied migrations to the configured database. Model code and the actual database schema are related but separate; editing models.py alone does not automatically change database tables.

### Q2. Which files are involved?
**Answer:** Terminal commands, profiles/migrations/0001_initial.py. Explain the responsibility of each file and how it connects to the rest of the Django application.

### Q3. Why is this feature important?
**Answer:** It helps keep application structure, presentation, data or schema changes understandable and maintainable.

### Q4. What is one common beginner mistake?
**Answer:** A migration file is generated after model changes. Always verify the exact file path, configuration and command output.

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

## 4. Mini-project viva — Database Migration Practice

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

- **1.** Create or update the Employee model from Day 34.
- **2.** Run python manage.py makemigrations profiles.
- **3.** Open the generated file inside profiles/migrations/.
- **4.** Read the CreateModel operation and field definitions.
- **5.** Run python manage.py showmigrations profiles.
- **6.** Apply changes using python manage.py migrate.
- **7.** Run showmigrations again and inspect the applied marker.
- **8.** Change one field and repeat the workflow.

## 6. Readiness checklist

- [ ] Explain the concept in simple words.
- [ ] Identify the correct files.
- [ ] Explain the command or configuration.
- [ ] Demonstrate the mini-project.
- [ ] Explain one troubleshooting case.
- [ ] Answer follow-up questions.
