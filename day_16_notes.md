# Day 16: Inheritance and Method Overriding

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 13–15 — Classes, objects, initialization and methods  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Employee Role Management System

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why inheritance is useful.
2. Identify a parent/base class and child/derived class.
3. Reuse parent attributes and methods in a child class.
4. Add child-specific attributes and methods.
5. Override a parent method.
6. Use `super()` to call parent behavior.
7. Understand the basic method resolution order.
8. Recognize when inheritance is appropriate and when composition is better.
9. Build an Employee Role Management System.

## 2. Start with a real-world problem

Imagine a company has three employee types:

- Developer
- Manager
- HR Executive

All employees have common details:
- Employee ID
- Name
- Department

But each role also has its own behavior:
- A developer writes code and works with technical tasks.
- A manager leads a team and reviews progress.
- An HR executive manages recruitment and employee records.

A first attempt might define three independent classes and repeat the common attributes and methods. That creates duplication.

Inheritance allows a child class to reuse common behavior from a parent class and add or customize its own behavior.

## 3. What is inheritance?

**Inheritance** is an OOP feature in which a new class can reuse and extend the attributes and methods of an existing class.

Vocabulary:

| Term | Meaning |
|---|---|
| Parent class | Existing class whose behavior is inherited |
| Base class | Another name for parent class |
| Child class | New class that inherits from another class |
| Derived class | Another name for child class |
| Inheritance | Reuse and extension relationship |

Example:
- Employee is the parent class.
- Developer is a child class.
- Manager is another child class.

A Developer is an Employee. This is an **is-a** relationship.

## 4. First inheritance example

```python
class Employee:
    def show_company(self):
        print("Company: TechPhile")

class Developer(Employee):
    def write_code(self):
        print("Developer writes code")

developer = Developer()

developer.show_company()
developer.write_code()
```

Output:

```text
Company: TechPhile
Developer writes code
```

Explanation:
1. Employee defines `show_company`.
2. Developer(Employee) declares that Developer inherits from Employee.
3. Developer defines its own `write_code` method.
4. We create an object from Developer.
5. The object can call the child method.
6. It can also call the inherited parent method.

The child does not need to copy the parent method.

## 5. Parent and child with attributes

```python
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_employee(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)

class Developer(Employee):
    def write_code(self):
        print(self.name, "is writing Python code")

developer = Developer(101, "Anil")
developer.display_employee()
developer.write_code()
```

Output:

```text
ID: 101
Name: Anil
Anil is writing Python code
```

The child class inherits the parent's initializer. Therefore, Developer can be initialized with employee_id and name even though it does not define its own `__init__`.

## 6. Add child-specific attributes

A Developer may also have a programming language. A Manager may have a team size.

```python
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_employee(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)

class Developer(Employee):
    def __init__(self, employee_id, name, language):
        self.employee_id = employee_id
        self.name = name
        self.language = language

    def display_language(self):
        print("Language:", self.language)

developer = Developer(101, "Anil", "Python")
developer.display_employee()
developer.display_language()
```

This works, but notice that we repeated the parent's initialization logic. If the parent later adds a new common attribute, we must remember to update the child too.

We can avoid this repetition with `super()`.

## 7. Understand super()

`super()` gives access to the next implementation in the method resolution order. In a simple single-inheritance example, it is commonly used to call the parent class's method.

Improved code:

```python
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_employee(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)

class Developer(Employee):
    def __init__(self, employee_id, name, language):
        super().__init__(employee_id, name)
        self.language = language

    def display_language(self):
        print("Language:", self.language)

developer = Developer(101, "Anil", "Python")
developer.display_employee()
developer.display_language()
```

Output:

```text
ID: 101
Name: Anil
Language: Python
```

Read the important line:

`super().__init__(employee_id, name)`

- Call the next initializer in the method resolution order.
- Pass the common employee values to it.
- The parent initializer stores employee_id and name.
- The child initializer stores language.

This avoids repeating the parent's initialization code.

## 8. Method overriding

A child class can provide its own implementation of a method that already exists in the parent. This is called **method overriding**.

```python
class Employee:
    def work(self):
        print("Employee performs assigned work")

class Developer(Employee):
    def work(self):
        print("Developer writes and tests code")

class Manager(Employee):
    def work(self):
        print("Manager plans and reviews team work")

employee = Employee()
developer = Developer()
manager = Manager()

employee.work()
developer.work()
manager.work()
```

Output:

```text
Employee performs assigned work
Developer writes and tests code
Manager plans and reviews team work
```

