# Day 10: Modules, Packages and Python Imports

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–9 — Python files, functions and collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Modular Billing Application

> **Beginner note:** So far, many examples fit inside one Python file. Real applications grow. If every calculation, message and feature is placed in one large file, finding and maintaining code becomes difficult. Today you will learn to divide code into reusable files.

## 1. Learning objectives

You should be able to:
- Explain what a module is.
- Import a module using import.
- Import selected functions using from.
- Use aliases with as.
- Explain what a package is.
- Organize a small multi-file project.
- Understand the purpose of `if __name__ == "__main__":`.

## 2. What is a module?

A **module** is a Python file that contains reusable code such as variables, functions and classes.

Imagine a billing program. It needs:
- Price calculations.
- Discount calculations.
- Invoice formatting.
- The main program that calls these operations.

Instead of putting everything in one file, you can keep related code in separate Python files.

A Python file ending in `.py` can be a module.

## 3. Create your first module

Create a folder named `billing_practice`.

Inside it, create a file named `calculations.py`:

```python
def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(amount, rate):
    return amount * rate / 100
```

This file contains two functions. It does not need to run the whole application. It provides reusable calculation operations.

Now create another file named `main.py` in the same folder:

```python
import calculations

total = calculations.calculate_total(250, 3)
print(total)
```

Run this command from the billing_practice folder:

```powershell
python main.py
```

Output:
```text
750
```

Understand the import:
- `import calculations` tells Python to load the calculations module.
- `calculations.calculate_total` accesses the function inside that module.
- The dot connects the module name to the function name.
- The function receives 250 and 3 and returns 750.

Project structure:
```text
billing_practice/
├── calculations.py
└── main.py
```

## 4. Import a complete module

Syntax:
```python
import module_name
```

Example:
```python
import calculations

subtotal = calculations.calculate_total(100, 4)
discount = calculations.calculate_discount(subtotal, 10)

print("Subtotal:", subtotal)
print("Discount:", discount)
```

Output:
```text
Subtotal: 400
Discount: 40.0
```

This style makes it clear which module provides the function.

## 5. Import a selected function using from

If you need one function, you can import it directly.

```python
from calculations import calculate_total

total = calculate_total(150, 2)
print(total)
```

Output: `300`

Explanation:
- `from calculations` identifies the module.
- `import calculate_total` selects the function.
- You can call the function directly without writing the module name.

Use explicit imports so it is clear which names your file depends on.

## 6. Import multiple functions

```python
from calculations import calculate_total, calculate_discount

subtotal = calculate_total(500, 2)
discount = calculate_discount(subtotal, 5)

print(subtotal)
print(discount)
```

Output:
```text
1000
50.0
```

You can import more than one name from a module by separating the names with commas.

## 7. Use an alias with as

An alias gives an imported module a shorter or clearer local name.

```python
import calculations as calc

total = calc.calculate_total(200, 3)
print(total)
```

Output: `600`

Here `calc` is the alias. It refers to the calculations module in this file.

Aliases are useful when a module name is long or a common short alias is widely understood. Avoid cryptic names that make code harder to read.

## 8. What is the Python standard library?

Python includes many modules that are installed with Python. These are part of the **standard library**.

You do not need to install them separately.

### 8.1 math module

```python
import math

print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.8))
```

Output:
```text
9.0
5
4
```

Understand the functions:
- `math.sqrt(81)` returns the square root of 81.
- `math.ceil(4.2)` rounds upward to the next integer.
- `math.floor(4.8)` rounds downward to the previous integer.

### 8.2 random module

```python
import random

number = random.randint(1, 10)
print(number)
```

The output is a random integer from 1 to 10, including both endpoints. Your output may be different each time.

This is useful for simple simulations and practice. Do not use the random module for security-sensitive tokens or passwords.

### 8.3 datetime module

```python
from datetime import date

today = date.today()
print(today)
```

The output depends on the date on your computer.

`date.today()` returns the current local date according to the system environment.

## 9. What is a package?

A **package** organizes related Python modules in a directory structure.

Think:
- Module = one Python file.
- Package = a directory that groups related modules.

Example:

```text
billing_app/
├── main.py
└── billing/
    ├── __init__.py
    ├── calculations.py
    └── invoice.py
```

Explanation:
- `billing_app` is the project folder.
- `billing` is the package directory.
- `calculations.py` contains calculation functions.
- `invoice.py` contains invoice-related functions.
- `__init__.py` marks a regular package and can contain package initialization code.

