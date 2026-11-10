# Day 4: Input/Output, String Formatting and User Interaction

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–3 — variables, data types, conversion and operators  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** User Registration Simulator

> **Before you start:** In Day 3, you assigned values directly in the code. Today you will make a program ask the user for information while it is running. Follow each example in the terminal and type the sample input shown.

## 1. What will you learn?

By the end of this lesson, you should be able to:
- Explain input and output.
- Read information using `input()`.
- Explain why `input()` returns a string.
- Convert input into an integer or float when needed.
- Display results using `print()`.
- Format output using f-strings.
- Use basic string formatting options.
- Build a simple terminal-based registration simulator.

## 2. What are input and output?

**Input** is information given to a program. **Output** is information produced by a program.

Think about an ATM:
- You enter a PIN and select an amount. These are inputs.
- The ATM displays your balance or a transaction message. These are outputs.

In a beginner Python terminal program:
- `input()` reads text typed by the user.
- `print()` displays information in the terminal.

## 3. Use input() to collect information

Example:

```python
name = input("Enter your name: ")
print("Welcome", name)
```

Example run:

```text
Enter your name: Asha
Welcome Asha
```

Understand it step by step:
1. Python reaches `input("Enter your name: ")`.
2. It displays the prompt.
3. The program waits for the user to type something.
4. The user types `Asha` and presses Enter.
5. The entered text is returned by `input()`.
6. That text is stored in the variable `name`.
7. `print()` displays the welcome message.

The text inside the parentheses is called the **prompt**. A prompt tells the user what information to enter.

## 4. Important: input() always returns a string

This is one of the most important beginner concepts.

Try this code:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

Example run:

```text
Enter your age: 21
21
<class 'str'>
```

You typed the digits 21, but Python received them as text. Why? Because `input()` returns a string.

### What happens if you try to calculate?

```python
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

print(first_number + second_number)
```

Example run:

```text
Enter first number: 10
Enter second number: 20
1020
```

Why did it display 1020 instead of 30? Both values are strings. The `+` operator joins strings together. This is called concatenation.

## 5. Convert input using int()

If you need whole-number calculations, convert the input to an integer.

```python
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

total = first_number + second_number

print("Total:", total)
```

Example run:

```text
Enter first number: 10
Enter second number: 20
Total: 30
```

Explanation:
- `input()` collects text.
- `int(...)` converts compatible text into an integer.
- The converted number is stored in the variable.
- The `+` operator now performs numeric addition.

If the user enters `ten`, the conversion fails with a `ValueError`. You will learn how to handle this safely on Day 12. For today's first examples, enter valid numbers.

## 6. Convert input using float()

Use `float()` when the user may enter a decimal number.

```python
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total price:", total)
```

Example run:

```text
Enter product price: 125.50
Enter quantity: 2
Total price: 251.0
```

Why use two conversion functions?
- Price may contain a decimal, so use `float()`.
- Quantity is a whole number, so use `int()`.

## 7. Display output using print()

The `print()` function displays values.

### Example 1: Print one value

```python
name = "Asha"
print(name)
```

Output: `Asha`

### Example 2: Print multiple values

```python
name = "Asha"
age = 21

print(name, age)
```

Output: `Asha 21`

By default, print separates multiple values with a space.

### Example 3: Use sep

The `sep` parameter controls the separator between values.

```python
print("Python", "Django", "Backend", sep=" | ")
```

Output:

```text
Python | Django | Backend
```

Explanation:
- `sep` means separator.
- Python places the supplied separator between printed values.
- It does not add the separator at the beginning or end.

### Example 4: Use end

The `end` parameter controls what print adds after its output. By default, it adds a newline.

```python
print("Hello", end=" ")
print("Asha")
```

Output: `Hello Asha`

Because the first print ends with a space rather than a newline, the second output appears on the same line.

## 8. String formatting with f-strings

Suppose you want to display an employee's name and salary. You could use commas in `print()`, but a formatted message can be easier to read.

An **f-string** lets you insert variable values directly inside a string.

```python
name = "Asha"
salary = 45000

print(f"Employee name is {name}")
print(f"Monthly salary is {salary}")
```

Output:

```text
Employee name is Asha
Monthly salary is 45000
```

How does it work?
- Put the letter `f` before the opening quotation mark.
- Write normal text inside the string.
- Put a variable inside curly braces `{}`.
- Python replaces the expression inside braces with its value.

### Use an expression inside an f-string

```python
basic_salary = 30000
allowance = 5000

print(f"Total salary: {basic_salary + allowance}")
```

Output: `Total salary: 35000`

Python evaluates the expression inside the braces and inserts the result.

## 9. Format decimal numbers

Sometimes a calculation produces many decimal digits. You can control how many decimal places are displayed.

```python
price = 125.5678

print(f"Price: {price:.2f}")
```

Output: `Price: 125.57`

