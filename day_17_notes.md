# Day 17: Encapsulation, Abstraction and Polymorphism

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations and OOP  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner to Intermediate  
**Prerequisites:** Day 16 — previous OOP lesson  
**Tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Banking Operations Simulator

> **Trainer approach:** First understand the problem, then run the smallest example, inspect the output and only then extend the code. Do not memorize a definition without being able to explain the example.

## 1. Learning objectives

By the end of this lesson, you should be able to:
1. Explain Encapsulation, Abstraction and Polymorphism in simple language.
2. Identify the problem this OOP concept solves.
3. Write and run a small Python example.
4. Explain the important statements and predict the output.
5. Apply the concept in Banking Operations Simulator.
6. Describe one relevant backend development use case.

## 2. Why this concept matters

A banking-style application should not allow unrelated code to change an account balance without validation. Different notification or payment implementations may also provide the same operation in different ways.

A backend developer should be able to read code written by other developers and understand why the code is divided into classes and methods. OOP gives a vocabulary for discussing responsibilities, reusable behavior and object state.

## 3. Key terms

Encapsulation groups data and behavior and controls state changes. Abstraction exposes essential operations while hiding implementation detail. Polymorphism allows different objects to respond to the same operation in their own way.

| Term | Meaning |
|---|---|
| Class | A definition describing the structure and behavior of objects |
| Object | One instance created from a class |
| Attribute | Data associated with an object or class |
| Method | A function defined inside a class |
| Instance | A particular object created from a class |
| Responsibility | The work that a class or method is expected to perform |

## 4. Start with the problem before the syntax

Ask these questions before writing code:
1. What real-world concept are we representing?
2. What information must be stored?
3. What actions must be supported?
4. Which information belongs to one object?
5. Which behavior can be reused?
6. What invalid situations must be prevented?
7. How will we prove the result is correct?

This small analysis prevents you from creating classes without a clear purpose.

## 5. Main worked example

Save this code in `day_17/main.py` and run `python main.py`.

```python
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def get_balance(self):
        return self.__balance

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("EMAIL:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)

def notify(channel, message):
    channel.send(message)

account = BankAccount(1000)
account.deposit(250)
print(account.get_balance())
notify(EmailNotification(), "Deposit complete")
notify(SMSNotification(), "Deposit complete")
```

### Expected output

```text
1250\nEMAIL: Deposit complete\nSMS: Deposit complete
```

### Read the code step by step

1. BankAccount groups balance data and the methods that operate on it; this is encapsulation.
2. The double underscore triggers name mangling, not encryption or strong security.
3. deposit() validates the amount before changing the stored balance.
4. Notification is an abstract base class; @abstractmethod declares an operation concrete subclasses must implement.
5. EmailNotification and SMSNotification implement send() differently. notify() can work with either object, demonstrating polymorphism.

### Run it yourself

1. Create the file in VS Code.
2. Type the code rather than blindly copying it.
3. Save the file.
4. Open the integrated terminal.
5. Run `python main.py`.
6. Compare your output with the expected output.
7. Change one value and run it again.
8. Explain what changed and why.

## 6. Understand the flow

```text
Requirement
    ↓
Identify the objects and responsibilities
    ↓
Define the class or classes
    ↓
Create objects
    ↓
Call methods / exchange objects
    ↓
Inspect output and validate behavior
```

The flow is a thinking guide, not a Python command sequence. A small exercise may use only one class. A larger application may use multiple cooperating objects.

## 7. How to read and debug OOP code

When an example does not behave as expected:
1. Check the class name and spelling.
2. Check indentation inside the class.
3. Check that the object was created.
4. Check the values passed to the initializer or method.
5. Print the relevant attribute values.
6. Check whether a method changes the intended object.
7. Re-run the smallest reproducible example.

| Symptom | Likely area to inspect |
|---|---|
| AttributeError | Attribute or method name, object initialization |
| TypeError | Number or order of arguments |
| NameError | Variable or class name is not defined in the current scope |
| Wrong object's value changes | Object reference passed to the method |
| Method does not override | Method name or inheritance declaration |
| Abstract class cannot be instantiated | Required abstract method is not implemented |

