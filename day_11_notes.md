# Day 11: File Handling — Reading, Writing and Working with CSV and JSON

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–10 — strings, collections, functions and imports  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** File-Based User Management System

> **Beginner note:** A variable stores information while your program is running. But what happens when you close the program? Normally, the in-memory value disappears. Files allow a small program to save information and read it again later.

## 1. Learning objectives

You should be able to:
- Explain why file handling is needed.
- Open and close a file safely using with.
- Read and write text files.
- Understand common file modes.
- Read and write CSV files.
- Convert Python data to JSON and JSON back to Python data.
- Recognize file path, overwrite and data-loss risks.

## 2. What is file handling?

File handling means using a program to create, read, update or write information in files.

Examples:
- Save a report.
- Read application configuration.
- Import employee information.
- Export student records.
- Exchange structured information between systems.

A Python list exists in memory while the program is running. If you close the program, that list is normally lost. If you save the information to a file, the program can read it in a later run.

Files are useful for learning and simple data exchange. A production multi-user backend normally uses a database for reliable concurrent data management.

## 3. Create your first text file

Python has a built-in function named `open()`.

Syntax:
```python
open(file_path, mode)
```

Beginner example:
```python
file = open("welcome.txt", "w")
file.write("Welcome to Python file handling")
file.close()
```

What each line does:
- `open()` opens or creates the file.
- `"welcome.txt"` is the file name.
- `"w"` means write mode.
- `write()` writes text into the file.
- `close()` closes the file and releases the resource.

After running this code, check your project folder. A file named welcome.txt should exist.

Important: write mode can replace the contents of an existing file. Do not use it carelessly when existing data must be preserved.

## 4. Use with open() — the safer approach

Manual close can be forgotten if an error occurs. Python provides a context manager using `with`.

```python
with open("welcome.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python file handling")

print("File saved")
```

Explanation:
- `with` manages the file resource.
- `open()` opens the file.
- `as file` gives the opened file object the name file.
- The indented write statement uses that file.
- When execution leaves the with block, Python closes the file automatically.

Use `with open()` as your normal file-handling pattern.

## 5. Understand file modes

The mode tells Python what you want to do with the file.

| Mode | Meaning | Important behavior |
|---|---|---|
| `r` | Read | File must exist |
| `w` | Write | Creates file or truncates existing content |
| `a` | Append | Adds content at the end |
| `x` | Create exclusively | Fails if the file already exists |
| `b` | Binary modifier | Used for binary data |
| `+` | Read and write modifier | Combines reading and writing |

### Read mode

```python
with open("welcome.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Output:
```text
Welcome to Python file handling
```

If the file does not exist, read mode raises FileNotFoundError.

### Append mode

```python
with open("welcome.txt", "a", encoding="utf-8") as file:
    file.write("\nSecond line added")
```

The new text is added at the end. The newline character `\n` starts a new line.

### Exclusive create mode

```python
with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("Created for the first time")
```

This creates a new file. If the file already exists, Python raises FileExistsError rather than overwriting it.

## 6. Read a file using read()

`read()` reads content from the file and returns it as a string.

```python
with open("welcome.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Use read() when the file is small enough to load into memory.

## 7. Read a file using readline()

`readline()` reads one line at a time.

```python
with open("employees.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print(first_line)
print(second_line)
```

Each call reads the next line from the current file position. If there are no more lines, it returns an empty string.

## 8. Read a file line by line using a loop

```python
with open("employees.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Explanation:
- The for loop visits each line.
- `line` contains one line of text.
- `strip()` removes surrounding whitespace, including the newline at the end.
- This approach avoids loading the entire file into one string.

For large files, processing one line at a time can use less memory.

## 9. Understand file paths and current working directory

A **file path** tells Python where a file is located.

A relative path such as `"welcome.txt"` is interpreted relative to the program's current working directory.

Check the working directory:

```python
import os

print(os.getcwd())
```

`os.getcwd()` returns the current working directory.

Common path problems:
- The file is in a different folder.
- The program is being run from an unexpected working directory.
- The filename spelling or extension is incorrect.

Use VS Code's terminal and inspect the folder before assuming the file is missing.

## 10. What is CSV?

CSV means **Comma-Separated Values**. It is a text format commonly used to store tabular information.

Example file named employees.csv:

```csv
employee_id,name,department
101,Asha,Engineering
102,Ravi,Finance
103,Meera,HR
```

The first line contains column headings. Each following line contains one record.

Python provides a built-in module called `csv`.

## 11. Read CSV using DictReader()

Create employees.csv as shown above.

```python
import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["employee_id"], row["name"], row["department"])
```

Output:
```text
101 Asha Engineering
102 Ravi Finance
103 Meera HR
```

Understand it:
- `import csv` imports the CSV module.
- `DictReader(file)` reads each row as a dictionary.
- The column headings become dictionary keys.
- `row["name"]` accesses the name column.
- The loop processes every data row.

CSV values are read as text by default. Convert numeric columns when numeric calculations are needed.

## 12. Read CSV using reader()

`csv.reader()` reads each row as a list.

```python
import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Example output:
```text
['employee_id', 'name', 'department']
['101', 'Asha', 'Engineering']
['102', 'Ravi', 'Finance']
['103', 'Meera', 'HR']
```

Difference:
- reader() gives each row as a list.
- DictReader() gives each row as a dictionary using header names.

## 13. Write CSV using DictWriter()

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

