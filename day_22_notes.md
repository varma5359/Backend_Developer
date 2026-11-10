# Day 22: JSON, XML Basics and Data Exchange Between Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 19–21 — Client-server, HTTP and response structure  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** JSON Data Exchange Tool

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why applications exchange structured data.
2. Understand JSON objects, arrays, strings, numbers, booleans and null.
3. Convert Python dictionaries and lists to JSON.
4. Parse JSON text into Python objects.
5. Read and write JSON files.
6. Understand the basic XML element, attribute and nesting structure.
7. Parse simple XML using Python's standard library.
8. Compare JSON and XML.
9. Build a JSON Data Exchange Tool.

## 2. Why do applications need data formats?

Imagine a frontend sends a new employee to a Python backend.

The information may contain:
- Employee ID.
- Name.
- Department.
- Active status.

The frontend and backend need an agreed format to represent this information.

JSON and XML are structured data formats used for data exchange.

They are not programming languages and they do not execute business logic by themselves.

## 3. What is JSON?

JSON stands for JavaScript Object Notation.

It is a text-based data format commonly used by web APIs.

Example:

```json
{
  "employee_id": 101,
  "name": "Anil",
  "department": "IT",
  "is_active": true
}
```

This represents one employee as a JSON object.

JSON is widely used because it is readable and supported by many programming languages.

## 4. JSON data types

JSON supports:
- Object.
- Array.
- String.
- Number.
- Boolean.
- Null.

| JSON type | Example |
|---|---|
| Object | `{"name": "Asha"}` |
| Array | `["Python", "Django"]` |
| String | `"Anil"` |
| Number | `45000` |
| Boolean | `true` |
| Null | `null` |

JSON uses lowercase `true`, `false` and `null`. Python uses `True`, `False` and `None`.

## 5. JSON object

A JSON object contains key-value pairs.

```json
{
  "name": "Asha",
  "course": "Backend Development",
  "duration_months": 3
}
```

Rules:
- Keys are strings in double quotes.
- A colon separates a key and value.
- A comma separates pairs.
- The last pair must not have a trailing comma in standard JSON.

## 6. JSON array

An array stores an ordered sequence of values.

```json
[
  "Python",
  "Django",
  "SQL"
]
```

An array can also contain objects:

```json
[
  {"id": 101, "name": "Asha"},
  {"id": 102, "name": "Ravi"}
]
```

This is a common API response shape for a collection of employees or products.

## 7. Python dictionary versus JSON object

They look similar, but they are not the same type.

Python dictionary:

```python
employee = {
    "employee_id": 101,
    "name": "Anil",
    "is_active": True,
    "manager": None
}
```

Equivalent JSON text:

```json
{
  "employee_id": 101,
  "name": "Anil",
  "is_active": true,
  "manager": null
}
```

Differences:
- Python uses True, False and None.
- JSON uses true, false and null.
- JSON object keys must be strings.
- JSON is text; a Python dictionary is an in-memory Python object.

## 8. Python json module

Python provides a standard-library module named `json`.

Import it:

```python
import json
```

Two important functions:
- `json.dumps()`: Python object to JSON string.
- `json.loads()`: JSON string to Python object.

For files:
- `json.dump()`: write Python data as JSON to a file.
- `json.load()`: read JSON from a file into Python data.

## 9. Convert Python dictionary to JSON string

```python
import json

employee = {
    "employee_id": 101,
    "name": "Anil",
    "department": "IT",
    "is_active": True
}

json_text = json.dumps(employee)

print(json_text)
print(type(json_text))
```

Expected output:

```text
{"employee_id": 101, "name": "Anil", "department": "IT", "is_active": true}
<class 'str'>
```

Explanation:
1. employee is a Python dictionary.
2. dumps converts it to JSON-formatted text.
3. json_text is a Python string.
4. Python's True becomes JSON true.

### 9.1 Pretty-print JSON

```python
print(json.dumps(employee, indent=4))
```

Output:

```json
{
    "employee_id": 101,
    "name": "Anil",
    "department": "IT",
    "is_active": true
}
```

Indentation makes the JSON easier for humans to read. It does not change the underlying data.

## 10. Convert JSON string to Python dictionary

```python
import json

json_text = '{"employee_id": 101, "name": "Anil", "is_active": true}'

employee = json.loads(json_text)

print(employee)
print(type(employee))
print(employee["name"])
print(employee["is_active"])
```

Output:

```text
{'employee_id': 101, 'name': 'Anil', 'is_active': True}
<class 'dict'>
Anil
True
```

The JSON true becomes Python True.

## 11. JSON arrays and Python lists

```python
import json

courses = ["Python", "Django", "SQL"]

json_text = json.dumps(courses)
print(json_text)

python_list = json.loads(json_text)
print(python_list)
print(type(python_list))
```

Output:

```text
["Python", "Django", "SQL"]
['Python', 'Django', 'SQL']
<class 'list'>
```