Do not fix several unrelated lines at once. Identify the exact failing statement first.

## 8. Industry scenario

A banking-style application should not allow unrelated code to change an account balance without validation. Different notification or payment implementations may also provide the same operation in different ways.

A professional implementation would also consider input validation, access control, error handling, tests, database persistence and concurrent requests. The class examples in this lesson are learning exercises, not production-ready services.

## 9. When to use the concept and when to avoid overengineering

- Use a class when related state and behavior need a clear reusable structure.
- Keep a simple value as a variable when a class adds no meaningful behavior.
- Give each class a focused responsibility.
- Avoid a class hierarchy just to save a few lines.
- Prefer composition when one object contains or manages another object.
- Add abstractions when they clarify a real variation or contract, not merely to make the code look advanced.

## 10. Common beginner mistakes

| Mistake | Why it causes trouble | Better approach |
|---|---|---|
| Memorizing OOP terms without running code | Definitions are hard to apply | Trace a real example |
| Creating one huge class | Responsibilities become mixed | Split meaningful responsibilities |
| Duplicating common behavior | Updates must be repeated | Reuse a parent class when an is-a relationship exists |
| Using inheritance for every relationship | Creates confusing hierarchies | Use composition for has-a relationships |
| Ignoring object state | Methods may update the wrong instance | Inspect attributes before and after a call |
| Assuming Python underscore names are secure | Naming conventions are not access-control security | Use application-level authorization and safe design |
| Writing a method without a clear purpose | Class becomes difficult to understand | Name methods after meaningful actions |

## 11. Guided practice

Complete each exercise in a separate small file or notebook cell.

### Exercise A — identify the design

Write down:
- The class or classes you need.
- The data each class should store.
- The methods each class should expose.
- One invalid input or state to test.

### Exercise B — modify the example

Change one attribute, method or class responsibility. Run the code again and record the changed output.

### Exercise C — explain it aloud

Explain the code as if you are teaching a fresher:
1. What problem does it solve?
2. What does each class represent?
3. Which object is being used?
4. Which method is called?
5. What output proves it worked?

## 12. Approved mini-project — Banking Operations Simulator

**Objective:** Build a small, understandable Python application using the day's OOP concept.

### Functional requirements

1. Create BankAccount with a name and an internally managed balance.
2. Implement deposit(), withdraw() and get_balance().
3. Reject non-positive amounts and insufficient funds.
4. Create an abstract Notification class with send().
5. Implement EmailNotification and SMSNotification.
6. Write one function that accepts either notification object and calls send().

### Suggested project structure

```text
projects/day_17/
├── README.md
├── main.py
├── models.py
└── tests/
    └── manual_test_cases.md
```

For the first attempt, you may keep the code in one file. Split it into modules only after the working version is understood.

### Implementation milestones

| Milestone | Work | Evidence |
|---|---|---|
| 1 | Read the requirement and list the classes | Short design notes |
| 2 | Implement the smallest class or object | First successful run |
| 3 | Add required attributes and methods | Updated terminal output |
| 4 | Implement the main workflow | Demonstration run |
| 5 | Test normal and invalid cases | Test-case table |
| 6 | Explain the design | README and short walkthrough |

### Validation checklist

- [ ] Valid deposits and withdrawals update the balance.
- [ ] Invalid operations do not change the balance.
- [ ] Both notification classes work through the same function.
- [ ] The learner explains that name mangling is not a security boundary.

### Submission requirements

- Source code.
- README with problem statement and run instructions.
- At least three test cases.
- Expected and actual output.
- Short explanation of each class and method.
- Limitations and one possible future improvement.

### Optional extension

Add one additional requirement only after all core requirements pass. Explain why the extension belongs in the existing class or requires a new responsibility.

## 13. AI-assisted learning guide

Use AI as a mentor, not as a replacement for your own implementation.

