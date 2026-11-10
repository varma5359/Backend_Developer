# Day 10: Modules, Packages and Python Imports

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–9; Python files, functions and collections  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Modular Billing Application

## 1. Learning objectives
- Explain modules and packages.
- Create and import a custom Python module.
- Use common import styles.
- Organize related files in a package.
- Split a small billing program into reusable files.

## 2. What is a module?
A Python module is a Python file that can contain functions, variables and classes. A file named `calculations.py` can be imported by another Python file.

Why modules?
- Organize code by responsibility.
- Reuse functions.
- Reduce one large script into smaller files.
- Make a project easier to understand and test.

## 3. Create a custom module
Project structure:
```text
billing_demo/
├── main.py
└── calculations.py
```

In `calculations.py`:
```python
def calculate_total(price, quantity):
    return price * quantity

def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100
```

In `main.py`:
```python
import calculations

subtotal = calculations.calculate_total(500, 2)
tax = calculations.calculate_tax(subtotal, 5)

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Final amount:", subtotal + tax)
```

Run from the project folder:
```bash
python main.py
```

Expected output:
```text
Subtotal: 1000
Tax: 50.0
Final amount: 1050.0
```

## 4. Different import styles

Import the module:
```python
import calculations
calculations.calculate_total(100, 2)
```

Import selected names:
```python
from calculations import calculate_total
calculate_total(100, 2)
```

Use an alias:
```python
import calculations as calc
calc.calculate_total(100, 2)
```

For beginner projects, avoid `from module import *`. It makes it unclear where names came from and can create naming conflicts.

## 5. What is a package?
A package is a way to organize related modules under a common directory. A regular Python package commonly contains an `__init__.py` file.

Structure:
```text
billing_demo/
├── main.py
└── billing/
    ├── __init__.py
    ├── pricing.py
    └── tax.py
```

In `billing/pricing.py`:
```python
def calculate_subtotal(price, quantity):
    return price * quantity
```

In `billing/tax.py`:
```python
def calculate_tax(amount, rate):
    return amount * rate / 100
```

In `main.py`:
```python
from billing.pricing import calculate_subtotal
from billing.tax import calculate_tax

subtotal = calculate_subtotal(800, 2)
tax = calculate_tax(subtotal, 5)
print(subtotal + tax)
```

Run:
```bash
python main.py
```

Expected output: `1680.0`.

Modern Python also supports namespace packages without an `__init__.py` in some cases. For this beginner pathway, use `__init__.py` to make the package boundary explicit.

## 6. Built-in modules
Python provides standard-library modules.

```python
import math
print(math.sqrt(81))
```

Output: `9.0`.

```python
from datetime import date
print(date.today())
```

The printed date depends on the machine's current date.

Other useful standard-library modules include json, csv, pathlib, os and logging. You will use several of them in later lessons.

## 7. Third-party packages
Third-party packages are installed separately, commonly using pip.

Example:
```bash
python -m pip install requests
```

Then:
```python
import requests
print(requests.__version__)
```

A module is importable code; a package is an organized collection of modules or importable components. In everyday Python usage, the term "package" is also used for installable distributions.

## 8. The __name__ guard
A common Python pattern:
```python
def main():
    print("Billing application started")

if __name__ == "__main__":
    main()
```

The guarded code runs when the file is executed directly. It does not run just because another file imports the module.

This helps a module provide reusable functions without automatically running its application entry point when imported.

## 9. Common import errors
| Error | Possible reason |
|---|---|
| ModuleNotFoundError | Module/package unavailable in current environment or import path |
| ImportError | Requested name cannot be imported |
| Circular import | Modules depend on each other during initialization |
| Wrong file name | Import name does not match module |
| Running from wrong folder | Project root/package path not resolved as expected |

Avoid naming your own files after standard-library modules such as `json.py`, `logging.py` or `random.py`, because this can shadow the real module.

## 10. Industry scenario
A billing backend has separate responsibilities for pricing, tax calculations and invoice formatting. Keeping them in separate modules allows each part to be understood and tested independently.

