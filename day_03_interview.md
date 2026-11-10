# Day 3: Interview Questions — Variables, Data Types, Type Conversion and Operators

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a variable in Python?
**Answer:**
- A variable is a name that refers to a value.
- Python determines the value's type at runtime.
- Variables can be reassigned.
- Use meaningful names that describe the data.

**Example:** `monthly_salary = 45000`.

**Follow-up:** Is Python statically or dynamically typed?

### Q2. Name common Python data types.
**Answer:**
- int: whole numbers.
- float: decimal numbers.
- str: text.
- bool: True or False.
- NoneType: absence of a value.

**Follow-up:** How can you check the type of a variable?

### Q3. What is type conversion?
**Answer:**
- Converting a value from one type to another.
- Common functions include int(), float() and str().
- Conversion succeeds only when the value is compatible.
- Invalid conversion may raise ValueError.

**Example:** `int("25")` returns the integer 25.

**Follow-up:** Why should user input be converted before addition?

### Q4. Explain arithmetic operators.
**Answer:**
- `+` addition.
- `-` subtraction.
- `*` multiplication.
- `/` division.
- `//` floor division.
- `%` remainder.
- `**` exponentiation.

**Follow-up:** What is the difference between / and //?

### Q5. What are comparison and logical operators?
**Answer:**
- Comparison operators compare values and return Boolean results.
- Examples: ==, !=, >, <, >= and <=.
- Logical operators combine or reverse Boolean conditions.
- Examples: and, or and not.

**Follow-up:** What is the result of a and b when a is True and b is False?

## 2. Scenario-based questions

### Q6. A salary is stored as "45000" and addition produces an unexpected result. What is the issue?
**Answer:**
- The value may be a string.
- String addition may concatenate text rather than perform numeric addition.
- Convert the value to int or float after validation.
- Use the appropriate numeric type for the calculation.

**Follow-up:** How would you handle invalid salary text?

### Q7. You need to check whether an employee has at least one year of experience and completed training. Which operator is suitable?
**Answer:**
- Use AND because both conditions must be true.
- Example: `experience >= 1 and training_completed`.
- The result is a Boolean.
- It can be used in a conditional statement in the next lesson.

**Follow-up:** When would OR be appropriate instead?

## 3. Project questions

### Q8. Explain your Employee Salary Calculator.
**Answer:**
- I collected employee information and salary components.
- I used numeric types for monetary values.
- I calculated gross salary by adding components.
- I calculated net salary by subtracting deductions.
- I verified calculations using sample cases.

**Follow-up:** What validations would you add before using this in a real payroll system?

### Q9. Why use meaningful variable names?
**Answer:**
- They make code easier to read.
- They make business formulas easier to review.
- They reduce confusion when debugging.
- They help other developers maintain the program.

**Follow-up:** Which name is clearer: x or monthly_salary?

## 4. Rapid revision
- Variable: name referring to a value.
- int: whole number.
- float: decimal number.
- str: text.
- bool: Boolean value.
- Type conversion: changing compatible data types.
- ==: equality comparison.
- =: assignment.
- and/or/not: logical operators.
