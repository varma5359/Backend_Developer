# Day 2: Python Installation, Environment Setup, Interpreter, VS Code and Jupyter Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Day 1 — backend development overview  
**Required tools:** Windows, Python 3, VS Code, terminal/PowerShell, optional Jupyter  
**Approved mini-project:** Python Environment Setup

## 1. Learning objectives
- Explain the Python interpreter and how a Python program runs.
- Verify a Python installation from the terminal.
- Create and run a Python file in VS Code.
- Create and activate a virtual environment.
- Install and verify a package inside the environment.

## 2. What is Python?
Python is a general-purpose programming language. A Python source file usually has the `.py` extension.

Example:
```python
print("Hello, Backend Developer!")
```

Save this as `hello.py`. The `print()` function displays output.

## 3. What is the Python interpreter?
The interpreter is the program that executes Python code. When you run a script, Python reads and executes the code.

Common commands on Windows:

```powershell
python --version
py --version
```

Expected output is a Python version, for example:
```text
Python 3.x.x
```

The exact version depends on the installed release.

If the command is not recognized:
- Check whether Python is installed.
- Reopen the terminal after installation.
- Check PATH configuration.
- On Windows, try the Python launcher command `py`.

## 4. Create and run your first file

### Step 1: Create a project folder
In PowerShell:
```powershell
mkdir backend_learning
cd backend_learning
```

### Step 2: Create a Python file
Create `hello.py` in VS Code and enter:
```python
message = "Python is ready for backend development"
print(message)
```

### Step 3: Run the file
```powershell
python hello.py
```

Expected output:
```text
Python is ready for backend development
```

Explanation:
- `message` is a variable holding text.
- The assignment operator `=` stores the value.
- `print(message)` displays the value.

## 5. What is VS Code?
Visual Studio Code is a code editor. With the Python extension, it can provide syntax highlighting, code completion, debugging and interpreter selection.

Basic workflow:
1. Open the project folder.
2. Create a `.py` file.
3. Select the installed Python interpreter.
4. Run the file using the terminal or editor controls.
5. Read errors in the terminal and correct them.

Keep the project folder open rather than opening unrelated files one by one. This makes relative paths and project organization easier to understand.

## 6. What is a virtual environment?
A virtual environment creates an isolated Python environment for a project. It helps prevent package versions from different projects interfering with one another.

Create it from the project folder:
```powershell
python -m venv .venv
```

Activate in PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you may use the Command Prompt activation command:
```cmd
.venv\Scripts\activate.bat
```

Or run the interpreter directly without activation:
```powershell
.venv\Scripts\python.exe --version
```

Deactivate an activated environment:
```powershell
deactivate
```

## 7. Install a package
With the environment activated:
```powershell
python -m pip install requests
```

Verify:
```powershell
python -m pip show requests
```

Why use `python -m pip`?
- It runs pip using the selected Python interpreter.
- It reduces confusion when multiple Python installations exist.
- It helps ensure the package is installed into the expected environment.

## 8. Save project dependencies
```powershell
python -m pip freeze > requirements.txt
```

Install recorded dependencies later:
```powershell
python -m pip install -r requirements.txt
```

For a small training exercise, this captures the installed environment. In maintained projects, review and pin only the dependencies actually required by the application.

## 9. What is Jupyter?
Jupyter Notebook is an interactive environment where code is run in separate cells. It is useful for experiments and learning.

Install:
```powershell
python -m pip install notebook
```

Start:
```powershell
jupyter notebook
```

For backend application development, normal `.py` files and a clear project structure are generally more suitable than putting the application entirely in a notebook. Jupyter is optional in this pathway.

## 10. Common environment commands

| Command | Purpose |
|---|---|
| `python --version` | Display selected Python version |
| `where.exe python` | Locate Python executables on Windows |
| `python -m venv .venv` | Create virtual environment |
| `.venv\Scripts\Activate.ps1` | Activate in PowerShell |
| `python -m pip install package` | Install a package |
| `python -m pip list` | List installed packages |
| `python -m pip freeze` | List installed packages with versions |
| `deactivate` | Leave active virtual environment |

