# Day 5: Conditional Statements and Decision-Making

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–4; variables, operators and input/output  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Employee Eligibility Checker

## 1. Learning objectives
- Explain how conditional statements control program flow.
- Use if, elif and else.
- Combine conditions with and, or and not.
- Apply nested conditions carefully.
- Implement a simple eligibility decision with understandable output.

## 2. Why do we need conditions?
Programs often need to make decisions.

Examples:
- Is the employee's experience sufficient?
- Is a registration field missing?
- Is the payment amount within the allowed range?
- Is a user allowed to access a resource?

A condition evaluates to True or False, and Python executes the matching block.

## 3. Basic if statement
```python
age = 22

if age >= 18:
    print("Eligible to register")
```

Output:
```text
Eligible to register
```

The indented line belongs to the if block. Python uses indentation to define code blocks.

## 4. if and else
```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output: `Minor`.

The else block runs when the if condition is false.

## 5. if, elif and else
Use elif to check additional alternatives.

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

Output: `B`.

Python evaluates conditions from top to bottom and executes the first matching branch.

## 6. Logical conditions
```python
experience = 2
training_completed = True

if experience >= 1 and training_completed:
    print("Eligible for review")
else:
    print("Not eligible")
```

- AND: every condition must be true.
- OR: at least one condition must be true.
- NOT: reverses a Boolean value.

Example using OR:
```python
role = "manager"

if role == "admin" or role == "manager":
    print("Can view team report")
```

## 7. Nested if
A nested if is a condition inside another condition.

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

Use nesting only when it improves readability. Complex conditions can often be simplified.

## 8. Truth values and common mistakes
Python treats some values as false in conditions, including:
- False
- None
- 0
- Empty string ""
- Empty list []

Example:
```python
email = ""

if not email:
    print("Email is required")
```

This checks whether email is empty. It does not validate email syntax.

Common mistakes:
- Using `=` instead of `==` in a comparison.
- Incorrect indentation.
- Writing conditions in the wrong order.
- Forgetting that elif branches are checked sequentially.
- Using nested conditions that are unnecessarily complex.

## 9. Industry scenario
An HR portal checks whether an employee can request a training reimbursement. Eligibility may depend on employment status, completed service period and whether required documents have been submitted. The backend applies these rules consistently rather than trusting a frontend-only decision.

## 10. Approved mini-project — Employee Eligibility Checker

**Objective:** Decide whether an employee meets a set of clearly defined training-program eligibility rules.

### Example rules for this exercise
An employee is eligible when:
- Employment status is "active".
- Experience is at least 1 year.
- Required training is completed.

### Requirements
1. Collect employee name.
2. Collect employment status.
3. Collect years of experience.
4. Collect training completion (yes/no).
5. Evaluate the three rules.
6. Display eligible or not eligible.
7. Display a clear reason when the employee does not qualify.

**Suggested structure**
```text
employee_eligibility_checker/
└── eligibility.py
```

### Example test cases
| Status | Experience | Training | Expected |
|---|---:|---|---|
| active | 2 | yes | Eligible |
| active | 0 | yes | Not eligible |
| inactive | 3 | yes | Not eligible |
| active | 2 | no | Not eligible |

### Validation
- Convert experience to a number.
- Normalize text input using strip() and lower().
- Test each failed requirement separately.
- Do not report "eligible" if any required rule fails.

## 11. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for combining three eligibility conditions." |
| 2 — Plan | "Break Employee Eligibility Checker into input, condition and result steps." |
| 3 — Example | "Show a small if/elif/else example for an employee status." |
| 4 — Guided implementation | "Guide me to implement the active-status condition first." |
| 5 — Explanation | "Explain why Python uses indentation in if blocks." |
| 6 — Debugging | "My code always prints Eligible. Help me inspect condition order and input values." |
| 7 — Review | "Review my conditions and verify all project test cases." |

**Planning prompt:** "Help me translate the eligibility rules into Boolean conditions and test cases. Do not write the entire program."

**Implementation prompt:** "Guide me through one condition at a time and ask me to test both True and False cases."

**Debugging/review prompt:** "Review my code and explain any incorrect comparison, input normalization or indentation problem."

## 12. Daily quiz

**Q1. Which keyword begins a conditional block?**  
A. repeat  
B. if  
C. define  
D. class  
**Correct: B.** if begins a conditional statement.

**Q2. When is an else block executed?**  
A. Always  
B. When the preceding if/elif conditions did not match  
C. Only when the program starts  
D. When a variable is created  
**Correct: B.** Else handles the case where no preceding branch matched.

**Q3. What does AND require?**  
A. At least one condition true  
B. All conditions true  
C. Every condition false  
D. No conditions  
**Correct: B.** AND returns true only when all operands are true.

**Q4. Which expression checks whether email is empty?**  
A. `if email = ""`  
B. `if not email`  
C. `if email > ""`  
D. `if empty(email)`  
**Correct: B.** An empty string is falsy, so not email is true.

**Q5. Why does condition order matter in an if/elif chain?**  
A. Python evaluates only the first matching branch  
B. Python evaluates all branches and runs all  
C. It changes variable types  
D. It changes the file extension  
**Correct: A.** More general conditions placed too early can prevent later branches from running.

## 13. Interview preparation

### Q1. Explain if, elif and else.
**Answer:** if checks the first condition. elif checks another condition if earlier conditions were false. else runs when none of the previous conditions matched. Python executes only the first matching branch in the chain.

**Follow-up:** What can go wrong if a broad condition is placed before a more specific one?

### Q2. What is the difference between and and or?
**Answer:** and requires all conditions to be true. or requires at least one condition to be true. For an employee eligibility rule requiring active status and completed training, use and.

**Follow-up:** How would you express a rule that allows either admin or manager access?

## 14. Completion checklist
- [ ] Use if, else and elif.
- [ ] Combine conditions with and/or/not.
- [ ] Understand indentation and branch order.
- [ ] Test eligible and ineligible cases.
- [ ] Complete Employee Eligibility Checker.

**Next lesson:** Day 6 — Loops: for, while, break and continue.
