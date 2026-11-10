# Day 13: Interview Questions — Introduction to OOP, Classes and Objects

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 13 notes](day_13_notes.md)  
**Approved mini-project:** Student Object Manager

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. What is OOP?
**Answer:** OOP is a programming approach that organizes code around objects. Objects combine attributes (data) and methods (behavior).

**Practical example:** A student object stores a student's name and course and can display a profile.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is a class?
**Answer:** A class is a blueprint defining the structure and behavior of objects.

**Practical example:** Student is a class; student1 is an object created from it.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. What is an object?
**Answer:** An object is an instance created from a class. Multiple objects can have different attribute values.

**Practical example:** Student() creates an instance.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. What are attributes and methods?
**Answer:** Attributes store information. Methods are functions defined inside a class that implement behavior.

**Practical example:** name is an attribute; display_profile() is a method.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. Can one class create multiple objects?
**Answer:** Yes. Each object is a separate instance and can hold its own values.

**Practical example:** A college portal can create one Student object for every student.

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A college portal has 2,000 student records. How can OOP help?

**Suggested answer:** Define a Student class for common data and behavior. Create a separate object for each student. This gives the application a consistent structure without inventing separate variable names for every record.

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Write a Book class, create two objects, assign title and author, and explain the class, objects, attributes and method.

**What the interviewer may evaluate**
- Correct class and object definitions.
- Clear naming and indentation.
- Correct use of attributes and methods.
- Ability to explain each line.
- Correct handling of normal and invalid cases.
- Ability to reason about design trade-offs.

**Suggested explanation sequence**
1. State the requirement.
2. Identify the class or classes.
3. Explain the data stored by each object.
4. Explain the method responsibilities.
5. Run a normal case.
6. Run an edge case.
7. Explain what the output proves.

## 5. Mini-project viva — Student Object Manager

Be prepared to answer:
1. What problem does the project solve?
2. Why did you create these classes?
3. What attributes belong to each class?
4. Which methods change object state?
5. How do you prevent invalid data?
6. What happens if the user repeats an operation?
7. Which test cases did you run?
8. What is currently not supported?
9. How would you extend the project?
10. What would be required to store data persistently?

**Strong project answer:** Describe what you personally implemented, show the evidence, explain one bug you found and how you fixed it. Do not claim features that are not implemented.

## 6. Common incorrect answers to avoid

| Incorrect statement | Better explanation |
|---|---|
| A class and an object are the same | A class defines a type; an object is an instance |
| self is a reserved keyword | self is a convention for the instance parameter |
| __init__ creates every part of an object by itself | Python creates the instance and calls __init__ to initialize it |
| Every method must be static | Choose method type based on whether it needs instance or class state |
| Inheritance is always better than composition | Choose the relationship that matches the domain |
| Double underscore makes data secure | Name mangling reduces accidental clashes; it is not security |
| Every Python object is saved in a database | Plain objects are normally in memory until explicitly persisted |

## 7. Rapid revision

- **What is OOP?** OOP is a programming approach that organizes code around objects. Objects combine attributes (data) and methods (behavior).
- **What is a class?** A class is a blueprint defining the structure and behavior of objects.
- **What is an object?** An object is an instance created from a class. Multiple objects can have different attribute values.
- **What are attributes and methods?** Attributes store information. Methods are functions defined inside a class that implement behavior.
- **Can one class create multiple objects?** Yes. Each object is a separate instance and can hold its own values.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Student Object Manager project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
