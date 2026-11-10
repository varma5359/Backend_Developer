# Day 77: Database Transactions and Atomic Operations

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–77 — Django, ORM, APIs, background tasks and deployment concepts  
**Tools:** Python, Django, database, VS Code and terminal  
**Approved mini-project:** Bank Transfer Transaction Simulator

> **Trainer guidance:** Explain what problem the feature solves and when it should be used. Measure behavior where relevant. Avoid adding caching, locking or middleware without a clear requirement.

## 1. Learning objectives

- Explain database transactions and atomic operations.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Explain the reliability or performance implications.
- Test normal and failure cases.
- Complete Bank Transfer Transaction Simulator.

## 2. Concept introduction

A database transaction groups related database operations so they succeed or fail together. Django transaction.atomic() creates an atomic block. For concurrent updates, row locking or database-side expressions may be needed. Financial-style workflows must protect against partial transfers and concurrent requests.

## 3. File-by-file implementation

### banking/services.py

```python
from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Account

@transaction.atomic
def transfer_funds(source_id, destination_id, amount):
    amount = Decimal(amount)
    if amount <= 0:
        raise ValidationError("Transfer amount must be positive")

    source = Account.objects.select_for_update().get(pk=source_id)
    destination = Account.objects.select_for_update().get(pk=destination_id)

    if source.balance < amount:
        raise ValidationError("Insufficient funds")

    source.balance -= amount
    destination.balance += amount

    source.save(update_fields=["balance"])
    destination.save(update_fields=["balance"])
```

### Transaction behavior

```python
from django.db import transaction

with transaction.atomic():
    # All database writes inside this block commit together.
    # An exception causes the transaction to roll back.
    create_transfer_record()
    update_account_balances()
```

## 4. Explain the important statements

### banking/services.py

1. `from decimal import Decimal` — Imports Django or Python components.
2. `from django.db import transaction` — Imports Django or Python components.
3. `from django.core.exceptions import ValidationError` — Imports Django or Python components.
4. `from .models import Account` — Imports Django or Python components.
5. ` ` — Part of the configuration; explain how it affects the request or database.
6. `@transaction.atomic` — Runs the function inside a database transaction.
7. `def transfer_funds(source_id, destination_id, amount):` — Defines a service function or middleware method.
8. `    amount = Decimal(amount)` — Part of the configuration; explain how it affects the request or database.
9. `    if amount <= 0:` — Part of the configuration; explain how it affects the request or database.
10. `        raise ValidationError("Transfer amount must be positive")` — Part of the configuration; explain how it affects the request or database.
11. ` ` — Part of the configuration; explain how it affects the request or database.
12. `    source = Account.objects.select_for_update().get(pk=source_id)` — Requests row locks inside a transaction on supported databases.
13. `    destination = Account.objects.select_for_update().get(pk=destination_id)` — Requests row locks inside a transaction on supported databases.
14. ` ` — Part of the configuration; explain how it affects the request or database.
15. `    if source.balance < amount:` — Part of the configuration; explain how it affects the request or database.
16. `        raise ValidationError("Insufficient funds")` — Part of the configuration; explain how it affects the request or database.
17. ` ` — Part of the configuration; explain how it affects the request or database.
18. `    source.balance -= amount` — Part of the configuration; explain how it affects the request or database.
19. `    destination.balance += amount` — Part of the configuration; explain how it affects the request or database.
20. ` ` — Part of the configuration; explain how it affects the request or database.
21. `    source.save(update_fields=["balance"])` — Part of the configuration; explain how it affects the request or database.
22. `    destination.save(update_fields=["balance"])` — Part of the configuration; explain how it affects the request or database.

### Transaction behavior

1. `from django.db import transaction` — Imports Django or Python components.
2. ` ` — Part of the configuration; explain how it affects the request or database.
3. `with transaction.atomic():` — Part of the configuration; explain how it affects the request or database.
4. `    # All database writes inside this block commit together.` — Part of the configuration; explain how it affects the request or database.
5. `    # An exception causes the transaction to roll back.` — Part of the configuration; explain how it affects the request or database.
6. `    create_transfer_record()` — Part of the configuration; explain how it affects the request or database.
7. `    update_account_balances()` — Part of the configuration; explain how it affects the request or database.

## 5. Important design considerations

