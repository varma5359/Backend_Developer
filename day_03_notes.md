# Day 3: Variables, Data Types, Type Conversion and Operators

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–2; Python environment and running a script  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Employee Salary Calculator

## 1. Learning objectives
- Create variables and assign values.
- Identify common Python data types.
- Convert values between compatible types.
- Use arithmetic, comparison and logical operators.
- Calculate an employee salary using clear intermediate variables.

## 2. What is a variable?
A variable is a name that refers to a value.

```python
employee_name = "Asha"
monthly_salary = 45000
is_active = True

print(employee_name)
print(monthly_salary)
print(is_active)
```

Expected output:
```text
Asha
45000
True
```

Python does not require you to declare a variable's type separately. The type is associated with the value at runtime.

## 3. Common data types

| Type | Example | Use |
|---|---|---|
| int | `25` | Whole numbers |
| float | `45000.50` | Decimal numbers |
| str | `"Asha"` | Text |
| bool | `True` | True/false conditions |
| NoneType | `None` | No value currently assigned |

Check a value's type:
```python
salary = 45000.50
print(type(salary))
```

Expected output:
```text
<class 'float'>
```

## 4. Naming variables
Prefer meaningful names:
```python
employee_id = 101
basic_salary = 30000
hra = 8000
```

Rules:
- Use letters, digits and underscores.
- Do not start a name with a digit.
- Names are case-sensitive.
- Avoid Python keywords such as `if`, `for` and `class`.
- Use names that describe the stored value.

## 5. Type conversion
Input collected from a terminal with `input()` is text. Convert it before numerical calculations.

```python
salary_text = "45000"
salary = int(salary_text)
print(salary + 5000)
```

Expected output:
```text
50000
```

Common conversions:
```python
age = int("24")
price = float("99.50")
employee_code = str(101)
```

Invalid conversion raises an error:
```python
# int("forty")  # ValueError
```

Do not assume every string contains a valid number. Validate or handle conversion errors in later lessons.

## 6. Operators

### Arithmetic operators
| Operator | Meaning | Example |
|---|---|---|
| + | Addition | 10 + 3 = 13 |
| - | Subtraction | 10 - 3 = 7 |
| * | Multiplication | 10 * 3 = 30 |
| / | Division | 10 / 3 |
| // | Floor division | 10 // 3 = 3 |
| % | Remainder | 10 % 3 = 1 |
| ** | Exponent | 2 ** 3 = 8 |

```python
basic_salary = 30000
bonus = 5000
total = basic_salary + bonus
print(total)
```

Expected output: `35000`.

### Comparison operators
`==`, `!=`, `>`, `<`, `>=`, `<=` compare values and return a Boolean.

```python
monthly_salary = 45000
print(monthly_salary >= 30000)
print(monthly_salary == 45000)
```

Expected output:
```text
True
True
```

### Logical operators
- `and`: both conditions must be true.
- `or`: at least one condition must be true.
- `not`: reverses a Boolean value.

```python
experience = 2
training_completed = True

eligible = experience >= 1 and training_completed
print(eligible)
```

Expected output: `True`.

## 7. Assignment operators
```python
salary = 30000
salary += 5000  # same effect as salary = salary + 5000
salary -= 1000
print(salary)
```

Expected output: `34000`.

## 8. Worked example — salary calculation
```python
basic_salary = 30000
hra = 8000
travel_allowance = 2000
deductions = 1500

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - deductions

print("Gross salary:", gross_salary)
print("Net salary:", net_salary)
```

Expected output:
```text
Gross salary: 40000
Net salary: 38500
```

Explanation:
1. Add basic salary, HRA and travel allowance.
2. Store the total in gross_salary.
3. Subtract deductions.
4. Store the result in net_salary.
5. Display both amounts.

These are illustrative salary components, not a payroll or tax calculation.

## 9. Industry scenario
A payroll application calculates an employee's monthly gross and net salary. Backend code must keep values numeric, apply correct arithmetic and avoid mixing text with numerical values.

For a real payroll system, rules for tax, provident fund, rounding, currency and statutory deductions must be defined by the organization.

## 10. Approved mini-project — Employee Salary Calculator

**Objective:** Calculate an employee's gross and net monthly salary from supplied salary components.

### Requirements
1. Store employee name and ID.
2. Store basic salary, HRA and allowance.
3. Store total deductions.
4. Calculate gross salary.
5. Calculate net salary.
6. Display an organized salary summary.
7. Use meaningful variable names and appropriate numeric types.

**Suggested structure**
```text
employee_salary_calculator/
└── salary_calculator.py
```

Example values for manual testing:
- Employee: Asha, ID 101
- Basic: 30,000
- HRA: 8,000
- Allowance: 2,000
- Deductions: 1,500

Expected gross: 40,000. Expected net: 38,500.

### Validation
- Ensure numerical fields use int or float.
- Ensure deductions do not exceed gross salary unless your requirements explicitly support a negative net result.
- Check that the output labels are clear.
- Test a second employee with different figures.

## 11. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| Hint | "Give me one hint for choosing numeric data types for salary values." |
| Plan | "Break the Employee Salary Calculator into variables, calculations and output." |
| Example | "Show a small example that calculates gross salary from three components." |
| Guided implementation | "Guide me through the gross salary calculation first, then wait." |
| Explanation | "Explain the difference between /, // and % with simple numbers." |
| Debugging | "Help me understand this TypeError in my salary calculation." |
| Review | "Review my program for clear variable names, correct formulas and test cases." |

**Planning prompt:** "Help me list the inputs, formulas, outputs and validation checks for the Employee Salary Calculator. Do not write the full program."

**Implementation prompt:** "Guide me one calculation at a time and explain each variable before moving to the next."

**Debugging/review prompt:** "Inspect my code and explain any type conversion or arithmetic mistakes without replacing the whole program."

## 12. Daily quiz

**Q1. What is the data type of `25`?**  
A. str  
B. int  
C. bool  
D. float  
**Correct: B.** An integer represents a whole number.

**Q2. What does `int("42")` return?**  
A. "42"  
B. 42 as an integer  
C. 42.0  
D. True  
**Correct: B.** The string is converted into an integer.

**Q3. What is the result of `10 % 3`?**  
A. 3  
B. 1  
C. 0  
D. 10  
**Correct: B.** The modulo operator returns the remainder.

**Q4. Which operator checks equality?**  
A. =  
B. ==  
C. +=  
D. !=  
**Correct: B.** A double equals sign compares two values for equality.

**Q5. What is the result of `True and False`?**  
A. True  
B. False  
C. None  
D. 0.5  
**Correct: B.** The AND operation is true only when both operands are true.

## 13. Interview preparation

### Q1. What is the difference between = and == in Python?
**Answer:** A single equals sign assigns a value to a variable. A double equals sign compares two values and returns True or False.

**Example:** `salary = 30000` assigns a value; `salary == 30000` checks it.

**Follow-up:** What does the expression return if the values are different?

### Q2. Why do we use type conversion?
**Answer:** Data often arrives as text, especially from user input or external sources. Converting it to the correct type allows valid calculations and comparisons. Invalid conversion can raise ValueError, so input must be checked.

**Follow-up:** What error can occur when converting "abc" to int?

## 14. Completion checklist
- [ ] Create variables with meaningful names.
- [ ] Identify int, float, str, bool and None.
- [ ] Convert compatible values.
- [ ] Use arithmetic and comparison operators.
- [ ] Complete Employee Salary Calculator.
- [ ] Answer the quiz and interview questions.

**Next lesson:** Day 4 — Input/output, string formatting and user interaction.
