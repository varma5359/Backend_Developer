# Day 17: Interview Questions — Encapsulation, Abstraction and Polymorphism

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 17 notes](day_17_notes.md)  
**Approved mini-project:** Banking Operations Simulator

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. What is encapsulation?
**Answer:** Encapsulation groups data and related methods in a class and provides controlled ways to access or change object state.

**Practical example:** A bank account exposes deposit() and withdraw() rather than asking callers to edit balance arbitrarily.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is abstraction?
**Answer:** Abstraction exposes essential operations while hiding implementation details. Python supports abstract base classes through abc.

**Practical example:** A Payment interface declares pay() while concrete providers implement it.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. What is polymorphism?
**Answer:** Polymorphism allows different objects to respond to the same operation with their own behavior.

**Practical example:** EmailNotification and SMSNotification both implement send().

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. Difference between _name and __name?
**Answer:** A single leading underscore is a convention for internal use. A double leading underscore triggers name mangling. Neither is strong security.

**Practical example:** __balance becomes a mangled attribute name, not encrypted data.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. What is duck typing?
**Answer:** Duck typing focuses on whether an object supports the required behavior rather than requiring a particular declared class.

**Practical example:** A function can accept any object with a send() method.

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A notification service accepts Email and SMS objects. Both have send(), but perform different actions. Which concept is demonstrated?

**Suggested answer:** Polymorphism. The caller uses a common operation while each object provides its own implementation. An abstract base class can define the expected interface.

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Create an account with a validated balance and two notification classes. Explain encapsulation, abstraction and polymorphism.

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

## 5. Mini-project viva — Banking Operations Simulator

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

- **What is encapsulation?** Encapsulation groups data and related methods in a class and provides controlled ways to access or change object state.
- **What is abstraction?** Abstraction exposes essential operations while hiding implementation details. Python supports abstract base classes through abc.
- **What is polymorphism?** Polymorphism allows different objects to respond to the same operation with their own behavior.
- **Difference between _name and __name?** A single leading underscore is a convention for internal use. A double leading underscore triggers name mangling. Neither is strong security.
- **What is duck typing?** Duck typing focuses on whether an object supports the required behavior rather than requiring a particular declared class.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Banking Operations Simulator project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
