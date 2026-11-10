# Day 75: Celery and Redis Fundamentals for Background Jobs

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–74 — Django, ORM, APIs, security and external integrations  
**Tools:** Python, Django, VS Code, terminal and local development services  
**Approved mini-project:** Asynchronous Email Task System

> **Trainer guidance:** Make the learner distinguish a synchronous HTTP request from work executed later by a worker. For payment workflows, use simulation data only; do not process real card details in a classroom project.

## 1. Learning objectives

- Explain celery and redis fundamentals for background jobs.
- Identify the service, task, broker or worker responsibilities.
- Implement the example step by step.
- Explain failure, retry and duplicate-processing risks.
- Complete Asynchronous Email Task System.

## 2. Concept introduction

Celery is a distributed task queue for executing work outside the web request process. Redis can act as a message broker and, optionally, a result backend. A Django application enqueues a task; a Celery worker consumes and executes it. Tasks should be idempotent where possible and should not assume a message is delivered exactly once.

## 3. File-by-file implementation

### config/celery.py

```python
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

### config/__init__.py

```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```

### config/settings.py

```python
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
```

### profiles/tasks.py

```python
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(email, subject, message):
    return send_mail(
        subject,
        message,
        "noreply@example.test",
        [email],
        fail_silently=False,
    )
```

### Call the task

```python
from profiles.tasks import send_notification_email

task_result = send_notification_email.delay(
    "test@example.test",
    "Welcome",
    "Your account is ready."
)
print(task_result.id)
```

## 4. Explain the important statements

### config/celery.py

1. `import os` — Part of the workflow; explain how it connects the request, queue and worker.
2. `from celery import Celery` — Imports Django, Celery or local service functionality.
3. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
4. `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")` — Part of the workflow; explain how it connects the request, queue and worker.
5. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
6. `app = Celery("config")` — Creates the Celery application instance.
7. `app.config_from_object("django.conf:settings", namespace="CELERY")` — Part of the workflow; explain how it connects the request, queue and worker.
8. `app.autodiscover_tasks()` — Asks Celery to discover task modules in installed Django apps.

### config/__init__.py

1. `from .celery import app as celery_app` — Imports Django, Celery or local service functionality.
2. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
3. `__all__ = ("celery_app",)` — Part of the workflow; explain how it connects the request, queue and worker.

### config/settings.py

1. `CELERY_BROKER_URL = "redis://localhost:6379/0"` — Configures the message broker address.
2. `CELERY_RESULT_BACKEND = "redis://localhost:6379/1"` — Part of the workflow; explain how it connects the request, queue and worker.

### profiles/tasks.py

1. `from celery import shared_task` — Imports Django, Celery or local service functionality.
2. `from django.core.mail import send_mail` — Imports Django, Celery or local service functionality.
3. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
4. `@shared_task` — Registers the function as a Celery task.
5. `def send_notification_email(email, subject, message):` — Defines a reusable service or task function.
6. `    return send_mail(` — Part of the workflow; explain how it connects the request, queue and worker.
7. `        subject,` — Part of the workflow; explain how it connects the request, queue and worker.
8. `        message,` — Part of the workflow; explain how it connects the request, queue and worker.
9. `        "noreply@example.test",` — Part of the workflow; explain how it connects the request, queue and worker.
10. `        [email],` — Part of the workflow; explain how it connects the request, queue and worker.
11. `        fail_silently=False,` — Part of the workflow; explain how it connects the request, queue and worker.
12. `    )` — Part of the workflow; explain how it connects the request, queue and worker.

### Call the task

1. `from profiles.tasks import send_notification_email` — Imports Django, Celery or local service functionality.
2. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
3. `task_result = send_notification_email.delay(` — Enqueues the task for asynchronous execution.
4. `    "test@example.test",` — Part of the workflow; explain how it connects the request, queue and worker.
5. `    "Welcome",` — Part of the workflow; explain how it connects the request, queue and worker.
6. `    "Your account is ready."` — Part of the workflow; explain how it connects the request, queue and worker.
7. `)` — Part of the workflow; explain how it connects the request, queue and worker.
8. `print(task_result.id)` — Part of the workflow; explain how it connects the request, queue and worker.

## 5. Background task flow

```text
Django view / service
      ↓ enqueue task
Message broker (Redis)
      ↓ worker receives task
Celery worker
      ↓ executes function
Result / status / notification
```

The broker stores task messages. The worker executes the Python function. A result backend can store task results, but not every application needs to store full results.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Redis connection refused | Redis service and broker URL |
| Task not discovered | tasks.py location and autodiscover_tasks() |
| delay() fails | Celery app import and broker connectivity |
| Task remains queued | Worker process and queue routing |
| Task runs twice | Idempotency and duplicate event handling |
| Task fails silently | Worker logs, task result and exception |
| Sensitive task data appears in logs | Task arguments and logging configuration |

