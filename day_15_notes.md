# Day 15: Instance Methods, Class Methods and Static Methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 13–14 — Classes, Objects and Initialization  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Employee Utility Manager

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why classes contain different method types.
2. Define and call instance methods.
3. Explain self.
4. Define class methods with `@classmethod`.
5. Explain cls.
6. Define static methods with `@staticmethod`.
7. Compare all three method types.
8. Choose a method type based on the data an operation needs.
9. Build an Employee Utility Manager using all three.

## 2. A real-world requirement

Imagine an organization has hundreds of employees.

Each employee has personal data:
- Employee ID.
- Name.
- Department.
- Monthly salary.

The organization also has shared data:
- Company name.
- Default work location.
- Company-wide configuration.

The application needs operations:
- Display one employee's profile.
- Calculate one employee's annual salary.
- Change the company's name.
- Validate whether a salary is non-negative.

Not every operation needs the same kind of information. This is why Python provides instance, class and static methods.

## 3. Compare the three method types

| Method type | First parameter supplied automatically | Decorator | Typical responsibility |
|---|---|---|---|
| Instance method | `self` | None | Work with one object's state |
| Class method | `cls` | `@classmethod` | Work with class-level state or create instances |
| Static method | None | `@staticmethod` | Utility logic needing neither instance nor class state |

The key question is: what information does the operation need?

## 4. Instance methods

An instance method works with a particular object. It receives that object through `self`.

### 4.1 Basic example

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self.department)

employee1 = Employee("Anil", "IT")
employee2 = Employee("Priya", "HR")

employee1.display_details()
employee2.display_details()
```

Output:

```text
Name: Anil
Department: IT
Name: Priya
Department: HR
```

The method is defined once. When called on employee1, self refers to employee1. When called on employee2, self refers to employee2.

### 4.2 Instance method changes object state

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def change_department(self, new_department):
        self.department = new_department

employee = Employee("Anil", "IT")
print(employee.department)

employee.change_department("Engineering")
print(employee.department)
```

Output:

```text
IT
Engineering
```

The method changes the object that called it.

### 4.3 Instance method returns a calculation

```python
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

employee = Employee("Anil", 40000)
print(employee.annual_salary())
```

Output: `480000`.

The method uses salary already stored on the employee object.

## 5. Class attributes

A class attribute is defined directly in the class body.

```python
class Employee:
    company_name = "TechPhile"

    def __init__(self, name):
        self.name = name

employee1 = Employee("Anil")
employee2 = Employee("Priya")

print(Employee.company_name)
print(employee1.company_name)
print(employee2.company_name)
```

Output:

```text
TechPhile
TechPhile
TechPhile
```

Both objects can read the class attribute. It is useful for information shared by instances, but avoid storing per-employee values as class attributes.

Try this:

```python
employee1.company_name = "City Services"

print(employee1.company_name)
print(employee2.company_name)
print(Employee.company_name)
```

Output:

```text
City Services
TechPhile
TechPhile
```

The assignment created an instance attribute for employee1. It did not change the class attribute.

## 6. Class methods

A class method receives the class as its first argument. The conventional parameter name is `cls`.

Use `@classmethod`.

### 6.1 Basic syntax

```python
class Employee:
    company_name = "TechPhile"

    @classmethod
    def show_company(cls):
        print("Company:", cls.company_name)

Employee.show_company()
```

Output: `Company: TechPhile`.

Step by step:
1. `@classmethod` marks the method as a class method.
2. Python supplies the class as the first argument.
3. `cls` refers to the class.
4. `cls.company_name` reads the class attribute.
5. The method is called through Employee.

### 6.2 Update class-level data

```python
class Employee:
    company_name = "TechPhile"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

Employee.change_company_name("TechPhile Technologies")
print(Employee.company_name)
```

Output: `TechPhile Technologies`.

This changes the class attribute. Instances that have not created their own attribute with the same name will see the updated value.

### 6.3 Why cls instead of self?

- self refers to one instance.
- cls refers to the class itself.

A class method can be called through an instance too, but the first argument remains the class. Calling through the class is generally clearer for class-wide operations.

## 7. Class methods as alternate constructors

A class method can create an object using an alternate input format.

Suppose a simple training file provides a row like:

`101,Anil,IT,45000`

We want to turn it into an Employee object.

```python
class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    @classmethod
    def from_row(cls, row):
        employee_id, name, department, salary = row.split(",")
        return cls(int(employee_id), name, department, float(salary))

employee = Employee.from_row("101,Anil,IT,45000")

print(employee.employee_id)
print(employee.name)
print(employee.department)
print(employee.salary)
```

Output:

```text
101
Anil
IT
45000.0
```

Explanation:
- `from_row` receives the class through cls.
- `split(",")` separates the text.
- int converts the ID.
- float converts the salary.
- `cls(...)` creates an instance of the class.
- return sends the created object to the caller.

