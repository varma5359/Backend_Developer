# Day 2: Python Installation, Environment Setup, Interpreter, VS Code and Jupyter Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Day 1 — backend development overview  
**Required tools:** Windows, Python 3, VS Code and PowerShell or Command Prompt  
**Approved mini-project:** Python Environment Setup

## 1. Learning objectives

- Explain what Python and the Python interpreter do.
- Verify Python installation from a terminal.
- Create and run a `.py` file in VS Code.
- Create and activate a virtual environment.
- Install and verify a package in the correct environment.
- Explain when a notebook is useful and when a normal Python file is preferable.

## 2. What is Python?

Python is a general-purpose programming language. It is used for scripting, automation, web development, data processing and many other tasks.

Python source files commonly use the `.py` extension.

```python
print("Hello, Backend Developer!")
```

Save this code in a file named `hello.py`. The `print()` function displays a value in the terminal.

## 3. What is the Python interpreter?

The Python interpreter is the program that runs Python code. When you execute a script, the interpreter reads the program and carries out its instructions.

Open PowerShell or Command Prompt and check:

```powershell
python --version
```

Possible output:

```text
Python 3.12.5
```

Your version may be different. The important point is that the command prints a Python 3 version.

On Windows, the Python launcher may also be available:

```powershell
py --version
```

To locate the executable:

```powershell
where.exe python
```

If Python is not recognized:

1. Confirm Python is installed.
2. Close and reopen the terminal after installation.
3. Check whether the Python installation directory is available through PATH.
4. Try `py --version` on Windows.
5. In VS Code, select the intended Python interpreter.

Do not install Python repeatedly before checking which executable your terminal is using.

## 4. Create a project folder

A project folder keeps related files together.

```powershell
mkdir backend_learning
cd backend_learning
```

- `mkdir` creates a directory.
- `cd` changes the current directory.

Create a file named `hello.py` in this folder.

```python
message = "Python is ready for backend development"
print(message)
```

Run it from the terminal:

```powershell
python hello.py
```

Expected output:

```text
Python is ready for backend development
```

The terminal must be in the folder containing `hello.py`, or you must provide the correct file path.

## 5. What is VS Code?

Visual Studio Code is a code editor. It is not Python itself. With the Python extension, it can help you:

- Highlight Python syntax.
- Suggest code while typing.
- Select a Python interpreter.
- Run Python files.
- Set breakpoints and debug programs.
- Work with project folders and a terminal.

Basic setup:

1. Install VS Code.
2. Open the project folder using **File → Open Folder**.
3. Install the Microsoft Python extension.
4. Open or create a `.py` file.
5. Select the intended interpreter from the interpreter selector.
6. Run the file and inspect terminal output.

If VS Code runs a different Python version from PowerShell, compare the selected interpreter path with the terminal executable.

## 6. What is a virtual environment?

A virtual environment is an isolated Python environment for one project. It keeps that project's installed packages separate from packages used by other projects.

Example: Project A may need one version of a library while Project B needs another. Separate environments reduce dependency conflicts.

Create an environment from the project folder:

```powershell
python -m venv .venv
```

Explanation:

- `python` runs the selected Python interpreter.
- `-m venv` runs Python's built-in virtual-environment module.
- `.venv` is the directory where the environment is created.

### Activate in PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

The prompt commonly shows `(.venv)` when activation succeeds.

### Activate in Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Verify the active interpreter

```powershell
python -c "import sys; print(sys.executable)"
```

The printed path should point inside your project's `.venv` directory.

### Deactivate

```powershell
deactivate
```

Deactivation exits the virtual environment in the current terminal session. It does not delete it.

If PowerShell blocks activation because of its execution policy, do not change machine-wide security settings casually. You can use Command Prompt activation or call the environment's Python executable directly:

```powershell
.venv\Scripts\python.exe --version
```

## 7. Install and verify a package

With the environment activated:

```powershell
python -m pip install requests
```

Verify installation:

```powershell
python -m pip show requests
```

Test importing it:

```python
import requests

print("Requests package is available")
print(requests.__version__)
```

Run the test file using the environment's Python interpreter.

