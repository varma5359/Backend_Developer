# Day 38: Interview Questions — Model Relationships: One-to-One, One-to-Many and Many-to-Many

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 38 class notes](day_38_notes.md)  
**Approved mini-project:** College Relationship Manager

## Core questions

### Q1. Explain model relationships: one-to-one, one-to-many and many-to-many.
**Answer:** Relational applications need to connect records. Django represents relationships using ForeignKey for many-to-one, OneToOneField for one-to-one and ManyToManyField for many-to-many relationships. These fields express database relationships and provide convenient ORM accessors.

### Q2. Which Django files or commands are involved?
**Answer:** profiles/models.py. Explain the role of each and how the feature is verified.

### Q3. What is a common beginner mistake?
**Answer:** ForeignKey expresses many employees to one department. Verify the exact file, configuration and output rather than assuming the feature is active.

### Q4. How do you verify the implementation?
**Answer:** Run Django system checks, execute the relevant management command or ORM query and inspect the actual admin/database result.

### Q5. What production concern should you consider?
**Answer:** Access permissions, data integrity, secure configuration, performance and safe schema changes should be considered.

## Scenario questions

### Q6. A feature does not appear as expected. What do you inspect?
**Suggested answer:** Confirm the model or configuration is correct, the app is installed, imports and registration are correct, migrations are applied and the server is running. Read the complete error.

### Q7. How would you explain the implementation to another developer?
**Suggested answer:** Describe the requirement, identify the model/admin/query file, explain the important fields or methods, show the command and provide evidence of the result.

## Practical coding discussion

Be ready to:
- Identify the correct file path.
- Explain important imports and fields.
- Demonstrate the relevant command or query.
- Explain normal and invalid cases.
- Describe the data integrity implications.

## Mini-project viva — College Relationship Manager

1. What problem does it solve?
2. Which models or admin classes are involved?
3. Which commands did you run?
4. What result did you verify?
5. How did you handle a missing or invalid record?
6. What test cases did you perform?
7. What would you improve for production?

## Rapid revision

- **1.** Create a Department model.
- **2.** Add a ForeignKey from Employee to Department.
- **3.** Explain that one department can be related to many employees.
- **4.** Create EmployeeProfile with OneToOneField to Employee.
- **5.** Explain that each employee has at most one profile in this relationship.
- **6.** Create Course and Student models with ManyToManyField.
- **7.** Run makemigrations and migrate.
- **8.** Use the ORM to create and inspect related objects.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Identify the file and command.
- [ ] Demonstrate the result.
- [ ] Explain one failure case.
- [ ] Present College Relationship Manager and its evidence.
