# Day 26: Interview Questions — Git, GitHub, Repositories, Commits, Branches and Merge Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Related notes:** [Day 26 class notes](day_26_notes.md)  
**Approved mini-project:** Version-Controlled Python Project

## Core questions

### Q1. What is the difference between Git and GitHub?
**Answer:** Git is distributed version-control software. GitHub is a hosting and collaboration platform for Git repositories.

### Q2. What is a repository?
**Answer:** A repository contains project files and the history Git tracks for those files.

### Q3. What is the staging area?
**Answer:** It is the area where selected changes are prepared for the next commit. git add stages changes.

### Q4. What is a commit?
**Answer:** A commit records a snapshot of staged changes in repository history. A useful commit message describes the change.

### Q5. Why use branches?
**Answer:** Branches isolate work so a developer can implement a feature or fix without immediately changing the main development line.

### Q6. What is a merge conflict?
**Answer:** Git cannot automatically reconcile competing changes. A developer must inspect the conflicting content, choose the intended result, test it and complete the merge.

### Q7. What is the difference between fetch and pull?
**Answer:** git fetch downloads remote commits and references without integrating them into the current branch. git pull fetches and integrates remote changes according to the configured strategy.

### Q8. Why use .gitignore?
**Answer:** It tells Git which untracked files or patterns to ignore, such as virtual environments and local .env files. It does not remove a file that is already tracked.

## Scenario-based questions

### Q9. Two developers are working on the same backend project. How can Git help?
**Suggested answer:** Each developer can work on a feature branch, create commits, push changes and integrate them through a reviewed merge or pull request.

### Q10. You accidentally staged a file containing a local environment secret. What should you do before committing?
**Suggested answer:** Unstage the file, add the appropriate pattern to .gitignore, verify that the file is not tracked, and keep the secret outside source control. If the secret was already pushed, rotate or revoke it.

### Q11. You see a merge conflict. What steps do you take?
**Suggested answer:** Open the conflicting files, understand both changes, resolve the content, remove conflict markers, run tests, stage the resolution and complete the merge.

## Command interpretation

| Command | Meaning |
|---|---|
| git init | Initialize a local repository |
| git status | Inspect current changes |
| git add main.py | Stage a file |
| git commit -m "message" | Record staged changes |
| git log --oneline | Show compact history |
| git switch -c feature/name | Create and switch to a branch |
| git merge feature/name | Merge a branch into current branch |
| git remote -v | List configured remotes |
| git push -u origin main | Push and set upstream |
| git fetch | Download remote history without integrating |
| git pull | Fetch and integrate remote changes |

## Project viva — Version-Controlled Python Project

Explain:
1. What did your first commit contain?
2. Why did you create a feature branch?
3. Which files did you stage?
4. How did you verify the merge?
5. What does a clean working tree mean?
6. How did you configure the remote?
7. What files did you exclude with .gitignore?
8. How did you avoid committing secrets?

## Common mistakes

| Mistake | Better approach |
|---|---|
| Committing without checking status | Inspect staged changes first |
| Using vague commit messages | Describe the change |
| Working directly on main for every task | Use feature branches |
| Assuming push runs tests | Run tests separately |
| Committing .env | Keep local secrets out of Git |
| Running reset --hard casually | Understand destructive effects and back up work |

## Rapid revision
- Git — version-control system.
- GitHub — hosted collaboration platform.
- Working tree — files being edited.
- Staging area — selected changes for the next commit.
- Commit — recorded snapshot.
- Branch — independent development line.
- Merge — integrate branch history.
- Remote — another repository location.
- Push — send commits to remote.
- Pull — fetch and integrate remote changes.

## Final checklist
- [ ] Explain Git versus GitHub.
- [ ] Explain staging and commits.
- [ ] Create and merge a feature branch.
- [ ] Explain a merge conflict.
- [ ] Explain fetch versus pull.
- [ ] Explain how secrets are kept out of Git.
- [ ] Present the mini-project and Git evidence.
