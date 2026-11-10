# Day 7: Strings, String Methods and Formatting

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–6; variables, input/output, conditions and loops  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Text Validation Utility

## 1. Learning objectives
- Explain how Python represents strings.
- Use indexing and slicing to access text.
- Apply common string methods.
- Validate and normalize simple text inputs.
- Format readable messages using f-strings.

## 2. What is a string?
A string is a sequence of characters, usually written in single or double quotes.

```python
first_name = "Asha"
message = 'Welcome to Python'
print(first_name)
print(message)
```

Strings are immutable: string methods return new strings rather than changing the original string in place.

## 3. Indexing
Each character has an index. Positive indexes start at zero; negative indexes count from the end.

```python
word = "PYTHON"
print(word[0])
print(word[1])
print(word[-1])
```

Output:
```text
P
Y
N
```

An index outside the available range raises IndexError.

## 4. Slicing
Slicing extracts part of a string.

```python
word = "BACKEND"
print(word[0:4])
print(word[4:])
print(word[:3])
```

Output:
```text
BACK
END
BAC
```

The ending index is excluded.

## 5. Useful string methods

| Method | Purpose | Example |
|---|---|---|
| lower() | Convert to lowercase | "HELLO".lower() |
| upper() | Convert to uppercase | "hello".upper() |
| title() | Title-case words | "asha rao".title() |
| strip() | Remove surrounding whitespace | " Asha ".strip() |
| replace() | Replace substring | "a-b".replace("-", "_") |
| split() | Split into a list | "a,b".split(",") |
| startswith() | Check prefix | "api".startswith("a") |
| endswith() | Check suffix | "file.txt".endswith(".txt") |
| find() | Find substring index or -1 | "python".find("th") |
| count() | Count occurrences | "banana".count("a") |

Examples:
```python
email = "  ASHA@EXAMPLE.COM "
clean_email = email.strip().lower()
print(clean_email)
```

Output:
```text
asha@example.com
```

## 6. split() and join()
```python
skills_text = "Python,Django,PostgreSQL"
skills = skills_text.split(",")
print(skills)

joined = " | ".join(skills)
print(joined)
```

Output:
```text
['Python', 'Django', 'PostgreSQL']
Python | Django | PostgreSQL
```

## 7. String membership
Use `in` to check whether a substring appears.

```python
email = "asha@example.com"
print("@" in email)
print(email.endswith(".com"))
```

These are simple checks for learning, not complete email validation. Real validation needs a suitable format policy and may also require confirmation that the address is controlled by the user.

## 8. Strings are immutable
```python
name = "asha"
updated_name = name.upper()

print(name)
print(updated_name)
```

Output:
```text
asha
ASHA
```

The original string remains unchanged. Assign the returned string to a variable when you need the modified value.

## 9. Industry scenario
An API receives a customer's email address with accidental spaces and inconsistent letter casing. The backend normalizes the value before applying the application's validation rules. Normalization should not replace proper validation or ownership verification.

## 10. Approved mini-project — Text Validation Utility

**Objective:** Build a small utility that cleans and checks common text fields.

### Requirements
1. Collect a person's full name.
2. Collect an email string.
3. Strip leading/trailing whitespace.
4. Normalize the email to lowercase.
5. Check that name and email are not blank.
6. Perform a basic presence check for "@" as a learning exercise.
7. Display a normalized summary and validation result.
8. Clearly state that this is not production-grade email validation.

**Suggested structure**
```text
text_validation_utility/
└── validate_text.py
```

### Sample tests
| Input name | Input email | Expected |
|---|---|---|
| " Asha Rao " | " ASHA@EXAMPLE.COM " | Non-blank, simple @ check passes |
| "   " | "asha@example.com" | Name invalid |
| "Ravi" | "ravi.example.com" | Email simple check fails |

### Validation
- Test uppercase and lowercase values.
- Test empty strings and whitespace-only strings.
- Confirm the output shows normalized values.
- Do not claim a simple @ check verifies a real mailbox.

## 11. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint to normalize an email string." |
| 2 — Plan | "Break Text Validation Utility into cleanup, checks and display." |
| 3 — Example | "Show a short strip and lower example." |
| 4 — Guided implementation | "Guide me to create the name validation first, then wait." |
| 5 — Explanation | "Explain indexing, slicing and string immutability." |
| 6 — Debugging | "Help me understand why my string index causes IndexError." |
| 7 — Review | "Review my utility and identify edge cases that my basic checks miss." |

**Planning prompt:** "Help me list text fields, normalization steps, simple checks and test cases. Do not provide the completed script."

**Implementation prompt:** "Guide me through one string method at a time using the sample inputs."

**Debugging/review prompt:** "Inspect my validation code and identify incorrect method usage or claims that are stronger than the checks support."

## 12. Daily quiz

**Q1. What is the first index of a Python string?**  
A. 1  
B. 0  
C. -1  
D. 2  
**Correct: B.** String indexing begins at zero.

**Q2. What does `" Asha ".strip()` return?**  
A. " Asha "  
B. "Asha"  
C. "asha"  
D. "ASHA"  
**Correct: B.** strip removes whitespace from both ends.

**Q3. What does split(",") return?**  
A. Always an integer  
B. A list of parts  
C. A Boolean  
D. A dictionary  
**Correct: B.** split divides a string into a list using the separator.

**Q4. What does `"python".upper()` return?**  
A. python  
B. Python  
C. PYTHON  
D. None  
**Correct: C.** upper returns a new uppercase string.

**Q5. What is true about Python strings?**  
A. They are mutable in place  
B. They are immutable  
C. They contain only digits  
D. They cannot be sliced  
**Correct: B.** String operations return new values rather than modifying the original string.

## 13. Interview preparation

### Q1. Are Python strings mutable or immutable?
**Answer:** Python strings are immutable. A string method such as upper() returns a new string. The original value remains unchanged unless a variable is reassigned to the returned value.

**Follow-up:** What happens when you call replace() on a string and do not store the result?

### Q2. Explain the difference between split() and join().
**Answer:** split() breaks a string into a list of parts using a separator. join() combines an iterable of strings into one string using the calling string as a separator.

**Follow-up:** What error can occur if the list passed to join() contains a non-string value?

## 14. Completion checklist
- [ ] Use positive and negative indexing.
- [ ] Extract text using slicing.
- [ ] Apply string methods.
- [ ] Explain immutability.
- [ ] Complete Text Validation Utility.
- [ ] Test blank and normalized inputs.

**Next lesson:** Day 8 — Lists, tuples, sets and dictionaries.
