# Day 84: Environment Variables, .env Files and Production Settings

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–83 — Django fundamentals, APIs, security and advanced backend concepts  
**Tools:** Python, Django, pytest where applicable, VS Code and terminal  
**Approved mini-project:** Environment Configuration Manager

> **Trainer guidance:** Tests and configuration are part of application quality. Do not use production data or secrets in a learning environment. Ask the learner to show repeatable evidence rather than only saying "it works".

## 1. Learning objectives

- Explain environment variables, .env files and production settings.
- Identify the files and tools involved.
- Implement the example step by step.
- Verify expected and failure behavior.
- Explain how the practice supports production readiness.
- Complete Environment Configuration Manager.

## 2. Concept introduction

Environment variables separate configuration from application code. Different environments may use different database URLs, secret keys, debug flags and allowed hosts. A .env file is convenient for local development but must not be committed. Production secrets should be supplied by a protected environment or secret manager.

## 3. File-by-file implementation

### config/settings.py

```python
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
    if host.strip()
]
```

### .env.example

```python
DJANGO_SECRET_KEY=replace-with-a-local-development-secret
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

### .gitignore

```gitignore
.env
.env.*
!.env.example
.venv/
__pycache__/
```

## 4. Explain the important statements

### config/settings.py

1. `import os` — Part of the configuration; explain how it affects repeatability or safety.
2. ` ` — Part of the configuration; explain how it affects repeatability or safety.
3. `SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]` — Reads configuration from the process environment.
4. `DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"` — Reads configuration from the process environment.
5. ` ` — Part of the configuration; explain how it affects repeatability or safety.
6. `ALLOWED_HOSTS = [` — Part of the configuration; explain how it affects repeatability or safety.
7. `    host.strip()` — Part of the configuration; explain how it affects repeatability or safety.
8. `    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")` — Reads configuration from the process environment.
9. `    if host.strip()` — Part of the configuration; explain how it affects repeatability or safety.
10. `]` — Part of the configuration; explain how it affects repeatability or safety.

### .env.example

1. `DJANGO_SECRET_KEY=replace-with-a-local-development-secret` — Part of the configuration; explain how it affects repeatability or safety.
2. `DJANGO_DEBUG=True` — Part of the configuration; explain how it affects repeatability or safety.
3. `DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost` — Part of the configuration; explain how it affects repeatability or safety.

### .gitignore

1. `.env` — Part of the configuration; explain how it affects repeatability or safety.
2. `.env.*` — Part of the configuration; explain how it affects repeatability or safety.
3. `!.env.example` — Part of the configuration; explain how it affects repeatability or safety.
4. `.venv/` — Part of the configuration; explain how it affects repeatability or safety.
5. `__pycache__/` — Part of the configuration; explain how it affects repeatability or safety.

## 5. Important terminology

| Term | Meaning |
|---|---|
| Unit test | Tests one small unit of behavior |
| Integration test | Tests multiple components working together |
| Fixture | Reusable test setup or data |
| Test client | Simulates requests to a Django application |
| APIClient | DRF test client for API requests |
| Environment variable | Configuration value supplied to the process |
| Secret | Sensitive configuration that must remain protected |
| Deployment check | Django check for production configuration issues |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Test not discovered | Filename and test function naming |
| Database access denied | Test database setup and markers |
| Wrong URL reverse name | URL pattern name |
| Test depends on prior test | Missing setup/cleanup and shared state |
| Secret missing | Environment variable configuration |
| DEBUG accidentally enabled | Production settings source |
| .env appears in Git | .gitignore and tracked-file status |

## 7. Industry scenario

Environment variables separate configuration from application code. Different environments may use different database URLs, secret keys, debug flags and allowed hosts. A .env file is convenient for local development but must not be committed. Production secrets should be supplied by a protected environment or secret manager.

## 8. Approved mini-project — Environment Configuration Manager

**Objective:** Environment Configuration Manager.

### Required tasks

1. Identify settings that vary by environment.
2. Move secret key, debug flag and allowed hosts into environment variables.
3. Read variables using os.environ or os.environ.get().
4. Create a safe .env.example with placeholder values only.
5. Add .env to .gitignore.
6. Configure a local environment without committing the real .env file.
7. Set DEBUG=False and explicit ALLOWED_HOSTS for production.
8. Run Django deployment checks.
9. Explain where production secrets should be stored.

### Suggested structure

```text
projects/day_84/
├── README.md
├── pytest.ini
├── .env.example
└── application/
    └── tests/
```

### Validation checklist

- [ ] Secret key is not hardcoded in committed settings.
- [ ] DEBUG is False in production configuration.
- [ ] ALLOWED_HOSTS is explicit.
- [ ] Real .env file is ignored by Git.
- [ ] Example file contains placeholders only.
- [ ] Missing required configuration fails clearly.

### Submission evidence

- Test files and test output.
- Screenshots or terminal report.
- Example configuration file.
- README with commands and setup.
- No production secrets or real user data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Environment Configuration Manager. List test cases or configuration values, files, commands and expected results. Do not write the complete test suite."

**Guided prompt:** "Help me write one test or setting at a time. Explain what it proves and wait for the test result."

**Debugging prompt:** "Here is my test failure or sanitized configuration. Identify the root cause and the smallest safe fix."

**Review prompt:** "Review the tests or settings for coverage, repeatability, secret safety and production readiness."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Make behavior repeatable and configuration safe.  
B. Replace Python.  
C. Disable errors.  
D. Commit secrets.  
**Answer: A.** Testing and configuration support reliable applications.

**Q2. What should a test verify?**  
A. Only that a file exists.  
B. Expected behavior and important failure cases.  
C. Only the editor theme.  
D. Nothing.  
**Answer: B.** Tests should verify observable behavior.

**Q3. What is a fixture used for?**  
A. Styling templates.  
B. Creating a Git tag.  
C. Reusable test setup.  
D. Replacing Django settings.  
**Answer: C.** Fixtures provide shared setup or test data.

**Q4. Should a real .env file be committed?**  
A. Always.  
B. Only if it contains a password.  
C. If it is renamed.  
D. No. Keep it ignored and provide a placeholder example.  
**Answer: D.** Do not commit private configuration.

**Q5. What is the strongest evidence of completion?**  
A. Repeatable tests pass and invalid cases are covered.  
B. A project folder exists.  
C. A code screenshot only.  
D. A planned test list only.  
**Answer: A.** Execution and results are required.

## 11. Interview preparation

**Q1. Explain environment variables, .env files and production settings.**  
**Answer:** Environment variables separate configuration from application code. Different environments may use different database URLs, secret keys, debug flags and allowed hosts. A .env file is convenient for local development but must not be committed. Production secrets should be supplied by a protected environment or secret manager.

**Q2. What is one common failure?**  
**Answer:** Secret key is not hardcoded in committed settings. Explain how to reproduce and fix it.

**Q3. How do you verify the implementation?**  
**Answer:** Run the test or deployment check, inspect output and confirm both expected and failure behavior.

**Follow-up:** Why should tests be isolated?  
**Answer:** Tests should not depend on previous tests or real external state, so they remain repeatable.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run tests or checks.
- [ ] Verify expected and failure behavior.
- [ ] Complete Environment Configuration Manager.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence.

**Next lesson:** Day 85.
