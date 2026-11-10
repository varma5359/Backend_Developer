# Day 9: Interview Questions — Functions, Parameters, Arguments and Return Values

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a function?
**Answer:**
- A reusable block of code that performs a task.
- Defined using def.
- Can accept input through parameters.
- Can return a result to the caller.
- Helps organize code and avoid repetition.

**Follow-up:** What is the difference between defining and calling a function?

### Q2. What is the difference between a parameter and an argument?
**Answer:**
- A parameter is named in the function definition.
- An argument is supplied at the function call.
- The argument value is assigned to the corresponding parameter.
- Positional and keyword arguments are common forms.

**Example:** In `def total(price)`, price is a parameter; in `total(500)`, 500 is an argument.

**Follow-up:** What happens when a required parameter is omitted?

### Q3. What is the difference between print and return?
**Answer:**
- print displays a value.
- return gives a value back to the caller.
- Returned values can be assigned to variables.
- return ends the current function execution.

**Follow-up:** What does a function return by default when no return statement is present?

### Q4. What are default arguments?
**Answer:**
- Parameters can be assigned default values in the definition.
- The default is used when the caller omits that argument.
- A caller can override it.
- Default values can make optional configuration convenient.

**Follow-up:** Why should mutable default values be handled carefully?

### Q5. What is local scope?
**Answer:**
- A local variable is defined inside a function.
- It is normally available only within that function.
- It helps keep implementation details separate.
- Values can be passed through parameters and returned.

**Follow-up:** Why is passing data through parameters usually preferable to using global variables?

## 2. Scenario-based questions

### Q6. A function prints the result, but another function cannot use it. Why?
**Answer:**
- The function may display the value instead of returning it.
- print is for output, not for passing a result to another function.
- Use return and assign the returned value.
- Test the function independently.

**Follow-up:** What would happen if the calling code assigns the result of a print-only function?

### Q7. A calculation is repeated in five places. How would you improve the code?
**Answer:**
- Identify the common calculation.
- Create a function with clear parameters.
- Return the result.
- Replace repeated logic with calls.
- Add tests for normal and boundary values.

**Follow-up:** How do functions improve maintainability?

## 3. Project questions

### Q8. Explain Reusable Calculation Toolkit.
**Answer:**
- I divided calculations into small functions.
- Each function accepts required parameters.
- Functions return values rather than only printing.
- I tested normal and boundary inputs.
- I created a summary function to present results.

**Follow-up:** How would you add exception handling to invalid calculations?

### Q9. What makes a good function?
**Answer:**
- A clear name.
- One understandable responsibility.
- Explicit inputs and outputs.
- Limited side effects.
- Useful validation and tests.
- Readable implementation.

**Follow-up:** When should a long function be split into smaller functions?

## 4. Rapid revision
- def: define a function.
- Call: execute a function.
- Parameter: variable in function definition.
- Argument: value passed to a call.
- return: sends a result to caller.
- Default argument: optional parameter value.
- Local scope: function-local variable.
- None: default return value without explicit return.