| Assistance level | Prompt |
|---|---|
| Hint | Give one small hint for Banking Operations Simulator; do not give the solution |
| Plan | Break the project into small implementation steps |
| Example | Show a tiny example of the specific concept only |
| Guided implementation | Help with one method, then wait for my output |
| Explanation | Explain each statement and object state |
| Debugging | Inspect my exact error and identify the root cause |
| Review | Compare my implementation with the requirements and tests |

**Planning prompt**

"Help me plan Banking Operations Simulator. List the classes, responsibilities, attributes, methods, test cases and implementation order. Do not write the complete solution."

**Implementation prompt**

"Guide me through the first step only. Explain the code and wait until I run it before moving to the next step."

**Debugging prompt**

"Here is my code, input and exact error. Identify the failing statement, explain the cause and suggest the smallest correction. Do not rewrite the whole project."

**Review prompt**

"Review my implementation against the approved requirements. Identify missing behavior, edge cases and design problems. Explain each finding before suggesting a change."

## 14. Daily quiz — multiple-choice questions

### Q1. Which statement best describes today's main concept?
A. It is a Python feature used to organize related data and behavior.  
B. It removes the need for testing.  
C. It automatically saves every object to PostgreSQL.  
D. It replaces all functions in Python.

**Correct answer: A.** The concept helps organize related state and behavior. It does not automatically provide database persistence or remove the need for tests.

### Q2. What should you inspect when the output is incorrect?
A. Only the filename.  
B. Object creation, values, method calls and state changes.  
C. Delete the class.  
D. Ignore the output.

**Correct answer: B.** OOP behavior depends on the object, its data and the method being called.

### Q3. Which is the best project practice?
A. Put all behavior into one giant method.  
B. Avoid all validation.  
C. Give each class a clear responsibility and test normal and invalid cases.  
D. Store secrets in the source code.

**Correct answer: C.** Clear responsibilities and validation make the project easier to understand and maintain.

### Q4. Why should you not treat the example as production-ready?
A. Python cannot run classes.  
B. A classroom example does not include all production concerns such as persistence, security, concurrency and monitoring.  
C. Methods cannot be tested.  
D. Objects cannot store data.

**Correct answer: B.** The demonstration teaches one concept; production systems need additional engineering controls.

### Q5. What is the strongest evidence that your mini-project is complete?
A. A project folder exists.  
B. You watched a video.  
C. The code is long.  
D. Required scenarios pass, output is recorded and you can explain the implementation.

**Correct answer: D.** Completion requires working behavior and the ability to explain and verify it.

## 15. Interview preparation

**Q1. Explain encapsulation, abstraction and polymorphism in your own words.**  
**Answer:** Encapsulation groups data and behavior and controls state changes. Abstraction exposes essential operations while hiding implementation detail. Polymorphism allows different objects to respond to the same operation in their own way.

**Practical follow-up:** Explain the main worked example and identify the class, object, method and state involved.

**Q2. Where can this concept help a backend developer?**  
**Answer:** It helps structure reusable application code and model business responsibilities. Django uses Python classes extensively, so a strong OOP foundation makes framework code easier to understand.

**Q3. What is one mistake a beginner should avoid?**  
**Answer:** Do not add complexity without a clear requirement. Keep responsibilities understandable, validate inputs and test the behavior.

**Follow-up:** What would you add before using this learning example in a production service?  
**Answer:** Tests, error handling, authorization where needed, safe data persistence, configuration management, logging and operational monitoring.

## 16. Day completion checklist

- [ ] Read the lesson and explain the key terms.
- [ ] Run the worked example successfully.
- [ ] Explain the important statements.
- [ ] Complete the guided exercises.
- [ ] Build Banking Operations Simulator.
- [ ] Validate normal and invalid scenarios.
- [ ] Complete all five MCQs.
- [ ] Answer the interview questions without copying.
- [ ] Submit source code, README and evidence.

**Next lesson:** Day 18 — Complete OOP Integration, Revision and Practical Design.

