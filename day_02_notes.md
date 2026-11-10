# Day 2: Python Installation, Environment Setup, Interpreter, VS Code and Jupyter Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Day 1 — backend development overview  
**Required tools:** Windows, internet connection, Python 3, VS Code and PowerShell or Command Prompt  
**Approved mini-project:** Python Environment Setup

> **Before you start:** Today is about preparing your computer to write and run Python programs. You do not need to understand advanced programming. Follow the steps in order and check the output after every command.

## 1. What will you learn today?

By the end of this lesson, you should be able to:
1. Explain what Python is and what the Python interpreter does.
2. Install Python and verify that it is available in the terminal.
3. Install and open Visual Studio Code.
4. Create a Python file and run it.
5. Understand what a virtual environment is and why backend projects use one.
6. Install a package inside the correct environment.
7. Explain the basic difference between a Python file and a Jupyter Notebook.

## 2. What is Python?

Python is a programming language. A programming language lets us write instructions that a computer can execute.

For example, imagine you want the computer to display a welcome message. You can write:

```python
print("Welcome to Python")
```

Output:

```text
Welcome to Python
```

Let's understand this line:
- `print` is a built-in Python function. A function performs an operation.
- Parentheses `()` are used to call the function.
- The text inside quotation marks is a string.
- Python displays that text as output.

Python is used in web development, automation, data processing, artificial intelligence and many other areas. In this pathway, we use Python to build backend applications with Django.

## 3. What is the Python interpreter?

You write Python instructions in a file, but the computer needs a program that can execute those instructions. That program is the **Python interpreter**.

Think of it this way:
- You write instructions in Python.
- The Python interpreter runs those instructions.
- You see the result in the terminal or another output area.

A simple flow:

```text
Python code (hello.py)
        |
        v
Python interpreter
        |
        v
Computer executes instructions
        |
        v
Output appears
```

Installing Python normally installs the interpreter and tools such as `pip`.

## 4. Install Python on Windows

1. Open the official Python downloads page: https://www.python.org/downloads/
2. Download a stable Python 3 release suitable for Windows.
3. Run the installer.
4. On the first installation screen, enable **Add Python to PATH** if the option is shown.
5. Select the installation option and wait for setup to finish.
6. Close and reopen PowerShell so it can read the updated PATH.

Why is PATH important? PATH is a list of folders Windows checks when you type a command. If the Python installation folder is available through PATH, you can type `python` without entering the full installation location.

## 5. Verify Python from PowerShell

Open PowerShell and type:

```powershell
python --version
```

Example output:

```text
Python 3.x.x
```

The exact version number depends on the version installed on your computer.

You can also try:

```powershell
py --version
```

The Windows Python launcher `py` may be available even when the `python` command is not configured as expected.

### What does this command mean?

- `python` asks Windows to run the Python interpreter.
- `--version` asks Python to display its version.
- It does not create a project or execute a Python file.

Check pip:

```powershell
python -m pip --version
```

`pip` is the package installer commonly used to install third-party Python packages. The `-m` option tells Python to run the named module. Using `python -m pip` helps ensure that pip belongs to the Python interpreter you invoked.

### If the command is not recognized

Try these checks:
1. Close and reopen PowerShell.
2. Try `py --version`.
3. Check whether Python was installed successfully.
4. Check the PATH option in the installation.
5. If needed, rerun the installer and select the option to add Python to PATH.

Do not download Python from an unknown website or run random commands copied from the internet.

## 6. What is VS Code?

Visual Studio Code (VS Code) is a code editor. It helps you write, organize, run and debug programs.

Download it from: https://code.visualstudio.com/

After installation:
1. Open VS Code.
2. Open the Extensions panel.
3. Search for **Python**.
4. Install the Python extension published by Microsoft.
5. Open a project folder rather than working with many unrelated files on the desktop.

The editor and Python interpreter are different:
- VS Code is where you edit code.
- Python is the program that executes code.
- The Python extension helps VS Code work with Python.

## 7. Create and run your first Python file

Create a folder named `python_backend_practice`. Open that folder in VS Code.

1. Select **File → Open Folder**.
2. Choose `python_backend_practice`.
3. Create a file named `hello.py`.
4. Enter this code:

```python
print("Hello, student!")
print("I am learning Python for backend development.")
```

5. Save the file.
6. Open the VS Code terminal using **Terminal → New Terminal**.
7. Run:

```powershell
python hello.py
```

Expected output:

```text
Hello, student!
I am learning Python for backend development.
```

Explanation:
- `python` starts the interpreter.
- `hello.py` tells the interpreter which file to execute.
- Python runs the first print statement and then the second.
- Each `print()` displays its text on a new line.

Try changing the message, save the file and run it again. This small change-and-run cycle is how you will practise throughout the course.

## 8. What is a terminal?

A terminal is a text-based interface where you type commands to interact with your computer or development tools.

Examples of commands:

| Command | What it does |
|---|---|
| `python --version` | Displays Python version |
| `python hello.py` | Runs a Python file |
| `pwd` | Shows the current folder in many shells |
| `dir` | Lists files in Windows Command Prompt or PowerShell |
| `cd folder_name` | Changes the current directory |
| `mkdir practice` | Creates a folder |

A command is not the same as Python code. For example, `python hello.py` is typed in the terminal, while `print("Hello")` is written inside the Python file.

## 9. What is a virtual environment?

Imagine that you are building two Python projects:

- Project A needs Django version X.
- Project B needs a different Django version.

