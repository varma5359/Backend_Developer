# Day 36: Interview Questions — Django Admin Panel and Model Registration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 36 class notes](day_36_notes.md)  
**Approved mini-project:** Admin-Based Inventory Manager

## Core questions

### Q1. Explain django admin panel and model registration.
**Answer:** Django Admin is a built-in interface for trusted staff to manage registered models. A model becomes available in the admin site after it is registered with an admin site. The admin interface uses Django authentication and permissions; it should not be exposed carelessly.

### Q2. Which Django files or commands are involved?
**Answer:** profiles/admin.py, Terminal commands. Explain the role of each and how the feature is verified.

### Q3. What is a common beginner mistake?
**Answer:** Employee appears in the admin index. Verify the exact file, configuration and output rather than assuming the feature is active.

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

## Mini-project viva — Admin-Based Inventory Manager

1. What problem does it solve?
2. Which models or admin classes are involved?
3. Which commands did you run?
4. What result did you verify?
5. How did you handle a missing or invalid record?
6. What test cases did you perform?
7. What would you improve for production?

## Rapid revision

- **1.** Confirm Employee is defined in profiles/models.py.
- **2.** Open profiles/admin.py.
- **3.** Import django.contrib.admin and Employee.
- **4.** Register Employee using admin.site.register or @admin.register.
- **5.** Add list_display to show useful columns.
- **6.** Add search_fields and list_filter.
- **7.** Create a superuser using the management command.
- **8.** Start the development server and sign in at /admin/.
- **9.** Create, update and delete a sample record in the admin interface.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Identify the file and command.
- [ ] Demonstrate the result.
- [ ] Explain one failure case.
- [ ] Present Admin-Based Inventory Manager and its evidence.
