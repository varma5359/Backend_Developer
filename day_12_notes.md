# Day 12: Exception Handling, Debugging and Basic Logging

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–11 — functions, conditions, loops, modules and file handling  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Error Handling and Report Generator

> **Beginner note:** Even when you write correct-looking code, a program can receive unexpected input or fail to find a file. A good developer does not assume that everything will always work. Today you will learn how to understand errors, handle expected failures and record useful information.

## 1. Learning objectives

By the end of this lesson, you should be able to:
- Explain what an exception is.
- Distinguish syntax errors from runtime exceptions.
- Use try and except to handle expected failures.
- Understand else and finally.
- Raise an exception when a value is invalid.
- Read a traceback.
- Use basic VS Code debugging.
- Record events using Python's logging module.

## 2. What is an error?

An error means that something has gone wrong in a program. Some errors prevent Python from understanding the code. Other problems occur while the program is running.

Two beginner categories:
1. Syntax errors.
2. Runtime exceptions.

## 3. Syntax error — Python cannot understand the code

Example with a missing colon:

```python
# Intentionally incorrect example:
# if age >= 18
#     print("Eligible")
```

Correct version:

```python
age = 20

if age >= 18:
    print("Eligible")
```

Output: `Eligible`

The colon is required after the if condition. If the syntax is invalid, Python cannot execute the program normally.

Other syntax problems include unmatched parentheses, missing quotation marks and incorrect indentation.

## 4. Runtime exception — code starts but an operation fails

A runtime exception occurs while Python is executing code.

Example:

```python
number = int("hello")
print(number)
```

This raises `ValueError`. The text "hello" cannot be converted into an integer.

Another example:

```python
result = 10 / 0
```

This raises `ZeroDivisionError`, because division by zero is not allowed.

Other common exceptions:
- FileNotFoundError — requested file cannot be found.
- KeyError — requested dictionary key is missing.
- IndexError — requested list or string index does not exist.
- TypeError — an operation is used with an inappropriate type.
- ValueError — value has the right general type but is not acceptable for the operation.

## 5. What happens when an exception is not handled?

```python
print("Program started")
number = int("hello")
print("Program completed")
```

The first message is printed. Then the conversion fails. The final print statement is not reached.

Python displays a traceback that describes where the error happened.

An unhandled exception usually stops the current flow of the program. In a backend application, an unhandled failure can cause a request to fail.

## 6. Handle an exception using try and except

Use a try block for code that may raise an expected exception. Use an except block to define what should happen when that exception occurs.

```python
try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid whole number.")
```

Example run with invalid input:

```text
Enter your age: twenty
Please enter a valid whole number.
```

Step by step:
1. Python enters the try block.
2. input() receives the text.
3. int() attempts to convert it.
4. The text cannot be converted, so ValueError is raised.
5. Python looks for a matching except block.
6. The ValueError handler runs and displays the message.

If the user enters 20, the conversion succeeds and the print statement displays the age.

## 7. Handle different exception types separately

```python
try:
    amount = float(input("Enter amount: "))
    result = 1000 / amount
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Amount cannot be zero.")
```

There are two possible expected failures:
- If the user enters letters, float() raises ValueError.
- If the user enters zero, division raises ZeroDivisionError.

Separate handlers let you give a useful response for each problem.

## 8. else — run only when no exception occurred

The else block runs when the try block completes without an exception.

```python
try:
    number = int("25")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", number)
```

Output: `Conversion successful: 25`

Use else for work that should happen only when the try operation succeeds.

## 9. finally — run cleanup code

The finally block runs as control leaves the try statement, whether an exception occurred or not.

```python
try:
    number = int("25")
    print(number)
except ValueError:
    print("Invalid number")
finally:
    print("Operation finished")
```

Output:
```text
25
Operation finished
```

If the conversion failed, the except block would run, and finally would still run.

Use finally for cleanup that must happen in either case. For ordinary file handling, a with statement is often simpler because it closes the file automatically.

