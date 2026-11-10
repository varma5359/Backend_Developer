# Day 9: Functions, Parameters, Arguments and Return Values

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–8; variables, conditions, loops and collections  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Reusable Calculation Toolkit

## 1. Learning objectives
- Explain why functions are used.
- Define and call a function using `def`.
- Distinguish parameters and arguments.
- Return a value from a function.
- Use positional, keyword and default arguments.
- Organize repeated calculations into reusable functions.

## 2. What is a function?
A function is a named, reusable block of code that performs a task. Instead of repeating the same calculation in different places, define it once and call it whenever required.

**Flow:** Define function → call function → provide arguments → execute function body → receive result (if returned).

## 3. Create and call a function
```python
def greet():
    print("Welcome to Python Backend Development")

greet()
```

Expected output:
```text
Welcome to Python Backend Development
```

Explanation:
- `def` starts a function definition.
- `greet` is the function name.
- Parentheses hold parameters when needed.
- The indented statement is the function body.
- `greet()` calls the function.

The function body does not run merely because the function is defined.

## 4. Parameters and arguments
A **parameter** is a variable named in a function definition. An **argument** is the value supplied when the function is called.

```python
def greet_employee(name):  # name is a parameter
    print(f"Welcome, {name}")

greet_employee("Asha")     # "Asha" is an argument
```

Output: `Welcome, Asha`.

## 5. Multiple parameters
```python
def calculate_total(price, quantity):
    total = price * quantity
    print("Total:", total)

calculate_total(250, 3)
```

Output: `Total: 750`.

The first argument is assigned to price and the second to quantity when positional arguments are used.

## 6. Return values
`return` sends a result back to the caller.

```python
def calculate_total(price, quantity):
    return price * quantity

amount = calculate_total(250, 3)
print(amount)
```

Output: `750`.

Difference:
- `print()` displays a value.
- `return` gives a value back so other code can use it.

A function without an explicit return statement returns `None`.

## 7. Positional and keyword arguments

Positional:
```python
def employee_details(name, department):
    print(name, department)

employee_details("Asha", "IT")
```

Keyword:
```python
employee_details(department="HR", name="Ravi")
```

Keyword arguments name the parameter, making calls clearer and allowing a different order.

## 8. Default arguments
A default value is used when the caller does not provide that argument.

```python
def calculate_discount(amount, rate=0.10):
    return amount * rate

print(calculate_discount(1000))
print(calculate_discount(1000, 0.20))
```

Output:
```text
100.0
200.0
```

Default arguments are useful for optional settings. Avoid mutable default values such as empty lists for state that should be created separately on each call.

## 9. Scope: local variables
A variable created inside a function is normally local to that function.

```python
def show_salary():
    salary = 45000
    print(salary)

show_salary()
```

The variable salary is created inside the function. Code outside the function cannot normally refer to that local variable.

Prefer passing required values as arguments and returning results instead of relying on global variables.

## 10. Practical validation inside a function
```python
def calculate_net_salary(gross_salary, deductions):
    if gross_salary < 0 or deductions < 0:
        return None

    if deductions > gross_salary:
        return None

    return gross_salary - deductions

print(calculate_net_salary(40000, 2500))
```

Output: `37500`.

This example returns None for invalid combinations. In later work, you will use exceptions to communicate invalid input more explicitly.

## 11. Functions and backend development
Backend code uses functions to separate responsibilities:
- Validate request data.
- Calculate totals.
- Format a response.
- Apply a business rule.
- Reuse a query or transformation.

A Django view is a callable function or class-based handler that participates in processing a web request. You will meet Django views later in the pathway.

## 12. Common beginner mistakes
| Mistake | Explanation / correction |
|---|---|
| Defining but never calling | The body will not execute until called |
| Forgetting parentheses | Use function_name() to call |
| Printing instead of returning | Printed text cannot be assigned as the return result |
| Argument count mismatch | Provide required arguments or define defaults |
| Incorrect order | Use keyword arguments for clarity |
| Relying on global state | Pass values in and return results |

