# Day 12: Interview Questions — Exception Handling, Debugging and Basic Logging

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is an exception?
**Answer:**
- An event that interrupts normal program execution.
- Can occur at runtime.
- Examples include ValueError, KeyError and FileNotFoundError.
- Can be handled using try and except.

**Follow-up:** What is the difference between an exception and a syntax error?

### Q2. Explain try and except.
**Answer:**
- try contains statements that may raise an exception.
- except handles a matching exception type.
- Specific exception handling is easier to understand and debug.
- The program can provide a clear message or take recovery action.

**Follow-up:** Why should you avoid catching every exception without a specific reason?

### Q3. Explain else and finally.
**Answer:**
- else runs when the try block completes without an exception.
- finally runs when control leaves the try construct, whether an exception occurred or not.
- finally is useful for cleanup.
- Context managers are often preferred for resources such as files.

**Follow-up:** What happens if an exception occurs inside the try block?

### Q4. What is raise?
**Answer:**
- raise explicitly signals an exception.
- It can communicate an invalid input or state.
- A caller can catch the exception.
- It helps make validation rules explicit.

**Follow-up:** Which exception would you raise for a negative salary?

### Q5. What is logging?
**Answer:**
- A way to record application events.
- It supports severity levels such as DEBUG, INFO, WARNING, ERROR and CRITICAL.
- It helps developers diagnose application behavior.
- Logs should not contain secrets or unnecessary personal data.

**Follow-up:** Which log level would you use for a failed operation?

## 2. Scenario-based questions

### Q6. A program crashes while converting a salary string to float. What do you do?
**Answer:**
- Read the exception type and traceback.
- Check the exact input value.
- Handle ValueError for malformed numeric text.
- Display a useful message.
- Add a test for valid and invalid salary values.

**Follow-up:** Should invalid salary be silently converted to zero?

### Q7. A report file cannot be opened because it does not exist. How should the program respond?
**Answer:**
- Identify the FileNotFoundError.
- Decide whether the file should be created or the operation should be rejected.
- Use the correct file mode and path.
- Log a useful event without exposing sensitive data.
- Test the missing-file scenario.

**Follow-up:** What is the difference between read mode and write mode?

### Q8. A developer catches Exception and ignores it. Why is this risky?
**Answer:**
- It can hide programming defects.
- It makes failures difficult to diagnose.
- It may let the program continue with invalid state.
- Catch expected exceptions, log useful context and re-raise when recovery is not safe.

**Follow-up:** When is a broad exception handler justified at an application boundary?

## 3. Project and phase assessment questions

### Q9. Explain Error Handling and Report Generator.
**Answer:**
- I read employee rows from a file or in-memory source.
- I validated required fields.
- I converted salary values and handled invalid rows.
- I recorded accepted/rejected counts.
- I wrote a report and used logging for processing events.

**Follow-up:** How did you prevent sensitive employee information from appearing in logs?

### Q10. Explain your Python Employee Management System.
**Answer:**
- I represented employees as dictionaries stored in a list.
- I used functions for add, display, search and update operations.
- I prevented duplicate IDs and validated salary values.
- I persisted data to JSON or CSV.
- I handled invalid input and file errors.
- I generated a summary and tested save/reload behavior.

**Follow-up:** What would change when this application moves from local files to PostgreSQL?

### Q11. How do you debug a Python program?
**Answer:**
- Reproduce the issue.
- Read the traceback.
- Identify the failing line and exception.
- Inspect variable values and types.
- Use a small test case or debugger breakpoint.
- Fix the root cause and rerun tests.

**Follow-up:** What is the advantage of a debugger over adding many print statements?

## 4. Rapid revision
- Syntax error: code cannot be parsed.
- Exception: runtime failure or exceptional condition.
- try: statements that may fail.
- except: handles a matching exception.
- else: runs when try succeeds.
- finally: cleanup path.
- raise: explicitly signal an exception.
- logging: record application events by severity.
- traceback: error location and call history.
