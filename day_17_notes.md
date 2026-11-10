# Day 17: Encapsulation, Abstraction and Polymorphism

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 13–16 — OOP fundamentals and inheritance  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Banking Operations Simulator

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain encapsulation and why state should be changed through meaningful methods.
2. Understand Python's public, protected-by-convention and name-mangled attributes.
3. Explain abstraction as exposing an interface while hiding implementation details.
4. Create an abstract base class using the abc module.
5. Explain polymorphism using a shared method name.
6. Use overriding to provide different behavior.
7. Choose between these concepts in a practical design.
8. Build a small Banking Operations Simulator.

## 2. One business problem, three design ideas

Imagine a banking application.

A bank account has a balance. The application should not let every part of the program change that balance to an invalid value.

The application may support multiple payment methods, but each payment method should provide a common operation such as `pay()`.

The application should allow callers to use that operation without needing to know every internal processing step.

These requirements introduce three OOP concepts:

- **Encapsulation:** group data and the operations that control it.
- **Abstraction:** expose the essential operation and hide unnecessary implementation detail.
- **Polymorphism:** different objects respond to the same operation in their own way.

## 3. Encapsulation

Encapsulation means grouping related data and methods together and controlling how the object's state is changed.

Think of a bank account:
- It stores a balance.
- It supports deposit.
- It supports withdrawal.
- It should reject invalid transactions.

A weak design allows arbitrary code to assign any balance. A better design provides methods that validate changes.

### 3.1 First example without controlled updates

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(1000)
account.balance = -5000

print(account.balance)
```

Output: `-5000`.

The assignment is allowed. The class has not protected its business rule.

### 3.2 Control changes through methods

```python
class BankAccount:
    def __init__(self, opening_balance):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)
```

Output: `1300`.

The methods enforce the rules for normal use. However, `balance` is still public and can be assigned directly. We will look at Python's naming conventions next.

## 4. Public, protected-by-convention and name-mangled attributes

Python does not use the same strict access modifiers as languages such as Java.

### 4.1 Public attribute

```python
class Employee:
    def __init__(self, name):
        self.name = name

employee = Employee("Anil")
print(employee.name)
```

A public attribute is intended to be accessed directly.

### 4.2 Single leading underscore

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary
```

A single underscore is a convention meaning: "This is an internal implementation detail; use it carefully."

It does not prevent access. It is not a security boundary.

### 4.3 Double leading underscore

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())
```

Output: `1000`.

A double leading underscore triggers name mangling. Python internally changes the attribute name to include the class name, which helps avoid accidental name clashes in subclasses.

It does not encrypt the value or make it impossible to access. Do not describe it as strong security.

## 5. A practical encapsulation example

```python
class BankAccount:
    def __init__(self, account_holder, opening_balance):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.account_holder = account_holder
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Asha", 5000)
account.deposit(1000)
account.withdraw(750)
print(account.get_balance())
```

Output: `5250`.

The balance is stored as `__balance`. The class provides methods that validate deposits and withdrawals.

Important: name mangling is not a substitute for application security. It does not stop a malicious user from accessing data through an exposed API. Authentication, authorization, database permissions and secure application design are separate concerns.

## 6. Abstraction

Abstraction means exposing the essential operations while hiding implementation details that callers do not need to manage.

Think of an ATM:
- You choose withdraw.
- You enter an amount.
- The system performs internal checks and processing.
- You receive the result.

You do not need to know every internal database or network operation to use the withdraw operation.

In Python, abstraction can be represented using abstract base classes and abstract methods.

## 7. Abstract base classes

Python's `abc` module provides tools for defining abstract base classes.

An abstract method declares an operation that a concrete child class must implement before it can be instantiated.

### 7.1 Basic example

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

Explanation:
- ABC is the base class for abstract base classes.
- `@abstractmethod` marks a method that concrete subclasses must implement.
- `pass` is a placeholder; it is not the implementation.

Trying to create `Payment()` directly raises TypeError because the abstract method has not been implemented.

### 7.2 Implement the abstract method

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("Processing card payment:", amount)

class UpiPayment(Payment):
    def pay(self, amount):
        print("Processing UPI payment:", amount)

card = CardPayment()
upi = UpiPayment()

card.pay(500)
upi.pay(750)
```

Output:

```text
Processing card payment: 500
Processing UPI payment: 750
```

Both child classes satisfy the abstract contract by implementing `pay`.

This is a teaching simulation, not a real payment gateway integration.

## 8. Polymorphism

