# Day 13: Introduction to OOP, Classes and Objects

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–12 Python fundamentals  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Student Object Manager

> **How to study this lesson:** Do not jump directly to the project. Read one concept, type the example yourself, run it, compare the output, and explain what happened. The goal is to understand objects—not to memorize the word OOP.

---

## 1. What you will learn today

By the end of this lesson, you should be able to:

1. Explain why developers use object-oriented programming.
2. Identify the difference between procedural programming and object-oriented programming.
3. Explain a class, object, instance, attribute and method in plain language.
4. Define a class using Python's `class` keyword.
5. Create more than one object from the same class.
6. Store different data in different objects.
7. call an instance method using dot notation.
8. Explain what `self` refers to at a beginner level.
9. Distinguish an attribute from a local variable.
10. Build a small Student Object Manager and test its behavior.
11. Recognize common OOP errors and correct them.
12. Explain where classes and objects appear in Django applications.

## 2. First understand the problem: managing student information

Imagine that a college has three students.

| Student ID | Name | Course | City |
|---:|---|---|---|
| 101 | Asha | Python | Hyderabad |
| 102 | Ravi | Django | Vijayawada |
| 103 | Meera | SQL | Visakhapatnam |

A beginner may store the information in separate variables:

```python
student1_name = "Asha"
student1_course = "Python"
student1_city = "Hyderabad"

student2_name = "Ravi"
student2_course = "Django"
student2_city = "Vijayawada"

student3_name = "Meera"
student3_course = "SQL"
student3_city = "Visakhapatnam"
```

This code is valid. For three students, it is manageable. Now imagine 500 students.

Questions to consider:

- How many variables would you need?
- How would you update one student's course?
- How would you display one student's complete profile?
- How would you avoid mixing Asha's city with Ravi's course?
- How would you reuse the same profile-display logic?

The problem is not that variables are bad. The problem is that related information and behavior are scattered.

**OOP gives us a way to group related data and behavior into a reusable structure.**

## 3. Procedural programming versus object-oriented programming

### 3.1 Procedural style

Procedural programming organizes a program around statements and functions.

```python
def display_student(name, course, city):
    print("Student name:", name)
    print("Course:", course)
    print("City:", city)

display_student("Asha", "Python", "Hyderabad")
display_student("Ravi", "Django", "Vijayawada")
```

Expected output:

```text
Student name: Asha
Course: Python
City: Hyderabad
Student name: Ravi
Course: Django
City: Vijayawada
```

This is a good approach for many small tasks. Functions help avoid repeating the same printing statements.

However, the data is still passed separately to the function every time. A class can group the data and the operations that belong to it.

### 3.2 Object-oriented style

```python
class Student:
    def display_profile(self):
        print("Student profile")

student1 = Student()
student2 = Student()

student1.display_profile()
student2.display_profile()
```

Expected output:

```text
Student profile
Student profile
```

We have defined one class and created two objects from it. Both objects can use the behavior defined by the class.

At this stage, the objects do not yet contain student names or courses. We will add those next.

### 3.3 When should you use each style?

| Situation | Suitable starting point |
|---|---|
| A short calculation with a few inputs | Function |
| A one-time data conversion | Function |
| Related data and operations belong together | Class |
| Many employees share a common structure | Class |
| A reusable operation has no object state | Function may be enough |
| A Django model represents a database entity | Class |

Do not create a class for every small piece of code. Choose the simplest structure that makes the program understandable.

## 4. What is a class?

A **class** is a definition that describes the data and behavior its objects can have.

Think of a class as a design or blueprint.

Examples:

- Student is a class.
- Employee is a class.
- Product is a class.
- BankAccount is a class.
- Order is a class.

A class is not one actual student or employee. It describes the common structure.

For example, a Student class may describe that every student profile has:

- A student ID.
- A name.
- A course.
- A city.
- A method to display the profile.

The class definition does not mean that a real student record has already been created. We create objects from the class.

### 4.1 Basic syntax

```python
class ClassName:
    # attributes and methods are defined here
    pass
```

Explanation:

1. `class` is a Python keyword.
2. `ClassName` is the name we choose.
3. The colon begins the class body.
4. The indented lines belong to the class.
5. `pass` is a placeholder statement. It lets us define an empty class temporarily.

Python convention uses **PascalCase** for class names: `Student`, `EmployeeProfile`, `BankAccount`.

## 5. Your first class

Create a folder named `day_13`. Inside it, create `first_class.py`.

```python
class Student:
    pass

print("Student class created")
```