This teaching example assumes simple comma-separated fields. For real CSV files, use Python's csv module because quoted values can contain commas.

## 8. Static methods

A static method is a function grouped inside a class because it is related to that class, but it does not automatically receive self or cls.

Use `@staticmethod`.

### 8.1 Basic example

```python
class Employee:
    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0

print(Employee.is_valid_salary(40000))
print(Employee.is_valid_salary(-100))
```

Output:

```text
True
False
```

The method only needs the supplied salary value. It does not need an employee object or class attribute.

### 8.2 Basic email-format helper

```python
class Employee:
    @staticmethod
    def has_basic_email_format(email):
        return "@" in email and "." in email.split("@")[-1]

print(Employee.has_basic_email_format("anil@example.com"))
print(Employee.has_basic_email_format("anil-example"))
```

Output:

```text
True
False
```

This is only a beginner demonstration. It is not complete email validation. Real applications should use suitable validators and may require email confirmation.

### 8.3 Calling a static method

A static method can be called through the class:

```python
Employee.is_valid_salary(25000)
```

It can also be called through an instance, but the class call makes its utility nature clearer.

## 9. All three method types in one class

```python
class Employee:
    company_name = "TechPhile"

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    # Instance method: reads one employee's data.
    def annual_salary(self):
        return self.monthly_salary * 12

    # Class method: reads class-level data.
    @classmethod
    def show_company(cls):
        return cls.company_name

    # Static method: checks an argument only.
    @staticmethod
    def is_valid_salary(amount):
        return amount >= 0


employee = Employee("Anil", 40000)

print(employee.annual_salary())
print(Employee.show_company())
print(Employee.is_valid_salary(40000))
```

Output:

```text
480000
TechPhile
True
```

Decision guide:
- Needs current employee state? Instance method.
- Needs class state or creates an instance through the class? Class method.
- Needs only supplied arguments? Static method may fit.
- Not meaningfully related to the class? Consider a module-level function instead.

## 10. Common mistakes

### Mistake A — static method tries to use self

Incorrect:

```python
class Employee:
    def __init__(self, salary):
        self.salary = salary

    @staticmethod
    def annual_salary():
        return self.salary * 12
```

This fails because static methods do not receive self automatically.

Correct:

```python
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12
```

### Mistake B — class method uses self

Use cls as the first parameter of a class method. It represents the class, not one employee object.

### Mistake C — missing decorator

Without `@classmethod`, Python does not bind the class as cls. Check the decorator and method signature together.

### Mistake D — every helper becomes a static method

A function does not need to be placed inside a class just because it is reusable. Keep unrelated logic in a module-level function.

## 11. Complete mini-project — Employee Utility Manager

### 11.1 Requirements

Build a command-line program that:
1. Creates employee objects.
2. Displays employee details.
3. Calculates annual salary.
4. Maintains a shared company name.
5. Changes the company name through a class method.
6. Validates salary through a static method.
7. Creates an employee from a simple row of text.

### 11.2 Folder structure

```text
day_15_employee_utility_manager/
├── main.py
└── README.md
```

### 11.3 Complete runnable code

```python
class Employee:
    company_name = "TechPhile"

    def __init__(self, employee_id, name, department, monthly_salary):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not self.is_valid_salary(monthly_salary):
            raise ValueError("Salary cannot be negative")

        self.employee_id = employee_id
        self.name = name.strip()
        self.department = department.strip()
        self.monthly_salary = monthly_salary

    # Instance method
    def display_details(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Monthly salary:", self.monthly_salary)
        print("Company:", self.company_name)

    # Instance method
    def annual_salary(self):
        return self.monthly_salary * 12

    # Class method
    @classmethod
    def change_company_name(cls, new_name):
        if not new_name.strip():
            raise ValueError("Company name cannot be empty")
        cls.company_name = new_name.strip()

    # Alternate constructor
    @classmethod
    def from_row(cls, row):
        parts = [part.strip() for part in row.split(",")]
        if len(parts) != 4:
            raise ValueError("Expected four comma-separated values")

        employee_id, name, department, salary = parts
        return cls(int(employee_id), name, department, float(salary))

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary >= 0


employees = [
    Employee(101, "Anil Kumar", "IT", 45000),
    Employee(102, "Priya Sharma", "HR", 42000),
]

employees.append(
    Employee.from_row("103,Meera Rao,Finance,50000")
)

print("EMPLOYEE REPORT")
print("===============")

for employee in employees:
    employee.display_details()
    print("Annual salary:", employee.annual_salary())
    print("----------------")

print("SALARY VALIDATION")
print(Employee.is_valid_salary(25000))
print(Employee.is_valid_salary(-500))

print("COMPANY UPDATE")
Employee.change_company_name("TechPhile Technologies")

for employee in employees:
    print(employee.name, "works at", employee.company_name)
```

