# Day 23: Relational database concepts, tables, primary keys and foreign keys

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations (Days 1–12), Day 16  
**Tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Student Database Designer

## 1. Learning objectives
1. Define the central terms of relational database concepts, tables, primary keys and foreign keys.
2. Explain how this concept supports backend applications.
3. Run and interpret a working example.
4. Diagnose a common mistake or failure.
5. Apply the concept in **Student Database Designer**.

## 2. Concept and motivation
Relational databases organize rows in tables. Primary keys uniquely identify rows. Foreign keys reference related records and help maintain referential integrity.

**Why it matters:** Backend developers must reason about communication, data, and reproducible software changes. A correct implementation should produce observable evidence rather than rely on assumptions.

**Key vocabulary:** `table`, `row`, `column`, `primary key`, `foreign key`, `one-to-many`, `many-to-many`.

## 3. How it works
Input or request → validation/processing → result → inspection and verification.

**Use it when:** You need the relevant behavior in a web or data workflow. **Avoid:** Treating a successful example as proof that production concerns (authentication, error handling, scalability or concurrent use) are solved.

## 4. Step-by-step practical demonstration
Create a new folder named `day_23` in VS Code. Save this example in `demo.py`.

Run the code below in Python:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
db.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, title TEXT NOT NULL)")
db.execute("""CREATE TABLE enrollments (
 student_id INTEGER REFERENCES students(id),
 course_id INTEGER REFERENCES courses(id),
 PRIMARY KEY(student_id, course_id)
)""")
print("Three related tables created")
db.close()
```

**How to run:** python design.py

**Expected result:**
```text
Three related tables created
```

**Code walkthrough:**
- sqlite3.connect opens a local SQLite database (memory-only for this demonstration).\n- SQL statements define tables, change records or query results.\n- execute runs a statement; fetchall/fetchone retrieves query results.\n- Parameter placeholders (?) safely bind values where shown.\n- PostgreSQL is the pathway's production database; SQLite is used here for zero-install practice.

## 5. Industry scenario
A college needs students, courses and enrollments without duplicating course data for every student. The developer should define the expected result, check failures, and communicate the outcome clearly to other team members.

## 6. Common mistakes and troubleshooting
| Problem | Check |
|---|---|
| Command or script fails | Verify interpreter/tool installation and current folder |
| Output differs | Inspect inputs, spelling, syntax and assumptions |
| Operation succeeds unexpectedly | Verify status, affected rows or actual saved state |
| Invalid or untrusted input | Validate before processing; never trust client data |
| Security concern | Use HTTPS for remote communication, parameterized SQL, and no secrets in source control |

## 7. Independent mini-project — Student Database Designer

**Goal:** Demonstrate relational database concepts, tables, primary keys and foreign keys with a small, testable application or workflow. **Estimated project time:** 30–75 minutes.

**Required deliverables:**
1. Write a short problem statement and input/output specification.
2. Create the project in `projects/day_23/`.
3. Implement the day's main concept using the demonstration as a reference, not a copied full project.
4. Include at least three realistic sample inputs or actions.
5. Capture terminal/browser/database evidence.
6. Write a short README with setup, run commands and limitations.

**Suggested structure:**
```text
projects/day_23/
├── README.md
├── main.py
└── evidence/
```

**Validation checklist:**
1. Identify primary keys.
2. Explain the enrollment bridge table.
3. Attempt a foreign key violation with enforcement enabled.

**Security and reliability:** Do not commit credentials, personal information or production secrets. Use local test data and handle errors explicitly.

**Optional extension:** Add one additional edge case and document how the implementation responds.

**Submission:** Source code or command transcript, README, sample outputs, test results and a short explanation of the result.

## 8. AI-assisted learning guide
| Level | Ask the AI mentor |
|---|---|
| Hint | Give one hint for Student Database Designer; don't solve it |
| Plan | Break the project into input, process, output and tests |
| Example | Explain a tiny example of table |
| Guided implementation | Help me implement only the first step, then wait |
| Explanation | Explain the demonstration line by line |
| Debugging | Analyze my exact error message and propose a minimal fix |
| Review | Check my implementation against the validation checklist |

**Planning prompt:** "Help me plan Student Database Designer with requirements, sample inputs and test cases. Do not write the complete solution."

**Implementation prompt:** "Guide me through one step at a time. Explain each command or line before continuing."

**Debugging/review prompt:** "Review my output, identify the root cause of any failure and explain how to verify the correction."

## 9. Daily MCQs
**Q1. Which statement best describes table?**  
A. Relational databases organize rows in tables.  
B. It is only a Python variable  
C. It always requires Django  
D. It replaces all validation  
**Answer: A.** Relational databases organize rows in tables. — this is the appropriate choice for the stated scenario.

**Q2. What is the most useful evidence that Student Database Designer works?**  
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
### Q1. What is a primary key?
**Answer:** A column or combination of columns that uniquely identifies a table row and cannot be null.

**Practical example:** A college needs students, courses and enrollments without duplicating course data for every student.

**Follow-up:** How would you verify this behavior in a real backend application?

### Q2. Why use a foreign key?
**Answer:** It expresses a relationship to another table and can enforce referential integrity.

**Practical example:** A college needs students, courses and enrollments without duplicating course data for every student.

**Follow-up:** How would you verify this behavior in a real backend application?

## 11. Completion checklist
- [ ] Explain the core terminology without notes.
- [ ] Run the demonstration and verify output.
- [ ] Explain important statements or commands.
- [ ] Complete Student Database Designer.
- [ ] Validate at least three cases.
- [ ] Answer five MCQs and two interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 18.