Run:

```powershell
python first_class.py
```

Expected output:

```text
Student class created
```

What happened?

- Python read the class definition.
- Python created a class object named `Student`.
- The `pass` statement did nothing.
- The print statement displayed the message.

Important: defining a class and creating an instance are two different actions.

## 6. What is an object?

An **object** is an instance created from a class.

If Student is the class, Asha's student profile can be one object and Ravi's profile can be another object.

```python
class Student:
    pass

student1 = Student()
student2 = Student()

print(type(student1))
print(type(student2))
print(student1 is student2)
```

Expected output:

```text
<class '__main__.Student'>
<class '__main__.Student'>
False
```

Explanation:

- `Student()` creates an instance of the Student class.
- `student1` refers to the first object.
- `student2` refers to the second object.
- Both objects have the same class.
- `is` checks whether two references point to the same object.
- The result is `False`, because these are two different objects.

### 6.1 Class and object comparison

| Class | Object |
|---|---|
| Defines a structure | Is one instance of that structure |
| Example: Student | Example: Asha's student profile |
| Defined using `class` | Created by calling the class |
| Can define methods | Can call available instance methods |

### 6.2 Real-world analogy

A building plan describes rooms, doors and dimensions. The plan is not the building itself. Multiple buildings can be constructed using the same plan.

In the same way:

- Class = building plan.
- Object = one constructed building.
- Attributes = details such as address and number of rooms.
- Methods = actions supported by the object.

The analogy helps you remember the idea, but remember that Python objects are created in computer memory.

## 7. What are attributes?

An **attribute** is a value associated with an object or class.

For today's first examples, we will use instance attributes: values associated with a particular object.

```python
class Student:
    pass

student1 = Student()
student1.name = "Asha"
student1.course = "Python"

print(student1.name)
print(student1.course)
```

Expected output:

```text
Asha
Python
```

Explanation:

- `student1 = Student()` creates an object.
- `student1.name = "Asha"` attaches a name attribute to that object.
- `student1.course = "Python"` attaches a course attribute.
- Dot notation accesses an object's attribute.

Python allows this simple assignment, but later we will use `__init__` to create the expected attributes consistently when an object is created.

### 7.1 Different objects can store different values

```python
class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "Asha"
student1.course = "Python"

student2.name = "Ravi"
student2.course = "Django"

print(student1.name, student1.course)
print(student2.name, student2.course)
```

Expected output:

```text
Asha Python
Ravi Django
```

Both objects were created from the same class, but their data is separate.

Try changing Ravi's course to SQL. Run the program again. Asha's course should remain Python.

### 7.2 Inspect an object's attributes

```python
class Student:
    pass

student = Student()
student.name = "Meera"
student.course = "SQL"

print(student.__dict__)
```

Expected output:

```text
{'name': 'Meera', 'course': 'SQL'}
```

`__dict__` is a useful inspection feature for many ordinary Python objects. It shows the object's stored instance attributes. It is a learning/debugging tool, not a substitute for a clear class design.

## 8. What is a method?

A **method** is a function defined inside a class.

A method describes behavior that belongs to the class's objects.

Examples:

- A Student object can display its profile.
- A BankAccount object can deposit money.
- An Employee object can calculate a bonus.
- A ShoppingCart object can add an item.

### 8.1 Define a method

```python
class Student:
    def display_message(self):
        print("Welcome to the student portal")

student1 = Student()
student1.display_message()
```

Expected output:

```text
Welcome to the student portal
```

Read it carefully:

1. `class Student:` defines the class.
2. `def display_message(self):` defines a method.
3. `self` is the parameter that receives the current object.
4. The print statement is the method's behavior.
5. `student1 = Student()` creates an object.
6. `student1.display_message()` calls the method for that object.

You do not pass `self` manually when calling an ordinary instance method through the object. Python supplies the object automatically.

## 9. Understand self step by step

This is one of the most important ideas in the first OOP lesson.

`self` refers to the current instance on which an instance method is being called.

Look at this example:

```python
class Student:
    def display_name(self):
        print("Current object:", self)

student1 = Student()
student2 = Student()

student1.display_name()
student2.display_name()
```

The output contains two different object representations. The exact memory-style representation may differ each time you run the program.

What matters:

- Calling `student1.display_name()` makes `self` refer to `student1`.
- Calling `student2.display_name()` makes `self` refer to `student2`.
- The method is shared in the class definition.
- The current object is supplied when the method is called.

### 9.1 See the automatic argument passing