Modern Python also supports namespace packages without an `__init__.py` in certain situations. For this beginner lesson, use the explicit package structure shown above.

## 10. Import a function from a package

Suppose `billing/calculations.py` contains:

```python
def calculate_total(price, quantity):
    return price * quantity
```

From `main.py`, write:

```python
from billing.calculations import calculate_total

total = calculate_total(150, 2)
print(total)
```

Run the program from the project root:

```powershell
python main.py
```

Output: `300`

Why run from the project root? Python needs to be able to locate the billing package from its import search path. Running from an unexpected folder can cause ModuleNotFoundError.

## 11. What does __name__ mean?

Python provides a special variable named `__name__`.

When a file is executed directly, Python sets its `__name__` value to `"__main__"`. When the file is imported as a module, its name is normally the module's import name.

Example file `calculations.py`:

```python
def calculate_total(price, quantity):
    return price * quantity

if __name__ == "__main__":
    print(calculate_total(100, 2))
```

If you run `python calculations.py`, the output is 200.

If another file imports calculations, the guarded print statement does not run automatically. The function can still be imported and called.

This pattern lets a file provide reusable functions while also allowing a small direct test.

## 12. How imports work in a Django project

Django applications are also organized into Python packages and modules. Later you will see files such as:
- `models.py` — database model definitions.
- `views.py` — request-handling functions or classes.
- `urls.py` — URL route definitions.
- `admin.py` — admin site configuration.

These are Python modules. Django uses imports to connect code across files.

Today, understand the Python import foundation. Django's project conventions will be explained when you create your first Django application.

## 13. Common import problems

| Problem | Common reason | What to check |
|---|---|---|
| ModuleNotFoundError | Python cannot locate module | Folder, filename, environment and working directory |
| ImportError | Requested name is not available | Check function spelling and module content |
| Wrong module imported | A local file shadows another module | Check filenames and folder |
| Circular import | Two modules depend on each other during import | Simplify dependency direction |
| Works from one folder only | Current working directory changes | Run from project root |

Do not name your own files `random.py`, `json.py`, `datetime.py` or `requests.py` when you intend to import those libraries. A local file can shadow the intended module.

## 14. Industry scenario

A billing application has separate responsibilities: calculations, invoice formatting and application flow. Developers organize these responsibilities into modules. This helps a team find code, reuse calculations and test one part without running the entire application.

Django projects use the same broad idea of organizing code across modules and packages, with additional framework conventions.

## 15. Interview preparation

**Q1. What is a Python module?**

Answer: A module is a Python file containing reusable code such as functions, variables and classes.

Follow-up: How do you import a module?  
Answer: Use the import statement, such as `import calculations`.

**Q2. Difference between module and package?**

Answer: A module is a Python file. A package organizes related modules in a directory structure.

**Q3. What is the purpose of if __name__ == "__main__"?**

Answer: It checks whether the file is being executed directly. The guarded code runs in that case, but not when the file is imported as a module.

**Q4. Why should we avoid naming a file random.py?**

Answer: It can shadow Python's standard-library random module and cause unexpected import behavior.

## 16. Approved mini-project — Modular Billing Application

**Objective:** Build a small billing program split into logical Python modules.

### Requirements
1. Create a package named `billing`.
2. Put price and discount calculations in `calculations.py`.
3. Put invoice text formatting in `invoice.py`.
4. Use `main.py` as the program entry point.
5. Import and call functions from the package.
6. Use `if __name__ == "__main__":` in the entry-point file.
7. Display item subtotal, discount and final amount.

### Suggested structure

```text
modular_billing_application/
├── main.py
└── billing/
    ├── __init__.py
    ├── calculations.py
    └── invoice.py
```

### Validation
Run the application from its project root. Change quantity and discount rate and verify the totals. Import a calculation function from a separate test file to demonstrate reuse.

## 17. Daily practice and completion check

1. Create a module containing one greeting function.
2. Import that function into another file.
3. Import a module using an alias.
4. Use one standard-library function.
5. Create a package with two modules.
6. Explain why the working directory matters.
7. Explain the purpose of the main guard.

You have completed Day 10 when you can create a two-file Python program and explain how one file reuses code from another.

**Next lesson:** Day 11 — File handling: reading, writing and working with CSV and JSON.
