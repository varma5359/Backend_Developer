# Day 16: Interview Questions — Inheritance and Method Overriding

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 16 notes](day_16_notes.md)  
**Approved mini-project:** Employee Role Management System

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. What is inheritance?
**Answer:** Inheritance allows a child class to reuse and extend attributes and methods from a parent class.

**Practical example:** Developer and Tester can inherit common employee details.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is method overriding?
**Answer:** A child class provides its own implementation of a method already defined in a parent class.

**Practical example:** Developer overrides work() to describe development work.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. What is super()?
**Answer:** super() provides access to methods in the next class in the method resolution order. It is commonly used to reuse parent initialization or behavior.

**Practical example:** super().__init__(name, employee_id) initializes shared fields.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. Does Python support multiple inheritance?
**Answer:** Yes. A class can inherit from multiple parent classes. Python uses method resolution order to determine lookup order.

**Practical example:** A class may inherit from two mixins, but the design needs care.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. Difference between inheritance and composition?
**Answer:** Inheritance models an is-a relationship. Composition models a has-a relationship.

**Practical example:** Developer is an Employee; Library has Books.

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A company has Developer and Tester roles. Both have employee ID and name, but their work differs. How could inheritance help?

**Suggested answer:** Define common fields and behavior in Employee. Developer and Tester inherit that behavior and add role-specific fields or override work().

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Build Employee, Developer and Tester classes. Use super() and override work(). Explain the output.

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

## 5. Mini-project viva — Employee Role Management System

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

- **What is inheritance?** Inheritance allows a child class to reuse and extend attributes and methods from a parent class.
- **What is method overriding?** A child class provides its own implementation of a method already defined in a parent class.
- **What is super()?** super() provides access to methods in the next class in the method resolution order. It is commonly used to reuse parent initialization or behavior.
- **Does Python support multiple inheritance?** Yes. A class can inherit from multiple parent classes. Python uses method resolution order to determine lookup order.
- **Difference between inheritance and composition?** Inheritance models an is-a relationship. Composition models a has-a relationship.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Employee Role Management System project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
