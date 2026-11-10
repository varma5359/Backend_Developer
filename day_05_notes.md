# Day 5: Conditional Statements and Decision-Making

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–4 — variables, data types, operators and input/output  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Employee Eligibility Checker

> **Beginner note:** A computer follows the instructions we write. It does not automatically understand what is fair, correct or suitable. We must teach it the rules. Today you will learn how to write those rules using conditions.

## 1. What will you learn?

By the end of this lesson, you should be able to:
- Explain why a program needs decision-making.
- Use `if`, `else` and `elif`.
- Compare values using comparison operators.
- Combine conditions using `and`, `or` and `not`.
- Understand indentation and the order of conditions.
- Use conditions to make a simple business decision.

## 2. Why do we need conditions?

Imagine a college registration system. A student can register only if the student is at least 18 years old. The application needs to check the student's age.

Another example: an employee can request a training benefit only if:
- The employee is active.
- The employee has completed one year of service.
- The required training is complete.

These are rules. A program needs to check the rules and choose what to do.

A **condition** is an expression that evaluates to either `True` or `False`.

Example:
```python
age = 21
print(age >= 18)
```

Output:
```text
True
```

Explanation:
- `age` contains 21.
- `>=` means greater than or equal to.
- 21 is greater than or equal to 18, so the answer is `True`.

Change age to 16 and run the code again. The result becomes `False`.

## 3. The if statement — execute code only when a condition is true

Syntax:
```python
if condition:
    statements
```

The colon `:` marks the beginning of the block. The indented statements belong to the if block.

Beginner example:
```python
age = 22

if age >= 18:
    print("You are eligible to register")

print("Program completed")
```

Output:
```text
You are eligible to register
Program completed
```

Line-by-line:
1. `age = 22` stores the age.
2. `if age >= 18:` checks whether the age is at least 18.
3. Because the condition is true, Python executes the indented print statement.
4. The final print statement is outside the if block, so it runs regardless of the condition.

Now change age to 16:

Output:
```text
Program completed
```

The eligibility message is skipped because the condition is false.

## 4. The else statement — what should happen when the condition is false?

Sometimes the program needs to choose between two alternatives. Use `else` for the alternative branch.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:
```text
Minor
```

How Python works:
- It checks the if condition first.
- If true, it executes the if block and skips else.
- If false, it skips the if block and executes else.
- Exactly one of these two branches executes.

Try age 25. The output will be `Adult`.

## 5. The elif statement — check more than two possibilities

Suppose an exam system assigns a grade:
- 90 or above: A
- 75 to 89: B
- 60 to 74: C
- Below 60: Needs improvement

There are more than two possible outcomes. Use `elif`, which means "else if".

```python
score = 78

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Needs improvement")
```

Output: `Grade B`

Important: Python checks conditions from top to bottom. When it finds the first true condition, it runs that block and skips the remaining branches.

Why order matters:
- If `score >= 60` were checked first, a score of 95 would match it.
- Python would print Grade C and never reach the Grade A condition.
- Therefore, check the highest threshold first in this example.

## 6. Comparison operators inside conditions

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | True |
| `!=` | Not equal to | `5 != 3` | True |
| `>` | Greater than | `8 > 4` | True |
| `<` | Less than | `2 < 4` | True |
| `>=` | Greater than or equal | `5 >= 5` | True |
| `<=` | Less than or equal | `4 <= 5` | True |

Example:
```python
salary = 45000

if salary > 30000:
    print("Salary is above 30000")
```

Output: `Salary is above 30000`

Remember: `=` assigns a value; `==` compares values.

## 7. The and operator — every condition must be true

Suppose an employee is eligible only if:
- Employment status is active.
- Experience is at least one year.

Both requirements must be satisfied. Use `and`.

```python
employment_status = "active"
experience = 2

if employment_status == "active" and experience >= 1:
    print("Eligible for training benefit")
else:
    print("Not eligible")
```

Output: `Eligible for training benefit`

Change experience to 0. The output becomes `Not eligible`.

Think of `and` as "this must be true AND that must also be true".

## 8. The or operator — at least one condition must be true

Suppose an internal report can be viewed by an admin or a manager.

```python
role = "manager"

if role == "admin" or role == "manager":
    print("Access allowed")
else:
    print("Access denied")
```

Output: `Access allowed`

If the role is admin, the condition is true. If the role is manager, it is also true. If it is student, both sides are false.

Think of `or` as "this condition OR that condition can be true".

## 9. The not operator — reverse a Boolean value

`not` changes True to False and False to True.

