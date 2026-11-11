# Day 54: Complete Django Application Integration and Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 6–8 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–53 — Django fundamentals, ORM, relationships, forms, CRUD, authentication, sessions, permissions, messages, search and pagination  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config; new jobs application  
**Approved mini-project:** Job Portal Web Application

> **Self-learning promise:** This is the integration day. You will connect models, migrations, forms, views, URLs, templates, authentication, permissions, messages, search, pagination and tests into one working Job Portal workflow. Build in small checkpoints. Do not skip migrations or test the final application only by opening the home page.

---

# PART 1 — UNDERSTAND THE COMPLETE APPLICATION

## 1. Business problem

A training institute wants a simple job portal.

The application has two main user types:

**Job seeker**
- Registers and signs in.
- Views active job openings.
- Searches and filters jobs.
- Opens a job detail page.
- Applies to a job.
- Views their own applications.

**Employer or authorized staff member**
- Signs in.
- Creates a job opening.
- Edits jobs they own or are authorized to manage.
- Views applications submitted for their job.
- Closes a job opening.

The portal must protect user information and prevent duplicate applications.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain how Django components work together.
2. Design a small multi-user application.
3. Create and register a new Django app.
4. Define related Job and JobApplication models.
5. Use settings.AUTH_USER_MODEL for user relationships.
6. Create and apply migrations.
7. Build ModelForms with validation.
8. Implement job list and detail views.
9. Implement search, filtering and pagination.
10. Require authentication before applying.
11. Prevent duplicate applications.
12. Restrict employer actions using permissions and ownership checks.
13. Display success and error messages.
14. Build templates and URL routes.
15. Register models in Django admin.
16. Write automated tests for models, forms, views and user journeys.
17. Run final validation checks.
18. Explain the complete request-response and database flow.
19. Complete Job Portal Web Application.

## 3. Important vocabulary

| Term | Meaning |
|---|---|
| Integration | Connecting separate components into one workflow |
| Model | Python representation of stored application data |
| Relationship | Connection between records |
| ForeignKey | Many records can reference one related record |
| Constraint | Database rule that protects data integrity |
| ModelForm | Form generated from a Django model |
| View | Code that processes a request and returns a response |
| URLconf | Configuration mapping paths to views |
| Template | File used to render HTML |
| Authentication | Verifying user identity |
| Authorization | Checking what a user may do |
| Ownership check | Confirming a user is allowed to access a particular record |
| Transaction | Group of database operations treated as one unit |
| Integration test | Test of multiple components working together |
| Regression test | Test that checks existing behavior still works after changes |

## 4. Complete application flow

~~~text
Browser
   |
   v
Job Portal URL
   |
   v
Django URL dispatcher
   |
   v
View
   |
   +---- Authentication check
   |
   +---- Permission / ownership check
   |
   +---- Form validation
   |
   v
ORM QuerySet / Model operation
   |
   v
Database
   |
   v
View builds context
   |
   v
Template renders HTML
   |
   v
HTTP response
   |
   v
Browser displays result
~~~

A real request may also pass through middleware, session handling, CSRF protection, messages and other components.

## 5. Project architecture

~~~text
student_portal/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
├── profiles/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
└── jobs/
    ├── migrations/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── tests.py
    └── templates/
        └── jobs/
~~~

The jobs app owns job-related features. The profiles app continues to own the earlier profile and employee features.

---

# PART 2 — PREPARE THE EXISTING PROJECT

## 6. Open the correct folder

Open the existing student_portal project in VS Code.

Open a PowerShell terminal.

Run:

~~~powershell
Get-Location
Get-ChildItem
~~~

Confirm manage.py exists in the current directory.

## 7. Activate the virtual environment

~~~powershell
.\.venv\Scripts\Activate.ps1
python --version
python -m django --version
~~~

The course baseline is Django 5.2.19.

Do not install a second version if the correct environment is already active.

## 8. Confirm installed apps

Open config/settings.py.

Keep the apps from previous lessons. Add the jobs app after it has been created:

~~~python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
    "catalog.apps.CatalogConfig",
    "jobs.apps.JobsConfig",
]
~~~

Your actual project may contain other apps. Preserve them.

## 9. Confirm middleware

The standard project should include:
- SecurityMiddleware.
- SessionMiddleware.
- CommonMiddleware.
- CsrfViewMiddleware.
- AuthenticationMiddleware.
- MessageMiddleware.
- Clickjacking protection middleware.

Do not remove middleware from earlier lessons.

## 10. Confirm template configuration

Check:
- APP_DIRS is True.
- request context processor exists.
- auth context processor exists.
- messages context processor exists.

The new jobs templates will be stored inside the jobs app.

## 11. Confirm database configuration

The project has used its configured development database in earlier lessons.

Do not change database settings for this project without a reason.

Run:

~~~powershell
python manage.py showmigrations
~~~

Confirm the previous migrations are present.

---

# PART 3 — CREATE THE JOBS APP

## 12. Create the app

From the folder containing manage.py:

~~~powershell
python manage.py startapp jobs
~~~

Django creates the jobs app.

## 13. Inspect the generated files

~~~text
jobs/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
~~~

Django does not automatically create forms.py, urls.py or templates. We will create them.

## 14. Register the app

Open config/settings.py and add:

~~~python
"jobs.apps.JobsConfig",
~~~

Save the file.

## 15. Confirm app registration

Run:

~~~powershell
python manage.py check
~~~

Expected output when no configuration issues exist:

~~~text
System check identified no issues (0 silenced).
~~~

---

# PART 4 — DESIGN THE DATABASE MODELS

## 16. Identify the main records

The portal needs two main records:

**Job**
- Represents one job opening.
- Has a title, description, location and salary range.
- Belongs to the user who posted it.
- Can be active or closed.

**JobApplication**
- Represents one user's application for one job.
- Belongs to a job.
- Belongs to the applicant.
- Stores a cover letter and submission time.

## 17. Relationship diagram

~~~text
User
  |
  | one user can post many jobs
  v
Job
  |
  | one job can receive many applications
  v
JobApplication
  ^
  |
  | one user can submit many applications
  |
User
~~~

More precisely:
- User to Job: one-to-many through posted_by.
- Job to JobApplication: one-to-many through job.
- User to JobApplication: one-to-many through applicant.
- A unique constraint prevents the same applicant from applying to the same job twice.

## 18. Create Job model

Open jobs/models.py.

Add:

~~~python
from django.conf import settings
from django.db import models
from django.db.models import Q


class Job(models.Model):
    EMPLOYMENT_TYPES = [
        ("FULL_TIME", "Full time"),
        ("PART_TIME", "Part time"),
        ("CONTRACT", "Contract"),
        ("INTERNSHIP", "Internship"),
    ]

    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="posted_jobs",
    )

    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=120)
    description = models.TextField()
    location = models.CharField(max_length=120)

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES,
    )

    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-pk"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(salary_min__isnull=True)
                    | Q(salary_max__isnull=True)
                    | Q(salary_min__lte=models.F("salary_max"))
                ),
                name="job_salary_min_lte_max",
            ),
        ]

    def __str__(self):
        return f"{self.title} at {self.company_name}"
