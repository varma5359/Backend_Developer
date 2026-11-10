# Day 73: Interview Questions — Payment Gateway Integration Concepts and Secure Payment Workflows

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 73 class notes](day_73_notes.md)  
**Approved mini-project:** Payment Workflow Simulator

## Core technical questions

### Q1. Explain payment gateway integration concepts and secure payment workflows.
**Answer:** A payment integration delegates card or bank handling to a payment provider. A backend should create a payment session or intent, redirect or return the client to the provider, verify signed webhooks and update order state idempotently. Never store raw card numbers or CVV in your Django database. This lesson is a safe workflow simulation, not a real payment integration.

### Q2. Which components are involved?
**Answer:** payments/models.py, payments/services.py. Explain the role of the service, broker, worker or provider workflow.

### Q3. What is one reliability concern?
**Answer:** Payment state begins as PENDING. Explain how you would observe and recover from the failure.

### Q4. How do you verify the implementation?
**Answer:** Use fake data and local services. Inspect task IDs, logs, state transitions and failure behavior.

### Q5. What should not be stored or logged?
**Answer:** Passwords, API tokens, payment card data, private keys and sensitive customer data.

## Scenario questions

### Q6. A task is queued but never completes. What do you inspect?
**Suggested answer:** Broker availability, worker process, queue routing, task discovery, worker logs and task result.

### Q7. A webhook or task is delivered twice. What should happen?
**Suggested answer:** Use an idempotency key or unique event identifier and ensure the state transition is applied only once.

## Project viva — Payment Workflow Simulator

1. What problem does the workflow solve?
2. Which components are involved?
3. How does the request return before the task finishes?
4. How do you track task status?
5. How are failures handled?
6. How do you prevent duplicate processing?
7. What security controls are required?

## Rapid revision

- **1.** Explain the roles of merchant backend, payment provider and customer browser.
- **2.** Create a PaymentRecord model for a safe simulation.
- **3.** Create a payment request with order reference, amount and currency.
- **4.** Keep raw card details outside the application.
- **5.** Explain provider-hosted checkout or tokenized payment fields.
- **6.** Explain webhook signature verification.
- **7.** Design idempotent event processing using a unique provider event ID.
- **8.** Test pending, success, failure and duplicate event cases.
- **9.** Document that the exercise does not charge real money.

## Readiness checklist
- [ ] Explain the workflow.
- [ ] Explain each component.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure or duplicate case.
- [ ] Present Payment Workflow Simulator with safe evidence.
