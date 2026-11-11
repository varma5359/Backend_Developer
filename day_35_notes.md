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

---

# Extended Beginner Lab — Migration Workflow and Safety

## 19. What is a migration?

A migration is a versioned description of a database schema change.

Examples:
- Create a table.
- Add a column.
- Change a field.
- Add a constraint.
- Rename a field.
- Remove a field.

Migrations allow developers to track schema evolution with source code.

## 20. Model code versus database schema

Changing models.py does not automatically change the database.

The usual workflow is:

~~~text
Edit model
   |
   v
makemigrations
   |
   v
Review migration file
   |
   v
migrate
   |
   v
Database schema updated
~~~

Do not skip the review step for important schema changes.

## 21. makemigrations

Run:

~~~powershell
python manage.py makemigrations
~~~

Django compares model definitions with migration state and creates migration files for detected changes.

The command does not apply them to the database.

## 22. migrate

Run:

~~~powershell
python manage.py migrate
~~~

Django applies unapplied migrations to the configured database.

It records applied migration state in the django_migrations table.

## 23. showmigrations

Run:

~~~powershell
python manage.py showmigrations
~~~

This shows migration files and whether they have been applied.

[X] means applied.

[ ] means not applied.

## 24. sqlmigrate

Run:

~~~powershell
python manage.py sqlmigrate profiles 0001
~~~

Replace the app label and migration number with the actual values in your project.

This shows the SQL Django plans to run for that migration.

It is useful for understanding schema operations and reviewing important changes.

## 25. migrate --plan

Run:

~~~powershell
python manage.py migrate --plan
~~~

This displays the migrations Django plans to apply.

Use it before applying changes in a sensitive environment.

## 26. Understand migration dependencies

A migration may depend on another migration.

For example:
- A model has a ForeignKey to another app.
- The referenced table must exist.
- Django records dependencies between migrations.

Do not manually delete dependency declarations to make a migration run.

## 27. Understand migration numbering

Migration names commonly contain a number and description.

Examples:
- 0001_initial.py
- 0002_add_phone_number.py

The number reflects sequence within the app, not a global order across every app.

Django uses dependencies to determine the full order.

## 28. Understand initial migration

The first migration for an app is often named 0001_initial.py.

It creates the initial schema for that app's models.

Do not assume every app's first migration is applied at the same time.

## 29. What if makemigrations says no changes detected?

Possible reasons:
- No model change was made.
- The app is not installed.
- The wrong settings module is active.
- The edited file was not saved.
- The change does not affect schema.
- You are running the command in another project.

Check the current folder and active interpreter before editing migrations manually.

## 30. What if migrate says no migrations to apply?

Possible reasons:
- All migrations are already applied.
- The model change was not converted into a migration.
- The app has no migration file.
- The command is running against another database/settings module.

Run showmigrations and inspect the actual database configuration.

## 31. Migration files belong in Git

Migration files are part of the application's source history.

They should normally be committed with the model changes they represent.

Do not add the database file as a substitute for migration history.

## 32. Never casually delete migration files

Deleting migrations can break:
- Other developers' environments.
- Deployment history.
- Migration dependencies.
- Existing databases.
- CI test setup.

If a migration problem occurs, inspect the migration graph and actual database state before choosing a repair.

## 33. Understand makemigrations --check

Run:

~~~powershell
python manage.py makemigrations --check --dry-run
~~~

This checks whether model changes are missing migration files without writing new migration files.

It is useful in CI.

## 34. Understand migration rollback

Django can migrate an app to an earlier migration state.

Example:

~~~powershell
python manage.py migrate profiles 0001
~~~

This asks Django to move the profiles app to migration 0001.

A rollback can remove columns or tables and may destroy data.

Do not run rollback commands on important data without a backup and a clear plan.

## 35. The danger of migrate app zero

A command such as:

~~~powershell
python manage.py migrate profiles zero
~~~

asks Django to unapply all migrations for the profiles app.

This can remove database structures and data.

Do not use it as a normal troubleshooting step.

## 36. Data migrations

Some migrations change data rather than only schema.

Examples:
- Populate a new field for existing rows.
- Normalize a status value.
- Move data between columns.

Django supports data migrations using RunPython.

Data migrations must be designed carefully:
- Use historical models from the migration app registry.
- Avoid importing current model classes directly.
- Make the operation safe for the intended data.
- Consider whether it is reversible.