~~~

## 19. Understand the imports

settings:
- Gives access to the configured user model setting.

models:
- Provides model field types and model options.

Q:
- Allows complex database conditions.
- Used here to express a salary rule.

## 20. Understand posted_by

~~~python
posted_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
    related_name="posted_jobs",
)
~~~

ForeignKey:
- Connects a Job record to one user.
- One user may post multiple jobs.
- Each job has one posting user.

settings.AUTH_USER_MODEL:
- Uses the configured user model.
- Avoids hard-coding the default User class.

PROTECT:
- Prevents deleting a user while protected Job records refer to that user.
- This is a data-retention decision for the example.

related_name:
- Allows reverse access such as user.posted_jobs.all().

## 21. Understand choices

EMPLOYMENT_TYPES defines allowed values and human-readable labels.

The database value is:
- FULL_TIME
- PART_TIME
- CONTRACT
- INTERNSHIP

The display label is:
- Full time
- Part time
- Contract
- Internship

Choices improve consistency. Do not store arbitrary spellings such as Fulltime, full time and FULL_TIME for the same category.

## 22. Understand DecimalField

Salary is represented using DecimalField.

max_digits=10:
- Maximum number of digits overall.

decimal_places=2:
- Two digits after the decimal point.

Use Decimal for monetary values rather than float.

The example does not specify a currency. A real portal should define currency and salary-period rules clearly.

## 23. Understand the salary constraint

The constraint ensures that when both salary values exist, minimum salary cannot be greater than maximum salary.

A database constraint protects stored data even when a write does not come through the browser form.

The form should also validate this rule so the user receives a helpful message.

## 24. Create JobApplication model

Continue in jobs/models.py:

~~~python
class JobApplication(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_applications",
    )

    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-applied_at", "-pk"]
        constraints = [
            models.UniqueConstraint(
                fields=["job", "applicant"],
                name="unique_job_applicant",
            ),
        ]

    def __str__(self):
        return f"{self.applicant} - {self.job}"
~~~

## 25. Understand JobApplication fields

job:
- Identifies the job being applied for.
- Many applications can refer to one job.

applicant:
- Identifies the user who submitted the application.
- One user can submit applications for different jobs.

cover_letter:
- Stores the applicant's text.

applied_at:
- Automatically stores the creation timestamp.

## 26. Understand the unique constraint

The constraint:

~~~python
models.UniqueConstraint(
    fields=["job", "applicant"],
    name="unique_job_applicant",
)
~~~

prevents duplicate rows for the same job/applicant pair.

Application-level validation improves the user experience, but the database constraint protects data integrity if two requests arrive at nearly the same time.

## 27. Understand on_delete choices

JobApplication.job uses CASCADE:
- If a job is deleted, related applications are deleted.
- This is a simplified training choice.
- A real recruitment system may need to preserve application history and close/archive the job instead of deleting it.

JobApplication.applicant uses CASCADE:
- Deleting the user deletes their applications.
- A production system may need a retention or anonymization policy instead.

These are important business decisions. Do not copy deletion rules into a real system without review.

---

# PART 5 — CREATE AND APPLY MIGRATIONS

## 28. Create migration

Run:

~~~powershell
python manage.py makemigrations jobs
~~~

Django should create a migration for Job and JobApplication.

## 29. Inspect the migration plan

Run:

~~~powershell
python manage.py sqlmigrate jobs 0001
~~~

If the migration number differs, use the actual number created.

This command shows the SQL Django plans to run for the migration.

Do not edit the database manually based only on the displayed SQL.

## 30. Apply migration

~~~powershell
python manage.py migrate
~~~

Expected:
- The jobs tables are created.
- The database records the migration as applied.
- The salary constraint and unique constraint are added where supported by the configured database.

## 31. Run system checks

~~~powershell
python manage.py check
~~~

If an error appears:
1. Read the full message.
2. Identify the file and line.
3. Check imports and model field names.
4. Check migration dependencies.
5. Fix the smallest issue.
6. Run the check again.

Do not delete migration files as a first response.

---

# PART 6 — REGISTER MODELS IN ADMIN

## 32. Open jobs/admin.py

Add:

~~~python
from django.contrib import admin
from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company_name",
        "location",
        "employment_type",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "employment_type",
        "location",
    )
    search_fields = (
        "title",
        "company_name",
        "location",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "job",
        "applicant",
        "applied_at",
    )
    search_fields = (
        "job__title",
        "applicant__username",
        "applicant__email",
    )
    readonly_fields = ("applied_at",)
~~~

## 33. Understand list_display

list_display controls which fields appear as columns in the admin list.

## 34. Understand list_filter

list_filter adds filter controls to the admin list page.

## 35. Understand search_fields

search_fields enables search across selected model fields.

A double underscore follows relationships:
- job__title searches the related Job title.
- applicant__username searches the related user username.

## 36. Understand readonly_fields

readonly_fields displays values without allowing normal editing through that admin form.

Timestamps created automatically should normally not be edited manually.

---

# PART 7 — CREATE JOB FORMS

## 37. What is a ModelForm?

A ModelForm is a Django form generated from a model.

It helps:
- Define which model fields users can submit.
- Render form fields.
- Validate values.
- Save a model instance.

Do not expose every model field automatically. Choose fields deliberately.

## 38. Create jobs/forms.py

Create the file if it does not exist.

Add:

~~~python
from django import forms
from .models import Job, JobApplication


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "company_name",
            "description",
            "location",
            "employment_type",
            "salary_min",
            "salary_max",
            "is_active",
        ]

    def clean(self):
        cleaned_data = super().clean()

        salary_min = cleaned_data.get("salary_min")
        salary_max = cleaned_data.get("salary_max")

        if (
            salary_min is not None
            and salary_max is not None
            and salary_min > salary_max
        ):
            raise forms.ValidationError(
                "Minimum salary cannot exceed maximum salary."
            )

        return cleaned_data


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["cover_letter"]
        widgets = {
            "cover_letter": forms.Textarea(
                attrs={"rows": 6}
            ),
        }
~~~

## 39. Why posted_by is excluded

The browser must not choose the job owner.

The view will assign:

~~~python
job.posted_by = request.user
~~~

If the form exposed posted_by, a user could attempt to submit another user's ID.

Always assign ownership from the authenticated request.

## 40. Why applicant and job are excluded

The applicant must be request.user.

The job must come from the URL parameter and be retrieved from the database.

The form accepts only the cover letter.

This avoids trusting user-supplied ownership identifiers.

## 41. Understand clean()

clean() is a form-wide validation method.

