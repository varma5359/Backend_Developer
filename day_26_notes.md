# Day 26: Git, GitHub, Repositories, Commits, Branches and Merge Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Estimated time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python fundamentals and Days 19–25  
**Tools:** Git, GitHub, VS Code and terminal  
**Approved mini-project:** Version-Controlled Python Project

## 1. Learning objectives

- Explain version control and why developers use it.
- Distinguish Git from GitHub.
- Initialize and inspect a repository.
- Understand working tree, staging area and commits.
- Create and switch branches.
- Merge a feature branch.
- Resolve a simple merge conflict safely.
- Push a local repository to GitHub.
- Avoid committing secrets.

## 2. What is version control?

Version control records changes to files over time. It helps developers understand what changed, compare versions, restore earlier work and collaborate.

Without version control, developers often create folders such as final, final_new and final_latest. This becomes difficult to manage.

Git stores a history of snapshots called commits.

## 3. Git versus GitHub

| Git | GitHub |
|---|---|
| Version-control software | Online hosting and collaboration platform |
| Works locally | Hosts remote repositories |
| Tracks commits and branches | Supports pull requests, issues and reviews |
| Used through commands or GUI | Accessed through website and integrations |

Git can be used without GitHub. GitHub repositories use Git.

## 4. Install and verify Git

Install Git for your operating system. Open a terminal and run:

```bash
git --version
```

Expected result is a Git version string. The exact version may differ.

Configure your author identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use your intended Git identity. Do not use someone else's account details.

## 5. Initialize a repository

Create a folder named `version_controlled_project`. Open it in VS Code and run:

```bash
git init
git status
```

- git init creates the local repository metadata.
- git status shows changed and untracked files.
- The working tree is the folder where you edit files.

Create a file named `main.py`:

```python
print("Employee management application")
```

Run:

```bash
python main.py
git status
```

Git should show main.py as an untracked file.

## 6. Understand the three important areas

```text
Working directory
      ↓ git add
Staging area
      ↓ git commit
Local repository history
      ↓ git push
Remote repository (GitHub)
```

- Working directory: where you edit files.
- Staging area: selected changes prepared for the next commit.
- Local repository: committed history stored on your machine.
- Remote repository: a hosted copy, for example on GitHub.

## 7. Stage and commit changes

```bash
git add main.py
git status
git commit -m "Add employee application entry point"
git log --oneline
```

Explanation:
1. git add selects the file changes for the next commit.
2. git status confirms what is staged.
3. git commit records a snapshot with a message.
4. git log displays commit history.

A good commit message describes the change, for example "Add employee salary validation".

## 8. Create a branch

A branch lets you work on a change without directly changing the branch used for stable work.

```bash
git switch -c feature/employee-profile
git branch
```

- git switch -c creates and switches to a new branch.
- git branch lists local branches.
- The asterisk marks the current branch.

Older tutorials may use git checkout. git switch is a clear command for switching branches.

## 9. Make a change on the feature branch

Update main.py:

```python
def display_employee(name):
    print(f"Employee: {name}")

display_employee("Asha")
```

Run:

```bash
python main.py
git status
git add main.py
git commit -m "Add employee profile display"
git log --oneline
```

Now the feature branch has a commit that the main branch does not yet contain.

## 10. Merge the feature branch

First switch to the destination branch. The default branch may be main or master; inspect with git branch.

```bash
git switch main
git merge feature/employee-profile
git log --oneline --graph --all
```

The merge integrates the feature branch history into main. If the branches can be combined automatically, Git completes the merge.

If your repository's default branch is master, use that name instead of main.

## 11. Understand merge conflicts

A merge conflict occurs when Git cannot automatically combine competing changes, commonly because the same lines were edited differently.

Git marks the conflicting area in the file:

```text
<<<<<<< HEAD
print("Employee Portal")
=======
print("Employee Management Portal")
>>>>>>> feature/update-title
```

Resolution process:
1. Open the conflicted file.
2. Understand both versions.
3. Choose the intended final content or combine them.
4. Remove conflict markers.
5. Run the program or tests.
6. Stage the resolved file.
7. Complete the merge commit if Git requests it.

Never remove conflict markers without understanding which change should remain.

## 12. Connect a local repository to GitHub

Create an empty repository on GitHub. Copy its remote URL. Then run the commands with your actual repository URL:

```bash
git remote add origin https://github.com/your-user/your-repository.git
git remote -v
git branch -M main
git push -u origin main
```

- origin is a common name for the remote.
- git remote -v shows configured remote URLs.
- git branch -M main renames the current branch to main.
- git push sends commits to the remote.
- -u sets the upstream tracking relationship for later pushes.

Do not paste passwords or personal access tokens into source files. Use Git Credential Manager or the recommended authentication flow.

## 13. Pull and fetch

- git fetch downloads remote history and references without automatically merging into your current branch.
- git pull fetches and integrates changes according to the configured strategy.
- git status and git log help you inspect the current state.

Before pulling into important work, commit or safely back up local changes. Avoid using destructive reset commands unless you understand exactly which changes will be discarded.

## 14. Useful everyday commands

| Command | Purpose |
|---|---|
| git status | Inspect working tree and staging area |
| git add file.py | Stage one file |
| git add . | Stage changes under current directory; inspect status first |
| git commit -m "message" | Record staged changes |
| git log --oneline | Compact commit history |
| git diff | Inspect unstaged changes |
| git diff --staged | Inspect staged changes |
| git branch | List branches |
| git switch branch-name | Switch branches |
| git switch -c branch-name | Create and switch |
| git merge branch-name | Merge a branch into current branch |
| git remote -v | Inspect remotes |
| git push | Push commits |
| git pull | Fetch and integrate remote changes |

