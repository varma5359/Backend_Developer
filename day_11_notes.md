# Day 11: File Handling — Reading, Writing and Working with CSV and JSON

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–10; strings, collections, functions and imports  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** File-Based User Management System

## 1. Learning objectives
- Explain why applications read and write files.
- Open and close files safely using with.
- Read text and write text.
- Read and write CSV records using the csv module.
- Read and write JSON using the json module.
- Choose an appropriate file format for simple structured data.

## 2. What is file handling?
File handling lets a program read information from storage and write results for later use.

Examples:
- Save application settings.
- Read a list of records from a CSV file.
- Exchange JSON data with another system.
- Write diagnostic or report output.

Files are not a replacement for a production database when multiple users need concurrent, reliable record operations. Database use is covered later in this pathway.

## 3. Open and close files
Python's open() function opens a file. Use a context manager with `with` so the file is closed automatically after the block.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python file handling")
```

Modes:
- `"r"`: read.
- `"w"`: write, replacing existing content.
- `"a"`: append at the end.
- `"x"`: create a new file and fail if it already exists.

## 4. Read a text file
```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

If the file does not exist in read mode, Python raises FileNotFoundError.

## 5. Read lines
```python
with open("employees.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Iterating over the file reads it line by line, which can be more memory-efficient than reading a very large file entirely into one string.

## 6. Append to a file
```python
with open("activity.txt", "a", encoding="utf-8") as file:
    file.write("New activity recorded\n")
```

Append mode preserves existing content and adds new content at the end.

## 7. Work with CSV
CSV (Comma-Separated Values) stores tabular rows. Python's csv module provides readers and writers.

Create `employees.csv`:
```python
import csv

employees = [
    {"id": 101, "name": "Asha", "department": "IT"},
    {"id": 102, "name": "Ravi", "department": "HR"}
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "name", "department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)
```

Read CSV:
```python
import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["id"], row["name"], row["department"])
```

CSV values are read as strings. Convert fields such as id to int if numerical operations are needed.

## 8. Work with JSON
JSON (JavaScript Object Notation) is a text format commonly used for structured data exchange.

Python's json module converts between Python data and JSON text:
- json.dump(): write Python data to a file.
- json.load(): read JSON data from a file.
- json.dumps(): convert Python data to a JSON string.
- json.loads(): parse a JSON string.

Write JSON:
```python
import json