Why use `python -m pip` instead of only `pip`?

- It runs pip through the Python interpreter selected by `python`.
- It reduces confusion when multiple Python installations exist.
- It helps install the package into the environment you intend to use.

If an import fails after installation, check whether the package was installed using the same interpreter that runs the script.

## 8. Record project dependencies

A dependency is an external package that your project uses.

Create a dependency list:

```powershell
python -m pip freeze > requirements.txt
```

The `>` operator redirects command output into a file.

Install dependencies later:

```powershell
python -m pip install -r requirements.txt
```

For a learning exercise, `pip freeze` records installed packages and versions. In a maintained project, review the file and keep only dependencies the project actually needs.

## 9. What is Jupyter Notebook?

Jupyter Notebook is an interactive environment where code is organized into cells. A student can run one cell, inspect its output and then run another cell.

Install it inside the selected environment:

```powershell
python -m pip install notebook
```

Start it:

```powershell
jupyter notebook
```

A browser tab normally opens with the notebook interface.

### Notebook versus Python script

| Python script (`.py`) | Jupyter Notebook (`.ipynb`) |
|---|---|
| Runs as a program or module | Runs code in separate cells |
| Suitable for application logic | Useful for interactive exploration |
| Common for Django projects | Useful for demonstrations and experiments |
| Easier to organize as application modules | Cell execution order can affect state |

For backend development, use normal Python files for application code. Jupyter is optional and useful for learning or experimentation.

## 10. Useful environment commands

| Command | Purpose |
|---|---|
| `python --version` | Show the selected Python version |
| `py --version` | Show the Windows Python launcher version |
| `where.exe python` | Locate Python executables |
| `python -m venv .venv` | Create a virtual environment |
| `.venv\Scripts\Activate.ps1` | Activate in PowerShell |
| `.venv\Scripts\activate.bat` | Activate in Command Prompt |
| `python -m pip install requests` | Install a package |
| `python -m pip list` | List installed packages |
| `python -m pip freeze` | List installed packages and versions |
| `deactivate` | Deactivate the environment |

## 11. Common problems and troubleshooting

| Problem | Likely reason | What to check |
|---|---|---|
| `python is not recognized` | Python is not installed or PATH is not configured | Installation and terminal PATH |
| Wrong Python version runs | Multiple Python installations | `where.exe python` and VS Code interpreter |
| `ModuleNotFoundError` | Package missing from active environment | `python -m pip show package_name` |
| Activation script is blocked | PowerShell execution policy | Use Command Prompt or direct interpreter path |
| File cannot be found | Terminal is in a different folder | Run `pwd` and check the file path |
| Package installs but import fails | pip and script use different interpreters | Compare `sys.executable` |

## 12. Industry scenario

A team maintains two Python services. One service depends on an older compatible version of a package, while another service uses a newer version. Installing both dependencies globally can create conflicts.

Separate virtual environments allow each project to use its own dependencies. This makes development more predictable and helps another developer reproduce the setup.

## 13. Connection to the approved mini-project

**Python Environment Setup**

Create a folder named `python_environment_setup` and demonstrate that:

- Python is installed and its version is recorded.
- A `.venv` environment exists.
- The environment's interpreter is being used.
- The `requests` package is installed in that environment.
- A `hello.py` file runs successfully.
- A `requirements.txt` file records dependencies.
- A README explains how to recreate the environment.

Suggested structure:

```text
python_environment_setup/
├── .venv/
├── hello.py
├── requirements.txt
├── .gitignore
└── README.md
```

Add `.venv/` to `.gitignore`. Do not commit the virtual-environment directory to GitHub; another developer should recreate it from the setup instructions.

## 14. Key takeaways

- Python is the language; the interpreter executes Python programs.
- VS Code is an editor that can be configured to use Python.
- A virtual environment isolates project dependencies.
- Use `python -m pip` to install packages through the intended interpreter.
- Use `requirements.txt` to record dependencies.
- Jupyter is useful for interactive learning, while Django application code belongs in organized Python files.

**Next lesson:** Day 3 — Variables, data types, type conversion and operators.
