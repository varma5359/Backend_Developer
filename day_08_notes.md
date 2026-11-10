# Day 8: Lists, Tuples, Sets and Dictionaries

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–7; variables, conditions, loops and strings  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Student Record Manager

## 1. Learning objectives
- Explain the differences between list, tuple, set and dictionary.
- Create, access and update collection values.
- Iterate through collection elements.
- Choose a suitable collection for a simple data requirement.
- Manage a small set of student records in memory.

## 2. Why collections?
Backend applications work with groups of related values:
- A list of employees.
- A set of unique permissions.
- A tuple of fixed coordinates.
- A dictionary containing one student's fields.

Choosing an appropriate collection makes data easier to organize and process.

## 3. List
A list is ordered and mutable. It allows duplicate values.

```python
students = ["Asha", "Ravi", "John"]
print(students[0])

students.append("Meera")
students[1] = "Rahul"
print(students)
```

Output:
```text
Asha
['Asha', 'Rahul', 'John', 'Meera']
```

Common methods:
- append(value): add one item at the end.
- insert(index, value): insert at a position.
- remove(value): remove first matching value.
- pop(): remove and return an item.
- sort(): sort the list in place.

## 4. Tuple
A tuple is ordered and immutable. It can contain duplicate values.

```python
coordinates = (17.4, 78.5)
print(coordinates[0])
```

Tuples are suitable for small fixed groupings of values that should not be modified.

## 5. Set
A set stores unique elements and does not provide positional indexing.

```python
skills = {"Python", "Django", "Python"}
skills.add("PostgreSQL")
print(skills)
```

Output order is not guaranteed. The duplicate "Python" appears only once.

Useful operations:
```python
a = {"Python", "Django"}
b = {"Django", "SQL"}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
```

## 6. Dictionary
A dictionary stores key-value pairs.

```python
student = {
    "student_id": 101,
    "name": "Asha",
    "course": "Python"
}

print(student["name"])
student["course"] = "Django"
student["email"] = "asha@example.com"
print(student)
```

Use `get()` for safe lookup when a key may not exist:
```python
print(student.get("phone", "Not provided"))
```

Common operations:
- keys(): view keys.
- values(): view values.
- items(): key-value pairs.
- update(): add or update entries.
- pop(key): remove a key.

## 7. Compare the collections

| Collection | Ordered? | Mutable? | Duplicates? | Example use |
|---|---|---|---|---|
| list | Yes | Yes | Yes | Employee records |
| tuple | Yes | No | Yes | Fixed coordinate pair |
| set | No positional order | Yes | No | Unique skills |
| dictionary | Insertion order preserved | Yes | Keys unique | Student fields |

## 8. Loop through collections
List:
```python
students = ["Asha", "Ravi"]
for name in students:
    print(name)
```

Dictionary:
```python
student = {"name": "Asha", "course": "Python"}
for key, value in student.items():
    print(key, value)
```

## 9. Nested collections
A list of dictionaries is a common in-memory representation of records.

```python
students = [
    {"id": 101, "name": "Asha", "course": "Python"},
    {"id": 102, "name": "Ravi", "course": "Django"}
]

for student in students:
    print(student["id"], student["name"])
```

This is a useful stepping stone toward working with JSON and database query results.

## 10. Industry scenario
A training portal may load a small set of student records into application memory. A list stores the records, and each dictionary stores fields for one student. A set can track unique course names. Real production records should be stored in a database, not only in a program variable.

## 11. Approved mini-project — Student Record Manager

**Objective:** Manage a small in-memory collection of student records.

### Requirements
1. Create a list to store multiple student dictionaries.
2. Each student should have ID, name and course.
3. Add at least three student records.
4. Display all students using a loop.
5. Search for a student by ID.
6. Update a student's course.
7. Create a set of unique course names.
8. Display a summary of student count and available courses.

**Suggested structure**
```text
student_record_manager/
└── student_manager.py
```

### Sample records
```python
students = [
    {"id": 101, "name": "Asha", "course": "Python"},
    {"id": 102, "name": "Ravi", "course": "Django"},
    {"id": 103, "name": "Meera", "course": "Python"}
]
```

Expected student count: 3. Unique courses: Python and Django.

### Validation
- Ensure IDs are unique.
- Search for an existing and a missing ID.
- Update only the matching student.
- Confirm the unique course set contains no duplicates.

## 12. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for searching a list of student dictionaries by ID." |
| 2 — Plan | "Break Student Record Manager into create, display, search, update and summary tasks." |
| 3 — Example | "Show a tiny example of iterating through a list of dictionaries." |
| 4 — Guided implementation | "Guide me through the search function logic without writing the whole project." |
| 5 — Explanation | "Explain the difference between list, tuple, set and dictionary using student data." |
| 6 — Debugging | "Help me resolve this KeyError when accessing a student's course." |
| 7 — Review | "Review my student records for duplicate IDs and update correctness." |

**Planning prompt:** "Help me define the data structure and operations for Student Record Manager. Do not provide the completed solution."

**Implementation prompt:** "Help me implement the display operation first, then ask me to test it."

**Debugging/review prompt:** "Inspect my list/dictionary operations and identify unsafe key access or incorrect update logic."

## 13. Daily quiz

**Q1. Which collection is ordered and mutable?**  
A. Tuple  
B. List  
C. Set  
D. None  
**Correct: B.** Lists preserve sequence order and can be modified.

**Q2. Which collection stores unique values?**  
A. Set  
B. List  
C. Tuple  
D. String  
**Correct: A.** A set does not keep duplicate elements.

**Q3. Which collection stores key-value pairs?**  
A. List  
B. Tuple  
C. Dictionary  
D. Set  
**Correct: C.** Dictionaries associate keys with values.

**Q4. What does dictionary.get("phone", "NA") do if phone is missing?**  
A. Raises KeyError always  
B. Returns "NA"  
C. Deletes the dictionary  
D. Creates a list  
**Correct: B.** get() returns the supplied default when the key is absent.

**Q5. Which structure is suitable for multiple student records where each record has named fields?**  
A. List of dictionaries  
B. One integer  
C. One Boolean  
D. One string  
**Correct: A.** Each dictionary stores a record and the list stores multiple records.

## 14. Interview preparation

### Q1. Compare list, tuple, set and dictionary.
**Answer:** A list is ordered and mutable; a tuple is ordered and immutable; a set stores unique elements; a dictionary stores key-value pairs with unique keys. Select the collection according to ordering, mutability and lookup needs.

**Follow-up:** Which collection would you use to store unique permissions for a user?

### Q2. What is the difference between dictionary[] and get()?
**Answer:** dictionary[key] raises KeyError when the key does not exist. get(key, default) returns a default value instead. get() is useful when a key is optional.

**Follow-up:** When would a missing dictionary key indicate a real programming error instead of an optional field?

## 15. Completion checklist
- [ ] Create and modify a list.
- [ ] Read values from a tuple.
- [ ] Use a set to remove duplicates.
- [ ] Add, update and retrieve dictionary values.
- [ ] Process a list of student dictionaries.
- [ ] Complete Student Record Manager.

**Next lesson:** Day 9 — Functions, parameters, arguments and return values.