## 10. Why should we catch specific exceptions?

Avoid this pattern unless you have a clear reason:

```python
try:
    number = int("hello")
except:
    print("Something went wrong")
```

This catches a broad range of exceptions and hides which kind of failure occurred. It may accidentally hide programming mistakes that should be fixed.

Prefer:

```python
try:
    number = int("hello")
except ValueError:
    print("Please provide a whole number")
```

A specific handler documents the failure you expect and makes debugging easier.

## 11. raise — create an exception when a rule is broken

Sometimes Python does not automatically know that a value violates your business rule. Your code can detect the problem and raise an exception.

```python
def calculate_discount(amount, rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if rate < 0 or rate > 100:
        raise ValueError("Rate must be between 0 and 100")

    return amount * rate / 100

print(calculate_discount(1000, 10))
```

Output: `100.0`

Understand:
- The function receives amount and rate.
- It checks whether amount is negative.
- It checks whether rate is outside the range 0 to 100.
- If a rule is broken, raise creates a ValueError with a helpful message.
- If both checks pass, the function calculates and returns the discount.

The caller can handle the exception:

```python
try:
    discount = calculate_discount(1000, 10)
    print(discount)
except ValueError as error:
    print("Calculation error:", error)
```

The variable `error` contains the exception object, and its message can be displayed.

## 12. What is a traceback?

A traceback is Python's report showing the sequence of calls that led to an unhandled exception.

When you see an error:
1. Read the final exception type and message.
2. Find the filename and line number.
3. Open the line mentioned.
4. Inspect the variables used in that statement.
5. Check the types and values.
6. Reproduce the problem with a small input.
7. Correct the cause and test again.

Do not randomly change several lines before understanding the error.

## 13. Debugging using print()

Debugging means finding and correcting the cause of incorrect behavior.

A temporary print can show the value and type of a variable:

```python
amount = "500"

print("Amount value:", amount)
print("Amount type:", type(amount))
```

Output:
```text
Amount value: 500
Amount type: <class 'str'>
```

This tells you that amount is text, not a number. That information can explain why a numeric operation fails.

Print debugging is simple, but remove unnecessary diagnostic prints when the code is ready.

## 14. Debugging using VS Code

VS Code has a debugger that lets you pause a program and inspect it.

Beginner steps:
1. Open your Python file in VS Code.
2. Click beside a line number to create a breakpoint.
3. Open the Run and Debug panel.
4. Start debugging.
5. When execution pauses, inspect the Variables panel.
6. Use Step Over to execute the next line.
7. Use Step Into to enter a called function.
8. Continue execution after understanding the state.

A **breakpoint** is a point where the debugger pauses the program. It helps you inspect values at the exact moment a problem may occur.

## 15. What is logging?

Logging records events while an application runs.

A temporary print statement is useful for a beginner exercise. A real application needs a more organized way to record information such as:
- Application started.
- File import completed.
- Invalid input received.
- A processing operation failed.

Python provides a built-in module named `logging`.

Beginner example:

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Detailed diagnostic")
logging.info("Application started")
logging.warning("Input needs review")
logging.error("Operation failed")
```

With INFO as the configured level, INFO, WARNING, ERROR and CRITICAL messages are normally shown. DEBUG is filtered out.

## 16. Understand logging levels

| Level | Meaning | Example |
|---|---|---|
| DEBUG | Detailed diagnostic information | Internal values during development |
| INFO | Normal application event | Application started |
| WARNING | Unexpected situation that may need attention | Optional field missing |
| ERROR | An operation failed | File import failed |
| CRITICAL | Serious failure | Application cannot continue |

The levels represent increasing severity. Choose a level based on how important the event is.

## 17. Configure a useful log format

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

logging.info("Application started")
logging.warning("One optional field is missing")
logging.error("Could not process the record")
```

Possible output:

```text
INFO:Application started
WARNING:One optional field is missing
ERROR:Could not process the record
```

