# Day 90: Interview Questions — Capstone: Database Design, Relationships and Django Models

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 8 — End-to-End Backend Capstone  
**Related notes:** [Day 90 class notes](day_90_notes.md)  
**Capstone:** Employee and Project Management System — Django Backend and REST API  
**Approved deliverable:** Database and Model Design

## Core questions

### Q1. Explain capstone: database design, relationships and django models.
**Answer:** The capstone database represents users, departments, employees, projects, tasks and notifications. Use primary keys, foreign keys, one-to-one and one-to-many relationships deliberately. Model constraints should protect important business rules, and indexes should be added only where query patterns justify them.

### Q2. What deliverables did you create?
**Answer:** Translate the Day 89 entities into database tables. Define primary keys and field types. Create Department and Employee models. Create Project with a manager relationship. Create Task with project and assigned employee relationships. Create Notification linked to a user. Choose on_delete behavior based on business meaning. Add constraints for unique values and valid states where needed. Generate and inspect migrations. Apply migrations to a clean development database. Create sample data and verify relationships using the ORM.

### Q3. What is one design decision?
**Answer:** Explain one decision, the alternatives and why your choice meets the requirement.

### Q4. How did you validate the work?
**Answer:** All required entities are represented. ForeignKey and OneToOneField relationships match the design. on_delete behavior is deliberate. Required fields and nullability are appropriate. Constraints protect key business rules. Migrations apply successfully. Sample records can be created and related correctly.

### Q5. What remains incomplete or out of scope?
**Answer:** Identify limitations honestly. Do not claim a feature is complete unless it is implemented and tested.

## Scenario-based questions

### Q6. A stakeholder requests a new feature late in the capstone. How do you respond?
**Suggested answer:** Compare it with the approved scope, estimate impact on dependencies and testing, document the decision and avoid destabilizing required deliverables.

### Q7. How do you explain the design to an interviewer?
**Suggested answer:** Start with the business problem, describe the architecture, show the implementation, explain a key trade-off and demonstrate test evidence.

## Capstone viva — Database and Model Design

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