The method name is the same, but the child classes provide role-specific behavior.

## 9. Extend parent behavior instead of replacing it completely

Sometimes the child needs the parent's behavior and additional behavior.

```python
class Employee:
    def display(self):
        print("Common employee details")

class Developer(Employee):
    def display(self):
        super().display()
        print("Role: Developer")

developer = Developer()
developer.display()
```

Output:

```text
Common employee details
Role: Developer
```

The child first calls the inherited implementation and then adds its own output.

## 10. Inheritance types: first overview

Python supports several inheritance structures.

### 10.1 Single inheritance

One child inherits from one parent.

```python
class Person:
    pass

class Employee(Person):
    pass
```

### 10.2 Multilevel inheritance

A class inherits from a child class, forming a chain.

```python
class Person:
    def identify(self):
        print("Person")

class Employee(Person):
    def work(self):
        print("Employee works")

class Developer(Employee):
    def code(self):
        print("Developer codes")

developer = Developer()
developer.identify()
developer.work()
developer.code()
```

### 10.3 Multiple inheritance

A child inherits from more than one parent.

```python
class Logger:
    def log(self):
        print("Logging activity")

class Exporter:
    def export(self):
        print("Exporting report")

class ReportService(Logger, Exporter):
    pass

service = ReportService()
service.log()
service.export()
```

Output:

```text
Logging activity
Exporting report
```

Multiple inheritance is supported, but it introduces method resolution and design complexity. Do not use it merely to reuse a few lines.

### 10.4 Hierarchical inheritance

Multiple child classes inherit from one parent.

```python
class Employee:
    def show_company(self):
        print("TechPhile")

class Developer(Employee):
    pass

class Manager(Employee):
    pass
```

Both child types inherit the common behavior.

## 11. Method Resolution Order (MRO)

When a class inherits from multiple parents and methods have the same name, Python needs a predictable rule for finding which implementation to use. This is called Method Resolution Order.

Inspect it with:

```python
print(ReportService.mro())
```

The output lists the order Python searches. In everyday single inheritance, you usually do not need to calculate MRO manually. You should still know that Python follows a defined order rather than randomly selecting a parent.

## 12. When inheritance is useful

Use inheritance when:
- The child really is a specialized form of the parent.
- Several child classes share common data and behavior.
- The child should satisfy the parent's expected interface.
- The shared behavior has a clear common meaning.

Avoid inheritance when:
- The relationship is actually "has-a".
- The parent class is becoming a large collection of unrelated features.
- A child must disable most parent behavior.
- The hierarchy is difficult to explain.
- Composition gives a simpler design.

Example:
- Developer is an Employee: inheritance can fit.
- Employee has a Laptop: composition is usually more suitable. An employee is not a laptop.

## 13. Composition: a quick contrast

```python
class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Employee:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

laptop = Laptop("Dell")
employee = Employee("Anil", laptop)

print(employee.name)
print(employee.laptop.brand)
```

Output:

```text
Anil
Dell
```

Employee contains a reference to a Laptop object. That is composition: a has-a relationship.

## 14. Complete mini-project — Employee Role Management System

### Requirements

Create:
- A base Employee class with ID, name and department.
- A Developer class with programming language.
- A Manager class with team size.
- A shared display method.
- An overridden work method for each role.
- Use super() to initialize common attributes.

### Project structure

```text
day_16_employee_roles/
├── main.py
└── README.md
```

### Complete runnable code

```python
class Employee:
    def __init__(self, employee_id, name, department):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")
        if not name.strip():
            raise ValueError("Employee name cannot be empty")

        self.employee_id = employee_id
        self.name = name.strip()
        self.department = department.strip()

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)

    def work(self):
        print("Employee performs assigned work")


class Developer(Employee):
    def __init__(self, employee_id, name, department, language):
        super().__init__(employee_id, name, department)
        self.language = language

    def work(self):
        print(self.name, "develops software using", self.language)


class Manager(Employee):
    def __init__(self, employee_id, name, department, team_size):
        super().__init__(employee_id, name, department)
        if team_size < 0:
            raise ValueError("Team size cannot be negative")
        self.team_size = team_size

    def work(self):
        print(self.name, "leads a team of", self.team_size)


employees = [
    Developer(101, "Anil", "Engineering", "Python"),
    Manager(102, "Priya", "Engineering", 8),
]

for employee in employees:
    employee.display_details()
    employee.work()
    print("----------------")
```

### Run

```powershell
python main.py
```

