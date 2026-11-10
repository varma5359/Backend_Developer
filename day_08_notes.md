# Day 8: Lists, Tuples, Sets and Dictionaries

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–7 — variables, conditions, loops and strings  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Student Record Manager

> **Beginner note:** A variable can refer to one value. But what if you need to store 100 student names? Creating 100 separate variables would be difficult. Python collections help us store and manage groups of values.

## 1. Learning objectives

You will learn to:
- Explain why collections are needed.
- Create and access lists, tuples, sets and dictionaries.
- Use important methods of each collection.
- Understand mutable and immutable collections.
- Choose the right collection for a simple business problem.
- Store multiple student records using a list of dictionaries.

## 2. What is a collection?

A collection is a data structure that stores multiple values together.

Imagine a college:
- The list of students in a class.
- The fixed coordinates of the college building.
- The unique courses offered.
- The details of one student.

Python has built-in collection types for these different requirements.

## 3. List — store multiple items in order

A **list** is an ordered and mutable collection. Ordered means items have positions. Mutable means we can add, remove or update items.

Create a list:

```python
students = ["Asha", "Ravi", "Meera"]
print(students)
```

Output:
```text
['Asha', 'Ravi', 'Meera']
```

A list uses square brackets `[]`. Items are separated by commas.

### 3.1 Access list items using index

```python
students = ["Asha", "Ravi", "Meera"]

print(students[0])
print(students[1])
print(students[-1])
```

Output:
```text
Asha
Ravi
Meera
```

Indexing starts at zero. Negative indexing starts at the end. An index that does not exist causes an IndexError.

### 3.2 Update a list item

```python
students = ["Asha", "Ravi", "Meera"]
students[1] = "John"

print(students)
```

Output: `['Asha', 'John', 'Meera']`

The item at index 1 was replaced. Lists are mutable, so this update is allowed.

### 3.3 append() — add one item at the end

Syntax: `list.append(item)`

```python
students = ["Asha", "Ravi"]
students.append("Meera")

print(students)
```

Output: `['Asha', 'Ravi', 'Meera']`

Explanation:
- append() receives one item.
- It adds that item to the end of the existing list.
- It changes the original list.
- It returns None; normally you do not assign the result back to the list.

A common mistake:
```python
# students = students.append("Meera")  # Wrong: students becomes None
```

Correct:
```python
students.append("Meera")
```

### 3.4 insert() — add an item at a particular position

Syntax: `list.insert(index, item)`

```python
students = ["Asha", "Meera"]
students.insert(1, "Ravi")

print(students)
```

Output: `['Asha', 'Ravi', 'Meera']`

The first argument is the position; the second is the value. Existing items at that position and after it move to the right.

Difference:
- append() adds at the end.
- insert() adds at the requested position.

### 3.5 extend() — add multiple items

```python
students = ["Asha", "Ravi"]
new_students = ["Meera", "John"]

students.extend(new_students)
print(students)
```

Output: `['Asha', 'Ravi', 'Meera', 'John']`

extend() takes items from another iterable and adds them individually.

Compare:
```python
first = ["Asha", "Ravi"]
first.append(["Meera", "John"])
print(first)

second = ["Asha", "Ravi"]
second.extend(["Meera", "John"])
print(second)
```

Output:
```text
['Asha', 'Ravi', ['Meera', 'John']]
['Asha', 'Ravi', 'Meera', 'John']
```

append() adds the entire list as one item. extend() adds each element.

### 3.6 remove() — remove a matching value

```python
students = ["Asha", "Ravi", "Meera"]
students.remove("Ravi")

print(students)
```

Output: `['Asha', 'Meera']`

remove() deletes the first matching value. If the value does not exist, Python raises ValueError.

Safe beginner check:
```python
if "Ravi" in students:
    students.remove("Ravi")
```

The `in` operator checks whether the value exists before removal.

### 3.7 pop() — remove and return an item