It is useful when validation depends on more than one field.

The method:
1. Calls the parent clean().
2. Reads cleaned field values.
3. Compares the salary values.
4. Raises ValidationError if the range is invalid.
5. Returns cleaned_data when valid.

## 42. Form validation and database constraints

The form validation displays a helpful message.

The database constraint protects stored data even if a write bypasses this form.

Both layers are useful:
- Form validation: user experience.
- Database constraint: integrity guarantee.

---

# PART 8 — BUILD JOB LIST AND SEARCH

## 43. Create jobs/views.py

Open jobs/views.py.

Add imports:

~~~python
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import JobApplicationForm, JobForm
from .models import Job, JobApplication
~~~

Keep imports organized and remove unused imports after implementation.

## 44. Job list view

Add:

~~~python
def job_list(request):
    search_term = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()
    employment_type = request.GET.get("type", "").strip()

    jobs = Job.objects.filter(is_active=True)

    if search_term:
        jobs = jobs.filter(
            Q(title__icontains=search_term)
            | Q(company_name__icontains=search_term)
            | Q(description__icontains=search_term)
        )

    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    allowed_types = {
        value
        for value, label in Job.EMPLOYMENT_TYPES
    }

    if employment_type in allowed_types:
        jobs = jobs.filter(
            employment_type=employment_type
        )
    elif employment_type:
        employment_type = ""

    jobs = jobs.order_by("-created_at", "-pk")

    paginator = Paginator(jobs, 10)
    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    query_params = request.GET.copy()
    pagination_links = {
        "previous": None,
        "next": None,
    }

    if page_obj.has_previous():
        previous_params = query_params.copy()
        previous_params["page"] = page_obj.previous_page_number()
        pagination_links["previous"] = (
            "?" + previous_params.urlencode()
        )

    if page_obj.has_next():
        next_params = query_params.copy()
        next_params["page"] = page_obj.next_page_number()
        pagination_links["next"] = (
            "?" + next_params.urlencode()
        )

    return render(
        request,
        "jobs/job_list.html",
        {
            "page_obj": page_obj,
            "search_term": search_term,
            "location": location,
            "employment_type": employment_type,
            "employment_types": Job.EMPLOYMENT_TYPES,
            "pagination_links": pagination_links,
        },
    )
~~~

## 45. Understand job search

The view starts with active jobs only.

It optionally searches:
- Title.
- Company name.
- Description.

Q objects combine these conditions with OR.

Location is a separate filter.

Employment type is checked against the model's allowed choices.

## 46. Why validate employment type?

The browser can send any value.

The view accepts only values defined in Job.EMPLOYMENT_TYPES.

This prevents unexpected filter values from being treated as valid categories.

## 47. Why order before pagination?

A stable order ensures that the same result set is arranged predictably.

The view uses:
- newest created_at first.
- primary key as tie-breaker.

---

# PART 9 — JOB DETAIL AND APPLICATION

## 48. Job detail view

Add:

~~~python
def job_detail(request, pk):
    job = get_object_or_404(
        Job,
        pk=pk,
        is_active=True,
    )

    already_applied = False

    if request.user.is_authenticated:
        already_applied = JobApplication.objects.filter(
            job=job,
            applicant=request.user,
        ).exists()

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job,
            "already_applied": already_applied,
        },
    )
~~~

## 49. Why check already_applied?

The page can display whether the current user has already applied.

This improves the interface.

The database unique constraint remains the final protection against duplicates.

## 50. Apply view

Add:

~~~python
@login_required
@require_POST
def apply_to_job(request, pk):
    job = get_object_or_404(
        Job,
        pk=pk,
        is_active=True,
    )

    form = JobApplicationForm(request.POST)

    if not form.is_valid():
        messages.error(
            request,
            "Please correct the application form.",
        )
        return redirect("job_detail", pk=job.pk)

    application = form.save(commit=False)
    application.job = job
    application.applicant = request.user

    try:
        with transaction.atomic():
            application.save()
    except IntegrityError:
        messages.warning(
            request,
            "You have already applied for this job.",
        )
        return redirect("job_detail", pk=job.pk)

    messages.success(
        request,
        "Your application was submitted successfully.",
    )
    return redirect("my_applications")
~~~

## 51. Understand login_required

Only authenticated users can apply.

Anonymous visitors are redirected to login.

## 52. Understand require_POST

Application submission changes database state.

The view accepts POST only.

A GET request must not create an application.

## 53. Understand commit=False

form.save(commit=False) creates a model instance without immediately writing it to the database.

The view fills fields that the browser is not allowed to control:
- job
- applicant

Then the view saves the instance.

## 54. Understand transaction.atomic()

transaction.atomic() groups database operations into a transaction.

If a database error occurs during the block, the transaction is rolled back.

This is important for multi-step operations.

## 55. Understand IntegrityError

The unique constraint prevents duplicate applications.

A race condition can occur:
- Two requests arrive close together.
- Both pass the initial page-level check.
- Both attempt to create an application.

The database constraint protects the record.

The view catches IntegrityError and displays a safe message.

Do not catch every possible exception and pretend it means duplicate application. Catch only the expected integrity failure around the save operation.

## 56. My applications view

Add:

~~~python
@login_required
def my_applications(request):
    applications = (
        JobApplication.objects
        .filter(applicant=request.user)
        .select_related("job")
        .order_by("-applied_at", "-pk")
    )

    return render(
        request,
        "jobs/my_applications.html",
        {"applications": applications},
    )
~~~

This view filters by the current user.

A user must not see another user's applications.

---

# PART 10 — EMPLOYER JOB MANAGEMENT

## 57. Authorization design

Creating and managing jobs is a privileged action.

This lesson uses Django's add and change model permissions.

The permission strings are:
- jobs.add_job
- jobs.change_job

A group such as Employers can receive these permissions.

The view must still check ownership where required.

## 58. Create job view

Add:

~~~python
@login_required
@permission_required("jobs.add_job", raise_exception=True)
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()

            messages.success(
                request,
                "Job opening created successfully.",
            )
            return redirect("job_detail", pk=job.pk)
    else:
        form = JobForm()

    return render(
        request,
        "jobs/job_form.html",
        {"form": form},
    )
~~~

## 59. Why assign posted_by in the view?

The browser must not choose the owner.

The authenticated user is the owner for this operation.

## 60. Edit job view with ownership check

Add:

~~~python
@login_required
@permission_required("jobs.change_job", raise_exception=True)
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if (
        not request.user.is_superuser
        and job.posted_by_id != request.user.pk
    ):
        messages.error(
            request,
            "You cannot edit a job posted by another user.",
        )
        return redirect("job_list")

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Job opening updated successfully.",
            )
            return redirect("job_detail", pk=job.pk)
    else:
        form = JobForm(instance=job)

    return render(
        request,
        "jobs/job_form.html",
        {
            "form": form,
            "job": job,
        },
    )