Expected behavior:
- First record shows Anil as a Developer and describes Python development.
- Second record shows Priya as a Manager and describes team leadership.
- Both records use the common employee display method.

### Test cases

| Test | Action | Expected |
|---|---|---|
| 1 | Create Developer with valid data | Object created |
| 2 | Create Manager with valid data | Object created |
| 3 | Use employee ID 0 | ValueError |
| 4 | Use blank name | ValueError |
| 5 | Use negative team size | ValueError |
| 6 | Call Developer.work | Developer-specific output |
| 7 | Call Manager.work | Manager-specific output |
| 8 | Call display_details on both | Common details displayed |

## 15. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| TypeError in child initializer | Parent arguments were not supplied correctly | Check super().__init__ arguments |
| Parent attributes missing | Parent initializer was never called | Use super().__init__ when required |
| Parent method runs instead of child method | Child method name/signature differs | Check exact method name |
| AttributeError for child attribute | Child initializer did not assign it | Assign the child-specific attribute |
| Unexpected method selected | Inheritance hierarchy or MRO differs from assumption | Inspect ClassName.mro() |
| Deep hierarchy is hard to follow | Too many inheritance layers | Simplify or use composition |

## 16. Practice exercises

1. Create a Vehicle parent class and Car child class.
2. Add a Bike child class with its own overridden start method.
3. Create a Person → Employee → Developer multilevel hierarchy.
4. Create a Printer and Scanner class and combine them in an OfficeMachine using multiple inheritance.
5. Build an Employee with a Laptop object using composition.
6. Explain why a Developer is an Employee but an Employee is not a Laptop.
7. Override a display method and call the parent method using super().

## 17. Interview questions

**1. What is inheritance?**  
A mechanism where a child class reuses and extends attributes and methods from a parent class.

**2. What is a parent class?**  
The base class whose behavior is inherited.

**3. What is method overriding?**  
A child class provides its own implementation of an inherited method with the same method name.

**4. What is super()?**  
A proxy that provides access to the next class in the method resolution order. In simple inheritance it is commonly used to call parent behavior.

**5. What is single inheritance?**  
One child class inherits from one parent class.

**6. What is multiple inheritance?**  
One class inherits from more than one parent class.

**7. What is MRO?**  
Method Resolution Order is the order Python follows to find attributes and methods in an inheritance hierarchy.

**8. Difference between inheritance and composition?**  
Inheritance models an is-a relationship; composition models a has-a relationship.

**9. Can a child class override an initializer?**  
Yes. If it defines its own __init__, it should call super().__init__ when it needs the parent's initialization.

**10. Why should inheritance not be overused?**  
It can create tight coupling and complicated hierarchies. Composition may be simpler for has-a relationships.

## 18. MCQs

**Q1. Which syntax declares inheritance?**  
A. `class Developer(Employee):`  
B. `class Developer -> Employee:`  
C. `inherit Developer Employee`  
D. `Developer extends Employee`  
**Answer: A.** The parent class is placed in parentheses.

**Q2. Which function commonly calls parent initialization?**  
A. print()  
B. super().__init__()  
C. self.parent()  
D. class()  
**Answer: B.** super() accesses the next initializer in the MRO.

**Q3. What is method overriding?**  
A. Deleting every parent method  
B. Child providing its own implementation of an inherited method  
C. Renaming a class  
D. Importing a module  
**Answer: B.** The child customizes inherited behavior.

**Q4. An Employee has a Laptop. Which relationship is this?**  
A. Is-a  
B. Has-a  
C. Is-not-a  
D. Overrides  
**Answer: B.** The employee contains or uses a laptop object.

**Q5. What does MRO stand for?**  
A. Method Runtime Object  
B. Method Resolution Order  
C. Main Return Operation  
D. Multiple Record Output  
**Answer: B.** It describes the order Python searches for methods.

**Q6. Which inheritance form has two or more parent classes?**  
A. Single  
B. Multiple  
C. Hierarchical  
D. None  
**Answer: B.** Multiple inheritance uses more than one base class.

## 19. Daily completion checklist

- [ ] I can explain inheritance.
- [ ] I can identify parent and child classes.
- [ ] I can reuse parent attributes and methods.
- [ ] I can add child-specific data.
- [ ] I can use super().
- [ ] I can override a method.
- [ ] I know the basic inheritance types.
- [ ] I can explain MRO at a high level.
- [ ] I can distinguish inheritance from composition.
- [ ] I completed Employee Role Management System.

**Next lesson:** Day 17 — Encapsulation, Abstraction and Polymorphism.
