# Day 18: Interview Questions — Complete OOP Integration and Practical Design

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 18 notes](day_18_notes.md)  
**Approved mini-project:** Library Management System

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. Explain the four commonly discussed OOP pillars.
**Answer:** Encapsulation groups data and behavior and controls state changes; abstraction exposes essential operations; inheritance reuses and extends behavior; polymorphism allows different objects to respond to a common operation differently.

**Practical example:** A payment service may use all four concepts in its design.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is composition?
**Answer:** Composition is a relationship where one object contains or manages another object.

**Practical example:** A Library object manages Book objects.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. When should inheritance be used?
**Answer:** Use inheritance when the child is a specialized form of the parent and shared behavior makes conceptual sense.

**Practical example:** Developer is a specialized Employee.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. Does a normal Python object automatically save to a database?
**Answer:** No. A normal object usually exists in memory. A file or database mechanism is needed for persistence. Django models integrate with a database through the ORM.

**Practical example:** A Book instance in a plain Python script is not automatically stored in PostgreSQL.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. How does OOP help a Django developer?
**Answer:** Django uses classes for models, forms, serializers and class-based views. Python OOP knowledge makes these structures easier to understand.

**Practical example:** A Django model defines fields and behavior for a database-backed entity.

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A library manages books. Should Library inherit from Book?

**Suggested answer:** No. A library is not a book; it contains or manages books. Composition is the more accurate relationship.

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Explain the Book, Member and Library classes in your project. Identify responsibilities and object relationships.

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

## 5. Mini-project viva — Library Management System

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

- **Explain the four commonly discussed OOP pillars.** Encapsulation groups data and behavior and controls state changes; abstraction exposes essential operations; inheritance reuses and extends behavior; polymorphism allows different objects to respond to a common operation differently.
- **What is composition?** Composition is a relationship where one object contains or manages another object.
- **When should inheritance be used?** Use inheritance when the child is a specialized form of the parent and shared behavior makes conceptual sense.
- **Does a normal Python object automatically save to a database?** No. A normal object usually exists in memory. A file or database mechanism is needed for persistence. Django models integrate with a database through the ORM.
- **How does OOP help a Django developer?** Django uses classes for models, forms, serializers and class-based views. Python OOP knowledge makes these structures easier to understand.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Library Management System project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
