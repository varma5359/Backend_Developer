# Day 54: Complete Django Application Integration and Validation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–53 — Django fundamentals, ORM, forms, users and access control  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Job Portal Web Application

> **Trainer guidance:** Explain the relationship between each file and the user journey. Show the learner how to verify the behavior using separate test accounts and sample records.

## 1. Learning objectives

- Explain complete django application integration and validation.
- Identify the Django components and settings involved.
- Implement the example step by step.
- Test normal, invalid and unauthorized cases.
- Explain one design or security decision.
- Complete Job Portal Web Application.

## 2. Concept introduction

A complete Django application connects user accounts, models, forms, views, templates, URLs, ORM queries, authentication and permissions. Integration testing verifies that these components work together across realistic user journeys, not just as isolated code snippets.

## 3. File-by-file implementation

### jobs/models.py

```python
from django.conf import settings
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["job", "applicant"],
                name="one_application_per_user_per_job"
            )
        ]
```

### jobs/forms.py

```python
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["cover_letter"]
```

### jobs/views.py

```python
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JobApplicationForm
from .models import Job

def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by("title")
    return render(request, "jobs/job_list.html", {"jobs": jobs})

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Application submitted.")
            return redirect("job_list")
    else:
        form = JobApplicationForm()
    return render(request, "jobs/apply.html", {"form": form, "job": job})
```

## 4. Understand the important statements

### jobs/models.py

1. `from django.conf import settings` — Imports Django components or the active user model setting.
2. `from django.db import models` — Imports Django components or the active user model setting.
3. ` ` — Part of the implementation; explain its role in the overall workflow.
4. `class Job(models.Model):` — Defines a model, form or class.
5. `    title = models.CharField(max_length=120)` — Part of the implementation; explain its role in the overall workflow.
6. `    company = models.CharField(max_length=120)` — Part of the implementation; explain its role in the overall workflow.
7. `    description = models.TextField()` — Part of the implementation; explain its role in the overall workflow.
8. `    is_active = models.BooleanField(default=True)` — Part of the implementation; explain its role in the overall workflow.
9. ` ` — Part of the implementation; explain its role in the overall workflow.
10. `class JobApplication(models.Model):` — Defines a model, form or class.
11. `    job = models.ForeignKey(Job, on_delete=models.CASCADE)` — Links a record to another model.
12. `    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)` — Links a record to another model.
13. `    cover_letter = models.TextField()` — Part of the implementation; explain its role in the overall workflow.
14. `    created_at = models.DateTimeField(auto_now_add=True)` — Part of the implementation; explain its role in the overall workflow.
15. ` ` — Part of the implementation; explain its role in the overall workflow.
16. `    class Meta:` — Defines a model, form or class.
17. `        constraints = [` — Part of the implementation; explain its role in the overall workflow.
18. `            models.UniqueConstraint(` — Part of the implementation; explain its role in the overall workflow.
19. `                fields=["job", "applicant"],` — Part of the implementation; explain its role in the overall workflow.
20. `                name="one_application_per_user_per_job"` — Part of the implementation; explain its role in the overall workflow.
21. `            )` — Part of the implementation; explain its role in the overall workflow.
22. `        ]` — Part of the implementation; explain its role in the overall workflow.

### jobs/forms.py

1. `from django import forms` — Imports Django components or the active user model setting.
2. `from .models import JobApplication` — Imports Django components or the active user model setting.
3. ` ` — Part of the implementation; explain its role in the overall workflow.
4. `class JobApplicationForm(forms.ModelForm):` — Defines a model, form or class.
5. `    class Meta:` — Defines a model, form or class.
6. `        model = JobApplication` — Part of the implementation; explain its role in the overall workflow.
7. `        fields = ["cover_letter"]` — Part of the implementation; explain its role in the overall workflow.

### jobs/views.py

1. `from django.contrib import messages` — Imports Django components or the active user model setting.
2. `from django.contrib.auth.decorators import login_required` — Imports Django components or the active user model setting.
3. `from django.shortcuts import get_object_or_404, redirect, render` — Imports Django components or the active user model setting.
4. `from .forms import JobApplicationForm` — Imports Django components or the active user model setting.
5. `from .models import Job` — Imports Django components or the active user model setting.
6. ` ` — Part of the implementation; explain its role in the overall workflow.
7. `def job_list(request):` — Defines a view function.
8. `    jobs = Job.objects.filter(is_active=True).order_by("title")` — Part of the implementation; explain its role in the overall workflow.
9. `    return render(request, "jobs/job_list.html", {"jobs": jobs})` — Part of the implementation; explain its role in the overall workflow.
10. ` ` — Part of the implementation; explain its role in the overall workflow.
11. `@login_required` — Requires an authenticated user.
12. `def apply_for_job(request, pk):` — Defines a view function.
13. `    job = get_object_or_404(Job, pk=pk, is_active=True)` — Part of the implementation; explain its role in the overall workflow.
14. `    if request.method == "POST":` — Part of the implementation; explain its role in the overall workflow.
15. `        form = JobApplicationForm(request.POST)` — Part of the implementation; explain its role in the overall workflow.
16. `        if form.is_valid():` — Part of the implementation; explain its role in the overall workflow.
17. `            application = form.save(commit=False)` — Part of the implementation; explain its role in the overall workflow.
18. `            application.job = job` — Part of the implementation; explain its role in the overall workflow.
19. `            application.applicant = request.user` — Part of the implementation; explain its role in the overall workflow.
20. `            application.save()` — Part of the implementation; explain its role in the overall workflow.
21. `            messages.success(request, "Application submitted.")` — Queues one-time user feedback.
22. `            return redirect("job_list")` — Part of the implementation; explain its role in the overall workflow.
23. `    else:` — Part of the implementation; explain its role in the overall workflow.
24. `        form = JobApplicationForm()` — Part of the implementation; explain its role in the overall workflow.
25. `    return render(request, "jobs/apply.html", {"form": form, "job": job})` — Part of the implementation; explain its role in the overall workflow.