A JSON array becomes a Python list.

## 12. Nested JSON

An object can contain another object or an array.

```python
import json

employee = {
    "employee_id": 101,
    "name": "Asha",
    "address": {
        "city": "Hyderabad",
        "state": "Telangana"
    },
    "skills": ["Python", "Django", "SQL"]
}

json_text = json.dumps(employee, indent=4)
print(json_text)
```

Access nested data in Python:

```python
print(employee["address"]["city"])
print(employee["skills"][0])
```

Output:

```text
Hyderabad
Python
```

Read from the outside inward:
- employee["address"] returns the nested dictionary.
- ["city"] selects its city value.
- employee["skills"] returns a list.
- [0] selects the first item.

## 13. Write JSON to a file

Create `employee.json` from Python:

```python
import json

employee = {
    "employee_id": 101,
    "name": "Asha",
    "department": "IT"
}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

print("JSON file created")
```

Expected terminal output:

`JSON file created`

Open employee.json in VS Code to inspect the saved content.

## 14. Read JSON from a file

```python
import json

with open("employee.json", "r", encoding="utf-8") as file:
    employee = json.load(file)

print(employee)
print("Employee:", employee["name"])
```

Expected output:

```text
{'employee_id': 101, 'name': 'Asha', 'department': 'IT'}
Employee: Asha
```

The difference:
- load reads from a file object.
- loads reads from a JSON string.
- dump writes to a file object.
- dumps returns a JSON string.

## 15. Handle invalid JSON

```python
import json

invalid_json = '{"name": "Asha", "department": }'

try:
    employee = json.loads(invalid_json)
except json.JSONDecodeError as error:
    print("Invalid JSON:", error)
```

JSONDecodeError occurs when the text is not valid JSON.

Common causes:
- Missing double quotes around keys.
- Missing value after a colon.
- Trailing comma.
- Single quotes used instead of double quotes.
- Missing closing brace or bracket.

## 16. What is XML?

XML stands for Extensible Markup Language.

It is a text-based markup format used to represent structured data.

Example:

```xml
<employee>
    <employee_id>101</employee_id>
    <name>Anil</name>
    <department>IT</department>
</employee>
```

XML uses tags to describe elements and values.

## 17. XML structure

Important terms:

| Term | Meaning |
|---|---|
| Element | A start tag, content and end tag |
| Root element | The single top-level element |
| Child element | Element nested inside another element |
| Attribute | Name-value metadata inside a start tag |
| Text content | Text between tags |
| Well-formed XML | XML following basic syntax and nesting rules |

Example:

```xml
<employee id="101">
    <name>Asha</name>
    <department>IT</department>
</employee>
```

Here:
- employee is the root element.
- id is an attribute.
- name and department are child elements.
- Asha and IT are text content.

## 18. Parse XML using Python

Python's standard library provides ElementTree.

```python
import xml.etree.ElementTree as ET

xml_text = """
<employee id="101">
    <name>Asha</name>
    <department>IT</department>
</employee>
"""

root = ET.fromstring(xml_text)

print(root.tag)
print(root.attrib["id"])
print(root.find("name").text)
print(root.find("department").text)
```

Output:

```text
employee
101
Asha
IT
```

Explanation:
- fromstring parses XML text.
- root represents the root element.
- root.tag returns the element name.
- root.attrib returns its attributes.
- find locates a child element.
- text reads the child element's text content.

## 19. Create XML using ElementTree

```python
import xml.etree.ElementTree as ET

root = ET.Element("employee", attrib={"id": "101"})

name = ET.SubElement(root, "name")
name.text = "Asha"

department = ET.SubElement(root, "department")
department.text = "IT"

xml_output = ET.tostring(root, encoding="unicode")
print(xml_output)
```

Output:

```xml
<employee id="101"><name>Asha</name><department>IT</department></employee>
```

The output is compact XML. Pretty printing is a separate formatting step.

## 20. JSON versus XML

| Feature | JSON | XML |
|---|---|---|
| Structure | Objects and arrays | Elements and attributes |
| Syntax | Key-value notation | Tags |
| Common use | Web APIs and application data | Document formats and some integrations |
| Data types | String, number, boolean, null, object, array | Text with schema/type conventions |
| Readability | Compact and familiar to API developers | More verbose but descriptive |
| Python support | json module | xml.etree.ElementTree |

Neither format is automatically more secure. Validate untrusted input and use safe parsers and sensible limits.

## 21. Send JSON through HTTP

JSON is commonly used as an HTTP request or response body.

```python
import json
from urllib.request import Request, urlopen

payload = {
    "name": "Asha",
    "course": "Django"
}

body = json.dumps(payload).encode("utf-8")

request = Request(
    "https://httpbin.org/post",
    data=body,
    method="POST",
    headers={"Content-Type": "application/json"}
)

with urlopen(request, timeout=10) as response:
    response_data = json.loads(response.read().decode("utf-8"))

print(response_data["json"])
```

