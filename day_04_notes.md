# Day 4: Input/Output, String Formatting and User Interaction

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–3 — variables, data types, conversion and operators  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** User Registration Simulator

## 1. Learning objectives

- Read user input using `input()`.
- Understand why `input()` returns a string.
- Convert input into appropriate data types.
- Display values using `print()`.
- Format strings using f-strings.
- Validate simple input before using it.
- Explain the difference between a terminal input program and a web form.

## 2. What are input and output?

**Input** is information supplied to a program. **Output** is information produced by a program.

For a terminal program:

- `input()` reads text typed by the user.
- `print()` displays information in the terminal.

```python
name = input("Enter your name: ")
print("Welcome", name)
```

Example run:

```text
Enter your name: Asha
Welcome Asha
```

The prompt inside `input()` tells the user what to enter.

## 3. Important: input() returns a string

Even if a user types digits, `input()` returns text.

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If the user enters 25:

```text
25
<class 'str'>
```

Convert the value before doing numeric calculations:

```python
age_text = input("Enter your age: ")
age = int(age_text)

print(age + 1)
```

If the input is `25`, the output is `26`.

If the user enters `twenty-five`, `int()` raises a `ValueError`. Day 12 covers structured exception handling. For now, test with valid input and understand why conversion is required.

## 4. Reading different kinds of input

### Example 1 — text input

```python
full_name = input("Enter full name: ")
print("Name:", full_name)
```

### Example 2 — integer input

```python
number_of_items = int(input("Enter item count: "))
print("Items:", number_of_items)
```

### Example 3 — decimal input

```python
unit_price = float(input("Enter unit price: "))
print("Unit price:", unit_price)
```

Use the conversion that matches the expected data. Do not convert every input to an integer; quantities, prices and names have different data requirements.

## 5. Display output using print()

The `print()` function displays one or more values.

```python
name = "Asha"
age = 25

print(name, age)
print("Name:", name, "Age:", age)
```

Output:

```text
Asha 25
Name: Asha Age: 25
```

By default, `print()` separates multiple values with a space and ends with a newline.

You can change the separator:

```python
print("2026", "11", "10", sep="-")
```

Output: `2026-11-10`

You can change the ending:

```python
print("Please wait", end=" ")
print("Completed")
```

Output: `Please wait Completed`

These options are useful for controlling simple terminal output.

## 6. String formatting

String formatting inserts values into readable text.

### 6.1 f-strings

An f-string starts with the letter `f` before the quote. Put a variable or expression inside curly braces.

```python
name = "Asha"
salary = 45000

print(f"Employee: {name}")
print(f"Monthly salary: {salary}")
```

Output:

```text
Employee: Asha
Monthly salary: 45000
```

You can include an expression:

```python
basic_salary = 40000
allowance = 5000

print(f"Gross salary: {basic_salary + allowance}")
```

Output: `Gross salary: 45000`

### 6.2 Format decimal places

```python
price = 125.6789
print(f"Price: {price:.2f}")
```

Output: `Price: 125.68`

The `.2f` format displays two digits after the decimal point. It formats the display; it does not change the original variable.

### 6.3 Alignment and width

```python
item = "Notebook"
price = 120

print(f"{item:<15} {price:>8}")
```

The text field is left-aligned in a width of 15 characters, and the price is right-aligned in a width of 8. This can help create simple terminal reports.

## 7. Combine input, conversion and formatting

```python
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))

gross_salary = basic_salary + allowance

print("\nEmployee Salary Summary")
print("-----------------------")
print(f"Employee: {employee_name}")
print(f"Basic salary: {basic_salary:.2f}")
print(f"Allowance: {allowance:.2f}")
print(f"Gross salary: {gross_salary:.2f}")
```

Example run:

```text
Enter employee name: Asha
Enter basic salary: 40000
Enter allowance: 5000

Employee Salary Summary
-----------------------
Employee: Asha
Basic salary: 40000.00
Allowance: 5000.00
Gross salary: 45000.00
```

The `\n` at the beginning of the heading creates a blank line.

## 8. Basic input validation

Validation checks whether input meets the rules required by the program.

Example — reject an empty name:

```python
name = input("Enter your name: ").strip()

if name == "":
    print("Name is required")
else:
    print(f"Welcome, {name}")
```

- `.strip()` removes whitespace from the beginning and end.
- The comparison checks whether the remaining text is empty.
- The program displays a message based on the result.

Example — basic email text check:

```python
email = input("Enter email: ").strip()

if "@" in email:
    print("Email contains @")
else:
    print("Email should contain @")
```

This is only a beginner demonstration, not complete email validation. Real applications need stronger validation and often confirmation through an email message.

Validation should happen on the backend even if a frontend form performs checks.

## 9. Terminal interaction versus a web form

| Terminal program | Web application |
|---|---|
| Reads input using `input()` | Receives submitted HTTP request data |
| Displays output using `print()` | Returns an HTTP response or renders a page |
| Runs in a terminal session | Runs through a server and client |
| Useful for early Python practice | Used for browser-based user interaction |

The logic is related, but Django does not use `input()` to collect browser form submissions. Later, Django views and forms will handle web requests.

## 10. Common mistakes and troubleshooting

| Problem | Why it happens | How to correct it |
|---|---|---|
| Adding input text to a number | `input()` returns str | Convert with `int()` or `float()` |
| ValueError during conversion | User entered incompatible text | Validate and handle conversion errors |
| Extra spaces in a name | User typed spaces around text | Use `.strip()` |
| F-string shows braces literally | Missing `f` prefix or incorrect braces | Use `f"Hello {name}"` |
| Decimal output has too many digits | Default float display | Use `{value:.2f}` for display |
| Empty value accepted | No required-field check | Check for an empty string |

## 11. Industry scenario

A registration workflow collects a person's name, email and phone number. A backend service must check that required fields are present and that values are in an expected format before saving them.

A terminal simulator helps learn input and output. A production registration endpoint will receive request data from a browser or mobile application and perform server-side validation.

Never log or display passwords unnecessarily. Passwords should be handled using secure authentication practices taught later.

## 12. Connection to the approved mini-project

**User Registration Simulator**

Create a terminal-based program that asks for a user's name, email and age, then displays a formatted registration summary.

Practice:

- Reading text using `input()`.
- Converting age to an integer.
- Removing accidental whitespace.
- Checking required values.
- Displaying a readable summary with f-strings.

Keep the program focused on input and output. Authentication, password storage and database persistence are not part of this day's scope.

## 13. Key takeaways

- `input()` reads user input as a string.
- Convert input before performing numeric calculations.
- `print()` displays program output.
- f-strings make formatted output readable.
- `.strip()` removes surrounding whitespace.
- Validate data before using or storing it.
- Terminal input is different from browser form submission in Django.

**Next lesson:** Day 5 — Conditional statements and decision-making.