## 5. Integration flow

```text
Browser request
   ↓
URL pattern
   ↓
Authentication / permission check
   ↓
View
   ↓
Form validation
   ↓
ORM and database
   ↓
Messages / redirect / template
   ↓
Browser response
```

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| User model import error | AUTH_USER_MODEL and app registration |
| Duplicate record | Database constraint and user feedback |
| Message not visible | Messages middleware, context processor and template |
| Pagination loses search | Preserve query parameters in page links |
| Search results are inconsistent | Ordering and Q conditions |
| User can perform restricted action | Server-side authorization |
| Form accepts untrusted ownership fields | Set owner/applicant in the view from request.user |

## 7. Industry scenario

A complete Django application connects user accounts, models, forms, views, templates, URLs, ORM queries, authentication and permissions. Integration testing verifies that these components work together across realistic user journeys, not just as isolated code snippets.

## 8. Approved mini-project — Job Portal Web Application

**Objective:** Job Portal Web Application.

### Required tasks

1. Create a jobs app and register it.
2. Create Job and JobApplication models.
3. Add a uniqueness constraint to prevent duplicate applications.
4. Create a ModelForm that exposes only the cover letter field.
5. Create a public job list view.
6. Protect the application view with login_required.
7. Set job and applicant on the server, not from untrusted form fields.
8. Add URL patterns and templates.
9. Run migrations and create sample jobs.
10. Test anonymous, authenticated, duplicate and inactive-job cases.
11. Document the application architecture and known limitations.

### Suggested structure

```text
projects/day_54/
├── manage.py
├── config/
└── jobs/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
```

### Validation checklist

- [ ] Active jobs appear in the job list.
- [ ] Anonymous users cannot apply.
- [ ] Authenticated users can submit an application.
- [ ] Applicant is taken from request.user, not user input.
- [ ] Duplicate applications are rejected by the constraint.
- [ ] Inactive jobs cannot be applied to.
- [ ] Success feedback is shown.
- [ ] The full user journey is tested.

### Test matrix

| User or input | Expected behavior |
|---|---|
| Anonymous visitor | Public pages load; protected action redirects or denies |
| Authenticated user | Allowed action succeeds |
| Invalid form | Errors display; no record is saved |
| Duplicate submission | Constraint prevents duplicate data |
| Missing or inactive record | Not found or denied as appropriate |
| Valid workflow | Database and browser state agree |

### Submission evidence

- Source code and migrations.
- Screenshots of the main user journey.
- Test results for positive and negative cases.
- README with setup and architecture.
- Explanation of authorization and data integrity.
- No real user credentials or personal data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Job Portal Web Application. Identify the models, forms, views, URLs, templates, permissions, migrations and test cases. Do not write the full project."

**Guided prompt:** "Guide me through one component at a time. Explain the file path and wait for my test result."

**Debugging prompt:** "Trace my user journey from URL to view to form to database. Identify where the behavior differs from the requirement."

**Review prompt:** "Review the project for integration correctness, duplicate handling, permissions, validation and test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Integrate multiple Django components into a complete user workflow.  
B. Replace the database.  
C. Remove authentication.  
D. Disable URL routing.  
**Answer: A.** Integration connects the individual components into a working feature.

**Q2. Where should the server get the identity of the logged-in applicant?**  
A. A hidden HTML field.  
B. request.user.  
C. A URL parameter supplied by the browser.  
D. A text box.  
**Answer: B.** Use the authenticated user supplied by Django.

**Q3. Why add a database uniqueness constraint?**  
A. To style a template.  
B. To create a URL.  
C. To enforce a rule even if multiple requests reach the database.  
D. To disable migrations.  
**Answer: C.** Database constraints protect integrity.

**Q4. What should an integration test cover?**  
A. Only one Python import.  
B. Only a screenshot.  
C. Only the model class.  
D. A realistic sequence across views, forms, authentication and database.  
**Answer: D.** Integration tests verify components working together.

**Q5. What is the strongest evidence of completion?**  
A. A tested end-to-end user journey with expected database state.  
B. A project folder only.  
C. A long code file.  
D. A list of planned features.  
**Answer: A.** Completion requires verified behavior.

## 11. Interview preparation

**Q1. Explain complete django application integration and validation.**  
**Answer:** A complete Django application connects user accounts, models, forms, views, templates, URLs, ORM queries, authentication and permissions. Integration testing verifies that these components work together across realistic user journeys, not just as isolated code snippets.

**Q2. What is one important design decision?**  
**Answer:** Explain the relationship, constraint or server-side value assignment used in the implementation.

**Q3. How do you verify the full application?**  
**Answer:** Test the end-to-end user journey with anonymous and authenticated users, valid and invalid inputs and expected database state.

**Follow-up:** Why are integration tests necessary if unit tests pass?  
**Answer:** Unit tests check individual components; integration tests verify that those components work together correctly.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Identify all connected components.
- [ ] Implement the example.
- [ ] Test valid and invalid user journeys.
- [ ] Complete Job Portal Web Application.
- [ ] Verify database state.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Phase 4 complete. Next: Phase 5 — REST API Development with Django REST Framework (Day 55).