## 11. Approved mini-project — Modular Billing Application

**Objective:** Organize a small billing workflow into reusable modules and a package.

### Requirements
1. Create a project entry file named `main.py`.
2. Create a package named `billing`.
3. Add a pricing module for subtotal calculation.
4. Add a tax module for tax calculation.
5. Add a summary module that formats invoice details.
6. Import and use those functions from main.py.
7. Use an `if __name__ == "__main__":` guard.
8. Test the calculations with at least two invoices.

**Suggested structure**
```text
modular_billing_application/
├── main.py
└── billing/
    ├── __init__.py
    ├── pricing.py
    ├── tax.py
    └── summary.py
```

**Example test values:** unit price 800, quantity 2, tax rate 5%. Expected subtotal 1600, tax 80, final 1680.

### Validation
- Run main.py from the project root.
- Import one function from each module.
- Confirm imports do not trigger unwanted output.
- Change a price and verify the result changes correctly.
- Ensure modules have one clear responsibility.

## 12. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for choosing which billing functions belong in separate modules." |
| 2 — Plan | "Plan the Modular Billing Application folder and module responsibilities." |
| 3 — Example | "Show a minimal import from a package submodule." |
| 4 — Guided implementation | "Guide me to create billing/pricing.py and test its import from main.py." |
| 5 — Explanation | "Explain module, package, import path and the __name__ guard." |
| 6 — Debugging | "Help me diagnose this ModuleNotFoundError using my folder structure." |
| 7 — Review | "Review my package for clear responsibilities and circular imports." |

**Planning prompt:** "Help me divide my billing workflow into pricing, tax and summary modules. Do not write all files for me."

**Implementation prompt:** "Guide me through creating one module at a time and tell me the exact file path for each."

**Debugging/review prompt:** "Inspect my folder tree and import statements. Explain why Python cannot find the module."

## 13. Daily quiz

**Q1. What is a Python module?**  
A. A Python file containing reusable code  
B. A database table  
C. A browser  
D. A network port  
**Correct: A.** A module is an importable Python file.

**Q2. Which file commonly marks a regular package?**  
A. requirements.txt  
B. __init__.py  
C. index.html  
D. manage.py  
**Correct: B.** __init__.py is commonly used to mark and initialize a package.

**Q3. What does `import calculations as calc` do?**  
A. Deletes calculations  
B. Imports the module with alias calc  
C. Creates a database  
D. Runs every function  
**Correct: B.** The alias provides a shorter name for the imported module.

**Q4. What is the purpose of the __name__ guard?**  
A. Prevent direct execution  
B. Run selected code only when the module is executed as the main program  
C. Install packages  
D. Define a class  
**Correct: B.** It separates direct execution behavior from import behavior.

**Q5. Why avoid naming a project file json.py?**  
A. Python cannot run files with underscores  
B. It may shadow the standard-library json module  
C. It deletes JSON data  
D. It changes the Python version  
**Correct: B.** The local file can be imported instead of the intended standard-library module.

## 14. Interview preparation

### Q1. What is the difference between a module and a package?
**Answer:** A module is a single importable Python file. A package organizes related modules under a directory and provides a structured import namespace. For example, billing/pricing.py can be imported as a submodule of billing.

**Follow-up:** What is the role of __init__.py in a regular package?

### Q2. What does if __name__ == "__main__" mean?
**Answer:** Python sets __name__ to "__main__" when the file is run as the entry script. When imported as a module, __name__ is normally the module's name. The guard lets code run only in direct execution mode.

**Follow-up:** Why is this useful in a module containing reusable functions?

## 15. Completion checklist
- [ ] Create and import a custom module.
- [ ] Organize modules into a package.
- [ ] Use selected and aliased imports.
- [ ] Explain the __name__ guard.
- [ ] Complete Modular Billing Application.
- [ ] Resolve and explain an import path.

**Next lesson:** Day 11 — File handling: reading, writing and working with CSV and JSON.
