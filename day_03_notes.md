# Day 3: Variables, Data Types, Type Conversion and Operators

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–2 — backend overview and Python environment  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Employee Salary Calculator

## 1. Learning objectives

- Explain variables and assignment.
- Identify common Python built-in data types.
- Check a value's type using `type()`.
- Convert compatible values between types.
- Use arithmetic, comparison, logical and assignment operators.
- Apply these concepts to simple business calculations.

## 2. What is a variable?

A variable is a name that refers to a value. Variables let us store information and reuse it later.

```python
employee_name = "Asha"
employee_age = 25
monthly_salary = 45000

print(employee_name)
print(employee_age)
print(monthly_salary)
```

Expected output:

```text
Asha
25
45000
```

- `employee_name`, `employee_age` and `monthly_salary` are variable names.
- `=` is the assignment operator. It binds the name on the left to the value on the right.
- `print()` displays each value.

Python is dynamically typed: you do not declare a variable's type in advance. The value has a type, and a name can later refer to a value of another type.

```python
value = 100
print(type(value))

value = "one hundred"
print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

## 3. Rules for naming variables

Good variable names explain what the value represents.

Valid examples:

```python
employee_id = 101
total_amount = 2500
is_active = True
customer_name = "Ravi"
```

Naming rules:

- A name can contain letters, digits and underscores.
- A name cannot begin with a digit.
- Names are case-sensitive: `salary` and `Salary` are different.
- Python keywords such as `if`, `for` and `class` cannot be used as variable names.
- Use descriptive `snake_case` names for variables and functions.

Avoid unclear names such as `x1`, `a` or `temp` when a descriptive name would make the program easier to understand.

## 4. Common Python data types

A data type describes the kind of value being represented.

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `employee_count = 12` |
| `float` | Decimal number | `salary = 45000.50` |
| `str` | Text | `name = "Asha"` |
| `bool` | True or false | `is_active = True` |
| `NoneType` | Absence of a value | `middle_name = None` |

Check types:

```python
employee_id = 101
salary = 45000.75
name = "Asha"
is_active = True
manager_name = None

print(type(employee_id))
print(type(salary))
print(type(name))
print(type(is_active))
print(type(manager_name))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

### 4.1 Integer

Use an integer for whole-number quantities such as counts and identifiers.

```python
number_of_employees = 25
print(number_of_employees + 5)
```

Output: `30`

An employee ID may be stored as an integer if it is used numerically. If an identifier can contain leading zeroes or letters, a string may be more appropriate.

### 4.2 Float

Use a float for values that need a fractional part.

```python
unit_price = 149.50
quantity = 3
total = unit_price * quantity

print(total)
```

Output: `448.5`

Floating-point values use binary representation and may not represent every decimal fraction exactly. For financial systems, Python's `decimal.Decimal` is often more suitable than float for exact decimal arithmetic. That is an advanced topic; the mini-project can use simple values while recognizing this limitation.

### 4.3 String

A string stores text.

```python
first_name = "Asha"
department = 'Engineering'

print(first_name)
print(department)
```

Strings can use single or double quotes. The opening and closing quote types must match.

### 4.4 Boolean

A boolean has one of two values: `True` or `False`.

```python
is_verified = True
has_access = False

print(is_verified)
print(has_access)
```

Booleans are useful for representing conditions such as whether an account is active or a payment is verified.

### 4.5 None

`None` represents the absence of a value.

```middle_name = None

print(middle_name)
print(type(middle_name))
```

Use `None` when a value is currently unavailable or intentionally not set. Do not confuse it with the text `"None"` or the number `0`.

## 5. Type conversion

Type conversion changes a value from one type to another when the conversion is valid.

Common functions:

| Function | Purpose | Example |
|---|---|---|
| `int()` | Convert to integer when possible | `int("25")` |
| `float()` | Convert to float when possible | `float("25.5")` |
| `str()` | Convert to text | `str(101)` |
| `bool()` | Convert to boolean using truth-value rules | `bool(1)` |

### Example 1 — string to integer

```python
age_text = "25"
age = int(age_text)

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

### Example 2 — string to float

```python
salary_text = "45000.75"
salary = float(salary_text)

print(salary + 1000)
```

Output: `46000.75`

### Example 3 — number to string

```python
employee_id = 101
message = "Employee ID: " + str(employee_id)