~~~

This policy allows:
- Users with the change_job permission to edit their own jobs.
- Superusers to edit any job.

A real application may use a different ownership and staff policy. Define it explicitly.

## 61. Close job view

A safer workflow is to close a job rather than delete it.

Add:

~~~python
@login_required
@permission_required("jobs.change_job", raise_exception=True)
@require_POST
def close_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if (
        not request.user.is_superuser
        and job.posted_by_id != request.user.pk
    ):
        messages.error(
            request,
            "You cannot close a job posted by another user.",
        )
        return redirect("job_list")

    job.is_active = False
    job.save(update_fields=["is_active", "updated_at"])

    messages.success(
        request,
        "The job opening has been closed.",
    )
    return redirect("job_detail", pk=job.pk)
~~~

## 62. Why close instead of delete?

Closing a job:
- Preserves its record.
- Keeps application history.
- Prevents new applications.
- Allows reporting and audit history.

Deleting a job may remove related applications because of the example's CASCADE rule.

For a real recruitment application, archiving is often safer than deleting.

## 63. View applicant list for a job

Add:

~~~python
@login_required
@permission_required("jobs.change_job", raise_exception=True)
def job_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if (
        not request.user.is_superuser
        and job.posted_by_id != request.user.pk
    ):
        messages.error(
            request,
            "You cannot view applications for this job.",
        )
        return redirect("job_list")

    applications = (
        job.applications
        .select_related("applicant")
        .order_by("-applied_at", "-pk")
    )

    return render(
        request,
        "jobs/job_applicants.html",
        {
            "job": job,
            "applications": applications,
        },
    )
~~~

The ownership check protects applicants' personal information.

---

# PART 11 — CREATE URL CONFIGURATION

## 64. Create jobs/urls.py

Create the file.

Add:

~~~python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("create/", views.job_create, name="job_create"),
    path("<int:pk>/edit/", views.job_update, name="job_update"),
    path("<int:pk>/close/", views.close_job, name="close_job"),
    path(
        "<int:pk>/applicants/",
        views.job_applicants,
        name="job_applicants",
    ),
    path(
        "<int:pk>/apply/",
        views.apply_to_job,
        name="apply_to_job",
    ),
    path(
        "my-applications/",
        views.my_applications,
        name="my_applications",
    ),
]
~~~

Important route-order note:
- The empty path matches the job list.
- More specific route paths should be tested carefully.
- Django checks URL patterns in order.
- If a route conflict occurs, move the more specific patterns before broad patterns.

## 65. Include jobs URLs

Open config/urls.py.

Add:

~~~python
path("jobs/", include("jobs.urls")),
~~~

Example:

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("jobs/", include("jobs.urls")),
    path("", include("profiles.urls")),
]
~~~

Preserve existing route includes.

## 66. Route reference table

| Browser path | Name | Method | Purpose |
|---|---|---|---|
| /jobs/ | job_list | GET | Browse jobs |
| /jobs/12/ | job_detail | GET | View job 12 |
| /jobs/create/ | job_create | GET, POST | Create job |
| /jobs/12/edit/ | job_update | GET, POST | Edit job 12 |
| /jobs/12/close/ | close_job | POST | Close job 12 |
| /jobs/12/applicants/ | job_applicants | GET | View applications |
| /jobs/12/apply/ | apply_to_job | POST | Apply to job 12 |
| /jobs/my-applications/ | my_applications | GET | View current user's applications |

The exact route order and names must match the URL file.

---

# PART 12 — CREATE TEMPLATES

## 67. Create template folders

Create:

~~~text
jobs/
└── templates/
    └── jobs/
        ├── base.html
        ├── job_list.html
        ├── job_detail.html
        ├── job_form.html
        ├── my_applications.html
        └── job_applicants.html
~~~

## 68. Create base.html

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Job Portal{% endblock %}</title>
</head>
<body>
    <header>
        <h1><a href="{% url 'job_list' %}">Job Portal</a></h1>

        <nav>
            <a href="{% url 'job_list' %}">Browse jobs</a>

            {% if user.is_authenticated %}
                <a href="{% url 'my_applications' %}">
                    My applications
                </a>

                <form method="post" action="{% url 'logout' %}">
                    {% csrf_token %}
                    <button type="submit">Sign out</button>
                </form>
            {% else %}
                <a href="{% url 'login' %}">Sign in</a>
                <a href="{% url 'register' %}">Register</a>
            {% endif %}
        </nav>
    </header>

    {% if messages %}
        <section aria-live="polite">
            {% for message in messages %}
                <p class="{{ message.tags }}">{{ message }}</p>
            {% endfor %}
        </section>
    {% endif %}

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
~~~

This template assumes the profiles app already provides login, logout and register URL names from Days 46–47.

## 69. Create job_list.html

~~~django
{% extends "jobs/base.html" %}

{% block title %}Browse Jobs{% endblock %}

{% block content %}
<h2>Available jobs</h2>

<form method="get">
    <label for="q">Search</label>
    <input
        type="search"
        id="q"
        name="q"
        value="{{ search_term }}"
        placeholder="Title, company or description"
    >

    <label for="location">Location</label>
    <input
        type="text"
        id="location"
        name="location"
        value="{{ location }}"
    >

    <label for="type">Employment type</label>
    <select name="type" id="type">
        <option value="">All types</option>
        {% for value, label in employment_types %}
            <option
                value="{{ value }}"
                {% if employment_type == value %}selected{% endif %}
            >
                {{ label }}
            </option>
        {% endfor %}
    </select>

    <button type="submit">Search jobs</button>
    <a href="{% url 'job_list' %}">Clear</a>
</form>

{% for job in page_obj %}
    <article>
        <h3>
            <a href="{% url 'job_detail' job.pk %}">
                {{ job.title }}
            </a>
        </h3>
        <p>{{ job.company_name }}</p>
        <p>{{ job.location }}</p>
        <p>{{ job.get_employment_type_display }}</p>
        <p>Posted {{ job.created_at }}</p>
    </article>
{% empty %}
    <p>No active jobs match your search.</p>
{% endfor %}

<nav aria-label="Job pages">
    {% if pagination_links.previous %}
        <a href="{{ pagination_links.previous }}">Previous</a>
    {% endif %}

    <span>
        Page {{ page_obj.number }}
        of {{ page_obj.paginator.num_pages }}
    </span>

    {% if pagination_links.next %}
        <a href="{{ pagination_links.next }}">Next</a>
    {% endif %}
</nav>
{% endblock %}
~~~

## 70. Create job_detail.html

~~~django
{% extends "jobs/base.html" %}

{% block title %}{{ job.title }}{% endblock %}