## 11. Industry scenario
A team maintains two Django services. One project depends on a specific package version while the other uses a newer release. Separate virtual environments allow both projects to install their own dependencies without unnecessarily changing the global Python installation.

## 12. Approved mini-project — Python Environment Setup

**Objective:** Create a clean, reproducible Python workspace ready for later Django lessons.

### Requirements
1. Create a project directory named `python_environment_setup`.
2. Verify the Python version.
3. Create a `.venv` environment.
4. Activate it and verify which Python executable is being used.
5. Install the `requests` package.
6. Create and run `hello.py`.
7. Generate `requirements.txt`.
8. Add a README that documents setup and activation commands.

**Suggested structure**
```text
python_environment_setup/
├── .venv/
├── hello.py
├── requirements.txt
└── README.md
```

Do not upload the `.venv` directory to GitHub. Add it to `.gitignore` when you begin version control.

### Validation
- `python --version` works.
- The active Python points to the project's virtual environment.
- `requests` is installed in that environment.
- `hello.py` runs successfully.
- `requirements.txt` contains dependency information.
- README instructions work in a second terminal session.

## 13. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint to verify whether my virtual environment is active." |
| 2 — Plan | "Break Python environment setup into commands for Windows PowerShell." |
| 3 — Example | "Show a small example requirements.txt and explain it." |
| 4 — Guided implementation | "Guide me through creating .venv, then wait while I run the command." |
| 5 — Explanation | "Explain the difference between Python, pip and a virtual environment." |
| 6 — Debugging | "My PowerShell activation command failed. Ask me for the error and help diagnose it." |
| 7 — Review | "Review my setup README and check whether another fresher could reproduce the environment." |

**Planning prompt:** "Help me plan the Python Environment Setup deliverable with commands, expected outputs and verification checks."

**Implementation prompt:** "Guide me through one setup command at a time. Explain what it does and wait for my terminal result."

**Debugging/review prompt:** "Review my terminal output and folder structure. Identify environment or PATH issues without giving unrelated installation steps."

## 14. Daily quiz

**Q1. What is the role of the Python interpreter?**  
A. Store database tables  
B. Execute Python code  
C. Design CSS  
D. Create GitHub accounts  
**Correct: B.** The interpreter executes Python programs.

**Q2. What does `python -m venv .venv` do?**  
A. Deletes Python  
B. Creates a virtual environment  
C. Runs a Django server  
D. Creates a database  
**Correct: B.** It creates an isolated environment in the `.venv` folder.

**Q3. Why use a virtual environment?**  
A. To isolate project dependencies  
B. To speed up the monitor  
C. To replace source code  
D. To publish an API  
**Correct: A.** Each project can manage its dependencies separately.

**Q4. What does `python -m pip install requests` do?**  
A. Installs requests using the selected Python interpreter  
B. Creates a virtual environment  
C. Starts Jupyter  
D. Deletes the package  
**Correct: A.** It runs pip through that interpreter.

**Q5. Which file commonly records Python project dependencies?**  
A. index.html  
B. requirements.txt  
C. manage.py  
D. Docker network file  
**Correct: B.** requirements.txt can list packages and versions needed by the project.

## 15. Interview preparation

### Q1. What is a Python virtual environment?
**Answer:** A virtual environment is an isolated Python environment for a project. It allows the project to install and use its own packages without interfering with other Python projects or the global environment.

**Follow-up:** How do you create and activate one on Windows?

### Q2. What is the difference between Python and pip?
**Answer:** Python is the interpreter used to execute Python programs. pip is a package installer used to install Python libraries. Running `python -m pip` uses pip associated with the selected Python interpreter.

**Follow-up:** Why might `pip install` and `python -m pip install` affect different environments?

## 16. Completion checklist
- [ ] Verify Python installation.
- [ ] Create and activate .venv.
- [ ] Run a Python file in VS Code.
- [ ] Install and verify a package.
- [ ] Create requirements.txt and README.
- [ ] Complete Python Environment Setup.

**Next lesson:** Day 3 — Variables, data types, type conversion and operators.
