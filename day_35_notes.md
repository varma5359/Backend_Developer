# Day 35: Django Migrations: makemigrations and migrate

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 1–34 as applicable; review the previous Django lessons before continuing  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Database Migration Practice

> **Trainer guidance:** Show the learner the exact file path before showing the code. Explain why the file exists, what each important line does, how to run the project and how to verify the result.

## 1. Learning objectives

- Explain django migrations: makemigrations and migrate.
- Identify the Django files and folders used.
- Implement the example step by step.
- Explain the relationship between Django code and the browser or database.
- Verify the result and troubleshoot common errors.
- Complete Database Migration Practice.

## 2. Concept introduction

Migrations are version-controlled instructions that describe changes to the database schema. makemigrations detects model changes and creates migration files. migrate applies unapplied migrations to the configured database. Model code and the actual database schema are related but separate; editing models.py alone does not automatically change database tables.

## 3. Why the concept matters

A Django application becomes easier to maintain when shared presentation is reused, data is represented consistently and database changes are tracked. These practices help teams review code and understand how a feature evolved.

## 4. File-by-file implementation

### File or command: `Terminal commands`

```bash
# Create migration instructions from model changes
python manage.py makemigrations profiles

# Review migration status
python manage.py showmigrations profiles

# Apply migrations to the configured database
python manage.py migrate

# Inspect SQL generated for a migration
python manage.py sqlmigrate profiles 0001
```

### File or command: `profiles/migrations/0001_initial.py`

```python
# Django generates this file.
# Do not normally hand-write an initial migration while learning.
# Inspect the operations and fields Django generated.
```

## 5. Explain the important statements

### Terminal commands

1. `# Create migration instructions from model changes` — Part of the file structure or configuration; understand how it supports the feature.
2. `python manage.py makemigrations profiles` — Runs a Django management command.
3. ` ` — Part of the file structure or configuration; understand how it supports the feature.
4. `# Review migration status` — Part of the file structure or configuration; understand how it supports the feature.
5. `python manage.py showmigrations profiles` — Runs a Django management command.
6. ` ` — Part of the file structure or configuration; understand how it supports the feature.
7. `# Apply migrations to the configured database` — Part of the file structure or configuration; understand how it supports the feature.
8. `python manage.py migrate` — Runs a Django management command.
9. ` ` — Part of the file structure or configuration; understand how it supports the feature.
10. `# Inspect SQL generated for a migration` — Part of the file structure or configuration; understand how it supports the feature.
11. `python manage.py sqlmigrate profiles 0001` — Runs a Django management command.

### profiles/migrations/0001_initial.py

1. `# Django generates this file.` — Part of the file structure or configuration; understand how it supports the feature.
2. `# Do not normally hand-write an initial migration while learning.` — Part of the file structure or configuration; understand how it supports the feature.
3. `# Inspect the operations and fields Django generated.` — Part of the file structure or configuration; understand how it supports the feature.

## 6. How to run and verify

1. Activate the project's virtual environment.
2. Open the terminal in the folder containing manage.py.
3. Run `python manage.py check`.
4. Execute the commands or start the development server as appropriate.
5. Open the page in a browser or inspect migration status.
6. Compare actual behavior with the expected result.
7. Record any warning and explain whether it is expected.

## 7. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Template block is not rendered | extends path and matching block names |
| CSS is missing | static directory, STATIC_URL, {% load static %} and URL |
| Model is not detected | app in INSTALLED_APPS and model import |
| Field configuration error | Field type and required field arguments |
| No migration is generated | Check whether model changes exist and the correct app is selected |
| Migration fails | Read the full database error and inspect migration dependencies |
| Database does not reflect model change | Run makemigrations and then migrate |

## 8. Industry scenario

A staff management website needs a consistent page header and styling, an employee data model and a repeatable way to update its database structure. Django's template inheritance, static files, model fields and migrations support these needs.

## 9. Approved mini-project — Database Migration Practice

**Objective:** Database Migration Practice.

### Functional requirements

1. Create or update the Employee model from Day 34.
2. Run python manage.py makemigrations profiles.
3. Open the generated file inside profiles/migrations/.
4. Read the CreateModel operation and field definitions.
5. Run python manage.py showmigrations profiles.
6. Apply changes using python manage.py migrate.
7. Run showmigrations again and inspect the applied marker.
8. Change one field and repeat the workflow.

### Suggested structure

```text
projects/day_35/
├── manage.py
├── config/
└── profiles/
    ├── models.py
    ├── migrations/
    ├── templates/
    └── static/
```

### Validation checklist

- [ ] A migration file is generated after model changes.
- [ ] The migration file is committed with source code.
- [ ] migrate applies the migration without error.
- [ ] showmigrations shows the migration as applied.
- [ ] The learner understands that makemigrations creates files while migrate applies them.

### Submission evidence

- Updated source files.
- Commands executed and terminal output.
- Browser screenshot or migration status.
- README with exact file paths and setup instructions.
- Explanation of one design decision and one error handled.

## 10. AI-assisted implementation guide

**Planning prompt:** "Help me plan Database Migration Practice. List the files, ordered tasks, commands and verification checks. Do not write the complete solution."

**Guided prompt:** "Guide me through one file at a time. Explain why the file is needed, show only the next change and wait for my output."

**Debugging prompt:** "Inspect my exact Django error, file path and command. Explain the likely cause and how to verify the fix."

**Review prompt:** "Review my implementation against the approved requirements. Identify missing validation, naming issues and maintainability concerns."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Organize Django presentation, data or database structure changes in a maintainable way.  
B. Replace Python.  
C. Disable validation.  
D. Remove all configuration.  
**Answer: A.** The concept supports a maintainable Django application.

**Q2. What should you inspect when the result is missing?**  
A. Only the browser theme.  
B. The relevant file path, setting and Django output.  
C. Delete the project.  
D. Ignore the warning.  
**Answer: B.** File paths and configuration commonly determine whether Django discovers the component.

**Q3. Which practice is safest?**  
A. Edit generated files without understanding them.  
B. Ignore migrations.  
C. Follow the correct workflow and verify each change.  
D. Commit local secrets.  
**Answer: C.** Use a repeatable workflow and inspect the result.

**Q4. What is the best evidence of completion?**  
A. A file exists.  
B. The code is long.  
C. The learner watched a video.  
D. The feature works and its behavior is verified.  
**Answer: D.** Evidence should show the required behavior.

**Q5. What should the README contain?**  
A. Setup, file paths, commands and validation results.  
B. Only a title.  
C. A private password.  
D. No instructions.  
**Answer: A.** Clear instructions make the project reproducible.

## 12. Interview preparation

**Q1. Explain django migrations: makemigrations and migrate.**  
**Answer:** Migrations are version-controlled instructions that describe changes to the database schema. makemigrations detects model changes and creates migration files. migrate applies unapplied migrations to the configured database. Model code and the actual database schema are related but separate; editing models.py alone does not automatically change database tables.

**Q2. Which files or commands are important?**  
**Answer:** Explain each file or command from the demonstration and its responsibility.

**Q3. How would you troubleshoot a failure?**  
**Answer:** Read the full traceback, confirm file paths and configuration, run Django system checks and verify the result after one focused correction.

**Follow-up:** What evidence would you show another developer?  
**Answer:** The source change, command output, browser behavior or migration status and a concise README.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Identify the relevant file paths.
- [ ] Implement the example.
- [ ] Run the required checks or commands.
- [ ] Verify the expected result.
- [ ] Complete Database Migration Practice.
- [ ] Test normal and error cases.
- [ ] Complete all five MCQs.
- [ ] Answer the interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 36.
