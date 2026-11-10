# Day 9: Functions, Parameters, Arguments and Return Values

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–8 — variables, conditions, loops, strings and collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Reusable Calculation Toolkit

> **Beginner note:** Imagine you calculate the total price of an order in five different places. Would you copy the same calculation five times? That makes a program difficult to maintain. A function lets you write the operation once and reuse it.

## 1. Learning objectives

By the end of this lesson, you should be able to:
- Explain what a function is and why it is useful.
- Define and call a function using `def`.
- Understand parameters and arguments.
- Use `return` to send a result back.
- Explain the difference between print() and return.
- Use positional, keyword and default arguments.
- Understand local variables and basic scope.
- Divide a small calculation into reusable functions.

## 2. What is a function?

A **function** is a named, reusable block of code that performs a particular task.

Real-life example: A calculator has an addition operation. You provide two numbers, it performs the addition and gives you the result. A Python function can work in a similar way.

Without a function, you may repeat the same instructions in different places. With a function, you define the task once and call it whenever needed.

## 3. Your first function

```python
def greet():
    print("Welcome to Python")

greet()
```

Output:
```text
Welcome to Python
```

Understand every line:
- `def` is the Python keyword used to define a function.
- `greet` is the function name.
- Parentheses contain parameters, if the function needs input.
- The colon starts the function body.
- The indented print statement belongs to the function.
- `greet()` calls the function and makes its body execute.

Important: Defining a function does not automatically run it. You must call it.

Try calling it twice:
```python
greet()
greet()
```
The message appears twice.

## 4. Function naming

Use names that explain the action:
- `calculate_total()`
- `display_employee()`
- `validate_email()`
- `get_student_details()`

Avoid unclear names such as `x()` or `abc()`. Function names commonly use lowercase words separated by underscores, called snake_case.

## 5. Parameters and arguments

A function often needs information to do its work.

```python
def greet_employee(name):
    print(f"Welcome, {name}")

greet_employee("Asha")
```

Output: `Welcome, Asha`

Understand the two important terms:
- **Parameter:** The variable written inside the function definition. Here, `name` is a parameter.
- **Argument:** The actual value supplied when calling the function. Here, `"Asha"` is the argument.

Think of a parameter as an empty input space and the argument as the value you place in that space.

## 6. Function with two parameters

```python
def add_numbers(first_number, second_number):
    result = first_number + second_number
    print(result)

add_numbers(10, 20)
```

Output: `30`

Step by step:
1. Python defines a function with two parameters.
2. The function call supplies 10 and 20.
3. 10 is assigned to first_number.
4. 20 is assigned to second_number.
5. Python adds the values.
6. print() displays 30.

Try `add_numbers(100, 50)`. You do not need to rewrite the function.

## 7. The return statement — send a result back

This is one of the most important function concepts.

First example:
```python
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(10, 20)
print(answer)
```

Output: `30`

What happens?
1. The function receives 10 and 20.
2. It calculates 30.
3. `return result` sends 30 back to the place where the function was called.
4. The returned value is stored in answer.
5. print() displays answer.

The returned result can be used in another calculation:

```python
def calculate_subtotal(price, quantity):
    return price * quantity

subtotal = calculate_subtotal(250, 2)
tax = subtotal * 0.05
grand_total = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Grand total:", grand_total)
```

Output:
```text
Subtotal: 500
Tax: 25.0
Grand total: 525.0
```

This is why return is useful: it allows other parts of the program to use the result.

## 8. Difference between print() and return

| print() | return |
|---|---|
| Displays output | Sends a value back to the caller |
| Mainly for showing information | Used when another part of the program needs the result |
| Does not provide the displayed value as the function result | Makes the returned value available to the caller |
| A function using only print normally returns None | Function returns the specified value |

Example:
```python
def show_total():
    print(100)

def get_total():
    return 100

first_result = show_total()
second_result = get_total()

print("First:", first_result)
print("Second:", second_result)
```

Output:
```text
100
100
First: None
Second: 100
```

Why is the first result None? The function displayed 100 but did not return a value. Python returns None when a function finishes without an explicit return statement.

**Remember:** Use print() to show a result to a person. Use return when the calling code needs to work with the result.

## 9. Positional arguments

Positional arguments are matched to parameters according to their position.

```python
def employee_details(name, department):
    print(f"Name: {name}")
    print(f"Department: {department}")

employee_details("Asha", "Engineering")
```

Output:
```text
Name: Asha
Department: Engineering
```

The first argument goes to name and the second goes to department. Supplying values in the wrong order can produce incorrect results.

## 10. Keyword arguments

Keyword arguments identify the parameter by name.

