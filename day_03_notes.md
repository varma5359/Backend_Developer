# Day 3: Variables, Data Types, Type Conversion and Operators

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–2 — backend overview and Python environment  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Employee Salary Calculator

> **Before you start:** Today you will learn how a program remembers information and performs calculations. Do not try to memorize every term at once. Run each small code example, compare the output and then change the values yourself.

## 1. What will you learn?

By the end of this lesson, you should be able to:
- Create variables and assign values.
- Identify common Python data types.
- Check a value's type using `type()`.
- Convert compatible values using `int()`, `float()` and `str()`.
- Perform calculations with arithmetic operators.
- Compare values using comparison operators.
- Combine conditions using logical operators.
- Apply these ideas to an employee salary calculation.

## 2. What is a variable?

Imagine that you are calculating an employee's salary. You need to remember the employee's name, basic salary and allowance while the program runs.

A **variable** is a name that refers to a value. It lets you store information and use that information later.

```python
employee_name = "Asha"
monthly_salary = 45000
department = "IT"

print(employee_name)
print(monthly_salary)
print(department)
```

Output:

```text
Asha
45000
IT
```

Understand each line:
- `employee_name` is a variable name.
- `=` is the assignment operator. It assigns the value on the right to the name on the left.
- `"Asha"` is a text value.
- `45000` is an integer value.
- `print()` displays the value.

A useful mental picture is a label attached to a value. The label `employee_name` lets you refer to the value `"Asha"`.

### Changing a variable

```python
salary = 30000
print(salary)

salary = 35000
print(salary)
```

Output:

```text
30000
35000
```

The name `salary` refers to the new value after the second assignment.

## 3. Rules for naming variables

Good variable names make programs easier to understand.

Valid examples:
```python
student_name = "Ravi"
age = 21
monthly_salary = 45000
total_amount = 2500
```

Invalid examples:
- `2name` — a variable name cannot start with a digit.
- `student-name` — a hyphen is not allowed in a normal variable name.
- `class` — this is a reserved Python keyword.

Recommended naming style is lowercase words separated by underscores. This style is called **snake_case**.

Prefer `employee_salary` over `x` because the first name explains what the value represents.

## 4. What is a data type?

A data type tells Python what kind of value is being represented. Different types support different operations.

Consider these values:

```python
name = "Asha"
age = 22
salary = 45000.50
is_active = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Let's understand each type.

### 4.1 String — str

A string stores text. Write text inside single or double quotation marks.

```python
employee_name = "Asha"
city = 'Hyderabad'

print(employee_name)
print(city)
```

Output:
```text
Asha
Hyderabad
```

Examples of strings:
- Names.
- Email addresses.
- Department names.
- Product descriptions.
- Status values such as `"active"`.

Even if a phone number contains only digits, it is often stored as text because we do not normally add or multiply phone numbers.

### 4.2 Integer — int

An integer is a whole number without a decimal part.

```python
age = 25
number_of_employees = 120

print(age)
print(number_of_employees)
print(type(age))
```

Output:
```text
25
120
<class 'int'>
```

Examples include age, quantity and the number of completed orders.

### 4.3 Float — float

A float represents a number with a decimal part.

```python
price = 250.75
percentage = 12.5

print(price)
print(percentage)
print(type(price))
```

Output:
```text
250.75
12.5
<class 'float'>
```

Floats are useful for many measurements and calculations. For financial applications, decimal arithmetic is often preferred over binary floating-point arithmetic because decimal currency values need predictable precision. You will learn more about this when working on real payment logic.

### 4.4 Boolean — bool

A Boolean value has only two possibilities: `True` or `False`.

```python
is_logged_in = True
is_blocked = False

print(is_logged_in)
print(is_blocked)
print(type(is_logged_in))
```

Output:
```text
True
False
<class 'bool'>
```

Boolean values are useful for questions such as:
- Is the account active?
- Is payment completed?
- Is the user verified?

Remember to write `True` and `False` with capital first letters.

## 5. Check the type using type()

The built-in `type()` function tells you the type of a value.

Syntax:
```python
type(value)
```

Example:
```python
price = 500
print(type(price))
```

Output:
```text
<class 'int'>
```

Explanation:
1. Python reads the value stored in `price`.
2. `type(price)` asks Python for the value's type.
3. `print()` displays the result.

Use `type()` when you are unsure what type a variable contains. It is especially helpful when debugging input and conversion problems.

## 6. What is type conversion?

Sometimes a value is stored in one type, but your calculation needs another type. **Type conversion** changes a value from one type to another when the conversion is valid.

### 6.1 Convert text to integer using int()

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

Explanation:
- `age_text` contains text, even though it looks like digits.
- `int(age_text)` converts the text `"25"` into integer `25`.
- The converted result is stored in `age`.

If the text is `"twenty"`, Python cannot convert it to an integer and raises `ValueError`. Error handling is covered on Day 12.

### 6.2 Convert to float using float()

```python
price_text = "250.75"
price = float(price_text)

print(price)
print(type(price))
```

Output:
```text
250.75
<class 'float'>
```

Use `float()` when a decimal number is needed.

### 6.3 Convert a number to text using str()

```python
employee_id = 101
employee_id_text = str(employee_id)

print(employee_id_text)
print(type(employee_id_text))
```

Output:
```text
101
<class 'str'>
```

The displayed value looks similar, but its type is now a string. You can combine it with other text more easily.

### 6.4 A common conversion mistake

```python
age = "25"
# print(age + 5)  # This causes a TypeError
```

Why? Python cannot add a string and an integer using the `+` operator.

Correct version:

```python
age = "25"
age = int(age)
print(age + 5)
```

Output:
```text
30
```

## 7. Arithmetic operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor division | `11 // 5` | 2 |
| `%` | Remainder | `11 % 5` | 1 |
| `**` | Power | `2 ** 3` | 8 |

