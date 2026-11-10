# Day 79: Backend Security: SQL Injection, XSS, CSRF and Secure Configuration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–80 — Django fundamentals, ORM, APIs, integrations and performance basics  
**Tools:** Python, Django, VS Code, terminal, database and testing tools  
**Approved mini-project:** Backend Security Assessment

> **Trainer guidance:** Teach security and performance as engineering decisions. Ask students to explain the threat or bottleneck, demonstrate the safe approach and verify the result.

## 1. Learning objectives

- Explain backend security: sql injection, xss, csrf and secure configuration.
- Identify the risk, bottleneck or design responsibility.
- Implement the example step by step.
- Verify the result using a check or measurement.
- Complete Backend Security Assessment.

## 2. Concept introduction

Backend security requires validating untrusted input, using parameterized database operations, escaping output, protecting browser state-changing requests and keeping secrets out of source control. Django provides protections by default, but developers can disable them accidentally or use unsafe APIs.

## 3. File-by-file implementation

### Safe ORM query

```python
# Safe: Django ORM parameterizes values
employees = Employee.objects.filter(full_name__icontains=user_input)

# Avoid constructing raw SQL using string concatenation.
# If raw SQL is necessary, use placeholders and parameters.
```

### Template output

```python
<!-- Django templates autoescape variables by default -->
<p>{{ employee.full_name }}</p>

<!-- Avoid mark_safe on untrusted user input. -->
```

### Production settings checklist

```python
DEBUG = False
ALLOWED_HOSTS = ["backend.example.com"]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Load SECRET_KEY and database credentials from protected environment settings.
```

## 4. Explain the important statements

### Safe ORM query

1. `# Safe: Django ORM parameterizes values` — Comment describing the safe or unsafe pattern.
2. `employees = Employee.objects.filter(full_name__icontains=user_input)` — Builds a parameterized ORM query.
3. ` ` — Part of the code or configuration; explain its purpose.
4. `# Avoid constructing raw SQL using string concatenation.` — Comment describing the safe or unsafe pattern.
5. `# If raw SQL is necessary, use placeholders and parameters.` — Comment describing the safe or unsafe pattern.

### Template output

1. `<!-- Django templates autoescape variables by default -->` — Part of the code or configuration; explain its purpose.
2. `<p>{{ employee.full_name }}</p>` — Part of the code or configuration; explain its purpose.
3. ` ` — Part of the code or configuration; explain its purpose.
4. `<!-- Avoid mark_safe on untrusted user input. -->` — Part of the code or configuration; explain its purpose.

### Production settings checklist

1. `DEBUG = False` — Part of the code or configuration; explain its purpose.
2. `ALLOWED_HOSTS = ["backend.example.com"]` — Part of the code or configuration; explain its purpose.
3. `CSRF_COOKIE_SECURE = True` — Part of the code or configuration; explain its purpose.
4. `SESSION_COOKIE_SECURE = True` — Part of the code or configuration; explain its purpose.
5. `SECURE_SSL_REDIRECT = True` — Part of the code or configuration; explain its purpose.
6. `SECURE_CONTENT_TYPE_NOSNIFF = True` — Part of the code or configuration; explain its purpose.
7. `X_FRAME_OPTIONS = "DENY"` — Part of the code or configuration; explain its purpose.
8. ` ` — Part of the code or configuration; explain its purpose.
9. `# Load SECRET_KEY and database credentials from protected environment settings.` — Comment describing the safe or unsafe pattern.

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

Backend security requires validating untrusted input, using parameterized database operations, escaping output, protecting browser state-changing requests and keeping secrets out of source control. Django provides protections by default, but developers can disable them accidentally or use unsafe APIs.

## 8. Approved mini-project — Backend Security Assessment

**Objective:** Backend Security Assessment.

### Required tasks

1. Explain SQL injection and how ORM parameterization helps prevent it.
2. Explain XSS and Django template autoescaping.
3. Explain CSRF and the role of CSRF tokens and middleware.
4. Identify unsafe APIs such as mark_safe for untrusted content.
5. Review DEBUG, ALLOWED_HOSTS and secret configuration.
6. Enable secure cookie and HTTPS settings for production.
7. Review file upload and authentication security.
8. Run Django's deployment check and record warnings.
9. Create a short security assessment with risk, impact and mitigation.

### Suggested structure

```text
projects/day_79/
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

- [ ] Untrusted SQL values are parameterized.
- [ ] Untrusted template values are escaped.
- [ ] CSRF protection remains enabled.
- [ ] No secrets are committed.
- [ ] DEBUG is disabled in production configuration.
- [ ] ALLOWED_HOSTS is explicit.
- [ ] Secure cookies and HTTPS settings are reviewed.

### Submission evidence

- Source files and configuration.
- Security or performance check results.
- Before/after measurements where relevant.
- Test output.
- README with risks, decisions and limitations.
- No secrets or personal data in the repository.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Backend Security Assessment. Identify risks or bottlenecks, files, tests and measurable acceptance criteria. Do not provide the entire solution."

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

**Q1. Explain backend security: sql injection, xss, csrf and secure configuration.**  
**Answer:** Backend security requires validating untrusted input, using parameterized database operations, escaping output, protecting browser state-changing requests and keeping secrets out of source control. Django provides protections by default, but developers can disable them accidentally or use unsafe APIs.

**Q2. What is one common failure?**  
**Answer:** Untrusted SQL values are parameterized. Explain the cause and the safe correction.

**Q3. How do you verify the result?**  
**Answer:** Run relevant tests, inspect configuration or query plans and compare actual behavior with acceptance criteria.

**Follow-up:** Why should you avoid premature optimization or abstraction?  
**Answer:** It adds complexity without evidence that it solves a real problem.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run the required checks.
- [ ] Test normal and failure cases.
- [ ] Complete Backend Security Assessment.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 80.