user = {
    "id": 101,
    "name": "Asha",
    "skills": ["Python", "Django"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
```

Read JSON:
```python
with open("user.json", "r", encoding="utf-8") as file:
    loaded_user = json.load(file)

print(loaded_user["name"])
print(loaded_user["skills"])
```

Expected output:
```text
Asha
['Python', 'Django']
```

JSON objects normally map to Python dictionaries, arrays to lists, strings to strings, numbers to numeric types, booleans to bool and null to None.

## 9. CSV versus JSON
| CSV | JSON |
|---|---|
| Best suited to rows and columns | Best suited to nested structured data |
| Often used for spreadsheet exchange | Often used for API payloads and configuration |
| Fields are usually read as text | Supports strings, numbers, booleans, arrays, objects and null |
| Simple tabular layout | Supports nested structures |

Choose based on the data structure and the system that consumes the file.

## 10. File paths and folders
Use pathlib to work with paths more reliably:
```python
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

file_path = data_folder / "users.json"
print(file_path)
```

Relative paths are resolved from the process's current working directory. Understand where the program is being run when a file cannot be found.

## 11. Common beginner mistakes
- Using write mode when append mode was intended.
- Forgetting that write mode replaces existing content.
- Using a wrong relative path.
- Forgetting encoding when working with text.
- Forgetting newline="" for CSV files on platforms where it matters.
- Treating CSV field values as numeric automatically.
- Assuming JSON files contain valid JSON without checking.

## 12. Industry scenario
A small internal tool needs to import employee records from a CSV file and export a summary to JSON for another application. Python can read each CSV row, validate fields and write a structured JSON file. A larger multi-user system would normally use a database and API instead of a shared local file.

## 13. Approved mini-project — File-Based User Management System

**Objective:** Create a simple terminal application that stores and retrieves user records using a JSON file and exports records to CSV.

### Requirements
1. Store users as a list of dictionaries.
2. Each user has ID, name and email.
3. Load existing users from a JSON file if it exists.
4. Add a user record.
5. Display all users.
6. Save records back to JSON.
7. Export the records to CSV.
8. Avoid storing passwords or other secrets in this exercise.

**Suggested structure**
```text
file_based_user_management/
├── main.py
├── users.json
└── users.csv
```

### Validation
- Start when users.json does not yet exist.
- Add at least two users.
- Run the application again and confirm saved records can be loaded.
- Export and open the CSV.
- Check that IDs, names and emails are written to the correct columns.

For safe persistence, avoid overwriting an existing file until the program has successfully built the new data. The project is a learning exercise, not a concurrent multi-user storage service.

## 14. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint for loading JSON only when the file exists." |
| 2 — Plan | "Break File-Based User Management System into load, add, display, save and export steps." |
| 3 — Example | "Show a small csv.DictWriter example for two records." |
| 4 — Guided implementation | "Guide me through JSON loading first; wait for my output." |
| 5 — Explanation | "Explain the difference between json.dump, json.load, dumps and loads." |
| 6 — Debugging | "Help me diagnose this FileNotFoundError using my current working directory." |
| 7 — Review | "Review my file-based user manager for data loss, malformed data and path issues." |

**Planning prompt:** "Help me design the record structure, file formats and operations. Do not write the complete program."

**Implementation prompt:** "Guide me one file operation at a time and explain the expected file contents."

**Debugging/review prompt:** "Inspect my file-handling code and explain any risky write mode, path or serialization issue."

## 15. Daily quiz

**Q1. Which mode opens a file for appending?**  
A. r  
B. w  
C. a  
D. x  
**Correct: C.** Append mode adds data at the end.

**Q2. Why use with open(...)?**  
A. It closes the file automatically after the block  
B. It converts CSV to JSON  
C. It starts a server  
D. It deletes the file  
**Correct: A.** The context manager handles file cleanup.

**Q3. Which module is used for CSV operations?**  
A. csv  
B. json  
C. math  
D. datetime  
**Correct: A.** Python provides the csv module for tabular text files.

**Q4. Which function reads JSON from an opened file object?**  
A. json.dump()  
B. json.load()  
C. json.dumps()  
D. json.loads()  
**Correct: B.** json.load parses JSON from a file object.

**Q5. What happens when a file is opened with mode "w"?**  
A. Existing content is normally replaced  
B. Content is always appended  
C. File is read only  
D. File is renamed  
**Correct: A.** Write mode truncates an existing file or creates a new one.

## 16. Interview preparation

### Q1. What is the difference between CSV and JSON?
**Answer:** CSV is a simple tabular format with rows and fields, often used for spreadsheet exchange. JSON supports nested objects and arrays and is widely used for APIs and structured configuration. Choose based on the shape of the data and the consuming system.

**Follow-up:** Which format would you choose for nested employee profile data and why?

### Q2. Why use a context manager when opening files?
**Answer:** The with statement ensures the file is closed after the block, including when an error occurs. This helps manage file resources safely and keeps code shorter than manually opening and closing files.

**Follow-up:** What problem can happen if a file remains open?

## 17. Completion checklist
- [ ] Read and write a text file.
- [ ] Explain read, write and append modes.
- [ ] Create and read CSV records.
- [ ] Create and read JSON data.
- [ ] Complete File-Based User Management System.
- [ ] Verify persistence across separate runs.

**Next lesson:** Day 12 — Exception handling, debugging and basic logging.