These two calls are equivalent for this simple example:

```python
student1.display_name()
Student.display_name(student1)
```

The first form is the normal style. The second makes the object argument visible and helps explain what Python does.

Do not normally write the second form in application code. Use the object and dot notation.

### 9.2 What happens if you forget self?

Incorrect example:

```python
class Student:
    def display_name():
        print("Student")

student = Student()
student.display_name()
```

This raises a `TypeError` because Python supplies the object as an argument, but the method has no parameter to receive it.

Correct example:

```python
class Student:
    def display_name(self):
        print("Student")

student = Student()
student.display_name()
```

Expected output:

```text
Student
```

Remember: `self` is a naming convention, not a reserved keyword. You could technically choose another parameter name, but use `self` because every Python developer expects it.

## 10. Put attributes and methods together

Now we can create a more useful class.

```python
class Student:
    def display_profile(self):
        print("Student profile")
        print("Name:", self.name)
        print("Course:", self.course)
        print("City:", self.city)

student1 = Student()
student1.name = "Asha"
student1.course = "Python"
student1.city = "Hyderabad"

student1.display_profile()
```

Expected output:

```text
Student profile
Name: Asha
Course: Python
City: Hyderabad
```

Line-by-line explanation:

- The class defines the Student type.
- The method describes how to display a profile.
- `self.name` means the name attribute belonging to the current object.
- `self.course` means the current object's course.
- `self.city` means the current object's city.
- The three assignments add data to student1.
- The method reads that data and displays it.

Important limitation: if you call this method on an object that does not have these attributes, Python raises `AttributeError`. Day 14 will introduce constructors so each new object can receive its required data at creation time.

## 11. Add a method that returns a value

Methods can return values. They do not have to print.

```python
class Student:
    def get_course_message(self):
        return "This student is learning Python"

student = Student()
message = student.get_course_message()

print(message)
```

Expected output:

```text
This student is learning Python
```

Difference:

| `print()` | `return` |
|---|---|
| Displays a value | Sends a value back to the caller |
| Mainly for visible output | Useful for further calculations and decisions |
| Does not automatically give the caller a reusable result | Caller can store and use the returned value |

A backend method usually returns data or a result to another part of the application. Printing is mainly useful for learning, debugging and command-line programs.

## 12. Multiple objects and independent state

```python
class Employee:
    def display(self):
        print(self.name, "-", self.department)

employee1 = Employee()
employee2 = Employee()

employee1.name = "Anil"
employee1.department = "IT"

employee2.name = "Priya"
employee2.department = "HR"

employee1.display()
employee2.display()
```

Expected output:

```text
Anil - IT
Priya - HR
```

Each object has its own values. Changing one object's attributes does not automatically change another object's attributes.

Try these experiments:

1. Change `employee1.department` to Finance.
2. Display both employees again.
3. Delete `employee2.department` using `del employee2.department`.
4. Call `employee2.display()` and observe the error.
5. Explain why the error occurs.

## 13. Class attributes and instance attributes: first look

An instance attribute belongs to an individual object. A class attribute is defined directly in the class and is shared through the class unless an instance overrides it.

```python
class Student:
    college_name = "TechPhile Institute"

student1 = Student()
student2 = Student()

student1.name = "Asha"
student2.name = "Ravi"

print(student1.college_name)
print(student2.college_name)
print(Student.college_name)
```

Expected output:

```text
TechPhile Institute
TechPhile Institute
TechPhile Institute
```

Here:

- `college_name` is defined in the class body.
- `name` is assigned separately to each object.
- Both objects can read the class attribute.

If you assign `student1.college_name = "City College"`, you create or replace an instance attribute for student1. You do not change the class attribute for every object.

```python
student1.college_name = "City College"

print(student1.college_name)
print(student2.college_name)
print(Student.college_name)
```

Expected output:

```text
City College
TechPhile Institute
TechPhile Institute
```

We will study class variables and methods more carefully on Day 15.

## 14. Naming and code organization

Use names that communicate purpose.

| Prefer | Avoid |
|---|---|
| `Student` | `s` as a class name |
| `student1` | `x` for a student object |
| `display_profile` | `do_it` |
| `course_name` | `a1` |
| `EmployeeManager` | `thing` |

Python naming conventions:

- Class names: `PascalCase`.
- Function and method names: `snake_case`.
- Variable names: `snake_case`.
- Constants: often `UPPER_SNAKE_CASE`.

Conventions improve readability. Python does not enforce all naming conventions as syntax rules.