| Concept | Consideration |
|---|---|
| Cache key | Include the data context and avoid collisions |
| Cache timeout | Decide how long stale data may be acceptable |
| Cache invalidation | Clear or refresh cached values after writes |
| Atomic transaction | Group related writes into one commit/rollback unit |
| Row locking | Use when concurrent writes require coordination |
| Middleware order | Earlier middleware wraps later middleware |
| Logging | Record safe metadata, not secrets or request bodies |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Cache remains stale | Cache invalidation and key design |
| Cache never hits | Key mismatch or backend configuration |
| Transaction partially updates | Operations outside atomic block |
| Deadlock or lock timeout | Lock order and transaction duration |
| Middleware import error | Module path and settings registration |
| Middleware blocks request | get_response call and exception handling |
| Sensitive information in logs | Log format and fields being recorded |

## 7. Industry scenario

A database transaction groups related database operations so they succeed or fail together. Django transaction.atomic() creates an atomic block. For concurrent updates, row locking or database-side expressions may be needed. Financial-style workflows must protect against partial transfers and concurrent requests.

## 8. Approved mini-project — Bank Transfer Transaction Simulator

**Objective:** Bank Transfer Transaction Simulator.

### Required tasks

1. Explain why two balance updates must succeed or fail together.
2. Use Decimal for money-like values.
3. Create a transaction service wrapped in transaction.atomic().
4. Lock rows using select_for_update() when supported and required.
5. Validate amount and available balance.
6. Update source and destination within the same transaction.
7. Create a transfer audit record.
8. Test insufficient funds and forced exceptions.
9. Explain database isolation and concurrency limitations.

### Suggested structure

```text
projects/day_77/
├── README.md
├── config/
└── application/
    ├── services.py
    ├── middleware.py
    └── tests/
```

### Validation checklist

- [ ] Non-positive transfer is rejected.
- [ ] Insufficient balance is rejected.
- [ ] Both account balances update together on success.
- [ ] An exception rolls back all writes in the atomic block.
- [ ] Concurrent access considerations are documented.
- [ ] Amounts use Decimal rather than float.

### Submission evidence

- Source files and configuration.
- Test output for normal and failure cases.
- Query or cache evidence where relevant.
- Safe logs showing request timing or status.
- README explaining trade-offs and limitations.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Bank Transfer Transaction Simulator. Identify the components, data flow, configuration, failure cases and test plan. Do not write the complete solution."

**Guided prompt:** "Help me implement the smallest working example. Explain how to verify it and wait for my output."

**Debugging prompt:** "Here is my configuration, code and observed behavior. Explain whether the issue is key design, transaction scope or middleware order."

**Review prompt:** "Review the implementation for stale data, atomicity, concurrency, middleware order and safe logging."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Improve or coordinate backend request/data behavior.  
B. Replace Django.  
C. Disable database constraints.  
D. Remove HTTP.  
**Answer: A.** The feature addresses performance or request/data consistency.

**Q2. What should be tested after a data change?**  
A. Only the code length.  
B. Cache/database state and expected output.  
C. Only the project title.  
D. Nothing.  
**Answer: B.** Verify the resulting state.

**Q3. What does transaction.atomic() provide?**  
A. CSS styling.  
B. A new URL.  
C. Commit/rollback behavior for grouped database operations.  
D. Email delivery.  
**Answer: C.** Operations in the atomic block succeed or roll back together.

**Q4. Why does middleware order matter?**  
A. It changes the editor theme.  
B. It determines database table names.  
C. It creates Git commits.  
D. Middleware wraps request and response processing in order.  
**Answer: D.** Ordering affects how requests and responses are processed.

**Q5. What is a safe logging practice?**  
A. Log method, path, status and timing while excluding secrets.  
B. Log passwords.  
C. Log all authorization headers.  
D. Log complete private request bodies.  
**Answer: A.** Keep logs useful without exposing sensitive information.

## 11. Interview preparation

**Q1. Explain database transactions and atomic operations.**  
**Answer:** A database transaction groups related database operations so they succeed or fail together. Django transaction.atomic() creates an atomic block. For concurrent updates, row locking or database-side expressions may be needed. Financial-style workflows must protect against partial transfers and concurrent requests.

**Q2. What is one common failure?**  
**Answer:** Non-positive transfer is rejected. Explain how to reproduce and resolve it.

**Q3. How do you verify the implementation?**  
**Answer:** Compare behavior before and after the change, inspect the database/cache/logs and test a failure case.

**Follow-up:** What is one trade-off?  
**Answer:** Caching can return stale data; transactions can hold locks; middleware adds work to every request. Choose based on measured need.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run the required checks.
- [ ] Test failure behavior.
- [ ] Complete Bank Transfer Transaction Simulator.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 78.