This is an advanced concept. Do not create a data migration without a specific requirement.

## 37. Migration conflicts

A conflict can occur when two branches create migrations from the same previous migration state.

Django may report conflicting leaf nodes.

Safe response:
1. Stop before applying migrations.
2. Inspect the conflicting files.
3. Inspect the branch history.
4. Understand which schema changes each file contains.
5. Create a merge migration if appropriate.
6. Run makemigrations --check.
7. Test migrations from a clean database.
8. Test migration from a copy of an existing database.

Do not delete one branch's migration without understanding its changes.

## 38. Backup before risky migrations

Before changing a database schema in a valuable environment:
- Make a database backup.
- Confirm the backup can be restored.
- Review migration SQL.
- Test on a copy.
- Plan downtime or deployment sequencing if required.

A Git commit does not back up database records.

## 39. Common migration errors

| Error/symptom | Possible cause | Safe investigation |
|---|---|---|
| No changes detected | Model not changed or wrong project | Check file, app and settings |
| Table already exists | Database schema and migration state disagree | Inspect migration history and schema |
| Column already exists | A schema operation was applied outside migration history | Inspect DB and migration state |
| NOT NULL constraint failed | Existing rows need a value | Plan a data migration/default |
| Foreign key constraint failed | Related record missing or invalid | Inspect relationship data |
| Conflicting migrations | Parallel branches changed schema | Inspect graph and create merge migration |
| Migration import error | Bad Python code or dependency | Read traceback and inspect migration file |

## 40. Safe migration exercise

In a local practice copy:
1. Add one optional field to a model.
2. Run makemigrations.
3. Open the generated migration.
4. Read the operation.
5. Run sqlmigrate.
6. Apply migrate.
7. Run showmigrations.
8. Confirm the field exists through the ORM.
9. Run makemigrations --check --dry-run.

Do not experiment with destructive rollback on the main pathway database.

## 41. Self-check questions

1. What is a migration?
2. What does makemigrations do?
3. What does migrate do?
4. What does showmigrations display?
5. What does sqlmigrate show?
6. What is a migration dependency?
7. Why should migration files be committed?
8. Why is deleting migrations dangerous?
9. What does migrate app zero do?
10. What is a data migration?
11. What can cause migration conflicts?
12. Why should important databases be backed up?

## 42. Answers

1. Versioned description of a database schema change.
2. Creates migration files from model changes.
3. Applies migration files to the database.
4. Applied and unapplied migration state.
5. SQL for a migration operation.
6. A requirement that another migration be applied first.
7. Other environments need the same schema history.
8. It can break dependencies and existing databases.
9. It unapplies all migrations for the app.
10. A migration that changes existing data.
11. Parallel branches creating migrations from the same state.
12. Schema changes can remove or transform data.

## 43. Independent challenge — Migration History Review

Choose one existing app.

Record:
- Migration filenames.
- Which are applied.
- One migration operation.
- SQL generated for that operation.
- Which model change it represents.

Do not edit or delete migration files during the review.

---

# Deep Practice Workbook — Migration Review and Recovery Thinking

## 44. Migration review scenario

A developer adds a required department field to a model that already has 500 employee rows.

Django asks how existing rows should receive a value.

Why?

The database cannot create a required non-null column for existing rows without deciding what value those records should contain.

Possible strategies:
- Supply a deliberate default.
- Make the field temporarily optional, populate data, then make it required.
- Use a data migration to assign values based on business rules.

Do not choose an arbitrary default merely to silence the prompt.

## 45. Safe staged migration

A staged approach may be:
1. Add the field as optional.
2. Create and apply migration.
3. Populate existing records with valid values.
4. Verify no records remain incomplete.
5. Change the field to required.
6. Create and apply the next migration.
7. Run tests.

The correct approach depends on the actual business rules and database.

## 46. Migration file reading exercise

Open an initial migration.

Identify:
- Migration class.
- dependencies.
- operations.
- CreateModel.
- AddField.
- AlterField.
- AddConstraint.

Write one sentence explaining each operation.

## 47. SQL review exercise

Run sqlmigrate for a migration.

Identify:
- CREATE TABLE.
- ALTER TABLE.
- CREATE INDEX.
- UNIQUE constraint.
- Foreign key.

The exact SQL depends on the database backend.

