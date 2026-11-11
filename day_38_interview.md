# Day 38: Interview Guide — Model Relationships: One-to-One, One-to-Many and Many-to-Many

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 38 notes](day_38_notes.md)  
**Mini-project:** College Relationship Manager

## 1. Technical questions with model answers

### Q1. Where should a ForeignKey be placed for one department and many students?

**Model answer:** On Student, the many side. Each student row stores the department reference.

### Q2. How does OneToOneField differ from ForeignKey?

**Model answer:** OneToOneField enforces that each referenced object can be linked to at most one row through that relation. It is implemented like a foreign key with a uniqueness constraint.

### Q3. How does ManyToManyField work in the database?

**Model answer:** Django uses an intermediary join table that stores pairs of related primary keys. A student can link to many courses and a course to many students.

### Q4. What does related_name provide?

**Model answer:** It defines the reverse accessor used from the related model, such as department.students or course.students.

### Q5. What is the difference between CASCADE and PROTECT?

**Model answer:** CASCADE deletes dependent objects when the referenced object is deleted. PROTECT blocks deletion while protected references exist.

### Q6. What happens when student.profile is accessed but no profile exists?

**Model answer:** The reverse OneToOne accessor raises StudentProfile.DoesNotExist/RelatedObjectDoesNotExist. Check with hasattr or catch the specific related-object exception.

## 2. Scenario-based interview question

**Scenario:** A student can enroll in multiple courses and each course can contain many students. Which field do you use and where is the data stored?

**Model answer:** Use ManyToManyField on one of the models, for example Student.courses. Django creates an intermediary table containing student and course IDs. Query from either direction using the related manager.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Explain the schema, migrate it, create sample records, run forward and reverse queries for all three relationship types, and test a student without a profile.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — College Relationship Manager

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present College Relationship Manager with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What does ForeignKey represent?
**Answer:** Many records can refer to one related record. For example, many students can belong to one department.

### Q6. What does OneToOneField represent?
**Answer:** One record is connected to one related record, such as one student having one student profile.

### Q7. What does ManyToManyField represent?
**Answer:** Many records on each side can be associated, such as students enrolled in many courses and courses containing many students.

### Q8. What does related_name control?
**Answer:** It defines the reverse accessor used to navigate from the related object.

### Q9. What is the difference between PROTECT and CASCADE?
**Answer:** PROTECT prevents deletion while protected related rows exist. CASCADE deletes related rows when the referenced object is deleted.

### Q10. Does remove() delete the related model object?
**Answer:** No. For a many-to-many relationship, remove() deletes the association, not the related Course record.

### Q11. Scenario: student.profile raises an exception.
**Answer:** A reverse OneToOne related profile may not exist. Handle the missing case or use get_or_create where appropriate.

### Q12. Scenario: relationship loop causes many queries.
**Answer:** Use select_related for single-valued relations and prefetch_related for collections after measuring the query pattern.

