# Day 14: Constructors, `__init__`, `self` and Instance Variables

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Day 13 — Classes and Objects  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Employee Profile System

> Type every example, run it, compare the output, and explain what Python did. Do not memorize the constructor definition without tracing the values.

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why objects need initial data.
2. Explain what `__init__` does and when Python calls it.
3. Store values on the current object using `self`.
4. Create instance variables consistently.
5. Pass positional and keyword arguments.
6. Use default argument values appropriately.
7. Distinguish parameters, local variables and instance attributes.
8. Validate object data during initialization.
9. Build an Employee Profile System and test valid and invalid cases.

## 2. Review: what problem are we solving?

On Day 13 we used this approach:

```python
class Employee:
    def display(self):
        print(self.name, self.department)

employee = Employee()
employee.name = "Anil"
employee.department = "IT"
employee.display()
```

Output: `Anil IT`

It works, but the object is created before its required data is assigned. If we forget `department`, calling `display()` raises an AttributeError. With many objects, repeating assignments becomes inconvenient.

We want to supply required information at object creation time.

## 3. Initialization in everyday language

Initialization means preparing a newly created object with its starting data.

Examples:
- A Student starts with an ID, name and course.
- An Employee starts with an ID, name and department.
- A Product starts with a product code, name and price.
- A BankAccount starts with an account number and opening balance.

An object should begin in a predictable state.

## 4. What is __init__?

`__init__` is a special method Python calls to initialize a newly created instance. Developers often call it the constructor, although technically `__new__` creates the instance and `__init__` initializes it.

For normal beginner code, remember: when you call `Employee(...)`, Python creates an instance and automatically invokes its `__init__` method.

### 4.1 First example

Create `day_14/first_init.py`.

```python
class Employee:
    def __init__(self):
        print("Employee object initialized")

employee1 = Employee()
employee2 = Employee()
```

Expected output:

```text
Employee object initialized
Employee object initialized
```

Explanation:
1. `class Employee` defines a class.
2. `def __init__(self)` defines the initialization method.
3. `self` receives the current instance.
4. The print statement runs during initialization.
5. Each call to `Employee()` creates a separate instance and calls the initializer.

The name must be exactly `__init__`: two underscores before and after init. `init`, `_init_` and `__int__` are different names.

## 5. Pass data into __init__

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

employee1 = Employee("Anil", "IT")
employee2 = Employee("Priya", "HR")

print(employee1.name, employee1.department)
print(employee2.name, employee2.department)
```

Expected output:

```text
Anil IT
Priya HR
```

### 5.1 Trace the first object

When Python evaluates `Employee("Anil", "IT")`:

- `self` refers to the new instance.
- `name` receives `"Anil"`.
- `department` receives `"IT"`.
- `self.name = name` stores Anil on this instance.
- `self.department = department` stores IT on this instance.

When the second object is created, the same method runs for a different instance.

### 5.2 Understand self.name = name

The two names have different roles:

| Expression | Meaning |
|---|---|
| `name` | Parameter holding the value passed by the caller |
| `self.name` | Attribute stored on the current object |
| `self.name = name` | Copy the parameter's value into the object's attribute |

Incorrect:

```python
class Employee:
    def __init__(self, name):
        name = name

employee = Employee("Anil")
print(employee.name)
```

This raises AttributeError because no instance attribute was created.

Correct:

```python
class Employee:
    def __init__(self, name):
        self.name = name

employee = Employee("Anil")
print(employee.name)
```

Output: `Anil`.

## 6. Positional arguments

Positional arguments are supplied in the same order as the parameters.

```python
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

product = Product(501, "Keyboard", 1200)

print(product.product_id)
print(product.name)
print(product.price)
```

Output:

```text
501
Keyboard
1200
```

The first value goes to product_id, the second to name, and the third to price. If you accidentally reverse values, Python may still run the program but the data will be wrong.

## 7. Keyword arguments

Keyword arguments identify parameters by name.

```python
product = Product(
    name="Keyboard",
    price=1200,
    product_id=501
)
```

The order does not matter when all values are passed by keyword. Keyword arguments make calls easier to read and reduce ordering mistakes.

You can combine positional and keyword arguments, but positional arguments must appear first:

```python
product = Product(501, name="Keyboard", price=1200)
```

## 8. Default values

A parameter can have a default when a sensible default exists.

```python
class Employee:
    def __init__(self, name, department="General"):
        self.name = name
        self.department = department

employee1 = Employee("Anil", "IT")
employee2 = Employee("Priya")

print(employee1.name, employee1.department)
print(employee2.name, employee2.department)
```

Output:

```text
Anil IT
Priya General
```

Do not invent defaults for critical business values such as salary, account balance or permission level. A missing critical value should usually be rejected.

## 9. Missing required arguments

```python
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