The test endpoint echoes the JSON body it receives. This example needs internet access.

## 22. Mini-project — JSON Data Exchange Tool

### Requirements

Create a command-line program that:
1. Stores multiple employee records in a Python list.
2. Converts the list into formatted JSON.
3. Saves it to employees.json.
4. Reads employees.json.
5. Prints employee names and departments.
6. Handles invalid JSON.
7. Converts one simple XML employee record into a Python dictionary or displays its fields.

### Suggested structure

```text
projects/day_22_json_data_exchange/
├── main.py
├── employees.json
└── README.md
```

### Starter implementation

```python
import json


employees = [
    {"id": 101, "name": "Asha", "department": "IT"},
    {"id": 102, "name": "Ravi", "department": "HR"},
    {"id": 103, "name": "Meera", "department": "Finance"},
]

with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

with open("employees.json", "r", encoding="utf-8") as file:
    loaded_employees = json.load(file)

for employee in loaded_employees:
    print(employee["name"], "-", employee["department"])
```

Expected output:

```text
Asha - IT
Ravi - HR
Meera - Finance
```

### Validation tests

| Test | Action | Expected |
|---|---|---|
| 1 | Save employee list | employees.json created |
| 2 | Read file | Python list returned |
| 3 | Access employee name | Correct name displayed |
| 4 | Add nested address | Nested JSON saved |
| 5 | Break JSON syntax | JSONDecodeError handled |
| 6 | Parse XML string | Root and child values displayed |

## 23. Common mistakes

| Mistake | Why it fails | Correction |
|---|---|---|
| Using Python True in raw JSON text | JSON expects lowercase true | Use true in JSON strings |
| Using single quotes in JSON | JSON strings use double quotes | Use double quotes |
| Using loads for a file object | loads expects a string | Use load for file objects |
| Using load for a string | load expects a file-like object | Use loads |
| Assuming JSON is a Python dict | JSON is text until parsed | Call json.loads |
| Missing XML closing tag | XML nesting is malformed | Close each element |
| Searching wrong XML child name | find returns None | Check tag spelling and existence |
| Trusting uploaded JSON | Input may be malformed or hostile | Validate and limit input |

## 24. Interview questions

**1. What is JSON?**  
A text-based data interchange format that represents structured values using objects, arrays, strings, numbers, booleans and null.

**2. What is the difference between JSON and a Python dictionary?**  
JSON is text; a Python dictionary is an in-memory Python object.

**3. What does json.dumps do?**  
Converts a Python object to a JSON string.

**4. What does json.loads do?**  
Parses a JSON string into a Python object.

**5. Difference between dump and dumps?**  
dump writes JSON to a file-like object; dumps returns JSON text.

**6. What is XML?**  
A markup language used to represent structured data with elements and attributes.

**7. What is an XML root element?**  
The single top-level element containing the document's other elements.

**8. Difference between JSON and XML?**  
JSON uses objects and arrays; XML uses nested elements and attributes.

**9. How does an API use JSON?**  
A client can send JSON in a request body and receive JSON in a response body.

**10. What exception is raised for invalid JSON text?**  
json.JSONDecodeError.

## 25. MCQs

**Q1. Which Python function converts a dictionary to JSON text?**  
A. json.dumps  
B. json.loads  
C. json.read  
D. json.parse_file  
**Answer: A.** dumps serializes a Python object into JSON text.

**Q2. Which JSON value represents Python None?**  
A. None  
B. null  
C. NULL  
D. empty  
**Answer: B.** JSON uses null.

**Q3. Which function reads JSON from a file object?**  
A. json.loads  
B. json.dump  
C. json.load  
D. json.dumps  
**Answer: C.** load reads from a file-like object.

**Q4. What is an XML root element?**  
A. The top-level element  
B. Any attribute  
C. A Python list  
D. The final closing tag only  
**Answer: A.** It contains the document's nested structure.

**Q5. Which Python module is used in this lesson to parse XML?**  
A. csv  
B. xml.etree.ElementTree  
C. pathlib  
D. sqlite3  
**Answer: B.** ElementTree parses and builds XML.

**Q6. What happens when JSON syntax is invalid?**  
A. JSONDecodeError may be raised  
B. Python silently fixes every error  
C. XML is generated  
D. The file is deleted  
**Answer: A.** Invalid JSON cannot be parsed successfully.

## 26. Completion checklist

- [ ] I can explain why applications exchange structured data.
- [ ] I can identify JSON data types.
- [ ] I can use dumps, loads, dump and load.
- [ ] I can read and write JSON files.
- [ ] I can parse a JSON array and nested object.
- [ ] I understand XML elements and attributes.
- [ ] I can parse XML using ElementTree.
- [ ] I can compare JSON and XML.
- [ ] I completed JSON Data Exchange Tool.
- [ ] I handled malformed input.

**Next lesson:** Day 23 — Relational Database Concepts, Tables, Primary Keys and Foreign Keys.
