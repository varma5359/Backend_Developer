# Day 7: Strings, String Methods and Formatting

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–6 — variables, conditions, loops and basic collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Text Validation Utility

> **Beginner note:** Backend applications receive lots of text: names, email addresses, phone numbers, search terms and messages. Today you will learn how Python stores and works with text.

## 1. Learning objectives

By the end of this lesson, you should be able to:
- Create strings and understand quotation marks.
- Access characters using indexing.
- Extract parts of text using slicing.
- Explain why strings are immutable.
- Use common string methods individually.
- Format text using f-strings.
- Perform basic text checks without confusing them with complete validation.

## 2. What is a string?

A **string** is a sequence of characters. Characters can include letters, digits, spaces and symbols.

```python
first_name = "Asha"
city = "Hyderabad"
message = "Welcome to Python!"

print(first_name)
print(city)
print(message)
```

Output:
```text
Asha
Hyderabad
Welcome to Python!
```

Text must be enclosed in quotation marks. Single quotes and double quotes are both valid.

```python
name = 'Ravi'
course = "Python Backend"
```

Use consistent quotation style in a project. If the text contains an apostrophe, choose quotes that make the string easy to write.

## 3. String indexing — access one character

Each character in a string has a position called an **index**. Python starts positive indexes at zero.

```python
word = "PYTHON"

print(word[0])
print(word[1])
print(word[2])
```

Output:
```text
P
Y
T
```

Why does `word[0]` give P? Because the first position is zero.

Index positions:

| Character | P | Y | T | H | O | N |
|---|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

Negative indexes start from the end:

```python
word = "PYTHON"
print(word[-1])
print(word[-2])
```

Output:
```text
N
O
```

If you request an index that does not exist, Python raises `IndexError`. For example, `word[10]` is invalid because the string has only six characters.

## 4. String slicing — extract a part of text

Slicing takes a section of a string.

Syntax:
```python
text[start:stop]
```

The start position is included; the stop position is excluded.

```python
word = "BACKEND"

print(word[0:4])
print(word[4:7])
print(word[:4])
print(word[4:])
```

Output:
```text
BACK
END
BACK
END
```

Explanation:
- `word[0:4]` takes indexes 0, 1, 2 and 3.
- `word[4:7]` takes indexes 4, 5 and 6.
- `word[:4]` starts from the beginning.
- `word[4:]` continues from index 4 to the end.

A step can also be supplied:

```python
word = "PYTHON"
print(word[::2])
```

Output: `PTO`

The step 2 means take every second character.

## 5. Strings are immutable

**Immutable** means that the original string cannot be changed character by character after it is created.

This example creates a new string:

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

The original variable still refers to `"asha"`. The method `upper()` returned a new string, which we stored in `updated_name`.

This is why the following assignment is invalid:

```python
# name[0] = "A"  # TypeError: strings do not support item assignment
```

Instead, use a string method or create a new string.

## 6. String methods — learn each one with an example

A **method** is an operation associated with an object. String methods are called using dot notation:

```python
text.method_name()
```

For example, `name.upper()` calls the upper method on the string stored in name.

### 6.1 upper() — convert letters to uppercase

```python
name = "asha rao"
result = name.upper()

print(result)
```

Output: `ASHA RAO`

It returns a new string with lowercase letters converted to uppercase. It does not change the original string.

### 6.2 lower() — convert letters to lowercase

```python
email = "ASHA@EXAMPLE.COM"
result = email.lower()

print(result)
```

Output: `asha@example.com`

This is useful when an application needs consistent text for comparisons. Follow the application's data policy before normalizing user data.

### 6.3 title() — capitalize the beginning of words

```python
name = "asha rao"
print(name.title())
```

Output: `Asha Rao`

This is useful for display formatting, but it is not a perfect name-correction tool. Names can contain unusual capitalization.

### 6.4 capitalize() — uppercase the first character

```python
message = "welcome to python"
print(message.capitalize())
```

Output: `Welcome to python`

It capitalizes the first character and lowercases the remaining letters.

### 6.5 strip() — remove surrounding whitespace

```python
name = "   Asha   "
clean_name = name.strip()

print(clean_name)
```

Output: `Asha`

Whitespace includes spaces, tabs and newline characters at the beginning and end. `strip()` does not remove spaces in the middle of the text.

### 6.6 lstrip() and rstrip()

`lstrip()` removes whitespace from the left side. `rstrip()` removes it from the right side.

```python
text = "   Python   "

print(text.lstrip())
print(text.rstrip())
```

Output:
```text
Python   
   Python
```

These methods are useful when you need to clean only one side of a string.

### 6.7 replace() — replace matching text

Syntax: `text.replace(old, new)`

```python
message = "I learn Java"
updated_message = message.replace("Java", "Python")

print(updated_message)
```

Output: `I learn Python`

The method returns a new string in which matching occurrences are replaced.

You can limit the number of replacements with the optional count argument:

```python
text = "cat cat cat"
print(text.replace("cat", "dog", 1))
```

Output: `dog cat cat`

### 6.8 split() — divide a string into a list

Syntax: `text.split(separator)`

```python
skills_text = "Python,Django,SQL"
skills = skills_text.split(",")

print(skills)
```

Output:
```text
['Python', 'Django', 'SQL']
```