employee = Employee("Anil")
```

Python raises TypeError because department is required but missing. This is useful feedback: the object cannot be initialized with the required information.

## 10. Parameters, local variables and instance attributes

```python
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        yearly = self.monthly_salary * 12
        return yearly

employee = Employee("Anil", 40000)
print(employee.annual_salary())
```

Output: `480000`.

| Name | Meaning |
|---|---|
| `name` | Parameter received by __init__ |
| `monthly_salary` | Parameter received by __init__ |
| `self.name` | Instance attribute stored on the object |
| `self.monthly_salary` | Instance attribute stored on the object |
| `yearly` | Local variable used during the method call |

A parameter is a name in a function definition. A local variable is created inside a function or method. An instance attribute belongs to the object and is accessed using `self`.

## 11. Methods use initialized values

```python
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def display(self):
        print("Employee:", self.name)
        print("Monthly salary:", self.monthly_salary)

    def annual_salary(self):
        return self.monthly_salary * 12

employee = Employee("Anil", 40000)
employee.display()
print("Annual salary:", employee.annual_salary())
```

Output:

```text
Employee: Anil
Monthly salary: 40000
Annual salary: 480000
```

The method reads values already stored on the object. The caller does not need to pass the employee's name and salary again.

## 12. Validate values during initialization

```python
class Employee:
    def __init__(self, name, monthly_salary):
        if not name.strip():
            raise ValueError("Employee name cannot be empty")

        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative")

        self.name = name.strip()
        self.monthly_salary = monthly_salary

employee = Employee("Anil", 40000)
print(employee.name)
```

Output: `Anil`.

Try these calls separately:

```python
Employee("", 40000)
Employee("Anil", -100)
```

Each raises ValueError with a useful message.

This is basic validation. Real applications also validate data types, lengths, business rules and values received from users. Django forms, serializers and model validation will be covered later.

## 13. Class attributes: first look

A class attribute is defined directly in the class body.

```python
class Employee:
    company_name = "TechPhile"

    def __init__(self, name):
        self.name = name

employee1 = Employee("Anil")
employee2 = Employee("Priya")