Run this example:

```python
first_number = 10
second_number = 3

print(first_number + second_number)
print(first_number - second_number)
print(first_number * second_number)
print(first_number / second_number)
print(first_number // second_number)
print(first_number % second_number)
print(first_number ** second_number)
```

Output:
```text
13
7
30
3.3333333333333335
3
1
1000
```

Understand the difference between `/` and `//`:
- `/` performs normal division and returns a float.
- `//` performs floor division, rounding the result down toward negative infinity.

The remainder operator `%` is useful for checking whether a number is divisible by another number.

## 8. Assignment operators

Assignment operators update a variable.

```python
total = 100
total += 50
print(total)

total -= 20
print(total)

total *= 2
print(total)
```

Output:
```text
150
130
260
```

What does `total += 50` mean? It is a shorter way of writing `total = total + 50`.

Other operators include `-=`, `*=`, `/=`, `//=` and `%=`.

## 9. Comparison operators

Comparison operators compare two values. Their result is Boolean: `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 10` |

Example:
```python
age = 22

print(age >= 18)
print(age == 18)
print(age != 18)
```

Output:
```text
True
False
True
```

Important difference:
- `=` assigns a value.
- `==` compares two values.

This is one of the most common beginner interview and coding mistakes.

## 10. Logical operators

Logical operators combine or reverse Boolean conditions.

### and

Both conditions must be true.

```python
age = 25
has_id = True

print(age >= 18 and has_id)
```

Output: `True`

If either condition is false, the complete `and` expression is false.

### or

At least one condition must be true.

```python
is_admin = False
is_manager = True

print(is_admin or is_manager)
```

Output: `True`

### not

`not` reverses a Boolean value.

```python
is_blocked = False
print(not is_blocked)
```

Output: `True`

You will use these operators with `if` conditions on Day 5.

## 11. Put the concepts together: salary calculation

Suppose an employee has:
- Basic salary: ₹30,000.
- House allowance: ₹5,000.
- Travel allowance: ₹2,000.

```python
employee_name = "Asha"
basic_salary = 30000
house_allowance = 5000
travel_allowance = 2000

total_salary = basic_salary + house_allowance + travel_allowance

print("Employee:", employee_name)
print("Basic salary:", basic_salary)
print("Total salary:", total_salary)
```

Output:
```text
Employee: Asha
Basic salary: 30000
Total salary: 37000
```

The computer adds the three numeric values and stores the result in `total_salary`. The employee name is text, while salary amounts are numeric values.

## 12. Common beginner mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Using `=` to compare | Assignment and comparison are confused | Use `==` for comparison |
| Adding text and a number | Input may be a string | Convert the value first |
| Writing `true` instead of `True` | Boolean capitalization is forgotten | Use `True` and `False` |
| Naming a variable `2salary` | Variable name starts with a digit | Start with a letter or underscore |
| Dividing by zero | Denominator is zero | Check the denominator before division |
| Assuming phone numbers are integers | Digits look numeric | Store identifiers and phone numbers as strings |

## 13. Interview preparation

**Question 1: What is a variable in Python?**

Answer: A variable is a name that refers to a value. It allows us to store information and use it again in a program.

Follow-up: Can a Python variable refer to values of different types at different times?  
Answer: Yes. Python is dynamically typed, so a name can be assigned a value of another type.

**Question 2: What is the difference between a list of data types and a variable's type?**

Answer: A variable refers to a value, and `type()` tells us the type of the value currently referenced by that variable.

**Question 3: What is the difference between `=` and `==`?**

Answer: `=` assigns a value to a variable. `==` compares two values and returns True or False.

**Question 4: Why do we convert input before calculation?**

Answer: Python's `input()` returns text. If we want to perform numeric calculations, we need to convert compatible input to an integer or float.

## 14. Approved mini-project — Employee Salary Calculator

**Objective:** Create a beginner-level program that calculates an employee's total monthly salary from separate salary components.

### Inputs

- Employee name.
- Basic salary.
- House allowance.
- Travel allowance.

### Requirements

1. Store the employee name in a string variable.
2. Store salary amounts as numeric values.
3. Calculate total salary using arithmetic operators.
4. Display the employee name and each salary component.
5. Display the final total.
6. Use meaningful variable names.
7. Check the data types using `type()` during development.

### Example data

```python
employee_name = "Asha"
basic_salary = 30000
house_allowance = 5000
travel_allowance = 2000
```

### Expected result

```text
Employee: Asha
Basic salary: 30000
House allowance: 5000
Travel allowance: 2000
Total salary: 37000
```

### Test cases

| Basic | House | Travel | Expected total |
|---:|---:|---:|---:|
| 30000 | 5000 | 2000 | 37000 |
| 25000 | 3000 | 1500 | 29500 |
| 40000 | 6000 | 2500 | 48500 |

For the first version, assign values directly in the Python file. User input and validation are taught on Day 4. Do not add tax or deductions because those rules are outside today's mini-project.

## 15. Daily practice and completion check

1. Create variables for your name, age, city and whether you are a student.
2. Print each value and its type.
3. Convert the text `"250"` into an integer.
4. Calculate the total of three product prices.
5. Compare two numbers using `>` and `==`.
6. Explain the difference between `and` and `or`.

You have completed Day 3 when you can explain variables, identify the four basic data types, convert simple values and perform calculations without copying the examples.

**Next lesson:** Day 4 — Input/output, string formatting and user interaction.
