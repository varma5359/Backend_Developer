# Day 12: Exception Handling, Debugging and Basic Logging

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–11 — functions, conditions, loops, modules and file handling  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Error Handling and Report Generator

## 1. Learning objectives

- Distinguish syntax errors from runtime exceptions.
- Handle expected errors using `try` and `except`.
- Use `else` and `finally` appropriately.
- Raise an exception when a value violates a rule.
- Read a traceback and use basic debugging tools.
- Record application events using Python's logging module.

## 2. What is an exception?

An exception is an event that interrupts the normal flow of a program.

Examples:

- Dividing a number by zero.
- Converting invalid text to an integer.
- Opening a file that does not exist.
- Accessing a missing dictionary key.

If an exception is not handled, the current operation may stop and Python displays a traceback containing information about the failure.

## 3. Syntax errors versus runtime exceptions

A **syntax error** occurs when Python cannot parse the code.

```python
# This example is intentionally incorrect:
# if age >= 18
#     print("Eligible")
```

The colon is missing after the condition.

A **runtime exception** occurs when syntactically valid code performs an operation that fails.

```python
number = int("hello")
```

This raises `ValueError` because the text cannot be converted to an integer.

## 4. Handle an exception with try and except

Put code that may fail inside `try`. Use `except` to handle a specific expected exception.

```python
try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid whole number.")
```

Example run:

```text
Enter age: twenty
Please enter a valid whole number.
```

The conversion raises `ValueError`, so Python runs the matching except block.

Avoid catching every possible exception without a reason. Specific exception handling makes defects easier to understand and avoids hiding programming mistakes.

## 5. Handle multiple exception types

Different failures can require different responses.

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

- `ValueError` occurs when the text cannot be converted to a number.
- `ZeroDivisionError` occurs when the denominator is zero.

Each except block handles a different expected problem.

## 6. else and finally

- `else` runs when the try block completes without an exception.
- `finally` runs as control leaves the try statement, whether an exception occurred or not.

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

Output:

```text
Conversion successful: 25
Operation finished
```

Use `finally` for cleanup that must happen in either case. For file handling, a `with` statement is often simpler because it manages file closing automatically.

## 7. Raise an exception

Use `raise` when your own code detects an invalid value or state and needs to report it.

```python
def calculate_discount(amount, rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if rate < 0 or rate > 100:
        raise ValueError("Rate must be between 0 and 100")

    return amount * rate / 100
```

The caller can handle the error:

```python
try:
    discount = calculate_discount(1000, 10)
    print(discount)
except ValueError as error:
    print("Calculation error:", error)
```

Output: `100.0`

If an invalid value is supplied, the function raises an exception and the caller handles it.

## 8. Read a traceback

A traceback is Python's report of the call sequence that led to an exception.

When an error appears:

1. Read the exception type and message at the end.
2. Locate the file and line number mentioned.
3. Inspect the statement on that line.
4. Check the values and types used by the statement.
5. Reproduce the issue with a small input.
6. Correct the cause.
7. Run the program again and test both valid and invalid cases.

Do not randomly change code before understanding the error message.

## 9. Basic debugging

Debugging is the process of finding and correcting the cause of incorrect behavior.

A temporary print can help inspect values:

```python
amount = "500"

print("amount:", amount)
print("type:", type(amount))
```

VS Code also supports a debugger:

1. Open the Python file.
2. Click beside a line number to set a breakpoint.
3. Start debugging.
4. Inspect variable values.
5. Use step over to execute the next line.
6. Use step into to enter a called function.
7. Continue after understanding the program state.

A breakpoint pauses execution so you can inspect what the program is doing at that point.

## 10. Basic logging

Logging records events while a program runs. Unlike temporary print statements, logging supports severity levels and configurable output destinations.

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

With the configured INFO level, INFO, WARNING, ERROR and CRITICAL messages are normally displayed; DEBUG is filtered out.

Common levels:

| Level | Meaning | Example |
|---|---|---|
| DEBUG | Detailed diagnostic detail | Variable or flow information |
| INFO | Normal application event | Application started |
| WARNING | Unexpected situation that may need attention | Optional field missing |
| ERROR | An operation failed | File import failed |
| CRITICAL | Serious failure | Application cannot continue |

Do not log passwords, access tokens, private keys or unnecessary personal information. Production logging also needs suitable retention, access control and monitoring.

## 11. print versus logging

| print | logging |
|---|---|
| Displays output directly | Records events through a configurable logging system |
| Useful for simple output and temporary checks | Useful for application diagnostics |
| No built-in severity levels | Supports DEBUG, INFO, WARNING, ERROR and CRITICAL |
| Usually written for a person at the terminal | Can be directed to files or centralized systems |

Use print for normal output in a small learning script. Use logging for operational events and diagnostics.

## 12. Common mistakes

- Catching a broad exception and silently ignoring it.
- Displaying an error but continuing with invalid data.
- Putting unrelated code inside a try block.
- Confusing a syntax error with a runtime exception.
- Raising an exception without a useful message.
- Logging passwords or tokens.
- Assuming a successful program run proves all inputs are valid.
- Fixing only the visible symptom instead of the root cause.

## 13. Industry scenario

An employee import utility reads a CSV file containing employee IDs and salary values. Some rows may have missing IDs or invalid salary text.

The program should identify invalid rows, record useful diagnostic information and continue or stop according to a defined processing policy. It should not crash without context or include sensitive employee information in its logs.

## 14. Approved mini-project — Error Handling and Report Generator

**Objective:** Read employee records, validate values, handle expected errors and generate a processing report.

### Example input

```csv
employee_id,name,salary
101,Asha,45000
102,Ravi,not_available
103,Meera,52000
,John,40000
```

### Requirements

1. Accept employee data from a small CSV file or a list of dictionaries.
2. Validate required fields such as employee ID and salary.
3. Convert salary text into a numeric value.
4. Handle missing or malformed values without an unhandled crash.
5. Track total, accepted and rejected row counts.
6. Write a report file containing summary counts.
7. Use logging for application start, invalid-row events and completion.
8. Do not include sensitive employee values in logs.

### Expected summary

- Total rows: 4
- Accepted rows: 2
- Rejected rows: 2

Define clearly that a row is rejected when any required field is invalid.

### Suggested structure

```text
error_handling_report_generator/
├── main.py
├── employees.csv
├── reports/
│   └── processing_report.txt
└── README.md
```

### Validation

- Test a valid input file.
- Test a missing file.
- Test a malformed salary.
- Test a missing employee ID.
- Confirm the report is written.
- Confirm the accepted and rejected counts match the input.
- Confirm logs do not contain sensitive values.

## 15. Key takeaways

- Syntax errors prevent Python from parsing code; runtime exceptions occur during execution.
- Use `try` and specific `except` blocks to handle expected failures.
- `else` runs after successful execution; `finally` is used for cleanup.
- `raise` reports invalid values or states.
- Read the traceback before changing code.
- Breakpoints help inspect execution and variables.
- Logging records useful application events at different severity levels.
- Never put secrets in logs.

**Phase 1 complete:** Python Programming Foundations (Days 1–12).  
**Next phase:** Phase 2 — Web Fundamentals, SQL and Development Tools (Days 13–20).
