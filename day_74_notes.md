# Day 74: Background Tasks and Asynchronous Processing Concepts

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–74 — Django, ORM, APIs, security and external integrations  
**Tools:** Python, Django, VS Code, terminal and local development services  
**Approved mini-project:** Background Report Generator

> **Trainer guidance:** Make the learner distinguish a synchronous HTTP request from work executed later by a worker. For payment workflows, use simulation data only; do not process real card details in a classroom project.

## 1. Learning objectives

- Explain background tasks and asynchronous processing concepts.
- Identify the service, task, broker or worker responsibilities.
- Implement the example step by step.
- Explain failure, retry and duplicate-processing risks.
- Complete Background Report Generator.

## 2. Concept introduction

Some backend work takes longer than a normal HTTP request should wait for, such as report generation, bulk email and file processing. A background task is placed on a queue and processed by a worker separately from the web request. The web request can return a job identifier or acknowledgement while the worker continues.

## 3. File-by-file implementation

### reports/services.py

```python
def build_sales_report(start_date, end_date):
    # Placeholder for a slow report-generation operation.
    # Keep the actual business logic in a reusable service.
    rows = load_sales_rows(start_date, end_date)
    return summarize_sales(rows)

def request_report(user, start_date, end_date):
    # In a queue-backed system, enqueue a task and return its ID.
    # The Day 75 lesson implements this with Celery.
    return {
        "status": "QUEUED",
        "requested_by": user.id,
    }
```

### Conceptual request flow

```python
HTTP request
   ↓
Validate request and create job record
   ↓
Enqueue task message
   ↓
Return accepted response / job ID
   ↓
Worker executes report generation
   ↓
Store result and task status
   ↓
Client checks job status or receives notification
```

## 4. Explain the important statements

### reports/services.py

1. `def build_sales_report(start_date, end_date):` — Defines a reusable service or task function.
2. `    # Placeholder for a slow report-generation operation.` — Part of the workflow; explain how it connects the request, queue and worker.
3. `    # Keep the actual business logic in a reusable service.` — Part of the workflow; explain how it connects the request, queue and worker.
4. `    rows = load_sales_rows(start_date, end_date)` — Part of the workflow; explain how it connects the request, queue and worker.
5. `    return summarize_sales(rows)` — Part of the workflow; explain how it connects the request, queue and worker.
6. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
7. `def request_report(user, start_date, end_date):` — Defines a reusable service or task function.
8. `    # In a queue-backed system, enqueue a task and return its ID.` — Part of the workflow; explain how it connects the request, queue and worker.
9. `    # The Day 75 lesson implements this with Celery.` — Part of the workflow; explain how it connects the request, queue and worker.
10. `    return {` — Part of the workflow; explain how it connects the request, queue and worker.
11. `        "status": "QUEUED",` — Part of the workflow; explain how it connects the request, queue and worker.
12. `        "requested_by": user.id,` — Part of the workflow; explain how it connects the request, queue and worker.
13. `    }` — Part of the workflow; explain how it connects the request, queue and worker.

### Conceptual request flow

1. `HTTP request` — Part of the workflow; explain how it connects the request, queue and worker.
2. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
3. `Validate request and create job record` — Part of the workflow; explain how it connects the request, queue and worker.
4. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
5. `Enqueue task message` — Part of the workflow; explain how it connects the request, queue and worker.
6. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
7. `Return accepted response / job ID` — Part of the workflow; explain how it connects the request, queue and worker.
8. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
9. `Worker executes report generation` — Part of the workflow; explain how it connects the request, queue and worker.
10. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
11. `Store result and task status` — Part of the workflow; explain how it connects the request, queue and worker.
12. `   ↓` — Part of the workflow; explain how it connects the request, queue and worker.
13. `Client checks job status or receives notification` — Part of the workflow; explain how it connects the request, queue and worker.

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

Some backend work takes longer than a normal HTTP request should wait for, such as report generation, bulk email and file processing. A background task is placed on a queue and processed by a worker separately from the web request. The web request can return a job identifier or acknowledgement while the worker continues.

## 9. Approved mini-project — Background Report Generator

**Objective:** Background Report Generator.

### Required tasks

1. Identify a task that should not block a normal web request.
2. Separate the business logic into a reusable service function.
3. Create a job/status record for long-running work.
4. Explain the role of a message broker and worker.
5. Return an acknowledgement or job identifier to the client.
6. Track queued, running, succeeded and failed states.
7. Design retry and duplicate-processing behavior.
8. Explain why the next lesson uses Celery and Redis.

### Suggested structure

```text
projects/day_74/
├── README.md
├── config/
│   ├── celery.py
│   └── settings.py
└── notifications/
    └── tasks.py
```

### Validation checklist

- [ ] Slow work is separated from the request handler.
- [ ] The request can return without waiting for the whole report.
- [ ] Task status can be tracked.
- [ ] Failures and retries are considered.
- [ ] Business logic is reusable outside the queue integration.

### Submission evidence

- Source files and configuration names.
- Terminal output from broker and worker.
- Task ID and result/status evidence.
- README with startup and stop commands.
- Test cases for success, failure and duplicate behavior.
- No real payment data, passwords or secret keys.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Background Report Generator. Identify the service, task, broker, worker, status tracking and failure cases. Do not create a real payment or email integration."

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

**Q1. Explain background tasks and asynchronous processing concepts.**  
**Answer:** Some backend work takes longer than a normal HTTP request should wait for, such as report generation, bulk email and file processing. A background task is placed on a queue and processed by a worker separately from the web request. The web request can return a job identifier or acknowledgement while the worker continues.

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
- [ ] Complete Background Report Generator.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 75.
