# Day 10: Interview Questions — Modules, Packages and Python Imports

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a Python module?
**Answer:**
- A module is an importable Python file.
- It can contain variables, functions and classes.
- It supports code reuse and organization.
- It is imported using import statements.

**Follow-up:** How do you import a module with an alias?

### Q2. What is a Python package?
**Answer:**
- A package organizes related modules.
- It usually uses a directory structure.
- A regular package commonly contains __init__.py.
- It allows structured imports such as package.module.

**Follow-up:** Is __init__.py required for every modern package form?

### Q3. Compare import module and from module import name.
**Answer:**
- import module makes the module name available.
- from module import name imports a selected object directly.
- Module-qualified access makes the source of a name clear.
- Avoid star imports in maintainable code.

**Follow-up:** What risk comes from using from module import *?

### Q4. What is the __name__ guard?
**Answer:**
- It checks whether a Python file is running as the main program.
- Direct execution sets __name__ to "__main__".
- Imported modules receive their module name.
- It prevents application entry code from running automatically on import.

**Follow-up:** How does this help with unit testing?

### Q5. What is a circular import?
**Answer:**
- Two or more modules depend on each other during import.
- Their initialization order can leave names unavailable.
- It often indicates responsibilities are too tightly coupled.
- Refactoring shared logic into another module can help.

**Follow-up:** How would you redesign two modules that import each other?

## 2. Scenario-based questions

### Q6. ModuleNotFoundError occurs even though the file exists. What do you inspect?
**Answer:**
- Current working directory.
- Project/package folder structure.
- Import name and spelling.
- Whether the correct interpreter/environment is active.
- Whether the package is on Python's import path.

**Follow-up:** Why should you run the application from the intended project root?

### Q7. Importing your helper module unexpectedly runs the full application. What is the likely issue?
**Answer:**
- Application code may be placed at module top level.
- Move executable workflow into a main() function.
- Use the __name__ guard.
- Keep reusable definitions separate from startup behavior.

**Follow-up:** What code should generally stay at module level?

## 3. Project questions

### Q8. Explain Modular Billing Application.
**Answer:**
- I created a billing package.
- I separated pricing, tax and summary responsibilities.
- I imported functions from the package into main.py.
- I used a main guard.
- I tested more than one invoice.

**Follow-up:** How would you add a payment integration module?

### Q9. How should a Python project be organized?
**Answer:**
- Group related code by responsibility.
- Keep the application entry point easy to locate.
- Use clear module and package names.
- Avoid circular imports.
- Add dependency and setup documentation.

**Follow-up:** How does this approach help Django projects?

## 4. Rapid revision
- Module: importable Python file.
- Package: organized collection of modules.
- import: load module.
- from ... import: import selected name.
- Alias: alternate import name.
- __init__.py: regular package initializer.
- __name__ guard: direct-execution check.
- Circular import: cyclic module dependency.
