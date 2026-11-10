# Day 14: Interview Questions — Constructors, __init__, self and Instance Variables

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 14 notes](day_14_notes.md)  
**Approved mini-project:** Employee Profile System

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. What is __init__()?
**Answer:** __init__() is a special initializer that Python calls when an object is initialized. It is commonly used to assign initial attribute values.

**Practical example:** Every new Employee receives an ID, name and department at creation.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is self?
**Answer:** self refers to the current instance inside an instance method. It lets the method access or update that object's attributes.

**Practical example:** self.name stores the name on the current employee object.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. Is self a reserved keyword?
**Answer:** No. It is a convention, but Python developers should follow it for readability.

**Practical example:** The interpreter passes the instance as the first argument to an instance method.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. What is an instance variable?
**Answer:** An instance variable is data associated with one particular object. Different objects can have different values.

**Practical example:** employee1.salary and employee2.salary can differ.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. Why use an initializer?
**Answer:** It initializes objects consistently and reduces the chance that required attributes are forgotten.

**Practical example:** Employee(101, 'Asha') supplies required values during object creation.

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A system requires every employee object to have an ID and name. Why use __init__?

**Suggested answer:** The initializer receives required values when the object is created and assigns them to instance attributes. This helps ensure each object begins in a consistent state.

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Create two employee objects and trace how self.name receives a different value for each object.

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

## 5. Mini-project viva — Employee Profile System

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

- **What is __init__()?** __init__() is a special initializer that Python calls when an object is initialized. It is commonly used to assign initial attribute values.
- **What is self?** self refers to the current instance inside an instance method. It lets the method access or update that object's attributes.
- **Is self a reserved keyword?** No. It is a convention, but Python developers should follow it for readability.
- **What is an instance variable?** An instance variable is data associated with one particular object. Different objects can have different values.
- **Why use an initializer?** It initializes objects consistently and reduces the chance that required attributes are forgotten.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Employee Profile System project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
