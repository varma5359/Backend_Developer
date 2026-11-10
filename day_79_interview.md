# Day 79: Interview Questions — Backend Security: SQL Injection, XSS, CSRF and Secure Configuration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 79 class notes](day_79_notes.md)  
**Approved mini-project:** Backend Security Assessment

## Core technical questions

### Q1. Explain backend security: sql injection, xss, csrf and secure configuration.
**Answer:** Backend security requires validating untrusted input, using parameterized database operations, escaping output, protecting browser state-changing requests and keeping secrets out of source control. Django provides protections by default, but developers can disable them accidentally or use unsafe APIs.

### Q2. Which Django APIs or settings are involved?
**Answer:** Safe ORM query, Template output, Production settings checklist. Explain how they support the implementation.

### Q3. What is one common mistake?
**Answer:** Untrusted SQL values are parameterized. Explain how to identify it through a check or measurement.

### Q4. How do you verify the result?
**Answer:** Run the relevant security check, query measurement or tests. Compare actual behavior against the acceptance criteria.

### Q5. What is one trade-off?
**Answer:** Explain the effect of security controls, indexes, caching or architectural layers on the rest of the application.

## Scenario questions

### Q6. A developer wants to optimize an endpoint immediately. What should happen first?
**Suggested answer:** Measure the current query count and response time, inspect the query plan and identify the actual bottleneck before making changes.

### Q7. How do you explain the design to another developer?
**Suggested answer:** Describe the requirement, identify the responsible modules, explain the data flow and show the tests or measurements that validate the decision.

## Project viva — Backend Security Assessment

1. What problem does it solve?
2. Which risk or bottleneck did you identify?
3. Which code or configuration did you change?
4. How did you test the result?
5. What trade-off did you consider?
6. What would you improve next?

## Rapid revision

- **1.** Explain SQL injection and how ORM parameterization helps prevent it.
- **2.** Explain XSS and Django template autoescaping.
- **3.** Explain CSRF and the role of CSRF tokens and middleware.
- **4.** Identify unsafe APIs such as mark_safe for untrusted content.
- **5.** Review DEBUG, ALLOWED_HOSTS and secret configuration.
- **6.** Enable secure cookie and HTTPS settings for production.
- **7.** Review file upload and authentication security.
- **8.** Run Django's deployment check and record warnings.
- **9.** Create a short security assessment with risk, impact and mitigation.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the design decision.
- [ ] Demonstrate verification evidence.
- [ ] Explain one trade-off.
- [ ] Present Backend Security Assessment.
