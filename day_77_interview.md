# Day 77: Interview Questions — Database Transactions and Atomic Operations

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 77 class notes](day_77_notes.md)  
**Approved mini-project:** Bank Transfer Transaction Simulator

## Core technical questions

### Q1. Explain database transactions and atomic operations.
**Answer:** A database transaction groups related database operations so they succeed or fail together. Django transaction.atomic() creates an atomic block. For concurrent updates, row locking or database-side expressions may be needed. Financial-style workflows must protect against partial transfers and concurrent requests.

### Q2. Which Django APIs or settings are involved?
**Answer:** banking/services.py, Transaction behavior. Explain their responsibility.

### Q3. What is one common failure?
**Answer:** Non-positive transfer is rejected. Explain how the behavior is observed and corrected.

### Q4. How do you verify the implementation?
**Answer:** Compare the expected and actual behavior, inspect relevant database/cache/log output and test failure cases.

### Q5. What is one trade-off?
**Answer:** Explain stale cache data, transaction locks or middleware overhead as appropriate.

## Scenario questions

### Q6. A feature works in a small test but performs poorly or becomes inconsistent under load. What do you inspect?
**Suggested answer:** Measure the behavior, inspect cache hit rate/query count/transaction duration/middleware work and identify the actual bottleneck before changing the design.

### Q7. What should never be logged?
**Suggested answer:** Passwords, tokens, authorization headers, private request bodies and unnecessary personal information.

## Project viva — Bank Transfer Transaction Simulator

1. What problem does it solve?
2. Which Django APIs are used?
3. How did you measure or verify behavior?
4. What failure case did you test?
5. What trade-off did you consider?
6. What would you improve for production?

## Rapid revision

- **1.** Explain why two balance updates must succeed or fail together.
- **2.** Use Decimal for money-like values.
- **3.** Create a transaction service wrapped in transaction.atomic().
- **4.** Lock rows using select_for_update() when supported and required.
- **5.** Validate amount and available balance.
- **6.** Update source and destination within the same transaction.
- **7.** Create a transfer audit record.
- **8.** Test insufficient funds and forced exceptions.
- **9.** Explain database isolation and concurrency limitations.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the implementation.
- [ ] Demonstrate normal and failure cases.
- [ ] Explain one trade-off.
- [ ] Present Bank Transfer Transaction Simulator.