## 15. A complete guided example: Student Object Manager

We will now combine the concepts in a small command-line application.

### 15.1 Requirements

The application should:

1. Create student objects.
2. Store a student ID, name, course and city.
3. Display one student's profile.
4. Display all student profiles.
5. Update a student's course.
6. Keep each student's information separate.

We are intentionally not using a database today. The goal is to understand objects in memory. Database storage and Django models come later in the pathway.

### 15.2 Create the project

Folder structure:

```text
day_13/
├── student_manager.py
└── README.md
```

Create `student_manager.py`.

### 15.3 First version: define the class

```python
class Student:
    def display_profile(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("City:", self.city)
```

At this stage, the class defines a display behavior. It assumes the object already has the four attributes.

### 15.4 Create the objects and add values

```python
student1 = Student()
student1.student_id = 101
student1.name = "Asha"
student1.course = "Python"
student1.city = "Hyderabad"

student2 = Student()
student2.student_id = 102
student2.name = "Ravi"
student2.course = "Django"
student2.city = "Vijayawada"
```

Notice that we repeat the assignments for each object. Day 14 will improve this using `__init__`.

### 15.5 Add a display method call

```python
student1.display_profile()
print("---")
student2.display_profile()
```

Expected output:

```text
Student ID: 101
Name: Asha
Course: Python
City: Hyderabad
---
Student ID: 102
Name: Ravi
Course: Django
City: Vijayawada
```

### 15.6 Add a course update method

Update the class:

```python
class Student:
    def display_profile(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("City:", self.city)

    def update_course(self, new_course):
        self.course = new_course
```

Call the method:

```python
student1.update_course("Django")
student1.display_profile()
```

The method receives the new course as `new_course`. It updates the course attribute on the object that called the method.

Check student2 afterwards. Its course should still be Django because it was already Django; change student2 to SQL before testing if you want to see the independence clearly.

### 15.7 Full runnable version

Replace the contents of `student_manager.py` with this complete version:

```python
class Student:
    def display_profile(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("City:", self.city)

    def update_course(self, new_course):
        self.course = new_course

    def get_profile_summary(self):
        return f"{self.name} is learning {self.course}"


student1 = Student()
student1.student_id = 101
student1.name = "Asha"
student1.course = "Python"
student1.city = "Hyderabad"

student2 = Student()
student2.student_id = 102
student2.name = "Ravi"
student2.course = "Django"
student2.city = "Vijayawada"

student3 = Student()
student3.student_id = 103
student3.name = "Meera"
student3.course = "SQL"
student3.city = "Visakhapatnam"

students = [student1, student2, student3]

print("ALL STUDENT PROFILES")
print("====================")

for student in students:
    student.display_profile()
    print("--------------------")

print("UPDATING ONE STUDENT")
student1.update_course("Django")

print(student1.get_profile_summary())
print(student2.get_profile_summary())
print(student3.get_profile_summary())
```

Expected output:

```text
ALL STUDENT PROFILES
====================
Student ID: 101
Name: Asha
Course: Python
City: Hyderabad
--------------------
Student ID: 102
Name: Ravi
Course: Django
City: Vijayawada
--------------------
Student ID: 103
Name: Meera
Course: SQL
City: Visakhapatnam
--------------------
UPDATING ONE STUDENT
Asha is learning Django
Ravi is learning Django
Meera is learning SQL
```

### 15.8 Understand the complete program

| Code | Meaning |
|---|---|
| `class Student:` | Defines the Student class |
| `display_profile(self)` | Defines behavior to display one object |
| `update_course(self, new_course)` | Receives a new course value |
| `self.course = new_course` | Changes the current object's course |
| `get_profile_summary(self)` | Returns a formatted string |
| `Student()` | Creates one Student object |
| `students = [...]` | Stores references to the three objects in a list |
| `for student in students:` | Visits each object in the list |
| `student.display_profile()` | Calls the method for the current object |

### 15.9 Test the application

| Test | Action | Expected result |
|---|---|---|
| T1 | Create student1 | One Student object exists |
| T2 | Set student1 name | Name is Asha |
| T3 | Create student2 | A separate object exists |
| T4 | Set student2 name | Name is Ravi |
| T5 | Display student1 | Only Asha's profile appears |
| T6 | Display student2 | Only Ravi's profile appears |
| T7 | Update student1 course | student1 course changes |
| T8 | Display student2 after update | student2 remains unchanged |
| T9 | Store objects in a list | All three can be processed in a loop |

### 15.10 What are the limitations of this first version?

