# Day 91: Interview Questions — Capstone: Application Development and Business Logic

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Related notes:** [Day 91 class notes](day_91_notes.md)  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Core Backend Application

## Core questions

### Q1. Explain capstone: application development and business logic.
**Answer:** The core application implements business workflows using Django models, forms or serializers, views and reusable services. Keep HTTP request handling separate from business rules. Validate state transitions, check user permissions and group related database writes in transactions when partial updates would be unsafe.

### Q2. What deliverables did you create?
**Answer:** Create the Django apps and register them. Implement employee and department management workflows. Implement project creation and manager assignment. Implement task creation, assignment and status transitions. Move reusable business rules into service functions. Move reusable read queries into selectors where useful. Use transactions for related database writes. Validate task states and assignment rules. Add notifications for important events where required. Write a short README for each main workflow.

### Q3. What is one design decision?
**Answer:** Explain one decision, the alternatives and why your choice meets the requirement.

### Q4. How did you validate the work?
**Answer:** Core CRUD workflows work. Business rules are enforced server-side. Invalid task status is rejected. Task assignment validates employee state. Related writes use transactions where needed. Views remain focused on HTTP handling. Queries retrieve the intended records.

### Q5. What remains incomplete or out of scope?
**Answer:** Identify limitations honestly. Do not claim a feature is complete unless it is implemented and tested.

## Scenario-based questions

### Q6. A stakeholder requests a new feature late in the capstone. How do you respond?
**Suggested answer:** Compare it with the approved scope, estimate impact on dependencies and testing, document the decision and avoid destabilizing required deliverables.

### Q7. How do you explain the design to an interviewer?
**Suggested answer:** Start with the business problem, describe the architecture, show the implementation, explain a key trade-off and demonstrate test evidence.

## Capstone viva — Core Backend Application

1. What problem does it solve?
2. Who are the users?
3. What requirements does this deliverable satisfy?
4. Which files or diagrams did you create?
5. What test proves the work?
6. What limitation remains?
7. What would you implement next?

## Readiness checklist

- [ ] Explain the deliverable.
- [ ] Present the artifact.
- [ ] Show validation evidence.
- [ ] Explain a design decision.
- [ ] State limitations honestly.
