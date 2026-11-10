# Day 9: Functions, Parameters, Arguments and Return Values

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–8 — variables, conditions, loops and collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Reusable Calculation Toolkit

## 1. Learning objectives

- Explain why functions are used.
- Define and call a function using `def`.
- Distinguish parameters from arguments.
- Return values from functions.
- Use positional, keyword and default arguments.
- Break a small problem into reusable operations.

## 2. What is a function?

A function is a named, reusable block of code that performs a task. Functions reduce repetition and help organize a program into understandable pieces.

For example, a billing program may need to calculate totals in several places. Instead of repeating the calculation, define it once and call it whenever required.

## 3. Define and call a function

```python
def greet():
    print("Welcome to the backend course")

greet()
```

Output:

```text
Welcome to the backend course
```

Explanation:

- `def` starts a function definition.
- `greet` is the function name.
- Parentheses contain parameters, if any.
- The indented block is the function body.
- `greet()` calls the function.

Defining a function does not execute its body. The body runs when the function is called.

## 4. Parameters and arguments

A **parameter** is a name in the function definition. An **argument** is the value supplied when the function is called.

```python
def greet_employee(name):
    print(f"Welcome, {name}")

greet_employee("Asha")
```

- `name` is the parameter.
- `"Asha"` is the argument.

## 5. Functions with multiple parameters

```python
def calculate_total(price, quantity):
    total = price * quantity
    print(total)

calculate_total(250, 3)
```

Output: `750`

The first argument is assigned to `price`, and the second to `quantity`.

## 6. return versus print

`print()` displays a value. `return` sends a value back to the code that called the function.

```python
def calculate_total(price, quantity):
    return price * quantity

total_amount = calculate_total(250, 3)
print(total_amount)
```

Output: `750`

Returning a value makes it possible to reuse the result in another calculation:

```python
def calculate_total(price, quantity):
    return price * quantity

subtotal = calculate_total(200, 2)
tax = subtotal * 0.05
grand_total = subtotal + tax

print(grand_total)
```

Output: `420.0`

A function without an explicit return statement returns `None`.

## 7. Positional and keyword arguments

### Positional arguments

Values are assigned according to their position.

```python
def employee_details(name, department):
    print(name, department)

employee_details("Asha", "Engineering")
```

### Keyword arguments

Values are assigned by parameter name.

```python
employee_details(department="Finance", name="Ravi")
```

Keyword arguments make calls clearer when a function has several parameters.

## 8. Default parameters

A default parameter value is used when the caller does not supply that argument.

```python
def calculate_discount(amount, rate=10):
    return amount * rate / 100

print(calculate_discount(1000))
print(calculate_discount(1000, 15))
```

Output:

```text
100.0
150.0
```

Parameters with default values should follow parameters without defaults in a normal function definition.

## 9. Local variables and scope

A variable created inside a function is normally local to that function.

```python
def calculate_salary():
    basic = 40000
    allowance = 5000
    return basic + allowance

print(calculate_salary())
```

The names `basic` and `allowance` are local variables. Code outside the function cannot directly refer to them.

Prefer passing required values as parameters and returning results instead of relying on many global variables.

## 10. A function can call another function

```python
def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100

subtotal = calculate_subtotal(500, 2)
tax = calculate_tax(subtotal, 5)

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", subtotal + tax)
```

Output:

```text
Subtotal: 1000
Tax: 50.0
Total: 1050.0
```

Each function has one clear responsibility, making the code easier to test and maintain.

## 11. Common mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Function does not run | It was defined but never called | Call it using parentheses |
| Missing argument | Required parameter was not supplied | Pass the required value |
| Confusing parameter and argument | Names are used interchangeably | Parameter is in definition; argument is in call |
| Returning nothing | Function only prints | Use `return` when caller needs the result |
| Code after return does not run | return exits the function | Put required statements before return |
| Too many global variables | Function depends on hidden state | Pass values as parameters |
| Unclear function name | Purpose is difficult to identify | Use descriptive verb-based names |

## 12. Industry scenario

An order management application needs to calculate item totals, discounts and taxes. Separate functions can perform each calculation. The order workflow can call those functions and combine their returned values.

This makes each calculation easier to test and reuse. In real payment workflows, monetary precision and approved business rules must also be considered.

## 13. Approved mini-project — Reusable Calculation Toolkit

**Objective:** Create a Python file containing reusable calculation functions.

### Requirements

Create functions for:

1. Adding two numbers.
2. Calculating the total price from unit price and quantity.
3. Calculating a percentage discount.
4. Calculating the final amount after discount.
5. Returning results rather than printing inside every calculation function.
6. Calling the functions with both positional and keyword arguments.
7. Displaying a small summary using the returned values.

### Suggested structure

```text
reusable_calculation_toolkit/
└── calculations.py
```

### Validation

Try more than one input for each function. Confirm that returned values can be reused in another calculation. State the assumptions for negative values and invalid rates; validation can be added as an extension.

## 14. Key takeaways

- Functions group reusable instructions under a name.
- Parameters appear in the function definition; arguments are supplied at the call.
- `return` sends a result to the caller; `print` displays output.
- Positional, keyword and default arguments support different calling styles.
- Local variables belong to the function scope.
- Small functions with clear responsibilities improve readability and testing.

**Next lesson:** Day 10 — Modules, packages and Python imports.
