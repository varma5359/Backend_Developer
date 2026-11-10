# Day 11: Interview Questions — File Handling: Reading, Writing and Working with CSV and JSON

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is file handling?
**Answer:**
- Reading information from files.
- Writing or appending information.
- Saving application output between program runs.
- Exchanging data using formats such as CSV and JSON.

**Follow-up:** When would a database be more appropriate than a local file?

### Q2. Compare file modes r, w, a and x.
**Answer:**
- r: read an existing file.
- w: write and replace existing content.
- a: append at the end.
- x: create a new file and fail if it already exists.

**Follow-up:** Which mode is safest when you must not overwrite an existing file?

### Q3. Why use with open()?
**Answer:**
- It uses a context manager.
- The file is closed automatically after the block.
- Cleanup still happens when an exception occurs.
- It reduces resource-management mistakes.

**Follow-up:** What is the purpose of the encoding parameter?

### Q4. What is the difference between json.load() and json.dump()?
**Answer:**
- json.load() parses JSON from a file object.
- json.dump() writes Python data as JSON into a file object.
- json.loads() parses a JSON string.
- json.dumps() creates a JSON string from Python data.

**Follow-up:** What Python type represents a JSON array after parsing?

### Q5. How do you read CSV data in Python?
**Answer:**
- Import the csv module.
- Open the file using an appropriate mode and encoding.
- Use csv.reader or csv.DictReader.
- Iterate through rows and process fields.
- Convert values when numeric types are needed.

**Follow-up:** Why use DictReader instead of reader?

## 2. Scenario-based questions

### Q6. Your records disappear after each program run. What might be wrong?
**Answer:**
- The program may store data only in memory.
- It may not save records to a file.
- It may write to a different relative path than expected.
- Check the save operation and current working directory.
- Confirm the file contains the expected records after the program exits.

**Follow-up:** How would you confirm which directory Python is using?

### Q7. A JSON file contains invalid syntax and json.load fails. What do you do?
**Answer:**
- Inspect the file content.
- Check commas, quotes, brackets and valid JSON values.
- Handle the parsing error safely.
- Preserve the original file for investigation.
- Do not silently replace user records with an empty collection.

**Follow-up:** What exception is commonly raised for invalid JSON?

### Q8. CSV numeric fields are strings. Is that unexpected?
**Answer:**
- No; CSV is a text-based format.
- Values commonly arrive as strings.
- Convert the fields to int or float after validation.
- Handle blank or malformed values deliberately.

**Follow-up:** What could happen if malformed numeric text is converted directly with int()?

## 3. Project questions

### Q9. Explain File-Based User Management System.
**Answer:**
- I represented each user as a dictionary.
- I stored multiple records in a list.
- I loaded and saved the records using JSON.
- I exported the records using CSV.
- I tested persistence by running the program more than once.

**Follow-up:** What are the limitations of a JSON file for concurrent users?

### Q10. How do you reduce accidental data loss when writing files?
**Answer:**
- Understand whether write or append mode is required.
- Validate data before replacing a file.
- Preserve backups or use a temporary file and controlled replacement where appropriate.
- Handle errors and verify the saved output.
- Use a database for multi-user transactional workflows.

**Follow-up:** Why is append mode not always the correct way to update a JSON file?

## 4. Rapid revision
- open(): opens a file.
- with: manages the file resource.
- r: read.
- w: write/replace.
- a: append.
- csv.DictReader: reads named columns as dictionaries.
- json.load: read JSON file.
- json.dump: write JSON file.
- pathlib: path handling.
