# Day 8: Lists, Tuples, Sets and Dictionaries

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–7 — variables, conditions, loops and strings  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Student Record Manager

## 1. Learning objectives

- Explain why collections are needed.
- Create and access lists, tuples, sets and dictionaries.
- Use common collection methods.
- Choose a collection based on the data and operations required.
- Represent simple business records using Python collections.

## 2. Why do we need collections?

A variable stores a reference to one value. Applications often need to manage many related values.

Examples:

- A list of employee names.
- A tuple representing fixed coordinates.
- A set of unique permission names.
- A dictionary containing one student's fields.

Python provides several built-in collection types for these purposes.

## 3. Lists

A list is an ordered, mutable collection. Mutable means its contents can be changed.

```python
students = ["Asha", "Ravi", "Meera"]

print(students)
print(students[0])
print(students[-1])
```

Output:

```text
['Asha', 'Ravi', 'Meera']
Asha
Meera
```

Common list methods:

| Method | Purpose |
|---|---|
| `append(value)` | Add one item at the end |
| `insert(index, value)` | Insert at a position |
| `extend(items)` | Add items from another iterable |
| `remove(value)` | Remove the first matching value |
| `pop(index)` | Remove and return an item |
| `sort()` | Sort the list in place |
| `count(value)` | Count occurrences |
| `index(value)` | Find the first matching position |

Example:

```python
students = ["Asha", "Ravi"]
students.append("Meera")
students.remove("Ravi")

print(students)
```

Output: `['Asha', 'Meera']`

If a value is not present, `remove()` raises `ValueError`. Check membership with `in` when necessary.

## 4. Tuples

A tuple is an ordered, immutable collection. Use it when the group of values should not be changed as a collection.

```python
location = (17.385, 78.4867)

print(location[0])
print(location[1])
```

Output:

```text
17.385
78.4867
```

A tuple can contain different types, but a common use is grouping related fixed values. A one-item tuple needs a trailing comma: `("Python",)`.

You can read tuple items, but cannot assign a new item at an index.

## 5. Sets

A set is an unordered collection of unique elements. It is useful when duplicates should be removed or membership should be checked.

```python
skills = {"Python", "Django", "Python", "SQL"}

print(skills)
print("Django" in skills)
```

The set contains each value once. The display order is not guaranteed.

Common methods:

- `add(value)` — add an element.
- `remove(value)` — remove an element; raises KeyError if missing.
- `discard(value)` — remove an element if present; does not raise if missing.
- `union(other)` — combine unique elements.
- `intersection(other)` — find common elements.

Example:

```python
team_a = {"Python", "SQL"}
team_b = {"Python", "Django"}

print(team_a.intersection(team_b))
print(team_a.union(team_b))
```

The shared skill is Python. Set display order can vary.

## 6. Dictionaries

A dictionary stores key-value pairs. It is useful for representing one record with named fields.

```python
student = {
    "student_id": 101,
    "name": "Asha",
    "course": "Python"
}

print(student["name"])
print(student["course"])
```

Output:

```text
Asha
Python
```

Access using a key:

- `student["name"]` raises `KeyError` if the key is absent.
- `student.get("email")` returns `None` by default if the key is absent.
- `student.get("email", "Not provided")` returns the supplied default.

Update and add fields:

```python
student["course"] = "Django"
student["email"] = "asha@example.com"

print(student)
```

Useful methods:

| Method | Purpose |
|---|---|
| `keys()` | Get dictionary keys |
| `values()` | Get values |
| `items()` | Get key-value pairs |
| `get(key)` | Read safely with an optional default |
| `update(data)` | Add or update multiple fields |
| `pop(key)` | Remove a key and return its value |

## 7. Loop through collections

```python
students = ["Asha", "Ravi", "Meera"]

for student_name in students:
    print(student_name)
```

For dictionary records:

```python
student = {"id": 101, "name": "Asha", "course": "Python"}

for key, value in student.items():
    print(key, ":", value)
```

A list of dictionaries can represent several records:

```python
students = [
    {"id": 101, "name": "Asha"},
    {"id": 102, "name": "Ravi"}
]

for student in students:
    print(student["id"], student["name"])
```

This structure is useful for small exercises and will help prepare for working with JSON records.

## 8. Choosing the right collection

| Collection | Ordered? | Mutable? | Duplicate values? | Common use |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Sequence of records |
| Tuple | Yes | No | Yes | Fixed group of values |
| Set | No guaranteed order | Yes | No | Unique values |
| Dictionary | Insertion-ordered | Yes | Keys are unique | Named fields for a record |

Choose based on how the data will be used, not just on syntax.

## 9. Common mistakes

- Accessing a list index that does not exist.
- Calling `remove()` for a value that is absent.
- Trying to modify a tuple.
- Expecting a set to preserve a meaningful display order.
- Using a dictionary key that is not present.
- Forgetting that dictionary keys must be unique.
- Modifying a list while iterating over it and unintentionally skipping items.

## 10. Industry scenario

A training platform needs to maintain student records. Each student's ID, name and course can be represented by a dictionary. A list can hold multiple student dictionaries. A set can keep a unique collection of course names.

This is a useful in-memory model for learning. A production multi-user application will normally store records in a database.

## 11. Approved mini-project — Student Record Manager

**Objective:** Create a small in-memory student record manager.

### Suggested data

Use a list of dictionaries. Each dictionary should contain student ID, name and course.

### Requirements

1. Add a student record.
2. Display all student records.
3. Search for a student using ID.
4. Update a student's course.
5. Prevent duplicate student IDs.
6. Display the unique course names using a set.
7. Use a tuple for a fixed institute or batch identifier if appropriate.

### Suggested structure

```text
student_record_manager/
└── student_manager.py
```

### Validation

- Add two students.
- Attempt to add a duplicate ID.
- Search for an existing and a missing ID.
- Update one course.
- Confirm unique course names are displayed once.

Do not add database persistence today; file handling is Day 11.

## 12. Key takeaways

- Lists are ordered and mutable.
- Tuples are ordered and immutable.
- Sets store unique values.
- Dictionaries map unique keys to values.
- A list of dictionaries is a simple way to represent multiple records.
- Select a collection based on the operations and guarantees you need.

**Next lesson:** Day 9 — Functions, parameters, arguments and return values.