This is a teaching application, not a production student-management system.

- It does not validate whether a student ID is unique.
- It allows attributes to be missing.
- It stores data only in program memory.
- Data disappears when the program ends.
- It has no database or user interface.
- It has no login or access control.
- It does not handle invalid user input.

These limitations are intentional. We will solve some of them in later lessons. Do not add a database before understanding the class and object concepts.

## 16. Common beginner errors

| Error or symptom | Why it happens | How to correct it |
|---|---|---|
| `NameError: name 'Student' is not defined` | The class was not defined or its name is misspelled | Check the class definition and spelling |
| `TypeError` when calling a method | The method parameters do not match the supplied arguments | Check the method signature and call |
| `AttributeError` for `name` | The object does not have a name attribute | Assign the attribute or initialize it in a constructor |
| IndentationError | The class or method body has incorrect indentation | Use consistent four-space indentation |
| Wrong object is updated | The method call was made on a different object | Trace the object before the dot |
| Output is not displayed | The method was defined but never called | Call it using object dot notation |
| Same values appear unexpectedly | Values were assigned to the wrong object or a shared class attribute | Inspect each object's attributes |
| Class name is lowercase | Naming convention is not followed | Use PascalCase for class names |

### 16.1 Debug one issue at a time

When the program fails:

1. Read the final line of the traceback first.
2. Identify the exception type.
3. Note the file and line number.
4. Inspect the exact object and method on that line.
5. Print the object's type if necessary.
6. Inspect its attributes.
7. Make one correction.
8. Run the smallest test again.

Do not delete the whole program because of one error. Trace the failing statement.

## 17. OOP in real backend development

Classes are common in backend systems because backend applications represent business entities and organize behavior.

Examples:

| Backend concept | Possible class or object |
|---|---|
| Student registration | Student |
| Employee portal | Employee |
| Shopping application | Product, Cart, Order |
| Banking system | BankAccount, Transaction |
| Django database layer | Model class and model instance |
| API validation | Serializer class and serializer instance |
| HTTP handling | Request object and response object |

In Django, a model is defined as a Python class. A model instance represents one record.

For example, a later Django lesson may contain:

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
```

Do not worry about `models.Model` or `CharField` yet. Those belong to Django. For now, recognize the familiar class syntax and understand that Django builds on Python's object model.

## 18. When classes are useful—and when they are unnecessary

Use a class when:

- You need multiple objects with the same general structure.
- Each object has its own state.
- Related behavior belongs with that state.
- The class name represents a meaningful concept in the application.
- The design becomes easier to understand with the class.

A function may be simpler when:

- You only need to transform a value.
- There is no meaningful object state.
- The operation is short and reusable on its own.
- A class would only wrap one function without adding clarity.

A good developer does not use OOP just to make a program look advanced. The design should make the code easier to understand and maintain.

## 19. Guided practice exercises

Complete these in order. Type the code yourself.

### Exercise 1 — Book class

Create a class named `Book`.

Create two objects:

- Book 1: title = Python Basics, author = A. Kumar.
- Book 2: title = Django Guide, author = S. Rao.

Display both books.

### Exercise 2 — Product class

Create a class named `Product`.

Each object should have:

- product_id
- product_name
- price

Create three product objects and display their details.

### Exercise 3 — Employee method

Create an Employee class with a method named `display_details`.

Create two employee objects with different names and departments.

### Exercise 4 — Return a value

Create a method called `get_annual_salary` that returns monthly salary multiplied by 12.

Use two employee objects and print the returned values.

### Exercise 5 — Update one object

Create two BankAccount objects. Add a method called `show_balance`. Change the balance of one object and prove the other object is unchanged.

### Exercise 6 — List of objects

Create four Product objects and store them in a list. Use a loop to display each product.

### Exercise 7 — Find a mistake

Run this code and correct it:

```python
class Employee:
    def display():
        print("Employee details")

employee = Employee()
employee.display()
```

Explain why it failed and why your correction works.

## 20. Mini-project submission requirements

**Project:** Student Object Manager

Submit:

1. `student_manager.py`.
2. A README containing the problem statement.
3. The class and object design.
4. At least three student objects.
5. A profile-display method.
6. A course-update method.
7. A list containing the objects.
8. Terminal output showing the application works.
9. A short explanation of how `self` works.
10. At least five manual test cases.

Suggested structure:

```text
projects/
└── day_13_student_object_manager/
    ├── README.md
    ├── student_manager.py
    └── evidence/
        └── terminal_output.txt
