# Day 73: Payment Gateway Integration Concepts and Secure Payment Workflows

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–74 — Django, ORM, APIs, security and external integrations  
**Tools:** Python, Django, VS Code, terminal and local development services  
**Approved mini-project:** Payment Workflow Simulator

> **Trainer guidance:** Make the learner distinguish a synchronous HTTP request from work executed later by a worker. For payment workflows, use simulation data only; do not process real card details in a classroom project.

## 1. Learning objectives

- Explain payment gateway integration concepts and secure payment workflows.
- Identify the service, task, broker or worker responsibilities.
- Implement the example step by step.
- Explain failure, retry and duplicate-processing risks.
- Complete Payment Workflow Simulator.

## 2. Concept introduction

A payment integration delegates card or bank handling to a payment provider. A backend should create a payment session or intent, redirect or return the client to the provider, verify signed webhooks and update order state idempotently. Never store raw card numbers or CVV in your Django database. This lesson is a safe workflow simulation, not a real payment integration.

## 3. File-by-file implementation

### payments/models.py

```python
from django.db import models

class PaymentRecord(models.Model):
    order_reference = models.CharField(max_length=50, unique=True)
    provider_reference = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, default="PENDING")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="INR")
    created_at = models.DateTimeField(auto_now_add=True)
```

### payments/services.py

```python
def create_payment_request(order):
    # Simulation only: a real integration calls a provider SDK/API.
    return {
        "order_reference": order.reference,
        "amount": str(order.total),
        "currency": "INR",
        "status": "PENDING",
    }

def apply_verified_payment_event(payment, event_id, provider_status):
    # Production code should store event_id with a unique constraint
    # and verify provider signature before calling this function.
    if payment.status == "PAID":
        return payment

    if provider_status == "success":
        payment.status = "PAID"
        payment.save(update_fields=["status"])
    return payment
```

## 4. Explain the important statements

### payments/models.py

1. `from django.db import models` — Imports Django, Celery or local service functionality.
2. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
3. `class PaymentRecord(models.Model):` — Defines a database model.
4. `    order_reference = models.CharField(max_length=50, unique=True)` — Part of the workflow; explain how it connects the request, queue and worker.
5. `    provider_reference = models.CharField(max_length=100, blank=True)` — Part of the workflow; explain how it connects the request, queue and worker.
6. `    status = models.CharField(max_length=20, default="PENDING")` — Part of the workflow; explain how it connects the request, queue and worker.
7. `    amount = models.DecimalField(max_digits=10, decimal_places=2)` — Part of the workflow; explain how it connects the request, queue and worker.
8. `    currency = models.CharField(max_length=3, default="INR")` — Part of the workflow; explain how it connects the request, queue and worker.
9. `    created_at = models.DateTimeField(auto_now_add=True)` — Part of the workflow; explain how it connects the request, queue and worker.

### payments/services.py

1. `def create_payment_request(order):` — Defines a reusable service or task function.
2. `    # Simulation only: a real integration calls a provider SDK/API.` — Part of the workflow; explain how it connects the request, queue and worker.
3. `    return {` — Part of the workflow; explain how it connects the request, queue and worker.
4. `        "order_reference": order.reference,` — Part of the workflow; explain how it connects the request, queue and worker.
5. `        "amount": str(order.total),` — Part of the workflow; explain how it connects the request, queue and worker.
6. `        "currency": "INR",` — Part of the workflow; explain how it connects the request, queue and worker.
7. `        "status": "PENDING",` — Part of the workflow; explain how it connects the request, queue and worker.
8. `    }` — Part of the workflow; explain how it connects the request, queue and worker.
9. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
10. `def apply_verified_payment_event(payment, event_id, provider_status):` — Defines a reusable service or task function.
11. `    # Production code should store event_id with a unique constraint` — Part of the workflow; explain how it connects the request, queue and worker.
12. `    # and verify provider signature before calling this function.` — Part of the workflow; explain how it connects the request, queue and worker.
13. `    if payment.status == "PAID":` — Part of the workflow; explain how it connects the request, queue and worker.
14. `        return payment` — Part of the workflow; explain how it connects the request, queue and worker.
15. ` ` — Part of the workflow; explain how it connects the request, queue and worker.
16. `    if provider_status == "success":` — Part of the workflow; explain how it connects the request, queue and worker.
17. `        payment.status = "PAID"` — Part of the workflow; explain how it connects the request, queue and worker.
18. `        payment.save(update_fields=["status"])` — Part of the workflow; explain how it connects the request, queue and worker.
19. `    return payment` — Part of the workflow; explain how it connects the request, queue and worker.

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

A payment integration delegates card or bank handling to a payment provider. A backend should create a payment session or intent, redirect or return the client to the provider, verify signed webhooks and update order state idempotently. Never store raw card numbers or CVV in your Django database. This lesson is a safe workflow simulation, not a real payment integration.

## 9. Approved mini-project — Payment Workflow Simulator

**Objective:** Payment Workflow Simulator.

### Required tasks

1. Explain the roles of merchant backend, payment provider and customer browser.
2. Create a PaymentRecord model for a safe simulation.
3. Create a payment request with order reference, amount and currency.
4. Keep raw card details outside the application.
5. Explain provider-hosted checkout or tokenized payment fields.
6. Explain webhook signature verification.
7. Design idempotent event processing using a unique provider event ID.
8. Test pending, success, failure and duplicate event cases.
9. Document that the exercise does not charge real money.

### Suggested structure

```text
projects/day_73/
├── README.md
├── config/
│   ├── celery.py
│   └── settings.py
└── notifications/
    └── tasks.py
```

### Validation checklist

- [ ] Payment state begins as PENDING.
- [ ] Raw card number and CVV are not stored.
- [ ] Only verified provider events can mark a payment successful.
- [ ] Duplicate webhook events do not double-process payment.
- [ ] Payment amount and order reference are validated.
- [ ] The learner clearly labels the project as a simulation.

### Submission evidence

- Source files and configuration names.
- Terminal output from broker and worker.
- Task ID and result/status evidence.
- README with startup and stop commands.
- Test cases for success, failure and duplicate behavior.
- No real payment data, passwords or secret keys.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Payment Workflow Simulator. Identify the service, task, broker, worker, status tracking and failure cases. Do not create a real payment or email integration."

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

**Q1. Explain payment gateway integration concepts and secure payment workflows.**  
**Answer:** A payment integration delegates card or bank handling to a payment provider. A backend should create a payment session or intent, redirect or return the client to the provider, verify signed webhooks and update order state idempotently. Never store raw card numbers or CVV in your Django database. This lesson is a safe workflow simulation, not a real payment integration.

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
- [ ] Complete Payment Workflow Simulator.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 74.
