# Day 15: Interview Questions — Instance Methods, Class Methods and Static Methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Related class notes:** [Day 15 notes](day_15_notes.md)  
**Approved mini-project:** Employee Utility Manager

## 1. How to answer OOP interview questions

For each answer, use this structure:
1. Give a direct definition in one or two sentences.
2. Explain the idea using a small example.
3. Explain why a backend developer needs it.
4. Mention one limitation or common mistake.
5. State how you would test the behavior.

Avoid memorizing a paragraph without understanding the code.

## 2. Core technical questions

### Q1. What is an instance method?
**Answer:** An instance method receives the current object through self. It is appropriate when behavior uses or changes instance attributes.

**Practical example:** increase_salary() changes one employee's salary.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q2. What is a class method?
**Answer:** A class method is declared with @classmethod and receives the class through cls. It is useful for class-level operations and alternative constructors.

**Practical example:** change_company() updates a class attribute.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q3. What is a static method?
**Answer:** A static method is declared with @staticmethod and receives no automatic self or cls argument. It is useful for related utility behavior.

**Practical example:** is_valid_salary(value) can validate a value without object state.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q4. What is the difference between self and cls?
**Answer:** self refers to one object instance; cls refers to the class itself.

**Practical example:** An instance method reads one employee's salary; a class method updates a shared company setting.

**Follow-up:** Give a real project example and explain how you would verify it.

### Q5. What is an alternative constructor?
**Answer:** A class method that creates and returns an instance using an alternative input format.

**Practical example:** from_text('Asha,Engineering') parses a string and returns cls(name, department).

**Follow-up:** Give a real project example and explain how you would verify it.

## 3. Scenario-based question

**Scenario:** A backend application needs to display one employee's salary, change a company-wide setting and validate a salary number. Which method type fits each?

**Suggested answer:** Use an instance method to display one employee's salary, a class method to change a class-level company setting, and a static method for a related validation utility that needs neither instance nor class state.

**Follow-up questions**
1. Which class or object is responsible for the behavior?
2. What values should be validated?
3. What should happen when the input is invalid?
4. How would you demonstrate that the behavior is correct?
5. What would need to change before production use?

## 4. Practical coding discussion

**Task:** Write one instance method, one class method and one static method. Explain why each uses its chosen method type.

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

## 5. Mini-project viva — Employee Utility Manager

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

- **What is an instance method?** An instance method receives the current object through self. It is appropriate when behavior uses or changes instance attributes.
- **What is a class method?** A class method is declared with @classmethod and receives the class through cls. It is useful for class-level operations and alternative constructors.
- **What is a static method?** A static method is declared with @staticmethod and receives no automatic self or cls argument. It is useful for related utility behavior.
- **What is the difference between self and cls?** self refers to one object instance; cls refers to the class itself.
- **What is an alternative constructor?** A class method that creates and returns an instance using an alternative input format.

## 8. Interview practice checklist

- [ ] I can answer each core question without reading.
- [ ] I can write a small example on a whiteboard or editor.
- [ ] I can explain the output.
- [ ] I can describe a real backend use case.
- [ ] I can identify one limitation or mistake.
- [ ] I can explain my Employee Utility Manager project honestly.

**Trainer note:** Ask the learner to explain the code in their own words. If they cannot explain an attribute, method or object reference, return to the related class note and rerun the example.