### 11.4 Run the program

```powershell
python main.py
```

Verify the following:
- Three employees appear.
- Annual salary is monthly salary multiplied by 12.
- The salary validator returns True for 25000 and False for -500.
- The company name changes for instances that do not shadow the class attribute.
- The alternate constructor creates the third employee.

### 11.5 Test cases

| Test | Action | Expected |
|---|---|---|
| 1 | Create employee with valid values | Object created |
| 2 | Calculate annual salary | Monthly × 12 |
| 3 | Check positive salary | True |
| 4 | Check negative salary | False |
| 5 | Change company name | Class attribute changes |
| 6 | Create from valid row | Employee object returned |
| 7 | Create from three-field row | ValueError |
| 8 | Create with blank name | ValueError |

## 12. How to select the right method

Ask these questions:
1. Does the operation need one object's attributes? Use an instance method.
2. Does it need class-level state or need to construct an object using the class? Consider a class method.
3. Does it need neither the instance nor the class? Consider a static method.
4. Is the operation unrelated to the class? A module-level function may be clearer.

Decorators define how Python binds the method. They are not added just to make the code look advanced.

## 13. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| NameError for self | Static method refers to self | Make it an instance method or pass the value |
| Missing cls argument | Class method decorator/signature mismatch | Check @classmethod and first parameter |
| Unexpected object argument | Method type and signature do not match | Decide whether self, cls or neither is required |
| AttributeError | Attribute not initialized or misspelled | Inspect initializer and object |
| Invalid row | Wrong number/type of fields | Validate before conversion |
| Company name appears unchanged | Instance attribute shadows class attribute | Inspect both class and instance values |

## 14. Practice exercises

1. Create a Student instance method that returns a grade summary.
2. Add class attribute `college_name`.
3. Add a class method that changes the college name.
4. Add a static method that checks whether a mark is between 0 and 100.
5. Add an alternate constructor that creates a Student from a dictionary.
6. Explain why annual_salary is an instance method.
7. Explain why a salary validation helper can be static.
8. Move a helper outside the class and decide which version is clearer.

## 15. Interview questions

**1. What is an instance method?**  
A method that receives the current instance as its first argument, conventionally named self.

**2. What is a class method?**  
A method decorated with `@classmethod` that receives the class as its first argument, conventionally named cls.

**3. What is a static method?**  
A method decorated with `@staticmethod` that does not receive self or cls automatically.

**4. Difference between self and cls?**  
self refers to an instance; cls refers to the class.

**5. Can a class method create an object?**  
Yes. It can call `cls(...)` and return the new instance.

**6. Can a static method access instance variables directly?**  
No. It receives no instance automatically. Required values must be passed as arguments.

**7. When should you use a static method?**  
When helper logic is related to the class but does not need instance or class state.

**8. Can a class method be called through an instance?**  
Yes, but calling through the class is often clearer.

**9. Can an instance method change class attributes?**  
It can access the class, but a class method communicates class-wide operations more clearly.

**10. Is every reusable function a static method?**  
No. A module-level function is often clearer when the behavior is not tied to the class.

## 16. MCQs

**Q1. Which decorator defines a class method?**  
A. `@staticmethod`  
B. `@classmethod`  
C. `@property`  
D. `@abstractmethod`  
**Answer: B.** A class method receives the class as its first argument.

**Q2. What is the conventional first parameter of an instance method?**  
A. cls  
B. self  
C. this  
D. object  
**Answer: B.** self refers to the current instance.

**Q3. Which method type receives no automatic first argument?**  
A. Instance method  
B. Class method  
C. Static method  
D. Constructor  
**Answer: C.** Static methods receive only explicitly supplied arguments.

**Q4. Which method suits calculating one employee's salary from stored monthly salary?**  
A. Instance method  
B. Static method with no arguments  
C. Class method only  
D. Import statement  
**Answer: A.** It needs the current employee's state.

**Q5. What does cls refer to?**  
A. Current instance  
B. Class  
C. Current function  
D. Database table  
**Answer: B.** cls is the class passed to a class method.

**Q6. Which method is commonly used for an alternate constructor?**  
A. Class method  
B. Static method  
C. Loop method  
D. Import method  
**Answer: A.** It can call cls(...) and return an instance.

## 17. Daily completion checklist

- [ ] I can define an instance method.
- [ ] I can explain self.
- [ ] I can define a class method.
- [ ] I can explain cls.
- [ ] I can define a static method.
- [ ] I can compare the three method types.
- [ ] I can select a method type based on required data.
- [ ] I completed Employee Utility Manager.
- [ ] I tested validation and the alternate constructor.

**Next lesson:** Day 16 — Inheritance and Method Overriding.
