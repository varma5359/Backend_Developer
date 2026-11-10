# Day 70: File Uploads, Media Files and Image Handling in Django

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–69 — Django, ORM, forms, authentication and REST APIs  
**Tools:** Python, Django, VS Code, terminal and local test data  
**Approved mini-project:** Document Upload Management System

> **Trainer guidance:** Treat external files, email addresses and API responses as untrusted input. Use local test data and fake credentials. Explain configuration and failure handling before connecting a real external service.

## 1. Learning objectives

- Explain file uploads, media files and image handling in django.
- Identify the Django files, settings and libraries involved.
- Implement the example step by step.
- Handle invalid input and external failures.
- Explain the security and reliability considerations.
- Complete Document Upload Management System.

## 2. Concept introduction

Uploaded files are untrusted input. Django receives file data through request.FILES when a multipart/form-data request is used. FileField and ImageField store file references, while the file bytes are stored using the configured storage backend. Validate size and content, use safe filenames and restrict access to private documents.

## 3. File-by-file implementation

### profiles/models.py

```python
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

### profiles/forms.py

```python
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title", "file"]

    def clean_file(self):
        uploaded = self.cleaned_data["file"]
        if uploaded.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File must be 5 MB or smaller.")
        return uploaded
```

### config/settings.py

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### profiles/views.py

```python
from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_document")
    else:
        form = DocumentForm()

    return render(request, "profiles/upload.html", {"form": form})
```

### profiles/templates/profiles/upload.html

```python
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

## 4. Explain the important statements

### profiles/models.py

1. `from django.db import models` — Imports Django, Python or external library functionality.
2. ` ` — Part of the example; explain how it supports the complete workflow.
3. `class Document(models.Model):` — Defines a model or form class.
4. `    title = models.CharField(max_length=120)` — Part of the example; explain how it supports the complete workflow.
5. `    file = models.FileField(upload_to="documents/")` — Part of the example; explain how it supports the complete workflow.
6. `    uploaded_at = models.DateTimeField(auto_now_add=True)` — Part of the example; explain how it supports the complete workflow.

### profiles/forms.py

1. `from django import forms` — Imports Django, Python or external library functionality.
2. `from .models import Document` — Imports Django, Python or external library functionality.
3. ` ` — Part of the example; explain how it supports the complete workflow.
4. `class DocumentForm(forms.ModelForm):` — Defines a model or form class.
5. `    class Meta:` — Defines a model or form class.
6. `        model = Document` — Part of the example; explain how it supports the complete workflow.
7. `        fields = ["title", "file"]` — Part of the example; explain how it supports the complete workflow.
8. ` ` — Part of the example; explain how it supports the complete workflow.
9. `    def clean_file(self):` — Defines a reusable service or view function.
10. `        uploaded = self.cleaned_data["file"]` — Part of the example; explain how it supports the complete workflow.
11. `        if uploaded.size > 5 * 1024 * 1024:` — Part of the example; explain how it supports the complete workflow.
12. `            raise forms.ValidationError("File must be 5 MB or smaller.")` — Part of the example; explain how it supports the complete workflow.
13. `        return uploaded` — Part of the example; explain how it supports the complete workflow.

### config/settings.py

1. `MEDIA_URL = "/media/"` — Part of the example; explain how it supports the complete workflow.
2. `MEDIA_ROOT = BASE_DIR / "media"` — Defines the local media storage directory.

### profiles/views.py

1. `from django.shortcuts import render, redirect` — Imports Django, Python or external library functionality.
2. `from .forms import DocumentForm` — Imports Django, Python or external library functionality.
3. ` ` — Part of the example; explain how it supports the complete workflow.
4. `def upload_document(request):` — Defines a reusable service or view function.
5. `    if request.method == "POST":` — Part of the example; explain how it supports the complete workflow.
6. `        form = DocumentForm(request.POST, request.FILES)` — Reads uploaded file content from the multipart request.
7. `        if form.is_valid():` — Part of the example; explain how it supports the complete workflow.
8. `            form.save()` — Part of the example; explain how it supports the complete workflow.
9. `            return redirect("upload_document")` — Part of the example; explain how it supports the complete workflow.
10. `    else:` — Part of the example; explain how it supports the complete workflow.
11. `        form = DocumentForm()` — Part of the example; explain how it supports the complete workflow.
12. ` ` — Part of the example; explain how it supports the complete workflow.
13. `    return render(request, "profiles/upload.html", {"form": form})` — Part of the example; explain how it supports the complete workflow.

### profiles/templates/profiles/upload.html

1. `<form method="post" enctype="multipart/form-data">` — Part of the example; explain how it supports the complete workflow.
2. `    {% csrf_token %}` — Part of the example; explain how it supports the complete workflow.
3. `    {{ form.as_p }}` — Part of the example; explain how it supports the complete workflow.
4. `    <button type="submit">Upload</button>` — Part of the example; explain how it supports the complete workflow.
5. `</form>` — Part of the example; explain how it supports the complete workflow.

