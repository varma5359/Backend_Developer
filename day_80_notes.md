# Day 80: Application Performance, Database Query Analysis and Optimization

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–80 — Django fundamentals, ORM, APIs, integrations and performance basics  
**Tools:** Python, Django, VS Code, terminal, database and testing tools  
**Approved mini-project:** Backend Performance Analyzer

> **Trainer guidance:** Teach security and performance as engineering decisions. Ask students to explain the threat or bottleneck, demonstrate the safe approach and verify the result.

## 1. Learning objectives

- Explain application performance, database query analysis and optimization.
- Identify the risk, bottleneck or design responsibility.
- Implement the example step by step.
- Verify the result using a check or measurement.
- Complete Backend Performance Analyzer.

## 2. Concept introduction

Performance work should begin with measurement. Common backend bottlenecks include N+1 database queries, missing indexes, large unpaginated result sets, slow external calls and unnecessary repeated computation. Django QuerySet.explain(), query logging and profiling tools help identify bottlenecks before optimizing.

## 3. File-by-file implementation

### Query inspection

```python
queryset = (
    Employee.objects
    .select_related("department")
    .order_by("full_name")
)

print(queryset.explain())
```

### Model index example

```python
class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=80, db_index=True)
    full_name = models.CharField(max_length=120, db_index=True)
```

### Measure queries in a test

```python
from django.test import TestCase
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as captured:
    list(Employee.objects.select_related("department"))

print("Queries:", len(captured))
```

## 4. Explain the important statements

### Query inspection

1. `queryset = (` — Part of the code or configuration; explain its purpose.
2. `    Employee.objects` — Part of the code or configuration; explain its purpose.
3. `    .select_related("department")` — Fetches a single-valued relation using a join.
4. `    .order_by("full_name")` — Part of the code or configuration; explain its purpose.
5. `)` — Part of the code or configuration; explain its purpose.
6. ` ` — Part of the code or configuration; explain its purpose.
7. `print(queryset.explain())` — Displays the database query plan.

### Model index example

1. `class Employee(models.Model):` — Part of the code or configuration; explain its purpose.
2. `    employee_code = models.CharField(max_length=20, unique=True)` — Part of the code or configuration; explain its purpose.
3. `    department = models.CharField(max_length=80, db_index=True)` — Requests an index for the field.
4. `    full_name = models.CharField(max_length=120, db_index=True)` — Requests an index for the field.

### Measure queries in a test

1. `from django.test import TestCase` — Part of the code or configuration; explain its purpose.
2. `from django.db import connection` — Part of the code or configuration; explain its purpose.
3. `from django.test.utils import CaptureQueriesContext` — Captures database queries executed in a code block.
4. ` ` — Part of the code or configuration; explain its purpose.
5. `with CaptureQueriesContext(connection) as captured:` — Captures database queries executed in a code block.
6. `    list(Employee.objects.select_related("department"))` — Fetches a single-valued relation using a join.
7. ` ` — Part of the code or configuration; explain its purpose.
8. `print("Queries:", len(captured))` — Part of the code or configuration; explain its purpose.

## 5. Risk, measurement or design checklist

| Area | What to verify |
|---|---|
| SQL injection | Parameterized ORM or SQL values |
| XSS | Output escaping and safe HTML handling |
| CSRF | Middleware and tokens for browser POST forms |
| Secrets | Environment or secret manager, never source control |
| Performance | Baseline query count and response time |
| Indexing | Actual query pattern and database plan |
| Architecture | Clear module responsibility and dependency direction |
| Transactions | Related writes succeed or roll back together |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| SQL injection risk | Raw SQL string construction |
| XSS vulnerability | Unescaped output or unsafe HTML marking |
| CSRF failure | Token, middleware and cookie configuration |
| Production security warning | Deployment settings and HTTPS |
| Slow endpoint | Query plan, N+1 pattern, pagination and external calls |
| Too many indexes | Write overhead and actual query usage |
| Circular import | Module dependencies and import direction |
| Overengineered code | Whether each abstraction solves a real problem |