## 7. Reliability and security

- Make tasks idempotent where practical.
- Avoid passing passwords or tokens in task arguments.
- Keep task payloads small.
- Define retry behavior carefully.
- Monitor failed and long-running tasks.
- Understand that task delivery and execution can be repeated.
- Protect Redis in production with network restrictions and authentication.
- Do not use a local classroom configuration as production security.

## 8. Industry scenario

Celery is a distributed task queue for executing work outside the web request process. Redis can act as a message broker and, optionally, a result backend. A Django application enqueues a task; a Celery worker consumes and executes it. Tasks should be idempotent where possible and should not assume a message is delivered exactly once.

## 9. Approved mini-project — Asynchronous Email Task System

**Objective:** Asynchronous Email Task System.

### Required tasks

1. Install Celery and the Redis Python client in the environment.
2. Start a local Redis service for development.
3. Create config/celery.py and configure the Celery app.
4. Expose the Celery app from config/__init__.py.
5. Configure the broker URL and optional result backend.
6. Create a task using @shared_task.
7. Call the task using delay() from a view or service.
8. Start a Celery worker in a separate terminal.
9. Inspect task execution and failure behavior.
10. Keep broker credentials in environment configuration for real deployments.

### Suggested structure

```text
projects/day_75/
├── README.md
├── config/
│   ├── celery.py
│   └── settings.py
└── notifications/
    └── tasks.py
```

### Validation checklist

- [ ] Celery app imports with Django settings.
- [ ] Redis broker is reachable.
- [ ] Worker starts and discovers the task.
- [ ] delay() enqueues a task and returns an ID.
- [ ] Worker executes the task.
- [ ] Task failure is visible and retry strategy is considered.
- [ ] Task is safe against duplicate execution where practical.

### Submission evidence

- Source files and configuration names.
- Terminal output from broker and worker.
- Task ID and result/status evidence.
- README with startup and stop commands.
- Test cases for success, failure and duplicate behavior.
- No real payment data, passwords or secret keys.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Asynchronous Email Task System. Identify the service, task, broker, worker, status tracking and failure cases. Do not create a real payment or email integration."

**Guided prompt:** "Guide me through Celery setup one file at a time. Explain which terminal runs Redis, which runs the Django server and which runs the worker."

**Debugging prompt:** "Here are sanitized worker logs and task status. Identify whether the failure is in broker connection, task discovery or task execution."

**Review prompt:** "Review the task for idempotency, retries, sensitive arguments and failure monitoring."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Execute slow work outside the normal request-response cycle or model a secure workflow.  
B. Replace Django models.  
C. Disable error handling.  
D. Store payment card data in plaintext.  
**Answer: A.** The design separates slow work or safely models provider workflows.

**Q2. What does a message broker do?**  
A. Renders HTML.  
B. Stores and delivers task messages to workers.  
C. Creates database migrations.  
D. Replaces authentication.  
**Answer: B.** The broker transports task messages.

**Q3. What does Celery worker do?**  
A. Edits templates.  
B. Runs SQL migrations only.  
C. Executes queued tasks.  
D. Replaces Redis.  
**Answer: C.** Workers consume tasks and execute their functions.

**Q4. Why should tasks be idempotent?**  
A. To make them longer.  
B. To disable retries.  
C. To remove task IDs.  
D. To make repeated execution safe where possible.  
**Answer: D.** Tasks may be delivered or executed more than once.

**Q5. Should a classroom payment simulator store raw card details?**  
A. No. Use a provider-hosted or tokenized flow in real integrations.  
B. Yes, in a text field.  
C. Yes, in Git.  
D. Only in logs.  
**Answer: A.** Never store raw card data in this learning project.

## 12. Interview preparation

**Q1. Explain celery and redis fundamentals for background jobs.**  
**Answer:** Celery is a distributed task queue for executing work outside the web request process. Redis can act as a message broker and, optionally, a result backend. A Django application enqueues a task; a Celery worker consumes and executes it. Tasks should be idempotent where possible and should not assume a message is delivered exactly once.

**Q2. What is one failure scenario?**  
**Answer:** Explain broker unavailability, worker failure, duplicate event processing or payment state inconsistency as appropriate.

**Q3. How do you verify the workflow?**  
**Answer:** Inspect task IDs, worker logs, resulting database state and failure handling. For payment simulation, verify state transitions and duplicate event behavior.

**Follow-up:** Why is a task queue not a guarantee that a task runs exactly once?  
**Answer:** Messages can be retried or redelivered, so task logic should be safe against repeated execution.

## 13. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Verify the broker/worker or payment state flow.
- [ ] Test success and failure.
- [ ] Complete Asynchronous Email Task System.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 76.
