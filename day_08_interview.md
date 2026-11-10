# Day 8: Interview Questions — Lists, Tuples, Sets and Dictionaries

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a list?
**Answer:**
- An ordered collection.
- Mutable, so items can be added, removed or changed.
- Allows duplicate values.
- Supports indexing and slicing.

**Follow-up:** How do you add an item to the end of a list?

### Q2. What is a tuple?
**Answer:**
- An ordered collection.
- Immutable after creation.
- Allows duplicates.
- Useful for fixed groupings of values.

**Follow-up:** Can a tuple contain a mutable object such as a list?

### Q3. What is a set?
**Answer:**
- A collection of unique elements.
- Duplicate values are removed.
- Does not support positional indexing.
- Supports union, intersection and difference.

**Follow-up:** How would you find common skills between two employees?

### Q4. What is a dictionary?
**Answer:**
- A key-value data structure.
- Keys must be unique and hashable.
- Values can be changed.
- It is useful for representing named fields.

**Follow-up:** What happens when you access a missing key with square brackets?

### Q5. Compare dictionary get() and square-bracket access.
**Answer:**
- dictionary[key] raises KeyError if the key is missing.
- get(key) returns None by default when the key is absent.
- get(key, default) returns a supplied fallback.
- Use direct indexing when the key is required.

**Follow-up:** How would you distinguish a missing key from a key whose value is None?

## 2. Scenario-based questions

### Q6. You need to store employees without duplicate email addresses. Which collection could help?
**Answer:**
- A set can track unique email strings.
- Check membership before accepting a new email.
- A real database should also enforce a uniqueness constraint.
- Application-level checks alone may not prevent concurrent duplicates.

**Follow-up:** Why is a database uniqueness constraint important?

### Q7. Your code raises KeyError while showing a student course. What do you check?
**Answer:**
- Confirm the dictionary contains the expected key.
- Check spelling and case of the key.
- Verify the record structure is consistent.
- Use get() for genuinely optional values.

**Follow-up:** Why should you not silently replace every missing required field with a default?

## 3. Project questions

### Q8. Explain Student Record Manager.
**Answer:**
- I stored multiple student dictionaries inside a list.
- I displayed records using a loop.
- I searched for a student ID.
- I updated a course value.
- I used a set to identify unique courses.

**Follow-up:** How would you store these records persistently?

### Q9. Why use a list of dictionaries?
**Answer:**
- Each dictionary represents one record with named attributes.
- The list holds multiple records in order.
- It is simple for small in-memory demonstrations.
- For production data, a database provides persistence and integrity.

**Follow-up:** When would you choose a database model instead?

## 4. Rapid revision
- List: ordered, mutable, duplicates allowed.
- Tuple: ordered, immutable.
- Set: unique elements.
- Dictionary: key-value pairs.
- append(): add list item.
- add(): add set item.
- get(): safe dictionary lookup with default.
- KeyError: missing dictionary key accessed directly.
