# Day 75: Interview Questions — Celery and Redis Fundamentals for Background Jobs

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 75 class notes](day_75_notes.md)  
**Approved mini-project:** Asynchronous Email Task System

## Core technical questions

### Q1. Explain celery and redis fundamentals for background jobs.
**Answer:** Celery is a distributed task queue for executing work outside the web request process. Redis can act as a message broker and, optionally, a result backend. A Django application enqueues a task; a Celery worker consumes and executes it. Tasks should be idempotent where possible and should not assume a message is delivered exactly once.

### Q2. Which components are involved?
**Answer:** config/celery.py, config/__init__.py, config/settings.py, profiles/tasks.py, Call the task. Explain the role of the service, broker, worker or provider workflow.

### Q3. What is one reliability concern?
**Answer:** Celery app imports with Django settings. Explain how you would observe and recover from the failure.

### Q4. How do you verify the implementation?
**Answer:** Use fake data and local services. Inspect task IDs, logs, state transitions and failure behavior.

### Q5. What should not be stored or logged?
**Answer:** Passwords, API tokens, payment card data, private keys and sensitive customer data.

## Scenario questions

### Q6. A task is queued but never completes. What do you inspect?
**Suggested answer:** Broker availability, worker process, queue routing, task discovery, worker logs and task result.

### Q7. A webhook or task is delivered twice. What should happen?
**Suggested answer:** Use an idempotency key or unique event identifier and ensure the state transition is applied only once.

## Project viva — Asynchronous Email Task System

1. What problem does the workflow solve?
2. Which components are involved?
3. How does the request return before the task finishes?
4. How do you track task status?
5. How are failures handled?
6. How do you prevent duplicate processing?
7. What security controls are required?

## Rapid revision

- **1.** Install Celery and the Redis Python client in the environment.
- **2.** Start a local Redis service for development.
- **3.** Create config/celery.py and configure the Celery app.
- **4.** Expose the Celery app from config/__init__.py.
- **5.** Configure the broker URL and optional result backend.
- **6.** Create a task using @shared_task.
- **7.** Call the task using delay() from a view or service.
- **8.** Start a Celery worker in a separate terminal.
- **9.** Inspect task execution and failure behavior.
- **10.** Keep broker credentials in environment configuration for real deployments.

## Readiness checklist
- [ ] Explain the workflow.
- [ ] Explain each component.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure or duplicate case.
- [ ] Present Asynchronous Email Task System with safe evidence.