print(employee1.company_name)
print(employee2.company_name)
print(Employee.company_name)
```

All three lines display `TechPhile`.

Now try:

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

The assignment created an instance attribute for employee1; it did not change the class attribute. Day 15 will explore class-level behavior in detail.

## 14. Complete mini-project — Employee Profile System

### 14.1 Business requirement

An HR team wants a command-line employee directory. Each employee has an ID, name, department, monthly salary and work location. The program should display profiles, calculate annual salary and update a department.

### 14.2 Project structure

```text
day_14_employee_profile/
├── main.py
└── README.md
```

### 14.3 Complete runnable code

Save as `main.py`:

```python
class Employee:
    def __init__(self, employee_id, name, department, monthly_salary, location):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive")
        if not name.strip():
            raise ValueError("Employee name cannot be empty")
        if monthly_salary < 0:
            raise ValueError("Monthly salary cannot be negative")

        self.employee_id = employee_id
        self.name = name.strip()
        self.department = department.strip()
        self.monthly_salary = monthly_salary
        self.location = location

    def display_profile(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Monthly salary:", self.monthly_salary)
        print("Location:", self.location)

    def annual_salary(self):
        return self.monthly_salary * 12

    def update_department(self, new_department):
        if not new_department.strip():
            raise ValueError("Department cannot be empty")
        self.department = new_department.strip()


employees = [
    Employee(101, "Anil Kumar", "IT", 45000, "Hyderabad"),
    Employee(102, "Priya Sharma", "HR", 42000, "Bengaluru"),
    Employee(103, "Meera Rao", "Finance", 50000, "Chennai"),
]

print("EMPLOYEE DIRECTORY")
print("==================")

for employee in employees:
    employee.display_profile()
    print("Annual salary:", employee.annual_salary())
    print("------------------")

print("UPDATING EMPLOYEE 102")
employees[1].update_department("Talent Acquisition")
employees[1].display_profile()
```

Run:

```powershell
python main.py
```

You should see three employee profiles, each with its annual salary. The final profile should show employee 102's updated department.

### 14.4 Understand the code

1. The class represents one employee.
2. The initializer receives five values.
3. Validation runs before storing the data.
4. Each `self.attribute` assignment stores a value on the current instance.
5. `display_profile` displays that instance's values.
6. `annual_salary` returns monthly salary multiplied by 12.
7. `update_department` validates and updates the current employee.
8. The list stores three separate Employee objects.
9. The loop visits each object.
10. `employees[1]` selects the second object because list indexes start at zero.

### 14.5 Test cases

| Test | Action | Expected result |
|---|---|---|
| 1 | Create employee with valid data | Object created |
| 2 | Use ID 0 | ValueError |
| 3 | Use empty name | ValueError |
| 4 | Use negative salary | ValueError |
| 5 | Calculate annual salary | Monthly salary × 12 |
| 6 | Update department with valid text | Department changes |
| 7 | Update department with empty text | ValueError |
| 8 | Update one employee | Other employees remain unchanged |

## 15. Common mistakes and troubleshooting

| Problem | Cause | Correction |
|---|---|---|
| Missing required positional argument | Required initializer value omitted | Supply it or define a meaningful default |
| AttributeError for an attribute | Used a local parameter instead of self | Assign using `self.attribute = parameter` |
| Too many positional arguments | Method signature and call do not match | Count self and caller-supplied arguments |
| Values stored in wrong fields | Positional order is incorrect | Use keyword arguments |
| Initializer does not run | Special method name misspelled | Use exactly `__init__` |
| IndentationError | Incorrect indentation | Use four spaces consistently |
| Shared data changes unexpectedly | Mutable class attribute used as per-object state | Store per-object values on self |
| Invalid salary accepted | Validation missing | Validate before assigning |

Debugging checklist:
1. Check spelling of `__init__`.
2. Count all parameters, including self.
3. Compare the call with the parameter order.
4. Check that assignments use self.
5. Inspect `object.__dict__` while learning.
6. Test one object first.
7. Test invalid input separately.

## 16. Practice exercises

1. Create a Student class with ID, name and course. Create three objects.
2. Create a Product class with ID, name and price. Reject a negative price.
3. Give Employee a default location of Hyderabad; override it for one employee.
4. Add methods for annual salary and a 10% annual bonus.
5. Create a Product using keyword arguments in a different order.
6. Remove self from one assignment, run the code and explain the error.
7. Create two accounts and show that changing one account's balance does not change the other.

## 17. Interview questions

**1. What is __init__?**  
A special method called automatically to initialize a newly created instance.

**2. Is __init__ technically the method that creates an object?**  
No. `__new__` creates the instance; `__init__` initializes it.

**3. Why do we use self?**  
It refers to the current instance and lets the method store or access that object's attributes.

**4. What is an instance variable?**  
An attribute associated with one object, commonly assigned using `self.attribute`.

**5. What if a required constructor argument is missing?**  
Python raises TypeError.

**6. Can __init__ return a value?**  
It should return None. Returning a non-None value causes TypeError.

**7. Difference between parameter and instance variable?**  
A parameter receives a value during a call; an instance variable stores data on the object.

**8. Can __init__ have default values?**  
Yes, if the defaults are meaningful and safe for the application.

**9. Why validate during initialization?**  
To prevent objects from starting with invalid state.

**10. Where is initialization used in Django?**  
Python initialization underlies Django's class-based components and objects. Django model construction has framework-specific behavior that will be taught in the Django module.

## 18. MCQs

**Q1. What is the main purpose of __init__?**  
A. Initialize an instance  
B. Delete a class  
C. Start a database server  
D. Import a package  
**Answer: A.** It prepares an instance with starting values.

**Q2. Which assignment stores a value on the current object?**  
A. `name = self.name`  
B. `self.name = name`  
C. `name == self`  
D. `Employee.name()`  
**Answer: B.** The left side is an instance attribute.

**Q3. What happens if a required argument is missing?**  
A. It becomes zero  
B. TypeError is raised  
C. The class is deleted  
D. Initialization is skipped  
**Answer: B.** Required arguments must be supplied.

**Q4. Which call uses keyword arguments?**  
A. `Employee(101, "Anil")`  
B. `Employee(name="Anil", employee_id=101)`  
C. `Employee()`  
D. `Employee["Anil"]`  
**Answer: B.** Parameter names are explicit.

**Q5. Which is an instance attribute?**  
A. `self.department`  
B. A temporary local variable only  
C. `__init__`  
D. `class`  
**Answer: A.** It is stored on the current object.

**Q6. Which special method creates an instance before initialization?**  
A. `__str__`  
B. `__new__`  
C. `__len__`  
D. `__repr__`  
**Answer: B.** `__new__` creates the instance; `__init__` initializes it.

## 19. Daily completion checklist

- [ ] I can explain object initialization.
- [ ] I can write __init__ correctly.
- [ ] I can explain self.
- [ ] I can assign instance attributes.
- [ ] I can use positional and keyword arguments.
- [ ] I can use appropriate default values.
- [ ] I can distinguish parameters, local variables and instance attributes.
- [ ] I can validate values.
- [ ] I completed Employee Profile System.
- [ ] I tested valid and invalid input.

**Next lesson:** Day 15 — Instance Methods, Class Methods and Static Methods.