```python
students = ["Asha", "Ravi", "Meera"]
removed_student = students.pop()

print(removed_student)
print(students)
```

Output:
```text
Meera
['Asha', 'Ravi']
```

By default, pop() removes the last item. You can supply an index:

```python
students = ["Asha", "Ravi", "Meera"]
removed_student = students.pop(0)

print(removed_student)
print(students)
```

Output:
```text
Asha
['Ravi', 'Meera']
```

Difference:
- remove(value) searches for a value and removes it.
- pop(index) removes an item at a position and returns it.

### 3.8 sort() — sort the list in place

```python
marks = [70, 95, 60, 85]
marks.sort()

print(marks)
```

Output: `[60, 70, 85, 95]`

sort() changes the original list. For descending order:

```python
marks = [70, 95, 60, 85]
marks.sort(reverse=True)

print(marks)
```

Output: `[95, 85, 70, 60]`

The parameter `reverse=True` requests descending order.

### 3.9 sorted() — return a new sorted list

```python
marks = [70, 95, 60]
result = sorted(marks)

print(result)
print(marks)
```

Output:
```text
[60, 70, 95]
[70, 95, 60]
```

Difference:
- sort() changes the original list and returns None.
- sorted() returns a new sorted list and leaves the original unchanged.

### 3.10 Other useful list operations

| Operation | Example | Meaning |
|---|---|---|
| length | `len(students)` | Number of items |
| count | `students.count("Asha")` | Number of occurrences |
| index | `students.index("Ravi")` | Position of first match |
| clear | `students.clear()` | Remove all items |
| copy | `students.copy()` | Make a shallow copy |

Example:
```python
students = ["Asha", "Ravi", "Asha"]
print(len(students))
print(students.count("Asha"))
print(students.index("Ravi"))
```

Output:
```text
3
2
1
```

index() raises ValueError if the requested value is not present. Check membership first if needed.

## 4. Tuple — store an ordered group that should not be changed

A **tuple** is ordered and immutable. It is similar to a list, but its elements cannot be reassigned after creation.

```python
location = (17.385, 78.4867)

print(location)
print(location[0])
print(location[1])
```

Output:
```text
(17.385, 78.4867)
17.385
78.4867
```

A tuple uses parentheses. You can read values using indexes, but this is not allowed:

```python
# location[0] = 20  # TypeError: tuple does not support item assignment
```

### 4.1 Why use a tuple?

Use a tuple when the group of values represents a fixed collection, such as:
- Coordinates.
- A fixed RGB color value.
- A fixed pair of dimensions.

### 4.2 One-item tuple

```python
single_item = ("Python",)
print(type(single_item))
```

Output:
```text
<class 'tuple'>
```

The comma is important. Without it, parentheses simply group the value.

### 4.3 Tuple methods

Tuples have fewer methods because they cannot be changed.

`count()` counts matching items:
```python
values = (10, 20, 10, 30)
print(values.count(10))
```
Output: `2`

`index()` returns the position of the first matching item:
```python
values = (10, 20, 30)
print(values.index(20))
```
Output: `1`

If the value does not exist, index() raises ValueError.

## 5. Set — store unique values

A **set** is a collection of unique elements. Duplicate values are removed. Sets do not provide positional indexing.

```python
skills = {"Python", "Django", "Python", "SQL"}
print(skills)
```

The set contains Python, Django and SQL once each. The display order is not guaranteed.

### 5.1 Create an empty set

```python
empty_set = set()
empty_dictionary = {}

print(type(empty_set))
print(type(empty_dictionary))
```

Output:
```text
<class 'set'>
<class 'dict'>
```

Important: `{}` creates an empty dictionary, not an empty set. Use `set()` for an empty set.

### 5.2 add() — add one element

```python
skills = {"Python", "SQL"}
skills.add("Django")
print(skills)
```

The set now contains all three unique skills. Its display order may vary.

If you add Python again, the set still contains only one Python element.

### 5.3 update() — add multiple elements

