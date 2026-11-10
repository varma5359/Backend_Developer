# Day 20: Git, GitHub, repositories, commits, branches and merge basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations (Days 1–12), Day 19  
**Tools:** Python 3, VS Code, terminal, Git  
**Approved mini-project:** Version-Controlled Python Project

## 1. Learning objectives
1. Define the central terms of git, github, repositories, commits, branches and merge basics.
2. Explain how this concept supports backend applications.
3. Run and interpret a working example.
4. Diagnose a common mistake or failure.
5. Apply the concept in **Version-Controlled Python Project**.

## 2. Concept and motivation
Git tracks file history locally. GitHub hosts repositories and collaboration. Commits record snapshots; branches allow parallel work; merges combine histories.

**Why it matters:** Backend developers must reason about communication, data, and reproducible software changes. A correct implementation should produce observable evidence rather than rely on assumptions.

**Key vocabulary:** `repository`, `working tree`, `staging area`, `commit`, `branch`, `merge`, `remote`, `push`.

## 3. How it works
Input or request → validation/processing → result → inspection and verification.

**Use it when:** You need the relevant behavior in a web or data workflow. **Avoid:** Treating a successful example as proof that production concerns (authentication, error handling, scalability or concurrent use) are solved.

## 4. Step-by-step practical demonstration
Create a new folder named `day_20` in VS Code. Save this example in `commands.txt`.

Run these commands one at a time in a terminal, not as Python:

```bash
git --version
git init
git status
git add .
git commit -m "Add initial Python billing script"
git switch -c feature/readme
git status
git switch main
git merge feature/readme
```

**How to run:** Run each command in a new test project; configure git user.name and user.email first; default branch may be master, so use git branch -M main after the initial commit if needed.

**Expected result:**
```text
Repository initialized; a commit is created; a feature branch is created and can be merged after changes.
```

**Code walkthrough:**
- git init creates the local repository metadata.\n- git add stages changes; git commit records them.\n- git switch creates or changes branches; git merge integrates history.\n- Always check git status before committing or merging.

## 5. Industry scenario
Two developers improve a billing application without overwriting each other's changes. The developer should define the expected result, check failures, and communicate the outcome clearly to other team members.

## 6. Common mistakes and troubleshooting
| Problem | Check |
|---|---|
| Command or script fails | Verify interpreter/tool installation and current folder |
| Output differs | Inspect inputs, spelling, syntax and assumptions |
| Operation succeeds unexpectedly | Verify status, affected rows or actual saved state |
| Invalid or untrusted input | Validate before processing; never trust client data |
| Security concern | Use HTTPS for remote communication, parameterized SQL, and no secrets in source control |

## 7. Independent mini-project — Version-Controlled Python Project

**Goal:** Demonstrate git, github, repositories, commits, branches and merge basics with a small, testable application or workflow. **Estimated project time:** 30–75 minutes.

**Required deliverables:**
1. Write a short problem statement and input/output specification.
2. Create the project in `projects/day_20/`.
3. Implement the day's main concept using the demonstration as a reference, not a copied full project.
4. Include at least three realistic sample inputs or actions.
5. Capture terminal/browser/database evidence.
6. Write a short README with setup, run commands and limitations.

**Suggested structure:**
```text
projects/day_20/
├── README.md
├── main.py
└── evidence/
```

**Validation checklist:**
1. Create a repo and commit a Python file.
2. Create a feature branch and make a distinct commit.
3. Merge it into main.
4. Verify git log and git status.

**Security and reliability:** Do not commit credentials, personal information or production secrets. Use local test data and handle errors explicitly.

**Optional extension:** Add one additional edge case and document how the implementation responds.

**Submission:** Source code or command transcript, README, sample outputs, test results and a short explanation of the result.

## 8. AI-assisted learning guide
| Level | Ask the AI mentor |
|---|---|
| Hint | Give one hint for Version-Controlled Python Project; don't solve it |
| Plan | Break the project into input, process, output and tests |
| Example | Explain a tiny example of repository |
| Guided implementation | Help me implement only the first step, then wait |
| Explanation | Explain the demonstration line by line |
| Debugging | Analyze my exact error message and propose a minimal fix |
| Review | Check my implementation against the validation checklist |

**Planning prompt:** "Help me plan Version-Controlled Python Project with requirements, sample inputs and test cases. Do not write the complete solution."

**Implementation prompt:** "Guide me through one step at a time. Explain each command or line before continuing."

**Debugging/review prompt:** "Review my output, identify the root cause of any failure and explain how to verify the correction."

## 9. Daily MCQs
**Q1. Which statement best describes repository?**  
A. Git tracks file history locally.  
B. It is only a Python variable  
C. It always requires Django  
D. It replaces all validation  
**Answer: A.** Git tracks file history locally. — this is the appropriate choice for the stated scenario.

**Q2. What is the most useful evidence that Version-Controlled Python Project works?**  
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
### Q1. What is the difference between Git and GitHub?
**Answer:** Git is a distributed version-control system; GitHub is a platform that hosts Git repositories and collaboration features.

**Practical example:** Two developers improve a billing application without overwriting each other's changes.

**Follow-up:** How would you verify this behavior in a real backend application?

### Q2. What is a merge conflict?
**Answer:** A conflict arises when Git cannot automatically reconcile competing changes; a developer must inspect and resolve them.

**Practical example:** Two developers improve a billing application without overwriting each other's changes.

**Follow-up:** How would you verify this behavior in a real backend application?

## 11. Completion checklist
- [ ] Explain the core terminology without notes.
- [ ] Run the demonstration and verify output.
- [ ] Explain important statements or commands.
- [ ] Complete Version-Controlled Python Project.
- [ ] Validate at least three cases.
- [ ] Answer five MCQs and two interview questions.
- [ ] Submit source, README and evidence.

## 12. Phase 2 cumulative assessment — Web-Connected Employee Database Workflow

**Scenario:** A small HR department needs an employee data service concept demonstration. Combine web request/response knowledge, JSON payloads, a relational employee database, SQL queries and Git version control.

**Requirements:** Design employee and department tables with primary/foreign keys; create, query, update and delete sample employee records; produce JSON representations of selected records; document GET/POST/PUT/PATCH/DELETE semantics and appropriate status codes; commit work on a feature branch and merge it safely. A local simulation is sufficient—Django is introduced in Phase 3.

**Evidence:** Schema, SQL script, sample JSON, HTTP request/response examples, terminal output, Git history and README.

**Validation:** Duplicate primary key rejected; invalid foreign key rejected when enforcement is enabled; UPDATE/DELETE restricted with WHERE; JSON parses successfully; Git working tree clean after merge.

**Rubric:** Concepts 20%, correctness 30%, reasoning 20%, code quality 15%, testing 10%, communication 5% = **100%**.

**Phase interview questions:** (1) Trace browser-to-server communication. (2) Explain HTTP methods and status codes. (3) Compare JSON and XML. (4) Explain primary/foreign keys. (5) Explain JOIN and GROUP BY. (6) Explain Git branch versus commit.

**Common mistakes:** Confusing 401 and 403, using unparameterized SQL, omitting WHERE, assuming JSON validates itself, committing credentials, and claiming an HTTP simulation is a deployed API.

**Phase 2 complete. Next: Phase 3 — Django Fundamentals (Days 21–35).**