## 13. Approved mini-project — Reusable Calculation Toolkit

**Objective:** Build a small Python module containing reusable business calculation functions.

### Requirements
Create functions for:
1. Calculating the total price from unit price and quantity.
2. Calculating a percentage discount.
3. Calculating the final amount after discount.
4. Calculating simple interest.
5. Returning a formatted summary for a calculation.

Use parameters and return values. Do not place all calculations directly at the top level of the file.

**Suggested structure**
```text
reusable_calculation_toolkit/
└── calculations.py
```

**Sample checks**
- Unit price 250 × quantity 3 → total 750.
- Amount 1000 with 10% discount → discount 100.
- Amount 1000 after a 10% discount → final amount 900.
- Principal 5000, rate 5%, time 2 years → simple interest 500.

### Validation
- Test zero quantity and zero discount.
- Test a non-default discount rate using a keyword argument.
- Confirm each calculation function returns a value.
- Confirm the summary function does not perform unrelated calculations.

## 14. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for deciding what should become a reusable function." |
| 2 — Plan | "Break Reusable Calculation Toolkit into small functions and test cases." |
| 3 — Example | "Show a tiny function that accepts two values and returns their product." |
| 4 — Guided implementation | "Guide me to write calculate_total first; wait for my test output." |
| 5 — Explanation | "Explain parameters, arguments, return and local scope using my code." |
| 6 — Debugging | "Help me diagnose why my function returns None." |
| 7 — Review | "Review my functions for clear names, single responsibilities and correct return values." |

**Planning prompt:** "Help me identify the inputs, outputs and responsibility of each function. Do not write the complete toolkit."

**Implementation prompt:** "Guide me to implement one function at a time and ask me to test it before moving on."

**Debugging/review prompt:** "Inspect my function calls and return values. Explain any mismatch without replacing the entire file."

## 15. Daily quiz

**Q1. Which keyword defines a Python function?**  
A. function  
B. def  
C. return  
D. import  
**Correct: B.** The def keyword begins a function definition.

**Q2. In `def add(a, b)`, what are a and b?**  
A. Arguments  
B. Parameters  
C. Modules  
D. Return values  
**Correct: B.** They are parameters named in the function definition.

**Q3. What does return do?**  
A. Displays a value only  
B. Sends a result back to the caller  
C. Defines a loop  
D. Imports a package  
**Correct: B.** The caller can store or use the returned result.

**Q4. What does a function return when it has no explicit return statement?**  
A. 0  
B. False  
C. None  
D. Empty string  
**Correct: C.** Python functions return None by default when no value is returned explicitly.

**Q5. Which call uses a keyword argument?**  
A. `calculate(100, 2)`  
B. `calculate(amount=100, rate=2)`  
C. `calculate()`  
D. `calculate[100]`  
**Correct: B.** The argument is associated with a parameter name.

## 16. Interview preparation

### Q1. What is the difference between a parameter and an argument?
**Answer:** A parameter is the variable named in a function definition. An argument is the actual value supplied when the function is called. For example, in `def greet(name)`, name is a parameter; in `greet("Asha")`, "Asha" is the argument.

**Follow-up:** What happens if a required parameter is not supplied?

### Q2. What is the difference between print and return?
**Answer:** print displays information to the output stream. return passes a value back to the caller and ends the function execution. Returned values can be stored, tested or used in further calculations.

**Follow-up:** What value is returned if a function reaches its end without return?

## 17. Completion checklist
- [ ] Define and call functions.
- [ ] Use positional and keyword arguments.
- [ ] Use default arguments.
- [ ] Return results and explain None.
- [ ] Complete Reusable Calculation Toolkit.
- [ ] Test normal and boundary inputs.

**Next lesson:** Day 10 — Modules, packages and Python imports.
