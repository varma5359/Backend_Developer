# Day 7: Strings, String Methods and Formatting

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–6 — variables, input/output, conditions and loops  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Text Validation Utility

## 1. Learning objectives

- Explain what a string is and why strings are immutable.
- Access characters using indexing and slicing.
- Use common string methods.
- Normalize and inspect text values.
- Format readable messages using f-strings.
- Recognize the limits of simple text checks.

## 2. What is a string?

A string is a sequence of characters used to represent text.

```python
first_name = "Asha"
message = 'Welcome to Python'

print(first_name)
print(message)
```

Strings are commonly used for names, email addresses, phone numbers, messages, identifiers and data received from web requests.

## 3. String indexing

Each character has a position called an index. Positive indexing starts at zero. Negative indexing starts at the end.

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

An index outside the valid range raises `IndexError`. Check the string length or use a safe approach when the input length is unknown.

## 4. String slicing

Slicing extracts a portion of a string.

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

The start index is included and the stop index is excluded. Omitting the start or stop uses the beginning or end of the string.

A step can also be supplied:

```python
word = "PYTHON"
print(word[::2])
```

Output: `PTO`

## 5. Strings are immutable

Immutable means the original string cannot be changed character by character. String methods return a new string.

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

The original value remains `asha`. Store the returned string when you need the transformed value.

## 6. Useful string methods

| Method | Purpose | Example |
|---|---|---|
| `lower()` | Convert letters to lowercase | `"HELLO".lower()` |
| `upper()` | Convert letters to uppercase | `"hello".upper()` |
| `title()` | Capitalize word beginnings | `"asha rao".title()` |
| `strip()` | Remove surrounding whitespace | `" Asha ".strip()` |
| `replace(old, new)` | Replace matching text | `"a-b".replace("-", "_")` |
| `split(separator)` | Split text into a list | `"a,b".split(",")` |
| `startswith(text)` | Check a prefix | `"api/v1".startswith("api")` |
| `endswith(text)` | Check a suffix | `"notes.txt".endswith(".txt")` |
| `find(text)` | Find position or return -1 | `"python".find("th")` |
| `count(text)` | Count occurrences | `"banana".count("a")` |

### Normalize text

```python
email = "  ASHA@EXAMPLE.COM "
clean_email = email.strip().lower()

print(clean_email)
```

Output: `asha@example.com`

This is a basic normalization example. Whether an application should lowercase every part of an email address depends on its identity and comparison policy.

## 7. split() and join()

`split()` divides a string into a list. `join()` combines strings using a separator.

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

The separator used by `join()` appears between each item.

## 8. Search and membership checks

Use `in` to check whether text contains another string.

```python
email = "asha@example.com"

print("@" in email)
print(email.endswith(".com"))
print(email.find("example"))
```

Output:

```text
True
True
5
```

These are simple string checks, not complete email validation. Real applications need an appropriate validation policy and may need to verify that the user controls the address.

## 9. String formatting with f-strings

An f-string allows values to be inserted into text.

```python
name = "Asha"
department = "Engineering"

print(f"Employee {name} works in {department}.")
```

Output: `Employee Asha works in Engineering.`

Expressions can be included:

```python
basic_salary = 40000
allowance = 5000

print(f"Gross salary: {basic_salary + allowance}")
```

Output: `Gross salary: 45000`

## 10. Common mistakes

| Mistake | Explanation | Correction |
|---|---|---|
| Using an invalid index | Position is outside the string | Check length and valid positions |
| Expecting a method to modify original text | Strings are immutable | Assign the returned string |
| Forgetting that slice stop is excluded | Slicing uses a half-open range | Check start and stop indexes |
| Calling `join()` on the list | join is a string method | Use `separator.join(list_of_strings)` |
| Treating `find()` result -1 as a valid position | Text was not found | Check whether result is -1 |
| Assuming `"@" in email` is full validation | It checks only one character | Apply a proper validation policy |

## 11. Industry scenario

A backend receives a search term or email address containing accidental spaces and inconsistent casing. It may normalize the text before applying search or validation rules.

Normalization should be consistent with the application's data policy. Do not silently alter user data when the original form must be preserved.

## 12. Approved mini-project — Text Validation Utility

**Objective:** Build a small program that accepts text values and reports whether they meet simple rules.

### Requirements

1. Accept a person's name and email text.
2. Remove surrounding whitespace.
3. Display the name in a consistent format.
4. Check that the name is not empty.
5. Check that the email text contains an `@` character.
6. Check whether the email ends with a chosen domain suffix for practice.
7. Display each check separately and explain that these are beginner-level checks, not production-grade email validation.

### Suggested structure

```text
text_validation_utility/
└── validate_text.py
```

Test with leading spaces, uppercase letters, an empty name and an email missing the `@` character.

## 13. Key takeaways

- Strings store text and support indexing and slicing.
- String indexes start at zero; negative indexes count from the end.
- Strings are immutable; methods return new strings.
- `strip()`, `lower()`, `split()` and `join()` are useful text operations.
- `in`, `find()` and `endswith()` help inspect text.
- f-strings make output readable.
- Simple string checks are not a substitute for complete validation.

**Next lesson:** Day 8 — Lists, tuples, sets and dictionaries.
