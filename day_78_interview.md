# Day 78: Interview Questions — Django Middleware and Request-Response Processing

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 78 class notes](day_78_notes.md)  
**Approved mini-project:** Request Monitoring Middleware

## Core technical questions

### Q1. Explain django middleware and request-response processing.
**Answer:** Middleware is a component that processes requests and responses globally around Django views. Middleware can inspect or modify requests before a view and responses afterward. Middleware order matters. It is useful for cross-cutting concerns such as request IDs, safe logging and response headers.

### Q2. Which Django APIs or settings are involved?
**Answer:** profiles/middleware.py, config/settings.py. Explain their responsibility.

### Q3. What is one common failure?
**Answer:** Middleware imports successfully. Explain how the behavior is observed and corrected.

### Q4. How do you verify the implementation?
**Answer:** Compare the expected and actual behavior, inspect relevant database/cache/log output and test failure cases.

### Q5. What is one trade-off?
**Answer:** Explain stale cache data, transaction locks or middleware overhead as appropriate.

## Scenario questions

### Q6. A feature works in a small test but performs poorly or becomes inconsistent under load. What do you inspect?
**Suggested answer:** Measure the behavior, inspect cache hit rate/query count/transaction duration/middleware work and identify the actual bottleneck before changing the design.

### Q7. What should never be logged?
**Suggested answer:** Passwords, tokens, authorization headers, private request bodies and unnecessary personal information.

## Project viva — Request Monitoring Middleware

1. What problem does it solve?
2. Which Django APIs are used?
3. How did you measure or verify behavior?
4. What failure case did you test?
5. What trade-off did you consider?
6. What would you improve for production?

## Rapid revision

- **1.** Explain where middleware sits in the request-response lifecycle.
- **2.** Create a middleware class with __init__ and __call__.
- **3.** Record a start time before calling the next component.
- **4.** Call get_response(request) to continue processing.
- **5.** Inspect response status and elapsed time afterward.
- **6.** Add the middleware path to settings.py.
- **7.** Run the server and inspect logs.
- **8.** Avoid logging request bodies, passwords, tokens or sensitive query values.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the implementation.
- [ ] Demonstrate normal and failure cases.
- [ ] Explain one trade-off.
- [ ] Present Request Monitoring Middleware.
