# Day 7: Interview Questions — Strings, String Methods and Formatting

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a string in Python?
**Answer:**
- A sequence of characters.
- Can be created using single, double or triple quotes.
- Supports indexing and slicing.
- Is immutable.

**Follow-up:** What is the difference between a string and a list of characters?

### Q2. What is string indexing?
**Answer:**
- Accessing a character using its position.
- Positive indexing starts at zero.
- Negative indexing starts from the end.
- An invalid index raises IndexError.

**Follow-up:** What does text[-1] return?

### Q3. What is slicing?
**Answer:**
- Extracting a portion of a sequence.
- Uses start, stop and optional step.
- The stop index is excluded.
- It returns a new string.

**Follow-up:** What does text[1:4] select?

### Q4. Explain strip(), lower() and upper().
**Answer:**
- strip() removes whitespace from the beginning and end.
- lower() returns lowercase text.
- upper() returns uppercase text.
- Each returns a new string.

**Follow-up:** Do these methods modify the original string?

### Q5. Compare split() and join().
**Answer:**
- split() converts a string into a list of parts.
- join() combines strings from an iterable.
- The separator is used by split or supplied as the string on which join is called.
- join expects string elements.

**Follow-up:** How would you turn "Python,Django" into "Python | Django"?

## 2. Scenario-based questions

### Q6. An email arrives with leading spaces and uppercase characters. What do you do?
**Answer:**
- Strip surrounding whitespace.
- Normalize case where appropriate.
- Apply the application's actual validation policy.
- Verify address ownership when the use case requires it.
- Avoid claiming that string cleanup proves the mailbox exists.

**Follow-up:** Why is checking only for @ insufficient?

### Q7. Your code calls text[10] and raises IndexError. What is the reason?
**Answer:**
- The string may have fewer than eleven characters.
- Python indexes begin at zero.
- Check the string length or validate before accessing an index.
- Use safe slicing if an optional portion is needed.

**Follow-up:** What happens when a slice goes beyond the string's length?

## 3. Project questions

### Q8. Explain Text Validation Utility.
**Answer:**
- I collected a name and email.
- I removed surrounding whitespace.
- I normalized email case.
- I checked blank fields and a simple @ condition.
- I documented that this is only a learning-level check.

**Follow-up:** What additional checks would a real registration service need?

### Q9. Why are strings immutable?
**Answer:**
- The contents cannot be changed in place.
- Operations return new strings.
- Immutability makes string values safer to share and reason about.
- Reassignment can bind a variable to the new string.

**Follow-up:** What is the difference between name.upper() and name = name.upper()?

## 4. Rapid revision
- String: sequence of characters.
- Index: position of a character.
- Slice: portion of a sequence.
- strip(): remove surrounding whitespace.
- split(): string to list.
- join(): iterable of strings to string.
- Immutable: cannot be changed in place.