The format string controls how each message is displayed. Here:
- `%(levelname)s` is replaced by the severity level.
- `%(message)s` is replaced by the log message.

Logging can also be configured to write to a file. Production applications need suitable retention, access controls and monitoring.

## 18. print versus logging

| print() | logging |
|---|---|
| Displays output directly | Records application events through a logging system |
| Useful for normal output and quick checks | Useful for diagnostics and operational events |
| No built-in severity levels | Supports DEBUG, INFO, WARNING, ERROR and CRITICAL |
| Usually displayed in the terminal | Can be directed to files or centralized systems |

Never log passwords, access tokens, private keys or unnecessary personal information.

## 19. Industry scenario

An employee import utility reads a CSV file containing employee IDs and salary values. Some rows may have missing IDs or invalid salary text.

A good program should:
- Identify invalid rows.
- Handle expected conversion errors.
- Record useful diagnostic information.
- Count accepted and rejected records.
- Continue or stop according to a defined processing policy.
- Avoid placing sensitive employee information in logs.

## 20. Common beginner mistakes

| Mistake | Why it is a problem | Better approach |
|---|---|---|
| Catching every exception silently | Hides the actual defect | Catch expected specific exceptions |
| Empty except block | Failure is ignored | Handle or report the problem |
| Putting unrelated code inside try | Makes it unclear which operation may fail | Keep try blocks focused |
| Confusing syntax error and exception | They happen at different stages | Read the error type and message |
| Raising unclear messages | Hard to diagnose | Use meaningful error messages |
| Logging secrets | Exposes sensitive data | Log safe identifiers or summaries only |
| Assuming no crash means correct output | Program may produce wrong results | Test valid and invalid cases |

## 21. Interview preparation

**Q1. What is an exception in Python?**

Answer: An exception is an event that interrupts normal program execution when an operation cannot be completed as expected.

Follow-up: Name three common exceptions.  
Answer: ValueError, TypeError and FileNotFoundError are common examples.

**Q2. Difference between syntax error and runtime exception?**

Answer: A syntax error prevents Python from parsing the code. A runtime exception occurs while Python is executing syntactically valid code.

**Q3. Difference between else and finally?**

Answer: else runs only if the try block completes without an exception. finally runs as control leaves the try statement whether an exception occurred or not.

**Q4. Why use logging instead of print?**

Answer: Logging supports severity levels and configurable output, making it more useful for application diagnostics and operations.

**Q5. What is a traceback?**

Answer: A traceback shows the call sequence and source locations associated with an exception, helping a developer find where the failure occurred.

## 22. Approved mini-project — Error Handling and Report Generator

**Objective:** Read employee records, validate values, handle expected errors and generate a processing report.

Example input:

```csv
employee_id,name,salary
101,Asha,45000
102,Ravi,not_available
103,Meera,52000
,John,40000
```

### Requirements
1. Accept employee data from a CSV file or a list of dictionaries.
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
- Confirm accepted and rejected counts match the input.
- Confirm logs do not contain sensitive values.

## 23. Phase 1 revision and completion

Phase 1 covered:
- Day 1: Backend development concepts.
- Day 2: Python environment setup.
- Day 3: Variables, types, conversion and operators.
- Day 4: Input, output and formatting.
- Day 5: Conditional statements.
- Day 6: Loops.
- Day 7: Strings and methods.
- Day 8: Lists, tuples, sets and dictionaries.
- Day 9: Functions.
- Day 10: Modules and packages.
- Day 11: File handling, CSV and JSON.
- Day 12: Exceptions, debugging and logging.

Before moving to Phase 2, make sure you can write a small Python program that uses variables, conditions, loops, collections, functions, imports, file reading and basic exception handling.

**Phase 1 complete:** Python Programming Foundations (Days 1–12).  
**Next phase:** Phase 2 — Web Fundamentals, SQL and Development Tools (Days 13–20).