Polymorphism means that different object types can be used through a common operation, while each object can provide its own behavior.

The word can be remembered as "many forms".

### 8.1 Same method name, different behavior

```python
class Developer:
    def work(self):
        print("Writing and testing code")

class Manager:
    def work(self):
        print("Planning and reviewing work")

class HR:
    def work(self):
        print("Managing recruitment activities")

employees = [Developer(), Manager(), HR()]

for employee in employees:
    employee.work()
```

Output:

```text
Writing and testing code
Planning and reviewing work
Managing recruitment activities
```

The loop does not need to know the exact class of each object. It calls the shared method name, and each object responds with its own implementation.

### 8.2 Polymorphism with inheritance

```python
class Employee:
    def work(self):
        print("Employee performs assigned work")

class Developer(Employee):
    def work(self):
        print("Developer writes software")

class Manager(Employee):
    def work(self):
        print("Manager leads a team")

roles = [Developer(), Manager(), Employee()]

for role in roles:
    role.work()
```

The child methods override the parent method. This is runtime polymorphism in a common OOP teaching example.

### 8.3 Duck typing

Python also supports polymorphism through duck typing. If an object supports the operation the caller needs, the caller can often use it without requiring a shared parent class.

```python
class PDFReport:
    def export(self):
        print("Exporting PDF report")

class CSVReport:
    def export(self):
        print("Exporting CSV report")

def export_report(report):
    report.export()

export_report(PDFReport())
export_report(CSVReport())
```

Output:

```text
Exporting PDF report
Exporting CSV report
```

The function only requires an object that provides an `export()` method.

## 9. Compare encapsulation, abstraction and polymorphism

| Concept | Main question | Example |
|---|---|---|
| Encapsulation | How do we group data and control valid changes? | BankAccount.deposit() |
| Abstraction | What operation should the caller see? | Payment.pay() contract |
| Polymorphism | How can different objects support the same operation differently? | CardPayment.pay() and UpiPayment.pay() |

They solve different design problems. Do not use the terms as if they mean the same thing.

## 10. Complete mini-project — Banking Operations Simulator

### 10.1 Requirements

Build a small local simulation that:
1. Creates a bank account.
2. Stores the balance as an internal attribute.
3. Allows deposits and withdrawals.
4. Rejects invalid amounts.
5. Defines an abstract payment method.
6. Implements two payment types.
7. Uses one function to process different payment objects.

This project does not connect to a real bank or payment provider. It is designed to teach OOP behavior and validation.

### 10.2 Project structure

```text
day_17_banking_simulator/
├── main.py
└── README.md
```

### 10.3 Complete runnable code

```python
from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, account_holder, opening_balance):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.account_holder = account_holder
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment must be positive")
        print("Card payment simulated:", amount)


class UpiPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment must be positive")
        print("UPI payment simulated:", amount)


def process_payment(payment_method, amount):
    payment_method.pay(amount)


account = BankAccount("Asha", 5000)

print("Opening balance:", account.get_balance())
account.deposit(1000)
print("After deposit:", account.get_balance())
account.withdraw(750)
print("After withdrawal:", account.get_balance())

card = CardPayment()
upi = UpiPayment()

process_payment(card, 500)
process_payment(upi, 300)
```

### 10.4 Expected output

```text
Opening balance: 5000
After deposit: 6000
After withdrawal: 5250
Card payment simulated: 500
UPI payment simulated: 300
```

### 10.5 Walkthrough

1. BankAccount groups account data and operations.
2. The balance is stored in a name-mangled attribute.
3. deposit validates the amount before adding it.
4. withdraw validates the amount and checks available balance.
5. get_balance provides a controlled read operation.
6. PaymentMethod defines an abstract pay contract.
7. CardPayment implements that contract.
8. UpiPayment implements the same contract differently.
9. process_payment accepts an object that supports pay.
10. Passing either payment object demonstrates polymorphism.

### 10.6 Test cases

| Test | Action | Expected result |
|---|---|---|
| 1 | Open account with 5000 | Account created |
| 2 | Open account with -1 | ValueError |
| 3 | Deposit 1000 | Balance becomes 6000 |
| 4 | Deposit 0 | ValueError |
| 5 | Withdraw 750 | Balance becomes 5250 |
| 6 | Withdraw more than balance | ValueError |
| 7 | Instantiate PaymentMethod | TypeError |
| 8 | Use CardPayment.pay | Card simulation message |
| 9 | Use UpiPayment.pay | UPI simulation message |

## 11. Security and production limitations

This is an in-memory teaching simulator. It is not a production banking system.

