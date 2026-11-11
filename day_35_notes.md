# Day 35: Django Migrations: makemigrations and migrate

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Duration:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Previous Django lessons; Python, OOP, HTTP and SQL foundations  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment and Django 5.2.19  
**Continuous project:** `student_portal` / `config` / `profiles`  
**Approved mini-project:** Database Migration Practice

> **Teaching rule:** Do not copy a command without understanding it. Use the exact file path, run one step at a time, inspect the output and explain what the framework is doing.

## 1. Learning objectives

1. Explain why database schema changes are version-controlled.
2. Distinguish makemigrations from migrate.
3. Inspect migrations with showmigrations and sqlmigrate.
4. Apply and verify a model schema change safely.

## 2. Concept introduction — start from zero

A model describes the database structure Django expects. A migration is a version-controlled instruction describing a schema change. makemigrations creates migration files from model changes. migrate applies unapplied migrations to the selected database. Creating a migration and applying it are two separate actions.

### Why a backend developer needs this

The Student Portal is being developed as a real, growing application. The code must remain organized and the result must be repeatable. Today's lesson adds one building block to that system. A junior developer should be able to explain the purpose of the component, not only remember its syntax.

## 3. Mental model

```text
Student / Browser
       |
       v
Django project (config)
       |
       v
profiles application
       |
       v
Today's Django component
       |
       +----> optional database / template / response work
       |
       v
Visible result or persisted schema
```

## 4. File map

- `profiles/models.py`
- `profiles/migrations/0001_initial.py (generated)`
- `db.sqlite3 (local database file)`

Project context:

```text
student_portal/
├── .venv/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── profiles/
    └── static/
        └── profiles/
```

Files are introduced gradually. Create a file only when this lesson tells you to.

## 5. Prepare the terminal

1. Open the existing `student_portal` folder in VS Code.
2. Open Terminal → New Terminal.
3. Confirm the current directory contains `manage.py`.
4. Activate the same virtual environment created earlier.
5. Confirm the interpreter and Django version.

```powershell
Get-Location
python --version
python -m django --version
```

If the current folder does not contain manage.py, move to the project root. Do not create a second project to avoid a path mistake.

## 6. Commands — exact order

```powershell
python manage.py makemigrations profiles
python manage.py showmigrations profiles
python manage.py sqlmigrate profiles 0001
python manage.py migrate
python manage.py showmigrations profiles
python manage.py check
```

### Understand every command

### Step 1 — `makemigrations profiles`

Looks at model changes for the profiles app and creates migration files describing the required schema operations. It does not apply them to the database.

### Step 2 — `showmigrations profiles`

Lists migration files for the app. [ ] means not applied; [X] means applied to the selected database.

### Step 3 — `sqlmigrate profiles 0001`

Shows the SQL Django would use for migration 0001 on the configured database backend. It is a preview, not an apply command.

### Step 4 — `migrate`

Applies all unapplied migrations needed by the project to the configured database.

### Step 5 — `showmigrations again`

Confirms whether the migration has been applied.

### Step 6 — `check`

Runs Django system checks after the schema operation.

## 7. Implementation — correct files

### Code demonstration

The code below may contain Python, HTML or CSS sections. Use the filename comments to put each section into the correct file. Never paste HTML into a .py file.

