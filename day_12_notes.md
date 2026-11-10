# Day 12: Exception Handling, Debugging and Basic Logging

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–11; functions, conditions, loops, modules and file handling  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Error Handling and Report Generator

## 1. Learning objectives
- Explain the difference between syntax errors and runtime exceptions.
- Handle expected errors using try and except.
- Use else and finally appropriately.
- Raise an exception when an input violates a rule.
- Debug a Python program using error messages and simple breakpoints.
- Record application events using the logging module.

## 2. What is an exception?
An exception is an event that interrupts the normal execution of a program.

Examples:
- Dividing by zero.
- Converting invalid text to an integer.
- Opening a file that does not exist.
- Accessing a missing dictionary key.

Without suitable handling, an unhandled exception may stop the current operation and produce a traceback.

## 3. Syntax error versus runtime exception
Syntax error: Python cannot parse the code.

```python
# Missing colon causes a syntax error
# if age >= 18
#     print("Eligible")
```

Runtime exception: code is syntactically valid but an operation fails while running.

```python
number = int("hello")
```

This raises ValueError because the text cannot be converted to an integer.

## 4. try and except
Place code that may fail inside try. Use except to handle a specific expected exception.

```python
try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid whole number.")
```

Example:
```text
Enter age: twenty
Please enter a valid whole number.
```

Avoid catching every exception without a reason. Specific exception handling makes defects easier to detect.

## 5. Multiple exception types
```python
try:
    amount = float(input("Enter amount: "))
    result = 1000 / amount
    print(result)
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("Amount cannot be zero.")
```

Each except block handles a specific failure.

## 6. else and finally
- else runs when the try block completes without an exception.
- finally runs whether an exception occurred or not.

```python
try:
    number = int("25")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", number)
finally:
    print("Operation finished")
```

Expected output:
```text
Conversion successful: 25
Operation finished
```

Use finally for cleanup that must happen regardless of success or failure. For file handling, a with statement is often simpler and preferred.

## 7. raise an exception
Use raise when your code detects an invalid state and wants to report it.

```python
def calculate_discount(amount, rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if rate < 0 or rate > 100:
        raise ValueError("Rate must be between 0 and 100")

    return amount * rate / 100
```

The caller can handle the exception:
```python
try:
    discount = calculate_discount(1000, 10)
    print(discount)
except ValueError as error:
    print("Calculation error:", error)
```

## 8. Debugging basics
Debugging is the process of finding and fixing the cause of incorrect behavior.

A useful sequence:
1. Read the complete error message.
2. Find the last relevant line in the traceback.
3. Identify the file and line number.
4. Inspect the values and types used at that line.
5. Reproduce the issue with a small input.
6. Fix the cause.
7. Run the test again.

Use print temporarily to inspect values:
```python
amount = "500"
print("amount:", amount, "type:", type(amount))
```

VS Code also supports breakpoints and stepping through code:
- Set a breakpoint beside the suspicious line.
- Start the debugger.
- Inspect variables.
- Step over or into statements.
- Continue execution after understanding the state.

## 9. Basic logging
Logging records events while a program runs. It is more configurable than using print statements for every diagnostic message.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