{% block content %}
<article>
    <h2>{{ job.title }}</h2>
    <p>{{ job.company_name }}</p>
    <p>{{ job.location }}</p>
    <p>{{ job.get_employment_type_display }}</p>

    {% if job.salary_min or job.salary_max %}
        <p>
            Salary range:
            {{ job.salary_min|default:"Not specified" }}
            -
            {{ job.salary_max|default:"Not specified" }}
        </p>
    {% endif %}

    <section>
        <h3>Job description</h3>
        {{ job.description|linebreaks }}
    </section>

    {% if user.is_authenticated %}
        {% if already_applied %}
            <p>You have already applied for this job.</p>
        {% else %}
            <form method="post"
                  action="{% url 'apply_to_job' job.pk %}">
                {% csrf_token %}
                <label for="cover_letter">Cover letter</label>
                <textarea
                    id="cover_letter"
                    name="cover_letter"
                    rows="6"
                    required
                ></textarea>
                <button type="submit">Apply now</button>
            </form>
        {% endif %}
    {% else %}
        <p>
            <a href="{% url 'login' %}">Sign in</a>
            to apply for this job.
        </p>
    {% endif %}

    {% if user.is_authenticated and job.posted_by_id == user.pk or user.is_superuser %}
        <a href="{% url 'job_update' job.pk %}">Edit job</a>

        <a href="{% url 'job_applicants' job.pk %}">
            View applicants
        </a>

        {% if job.is_active %}
            <form method="post"
                  action="{% url 'close_job' job.pk %}">
                {% csrf_token %}
                <button type="submit">Close job</button>
            </form>
        {% endif %}
    {% endif %}
</article>
{% endblock %}
~~~

Template conditional note:
- For complex ownership/permission logic, prepare explicit Boolean values in the view.
- Do not rely on complicated template conditions as the security boundary.
- The edit and applicants views must still enforce permissions and ownership.

## 71. Improve detail view context for ownership

For a clearer template, update job_detail view to calculate:

~~~python
can_manage_job = (
    request.user.is_authenticated
    and (
        request.user.is_superuser
        or (
            request.user.has_perm("jobs.change_job")
            and job.posted_by_id == request.user.pk
        )
    )
)
~~~

Pass can_manage_job to the template.

Then use:

~~~django
{% if can_manage_job %}
    ...
{% endif %}
~~~

This improves presentation. Backend views still enforce access.

## 72. Create job_form.html

~~~django
{% extends "jobs/base.html" %}

{% block title %}Job Form{% endblock %}

{% block content %}
<h2>
    {% if job %}Edit job{% else %}Create job{% endif %}
</h2>

<form method="post">
    {% csrf_token %}

    {{ form.non_field_errors }}

    {% for field in form %}
        <div>
            {{ field.label_tag }}
            {{ field }}
            {{ field.errors }}

            {% if field.help_text %}
                <small>{{ field.help_text }}</small>
            {% endif %}
        </div>
    {% endfor %}

    <button type="submit">Save job</button>
</form>
{% endblock %}
~~~

## 73. Create my_applications.html

~~~django
{% extends "jobs/base.html" %}

{% block title %}My Applications{% endblock %}

{% block content %}
<h2>My applications</h2>

{% for application in applications %}
    <article>
        <h3>
            <a href="{% url 'job_detail' application.job.pk %}">
                {{ application.job.title }}
            </a>
        </h3>
        <p>{{ application.job.company_name }}</p>
        <p>Applied: {{ application.applied_at }}</p>
    </article>
{% empty %}
    <p>You have not applied for any jobs yet.</p>
{% endfor %}
{% endblock %}
~~~

## 74. Create job_applicants.html

~~~django
{% extends "jobs/base.html" %}

{% block title %}Applicants{% endblock %}

{% block content %}
<h2>Applicants for {{ job.title }}</h2>

{% for application in applications %}
    <article>
        <h3>{{ application.applicant.username }}</h3>
        <p>{{ application.applicant.email }}</p>
        <p>Applied: {{ application.applied_at }}</p>
        <h4>Cover letter</h4>
        {{ application.cover_letter|linebreaks }}
    </article>
{% empty %}
    <p>No applications have been submitted.</p>
{% endfor %}
{% endblock %}
~~~

Applicant data is private. The job_applicants view must enforce ownership and permission checks before rendering this template.

---

# PART 13 — SET UP EMPLOYER PERMISSIONS

## 75. Default permissions

After jobs migrations, Django creates default model permissions for Job and JobApplication.

For Job:
- jobs.add_job
- jobs.change_job
- jobs.delete_job
- jobs.view_job

## 76. Create an Employers group

Open the shell:

~~~powershell
python manage.py shell
~~~

Run:

~~~python
from django.contrib.auth.models import Group, Permission

employers, created = Group.objects.get_or_create(
    name="Employers"
)

add_job = Permission.objects.get(
    content_type__app_label="jobs",
    codename="add_job",
)

change_job = Permission.objects.get(
    content_type__app_label="jobs",
    codename="change_job",
)

view_job = Permission.objects.get(
    content_type__app_label="jobs",
    codename="view_job",
)

employers.permissions.add(
    add_job,
    change_job,
    view_job,
)
~~~

The group does not receive delete_job in this example.

## 77. Add a user to Employers

~~~python
from django.contrib.auth import get_user_model

User = get_user_model()

employer_user = User.objects.get(
    username="employer_demo"
)

employer_user.groups.add(employers)
~~~

Use a fictional local account.

## 78. Verify permissions

~~~python
employer_user.has_perm("jobs.add_job")
employer_user.has_perm("jobs.change_job")
employer_user.has_perm("jobs.delete_job")
~~~

Expected:
- add_job: True.
- change_job: True.
- delete_job: False.

This assumes no other direct or group permission grants delete access and the user is not a superuser.

---

# PART 14 — END-TO-END VALIDATION

## 79. Validate configuration

Run:

~~~powershell
python manage.py check
~~~

Expected:

~~~text
System check identified no issues (0 silenced).
~~~

## 80. Validate migrations

Run:

~~~powershell
python manage.py makemigrations --check --dry-run
python manage.py migrate --check
~~~

The first command checks whether model changes are missing migration files.

The second checks whether unapplied migrations remain.

## 81. Validate admin

Run:

~~~powershell
python manage.py createsuperuser
~~~

If a superuser already exists, do not create another unnecessarily.

Start the server:

~~~powershell
python manage.py runserver
~~~

Open /admin/ and verify:
- Job model appears.
- JobApplication model appears.
- List displays and search fields work.
- Related user and job values appear.

## 82. Manual job seeker journey

1. Open the registration page.
2. Create a fictional job seeker account.
3. Sign in.
4. Open /jobs/.
5. Search for a job.
6. Filter by location and employment type.
7. Open a job detail page.
8. Submit an application.
9. Open My Applications.
10. Confirm the application appears.
11. Try applying again.
12. Confirm duplicate application is prevented.
13. Sign out.
14. Try to open My Applications.
15. Confirm redirection to login.

## 83. Manual employer journey

