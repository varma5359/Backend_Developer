# Day 74: Interview Questions — Background Tasks and Asynchronous Processing Concepts

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 74 class notes](day_74_notes.md)  
**Approved mini-project:** Background Report Generator

## Core technical questions

### Q1. Explain background tasks and asynchronous processing concepts.
**Answer:** Some backend work takes longer than a normal HTTP request should wait for, such as report generation, bulk email and file processing. A background task is placed on a queue and processed by a worker separately from the web request. The web request can return a job identifier or acknowledgement while the worker continues.

### Q2. Which components are involved?
**Answer:** reports/services.py, Conceptual request flow. Explain the role of the service, broker, worker or provider workflow.

### Q3. What is one reliability concern?
**Answer:** Slow work is separated from the request handler. Explain how you would observe and recover from the failure.

### Q4. How do you verify the implementation?
**Answer:** Use fake data and local services. Inspect task IDs, logs, state transitions and failure behavior.

### Q5. What should not be stored or logged?
**Answer:** Passwords, API tokens, payment card data, private keys and sensitive customer data.

## Scenario questions

### Q6. A task is queued but never completes. What do you inspect?
**Suggested answer:** Broker availability, worker process, queue routing, task discovery, worker logs and task result.

### Q7. A webhook or task is delivered twice. What should happen?
**Suggested answer:** Use an idempotency key or unique event identifier and ensure the state transition is applied only once.

## Project viva — Background Report Generator

1. What problem does the workflow solve?
2. Which components are involved?
3. How does the request return before the task finishes?
4. How do you track task status?
5. How are failures handled?
6. How do you prevent duplicate processing?
7. What security controls are required?

## Rapid revision

- **1.** Identify a task that should not block a normal web request.
- **2.** Separate the business logic into a reusable service function.
- **3.** Create a job/status record for long-running work.
- **4.** Explain the role of a message broker and worker.
- **5.** Return an acknowledgement or job identifier to the client.
- **6.** Track queued, running, succeeded and failed states.
- **7.** Design retry and duplicate-processing behavior.
- **8.** Explain why the next lesson uses Celery and Redis.

## Readiness checklist
- [ ] Explain the workflow.
- [ ] Explain each component.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure or duplicate case.
- [ ] Present Background Report Generator with safe evidence.