logging.debug("Detailed diagnostic")
logging.info("Application started")
logging.warning("Input needs review")
logging.error("Operation failed")
```

The configured INFO level normally displays INFO, WARNING, ERROR and CRITICAL messages, but not DEBUG.

Common levels:
- DEBUG: detailed diagnostic information.
- INFO: normal application events.
- WARNING: unexpected situation that may need attention.
- ERROR: an operation failed.
- CRITICAL: serious failure.

Do not log passwords, access tokens, private keys or unnecessary personal data. Production logging needs thoughtful format, retention and access controls.

## 10. Industry scenario
An employee import utility reads a file containing employee IDs and salary fields. Some rows may have missing or invalid values. The tool should identify a bad row, record a useful diagnostic message and continue or stop according to a documented rule, rather than failing without context.

## 11. Approved mini-project — Error Handling and Report Generator

**Objective:** Read simple employee records, validate their values, handle expected errors and generate a processing report.

### Requirements
1. Accept employee data from a small CSV or a list of dictionaries.
2. Validate required fields such as employee ID and salary.
3. Convert salary text to a numeric value.
4. Handle missing or malformed values without an unhandled crash.
5. Track how many rows were processed, accepted and rejected.
6. Write a report file containing summary counts.
7. Use logging to record application start, invalid row and completion.
8. Do not include sensitive employee data in logs.

**Suggested structure**
```text
error_handling_report_generator/
├── main.py
├── employees.csv
├── reports/
│   └── processing_report.txt
└── README.md
```

**Example input rows**
```csv
employee_id,name,salary
101,Asha,45000
102,Ravi,not_available
103,Meera,52000
,John,40000
```

Expected summary:
- Total rows: 4
- Accepted rows: 2
- Rejected rows: 2

The exact report wording is your design choice. Define whether a row is counted as rejected when any required field is invalid.

### Validation
- Test a valid file.
- Test a missing file.
- Test a malformed salary.
- Test a missing employee ID.
- Confirm the report is written.
- Confirm logs do not include sensitive values.
- Confirm the accepted/rejected counts match the test data.

## 12. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for choosing which exception to catch for invalid numeric input." |
| 2 — Plan | "Break Error Handling and Report Generator into loading, validation, counting and reporting steps." |
| 3 — Example | "Show a small try/except example for converting a salary string to float." |
| 4 — Guided implementation | "Guide me to handle a missing CSV file first; wait for my test result." |
| 5 — Explanation | "Explain try, except, else, finally and raise using my employee import scenario." |
| 6 — Debugging | "Help me interpret this traceback and identify the failing line." |
| 7 — Review | "Review my program for exception handling, useful logs and correct row counts." |

**Planning prompt:** "Help me define validation rules, exceptions, report counts and test cases. Do not write the complete program."

**Implementation prompt:** "Guide me one component at a time: file loading, row validation, reporting and logging."

**Debugging/review prompt:** "Inspect my error message and attempted code. Explain the root cause and show the smallest correction."

## 13. Daily quiz

**Q1. Which block contains code that may raise an exception?**  
A. try  
B. else  
C. finally  
D. import  
**Correct: A.** The try block contains code whose exceptions may be handled.

**Q2. Which exception is commonly raised by int("abc")?**  
A. KeyError  
B. ValueError  
C. IndexError  
D. ZeroDivisionError  
**Correct: B.** The string is not a valid integer representation.

**Q3. When does finally execute?**  
A. Only when no error occurs  
B. Only when ValueError occurs  
C. Whether or not an exception occurs, as control leaves the construct  
D. Only at import time  
**Correct: C.** finally is used for cleanup that should run in either case.

**Q4. Which logging level is intended for detailed diagnostic information?**  
A. CRITICAL  
B. DEBUG  
C. ERROR  
D. WARNING  
**Correct: B.** DEBUG is the most detailed common application log level.

**Q5. What is a good debugging first step?**  
A. Delete the program  
B. Read the traceback and identify the failing line  
C. Ignore the error  
D. Reinstall every package  
**Correct: B.** The traceback provides the location and exception type needed to investigate.

## 14. Interview preparation

### Q1. What is exception handling in Python?
**Answer:** Exception handling allows a program to respond to runtime failures using try and except. Specific exception types should be handled so expected problems can be reported or recovered from. else can run after successful execution, and finally can perform cleanup.

**Follow-up:** Why is catching a broad Exception without logging or re-raising often a bad idea?

### Q2. What is the difference between print and logging?
**Answer:** print displays output, often for simple scripts or temporary debugging. Logging provides severity levels and configurable output, making it more suitable for application diagnostics. Logs must be designed so that secrets and sensitive information are not exposed.

**Follow-up:** Which log level would you use for an invalid but recoverable input row?

## 15. Phase 1 cumulative assessment — Python Employee Management System

**Phase:** 1 — Python Programming Foundations (Days 1–12)  
**Assessment project from the approved roadmap:** Python Employee Management System

### Scenario
A small organization currently maintains employee details in separate text files. Build a beginner-level Python program that manages a set of employee records in memory and can save/load records from a file.

### Requirements and constraints
- Use Python fundamentals taught in Days 1–12 only.
- Use functions to separate operations.
- Use collections such as a list of dictionaries.
- Organize code into modules if useful.
- Use JSON or CSV for persistence.
- Handle invalid input and expected file errors.
- Use basic logging for useful operational events.
- Do not build a Django web application or database in this phase.

### Required features
1. Add an employee with ID, name, department and salary.
2. Display all employees.
3. Search for an employee by ID.
4. Update an employee's department or salary.
5. Prevent duplicate employee IDs.
6. Validate required fields and salary values.
7. Save records to JSON or CSV.
8. Load saved records when the program starts.
9. Generate a simple summary report such as employee count and average salary.
10. Display clear success and error messages.

### Suggested structure
```text
python_employee_management_system/
├── main.py
├── employee_manager.py
├── file_storage.py
├── employees.json
├── reports/
│   └── employee_summary.txt
└── README.md
```

### Expected workflow
```text
Start program
    ↓