## 5. Reliability and security checklist

- Validate file size and allowed content types.
- Do not trust file extensions alone.
- Use generated or sanitized filenames.
- Restrict access to private uploads.
- Configure email and API credentials outside source control.
- Set timeouts for external HTTP requests.
- Handle network and service errors.
- Avoid logging passwords, tokens, private file contents or unnecessary personal data.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Uploaded file is empty | Form enctype and request.FILES |
| File path not saved | MEDIA_ROOT, storage backend and model field |
| Email not visible | EMAIL_BACKEND and console output |
| Email provider rejects message | Sender/recipient configuration and provider response |
| External API times out | Timeout setting and service availability |
| 401 from external API | Credential configuration and API permissions |
| JSON key missing | Response schema and defensive validation |
| External service returns 5xx | Retry policy, fallback and user-facing error |

## 7. Industry scenario

Uploaded files are untrusted input. Django receives file data through request.FILES when a multipart/form-data request is used. FileField and ImageField store file references, while the file bytes are stored using the configured storage backend. Validate size and content, use safe filenames and restrict access to private documents.

## 8. Approved mini-project — Document Upload Management System

**Objective:** Document Upload Management System.

### Required tasks

1. Create a Document model with FileField.
2. Configure MEDIA_ROOT and MEDIA_URL for local development.
3. Create a ModelForm and validate file size.
4. Pass request.POST and request.FILES to the form.
5. Set enctype=multipart/form-data in the HTML form.
6. Run makemigrations and migrate.
7. Upload a small test document.
8. Verify the saved file path and metadata.
9. Explain why production media storage and access control need additional configuration.

### Suggested structure

```text
projects/day_70/
├── README.md
├── config/
├── services/
└── application/
    ├── models.py
    ├── forms.py
    └── views.py
```

### Validation checklist

- [ ] The form includes multipart/form-data.
- [ ] The view passes request.FILES.
- [ ] File size validation works.
- [ ] Uploaded file is stored under the configured media root.
- [ ] File paths and metadata are saved.
- [ ] Private files are not exposed without authorization.

### Submission evidence

- Source files and configuration examples.
- Test output using local sample data.
- Error-handling evidence.
- README with setup and environment variable names.
- No real credentials, private files or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Document Upload Management System. List components, settings, failure cases, security checks and tests. Do not include real credentials."

**Guided prompt:** "Guide me through one file at a time. Explain the configuration and wait for my test output."

**Debugging prompt:** "Here is my code, sanitized response and error message. Identify the cause without asking for API keys or private data."

**Review prompt:** "Review the workflow for input validation, timeouts, secret handling, error responses and safe storage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Connect a Django backend to files, email or external services safely.  
B. Replace the database.  
C. Disable validation.  
D. Store secrets in Git.  
**Answer: A.** Backend integrations need reliable and secure handling.

**Q2. What should be used for an external HTTP request?**  
A. No timeout.  
B. A reasonable timeout and error handling.  
C. A hardcoded secret.  
D. An infinite retry loop.  
**Answer: B.** Timeouts prevent requests from waiting indefinitely.

**Q3. Where should private API keys be stored?**  
A. Public README.  
B. HTML form.  
C. Protected environment configuration or secret manager.  
D. Git commit message.  
**Answer: C.** Keep secrets outside source control.

**Q4. What should happen when an external service fails?**  
A. Return raw traceback to the user.  
B. Ignore the failure.  
C. Pretend the response is successful.  
D. Handle the error and return a controlled response.  
**Answer: D.** Do not expose internal details.

**Q5. What is the strongest evidence of completion?**  
A. Normal and failure cases are tested and documented.  
B. A project title only.  
C. A copied code snippet.  
D. A screenshot of an editor.  
**Answer: A.** Verify the integration and its failure behavior.

## 11. Interview preparation

**Q1. Explain file uploads, media files and image handling in django.**  
**Answer:** Uploaded files are untrusted input. Django receives file data through request.FILES when a multipart/form-data request is used. FileField and ImageField store file references, while the file bytes are stored using the configured storage backend. Validate size and content, use safe filenames and restrict access to private documents.

**Q2. What is one reliability concern?**  
**Answer:** Explain timeouts, validation, delivery failure, file restrictions or secret handling as appropriate.

**Q3. How do you test the integration?**  
**Answer:** Use mocked responses or local test backends, exercise success and failure cases and verify the resulting database or HTTP response.

**Follow-up:** Why should you not rely only on a live external API test?  
**Answer:** External services can be unavailable or change behavior. Mocked tests make application behavior repeatable.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid cases.
- [ ] Verify error handling.
- [ ] Complete Document Upload Management System.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and safe evidence.

**Next lesson:** Day 71.
