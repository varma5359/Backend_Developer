# Day 5: Conditional Statements and Decision-Making

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–4 — variables, operators and input/output  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Employee Eligibility Checker

## 1. Learning objectives

- Explain how conditions control program flow.
- Use `if`, `elif` and `else`.
- Combine conditions using `and`, `or` and `not`.
- Understand indentation, branch order and truth values.
- Translate simple business rules into Python conditions.

## 2. Why do programs need decisions?

A program often needs to choose what to do based on information.

Examples in backend applications:

- Is a registration form complete?
- Is an employee active?
- Is an order eligible for a discount?
- Does a user have permission to view a report?
- Is a payment amount valid?

A condition is an expression that evaluates to a truth value: `True` or `False`. Python uses that result to decide which block to execute.

## 3. The if statement

Use `if` when an action should happen only when a condition is true.

```python
age = 22

if age >= 18:
    print("Eligible to register")
```

Output:

```text
Eligible to register
```

Explanation:

- `age >= 18` is the condition.
- The colon `:` marks the start of the block.
- The indented `print()` belongs to the if block.
- If the condition is false, the block is skipped.

Python uses indentation to identify blocks. Use consistent four-space indentation.

## 4. if and else

Use `else` to define what happens when the `if` condition is false.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output: `Minor`

Only one of the two branches executes.

## 5. if, elif and else

Use `elif` when there are multiple possible conditions.

```python
score = 76

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Needs improvement"

print(grade)
```

Output: `B`

Python checks branches from top to bottom and executes the first matching branch. Order matters. If `score >= 60` were placed first, a score of 95 would match it and later branches would never be reached.

## 6. Combining conditions

### and

All conditions must be true.

```python
experience = 2
training_completed = True

if experience >= 1 and training_completed:
    print("Eligible for review")
else:
    print("Not eligible")
```

### or

At least one condition must be true.

```python
role = "manager"

if role == "admin" or role == "manager":
    print("Can view team report")
```

### not

Reverses a truth value.

```python
is_blocked = False

if not is_blocked:
    print("Account is not blocked")
```

Use parentheses to make complex conditions easier to read:

```python
is_active = True
is_manager = False
is_admin = True

if is_active and (is_manager or is_admin):
    print("Access review dashboard")
```

## 7. Nested conditions

A nested condition is an `if` statement inside another conditional block.

```python
age = 25
identity_verified = True

if age >= 18:
    if identity_verified:
        print("Registration can continue")
    else:
        print("Complete identity verification")
else:
    print("Minimum age requirement not met")
```

Nesting can express a sequence of decisions. Avoid excessive nesting; a long chain of conditions is harder to maintain. Later, functions can help separate complex business rules.

## 8. Truth values and empty values

Python treats some values as false in a condition:

- `False`
- `None`
- Numeric zero
- Empty string `""`
- Empty list `[]`
- Empty dictionary `{}`

Example:

```python
email = ""

if not email:
    print("Email is required")
else:
    print("Email was provided")
```

This checks whether the string is empty. It does not prove that a non-empty value is a valid email address.

## 9. Common mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Using `=` instead of `==` | Assignment is confused with comparison | Use `==` to compare values |
| Incorrect indentation | Block structure is unclear | Indent each block consistently |
| Broad condition first | Later branches become unreachable | Put specific conditions before broad ones |
| Using `or` instead of `and` | Business rule is translated incorrectly | Write the rule in plain language first |
| Assuming non-empty means valid | Presence and correctness are different | Apply the actual validation rule |
| Too many nested blocks | Decisions are mixed together | Simplify or separate logic |

## 10. Industry scenario

An HR portal checks whether an employee can request a training reimbursement. The rule may require the employee to be active, have completed at least one year of service and have submitted the required training proof.

The backend must evaluate the approved business rules. Hiding or showing a button in the frontend is not sufficient security; the backend must enforce the rule when the request arrives.

## 11. Approved mini-project — Employee Eligibility Checker

**Objective:** Decide whether an employee meets a clearly defined training-program eligibility policy.

### Rules for this exercise

An employee is eligible only when:

- Employment status is `active`.
- Experience is at least one year.
- Required training is completed.

### Requirements

1. Collect employee name.
2. Collect employment status.
3. Collect years of experience.
4. Collect training completion as yes/no.
5. Normalize text input with `.strip().lower()`.
6. Evaluate all three requirements.
7. Display an eligibility decision.
8. Explain which requirement was not met.

### Suggested structure

```text
employee_eligibility_checker/
└── eligibility.py
```

### Test cases

| Status | Experience | Training | Expected result |
|---|---:|---|---|
| active | 2 | yes | Eligible |
| active | 0 | yes | Not eligible |
| inactive | 3 | yes | Not eligible |
| active | 2 | no | Not eligible |

Test each failed requirement separately. Convert experience to a number before comparing it. Assume valid numeric input for the first implementation; robust input error handling is covered on Day 12.

## 12. Key takeaways

- `if` executes a block when its condition is true.
- `elif` checks another condition; `else` handles the remaining case.
- `and` requires all conditions; `or` requires at least one.
- `not` reverses a truth value.
- Python uses indentation to define conditional blocks.
- Translate business rules into plain language before writing conditions.

**Next lesson:** Day 6 — Loops: for, while, break and continue.