```python
skills = {"Python"}
skills.update(["Django", "SQL"])
print(skills)
```

update() adds elements from an iterable.

### 5.4 remove() and discard()

```python
skills = {"Python", "Django", "SQL"}
skills.remove("SQL")
skills.discard("Java")
print(skills)
```

- remove() deletes an existing element but raises KeyError if it is missing.
- discard() deletes the element if present and does not raise an error if it is absent.

### 5.5 Set union()

Union combines elements from two sets, keeping unique values.

```python
team_a = {"Python", "SQL"}
team_b = {"Python", "Django"}

print(team_a.union(team_b))
```

The result contains Python, SQL and Django.

### 5.6 Set intersection()

Intersection returns values common to both sets.

```python
team_a = {"Python", "SQL"}
team_b = {"Python", "Django"}

print(team_a.intersection(team_b))
```

Output: `{'Python'}`

### 5.7 Set difference()

Difference returns elements in the first set that are not in the second.

```python
team_a = {"Python", "SQL"}
team_b = {"Python", "Django"}

print(team_a.difference(team_b))
```

Output: `{'SQL'}`

### 5.8 Membership check

```python
skills = {"Python", "Django"}
print("Python" in skills)
print("Java" in skills)
```

Output:
```text
True
False
```

This is useful when checking whether a unique permission or skill is present.

## 6. Dictionary — store data as key-value pairs

A **dictionary** stores information using keys and values. It is useful for describing one record.

Imagine one student record:
- Student ID: 101.
- Name: Asha.
- Course: Python.

```python
student = {
    "student_id": 101,
    "name": "Asha",
    "course": "Python"
}

print(student)
print(student["name"])
print(student["course"])
```

Output:
```text
{'student_id': 101, 'name': 'Asha', 'course': 'Python'}
Asha
Python
```

A dictionary uses curly braces. Each key is associated with a value using a colon.

### 6.1 Access a value using a key

```python
student = {"id": 101, "name": "Asha"}
print(student["name"])
```

Output: `Asha`

If the key does not exist, square-bracket access raises KeyError.

### 6.2 get() — read a value safely

```python
student = {"id": 101, "name": "Asha"}

print(student.get("name"))
print(student.get("email"))
print(student.get("email", "Not provided"))
```

Output:
```text
Asha
None
Not provided
```

Explanation:
- get("name") returns the name.
- get("email") returns None because the key is missing.
- get("email", "Not provided") returns the supplied default.

Use get() when a key may be absent and you want to avoid KeyError.

### 6.3 Add a new key-value pair

```python
student = {"id": 101, "name": "Asha"}
student["email"] = "asha@example.com"

print(student)
```

A new email key is added.

### 6.4 Update an existing value

```python
student = {"id": 101, "course": "Python"}
student["course"] = "Django"

print(student)
```

Output: `{'id': 101, 'course': 'Django'}`

The key already exists, so its value is replaced.

### 6.5 update() — add or update multiple pairs

```python
student = {"id": 101, "name": "Asha"}
student.update({"course": "Python", "city": "Hyderabad"})

print(student)
```

update() adds new keys or replaces values for keys that already exist.

### 6.6 keys(), values() and items()

```python
student = {"id": 101, "name": "Asha", "course": "Python"}

print(student.keys())
print(student.values())
print(student.items())
```

- keys() provides the dictionary's keys.
- values() provides the values.
- items() provides key-value pairs.

Use them in loops:
```python
for key, value in student.items():
    print(key, ":", value)
```

### 6.7 pop() — remove a key and return its value

```python
student = {"id": 101, "name": "Asha", "course": "Python"}
removed_course = student.pop("course")

print(removed_course)
print(student)
```

pop() removes the key and returns its value. If the key is absent, it raises KeyError unless a default is supplied.

### 6.8 len() — count key-value pairs

```python
student = {"id": 101, "name": "Asha", "course": "Python"}
print(len(student))
```

Output: `3`

The result is the number of key-value pairs, not the number of characters in the values.