If both projects use one shared package location, changing a package for one project may affect the other. A **virtual environment** creates an isolated package environment for a project.

A virtual environment:
- Keeps project dependencies separate.
- Helps reproduce the same setup on another computer.
- Reduces conflicts between project packages.
- Makes it easier to document required dependencies.

It does not install a separate operating system or a completely independent Python installation. It provides an isolated environment for Python packages and project execution.

## 10. Create a virtual environment on Windows

Open the terminal in your project folder and run:

```powershell
python -m venv .venv
```

Understand the command:
- `python` runs Python.
- `-m venv` runs Python's built-in virtual-environment module.
- `.venv` is the folder name where the environment will be created.

After running the command, your project may look like this:

```text
python_backend_practice/
├── .venv/
└── hello.py
```

The `.venv` folder contains environment files. Do not manually edit files inside it.

### Activate the environment in PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

When activation succeeds, the terminal prompt commonly shows `(.venv)`.

If PowerShell blocks activation because of its execution policy, do not change system-wide security settings without understanding them. You can use Command Prompt activation instead:

```cmd
.venv\Scripts\activate.bat
```

To leave the environment:

```powershell
deactivate
```

## 11. Install and verify a package

A package is reusable code created by Python developers. For example, Django is a package that provides tools for web development.

With the virtual environment active, install a package:

```powershell
python -m pip install requests
```

What happens?
- `python -m pip` runs pip for the active Python interpreter.
- `install` tells pip to install a package.
- `requests` is the package name.

Verify installation:

```powershell
python -m pip show requests
```

You can also check installed packages:

```powershell
python -m pip list
```

For this lesson, installing Requests is only a package-management demonstration. Django installation and project creation are taught later in the pathway.

## 12. What is Jupyter Notebook?

Jupyter Notebook is an interactive environment where you can write and execute code in small cells.

For example, one cell can contain:

```python
name = "Asha"
```

A second cell can contain:

```python
print(name)
```

Output:

```text
Asha
```

The second cell can use the variable created in the first cell, as long as the first cell has already been executed in the current kernel session.

A notebook is useful for:
- Learning and experimenting.
- Running small code examples.
- Displaying outputs near the code.
- Writing explanations between code cells.

For backend application development, normal `.py` files are generally the main choice because projects need organized modules, packages, tests and application entry points.

You do not need to install Jupyter today unless your trainer specifically wants it. The main goal is to understand the difference.

## 13. Python file versus Jupyter Notebook

| Python file (.py) | Jupyter Notebook (.ipynb) |
|---|---|
| Runs as a script | Runs code in separate cells |
| Common for backend applications | Common for learning and experiments |
| Execution normally starts from the script | Cells can be run in different orders |
| Good for modules and packages | Good for combining code, output and notes |

## 14. Common beginner problems

| Problem | Possible reason | What to do |
|---|---|---|
| `python` is not recognized | Python PATH is not configured | Reopen terminal, try `py`, check installation |
| File not found | Terminal is in a different folder | Use `dir` and `cd` to locate the file |
| Package installed but import fails | Package installed into another interpreter | Activate the environment and use `python -m pip` |
| Activation is blocked | PowerShell execution policy | Use Command Prompt activation or follow approved setup guidance |
| Code changes do not appear | File was not saved or wrong file was run | Save and verify the filename |
| VS Code selects another Python | Interpreter selection differs | Select the project's `.venv` interpreter |

## 15. Approved mini-project — Python Environment Setup

**Objective:** Prepare a clean Python workspace and prove that Python code runs inside the selected environment.

### Requirements

1. Create a folder named `python_backend_practice`.
2. Open the folder in VS Code.
3. Create a file named `hello.py`.
4. Print your name and a backend-learning message.
5. Verify the Python version.
6. Create a virtual environment named `.venv`.
7. Activate the environment.
8. Install the `requests` package inside it.
9. Verify the package using `python -m pip show requests`.
10. Run `hello.py` from the terminal.

### Suggested structure

```text
python_backend_practice/
├── .venv/
└── hello.py
```

### Evidence to submit

- Screenshot of `python --version`.
- Screenshot showing the activated `.venv` prompt.
- Screenshot showing the package verification.
- Screenshot showing the program output.

Do not upload the `.venv` folder to GitHub. It can be recreated using setup instructions and a dependency file.

## 16. Interview preparation

**Question 1: What is the Python interpreter?**

Beginner answer: The Python interpreter is the program that executes Python code. We write instructions in a Python file, and the interpreter runs those instructions.

Follow-up: How do you check the installed Python version?  
Answer: Run `python --version` or, on Windows where available, `py --version`.

**Question 2: Why do we use a virtual environment?**

Beginner answer: A virtual environment keeps the packages for one project separate from other projects. This helps avoid dependency conflicts and makes project setup easier to reproduce.

Follow-up: How do you create one?  
Answer: Run `python -m venv .venv` from the project folder.

**Question 3: What is the difference between VS Code and Python?**

Answer: VS Code is a code editor. Python is the interpreter that executes Python programs. VS Code helps us write and manage code, but Python runs it.

## 17. Daily practice and completion check

Try these tasks without copying the earlier commands:
1. Display your Python version.
2. Create a file named `about_me.py`.
3. Print your name and your learning goal.
4. Create and activate a virtual environment.
5. Explain why a virtual environment is useful.
6. Explain the difference between a terminal command and Python code.

You have completed Day 2 when you can create a Python file, run it from VS Code's terminal and explain which interpreter and environment are being used.

**Next lesson:** Day 3 — Variables, data types, type conversion and operators.
