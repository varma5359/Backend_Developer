# Day 71: Email Integration and Sending Application Notifications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–69 — Django, ORM, forms, authentication and REST APIs  
**Tools:** Python, Django, VS Code, terminal and local test data  
**Approved mini-project:** Email Notification Service

> **Trainer guidance:** Treat external files, email addresses and API responses as untrusted input. Use local test data and fake credentials. Explain configuration and failure handling before connecting a real external service.

## 1. Learning objectives

- Explain email integration and sending application notifications.
- Identify the Django files, settings and libraries involved.
- Implement the example step by step.
- Handle invalid input and external failures.
- Explain the security and reliability considerations.
- Complete Email Notification Service.

## 2. Concept introduction

Backend applications send emails for account events, status updates and workflow notifications. Django provides send_mail() and EmailMessage. Email configuration should be externalized and environment-specific. In development, the console email backend can display messages in the terminal without sending real email.

## 3. File-by-file implementation

### config/settings.py — local development

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@example.test"
```

### profiles/email_service.py

```python
from django.conf import settings
from django.core.mail import send_mail

def send_welcome_email(user_email, user_name):
    subject = "Welcome to the employee portal"
    message = f"Hello {user_name}, your account is ready."

    return send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
```

### Call from a view or service

```python
from django.contrib import messages
from django.shortcuts import redirect
from .email_service import send_welcome_email

def notify_user(request):
    send_welcome_email("test@example.test", "Asha")
    messages.success(request, "Notification email prepared.")
    return redirect("employee_list")
```

## 4. Explain the important statements

### config/settings.py — local development

1. `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"` — Part of the example; explain how it supports the complete workflow.
2. `DEFAULT_FROM_EMAIL = "noreply@example.test"` — Part of the example; explain how it supports the complete workflow.

### profiles/email_service.py

1. `from django.conf import settings` — Imports Django, Python or external library functionality.
2. `from django.core.mail import send_mail` — Imports Django, Python or external library functionality.
3. ` ` — Part of the example; explain how it supports the complete workflow.
4. `def send_welcome_email(user_email, user_name):` — Defines a reusable service or view function.
5. `    subject = "Welcome to the employee portal"` — Part of the example; explain how it supports the complete workflow.
6. `    message = f"Hello {user_name}, your account is ready."` — Part of the example; explain how it supports the complete workflow.
7. ` ` — Part of the example; explain how it supports the complete workflow.
8. `    return send_mail(` — Sends an email through Django's configured backend.
9. `        subject,` — Part of the example; explain how it supports the complete workflow.
10. `        message,` — Part of the example; explain how it supports the complete workflow.
11. `        settings.DEFAULT_FROM_EMAIL,` — Part of the example; explain how it supports the complete workflow.
12. `        [user_email],` — Part of the example; explain how it supports the complete workflow.
13. `        fail_silently=False,` — Part of the example; explain how it supports the complete workflow.
14. `    )` — Part of the example; explain how it supports the complete workflow.

### Call from a view or service

1. `from django.contrib import messages` — Imports Django, Python or external library functionality.
2. `from django.shortcuts import redirect` — Imports Django, Python or external library functionality.
3. `from .email_service import send_welcome_email` — Imports Django, Python or external library functionality.
4. ` ` — Part of the example; explain how it supports the complete workflow.
5. `def notify_user(request):` — Defines a reusable service or view function.
6. `    send_welcome_email("test@example.test", "Asha")` — Part of the example; explain how it supports the complete workflow.
7. `    messages.success(request, "Notification email prepared.")` — Part of the example; explain how it supports the complete workflow.
8. `    return redirect("employee_list")` — Part of the example; explain how it supports the complete workflow.

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

Backend applications send emails for account events, status updates and workflow notifications. Django provides send_mail() and EmailMessage. Email configuration should be externalized and environment-specific. In development, the console email backend can display messages in the terminal without sending real email.

## 8. Approved mini-project — Email Notification Service

**Objective:** Email Notification Service.

### Required tasks

1. Explain email use cases in backend systems.
2. Configure the console email backend for local development.
3. Create a service function that calls send_mail().
4. Use DEFAULT_FROM_EMAIL from settings.
5. Call the service from an appropriate business workflow.
6. Inspect the email output in the terminal.
7. Configure a real provider only through protected environment settings.
8. Handle delivery failures and avoid logging sensitive content.

### Suggested structure

```text
projects/day_71/
├── README.md
├── config/
├── services/
└── application/
    ├── models.py
    ├── forms.py
    └── views.py
```

### Validation checklist

- [ ] Local console backend prints the message.
- [ ] Recipient and sender are passed correctly.
- [ ] Email service is separated from unrelated view logic.
- [ ] Failure behavior is understood.
- [ ] No real email credentials are committed.

### Submission evidence

- Source files and configuration examples.
- Test output using local sample data.
- Error-handling evidence.
- README with setup and environment variable names.
- No real credentials, private files or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Email Notification Service. List components, settings, failure cases, security checks and tests. Do not include real credentials."

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

**Q1. Explain email integration and sending application notifications.**  
**Answer:** Backend applications send emails for account events, status updates and workflow notifications. Django provides send_mail() and EmailMessage. Email configuration should be externalized and environment-specific. In development, the console email backend can display messages in the terminal without sending real email.

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
- [ ] Complete Email Notification Service.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and safe evidence.

**Next lesson:** Day 72.
