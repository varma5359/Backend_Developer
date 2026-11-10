# Day 10: Modules, Packages and Python Imports

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–9 — Python files, functions and collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Modular Billing Application

## 1. Learning objectives

- Explain the difference between a module and a package.
- Import a complete module or selected names.
- Use aliases with imports.
- Organize related Python files into a project.
- Explain the purpose of `__name__ == "__main__"`.
- Run a small multi-file Python application.

## 2. Why do we need modules?

As a program grows, keeping every function in one large file makes it difficult to understand and maintain.

A **module** is a Python file that can contain variables, functions and classes. A **package** organizes related modules under a common package structure.

For example, a billing application might separate price calculations, invoice formatting and the program entry point.

## 3. Create your first module

Create a file named `calculations.py`:

```python
def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(amount, rate):
    return amount * rate / 100
```

Create another file named `main.py` in the same folder:

```python
import calculations

total = calculations.calculate_total(250, 3)
print(total)
```

Run:

```powershell
python main.py
```

Output: `750`

The statement `import calculations` loads the module. Use the module name followed by a dot to access its function.

## 4. Import selected functions

Instead of importing the module name, you can import a specific function.

```python
from calculations import calculate_total

total = calculate_total(250, 3)
print(total)
```

This makes the function available directly in the current file.

Avoid importing many names without understanding where they came from. Explicit imports help readers identify dependencies.

## 5. Use an alias

An alias gives an imported module another local name.

```python
import calculations as calc

total = calc.calculate_total(100, 4)
print(total)
```

Aliases are common for modules with long or widely recognized names. Use clear aliases rather than cryptic ones.

## 6. Standard library modules

Python includes a standard library: modules that come with Python and do not need a separate package installation.

Example using `math`:

```python
import math

print(math.sqrt(81))
print(math.ceil(4.2))
```

Output:

```text
9.0
5
```

Example using `datetime`:

```python
from datetime import date

today = date.today()
print(today)
```

The displayed date depends on the machine's current date.

## 7. What is a package?

A package groups related modules. A simple package structure can look like this:

```text
billing_app/
├── main.py
└── billing/
    ├── __init__.py
    ├── calculations.py
    └── invoice.py
```

- `billing/` is the package directory.
- `__init__.py` marks a regular package and can also contain package initialization code.
- `calculations.py` and `invoice.py` are modules.

Modern Python also supports namespace packages without an `__init__.py` in some situations. For this beginner lesson, use the explicit structure shown above.

Import a function:

```python
from billing.calculations import calculate_total

print(calculate_total(150, 2))
```

Run the command from the project root so Python can find the `billing` package.

## 8. The __name__ variable

When a Python file is run directly, Python sets its `__name__` value to `"__main__"`. When it is imported as a module, its name is normally the module's import name.

```python
def show_message():
    print("Billing application started")

if __name__ == "__main__":
    show_message()
```

This pattern lets a file be both imported by another module and run directly for a simple test or entry point.

## 9. Common import problems

| Problem | Common reason | What to check |
|---|---|---|
| `ModuleNotFoundError` | Python cannot locate the module | Current folder, package path and environment |
| Importing wrong file | A local file shadows a standard library or installed package | Check filenames |
| Circular import | Modules depend on each other during import | Review dependency direction |
| Works from one folder only | Command is run from an unexpected working directory | Run from project root |
| Function name not found | Incorrect import path or spelling | Check module and function names |

Do not name your own files `json.py`, `random.py`, `datetime.py` or `requests.py` when you intend to import those libraries; the local file can shadow the intended module.

## 10. Industry scenario

A small billing tool has calculations, invoice formatting and user interaction. Keeping these responsibilities in separate modules makes it easier for developers to find code, test a calculation independently and reuse it elsewhere.

Django projects use the same broad idea of organizing code across files and applications, although Django introduces its own project conventions later in the pathway.

## 11. Approved mini-project — Modular Billing Application

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

Run the application from its project root. Change the quantity and discount rate and verify the displayed totals. Import a calculation function from a separate test file to demonstrate reuse.

## 12. Key takeaways

- A module is a Python file containing reusable code.
- A package organizes related modules.
- `import` and `from ... import ...` provide access to code.
- Use aliases when they improve clarity.
- The standard library includes useful modules.
- `if __name__ == "__main__":` separates direct execution from import behavior.
- Project structure and working directory affect imports.

**Next lesson:** Day 11 — File handling: reading, writing and working with CSV and JSON.