Understand `:.2f`:
- `:` starts the formatting instruction.
- `.2` asks for two digits after the decimal point.
- `f` formats the value as a floating-point number.

This changes how the value is displayed; it does not change the original variable.

## 10. Use format() as another formatting method

Python also provides the string `format()` method.

```python
name = "Ravi"
course = "Python"

message = "Student {} is learning {}".format(name, course)
print(message)
```

Output: `Student Ravi is learning Python`

The curly-brace placeholders are filled using the values passed to `format()`, in order.

You may also use named placeholders:

```python
message = "Name: {name}, Course: {course}".format(
    name="Asha",
    course="Django"
)

print(message)
```

Output: `Name: Asha, Course: Django`

For new beginner Python code, f-strings are usually the clearest option. You should still recognize `format()` when reading existing code.

## 11. Multi-line output

You can display a message across multiple lines.

```python
name = "Asha"
course = "Python Backend"

print(f"""
Registration Summary
--------------------
Name: {name}
Course: {course}
Status: Submitted
""")
```

This uses triple quotation marks to create a multi-line string. It is useful for simple reports and readable terminal output.

## 12. A simple user interaction program

Let's combine input, conversion and output.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nStudent Details")
print("----------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

Example run:

```text
Enter your name: Asha
Enter your age: 21
Enter your city: Hyderabad

Student Details
----------------
Name: Asha
Age: 21
City: Hyderabad
```

The sequence is:
1. Collect name as text.
2. Collect age as text and convert it to an integer.
3. Collect city as text.
4. Display a formatted summary.

The sequence `\n` means a newline character. It creates a blank line before the heading.

## 13. How is terminal input different from a web form?

Today's programs collect information using `input()` in the terminal. A real website uses a frontend form to collect information and sends it to a backend through a request.

| Terminal practice | Web application equivalent |
|---|---|
| `input()` | HTML form or frontend input |
| `print()` | Web page or API response |
| Python script | Backend application |
| Values typed in terminal | Values submitted by a client |

The purpose of today's lesson is to understand the input → processing → output pattern. Later, Django will handle web requests rather than asking users to type into the terminal.

## 14. Common beginner mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Adding two inputs gives 1020 | Both values are strings | Convert them using `int()` |
| Decimal input fails with int() | Integer conversion does not accept decimal text such as `"12.5"` | Use `float()` |
| Forgetting quotation marks | Text is interpreted as a variable name | Put text inside quotes |
| Using an undefined variable | Name was never assigned | Check spelling and assignment |
| Expecting `:.2f` to change the stored number | Formatting controls display | Use numeric rounding or decimal logic when changing a value is required |
| Entering text for an integer prompt | Conversion cannot parse the text | Enter valid digits; later add exception handling |

## 15. Interview preparation

**Question 1: What is the purpose of input() in Python?**

Answer: `input()` displays a prompt, waits for the user to enter text and returns the entered value as a string.

Follow-up: What happens if the user enters 25?  
Answer: The returned value is `"25"`, which is a string until it is converted.

**Question 2: Why do we use int() and float()?**

Answer: We use them to convert compatible values into integer and floating-point types so that numeric operations can be performed.

Follow-up: What happens if `int("hello")` is executed?  
Answer: Python raises a `ValueError` because the text cannot be converted to an integer.

**Question 3: What is an f-string?**

Answer: An f-string is a formatted string that allows us to place variable values or expressions inside curly braces within a string prefixed with `f`.

## 16. Approved mini-project — User Registration Simulator

**Objective:** Build a terminal program that collects basic user registration information and displays a formatted confirmation.

### Required inputs

- Full name.
- Age.
- Email address.
- Course name.
- Course fee.

### Requirements

1. Ask the user for each value using `input()`.
2. Convert age to an integer.
3. Convert course fee to a float.
4. Display all details in a readable registration summary.
5. Use f-strings for the summary.
6. Display the course fee with two decimal places.
7. Do not store passwords or sensitive information.
8. For this first version, assume the user enters valid numeric values. Robust error handling comes on Day 12.

### Example run

```text
Enter full name: Asha Rao
Enter age: 21
Enter email: asha@example.com
Enter course: Python Backend
Enter course fee: 12500

REGISTRATION SUMMARY
--------------------
Name: Asha Rao
Age: 21
Email: asha@example.com
Course: Python Backend
Course fee: 12500.00
Registration status: Submitted
```

### Test cases

Try different names, ages, course names and fee amounts. Confirm that text values are displayed correctly and the fee is shown with two decimal places.

## 17. Daily practice and completion check

1. Ask for two numbers and display their sum.
2. Ask for a product price and quantity and display the total.
3. Ask for a student's name and course and display a formatted message.
4. Print three values using `sep`.
5. Print two messages on the same line using `end`.
6. Explain why `input()` returns a string.

You have completed Day 4 when you can collect user input, convert numeric values and produce a readable output without copying the full example.

**Next lesson:** Day 5 — Conditional statements and decision-making.