Load saved employee records
    ↓
Show menu
    ↓
Add / Display / Search / Update / Save / Report
    ↓
Validate input and handle errors
    ↓
Save changes
    ↓
Exit safely
```

### Required test cases

| Test | Input/action | Expected result |
|---|---|---|
| 1 | Add a new unique employee ID | Employee is added |
| 2 | Add an existing employee ID | Duplicate is rejected |
| 3 | Search an existing ID | Correct employee is displayed |
| 4 | Search a missing ID | Clear not-found message |
| 5 | Update an existing employee | Selected fields are changed |
| 6 | Enter a negative salary | Input is rejected |
| 7 | Start when data file is missing | Program initializes an empty record list or reports it safely |
| 8 | Save and restart | Saved employees are loaded |
| 9 | Enter a non-numeric menu choice | Program handles invalid input |
| 10 | Generate summary | Employee count and average salary are correct |

### Assessment rubric

| Assessment dimension | Weight |
|---|---:|
| Conceptual understanding of Python fundamentals | 20% |
| Practical correctness and required features | 30% |
| Problem-solving and reasoning | 20% |
| Code quality, organization and maintainability | 15% |
| Testing, validation and interpretation | 10% |
| Communication and evidence | 5% |
| **Total** | **100%** |

### Common mistakes and validation checks
- Keeping all code in one large script rather than separating responsibilities.
- Using strings for salary calculations without conversion.
- Allowing duplicate IDs.
- Losing saved records by using write mode at the wrong time.
- Catching every exception without identifying the cause.
- Logging sensitive employee information.
- Reporting an average without checking whether the employee list is empty.
- Failing to test persistence across program runs.

### Phase 1 interview questions
1. Explain the difference between a list, tuple, set and dictionary.
2. What is the difference between a parameter and an argument?
3. Why do we use modules and packages?
4. What is the difference between CSV and JSON?
5. Explain try, except, else and finally.
6. How would you prevent duplicate employee IDs in an in-memory application?
7. How would you preserve employee records after the program exits?

### Submission evidence
- Source code and folder structure.
- Sample data file.
- README with setup/run instructions.
- Output screenshots or terminal transcript.
- Evidence for at least ten required test cases.
- Short explanation of the program's functions and data flow.

## 16. Completion checklist
- [ ] Explain syntax errors and runtime exceptions.
- [ ] Handle expected errors with specific except blocks.
- [ ] Use raise for invalid values.
- [ ] Debug using traceback and variable inspection.
- [ ] Use logging levels appropriately.
- [ ] Complete Error Handling and Report Generator.
- [ ] Complete Python Employee Management System assessment.
- [ ] Submit test evidence and explain the implementation.

**Phase 1 complete:** Python Programming Foundations (Days 1–12).  
**Next phase:** Phase 2 — Web Fundamentals, SQL and Development Tools (Days 13–20).