## 7. A list of dictionaries — represent many records

A common beginner-friendly structure for multiple records is a list where each item is a dictionary.

```python
students = [
    {"id": 101, "name": "Asha", "course": "Python"},
    {"id": 102, "name": "Ravi", "course": "Django"},
    {"id": 103, "name": "Meera", "course": "Python"}
]

for student in students:
    print(student["id"], student["name"], student["course"])
```

Output:
```text
101 Asha Python
102 Ravi Django
103 Meera Python
```

Understand the structure:
- The outer square brackets create a list.
- Each inner curly-brace group is one dictionary.
- Each dictionary represents one student.
- The loop visits one student record at a time.

This structure resembles the kind of records you may later receive from an API. It is an in-memory example, not a database.

## 8. Compare the four collections

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `set()` or `{}` with items | `{key: value}` |
| Ordered | Yes | Yes | No positional order | Insertion-ordered |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No duplicate elements | Keys are unique |
| Access | Index | Index | Membership | Key |
| Common use | Sequence of records | Fixed group | Unique values | Named record fields |

## 9. Common beginner mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Using append() when you want to add each item from another list | append adds the whole object as one item | Use extend() |
| Assigning the result of sort() | sort changes the list and returns None | Call sort() separately |
| Using an invalid list index | Position does not exist | Check length and valid indexes |
| Trying to update a tuple | Tuples are immutable | Create a new tuple if needed |
| Expecting set order | Sets do not support positional order | Use a list if order matters |
| Using {} for an empty set | Empty braces create a dictionary | Use set() |
| Accessing a missing dictionary key | Key is absent | Use get() or check membership |
| Assuming dictionary values are unique | Only keys must be unique | Check values if uniqueness is required |

## 10. Industry scenario

A training platform needs to manage student records. Each student has an ID, name and course. A dictionary represents one student, and a list stores multiple student dictionaries. A set can store the unique course names.

This is a learning model. A real multi-user application will store records in a database, which you will learn later.

## 11. Interview preparation

**Q1. Difference between list and tuple?**

Answer: Both are ordered collections. A list is mutable, while a tuple is immutable.

Follow-up: When would you use a tuple?  
Answer: When a fixed group of values should not be changed as a collection, such as coordinates.

**Q2. Why use a set?**

Answer: A set stores unique elements and is useful for removing duplicates and checking membership.

Follow-up: How do you create an empty set?  
Answer: Use set(), because {} creates an empty dictionary.

**Q3. Difference between append() and extend()?**

Answer: append() adds one object as one item. extend() adds each element from an iterable.

**Q4. Difference between dictionary [] and get()?**

Answer: Square-bracket access raises KeyError if the key is absent. get() returns None or a supplied default.

## 12. Approved mini-project — Student Record Manager

**Objective:** Create an in-memory program to manage a small set of student records.

### Suggested data

Use a list of dictionaries. Each dictionary should contain student ID, name and course.

### Requirements
1. Add a student record.
2. Display all student records.
3. Search for a student using ID.
4. Update a student's course.
5. Prevent duplicate student IDs.
6. Display unique course names using a set.
7. Use a tuple for a fixed batch identifier if appropriate.

### Validation
- Add two students.
- Attempt to add a duplicate ID.
- Search for an existing and a missing ID.
- Update one course.
- Confirm that unique course names appear once.

Do not add database persistence today. File handling is Day 11.

## 13. Daily practice and completion check

1. Create a list of five student names.
2. Add one name using append().
3. Insert a name at index 1.
4. Remove a name using remove() and pop().
5. Create a tuple of three fixed values.
6. Create a set from a list containing duplicates.
7. Create a dictionary for one employee.
8. Create a list of three employee dictionaries and print each employee's name.

You have completed Day 8 when you can explain why you chose a list, tuple, set or dictionary for a particular requirement and demonstrate its common operations.

**Next lesson:** Day 9 — Functions, parameters, arguments and return values.