Explanation:
- `fieldnames` defines the CSV columns and their order.
- `DictWriter()` prepares a writer that expects dictionaries.
- `writeheader()` writes the column names.
- `writerows()` writes all employee records.

Use write mode only when creating or intentionally replacing the export file.

## 14. What is JSON?

JSON stands for **JavaScript Object Notation**. It is a text format used to exchange structured data between applications.

Example JSON:

```json
{
  "employee_id": 101,
  "name": "Asha",
  "skills": ["Python", "Django"],
  "active": true
}
```

JSON supports objects, arrays, strings, numbers, booleans and null. It is common in web APIs because it can represent structured and nested data.

Python's built-in `json` module converts between JSON text and Python objects.

## 15. Write JSON using dump()

```python
import json

employee = {
    "employee_id": 101,
    "name": "Asha",
    "skills": ["Python", "Django"],
    "active": True
}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)
```

Explanation:
- `import json` imports the JSON module.
- `json.dump()` writes a Python object to a file.
- `indent=4` formats the saved JSON with indentation so it is easy to read.

## 16. Read JSON using load()

```python
import json

with open("employee.json", "r", encoding="utf-8") as file:
    employee = json.load(file)

print(employee["name"])
print(employee["skills"])
print(employee["active"])
```

Output:
```text
Asha
['Python', 'Django']
True
```

json.load() reads JSON from a file and converts it into corresponding Python values.

## 17. dump(), load(), dumps() and loads()

These four names are easy to confuse. Remember that the final s means string.

| Function | Purpose |
|---|---|
| `json.dump(data, file)` | Write Python data to a file |
| `json.load(file)` | Read JSON from a file |
| `json.dumps(data)` | Convert Python data to a JSON string |
| `json.loads(text)` | Convert a JSON string into Python data |

Example with strings:

```python
import json

employee = {"id": 101, "name": "Asha"}

json_text = json.dumps(employee)
print(json_text)

python_data = json.loads(json_text)
print(python_data["name"])
```

Output:
```text
{"id": 101, "name": "Asha"}
Asha
```

## 18. CSV versus JSON

| CSV | JSON |
|---|---|
| Best suited to rows and columns | Supports objects, arrays and nested structures |
| Common for spreadsheet exchange | Common for API data exchange |
| Usually has a header row | Uses keys and values |
| Less suitable for nested data | Represents nested data naturally |

Choose the format based on the system receiving the data and the structure you need.

## 19. Common errors and safety

| Error/problem | Possible reason | What to check |
|---|---|---|
| FileNotFoundError | File path is wrong or file is missing | Current working directory and filename |
| PermissionError | Process cannot access the file | File permissions and whether another process is using it |
| Existing content disappears | File opened with w | Use append or a safe replacement strategy |
| JSONDecodeError | File content is not valid JSON | Inspect the file content |
| Wrong CSV columns | Header or delimiter mismatch | Check the input file and reader configuration |

Never save passwords or API keys in plain-text practice files. Do not assume a local JSON file is safe storage for a multi-user application.

## 20. Industry scenario

An internal tool imports employee details from a CSV file, checks the records and exports a structured JSON summary for another system. Python can read rows, validate fields and write the result.

A local file is suitable for this controlled exercise. A real multi-user employee application would normally use a database and backend APIs rather than a shared JSON file.

## 21. Interview preparation

**Q1. Why do we use with open() in Python?**

Answer: It uses a context manager to manage the file resource. The file is closed automatically when execution leaves the block, including when an exception occurs.

**Q2. Difference between read() and readline()?**

Answer: read() reads file content as a string. readline() reads one line at a time.

**Q3. Difference between json.dump() and json.dumps()?**

Answer: dump() writes JSON to a file object. dumps() returns JSON text as a string.

**Q4. Difference between CSV and JSON?**

Answer: CSV is commonly used for tabular rows and columns. JSON supports nested objects and arrays and is widely used for API data exchange.

## 22. Approved mini-project — File-Based User Management System

**Objective:** Create a terminal application that stores user records in JSON and exports them to CSV.

### Requirements
1. Store users as a list of dictionaries.
2. Each user has an ID, name and email.
3. Load existing users from a JSON file if it exists.
4. Add a user record.
5. Display all users.
6. Save records back to JSON.
7. Export records to CSV.
8. Do not store passwords or secrets.
9. Avoid overwriting data unintentionally.

### Suggested structure

```text
file_based_user_management/
├── main.py
├── users.json
└── users.csv
```

### Validation
- Start when users.json does not exist.
- Add at least two users.
- Run the program again and confirm saved records load.
- Export and inspect the CSV.
- Check that IDs, names and emails appear in the correct columns.
- Confirm the program does not erase records unintentionally.

For a safer replacement workflow, write new content to a temporary file and replace the old file only after the new content has been written successfully. This exercise is not a concurrent multi-user storage service.

## 23. Daily practice and completion check

1. Create a text file and write a message.
2. Read the message using read().
3. Read a file line by line.
4. Create a small CSV and read it with DictReader().
5. Write a CSV using DictWriter().
6. Save a dictionary as JSON using dump().
7. Read the JSON using load().
8. Explain the difference between dump() and dumps().

You have completed Day 11 when you can save Python data to a file, load it again and explain which format is suitable for a simple tabular export versus structured application data.

**Next lesson:** Day 12 — Exception handling, debugging and basic logging.