print(message)
```

Output: `Employee ID: 101`

### Invalid conversion

```python
quantity = int("five")
```

This raises `ValueError`, because the text `"five"` is not an integer representation. You will learn to handle this safely with exception handling on Day 12.

## 6. Operators in Python

An operator performs an operation on one or more values.

### 6.1 Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 3` | 13 |
| `-` | Subtraction | `10 - 3` | 7 |
| `*` | Multiplication | `10 * 3` | 30 |
| `/` | Division | `10 / 3` | 3.333... |
| `//` | Floor division | `10 // 3` | 3 |
| `%` | Remainder | `10 % 3` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

```python
price = 200
quantity = 3

total = price * quantity
print(total)
```

Output: `600`

### 6.2 Comparison operators

Comparison operators produce a boolean result.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

```python
salary = 45000

print(salary >= 30000)
print(salary == 45000)
print(salary != 0)
```

Output:

```text
True
True
True
```

Do not confuse `=` (assignment) with `==` (comparison).

### 6.3 Logical operators

Logical operators combine or reverse conditions.

- `and`: true when both conditions are true.
- `or`: true when at least one condition is true.
- `not`: reverses a truth value.

```python
salary = 45000
is_active = True

eligible = salary >= 30000 and is_active
print(eligible)
```

Output: `True`

Python evaluates logical expressions using short-circuit behavior: in an `and` expression, it may stop once the result is known to be false; in an `or` expression, it may stop once the result is known to be true.

### 6.4 Assignment operators

```python
total = 100
total += 50
total -= 10
total *= 2

print(total)
```

Output: `280`

For example, `total += 50` means update total by adding 50.

## 7. Operator precedence

Python follows precedence rules. Parentheses make the intended order explicit.

```python
result = 10 + 5 * 2
print(result)

result_with_parentheses = (10 + 5) * 2
print(result_with_parentheses)
```

Output:

```text
20
30
```

Multiplication is evaluated before addition. Use parentheses when they improve readability or avoid ambiguity.

## 8. Practical example — calculate employee monthly pay

```python
employee_name = "Asha"
basic_salary = 40000
allowance = 5000
deduction = 2000

gross_salary = basic_salary + allowance
net_salary = gross_salary - deduction

print("Employee:", employee_name)
print("Gross salary:", gross_salary)
print("Net salary:", net_salary)
```

Output:

```text
Employee: Asha
Gross salary: 45000
Net salary: 43000
```

Interpretation:

- Gross salary is basic salary plus allowance.
- Net salary is gross salary minus the deduction.
- The example is a simplified calculation, not a complete payroll or tax calculation.

## 9. Common mistakes

| Mistake | Why it happens | Better approach |
|---|---|---|
| Adding a number to numeric text | Input is a string | Convert and validate the input |
| Using `=` in a comparison | Assignment and equality look similar | Use `==` for comparison |
| Converting `"12.5"` with `int()` | Decimal text is not a direct integer representation | Use `float()` if a decimal is required |
| Treating `None` as text | Confusing a value with a string | Compare with `is None` |
| Using unclear variable names | Names do not describe meaning | Use descriptive snake_case |
| Assuming float is exact for money | Binary floating-point representation | Learn Decimal for financial precision |

## 10. Industry scenario

An employee salary calculator receives basic salary, allowance and deductions. The program must distinguish text received from a form from numeric values used in calculations. If a salary arrives as text, it must be converted and validated before arithmetic is performed.

This is a small example of a common backend responsibility: validate incoming data before using it in business logic.

## 11. Connection to the approved mini-project

**Employee Salary Calculator**

The calculator should use descriptive variables for employee name, basic salary, allowance and deductions. It should calculate gross and net salary and display a clear summary.

Use the day's concepts:

- Strings for employee name.
- Numeric values for salary components.
- Arithmetic operators for calculations.
- Comparison operators later when checking allowed ranges.
- Type conversion when handling numeric text.

Keep the assumptions explicit. Do not present the simplified calculation as a real payroll or tax engine.

## 12. Key takeaways

- Variables give reusable names to values.
- Python has built-in types such as int, float, str, bool and NoneType.
- `type()` helps inspect a value's type.
- Convert input carefully before performing calculations.
- Arithmetic operators calculate; comparison operators return booleans.
- Logical operators combine conditions.
- Use clear variable names and parentheses to make code readable.

**Next lesson:** Day 4 — Input/output, string formatting and user interaction.
