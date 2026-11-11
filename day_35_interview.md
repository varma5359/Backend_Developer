# Day 35: Interview Guide — Django Migrations: makemigrations and migrate

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 35 notes](day_35_notes.md)  
**Mini-project:** Database Migration Practice

## 1. Technical questions with model answers

### Q1. Why does Django use migrations?

**Model answer:** Migrations record schema changes as versioned Python operations so the database structure can evolve consistently across development and deployment environments.

### Q2. What is the difference between makemigrations and migrate?

**Model answer:** makemigrations compares model state with migration history and creates migration files. migrate applies unapplied migration operations to the configured database.

### Q3. What does showmigrations show?

**Model answer:** It lists migrations for apps and indicates which have been applied to the current database.

### Q4. What does sqlmigrate do?

**Model answer:** It displays the SQL Django plans to execute for a specified migration and database connection. It does not apply that SQL.

### Q5. Why should migration files be committed to version control?

**Model answer:** They are part of the application's schema history. Other developers and deployment environments need the same ordered changes.

### Q6. What should you do when adding a non-null field to a table that already has records?

**Model answer:** Decide the correct business default or data migration. Inspect Django's prompt and generated migration. Do not choose an arbitrary value merely to make the command finish.

## 2. Scenario-based interview question

**Scenario:** A teammate deleted a migration file because its number looked incorrect. What risks does this create?

**Model answer:** Other databases may already have applied it and later migrations may depend on it. The migration graph and actual database schema can diverge. Restore the shared migration history or create a deliberate forward migration; do not reset production data or delete applied history casually.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Change a model field, generate a migration, inspect its operations, inspect SQL with sqlmigrate, apply it, verify showmigrations and explain the difference between model code and database schema.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Database Migration Practice

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Database Migration Practice with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is a migration?
**Answer:** A versioned description of a database schema change.

### Q6. What does makemigrations do?
**Answer:** It creates migration files based on model changes. It does not apply them to the database.

### Q7. What does migrate do?
**Answer:** It applies pending migrations to the configured database.

### Q8. Why inspect sqlmigrate output?
**Answer:** It shows the SQL Django plans to execute and helps developers understand schema changes.

### Q9. What is a data migration?
**Answer:** A migration that transforms existing database records rather than only changing the schema.

### Q10. Why should migrations be committed?
**Answer:** Other developers, CI and deployment environments need the same schema history.

### Q11. Scenario: makemigrations says no changes detected.
**Answer:** Check whether the model was saved, the app is installed and the command is running against the intended settings module.

### Q12. Scenario: two branches create conflicting migrations.
**Answer:** Inspect both migration files and dependencies, then create a merge migration if the operations are compatible. Do not delete a migration blindly.

