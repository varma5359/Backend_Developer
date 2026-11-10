# Day 37: Interview Questions — Django ORM Fundamentals and Querying Records

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related notes:** [Day 37 class notes](day_37_notes.md)  
**Approved mini-project:** Product Query Explorer

## Core questions

### Q1. Explain django orm fundamentals and querying records.
**Answer:** The Django ORM lets Python code interact with database records through model classes and QuerySets. A QuerySet represents a database query and is generally evaluated when its results are needed. ORM methods such as all(), filter(), exclude(), get(), order_by() and values() help retrieve records.

### Q2. Which Django files or commands are involved?
**Answer:** Django shell, Shell examples. Explain the role of each and how the feature is verified.

### Q3. What is a common beginner mistake?
**Answer:** The model imports successfully. Verify the exact file, configuration and output rather than assuming the feature is active.

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

## Mini-project viva — Product Query Explorer

1. What problem does it solve?
2. Which models or admin classes are involved?
3. Which commands did you run?
4. What result did you verify?
5. How did you handle a missing or invalid record?
6. What test cases did you perform?
7. What would you improve for production?

## Rapid revision

- **1.** Run python manage.py shell from the project folder.
- **2.** Import the Employee model.
- **3.** Inspect all() and understand that it returns a QuerySet.
- **4.** Use filter() with an exact field value.
- **5.** Use exclude() to remove matching records.
- **6.** Use get() for a record expected to match exactly one row and understand DoesNotExist/MultipleObjectsReturned.
- **7.** Use order_by() to sort results.
- **8.** Use values() to return selected fields as dictionaries.
- **9.** Compare the ORM query with the SQL concept it represents.

## Readiness checklist
- [ ] Explain the feature.
- [ ] Identify the file and command.
- [ ] Demonstrate the result.
- [ ] Explain one failure case.
- [ ] Present Product Query Explorer and its evidence.
