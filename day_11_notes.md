# Day 11: File Handling — Reading, Writing and Working with CSV and JSON

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–10 — strings, collections, functions and imports  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** File-Based User Management System

## 1. Learning objectives

- Explain why programs read and write files.
- Open and close files safely using `with`.
- Understand common file modes.
- Read and write text files.
- Read and write CSV records.
- Convert between Python data and JSON.
- Recognize basic file path and data-loss risks.

## 2. Why is file handling needed?

Variables and collections hold data while a program runs. When the program exits, those in-memory values normally disappear.

Files allow a small program to save information and load it during a later run.

Examples:

- Export a report.
- Read configuration values.
- Import employee records.
- Exchange structured data with another system.
- Save a local training exercise's records.

A file is useful for learning and simple interchange. A production multi-user backend usually uses a database for concurrent, reliable data management.

## 3. Open and close a file

Python's built-in `open()` function opens a file.

```python
file = open("welcome.txt", "w")
file.write("Welcome to Python file handling")
file.close()
```

- The first argument is the file path.
- `"w"` opens the file for writing.
- `write()` writes text.
- `close()` releases the file resource.

If an error occurs before `close()`, manual cleanup can be missed. Prefer a context manager.

## 4. Use with open()

```python
with open("welcome.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python file handling")

print("File saved")
```

The file is closed automatically when execution leaves the `with` block, including when an exception occurs.

Read the file:

```python
with open("welcome.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Output:

```text
Welcome to Python file handling
```

## 5. Common file modes

| Mode | Meaning |
|---|---|
| `r` | Read; file must exist |
| `w` | Write; creates or truncates an existing file |
| `a` | Append; adds content at the end |
| `x` | Create a new file; fails if it already exists |
| `b` | Binary mode modifier |
| `+` | Read and write modifier |

Important: `w` can erase existing file content. Use it only when replacing the content is intended. Use `a` when appending is appropriate.

## 6. Read a file in different ways

`read()` reads the content as one string.

```python
with open("employees.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

`readline()` reads one line. Iterating over the file reads it line by line:

```python
with open("employees.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Line-by-line processing can be useful when a file is too large to load entirely into memory.

## 7. Work with CSV files

CSV means Comma-Separated Values. It is a simple tabular format with rows and columns.

Example file `employees.csv`:

```csv
employee_id,name,department
101,Asha,Engineering
102,Ravi,Finance
```

Use Python's built-in `csv` module.

### Read CSV using DictReader

```python
import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["employee_id"], row["name"], row["department"])
```

Expected output:

```text
101 Asha Engineering
102 Ravi Finance
```

Each row is represented as a dictionary using the header names as keys.

### Write CSV using DictWriter

```python
import csv

employees = [
    {"employee_id": 101, "name": "Asha", "department": "Engineering"},
    {"employee_id": 102, "name": "Ravi", "department": "Finance"}
]

with open("employee_export.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["employee_id", "name", "department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(employees)
```

`writeheader()` writes the column names. `writerows()` writes all records.

## 8. Work with JSON

JSON stands for JavaScript Object Notation. It is a text format commonly used for exchanging structured data between applications.

Example JSON:

```json
{
  "employee_id": 101,
  "name": "Asha",
  "skills": ["Python", "Django"]
}
```

Python's `json` module converts between JSON text and Python objects.

### Write JSON to a file

```python
import json

employee = {
    "employee_id": 101,
    "name": "Asha",
    "skills": ["Python", "Django"]
}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)
```

- `json.dump()` writes a Python object to a file object.
- `indent=4` makes the saved JSON easier to read.

### Read JSON from a file

```python
import json

with open("employee.json", "r", encoding="utf-8") as file:
    employee = json.load(file)

print(employee["name"])
print(employee["skills"])
```

Output:

```text
Asha
['Python', 'Django']
```

Remember the difference:

| Function | Purpose |
|---|---|
| `json.dump()` | Write Python data to a file |
| `json.load()` | Read JSON data from a file |
| `json.dumps()` | Convert Python data to a JSON string |
| `json.loads()` | Convert a JSON string to Python data |

## 9. CSV versus JSON

| CSV | JSON |
|---|---|
| Best suited to rows and columns | Supports objects, arrays and nested structures |
| Often used for spreadsheet exchange | Commonly used in APIs and configuration |
| Usually has a header row | Uses keys and values |
| Less suitable for nested data | Represents nested data naturally |

Choose the format based on the structure and needs of the system receiving the data.

## 10. File paths and common errors

A relative path is interpreted from the program's current working directory.

Check the working directory:

```python
import os

print(os.getcwd())
```

Common issues:

| Error/problem | Possible reason | Response |
|---|---|---|
| `FileNotFoundError` | Path is wrong or file is absent | Check working directory and path |
| `PermissionError` | Process cannot access the file | Check permissions and whether another process holds it |
| Existing content disappears | File opened with `w` | Use append or a safe replacement strategy |
| `JSONDecodeError` | File does not contain valid JSON | Inspect the saved content |
| CSV columns are incorrect | Header or delimiter mismatch | Check the file format and DictReader configuration |

Do not assume that a missing file is always an error. A new application may intentionally initialize an empty data store, but this behavior should be explicit.

## 11. Industry scenario

An internal tool imports employee records from a CSV file and exports a structured JSON summary for another application. Python can read rows, validate fields and write the result.

A local file is suitable for this controlled exercise. A real multi-user employee application would generally use a database and backend APIs rather than a shared JSON file.

## 12. Approved mini-project — File-Based User Management System

**Objective:** Create a terminal application that stores user records in JSON and exports them to CSV.

### Requirements

1. Store users as a list of dictionaries.
2. Each user has an ID, name and email.
3. Load existing users from a JSON file if it exists.
4. Add a user record.
5. Display all users.
6. Save records back to JSON.
7. Export records to CSV.
8. Do not store passwords or other secrets.

### Suggested structure

```text
file_based_user_management/
├── main.py
├── users.json
└── users.csv
```

### Validation

- Start when `users.json` does not exist.
- Add at least two users.
- Run the program again and confirm saved records load.
- Export and inspect the CSV.
- Check that IDs, names and emails appear in the correct columns.
- Confirm that the program does not unintentionally erase records.

For a safer replacement workflow, write new content to a temporary file and replace the old file only after the new data has been written successfully. This exercise is not a concurrent multi-user storage service.

## 13. Key takeaways

- Files preserve data after a program exits.
- Use `with open()` to manage file resources safely.
- Understand the difference between read, write, append and create modes.
- Python's `csv` module handles tabular text files.
- Python's `json` module exchanges structured data.
- Be careful with relative paths and write mode.
- Files are useful for learning and interchange; databases are normally used for production multi-user applications.

**Next lesson:** Day 12 — Exception handling, debugging and basic logging.
