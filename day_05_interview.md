# Day 5: Interview Questions — Conditional Statements and Decision-Making

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a conditional statement?
**Answer:**
- It controls program flow based on a condition.
- The condition evaluates to True or False.
- Python executes the matching branch.
- Common keywords are if, elif and else.

**Follow-up:** Why is indentation important in Python?

### Q2. Explain if, elif and else.
**Answer:**
- if checks the first condition.
- elif checks another condition when earlier conditions are false.
- else handles the remaining case.
- Only the first matching branch runs.

**Follow-up:** What happens when none of the conditions match and no else exists?

### Q3. Compare and and or.
**Answer:**
- and requires every condition to be true.
- or requires at least one condition to be true.
- Both are used to combine Boolean expressions.
- Choose based on the actual business rule.

**Follow-up:** Which operator checks either admin or manager role?

### Q4. What is a nested if?
**Answer:**
- A conditional statement inside another conditional block.
- It is useful when one decision depends on an earlier decision.
- Excessive nesting can reduce readability.
- Conditions should be organized clearly.

**Follow-up:** How could you simplify deeply nested conditions?

### Q5. What are truthy and falsy values?
**Answer:**
- Python evaluates values in Boolean contexts.
- Empty strings, empty lists, zero, None and False are falsy.
- Many non-empty values are truthy.
- This can be used for simple presence checks.

**Follow-up:** Does a non-empty email string guarantee a valid email address?

## 2. Scenario-based questions

### Q6. Your program prints a high grade for every score. What would you inspect?
**Answer:**
- Condition order.
- Comparison operators.
- Whether a broad condition is placed too early.
- Input conversion and actual stored value.
- Boundary test cases.

**Follow-up:** How would you test the grade boundaries?

### Q7. A user can access a manager page because the frontend hides the link for other users. Is that sufficient?
**Answer:**
- No.
- Frontend visibility is not a security boundary.
- The backend must validate authentication and authorization for the requested resource.
- A client can send requests without using the visible page.

**Follow-up:** Which is the difference between authentication and authorization?

## 3. Project questions

### Q8. Explain Employee Eligibility Checker.
**Answer:**
- I collected status, experience and training completion.
- I normalized text inputs.
- I converted experience to a number.
- I combined requirements into conditions.
- I tested cases where each individual requirement failed.

**Follow-up:** How would you make the rule easier to change when HR updates the policy?

### Q9. How do you test conditional logic?
**Answer:**
- Test a case where all conditions are true.
- Test each condition failing individually.
- Test boundary values.
- Test invalid input separately.
- Compare actual results with expected results.

**Follow-up:** What is boundary-value testing?

## 4. Rapid revision
- if: first condition.
- elif: alternative condition.
- else: fallback branch.
- and: all conditions true.
- or: at least one condition true.
- not: Boolean negation.
- Indentation: defines Python code blocks.
- Truthy/falsy: values interpreted in Boolean context.