## 7. Industry scenario

Performance work should begin with measurement. Common backend bottlenecks include N+1 database queries, missing indexes, large unpaginated result sets, slow external calls and unnecessary repeated computation. Django QuerySet.explain(), query logging and profiling tools help identify bottlenecks before optimizing.

## 8. Approved mini-project — Backend Performance Analyzer

**Objective:** Backend Performance Analyzer.

### Required tasks

1. Choose a slow endpoint and define the expected response.
2. Measure response time and database query count.
3. Inspect generated SQL using queryset.explain().
4. Look for N+1 related-object access.
5. Apply select_related or prefetch_related when appropriate.
6. Consider indexes for frequently filtered or joined fields.
7. Paginate large result sets.
8. Re-measure and compare correctness and performance.
9. Document the before/after evidence.

### Suggested structure

```text
projects/day_80/
├── README.md
├── config/
└── application/
    ├── models.py
    ├── views.py
    ├── services.py
    ├── selectors.py
    └── tests/
```

### Validation checklist

- [ ] A baseline measurement is recorded.
- [ ] Slow query or repeated query pattern is identified.
- [ ] An optimization is applied for a measured reason.
- [ ] Result data remains correct.
- [ ] Query count or response time is compared.
- [ ] No unnecessary index or cache is added without a reason.

### Submission evidence

- Source files and configuration.
- Security or performance check results.
- Before/after measurements where relevant.
- Test output.
- README with risks, decisions and limitations.
- No secrets or personal data in the repository.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Backend Performance Analyzer. Identify risks or bottlenecks, files, tests and measurable acceptance criteria. Do not provide the entire solution."

**Guided prompt:** "Help me address one issue at a time. Explain the threat or measurement and wait for my evidence."

**Debugging prompt:** "Here is my sanitized configuration, query plan or traceback. Identify the likely cause and propose a safe test."

**Review prompt:** "Review the implementation for security, performance, maintainability and unnecessary complexity."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Reduce risk, measure performance or organize code responsibly.  
B. Replace Python.  
C. Disable testing.  
D. Store secrets in Git.  
**Answer: A.** The concept improves safety, performance or maintainability.

**Q2. What should be done before optimizing?**  
A. Add every possible index.  
B. Measure the current behavior.  
C. Remove all tests.  
D. Rewrite the application.  
**Answer: B.** Measure first so optimization targets a real bottleneck.

**Q3. What is a safe approach to untrusted SQL values?**  
A. Concatenate into raw SQL.  
B. Disable database validation.  
C. Use parameterized queries or ORM filters.  
D. Put values into comments.  
**Answer: C.** Keep values separate from SQL syntax.

**Q4. What is a good architecture principle?**  
A. One giant view for every feature.  
B. Duplicate all business logic.  
C. Add layers without reason.  
D. Give modules clear responsibilities.  
**Answer: D.** Clear responsibilities make code easier to maintain.

**Q5. What is the strongest evidence of completion?**  
A. Verified tests, measurements or security checks.  
B. A folder exists.  
C. A long file.  
D. A diagram only.  
**Answer: A.** Evidence should demonstrate the expected outcome.

## 11. Interview preparation

**Q1. Explain application performance, database query analysis and optimization.**  
**Answer:** Performance work should begin with measurement. Common backend bottlenecks include N+1 database queries, missing indexes, large unpaginated result sets, slow external calls and unnecessary repeated computation. Django QuerySet.explain(), query logging and profiling tools help identify bottlenecks before optimizing.

**Q2. What is one common failure?**  
**Answer:** A baseline measurement is recorded. Explain the cause and the safe correction.

**Q3. How do you verify the result?**  
**Answer:** Run relevant tests, inspect configuration or query plans and compare actual behavior with acceptance criteria.

**Follow-up:** Why should you avoid premature optimization or abstraction?  
**Answer:** It adds complexity without evidence that it solves a real problem.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run the required checks.
- [ ] Test normal and failure cases.
- [ ] Complete Backend Performance Analyzer.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 81.