Do not edit generated SQL as a substitute for changing model definitions and migrations.

## 48. Migration graph exercise

A migration may depend on another app's migration.

Draw:
- App A migration.
- App B migration.
- Dependency arrow.
- Which migration must be applied first.

Explain why a foreign key can create migration dependencies.

## 49. Migration conflict scenario

Two developers create migrations on separate branches from the same previous migration.

Both add a field.

When merged, Django may report conflicting leaf migrations.

A merge migration can depend on both branches and combine the graph.

Before creating it:
- Inspect both migration files.
- Check whether operations conflict.
- Check whether both are needed.
- Run migrations from a clean database.
- Test upgrade from an existing database copy.

## 50. Database backup scenario

A migration removes a column that contains important information.

A Git commit cannot restore the deleted database values.

A database backup or tested data migration strategy is required.

Always separate:
- Source-code history.
- Database schema history.
- Database record backup.

## 51. Migration commands review

| Command | Use |
|---|---|
| makemigrations | Generate migration files |
| migrate | Apply or unapply migration operations |
| showmigrations | Display migration state |
| sqlmigrate | Display SQL for a migration |
| migrate --plan | Preview planned migration operations |
| makemigrations --check --dry-run | Check for model changes without migration files |

## 52. Safe recovery decision tree

If migration fails:
1. Stop.
2. Do not delete migration files.
3. Do not reset the database.
4. Read the full traceback.
5. Check the active project and database.
6. Inspect showmigrations.
7. Inspect migration files and dependencies.
8. Check whether the schema was changed manually.
9. Back up data before repair.
10. Test the repair on a copy.

## 53. Self-check questions

1. Why can adding a required field need a default?
2. What is a data migration?
3. What does a migration dependency mean?
4. Why inspect sqlmigrate output?
5. What is a merge migration?
6. Why is deleting a migration file dangerous?
7. What is the difference between Git history and database backup?
8. What should be done before a risky schema change?

## 54. Answers

1. Existing rows need a value for the new required column.
2. A migration that transforms existing records.
3. One migration must be applied before another.
4. To understand the database operations being applied.
5. A migration that joins parallel migration branches.
6. It can break migration history and existing environments.
7. Git stores code; a database backup stores database state.
8. Review, backup, test on a copy and plan rollback.

## 55. Final migration report

Choose one migration and report:
- Model change.
- Migration file.
- Dependency.
- SQL effect.
- Applied state.
- Validation performed.
- Data safety consideration.

## 56. Final migration safety assessment

A teammate asks you to delete migration files because the local database reports an error.

Explain why this is unsafe.

Your response must include:
- The difference between model state and database state.
- How to inspect showmigrations.
- How to inspect migration dependencies.
- How sqlmigrate helps.
- Why a database backup is different from a Git commit.
- Why the problem must be reproduced on a copy before repair.

Do not run destructive migration commands on important data.


## 57. Migration handover questions

Before a migration is merged, answer:
1. Which model change caused it?
2. Which database operations will run?
3. Which migration does it depend on?
4. Does it affect existing records?
5. Is it reversible?
6. Does it need a data migration?
7. Has it been tested on a clean database?
8. Has it been tested against an existing database copy?
9. Is a backup required?
10. How will failure be detected?

Keep the answers with the pull request or change record.


## 58. Explain-back assessment

Without reading the notes, explain:
1. Why a model edit does not directly change the database.
2. What makemigrations creates.
3. What migrate applies.
4. How showmigrations helps.
5. Why inspect SQL.
6. What migration dependencies represent.
7. How data migrations differ from schema migrations.
8. Why existing rows matter when adding required fields.
9. Why migration conflicts occur.
10. Why backups are separate from Git history.

## 59. Submission reflection

Write a safe migration plan for adding a required field to an existing table. Include the initial optional schema change, legacy data population, validation of existing rows, final required-field migration, test database run, backup and deployment rollback consideration. Explain why a default should represent a real business value.

## 60. Final reviewer prompt

Ask another learner to inspect your migration plan. They must identify the model change, SQL effect, dependency, existing-data impact and rollback concern. Do not apply the migration to important data until the review is complete.

## 61. Final readiness statement

Do not mark a migration complete until you can explain its schema effect, inspect its SQL, identify its dependencies, validate existing data and describe how you would recover from a failed deployment.
