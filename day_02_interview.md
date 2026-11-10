# Day 2: Interview Questions — Python Installation, Environment Setup, Interpreter, VS Code and Jupyter Basics

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is the Python interpreter?
**Answer:**
- It executes Python code.
- It translates source instructions into operations the runtime can perform.
- It reports syntax and runtime errors.
- It can run a script or interactive commands.

**Follow-up:** How can you check the Python version in a terminal?

### Q2. What is a virtual environment?
**Answer:**
- An isolated environment for a Python project.
- It keeps project dependencies separate.
- It helps different projects use different package versions.
- It makes setup easier to reproduce.

**Follow-up:** What command creates a virtual environment on Windows?

### Q3. Why should you use `python -m pip`?
**Answer:**
- It invokes pip through the selected Python interpreter.
- It helps avoid installing into a different Python installation.
- It is useful when multiple Python versions exist.
- It makes the intended environment clearer.

**Follow-up:** How do you verify where a package is installed?

### Q4. What is VS Code?
**Answer:**
- A source-code editor.
- It supports Python through an extension.
- It provides syntax highlighting, completion and debugging.
- It can run programs in an integrated terminal.

**Follow-up:** Why is selecting the correct interpreter important?

### Q5. What is Jupyter Notebook?
**Answer:**
- An interactive notebook environment.
- It lets developers execute code in separate cells.
- It is useful for experimentation and demonstrations.
- Normal Python source files are generally more suitable for organized Django applications.

**Follow-up:** When would you choose a .py file over a notebook?

## 2. Scenario questions

### Q6. You installed a package, but Python reports ModuleNotFoundError. What do you check?
**Answer:**
- Is the correct virtual environment activated?
- Does VS Code use the same interpreter?
- Was the package installed using that interpreter?
- Verify with `python -m pip show package_name`.
- Restart the terminal or editor if interpreter selection changed.

**Follow-up:** How would you check the active Python executable?

### Q7. Two projects need different versions of the same library. What is the solution?
**Answer:**
- Create a separate virtual environment for each project.
- Install the required version in each environment.
- Record dependencies in project-specific files.
- Avoid changing global packages unnecessarily.

**Follow-up:** What risk comes from sharing one global environment?

### Q8. PowerShell blocks the activation script. What can you do?
**Answer:**
- Read the full error and confirm the shell.
- Use Command Prompt activation if appropriate.
- Run the virtual environment's Python executable directly.
- Follow organizational device policy rather than weakening security controls broadly.

**Follow-up:** What is the activation command in Command Prompt?

## 3. Project questions

### Q9. Describe your Python Environment Setup project.
**Answer:**
- I created a project folder.
- I verified the Python installation.
- I created and activated a virtual environment.
- I installed a package using the selected interpreter.
- I ran a Python script and recorded dependencies in requirements.txt.

**Follow-up:** How would another developer recreate your environment?

### Q10. Why should .venv normally not be committed to Git?
**Answer:**
- It contains environment-specific installed files.
- It can be large.
- It can differ by operating system and Python version.
- Commit dependency definitions and setup instructions instead.

**Follow-up:** Which file can exclude .venv from Git?

## 4. Rapid revision
- Interpreter: executes Python code.
- VS Code: code editor.
- Jupyter: interactive notebook.
- venv: isolated environment.
- pip: package installer.
- requirements.txt: dependency list.
- Interpreter selection: determines which Python executes the project.