```python
is_blocked = False

if not is_blocked:
    print("Account can continue")
```

Output: `Account can continue`

Read `not is_blocked` as "the account is not blocked".

## 10. Combine conditions and use parentheses

A more realistic rule may say: the user must be active and must be either an admin or a manager.

```python
is_active = True
role = "manager"

if is_active and (role == "admin" or role == "manager"):
    print("Can access the management report")
else:
    print("Access denied")
```

Output: `Can access the management report`

The parentheses make the intended grouping clear:
1. Check whether the role is admin or manager.
2. Check whether the account is active.
3. Both the active check and role check must pass.

Use parentheses when they make a complex condition easier to read.

## 11. Nested if — one decision inside another

A nested if is an if statement inside another if block.

```python
age = 22
identity_verified = True

if age >= 18:
    if identity_verified:
        print("Registration can continue")
    else:
        print("Please verify your identity")
else:
    print("Minimum age requirement not met")
```

Output: `Registration can continue`

Read it step by step:
1. Check age.
2. If age is at least 18, check identity verification.
3. If identity is verified, allow registration to continue.
4. If age is below 18, the inner check is never reached.

Nested conditions are useful when one decision depends on another. Too many nested blocks can become difficult to read, so keep the logic simple.

## 12. Truthy and falsy values

Python can use values other than True and False directly in a condition.

Common falsy values include:
- `False`
- `None`
- `0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)

Example:
```python
email = ""

if not email:
    print("Email is required")
else:
    print("Email was provided")
```

Output: `Email is required`

This checks whether the string is empty. It does not prove that a non-empty email is valid.

## 13. Common mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Using `=` in a condition | Confusing assignment with comparison | Use `==` |
| Missing colon | Forgetting Python block syntax | Add `:` after if/elif/else |
| Incorrect indentation | Python uses indentation to define blocks | Use consistent four-space indentation |
| Wrong elif order | A broad condition matches too early | Put more restrictive conditions first |
| Using or instead of and | Translating the rule incorrectly | Write the business rule in plain English first |
| Treating a non-empty email as valid | Presence is not the same as validity | Use an appropriate validation rule |

## 14. Industry scenario

An employee portal receives a request for training reimbursement. The backend checks the employee's status, service duration and training completion. The backend must perform these checks when the request arrives. Hiding a button in the frontend is not sufficient because users can send requests through other means.

Today you are learning the decision logic. Authentication and database-backed permissions will be taught in later phases.

## 15. Interview preparation

**Q1. What is the difference between if, elif and else?**

Answer: `if` checks the first condition. `elif` checks another condition if earlier conditions were false. `else` runs when none of the preceding conditions matched.

Follow-up: Can we use multiple elif blocks?  
Answer: Yes. We can use as many elif branches as needed before an optional else.

**Q2. What is the difference between and and or?**

Answer: `and` requires all conditions to be true. `or` requires at least one condition to be true.

Follow-up: Which operator is suitable when an employee must be active and have at least one year of experience?  
Answer: `and`, because both requirements must be satisfied.

**Q3. Why is indentation important in Python?**

Answer: Indentation identifies which statements belong to a block, such as an if or else block. Incorrect indentation can cause an error or change the program's logic.

## 16. Approved mini-project — Employee Eligibility Checker

**Objective:** Decide whether an employee meets a training-program eligibility policy.

### Rules
An employee is eligible only when:
1. Employment status is `active`.
2. Experience is at least one year.
3. Required training is completed.

### Requirements
1. Store employee name, employment status, experience and training completion.
2. Normalize status text using `.strip().lower()` if you collect it as input.
3. Check each requirement.
4. Display Eligible or Not eligible.
5. Explain which requirement was not met.
6. Test all three requirements separately.

### Test cases

| Status | Experience | Training complete | Expected |
|---|---:|---|---|
| active | 2 | yes | Eligible |
| active | 0 | yes | Not eligible |
| inactive | 3 | yes | Not eligible |
| active | 2 | no | Not eligible |

For the first version, use values assigned in the file. You can add terminal input as an extension.

## 17. Daily practice and completion check

1. Write an if statement to check whether a number is positive.
2. Write if/else to check whether a person is at least 18.
3. Assign a grade using if/elif/else.
4. Check whether a user is active and is an admin.
5. Explain the difference between and, or and not.
6. Explain why condition order matters.

You have completed Day 5 when you can translate a plain-English rule into a correct Python condition and explain why each branch runs.

**Next lesson:** Day 6 — Loops: for, while, break and continue.