A real banking application also needs:
- Authentication and authorization.
- Secure database storage.
- Database transactions and concurrency controls.
- Audit records.
- Idempotency and duplicate request protection.
- Secure communication.
- Provider integration and verification.
- Fraud detection and operational monitoring.

Do not infer that a private-looking Python attribute protects real financial information. OOP encapsulation is a code-organization and state-management technique, not a complete security system.

## 12. Common mistakes and troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Cannot instantiate abstract class | An abstract method is not implemented | Implement every required abstract method |
| AttributeError for balance | Wrong attribute name or method | Use the intended getter or inspect spelling |
| Negative balance appears | Validation missing or state changed outside methods | Enforce rules in state-changing operations |
| Child does not satisfy abstract contract | Method name/signature is wrong | Match the abstract operation |
| Polymorphic function fails | Object does not provide the expected method | Check the required interface |
| Think double underscore is encryption | Misunderstanding name mangling | Treat it as a naming mechanism, not security |

## 13. Practice exercises

1. Add a transfer method to BankAccount that withdraws from one account and deposits into another. Validate both operations.
2. Create a Notification abstract base class with send(message).
3. Implement EmailNotification and SMSNotification.
4. Write a function that accepts any notification object and calls send.
5. Create a Shape abstract class with area(), then implement Circle and Rectangle.
6. Demonstrate a public attribute, a single-underscore attribute and a double-underscore attribute. Explain the difference.
7. Explain why name mangling does not secure an API.

## 14. Interview questions

**1. What is encapsulation?**  
Grouping data and behavior together and providing controlled ways to interact with object state.

**2. What is abstraction?**  
Exposing essential operations while hiding implementation details that callers do not need.

**3. What is polymorphism?**  
Different object types supporting a common operation with type-specific behavior.

**4. What does a single underscore mean in Python?**  
It is a convention indicating an internal or non-public implementation detail.

**5. What does a double leading underscore do?**  
It triggers name mangling to reduce accidental name clashes; it is not encryption.

**6. What is an abstract class?**  
A class that defines an interface or shared contract and may not be instantiated until required abstract methods are implemented.

**7. What is an abstract method?**  
A method marked with @abstractmethod that concrete subclasses are expected to implement.

**8. What is duck typing?**  
Using an object based on the operations it supports rather than requiring a specific class.

**9. Difference between overriding and overloading?**  
Overriding replaces inherited behavior in a child class. Python does not support traditional signature-based method overloading in the same way as some statically typed languages; default arguments or dispatch techniques are commonly used.

**10. Is encapsulation the same as security?**  
No. Encapsulation organizes access to object state. Application security requires separate controls.

## 15. MCQs

**Q1. Which concept groups data and methods and controls state changes?**  
A. Encapsulation  
B. Looping  
C. Compilation  
D. Importing  
**Answer: A.** Encapsulation groups state and behavior.

**Q2. Which decorator marks an abstract method?**  
A. @classmethod  
B. @abstractmethod  
C. @staticmethod  
D. @property  
**Answer: B.** It marks an operation that concrete subclasses must implement.

**Q3. Different classes implement the same pay() operation. Which concept is demonstrated?**  
A. Polymorphism  
B. File handling  
C. Recursion  
D. Indexing  
**Answer: A.** Different objects respond to the same operation in their own way.

**Q4. Does a double underscore make an attribute encrypted?**  
A. Yes  
B. No  
C. Only in Django  
D. Only on Windows  
**Answer: B.** It triggers name mangling, not encryption.

**Q5. What does duck typing focus on?**  
A. Object capabilities and supported operations  
B. Variable spelling only  
C. Database size  
D. File permissions  
**Answer: A.** The caller uses the operation an object provides.

**Q6. What happens if an abstract method is not implemented by a concrete child?**  
A. It can remain abstract and cannot be instantiated  
B. Python invents an implementation  
C. It returns zero  
D. It deletes the parent class  
**Answer: A.** The class remains abstract until the required method is implemented.

## 16. Daily completion checklist

- [ ] I can explain encapsulation.
- [ ] I understand public, underscore and name-mangled attributes.
- [ ] I can explain why name mangling is not security.
- [ ] I can explain abstraction.
- [ ] I can define an abstract base class.
- [ ] I can implement an abstract method.
- [ ] I can explain polymorphism and duck typing.
- [ ] I completed Banking Operations Simulator.
- [ ] I tested invalid deposits and withdrawals.

**Next lesson:** Day 18 — Complete OOP Integration and Revision.
