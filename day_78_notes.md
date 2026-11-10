# Day 78: Django Middleware and Request-Response Processing

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–77 — Django, ORM, APIs, background tasks and deployment concepts  
**Tools:** Python, Django, database, VS Code and terminal  
**Approved mini-project:** Request Monitoring Middleware

> **Trainer guidance:** Explain what problem the feature solves and when it should be used. Measure behavior where relevant. Avoid adding caching, locking or middleware without a clear requirement.

## 1. Learning objectives

- Explain django middleware and request-response processing.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Explain the reliability or performance implications.
- Test normal and failure cases.
- Complete Request Monitoring Middleware.

## 2. Concept introduction

Middleware is a component that processes requests and responses globally around Django views. Middleware can inspect or modify requests before a view and responses afterward. Middleware order matters. It is useful for cross-cutting concerns such as request IDs, safe logging and response headers.

## 3. File-by-file implementation

### profiles/middleware.py

```python
import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration_ms = (time.perf_counter() - start) * 1000

        logger.info(
            "method=%s path=%s status=%s duration_ms=%.2f",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
        )
        return response
```

### config/settings.py

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "profiles.middleware.RequestTimingMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
```

## 4. Explain the important statements

### profiles/middleware.py

1. `import time` — Part of the configuration; explain how it affects the request or database.
2. `import logging` — Part of the configuration; explain how it affects the request or database.
3. ` ` — Part of the configuration; explain how it affects the request or database.
4. `logger = logging.getLogger(__name__)` — Part of the configuration; explain how it affects the request or database.
5. ` ` — Part of the configuration; explain how it affects the request or database.
6. `class RequestTimingMiddleware:` — Part of the configuration; explain how it affects the request or database.
7. `    def __init__(self, get_response):` — Defines a service function or middleware method.
8. `        self.get_response = get_response` — Passes the request to the next middleware or view.
9. ` ` — Part of the configuration; explain how it affects the request or database.
10. `    def __call__(self, request):` — Defines a service function or middleware method.
11. `        start = time.perf_counter()` — Part of the configuration; explain how it affects the request or database.
12. `        response = self.get_response(request)` — Passes the request to the next middleware or view.
13. `        duration_ms = (time.perf_counter() - start) * 1000` — Part of the configuration; explain how it affects the request or database.
14. ` ` — Part of the configuration; explain how it affects the request or database.
15. `        logger.info(` — Part of the configuration; explain how it affects the request or database.
16. `            "method=%s path=%s status=%s duration_ms=%.2f",` — Part of the configuration; explain how it affects the request or database.
17. `            request.method,` — Part of the configuration; explain how it affects the request or database.
18. `            request.path,` — Part of the configuration; explain how it affects the request or database.
19. `            response.status_code,` — Part of the configuration; explain how it affects the request or database.
20. `            duration_ms,` — Part of the configuration; explain how it affects the request or database.
21. `        )` — Part of the configuration; explain how it affects the request or database.
22. `        return response` — Part of the configuration; explain how it affects the request or database.

### config/settings.py

1. `MIDDLEWARE = [` — Part of the configuration; explain how it affects the request or database.
2. `    "django.middleware.security.SecurityMiddleware",` — Part of the configuration; explain how it affects the request or database.
3. `    "django.contrib.sessions.middleware.SessionMiddleware",` — Part of the configuration; explain how it affects the request or database.
4. `    "django.middleware.common.CommonMiddleware",` — Part of the configuration; explain how it affects the request or database.
5. `    "django.middleware.csrf.CsrfViewMiddleware",` — Part of the configuration; explain how it affects the request or database.
6. `    "django.contrib.auth.middleware.AuthenticationMiddleware",` — Part of the configuration; explain how it affects the request or database.
7. `    "profiles.middleware.RequestTimingMiddleware",` — Part of the configuration; explain how it affects the request or database.
8. `    "django.contrib.messages.middleware.MessageMiddleware",` — Part of the configuration; explain how it affects the request or database.
9. `]` — Part of the configuration; explain how it affects the request or database.

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

Middleware is a component that processes requests and responses globally around Django views. Middleware can inspect or modify requests before a view and responses afterward. Middleware order matters. It is useful for cross-cutting concerns such as request IDs, safe logging and response headers.

## 8. Approved mini-project — Request Monitoring Middleware

**Objective:** Request Monitoring Middleware.

### Required tasks

1. Explain where middleware sits in the request-response lifecycle.
2. Create a middleware class with __init__ and __call__.
3. Record a start time before calling the next component.
4. Call get_response(request) to continue processing.
5. Inspect response status and elapsed time afterward.
6. Add the middleware path to settings.py.
7. Run the server and inspect logs.
8. Avoid logging request bodies, passwords, tokens or sensitive query values.

### Suggested structure

```text
projects/day_78/
├── README.md
├── config/
└── application/
    ├── services.py
    ├── middleware.py
    └── tests/
```

### Validation checklist

- [ ] Middleware imports successfully.
- [ ] Middleware is registered in settings.
- [ ] Request reaches the view.
- [ ] Response returns through middleware.
- [ ] Timing and status are logged.
- [ ] Sensitive request data is not logged.

### Submission evidence

- Source files and configuration.
- Test output for normal and failure cases.
- Query or cache evidence where relevant.
- Safe logs showing request timing or status.
- README explaining trade-offs and limitations.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Request Monitoring Middleware. Identify the components, data flow, configuration, failure cases and test plan. Do not write the complete solution."

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

**Q1. Explain django middleware and request-response processing.**  
**Answer:** Middleware is a component that processes requests and responses globally around Django views. Middleware can inspect or modify requests before a view and responses afterward. Middleware order matters. It is useful for cross-cutting concerns such as request IDs, safe logging and response headers.

**Q2. What is one common failure?**  
**Answer:** Middleware imports successfully. Explain how to reproduce and resolve it.

**Q3. How do you verify the implementation?**  
**Answer:** Compare behavior before and after the change, inspect the database/cache/logs and test a failure case.

**Follow-up:** What is one trade-off?  
**Answer:** Caching can return stale data; transactions can hold locks; middleware adds work to every request. Choose based on measured need.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run the required checks.
- [ ] Test failure behavior.
- [ ] Complete Request Monitoring Middleware.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 79.