```python
def employee_details(name, department):
    print(f"Name: {name}")
    print(f"Department: {department}")

employee_details(department="Finance", name="Ravi")
```

Output:
```text
Name: Ravi
Department: Finance
```

The order can be different because the parameter names identify where each value belongs.

## 11. Default parameters

A default parameter has a value that Python uses when the caller does not supply an argument for it.

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}")

greet("Asha")
greet("Ravi", "Good morning")
```

Output:
```text
Welcome, Asha
Good morning, Ravi
```

In the first call, the default message is used. In the second call, the supplied message replaces the default.

Parameters without default values should appear before parameters with default values in a function definition.

## 12. Multiple return values

Python can return more than one value. They are returned together as a tuple and can be unpacked.

```python
def calculate_values(a, b):
    total = a + b
    difference = a - b
    return total, difference

sum_result, difference_result = calculate_values(20, 5)

print(sum_result)
print(difference_result)
```

Output:
```text
25
15
```

This can be useful when one operation produces a few related results.

## 13. Local variables and scope

A variable created inside a function is normally local to that function.

```python
def calculate_salary():
    basic = 40000
    allowance = 5000
    total = basic + allowance
    return total

print(calculate_salary())
```

Output: `45000`

The variables basic, allowance and total are created inside the function. They are local variables and are not directly available outside it.

Prefer passing required values as parameters and returning results. This makes functions easier to understand and test.

## 14. A function can call another function

```python
def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_tax(subtotal, rate):
    return subtotal * rate / 100

subtotal = calculate_subtotal(500, 2)
tax = calculate_tax(subtotal, 5)

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Final:", subtotal + tax)
```

Output:
```text
Subtotal: 1000
Tax: 50.0
Final: 1050.0
```

Each function has one responsibility. One calculates the subtotal; another calculates tax. This separation helps testing and maintenance.

## 15. Common beginner mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Function never runs | It was defined but not called | Call it using parentheses |
| Missing argument | Required parameter was not supplied | Pass the required value |
| Confusing parameter and argument | Both terms sound similar | Parameter is in definition; argument is in call |
| Printing instead of returning | Caller needs a reusable result | Use return |
| Code after return does not run | return exits the function | Put required work before return |
| Wrong positional order | Values are matched by position | Use keyword arguments when clearer |
| Too many global variables | Function depends on hidden state | Pass values as parameters |

## 16. Industry scenario

An order management application needs to calculate item subtotals, discounts and taxes. Separate functions can perform each calculation. The order workflow calls those functions and combines the returned values.

For example:
- calculate_subtotal() receives price and quantity.
- calculate_discount() receives subtotal and discount rate.
- calculate_final_amount() receives subtotal and discount.

The functions should return results so that other code can use them. Production payment calculations require suitable precision and validated business rules.

## 17. Interview preparation

**Q1. What is a function in Python?**

Answer: A function is a reusable block of code that performs a particular task. It is defined using def and called using its name followed by parentheses.

Follow-up: Does defining a function execute it?  
Answer: No. The function body executes when the function is called.

**Q2. Difference between parameter and argument?**

Answer: A parameter is a variable in the function definition. An argument is the actual value supplied during the function call.

**Q3. Difference between print and return?**

Answer: print displays a value. return sends a value back to the caller so it can be stored or used in another expression.

**Q4. What is a default argument?**

Answer: It is a value assigned to a parameter in the function definition. Python uses it when the caller does not supply that argument.

## 18. Approved mini-project — Reusable Calculation Toolkit

**Objective:** Create a Python file containing reusable calculation functions.

### Requirements
Create functions for:
1. Adding two numbers.
2. Calculating total price from unit price and quantity.
3. Calculating a percentage discount.
4. Calculating the final amount after discount.
5. Returning results rather than printing inside every calculation function.
6. Calling functions with positional and keyword arguments.
7. Displaying a summary using returned values.

### Suggested structure
```text
reusable_calculation_toolkit/
└── calculations.py
```

### Validation
Try different inputs for each function. Confirm that returned values can be reused in another calculation. State assumptions for negative values and invalid discount rates; input validation can be added as an extension.

## 19. Daily practice and completion check

1. Write a function that displays a welcome message.
2. Write a function that receives two numbers and returns their sum.
3. Write a function that calculates the total price.
4. Write a function with a default parameter.
5. Call a function using keyword arguments.
6. Explain why a function that only prints returns None.
7. Explain how one function can use another function's result.

You have completed Day 9 when you can write a small function, call it with different values and explain the difference between printing and returning.

**Next lesson:** Day 10 — Modules, packages and Python imports.