Explanation:
- The comma is the separator.
- Python finds each comma.
- It divides the text at those positions.
- It returns a list containing the pieces.

If you call `split()` without a separator, Python splits on whitespace.

### 6.9 join() — combine strings from an iterable

`join()` is called on the separator string.

```python
skills = ["Python", "Django", "SQL"]
result = " | ".join(skills)

print(result)
```

Output: `Python | Django | SQL`

Read it as: join the list items, placing `" | "` between them.

Important: the items must be strings. If your list contains integers, convert them to strings before joining.

### 6.10 startswith() — check the beginning

```python
path = "api/v1/students"
print(path.startswith("api"))
```

Output: `True`

It returns True if the string begins with the supplied prefix; otherwise False.

### 6.11 endswith() — check the ending

```python
filename = "students.csv"
print(filename.endswith(".csv"))
```

Output: `True`

This can help identify a file extension, but a filename ending alone does not prove that the file's content is valid CSV.

### 6.12 find() — find the position of text

```python
message = "Learn Python"
print(message.find("Python"))
print(message.find("Java"))
```

Output:
```text
6
-1
```

The first result is the starting index of the matching text. If it is not found, `find()` returns -1.

Do not treat -1 as a valid character position. Check the result before using it.

### 6.13 count() — count occurrences

```python
message = "banana"
print(message.count("a"))
print(message.count("na"))
```

Output:
```text
3
2
```

The method counts non-overlapping occurrences of the supplied substring.

### 6.14 isalpha() — check whether all characters are letters

```python
name = "Asha"
print(name.isalpha())
```

Output: `True`

A string containing a space or digit will return False. This is a basic character check, not a complete real-world name validation rule.

### 6.15 isdigit() — check whether all characters are digits

```python
code = "12345"
print(code.isdigit())
```

Output: `True`

It can help check simple numeric text, such as a one-time code. It does not convert the string into an integer.

### 6.16 isalnum() — letters or digits only

```python
username = "asha123"
print(username.isalnum())
```

Output: `True`

If the string contains a space or punctuation mark, the result is False.

## 7. Membership operator: in

The `in` operator checks whether one piece of text exists inside another.

```python
email = "asha@example.com"

print("@" in email)
print("gmail" in email)
```

Output:
```text
True
False
```

This is a simple presence check. It is not a full email validation method.

## 8. String formatting with f-strings

```python
name = "Asha"
course = "Python"

message = f"{name} is learning {course}"
print(message)
```

Output: `Asha is learning Python`

The f before the quotation mark tells Python to evaluate expressions inside curly braces.

## 9. Industry example: normalize a search value

Suppose a user searches for a course and accidentally enters spaces and different letter casing.

```python
search_text = "   PYTHON Backend   "

clean_search = search_text.strip().lower()

print(clean_search)
```

Output: `python backend`

Explanation:
1. `strip()` removes spaces at the beginning and end.
2. `lower()` converts letters to lowercase.
3. The cleaned value can be used in a consistent comparison.

Whether a real application should normalize a particular field depends on its requirements.

## 10. Common mistakes

| Mistake | Explanation | Correction |
|---|---|---|
| Accessing an invalid index | Position does not exist | Check length or use safe logic |
| Expecting methods to change the original | Strings are immutable | Store the returned string |
| Forgetting slice stop is excluded | Slicing uses start-inclusive, stop-exclusive positions | Check index boundaries |
| Calling join() on the list | join is a string method | Use separator.join(list) |
| Treating find() result -1 as a match | Text was not found | Check the result |
| Treating '@' check as email validation | Only one character was checked | Use a proper validation process |

## 11. Interview preparation

**Q1. What is a string in Python?**

Answer: A string is an immutable sequence of Unicode characters used to represent text.

Follow-up: Can we change one character in a string by index?  
Answer: No. Strings are immutable. We create a new string instead.

**Q2. Difference between split() and join()?**

Answer: split() divides a string into a list. join() combines strings from an iterable using the string on which join is called as the separator.

**Q3. Difference between find() and count()?**

Answer: find() returns the starting position of a matching substring or -1 if it is not found. count() returns the number of non-overlapping occurrences.

**Q4. What does strip() do?**

Answer: strip() returns a new string with leading and trailing whitespace removed.

## 12. Approved mini-project — Text Validation Utility

**Objective:** Accept basic text values and report whether they meet simple practice rules.

### Requirements
1. Accept a person's name and email text.
2. Remove surrounding whitespace using strip().
3. Display the name in a consistent format.
4. Check that the name is not empty.
5. Check whether the email contains an @ character.
6. Check whether it ends with a chosen suffix for practice.
7. Display each check separately.
8. Explain in the output or README that these checks are not production-grade email validation.

### Test inputs
- Name with leading and trailing spaces.
- Empty name.
- Uppercase email.
- Email without @.
- Email with a different ending.

## 13. Daily practice and completion check

1. Print the first and last character of a word.
2. Extract the first four characters using slicing.
3. Convert a sentence to lowercase.
4. Remove spaces around a name.
5. Split a comma-separated list of skills.
6. Join a list using a pipe separator.
7. Explain the difference between find() and count().

You have completed Day 7 when you can choose a string method, explain its purpose and predict the output before running the code.

**Next lesson:** Day 8 — Lists, tuples, sets and dictionaries.