1. Create a fictional employer account.
2. Add the account to Employers group.
3. Sign in as the employer.
4. Open the create-job page.
5. Create a job.
6. Open the job detail page.
7. Edit the job.
8. Close the job.
9. Confirm the closed job no longer appears in the active job list.
10. Reopen the job detail through a direct URL if the design allows it.
11. Confirm new applications are not accepted for closed jobs.
12. View applications for a job owned by that employer.

## 84. Authorization journey

Test:
- Job seeker attempts to create a job.
- Employer attempts to edit another employer's job.
- Employer attempts to view another employer's applicants.
- Anonymous visitor attempts to apply.
- A signed-in user tries to apply to the same job twice.

Expected:
- Unauthorized job management is denied.
- Ownership checks block access to another employer's private applications.
- Anonymous visitors must sign in.
- Duplicate application is blocked by application validation and database constraint.

---

# PART 15 — AUTOMATED TESTS

## 85. Why integration tests matter

A page loading successfully does not prove the complete workflow works.

Test:
- Model constraints.
- Form validation.
- View authorization.
- URL resolution.
- Database writes.
- Redirects.
- Message feedback.
- Ownership restrictions.

## 86. Create jobs/tests.py

Use the following as a starting test suite. Keep tests that already exist and merge imports/classes carefully.

~~~python
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse

from .forms import JobForm
from .models import Job, JobApplication

User = get_user_model()


