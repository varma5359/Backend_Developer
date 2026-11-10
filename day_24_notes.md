# Day 24: SQL fundamentals: CREATE, INSERT, SELECT, UPDATE and DELETE

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations (Days 1–12), Day 17  
**Tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Employee Database Manager

## 1. Learning objectives
1. Define the central terms of sql fundamentals: create, insert, select, update and delete.
2. Explain how this concept supports backend applications.
3. Run and interpret a working example.
4. Diagnose a common mistake or failure.
5. Apply the concept in **Employee Database Manager**.

## 2. Concept and motivation
SQL defines and manipulates relational data. CREATE makes tables; INSERT adds rows; SELECT retrieves; UPDATE modifies; DELETE removes. WHERE restricts changes to selected rows.

**Why it matters:** Backend developers must reason about communication, data, and reproducible software changes. A correct implementation should produce observable evidence rather than rely on assumptions.

**Key vocabulary:** `DDL`, `DML`, `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`.

## 3. How it works
Input or request → validation/processing → result → inspection and verification.

**Use it when:** You need the relevant behavior in a web or data workflow. **Avoid:** Treating a successful example as proof that production concerns (authentication, error handling, scalability or concurrent use) are solved.

## 4. Step-by-step practical demonstration
Create a new folder named `day_24` in VS Code. Save this example in `demo.py`.

Run the code below in Python:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")
db.execute("INSERT INTO employees VALUES (?, ?, ?)", (101, "Asha", 45000))
db.execute("INSERT INTO employees VALUES (?, ?, ?)", (102, "Ravi", 50000))
db.execute("UPDATE employees SET salary = ? WHERE id = ?", (47000, 101))
print(db.execute("SELECT id, name, salary FROM employees ORDER BY id").fetchall())
db.execute("DELETE FROM employees WHERE id = ?", (102,))
db.commit()
print("Remaining:", db.execute("SELECT COUNT(*) FROM employees").fetchone()[0])
db.close()
```

**How to run:** python employees.py

**Expected result:**
```text
[(101, 'Asha', 47000), (102, 'Ravi', 50000)]\nRemaining: 1
```

**Code walkthrough:**
- sqlite3.connect opens a local SQLite database (memory-only for this demonstration).\n- SQL statements define tables, change records or query results.\n- execute runs a statement; fetchall/fetchone retrieves query results.\n- Parameter placeholders (?) safely bind values where shown.\n- PostgreSQL is the pathway's production database; SQLite is used here for zero-install practice.

## 5. Industry scenario
An HR team maintains employee records and needs safe updates. The developer should define the expected result, check failures, and communicate the outcome clearly to other team members.

## 6. Common mistakes and troubleshooting
| Problem | Check |
|---|---|
| Command or script fails | Verify interpreter/tool installation and current folder |
| Output differs | Inspect inputs, spelling, syntax and assumptions |
| Operation succeeds unexpectedly | Verify status, affected rows or actual saved state |
| Invalid or untrusted input | Validate before processing; never trust client data |
| Security concern | Use HTTPS for remote communication, parameterized SQL, and no secrets in source control |

## 7. Independent mini-project — Employee Database Manager

**Goal:** Demonstrate sql fundamentals: create, insert, select, update and delete with a small, testable application or workflow. **Estimated project time:** 30–75 minutes.

**Required deliverables:**
1. Write a short problem statement and input/output specification.
2. Create the project in `projects/day_24/`.
3. Implement the day's main concept using the demonstration as a reference, not a copied full project.
4. Include at least three realistic sample inputs or actions.
5. Capture terminal/browser/database evidence.
6. Write a short README with setup, run commands and limitations.

**Suggested structure:**
```text
projects/day_24/
├── README.md
├── main.py
└── evidence/
```

**Validation checklist:**
1. Insert two employees.
2. Update one employee using WHERE.
3. Delete only the specified ID.
4. Use parameter placeholders rather than string interpolation.

**Security and reliability:** Do not commit credentials, personal information or production secrets. Use local test data and handle errors explicitly.

**Optional extension:** Add one additional edge case and document how the implementation responds.

**Submission:** Source code or command transcript, README, sample outputs, test results and a short explanation of the result.

## 8. AI-assisted learning guide
| Level | Ask the AI mentor |
|---|---|
| Hint | Give one hint for Employee Database Manager; don't solve it |
| Plan | Break the project into input, process, output and tests |
| Example | Explain a tiny example of DDL |
| Guided implementation | Help me implement only the first step, then wait |
| Explanation | Explain the demonstration line by line |
| Debugging | Analyze my exact error message and propose a minimal fix |
| Review | Check my implementation against the validation checklist |

**Planning prompt:** "Help me plan Employee Database Manager with requirements, sample inputs and test cases. Do not write the complete solution."

**Implementation prompt:** "Guide me through one step at a time. Explain each command or line before continuing."

**Debugging/review prompt:** "Review my output, identify the root cause of any failure and explain how to verify the correction."

## 9. Daily MCQs
**Q1. Which statement best describes DDL?**  
A. SQL defines and manipulates relational data.  
B. It is only a Python variable  
C. It always requires Django  
D. It replaces all validation  
**Answer: A.** SQL defines and manipulates relational data. — this is the appropriate choice for the stated scenario.

**Q2. What is the most useful evidence that Employee Database Manager works?**  
A. A project name  
B. Observed output matching documented test cases  
C. A screenshot of the editor alone  
D. A file with no executable code  
**Answer: B.** Observed output matching documented test cases — this is the appropriate choice for the stated scenario.

**Q3. What should you do when the demonstration produces unexpected output?**  
A. Ignore it  
B. Copy another project  
C. Inspect inputs, errors and assumptions  
D. Delete the repository  
**Answer: C.** Inspect inputs, errors and assumptions — this is the appropriate choice for the stated scenario.

**Q4. Which practice is safest for backend development?**  
A. Trust all client input  
B. Store secrets in Git  
C. Skip validation  
D. Validate input and avoid exposing secrets  
**Answer: D.** Validate input and avoid exposing secrets — this is the appropriate choice for the stated scenario.

**Q5. What should the project README contain?**  
A. Setup, execution and validation instructions  
B. Only the student's name  
C. Only a picture  
D. No technical details  
**Answer: A.** Setup, execution and validation instructions — this is the appropriate choice for the stated scenario.

## 10. Interview practice
### Q1. Why is WHERE important in UPDATE and DELETE?
**Answer:** Without WHERE, these statements can affect every row in the table.

**Practical example:** An HR team maintains employee records and needs safe updates.

**Follow-up:** How would you verify this behavior in a real backend application?

### Q2. How can SQL injection be prevented?
**Answer:** Use parameterized queries for values, validate inputs and follow least-privilege database access.

**Practical example:** An HR team maintains employee records and needs safe updates.

**Follow-up:** How would you verify this behavior in a real backend application?

## 11. Completion checklist
- [ ] Explain the core terminology without notes.
- [ ] Run the demonstration and verify output.
- [ ] Explain important statements or commands.
- [ ] Complete Employee Database Manager.
- [ ] Validate at least three cases.
- [ ] Answer five MCQs and two interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 19.