```python
# Example shape of a generated migration. Django generates this file.
# profiles/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name="ID",
                )),
                ("employee_code", models.CharField(max_length=12, unique=True)),
                ("full_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("salary", models.DecimalField(max_digits=10, decimal_places=2)),
                ("joining_date", models.DateField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

### Before saving

1. Read the existing file.
2. Preserve working code from earlier days.
3. Add the new code at the correct location.
4. Check spelling and indentation.
5. Save the file.
6. Run the relevant Django command.
7. Inspect terminal output before opening the browser.

## 8. Detailed explanation

### Why migrations exist
A database schema changes as the application evolves. A team needs a repeatable history of those changes. Migration files are committed to version control so other developers and deployment environments can apply the same sequence.

### makemigrations versus migrate
- makemigrations: model state → migration file.
- migrate: migration file → actual database schema.
Running only makemigrations does not create the table in the database.

### showmigrations
This command shows the migration state in the currently selected database. A migration can exist on disk but remain unapplied.

### sqlmigrate
This displays the SQL generated for a specific migration and current database backend. It is useful for understanding what will happen before applying a schema change.

### Migration files are source code
Commit migration files. They are part of the application's schema history. Do not delete or rewrite migrations that teammates or production environments may already have applied without a coordinated migration plan.

### What about db.sqlite3?
The local SQLite database file contains local data and schema. It is usually not committed for a shared application; each developer applies migrations to their own database. Production databases are managed separately.

### Existing data and required fields
Adding a new non-null field to a table with existing rows can require a default or staged data migration. Think about existing records before changing schema. Do not blindly accept a generated one-off default without understanding the data implications.

### Dependencies and order
Migrations can depend on earlier migrations or migrations in another app. Django orders them using dependency metadata.

### Common errors
- No changes detected: ensure model file is saved and app is installed.
- Table already exists: database schema and migration history may be out of sync; inspect before deleting anything.
- Cannot add non-null field: existing rows need a safe value.
- Wrong database: verify settings and active environment before migrating.
- Migration conflict: coordinate changes and inspect migration graph; don't delete files blindly.

## 9. Execution trace

Explain these questions aloud:
1. What is the input or requested operation?
2. Which file or command handles it?
3. What does Django do automatically?
4. What did the developer implement?
5. What result should be produced?
6. How do we prove that result is correct?

## 10. Verification checklist

- [ ] Migration file is created by Django.
- [ ] showmigrations shows unapplied state before migrate.
- [ ] sqlmigrate prints SQL for the migration.
- [ ] migrate applies the migration successfully.
- [ ] showmigrations displays [X] after applying.
- [ ] The learner explains migration file versus database schema.

Run the general project check:

```powershell
python manage.py check
```

Expected when project configuration is valid:

```text
System check identified no issues (0 silenced).
```

The system check does not prove every browser interaction or database operation. Perform the specific checks above.

## 11. Troubleshooting

| Symptom | Likely cause | Diagnostic |
|---|---|---|
| manage.py not found | Wrong directory | Get-Location and locate manage.py |
| No module named django | Wrong environment | Check sys.executable and Django version |
| App not loaded | Missing app registration | Inspect INSTALLED_APPS |
| Template not found | Incorrect folder/file path | Check app/templates/app_name/ |
| Route returns 404 | URL pattern missing or order issue | Inspect root and app URLconf |
| Database table missing | Migration not applied | Run showmigrations and migrate |
| CSS missing | Incorrect static path | Inspect browser Network tab |
| SyntaxError | Incorrect Python syntax | Read traceback file and line |

### Safe debugging process
1. Reproduce the problem.
2. Read the complete error.
3. Locate the first relevant line in your own code.
4. Confirm the correct Python environment and project folder.
5. Check the filename, imports, spelling and configuration.
6. Change one thing at a time.
7. Rerun the appropriate check.
8. Verify the actual behavior again.

## 12. Industry scenario

A training institute needs to maintain a Student Portal. A backend developer must make the application easy to extend and debug. Today's concept is useful because it gives a predictable way to organize or operate one part of the system.

Discuss:
- What problem does the user face?
- Which component is responsible?
- What information enters the feature?
- What result should the user or developer observe?
- What failure case should be tested?

## 13. Approved mini-project — Database Migration Practice

### Objective
Build a working demonstration of today's approved concept in the existing Student Portal.

### Ordered tasks

1. Run makemigrations profiles and inspect the created migration file.
2. Run showmigrations profiles before applying; identify the unchecked migration.
3. Run sqlmigrate and read the CREATE TABLE and constraints in the SQL.
4. Run migrate.
5. Run showmigrations again and confirm the migration is checked.
6. Open Django shell and inspect Employee.objects.count().

### Acceptance checks

- [ ] Migration file is created by Django.
- [ ] showmigrations shows unapplied state before migrate.
- [ ] sqlmigrate prints SQL for the migration.
- [ ] migrate applies the migration successfully.
- [ ] showmigrations displays [X] after applying.
- [ ] The learner explains migration file versus database schema.

### Submission evidence
- Relevant source files.
- Terminal output from checks and commands.
- Browser screenshot or database evidence, where relevant.
- README with setup and verification steps.
- Short explanation of one error and its correction.

### Optional extension
Make one small change, predict its result, run it and explain the difference.

## 14. AI-assisted implementation

First attempt each step using the lesson. If you are still stuck, use an optional AI learning assistant for hints and explanations; do not ask it to hide the implementation from you.

**Planning prompt**
```text
I am a beginner. Help me plan Database Migration Practice.
Give me ordered tasks and checkpoints. Do not give me the complete solution.
```

**Guided implementation prompt**
```text
Guide me one file and one step at a time. Explain the command,
the code and the expected output. Wait for my result before continuing.
```

**Debugging prompt**
```text
Here is my exact command, current directory, relevant file and full error.
Explain the likely cause and the smallest safe fix. Do not rewrite unrelated files.
```

## 15. Daily MCQ assessment

### Q1. What does makemigrations do?

A. Applies SQL immediately
B. Creates migration files from model changes
C. Starts the web server
D. Creates a superuser

**Answer: B.** It generates version-controlled schema-change instructions.

### Q2. What does migrate do?

A. Applies unapplied migrations
B. Creates HTML templates
C. Registers views
D. Changes URL paths

**Answer: A.** migrate applies the migration operations to the configured database.

### Q3. What does [X] mean in showmigrations?

A. Migration is missing
B. Migration is applied
C. Migration has a syntax error
D. Migration is ignored

**Answer: B.** The checked marker indicates the migration is applied to that database.

### Q4. What does sqlmigrate show?

A. Browser HTML
B. Generated SQL for a migration
C. Python version
D. User passwords

**Answer: B.** It previews the SQL Django will execute for the named migration.

### Q5. Should migration files normally be committed?

A. No, delete them after use
B. Yes, they are part of the schema history
C. Only if SQLite is used
D. Only when there are no models

**Answer: B.** Migration files allow teammates and deployments to apply the same schema evolution.

## 16. Interview preparation

### Q1. Explain today's topic in simple words.
**Answer:** A model describes the database structure Django expects. A migration is a version-controlled instruction describing a schema change. makemigrations creates migration files from model changes. migrate applies unapplied migrations to the selected database. Creating a migration and applying it are two separate actions.

**Follow-up:** Give an example from the Student Portal.

### Q2. Which files or commands are important?
**Answer:** `profiles/models.py`, `profiles/migrations/0001_initial.py (generated)`, `db.sqlite3 (local database file)`. Explain the responsibility of each.

**Follow-up:** What would you inspect if the expected behavior did not appear?

### Q3. How do you verify the implementation?
**Answer:** Run the commands, inspect output and verify the browser or database behavior. Explain the edge case you tested.

**Follow-up:** Does a successful system check guarantee that every feature works?

**Answer:** No. It checks selected project configuration and framework conditions. Feature behavior needs direct testing.

### Q4. What is a common beginner mistake?
**Answer:** Running commands from the wrong folder, editing the wrong file or assuming code works without verification. Read the error and isolate the cause.

## 17. Completion checklist

- [ ] I can explain today's concept without reading.
- [ ] I know the exact file paths.
- [ ] I can explain the important code.
- [ ] I ran the required commands.
- [ ] The Django system check passes.
- [ ] I verified the expected behavior.
- [ ] I tested an edge case.
- [ ] I completed Database Migration Practice.
- [ ] I submitted reproducible evidence.
- [ ] I can answer the interview questions.

## 18. Independent completion test

Do not mark the day complete merely because a file contains code. Complete every check yourself:
1. Demonstrate the result in the browser or terminal.
2. Explain the execution flow without reading the notes.
3. Modify one small part independently and predict the result before running it.
4. Compare the actual result with your prediction.
5. Diagnose and fix one controlled mistake, such as a misspelled variable, template path or setting.

**Next lesson:** Day 36 — Django Admin Panel and Model Registration
