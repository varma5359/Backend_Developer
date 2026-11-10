# Day 4: Interview Questions — Input/Output, String Formatting and User Interaction

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is input() in Python?
**Answer:**
- It reads text entered by the user.
- It returns a string.
- Convert it before numerical operations.
- It can display a prompt to the user.

**Follow-up:** What happens if the user enters "abc" and your code calls int()?

### Q2. What is print()?
**Answer:**
- It displays values to the output stream.
- It can print multiple values.
- sep controls the separator.
- end controls the ending character or string.

**Follow-up:** What is the default value of sep?

### Q3. What is an f-string?
**Answer:**
- A formatted string literal prefixed with f.
- It embeds variables or expressions inside curly braces.
- It makes output easier to read.
- It supports format specifications such as decimal precision.

**Example:** `f"Hello {name}"`.

**Follow-up:** How do you display a float to two decimal places?

### Q4. Why use strip() on user input?
**Answer:**
- It removes whitespace at the beginning and end.
- It helps prevent accidental spaces around values.
- It does not validate the meaning or format of the input.
- Additional validation may be required.

**Follow-up:** Does strip() remove spaces between words?

### Q5. Why store phone numbers as strings?
**Answer:**
- They may include a leading zero.
- They may include a country prefix such as +91.
- They are identifiers, not values used for arithmetic.
- String storage preserves their representation.

**Follow-up:** What data type would you use for a person's age?

## 2. Scenario-based questions

### Q6. A user enters age as 25, but your program cannot compare it with an integer. Why?
**Answer:**
- input() returns a string.
- The entered text must be converted to int.
- Invalid numeric text may cause ValueError.
- Robust applications validate and handle such errors.

**Follow-up:** What should the application display when the age is invalid?

### Q7. Your registration summary contains extra spaces around the email. How can you clean it?
**Answer:**
- Read the email using input().
- Apply strip() to remove leading/trailing whitespace.
- Store the cleaned result.
- Still perform actual email-format validation separately.

**Follow-up:** Why is strip() not a complete email validator?

## 3. Project questions

### Q8. Explain your User Registration Simulator.
**Answer:**
- I collected name, email, phone and age.
- I cleaned text inputs using strip().
- I converted age to an integer.
- I displayed a formatted registration summary using f-strings.
- I tested blank values and invalid age input.

**Follow-up:** What security checks would a real registration backend require?

### Q9. How do you make terminal output user-friendly?
**Answer:**
- Use clear prompts.
- Group related output.
- Add labels and readable spacing.
- Use f-strings for dynamic values.
- Avoid exposing sensitive information.

**Follow-up:** How might a web form present validation errors differently from a terminal program?

## 4. Rapid revision
- input(): reads a string.
- print(): displays output.
- strip(): trims surrounding whitespace.
- f-string: formatted string literal.
- sep: separator between print values.
- end: ending after print output.
- Type conversion: required for numeric input operations.
