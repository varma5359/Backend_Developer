# Day 84: Interview Questions — Environment Variables, .env Files and Production Settings

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 84 class notes](day_84_notes.md)  
**Approved mini-project:** Environment Configuration Manager

## Core technical questions

### Q1. Explain environment variables, .env files and production settings.
**Answer:** Environment variables separate configuration from application code. Different environments may use different database URLs, secret keys, debug flags and allowed hosts. A .env file is convenient for local development but must not be committed. Production secrets should be supplied by a protected environment or secret manager.

### Q2. Which tools or files are involved?
**Answer:** config/settings.py, .env.example, .gitignore. Explain how they are used.

### Q3. What is one common mistake?
**Answer:** Secret key is not hardcoded in committed settings. Explain how it affects repeatability or production safety.

### Q4. How do you verify the result?
**Answer:** Run the tests or checks and inspect the output. Include both successful and failure scenarios.

### Q5. What is one production consideration?
**Answer:** Repeatability, secret management, access control, logging and environment separation are important.

## Scenario questions

### Q6. A test passes locally but fails in another environment. What do you inspect?
**Suggested answer:** Dependency versions, settings module, environment variables, test database, test isolation and external service assumptions.

### Q7. How do you prove that configuration is safe?
**Suggested answer:** Verify secrets are loaded from protected environment settings, .env is ignored, DEBUG is disabled in production and allowed hosts are explicit.

## Project viva — Environment Configuration Manager

1. What does the project verify?
2. Which tests or settings did you create?
3. How do you run them?
4. What failure case did you test?
5. How do you avoid relying on production data?
6. What would you improve?

## Rapid revision

- **1.** Identify settings that vary by environment.
- **2.** Move secret key, debug flag and allowed hosts into environment variables.
- **3.** Read variables using os.environ or os.environ.get().
- **4.** Create a safe .env.example with placeholder values only.
- **5.** Add .env to .gitignore.
- **6.** Configure a local environment without committing the real .env file.
- **7.** Set DEBUG=False and explicit ALLOWED_HOSTS for production.
- **8.** Run Django deployment checks.
- **9.** Explain where production secrets should be stored.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Demonstrate the command or configuration.
- [ ] Show test/check output.
- [ ] Explain one failure case.
- [ ] Present Environment Configuration Manager.