```

## 21. Interview preparation

### Q1. What is object-oriented programming?

**Answer:** Object-oriented programming is a programming approach that organizes code around objects. Objects combine data and behavior. Python supports OOP through classes and objects.

### Q2. What is a class?

**Answer:** A class is a definition that describes the attributes and methods its instances can have.

### Q3. What is an object?

**Answer:** An object is an instance created from a class. Two objects created from the same class can store different instance data.

### Q4. What is the difference between a class and an object?

**Answer:** A class defines a structure; an object is one instance of that structure.

### Q5. What is an attribute?

**Answer:** An attribute is a value associated with an object or class. For example, `student.name` can hold a student's name.

### Q6. What is a method?

**Answer:** A method is a function defined inside a class. An instance method can use the current object through `self`.

### Q7. What is self in Python?

**Answer:** `self` refers to the current instance. Python supplies it automatically when an instance method is called through an object.

### Q8. Is self a keyword?

**Answer:** No. It is a strong naming convention. Developers use it because it makes instance methods consistent and readable.

### Q9. Can we create multiple objects from one class?

**Answer:** Yes. Each call to the class creates an instance. Each instance can hold its own instance attributes.

### Q10. What happens if we forget self in an instance method?

**Answer:** Python still supplies the instance during an ordinary bound method call, so the argument count will not match and a TypeError is raised.

### Q11. What is the difference between an attribute and a method?

**Answer:** An attribute stores or exposes data. A method defines behavior that can be called.

### Q12. Where do you see classes in Django?

**Answer:** Django uses classes for models, class-based views, forms, serializers in DRF and many framework components. The exact role of each class will be taught in later Django lessons.

## 22. Daily MCQs

**Q1. Which statement best describes a class?**

A. A definition for creating objects  
B. A database row only  
C. A Python loop  
D. A print statement  

**Answer: A.** A class defines the structure and behavior that its instances can use.

**Q2. What does `Student()` do when Student is a class?**

A. Deletes the class  
B. Creates an instance  
C. Prints the class  
D. Imports a package  

**Answer: B.** Calling the class creates an instance.

**Q3. What does self normally refer to inside an instance method?**

A. The current instance  
B. The parent folder  
C. The Python interpreter  
D. A database connection  

**Answer: A.** It refers to the object on which the method was called.

**Q4. Which is the conventional class name?**

A. `student_profile`  
B. `student-profile`  
C. `StudentProfile`  
D. `STUDENT PROFILE`  

**Answer: C.** Python class names conventionally use PascalCase.

**Q5. What is the result of creating two objects from the same class?**

A. Both names must refer to one object  
B. They are separate instances of the same class  
C. The class is deleted  
D. Python raises an error  

**Answer: B.** Each class call creates a separate instance.

**Q6. Which statement calls an instance method?**

A. `student.display_profile()`  
B. `display_profile student`  
C. `class.display_profile`  
D. `method = student`  

**Answer: A.** Dot notation calls the method on the specified object.

**Q7. What is an instance attribute?**

A. Data associated with an individual object  
B. A Python keyword  
C. A SQL query  
D. A file extension  

**Answer: A.** Instance attributes store data associated with one object.

**Q8. What happens if a method tries to read an attribute that the object does not have?**

A. It always returns zero  
B. It creates the attribute automatically  
C. It can raise AttributeError  
D. It closes Python  

**Answer: C.** Accessing a missing attribute normally raises AttributeError.

## 23. Trainer-led review

Ask learners to answer without reading the notes:

1. Why did we introduce a Student class?
2. What is the difference between Student and student1?
3. Can two objects have different names?
4. What does `self.name` mean?
5. Why does an instance method need self?
6. What is the difference between printing and returning?
7. Why is a class not automatically a database table?
8. Where will these ideas be used in Django?

If a learner cannot explain an answer, return to the corresponding runnable example instead of asking them to memorize a definition.

## 24. Final completion checklist

- [ ] I can explain the problem OOP helps organize.
- [ ] I can define a class.
- [ ] I can create two or more objects.
- [ ] I can explain class versus object.
- [ ] I can create and read instance attributes.
- [ ] I can define and call an instance method.
- [ ] I can explain self in my own words.
- [ ] I can distinguish print from return.
- [ ] I completed Student Object Manager.
- [ ] I tested that changing one object does not change another.
- [ ] I answered the MCQs and interview questions.
- [ ] I can explain how classes are used in backend development.

**Next lesson:** Day 14 — Constructors, `__init__`, `self` and instance variables.