class JobModelTests(TestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            username="model_employer",
            password="Test-Only-Password-123!",
        )

    def test_job_string_representation(self):
        job = Job.objects.create(
            posted_by=self.employer,
            title="Python Developer",
            company_name="Example Tech",
            description="Build backend services.",
            location="Hyderabad",
            employment_type="FULL_TIME",
        )

        self.assertEqual(
            str(job),
            "Python Developer at Example Tech",
        )

    def test_salary_range_validation(self):
        form = JobForm(
            data={
                "title": "Backend Developer",
                "company_name": "Example Tech",
                "description": "Build APIs.",
                "location": "Hyderabad",
                "employment_type": "FULL_TIME",
                "salary_min": "90000.00",
                "salary_max": "50000.00",
                "is_active": True,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)


class JobApplicationTests(TestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            username="application_employer",
            password="Test-Only-Password-123!",
        )
        self.applicant = User.objects.create_user(
            username="application_seeker",
            password="Test-Only-Password-123!",
        )
        self.job = Job.objects.create(
            posted_by=self.employer,
            title="Django Developer",
            company_name="Example Company",
            description="Develop Django applications.",
            location="Hyderabad",
            employment_type="FULL_TIME",
            is_active=True,
        )

    def test_authenticated_user_can_apply(self):
        self.client.force_login(self.applicant)

        response = self.client.post(
            reverse("apply_to_job", args=[self.job.pk]),
            {"cover_letter": "I am interested in this role."},
        )

        self.assertRedirects(
            response,
            reverse("my_applications"),
        )
        self.assertTrue(
            JobApplication.objects.filter(
                job=self.job,
                applicant=self.applicant,
            ).exists()
        )

    def test_anonymous_user_cannot_apply(self):
        response = self.client.post(
            reverse("apply_to_job", args=[self.job.pk]),
            {"cover_letter": "Test letter"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            JobApplication.objects.count(),
            0,
        )

    def test_duplicate_application_is_rejected(self):
        JobApplication.objects.create(
            job=self.job,
            applicant=self.applicant,
            cover_letter="First application",
        )

        self.client.force_login(self.applicant)

        response = self.client.post(
            reverse("apply_to_job", args=[self.job.pk]),
            {"cover_letter": "Second application"},
        )

        self.assertRedirects(
            response,
            reverse("job_detail", args=[self.job.pk]),
        )
        self.assertEqual(
            JobApplication.objects.filter(
                job=self.job,
                applicant=self.applicant,
            ).count(),
            1,
        )

    def test_my_applications_shows_only_current_user(self):
        other_user = User.objects.create_user(
            username="another_seeker",
            password="Test-Only-Password-123!",
        )

        JobApplication.objects.create(
            job=self.job,
            applicant=other_user,
            cover_letter="Private application",
        )

        self.client.force_login(self.applicant)

        response = self.client.get(
            reverse("my_applications")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["applications"].count(),
            0,
        )


class EmployerPermissionTests(TestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            username="permission_employer",
            password="Test-Only-Password-123!",
        )

        self.seeker = User.objects.create_user(
            username="permission_seeker",
            password="Test-Only-Password-123!",
        )

        self.group = Group.objects.create(name="Test Employers")

        self.add_permission = Permission.objects.get(
            content_type__app_label="jobs",
            codename="add_job",
        )
        self.change_permission = Permission.objects.get(
            content_type__app_label="jobs",
            codename="change_job",
        )

        self.group.permissions.add(
            self.add_permission,
            self.change_permission,
        )
        self.employer.groups.add(self.group)

    def test_employer_has_add_permission(self):
        self.assertTrue(
            self.employer.has_perm("jobs.add_job")
        )

    def test_job_seeker_lacks_add_permission(self):
        self.assertFalse(
            self.seeker.has_perm("jobs.add_job")
        )

    def test_job_create_denied_without_permission(self):
        self.client.force_login(self.seeker)

        response = self.client.get(
            reverse("job_create")
        )

        self.assertEqual(response.status_code, 403)
~~~

## 87. Important test assumptions

The tests assume:
- The app label is jobs.
- Model names are Job and JobApplication.
- The URL names match this lesson.
- The create view uses permission_required with raise_exception=True.
- The JobForm performs salary range validation.
- The application view redirects to my_applications on success.

If your implementation intentionally uses a different policy, update the tests to match the approved behavior.

## 88. Run the tests

~~~powershell
python manage.py test jobs
~~~

Then run all project tests:

~~~powershell
python manage.py test
~~~

The full test command may run tests from profiles, catalog and jobs.

## 89. Understand test output

A passing test run ends with:

~~~text
Ran N tests
OK
~~~

The number N depends on the project.

A test failure should be investigated, not hidden by deleting the test.

---

# PART 16 — COMMON ERRORS AND TROUBLESHOOTING

## 90. NoReverseMatch

Check:
- URL name exists.
- The route is included in config/urls.py.
- The correct primary key argument is supplied.
- The app URL prefix is correct.
- The route order does not capture another path.

## 91. PermissionDenied

Check:
- The user is in the correct group.
- The group has the correct permission.
- The permission codename uses the correct app label and model.
- The user is not using an unexpected account.
- The user is not a superuser during the test.

## 92. Job creation denied for employer

Check:
- jobs app is installed.
- Job migrations are applied.
- add_job permission exists.
- Employer group has the permission.
- User belongs to the group.
- The browser is signed in as the intended user.

## 93. IntegrityError for duplicate application

This may be expected when the same applicant applies twice.

The view should catch the expected duplicate constraint error and show a safe message.

Do not remove the unique constraint.

## 94. Salary constraint failure

Check:
- salary_min is less than or equal to salary_max.
- Empty salary values are allowed as intended.
- The form validation matches the database constraint.
- Decimal values are used.

## 95. TemplateDoesNotExist

Check:
- jobs app is installed.
- Template folder is jobs/templates/jobs.
- The filename matches the render() call.
- APP_DIRS is enabled.
- The correct project is running.

## 96. Application list shows another user's data

Check that the QuerySet includes:

~~~python
.filter(applicant=request.user)
~~~

Do not remove this filter.

Also verify that the template is rendering the view's filtered context rather than querying all applications separately.

## 97. Employer can edit another employer's job

Check:
- The job_update view performs the ownership check.
- The permission check is present.
- The applicant list view has its own ownership check.
- No alternate route bypasses the protection.

Hiding the edit link is not enough.

## 98. Closed job still accepts applications

Check that apply_to_job retrieves only active jobs:

~~~python
get_object_or_404(
    Job,
    pk=pk,
    is_active=True,
)
~~~

A closed job should not be eligible for new applications.

## 99. Migration conflict

Check:
- Which project directory contains manage.py?
- Which migration files were changed?
- Is the database using the expected settings?
- Did two branches create conflicting migrations?

Do not delete migrations or reset the database as a first response. Inspect the migration graph and resolve the actual conflict.

---

# PART 17 — PRODUCTION READINESS DISCUSSION

## 100. What this training project does not include

This is an educational Django application, not a complete commercial recruitment platform.

It does not implement:
- Real email verification.
- Resume file upload and scanning.
- Payment processing.
- Background tasks.
- Advanced audit trails.
- Multi-tenant organization isolation.
- Production deployment.
- Full privacy and data-retention policy.
- High-volume search infrastructure.
- Advanced spam and abuse controls.

Do not claim these features exist unless they are implemented and tested.

## 101. Security checklist

Before production:
- Enforce HTTPS.
- Configure secure cookies.
- Store secrets outside source control.
- Review password validators.
- Add rate limiting to sensitive endpoints.
- Validate all user input.
- Check object ownership.
- Restrict applicant personal data.
- Use CSRF protection.
- Avoid exposing stack traces.
- Review file upload handling if introduced.
- Back up the database.
- Apply security updates.
- Monitor errors without logging secrets.

## 102. Data integrity checklist

- Job salary range is valid.
- One applicant cannot apply twice to the same job.
- Job owner is assigned by the server.
- Applicant is assigned by the server.
- Closed jobs cannot receive applications.
- Applications are filtered by current user.
- Employer-only views check permissions and ownership.

## 103. Performance checklist

- Use pagination for job lists.
- Use select_related() for foreign-key display where needed.
- Use prefetch_related() for reverse or many-to-many collections where needed.
- Avoid querying inside template loops.
- Inspect database query counts for high-traffic pages.
- Add indexes only when supported by query patterns and measurements.

---

# PART 18 — FINAL PROJECT ACCEPTANCE

## 104. Job Portal Web Application acceptance criteria

### Job seeker

- [ ] Can register.
- [ ] Can sign in.
- [ ] Can browse active jobs.
- [ ] Can search by title/company/description.
- [ ] Can filter by location and employment type.
- [ ] Can open job details.
- [ ] Can apply while authenticated.
- [ ] Cannot apply to a closed job.
- [ ] Cannot submit duplicate applications.
- [ ] Can view only their own applications.
- [ ] Can sign out.

### Employer

- [ ] Can sign in.
- [ ] Has the correct group permission.
- [ ] Can create a job.
- [ ] Is assigned as job owner by the server.
- [ ] Can edit their own job.
- [ ] Cannot edit another employer's job.
- [ ] Can close their own job.
- [ ] Can view applicants for their own job.
- [ ] Cannot view another employer's applicants.

### Application quality

- [ ] Models are migrated.
- [ ] Forms validate inputs.
- [ ] Database constraints protect integrity.
- [ ] URLs map to the correct views.
- [ ] Templates render expected data.
- [ ] Messages provide clear feedback.
- [ ] Pagination works.
- [ ] Search/filter state is preserved.
- [ ] Automated tests pass.
- [ ] No real secrets or credentials are committed.

## 105. Submission structure

Submit a project folder or repository containing:

~~~text
job_portal_submission/
├── README.md
├── requirements.txt
├── manage.py
├── config/
├── profiles/
├── catalog/
└── jobs/
~~~

Do not include:
- .venv/
- __pycache__/
- real passwords.
- secret keys.
- session cookies.
- reset tokens.
- private database dumps.

## 106. README content

Your README should explain:
1. Project purpose.
2. Python and Django versions.
3. Environment setup.
4. Dependency installation.
5. Database migrations.
6. How to create a superuser.
7. How to create an employer group.
8. How to run the server.
9. Main URLs.
10. How to run tests.
11. Known limitations.
12. Screenshots or evidence using fictional data.

---

# PART 19 — SELF-ASSESSMENT

## 107. Short-answer questions

1. What does integration mean in a Django application?
2. Why do we separate features into apps?
3. What is the purpose of the Job model?
4. What is the purpose of JobApplication?
5. Why use settings.AUTH_USER_MODEL?
6. What does ForeignKey represent?
7. Why use a unique constraint on job and applicant?
8. Why exclude posted_by from JobForm?
9. Why exclude applicant and job from JobApplicationForm?
10. What does form.save(commit=False) do?
11. Why use transaction.atomic()?
12. Why is IntegrityError handled?
13. Why does job_list use Q objects?
14. Why paginate job results?
15. Why does my_applications filter by request.user?
16. Why does job_update check ownership?
17. Why should closing a job be POST?
18. Why is hiding a button not enough?
19. What does select_related() help with?
20. What should be tested before publishing a paid learning project?

## 108. Self-check answers

1. Connecting models, forms, views, URLs, templates, auth and database behavior into one workflow.
2. Apps keep related features organized and maintainable.
3. It stores a job opening.
4. It stores one user's application to one job.
5. It references the configured user model.
6. A many-to-one relationship.
7. It prevents duplicate applications at database level.
8. The server must assign the authenticated owner.
9. The server must assign the job and applicant from trusted request/database data.
10. It creates an unsaved model instance.
11. It groups database operations into a transaction.
12. It handles a database uniqueness failure safely.
13. It combines search conditions with OR.
14. It keeps result pages manageable.
15. It prevents one user from viewing another user's applications.
16. Permission alone may not restrict which individual job can be edited.
17. Closing changes database state.
18. A user can manually request the endpoint.
19. It retrieves related foreign-key objects efficiently with a join.
20. Normal flows, invalid input, permissions, ownership, database constraints, migrations, templates, tests and deployment limitations.

## 109. MCQ assessment

### Question 1
Which model stores a user's application to a job?

- A. JobApplication
- B. Session
- C. Permission
- D. Message

**Answer: A.** JobApplication connects the job and applicant and stores application details.

### Question 2
Why is posted_by excluded from the JobForm?

- A. It is not a database field
- B. The server should assign the authenticated owner
- C. It is a template name
- D. It is a session key

**Answer: B.** Ownership must come from trusted request context, not browser input.

### Question 3
What prevents the same applicant applying to the same job twice at database level?

- A. CSS class
- B. UniqueConstraint
- C. Redirect
- D. Pagination

**Answer: B.** The database constraint protects against duplicate job/applicant pairs.

### Question 4
Why does my_applications filter by request.user?

- A. To show every application
- B. To show only the current user's applications
- C. To delete applications
- D. To change job salary

**Answer: B.** It enforces user-specific data access.

### Question 5
Why must employer ownership be checked in the backend?

- A. Templates are slow
- B. Users can manually request URLs
- C. Models cannot use permissions
- D. Django does not support redirects

**Answer: B.** A hidden link does not prevent direct access to an endpoint.

### Question 6
What is the purpose of transaction.atomic()?

- A. Group database operations transactionally
- B. Create HTML templates
- C. Send email
- D. Change a URL

**Answer: A.** It helps ensure related database operations are committed or rolled back together.

### Question 7
Which view should normally require authentication before a job application is submitted?

- A. job_list
- B. job_detail
- C. apply_to_job
- D. static page

**Answer: C.** Applying creates a user-specific database record.

### Question 8
Which HTTP method should close a job?

- A. GET
- B. POST
- C. TRACE
- D. OPTIONS

**Answer: B.** Closing a job changes server state.

---

# PART 20 — INTERVIEW PREPARATION

## 110. Explain the Job Portal architecture

**Answer:** The jobs app contains Job and JobApplication models, forms for job creation and application, views for browsing and managing jobs, URL patterns and templates. Authentication identifies users, permissions control employer actions, ownership checks restrict access to individual jobs, and database constraints protect duplicate applications and salary rules.

**Follow-up:** Why not place every model in profiles/models.py?

**Answer:** A separate jobs app keeps the job domain organized and makes the application easier to maintain.

## 111. Why use a database unique constraint for applications?

**Answer:** Application-level checks improve the user experience, but two requests can arrive at nearly the same time. A database unique constraint is the final protection against duplicate job/applicant pairs.

**Follow-up:** What exception may be raised?

**Answer:** IntegrityError.

## 112. Why use transaction.atomic()?

**Answer:** It groups database operations into a transaction. If a failure occurs inside the block, the transaction can be rolled back rather than leaving a partial result.

**Follow-up:** Does atomic() replace validation?

**Answer:** No. Forms and model/database constraints still validate data.

## 113. Why assign applicant from request.user?

**Answer:** The applicant identity must come from the authenticated request. If the browser could submit an arbitrary applicant ID, one user could attempt to create an application for another user.

## 114. Why check job ownership in addition to change permission?

**Answer:** A model permission can allow a user to change Job records generally. The business rule may allow them to edit only jobs they posted. The view must check the specific object's owner.

## 115. Scenario: employer changes the job ID in the URL

**Answer:** The view must retrieve the job and compare its owner with the current user after checking the required permission. If the user does not own the job and is not an authorized administrator, deny access.

## 116. Scenario: a user can see another user's applications

**Answer:** The application list query is missing the applicant=request.user filter or the view exposes an unfiltered QuerySet. Filter the queryset by the current user and test with two separate accounts.

## 117. Scenario: duplicate applications appear

**Answer:** Add application-level feedback and a database UniqueConstraint on job and applicant. Handle the expected IntegrityError so the user receives a safe message.

---

# PART 21 — FINAL INDEPENDENT COMPLETION

## 118. Explain the complete request flow

Choose one action: a student applies for a job.

Explain:
1. Which URL receives the request?
2. Which view handles it?
3. Which HTTP method is accepted?
4. How is the user authenticated?
5. How is the job retrieved?
6. How is the form validated?
7. How are job and applicant assigned?
8. Which database constraint protects duplicate applications?
9. How is the message added?
10. Where is the browser redirected?
11. Which template displays the result?
12. Which test proves the workflow works?

## 119. Explain the employer flow

Explain:
1. How employer permission is assigned.
2. How the create view checks permission.
3. How posted_by is assigned.
4. How edit view checks ownership.
5. How applicant list is protected.
6. Why closing a job is POST.
7. Why a hidden template link is not enough.

## 120. Controlled debugging

In a local practice branch:
- Remove the jobs app from INSTALLED_APPS and inspect the failure.
- Restore it.
- Change a URL name and inspect NoReverseMatch.
- Restore it.
- Submit a salary range where minimum exceeds maximum.
- Submit a duplicate application.
- Try editing another employer's job.
- Try applying to a closed job.
- Restore the correct code and re-run all tests.

Do not commit intentional errors.

## 121. Final checklist

- [ ] I created the jobs app.
- [ ] I registered it.
- [ ] I created Job and JobApplication models.
- [ ] I applied migrations.
- [ ] I registered models in admin.
- [ ] I created and validated forms.
- [ ] I built job list and detail views.
- [ ] I implemented search and filters.
- [ ] I implemented pagination.
- [ ] I implemented authenticated applications.
- [ ] I prevented duplicate applications.
- [ ] I implemented employer permissions.
- [ ] I checked object ownership.
- [ ] I created templates.
- [ ] I configured URLs.
- [ ] I displayed messages.
- [ ] I tested the job seeker journey.
- [ ] I tested the employer journey.
- [ ] I ran the full test suite.
- [ ] I documented setup and limitations.
- [ ] I completed Job Portal Web Application.

**Phase 4 outcome:** Django ORM, forms, authentication, sessions, permissions, messages, search, pagination and application integration have now been brought together in one project workflow.

**Next phase:** Day 55 — REST API Development with Django REST Framework.

---

## 122. Official references

1. Django models: https://docs.djangoproject.com/en/5.2/topics/db/models/
2. Django model constraints: https://docs.djangoproject.com/en/5.2/ref/models/constraints/
3. Django forms: https://docs.djangoproject.com/en/5.2/topics/forms/
4. Django authentication: https://docs.djangoproject.com/en/5.2/topics/auth/
5. Django permissions: https://docs.djangoproject.com/en/5.2/topics/auth/default/
6. Django transactions: https://docs.djangoproject.com/en/5.2/topics/db/transactions/
7. Django QuerySets: https://docs.djangoproject.com/en/5.2/topics/db/queries/
8. Django testing: https://docs.djangoproject.com/en/5.2/topics/testing/

**Version reminder:** This lesson targets Django 5.2.19. The code is a training reference that must be executed against the actual repository state. Do not claim runtime validation until the project has been run and the complete test suite has passed.
