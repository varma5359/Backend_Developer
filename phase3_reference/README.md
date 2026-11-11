# Phase 3 Django Reference Application

This is a small runnable reference implementation used to validate the Django examples and the integrated Student Management Website described in Phase 3 (Days 27–41).

It is a **quality-assurance reference**, not a replacement for completing the class notes. Students should build the feature from the daily instructions first, then compare their implementation with this reference when they need to inspect a working example.

## Environment

- Python 3.12 (CI)
- Django 5.2.19
- SQLite for local testing
- App: `profiles`
- Project package: `config`

## Run locally (Windows PowerShell)

From the repository root:

```powershell
Set-Location phase3_reference
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations profiles
python manage.py migrate
python manage.py runserver
```

Open these routes:

| URL | What it demonstrates |
|---|---|
| `/` | Root route and base template |
| `/about/` | Child template and inheritance |
| `/profile/25/` | Integer path converter |
| `/member/asha/` | String path converter |
| `/welcome/?name=asha` | Query string and template variable |
| `/request-info/` | Request method |
| `/employee/` | Template variables, filters, loops and conditionals |
| `/students/` | Student directory and empty state |
| `/students/register/` | GET/POST ModelForm, validation, CSRF and redirect |
| `/admin/` | Django admin |

## Run tests

From `phase3_reference`:

```powershell
python manage.py test profiles -v 2
```

The automated suite checks:

- URL routing and integer/string path converters.
- Query-string handling and request method.
- Template inheritance, template variables, filters, loops and static CSS URL generation.
- Employee, Student, Department, Course and StudentProfile models.
- ForeignKey, OneToOneField and ManyToManyField access in both directions.
- PROTECT and CASCADE behavior.
- ModelForm field validation, cross-field validation and duplicate unique values.
- Valid and invalid registration submissions.
- CSRF rejection without a token and acceptance with a token.
- Employee admin registration and admin login page.

## Security and scope

- The settings are for local testing only.
- The SECRET_KEY is a non-secret development placeholder.
- DEBUG is enabled only for local testing.
- Do not deploy this reference configuration as-is.
- Full update/delete CRUD, authentication flows for public users, production deployment and PostgreSQL are outside Phase 3's scope and belong to later phases.

## CI

The repository workflow installs the pinned Django version, runs `manage.py check`, generates/applies migrations, verifies static-file discovery and runs the test suite. A passing workflow proves this reference application works in the CI environment; it does not prove every learner's local environment is configured correctly or that a beginner can complete the lessons without assistance.