## 15. .gitignore and secrets

Create a `.gitignore` file to exclude generated or private files. Example:

```gitignore
__pycache__/
*.py[cod]
.venv/
.env
.vscode/
.pytest_cache/
```

Never commit:
- API keys.
- Database passwords.
- Django SECRET_KEY values.
- Private keys.
- Access tokens.
- Customer personal data.

If a secret is committed, deleting it in a later commit does not make the old secret safe. Rotate or revoke it.

## 16. Industry scenario

Two developers work on an employee management backend. One builds employee profiles while another improves salary validation. Feature branches allow separate changes, commits record progress and a merge brings reviewed work together.

## 17. Common mistakes

| Mistake | Better approach |
|---|---|
| Forgetting git status | Inspect status before staging and committing |
| Committing every file blindly | Review staged changes |
| Using vague commit messages | Describe the actual change |
| Editing main for every feature | Use focused feature branches |
| Ignoring merge conflicts | Resolve carefully and run tests |
| Committing .env | Add private configuration to .gitignore |
| Assuming push means tests passed | Run validation independently |
| Running destructive reset commands casually | Understand the target commit and backup important work |

## 18. Approved mini-project — Version-Controlled Python Project

Objective: Build a small Python employee utility and manage its history using Git.

Requirements:
1. Create a project folder and initialize Git.
2. Add a main.py file with a simple employee display function.
3. Make the first commit.
4. Create a feature branch.
5. Add a salary validation function.
6. Run the script and test valid and invalid values.
7. Commit the feature.
8. Switch to main and merge the feature branch.
9. Create a GitHub repository and push the project.
10. Add a README and .gitignore.
11. Verify git status and git log.
12. Confirm no secret files are committed.

Suggested structure:
```text
version_controlled_project/
├── .gitignore
├── README.md
└── main.py
```

Validation:
- [ ] Git repository initialized.
- [ ] At least two meaningful commits created.
- [ ] Feature branch created.
- [ ] Feature branch merged.
- [ ] Remote repository configured.
- [ ] Code pushed to GitHub.
- [ ] Working tree clean after commit.
- [ ] No secrets committed.

## 19. Five daily MCQs

**Q1. What is Git?**  
A. A distributed version-control system  
B. A relational database  
C. A Python framework  
D. An HTTP method  
**Answer: A.** Git tracks changes and history in files.

**Q2. Which command stages a file?**  
A. git push  
B. git add  
C. git log  
D. git merge  
**Answer: B.** git add stages selected changes.

**Q3. What is a branch used for?**  
A. Deleting repository history  
B. Encrypting passwords  
C. Isolating work on a line of development  
D. Installing Django  
**Answer: C.** Branches let developers work on changes independently.

**Q4. Which file commonly excludes .env from Git?**  
A. requirements.txt  
B. main.py  
C. README.md  
D. .gitignore  
**Answer: D.** .gitignore specifies untracked files Git should ignore.

**Q5. What should you do after resolving a merge conflict?**  
A. Remove markers, test, stage and complete the merge  
B. Delete the repository  
C. Push without checking  
D. Ignore the conflict  
**Answer: A.** Resolve the content, validate it and complete the merge.

## 20. Interview preparation

**Q1. What is the difference between Git and GitHub?**  
Git is version-control software. GitHub hosts Git repositories and collaboration features.

**Q2. What is a commit?**  
A recorded snapshot of staged changes in the local repository history.

**Q3. What is a branch?**  
An independent line of development that allows work to be isolated before integration.

**Q4. What is a merge conflict?**  
A situation where Git cannot automatically reconcile competing changes.

**Q5. How do you avoid committing secrets?**  
Use .gitignore for private files, keep secrets in secure environment configuration, inspect staged changes and rotate any exposed credential.

## 21. Phase 2 cumulative assessment — Web-Connected Employee Database Workflow

**Scenario:** An HR team needs a small employee data service concept demonstration. Combine HTTP request/response knowledge, JSON payloads, relational tables, SQL queries and Git version control.

**Requirements**
1. Design employee and department tables with primary and foreign keys.
2. Create, query, update and delete sample employee records.
3. Produce JSON representations of selected records.
4. Document GET, POST, PUT, PATCH and DELETE semantics.
5. Give suitable examples of success and error status codes.
6. Commit work on a feature branch and merge it safely.
7. Document setup and verification steps in README.

**Evidence:** Database schema, SQL script, sample JSON, HTTP examples, terminal output, Git history and README.

**Validation:** Duplicate primary keys are rejected; invalid foreign keys are rejected when enforcement is enabled; UPDATE and DELETE are restricted with WHERE; JSON parses successfully; Git working tree is clean after merge.

**Rubric:** Concepts 20%, correctness 30%, reasoning 20%, code quality 15%, testing 10%, communication 5% = 100%.

**Phase interview questions**
1. Trace browser-to-server communication.
2. Explain HTTP methods and status codes.
3. Compare JSON and XML.
4. Explain primary and foreign keys.
5. Explain JOIN and GROUP BY.
6. Explain Git branch versus commit.

**Phase 2 complete. Next: Phase 3 — Django Fundamentals (Days 27–41).**
