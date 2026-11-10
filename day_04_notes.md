# Day 4: Input/Output, String Formatting and User Interaction

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–3; variables, data types and conversion  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** User Registration Simulator

## 1. Learning objectives
- Collect user input using input().
- Convert input to the required data type.
- Display readable output using print().
- Format strings using f-strings.
- Build a simple registration interaction and validate basic required values.

## 2. Input and output
- `input()` reads text entered by the user.
- `print()` displays output in the terminal.
- Input is returned as a string, even when the user types digits.

```python
name = input("Enter your name: ")
print("Welcome", name)
```

Example terminal interaction:
```text
Enter your name: Asha
Welcome Asha
```

## 3. Convert user input
```python
age_text = input("Enter your age: ")
age = int(age_text)

print("Next year you will be", age + 1)
```

Example:
```text
Enter your age: 24
Next year you will be 25
```

If a user enters text such as "twenty", int() raises ValueError. You will study structured exception handling on Day 12.

## 4. print() parameters
```python
print("Python", "Django", "Backend")
print("Python", "Django", sep=" | ")
print("Loading", end="...")
print("Done")
```

Expected output:
```text
Python Django Backend
Python | Django
Loading...Done
```

- `sep` controls the text placed between values.
- `end` controls what is printed after the values.
- By default, sep is a space and end is a newline.

## 5. String formatting with f-strings
F-strings let you place variable values inside a string.

```python
name = "Asha"
role = "Backend Developer"
print(f"{name} is learning {role}")
```

Output:
```text
Asha is learning Backend Developer
```

Formatting decimal values:
```python
fee = 1250.567
print(f"Fee: {fee:.2f}")
```

Output:
```text
Fee: 1250.57
```

The `:.2f` format displays a floating-point value with two digits after the decimal point.

## 6. Multi-line output
```python
name = "Asha"
email = "asha@example.com"

print("REGISTRATION SUMMARY")
print(f"Name  : {name}")
print(f"Email : {email}")
```

Expected output:
```text
REGISTRATION SUMMARY
Name  : Asha
Email : asha@example.com
```

## 7. Basic input validation
At this stage, validate simple requirements using conditions from the next lesson conceptually; detailed conditional statements are introduced on Day 5.

```python
name = input("Enter name: ").strip()
email = input("Enter email: ").strip()

print("Name entered:", name)
print("Email entered:", email)
```

The `strip()` method removes leading and trailing whitespace. It does not prove that an email address is valid. Real applications need proper validation and server-side checks.

## 8. Industry scenario
A user registration page collects name, email and phone number. The backend receives the values as data, checks their validity and returns a response. The frontend should show clear errors, while backend validation remains authoritative because clients can be modified or bypassed.

## 9. Approved mini-project — User Registration Simulator

**Objective:** Create a terminal-based interaction that collects and displays basic registration details.

### Requirements
1. Ask for full name.
2. Ask for email.
3. Ask for phone number as text (preserve leading zeros and plus sign).
4. Ask for age and convert it to an integer.
5. Remove accidental leading/trailing spaces from text inputs.
6. Display a formatted registration summary.
7. Do not store real passwords or sensitive information in this beginner simulation.

**Suggested structure**
```text
user_registration_simulator/
└── registration.py
```

Example interaction:
```text
Full name: Asha Rao
Email: asha@example.com
Phone: +91 9876543210
Age: 24

REGISTRATION SUMMARY
Name: Asha Rao
Email: asha@example.com
Phone: +91 9876543210
Age: 24
```

### Validation
- Ensure name and email are not blank.
- Keep phone number as string.
- Ensure age is converted to an integer.
- Test blank values and non-numeric age; note that robust error handling is a later lesson.

## 10. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for collecting phone numbers without losing the leading zero." |
| 2 — Plan | "Break User Registration Simulator into input, cleanup and summary steps." |
| 3 — Example | "Show a small f-string summary with a name and email." |
| 4 — Guided implementation | "Guide me to collect one field at a time and explain the data type." |
| 5 — Explanation | "Explain input(), strip(), print() and f-string placeholders." |
| 6 — Debugging | "Help me diagnose why my age conversion fails for a non-numeric input." |
| 7 — Review | "Review my registration simulator for input handling and readable output." |

**Planning prompt:** "Help me design the registration questions and output format, but don't write the full script."

**Implementation prompt:** "Guide me through input collection one field at a time, then ask me to test the result."

**Debugging/review prompt:** "Inspect my code and explain any incorrect input conversions or formatting problems."

## 11. Daily quiz

**Q1. What type of value does input() return?**  
A. int  
B. str  
C. bool  
D. float  
**Correct: B.** input() returns text.

**Q2. Which method removes leading and trailing whitespace?**  
A. upper()  
B. strip()  
C. splitlines()  
D. replaceall()  
**Correct: B.** strip() removes whitespace at the beginning and end.

**Q3. Which is an f-string?**  
A. `print("Hello {name}")`  
B. `print(f"Hello {name}")`  
C. `print(input name)`  
D. `print(str: name)`  
**Correct: B.** The f prefix enables expression placeholders.

**Q4. Why should a phone number generally be stored as text?**  
A. It is always used in arithmetic  
B. It may contain a leading zero or plus sign  
C. It is a Boolean  
D. It is a Python keyword  
**Correct: B.** Phone numbers are identifiers/contact values, not quantities for arithmetic.

**Q5. What does `print("A", "B", sep="-")` display?**  
A. A B  
B. A-B  
C. AB-  
D. -AB  
**Correct: B.** sep inserts the hyphen between the arguments.

## 12. Interview preparation

### Q1. What is the difference between input() and print()?
**Answer:** input() reads user input and returns it as a string. print() displays values to the output stream, usually the terminal. Convert input when a numeric calculation is required.

**Follow-up:** Why does input("Age: ") need int() before numeric comparison?

### Q2. What is an f-string?
**Answer:** An f-string is a formatted string literal prefixed with f. It lets a developer place variables or expressions inside curly braces, improving readability when building messages and summaries.

**Follow-up:** How would you display a decimal value with two digits after the point?

## 13. Completion checklist
- [ ] Collect values using input().
- [ ] Convert age to int.
- [ ] Keep phone as text.
- [ ] Use strip() for text cleanup.
- [ ] Format output using f-strings.
- [ ] Complete User Registration Simulator.

**Next lesson:** Day 5 — Conditional statements and decision-making.
