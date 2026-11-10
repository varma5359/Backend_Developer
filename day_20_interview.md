# Day 20: Interview Questions — Git, GitHub, repositories, commits, branches and merge basics

**Pathway:** Python Backend Developer (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools

## 1. Core technical questions

### Q1. What is the difference between Git and GitHub?
**Answer:**
- Git is a distributed version-control system; GitHub is a platform that hosts Git repositories and collaboration features.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** Two developers improve a billing application without overwriting each other's changes.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q2. What is a merge conflict?
**Answer:**
- A conflict arises when Git cannot automatically reconcile competing changes; a developer must inspect and resolve them.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** Two developers improve a billing application without overwriting each other's changes.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q3. What is the main purpose of repository?
**Answer:** Git tracks file history locally. GitHub hosts repositories and collaboration. Commits record snapshots; branches allow parallel work; merges combine histories.

**Follow-up:** What would go wrong if the concept were misunderstood?

### Q4. Which tools are appropriate for this lesson?
**Answer:** Python and VS Code for demonstrations, terminal commands for execution, and Git/GitHub for repository operations.

**Follow-up:** What would change in a deployed Django service?

### Q5. How do you verify the implementation?
**Answer:** Define expected inputs and outputs, run normal and edge cases, inspect actual responses or database state, and document failures.

**Follow-up:** Why is a successful command not always proof of correct business behavior?

## 2. Scenario-based interview questions

### Q6. Two developers improve a billing application without overwriting each other's changes. What should the developer verify?
**Answer:**
- Define the expected result before implementation.
- Check that the chosen repository behavior matches the requirement.
- Validate inputs and inspect actual results.
- Record reproducible test evidence.

**Follow-up:** What error case would you test first?

### Q7. A beginner's output differs from the expected result. How do you troubleshoot?
**Answer:**
- Reproduce the issue with the smallest sample.
- Check tool installation, file location and input.
- Inspect exceptions, response status or SQL result.
- Change one variable at a time and rerun.
- Document the fix and regression test.

**Follow-up:** How would you explain the root cause to a non-technical colleague?

## 3. Project and practical questions

### Q8. Explain your Version-Controlled Python Project.
**Answer:**
- I defined the inputs, operations and expected outputs.
- I implemented a small demonstration of git, github, repositories, commits, branches and merge basics.
- I tested normal and edge cases.
- I captured evidence and documented limitations.
- I did not assume a learning exercise was production-ready.

**Follow-up:** Which part would you improve first for production use?

### Q9. What mistakes should you avoid in this project?
**Answer:**
- Skipping validation.
- Failing to verify observable results.
- Mixing unrelated responsibilities.
- Hardcoding secrets or private data.
- Ignoring error cases.

**Follow-up:** What is one automated test you would add?

## 4. Rapid revision
- **repository:** explain its role in git, github, repositories, commits, branches and merge basics.
- **working tree:** explain its role in git, github, repositories, commits, branches and merge basics.
- **staging area:** explain its role in git, github, repositories, commits, branches and merge basics.
- **commit:** explain its role in git, github, repositories, commits, branches and merge basics.
- **branch:** explain its role in git, github, repositories, commits, branches and merge basics.
- **merge:** explain its role in git, github, repositories, commits, branches and merge basics.
- **remote:** explain its role in git, github, repositories, commits, branches and merge basics.
- **push:** explain its role in git, github, repositories, commits, branches and merge basics.

**Interview preparation tip:** Give a definition, show a small practical example, explain a failure mode, and state how you would verify it.
