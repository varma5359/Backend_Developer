# Day 27: Introduction to Django, Features, Architecture and Installation

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours (self-paced reading, hands-on setup and independent verification)  
**Level:** Beginner  
**Prerequisites:** Days 1–26 — Python, OOP, HTTP, SQL and Git fundamentals  
**Tools:** Windows 10/11, Python, VS Code, PowerShell, Git and internet access  
**Approved mini-project:** Django Environment Setup

> **Teaching promise:** Do not copy commands without understanding them. This lesson explains what each command does, why we use it, where to run it, what result to expect and how to troubleshoot it. The learner should finish with a clean, repeatable Django development environment.

---

# PART 1 — UNDERSTAND DJANGO BEFORE INSTALLING IT

## 1. What will we learn today?

By the end of this lesson, you should be able to:

1. Explain what Django is in your own words.
2. Explain why backend developers use a web framework.
3. Distinguish a programming language, library and framework.
4. Understand what problems Django solves.
5. Identify Django's major built-in features.
6. Understand the high-level Django request-response lifecycle.
7. Explain the difference between a Django project and a Django application.
8. Understand the role of Python, pip and a virtual environment.
9. Select a compatible Python and Django version.
10. Create and activate a virtual environment on Windows.
11. Install a fixed Django version inside that environment.
12. Verify that the correct Django installation is being used.
13. Save the dependency version in a requirements file.
14. Diagnose common installation and environment problems.
15. Submit a reproducible Django Environment Setup project.

## 2. First understand what we are building

Before learning Django, imagine a company asks you to develop an employee portal.

The company wants employees to:

- Open a website.
- Log in with their account.
- View their profile.
- See their department.
- Update selected personal information.
- Submit a leave request.
- Check the status of a leave request.

A website like this needs more than a Python print statement.

It needs to receive browser requests, understand which page the user wants, execute application rules, read or save information, and send a response back to the browser.

That server-side work is called **backend development**.

### 2.1 What does the user see?

The user may see a page like this:

\`\`\`text
-----------------------------------------
              EMPLOYEE PORTAL
-----------------------------------------
Welcome, Asha

Employee ID : EMP101
Department  : Data Science
Email       : asha@example.com

[View Profile]  [Apply Leave]  [Logout]
-----------------------------------------
\`\`\`

This is only an example of a user interface. The page is not the entire application.

Behind the page, the backend must answer questions:

- Who is the logged-in user?
- Is the requested employee record available?
- Is this user allowed to view it?
- Is the submitted leave date valid?
- Should the database be updated?
- What response should be returned?

Django helps us build this backend in an organized way.

## 3. What is Django?

**Django is a high-level Python web framework used to build web applications.**

Let's understand each word.

### 3.1 Python

Python is the programming language.

We write application logic using Python syntax:

\`\`\`python
employee_name = "Asha"
department = "Data Science"

print(employee_name)
print(department)
\`\`\`

Python provides the language features: variables, conditions, loops, functions, classes, exceptions and modules.

### 3.2 Web

A web application communicates over a network, commonly using HTTP or HTTPS.

Examples:

- Employee portals.
- Shopping websites.
- Job portals.
- Learning management systems.
- Banking portals.
- Booking systems.
- Business dashboards.

A web application normally has a client and a server.

### 3.3 Framework

A framework provides an organized structure and reusable tools for building an application.

Instead of writing every common web feature from the beginning, we use the framework's existing components and follow its conventions.

Django provides tools for:

- URL routing.
- Handling HTTP requests.
- Returning HTTP responses.
- Rendering HTML templates.
- Defining database models.
- Querying a database.
- Validating forms.
- Managing users and authentication.
- Enforcing permissions.
- Protecting against common web security risks.
- Managing application configuration.

### 3.4 Put the meaning together

\`\`\`text
Python
  |
  | Programming language
  v
Django
  |
  | Web framework built with Python
  v
Web application
  |
  +--> Receives browser requests
  +--> Runs backend logic
  +--> Reads/writes database records
  +--> Returns HTML or other responses
\`\`\`

**Remember:** Django does not replace Python. Django is written in Python and we use Python to build applications with Django.

## 4. What problem does Django solve?

Let's compare two approaches.

### 4.1 Without a web framework

Suppose you decide to build a web application using only low-level Python code.

You would need to think about:

1. How to receive HTTP requests.
2. How to identify the requested URL.
3. How to decide which Python function should run.
4. How to create an HTTP response.
5. How to produce HTML.
6. How to validate submitted data.
7. How to connect to a database.
8. How to manage users and passwords.
9. How to protect private pages.
10. How to organize all the files.
11. How to handle errors.
12. How to test the application.

You can build web applications without Django, but you would need to implement or assemble many of these pieces yourself.

### 4.2 With Django

Django already provides standard components for many common tasks.

| Requirement | Django component or feature |
|---|---|
| Decide which code handles a URL | URL dispatcher |
| Process an HTTP request | View |
| Return an HTTP response | HttpResponse and related response classes |
| Generate HTML from data | Template engine |
| Define database structure | Models |
| Query database records | Django ORM |
| Change database structure safely | Migrations |
| Manage records through an admin site | Django admin |
| Validate user-submitted data | Forms and model forms |
| Manage user login | Authentication system |
| Restrict actions | Permissions and authorization |
| Protect forms against CSRF | CSRF protection |
| Run development checks | Django management commands |

Django does not automatically build your business application. You still decide what the application should do and write the business logic.

### 4.3 Important distinction

Django provides a foundation. It does not understand your company's rules automatically.

For example, Django does not know:

- Whether an employee is eligible for leave.
- How many leave days a particular employee receives.
- Which manager approves the leave.
- Whether a leave request conflicts with an existing request.

You must implement those rules.

## 5. Programming language vs library vs framework

Students often use these words as if they mean the same thing. They are different.

### 5.1 Programming language

A programming language defines syntax and rules used to write instructions.

Example: Python.

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)
print(total)
\`\`\`

Python tells us how to write the function, pass arguments and return a result.

### 5.2 Library

A library is reusable code that your program can call when it needs a particular capability.

Example: Python's \`json\` library.

\`\`\`python
import json

employee = {"name": "Asha", "department": "IT"}

json_text = json.dumps(employee)

print(json_text)
\`\`\`

Here, our code decides when to call \`json.dumps()\`.

### 5.3 Framework

A framework provides a larger structure and controls important parts of the application's execution flow.

In Django, the framework receives an HTTP request, performs framework processing, resolves the URL and calls the appropriate view.

We write the view, but Django controls the surrounding request-processing process.

### 5.4 Comparison table

| Point | Language | Library | Framework |
|---|---|---|---|
| Example | Python | json | Django |
| Main purpose | Write instructions | Reuse functionality | Organize and run an application |
| Who writes business code? | Developer | Developer | Developer |
| Who controls application flow? | Your program | Mostly your program | Framework controls key lifecycle steps |
| Example | Define a function | Convert a dictionary to JSON | Route a URL to a Django view |

### 5.5 What is inversion of control?

This phrase may sound difficult. Understand it with a simple comparison.

**When using a library:**

\`\`\`text
Your Python code
      |
      v
Calls a library function
      |
      v
Gets the result
\`\`\`

**When using a framework:**

\`\`\`text
Django receives a request
      |
      v
Django performs framework processing
      |
      v
Django calls your view at the correct time
      |
      v
Your view returns a response
      |
      v
Django completes response processing
\`\`\`

The framework calls your code as part of its lifecycle. This is one important idea behind inversion of control.

Do not worry about mastering the terminology today. You will see this behavior repeatedly when we write Django views.

## 6. Where is Django used?

Django can be used for many kinds of backend applications.

| Application | Example backend responsibility |
|---|---|
| E-commerce | Products, carts, orders and customer accounts |
| Job portal | Candidate profiles, job listings and applications |
| Learning platform | Courses, lessons, enrollment and progress |
| Employee portal | Employee records, leave requests and approvals |
| Inventory system | Products, stock movements and suppliers |
| Booking application | Availability, reservations and user accounts |
| Content platform | Articles, authors, categories and publishing |
| REST API backend | JSON endpoints for web and mobile clients |

These are examples of possible application types, not claims that every company uses Django for every such system.

## 7. Django's major features

We will study these features across the upcoming days. Today, understand what each feature is responsible for.

### 7.1 URL routing

URL routing connects a requested URL to the code that should handle it.

For example:

\`\`\`text
/employees/       -> employee list page
/employees/101/   -> employee detail page
/about/           -> about page
\`\`\`

Django uses URL configuration to map paths to views.

We will implement URL routing in Day 30.

### 7.2 Views

A view is Python code that receives a request and returns a response.

A view may:

- Read request information.
- Validate input.
- Call business logic.
- Query a model.
- Render a template.
- Return JSON or another response.

We will learn function-based views in Day 31.

### 7.3 Templates

Templates help generate HTML using data supplied by the backend.

For example, the backend may provide:

\`\`\`python
employee = {
    "name": "Asha",
    "department": "IT"
}
\`\`\`

A template can display the employee's name and department in an HTML page.

We will learn templates in Days 32 and 33.

### 7.4 Models and ORM

A model describes the structure of data managed by Django.

For example, an Employee model may describe:

- Employee ID.
- Employee name.
- Email address.
- Department.
- Joining date.

Django's Object-Relational Mapper (ORM) allows developers to work with database records using Python objects and query expressions.

We will study models, migrations and ORM in Days 34, 35 and 37.

### 7.5 Migrations

A migration records a database schema change.

Suppose we add a \`department\` field to an Employee model. The Python model has changed, but the database table also needs to be updated.

Django migrations provide a controlled way to apply schema changes.

We will study this in Day 35.

### 7.6 Django Admin

Django includes an admin site that can help authorized staff manage application data.

For example, an administrator may add, update or inspect employee records through a browser interface.

The admin site is not a replacement for every custom user-facing application screen.

We will learn it in Day 36.

### 7.7 Forms and validation

Forms help collect and validate submitted data.

For example, an employee registration form may require:

- A non-empty name.
- A valid email address.
- A valid joining date.
- A selected department.

We will study forms and validation in Days 39 and 40.

### 7.8 Authentication and permissions

Authentication answers:

**Who are you?**

Authorization answers:

**What are you allowed to do?**

For example:

- An employee can view their own profile.
- A manager can review leave requests for their team.
- An administrator can manage selected records.

These topics are covered later in Phase 4.

### 7.9 Security protections

Django includes protections and recommended practices for common web security concerns.

Examples include:

- Cross-site request forgery (CSRF) protection.
- Safe password hashing through the authentication system.
- Query parameterization through the ORM.
- Host validation.
- Security-related settings.
- Template autoescaping for ordinary variable output.

These protections do not make an application automatically secure. Developers must configure and use Django correctly.

## 8. What Django does not do automatically

This is important because beginners sometimes think a framework handles everything.

| Django provides | Developer must still do |
|---|---|
| URL routing mechanism | Define the application's URL patterns |
| View system | Write correct request-handling logic |
| ORM | Design sensible models and relationships |
| Authentication tools | Define registration and access requirements |
| Form system | Define fields and validation rules |
| Admin site | Register models and configure admin behavior |
| Security mechanisms | Configure settings and follow secure coding practices |
| Testing framework | Write meaningful tests |
| Development server | Configure a production deployment |

**Key lesson:** Knowing the names of Django features is not the same as knowing how to build an application with them.

---

# PART 2 — UNDERSTAND DJANGO ARCHITECTURE

## 9. What happens when a user opens a website?

Imagine a user opens:

\`http://127.0.0.1:8000/employees/\`

The browser sends an HTTP request to the local Django development server.

Django processes that request and eventually returns a response.

Let's understand the high-level flow before writing code.

\`\`\`text
                 USER
                  |
                  | Opens /employees/
                  v
              WEB BROWSER
                  |
                  | HTTP GET request
                  v
          DJANGO DEVELOPMENT SERVER
                  |
                  v
              MIDDLEWARE
                  |
                  v
             URL RESOLVER
                  |
                  | Finds matching URL pattern
                  v
                 VIEW
                  |
          +-------+--------+
          |                |
          v                v
     BUSINESS LOGIC     DJANGO MODEL
                           |
                           v
                        DATABASE
                           |
                           v
                       QUERY RESULT
          |                |
          +-------+--------+
                  |
                  v
             TEMPLATE
                  |
                  v
             HTTP RESPONSE
                  |
                  v
              WEB BROWSER
                  |
                  v
             USER SEES PAGE
\`\`\`

This diagram is simplified. Not every request uses a database or template. A view can return a plain text response, JSON, a redirect or another response type.

## 10. Understand each architecture component

### 10.1 Browser

The browser is the client.

Examples:

- Google Chrome.
- Microsoft Edge.
- Firefox.

The browser sends a request and displays or processes the response.

### 10.2 Development server

During local development, Django provides a lightweight development server.

It listens on a local address and port, receives HTTP requests and passes them into Django's request handling.

We will start it in Day 28 after creating a project.

### 10.3 Middleware

Middleware is a framework mechanism that processes requests and responses around the view.

Examples of middleware responsibilities include:

- Session handling.
- Authentication integration.
- CSRF checks.
- Security-related processing.
- Common request and response processing.

Middleware is not the same thing as a view. We will study middleware much later in the pathway.

### 10.4 URL resolver

The URL resolver examines the requested path and finds a matching URL pattern.

For example:

\`\`\`text
Requested path: /employees/
          |
          v
URL configuration
          |
          v
Matching view is selected
\`\`\`

If no pattern matches, Django normally returns a 404 response.

We will write URL patterns in Day 30.

### 10.5 View

The view is the Python component that handles the request.

A view might:

1. Receive the request.
2. Read a URL parameter.
3. Query a database.
4. Prepare data.
5. Return a response.

We will write our first Django view in Day 31.

### 10.6 Model

A model describes data and database behavior.

For example, an Employee model may represent employee records.

The model is a Python class that Django maps to database structures through the ORM.

We will create our first model in Day 34.

### 10.7 Database

The database stores persistent information.

Examples:

- Employee records.
- Department records.
- User accounts.
- Leave requests.

Django uses SQLite by default for a newly generated project unless configured otherwise. PostgreSQL is the primary database target for this career pathway.

### 10.8 Template

A template generates an HTML response using data passed by the view.

A template is not a Python view. It is a presentation file interpreted by Django's template engine.

We will study it in Day 32.

### 10.9 Response

A response is sent back to the client.

Examples:

- HTML page.
- JSON data.
- Plain text.
- Redirect.
- 404 response.
- 403 response.

## 11. Understand a simple request-response story

Suppose Asha opens the employee list page.

1. Asha enters the URL in Chrome.
2. Chrome sends a GET request.
3. The development server receives it.
4. Django runs its request-processing pipeline.
5. The URL resolver finds the employee-list route.
6. Django calls the view connected to that route.
7. The view asks the model for employee records.
8. The ORM communicates with the database.
9. The database returns the matching records.
10. The view sends the records to a template.
11. Django renders the template.
12. Django returns an HTTP response.
13. Chrome displays the HTML page.

At this stage, you are learning the flow, not implementing every component.

## 12. Django uses the Model-Template-View pattern

Django commonly describes its architecture using **Model-Template-View (MTV)**.

| Component | Responsibility | Simple interpretation |
|---|---|---|
| Model | Data structure and database interaction | What data does the application manage? |
| Template | Presentation | How should the HTML page look? |
| View | Request handling and application logic | What should happen for this request? |

### 12.1 Model

The model describes data.

Example concept:

\`\`\`text
Employee
  |
  +-- employee_id
  +-- name
  +-- email
  +-- department
\`\`\`

### 12.2 Template

The template controls how information is presented.

Example concept:

\`\`\`html
<h1>Employee Details</h1>
<p>Name: Asha</p>
<p>Department: IT</p>
\`\`\`

This is a simple HTML illustration, not a complete Django template implementation.

### 12.3 View

The view coordinates the request and response.

Conceptually:

\`\`\`text
Request
   |
   v
View
   |
   +--> Obtain data from model
   |
   +--> Send data to template
   |
   v
Response
\`\`\`

### 12.4 Is Django exactly the same as MVC?

Django's MTV pattern is related to Model-View-Controller (MVC), but the naming differs.

A rough comparison:

| General MVC term | Django concept |
|---|---|
| Model | Model |
| View (presentation) | Template |
| Controller (request coordination) | View plus framework URL/request machinery |

Do not memorize this as a perfect one-to-one mapping. The important point is to understand each responsibility.

## 13. Project versus application

This distinction is essential for the next lesson.

### 13.1 Django project

A Django project is the overall configuration and collection of applications that make up a website.

Think of it as the complete website workspace.

Example:

\`\`\`text
employee_portal/
    project configuration
    employee feature
    leave feature
    accounts feature
\`\`\`

### 13.2 Django application

A Django application is a Python package that provides a particular set of features.

Examples:

- employees — employee profile features.
- leave — leave requests and approvals.
- accounts — account-related features.
- inventory — product and stock features.

### 13.3 Analogy

Think of a college:

- College = Django project.
- Departments = Django applications.
- Students, teachers and courses = data managed by those applications.

A project can contain multiple applications.

An application can also be reusable in more than one project if designed appropriately.

### 13.4 Comparison

| Project | Application |
|---|---|
| Represents the overall website configuration | Represents a feature or functional component |
| Contains project-level settings and URL configuration | Contains feature-specific code |
| Can include multiple apps | Belongs to a project when installed/used |
| Example: employee_portal | Example: employees |

We will create a project and an application in Day 28.

---

# PART 3 — PLAN THE DEVELOPMENT ENVIRONMENT

## 14. What software do we need?

For this course, use:

| Software | Why we need it |
|---|---|
| Python | Programming language |
| pip | Installs Python packages |
| venv | Creates an isolated environment |
| Django | Python web framework |
| VS Code | Code editor |
| PowerShell | Windows terminal |
| Git | Version control |
| Web browser | Verify web application behavior |

You do not need to install PostgreSQL today. Django's initial environment setup can use SQLite, and PostgreSQL will be configured in the appropriate later lessons.

## 15. Understand the Python environment

Before installing Django, understand where Python packages are installed.

Imagine you have two projects:

\`\`\`text
Project A -> Django 5.2
Project B -> Flask
\`\`\`

If every package is installed into one shared Python environment, projects can interfere with one another.

For example:

- Project A needs one Django version.
- Project B may need a different dependency version.
- Updating a shared package may unexpectedly break another project.

A virtual environment isolates the packages for a project.

## 16. What is pip?

\`pip\` is Python's package installer.

It installs packages from package indexes or other supported package sources.

Example:

\`\`\`powershell
python -m pip install django
\`\`\`

Meaning:

- \`python\` selects the Python interpreter.
- \`-m\` asks Python to run a module as a script.
- \`pip\` is the module being run.
- \`install\` is the pip operation.
- \`django\` is the package name.

### 16.1 Why use python -m pip instead of only pip?

On a machine with multiple Python installations, the \`pip\` command may point to a different Python interpreter than the \`python\` command.

Using:

\`\`\`powershell
python -m pip --version
\`\`\`

helps show which Python installation is running pip.

After activating a virtual environment, \`python -m pip\` uses that environment's interpreter.

This reduces package-installation confusion.

## 17. What is a virtual environment?

A virtual environment is an isolated Python environment for a project.

It contains:

- An environment-specific Python executable or interpreter reference.
- An environment-specific package installation location.
- Scripts used to activate the environment.

The environment folder is commonly named \`.venv\`.

### 17.1 Without a virtual environment

\`\`\`text
Computer Python installation
        |
        +--> Django
        +--> Flask
        +--> Requests
        +--> Other packages
\`\`\`

All projects may share the same packages.

### 17.2 With virtual environments

\`\`\`text
Computer
  |
  +--> Project A
  |      |
  |      +--> .venv
  |             |
  |             +--> Django
  |             +--> Project A packages
  |
  +--> Project B
         |
         +--> .venv
                |
                +--> Flask
                +--> Project B packages
\`\`\`

Each project can manage its own dependencies.

### 17.3 Is .venv part of the application source code?

The \`.venv\` folder is a local development environment. It is not normally committed to Git.

Instead, we record package dependencies in a file such as \`requirements.txt\`.

Another developer can create their own virtual environment and install the same dependencies from that file.

## 18. Choose a Django version for this course

Django releases change over time. A teaching repository should not silently change versions every time a student installs the framework.

For this pathway, use a consistent baseline:

<box border radius="lg" padding={3} gap={2}>
  **Course baseline**

  <title size="2xl" color="success" tabularNums>5.2.19</title>
  **Django 5.2 LTS**

  - Course installation target: Django 5.2.19
  - Python compatibility: Python 3.10–3.14
  - Support horizon listed by Django: extended support through April 2028
  - Use the same Django 5.2 series for the lesson examples unless a later lesson explicitly explains a version difference.
</box>

Why choose this baseline?

1. It is an LTS release series.
2. It supports a broad range of Python versions used in teaching environments.
3. It gives the class a consistent API and behavior.
4. It reduces differences between student machines.
5. It has an official support horizon suitable for a course that students may revisit.

The official Django download and installation pages should always be checked before a new cohort starts. The latest release may change after this lesson is published.

Official references:

- Django download and supported releases: https://www.djangoproject.com/download/
- Django 5.2 installation documentation: https://docs.djangoproject.com/en/5.2/topics/install/
- Django 5.2 installation FAQ: https://docs.djangoproject.com/en/5.2/faq/install/

### 18.1 What if my Python version is different?

The course baseline uses Python 3.10 through 3.14.

Check your Python version before installing Django.

If your Python version is outside the supported range:

- Do not randomly install a different Django version.
- Check the official compatibility table.
- Install a compatible Python version or use the appropriate Django release.
- Keep the classroom version consistent.

Django 6.1 has a newer Python compatibility requirement. Do not install Django 6.1 for this course while following examples that are pinned to Django 5.2 unless the course baseline has deliberately been migrated and tested.

---

# PART 4 — STEP-BY-STEP INSTALLATION ON WINDOWS

## 19. Step 1: Open PowerShell

We will use Windows PowerShell for the main classroom instructions.

1. Press the Windows key.
2. Search for PowerShell.
3. Open Windows PowerShell or the VS Code integrated terminal.
4. If using VS Code, select Terminal → New Terminal.
5. Check that the terminal profile is PowerShell.

You should see a prompt similar to:

\`\`\`text
PS C:\Users\Student>
\`\`\`

Your username and path will be different. That is normal.

**Important:** Commands in this lesson must be run in a terminal, not typed into the Python interactive prompt.

A Python prompt looks like:

\`\`\`text
>>>
\`\`\`

If you see \`>>>\`, you are inside Python. Type \`exit()\` and press Enter to return to PowerShell.

## 20. Step 2: Check Python is installed

Run:

\`\`\`powershell
python --version
\`\`\`

Possible output:

\`\`\`text
Python 3.12.8
\`\`\`

Your patch version may be different.

### 20.1 What does this command do?

- \`python\` asks the operating system to run Python.
- \`--version\` asks Python to display its version.
- The command does not install or update Python.

### 20.2 If python is not recognized

You may see:

\`\`\`text
python : The term 'python' is not recognized...
\`\`\`

Possible causes:

- Python is not installed.
- Python is installed but not available on PATH.
- The terminal was opened before PATH changed.
- Windows is resolving the command to an unwanted alias.

Try:

\`\`\`powershell
py --version
\`\`\`

The Windows Python launcher may be available even when the \`python\` command is not.

If \`py --version\` works, you can use \`py\` for the initial environment creation.

If neither command works, install Python from the official Python website and reopen the terminal:

https://www.python.org/downloads/

Do not continue until one intended Python installation can be run.

## 21. Step 3: Check which Python executable is being used

Run:

\`\`\`powershell
where.exe python
\`\`\`

Possible output:

\`\`\`text
C:\Users\Student\AppData\Local\Programs\Python\Python312\python.exe
\`\`\`

This command shows executable paths found through PATH.

If multiple paths appear, your machine may have multiple Python installations.

That is not automatically a problem. You must be consistent about which interpreter is used for the project.

You can also run:

\`\`\`powershell
python -c "import sys; print(sys.executable)"
\`\`\`

Possible output:

\`\`\`text
C:\Users\Student\AppData\Local\Programs\Python\Python312\python.exe
\`\`\`

This command prints the exact Python executable used by the current \`python\` command.

### 21.1 Understand the command

- \`-c\` tells Python to execute the code supplied as a string.
- \`import sys\` imports Python's system-related module.
- \`sys.executable\` contains the path to the current Python executable.
- \`print()\` displays that path.

## 22. Step 4: Create the course workspace

Choose a location where you can keep your backend learning projects.

Example:

\`\`\`text
D:\TechPhile\Backend_Developer
\`\`\`

If the D drive does not exist on your computer, use another location.

Create the folder:

\`\`\`powershell
New-Item -ItemType Directory -Force -Path "D:\TechPhile\Backend_Developer"
\`\`\`

Change into it:

\`\`\`powershell
Set-Location "D:\TechPhile\Backend_Developer"
\`\`\`

Verify:

\`\`\`powershell
Get-Location
\`\`\`

Expected output should show the folder you selected.

### 22.1 What is the current working directory?

The current working directory is the folder where a command runs by default.

When we create a virtual environment using:

\`\`\`powershell
python -m venv .venv
\`\`\`

the \`.venv\` folder is created inside the current working directory.

If you run the command from the wrong folder, you may create the environment in the wrong place.

**Self-check:** Run \`Get-Location\`. Confirm that PowerShell shows the workspace folder you created for this lesson. If it shows a different folder, use \`Set-Location\` to move into the correct workspace before creating \`.venv\`. Do not continue until the current folder is correct.

## 23. Step 5: Open the folder in VS Code

If the \`code\` command is available, run:

\`\`\`powershell
code .
\`\`\`

The dot means the current folder.

If the command is not available:

1. Open VS Code from the Start menu.
2. Select File → Open Folder.
3. Choose the Backend_Developer folder.
4. Confirm that the correct folder appears in the Explorer panel.
5. Open Terminal → New Terminal.

The VS Code Explorer should show the project workspace.

Do not create the virtual environment in a random folder outside this workspace.

## 24. Step 6: Create a virtual environment

Make sure the terminal is inside the workspace.

Run:

\`\`\`powershell
python -m venv .venv
\`\`\`

If you are using the Windows Python launcher instead:

\`\`\`powershell
py -m venv .venv
\`\`\`

### 24.1 Understand every part

| Part | Meaning |
|---|---|
| python | Runs the selected Python interpreter |
| -m | Runs a Python module as a command |
| venv | Python's built-in virtual environment module |
| .venv | Name of the environment folder to create |

### 24.2 What happens after execution?

Python creates a folder similar to:

\`\`\`text
Backend_Developer/
    .venv/
        Include/
        Lib/
        Scripts/
        pyvenv.cfg
\`\`\`

The exact contents can vary by operating system and Python version.

You do not need to edit the files inside \`.venv\`.

### 24.3 Verify that the folder exists

Run:

\`\`\`powershell
Get-ChildItem -Force
\`\`\`

You should see a \`.venv\` directory.

The \`-Force\` option includes hidden items.

## 25. Step 7: Activate the virtual environment

For Windows PowerShell:

\`\`\`powershell
.\.venv\Scripts\Activate.ps1
\`\`\`

After activation, the prompt normally starts with:

\`\`\`text
(.venv) PS D:\TechPhile\Backend_Developer>
\`\`\`

The \`(.venv)\` label indicates that the environment is active.

### 25.1 What does activation mean?

Activation adjusts the current shell session so that commands such as \`python\` and \`pip\` resolve to the virtual environment first.

It does not install Django.

It does not create a Django project.

It does not permanently change every terminal on your computer.

It affects the terminal session where you activated it.

### 25.2 Verify the active Python

Run:

\`\`\`powershell
python -c "import sys; print(sys.executable)"
\`\`\`

Expected path should point inside your workspace:

\`\`\`text
D:\TechPhile\Backend_Developer\.venv\Scripts\python.exe
\`\`\`

If it points to a global Python installation, stop and check activation.

### 25.3 PowerShell says script execution is disabled

You may see an error similar to:

\`\`\`text
...Activate.ps1 cannot be loaded because running scripts is disabled...
\`\`\`

This is a PowerShell execution policy restriction.

First, do not run random commands copied from the internet.

For a classroom machine, follow the organization's approved IT policy.

If your organization permits it, a temporary policy for the current PowerShell process can be considered:

\`\`\`powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
\`\`\`

Then retry activation:

\`\`\`powershell
.\.venv\Scripts\Activate.ps1
\`\`\`

The Process scope applies to the current PowerShell process and is discarded when that process closes. It does not change the machine-wide policy.

If your organization does not permit this, use Command Prompt activation or ask the administrator for the approved method.

### 25.4 Activate using Command Prompt instead

Open Command Prompt (cmd.exe), change into the project folder, and run:

\`\`\`cmd
.venv\Scripts\activate.bat
\`\`\`

The prompt should show:

\`\`\`text
(.venv) D:\TechPhile\Backend_Developer>
\`\`\`

### 25.5 Activate using Git Bash

If using Git Bash:

\`\`\`bash
source .venv/Scripts/activate
\`\`\`

Use the activation command that matches your terminal. Do not paste PowerShell activation syntax into Git Bash.

## 26. Step 8: Upgrade pip inside the environment

With \`.venv\` active, run:

\`\`\`powershell
python -m pip install --upgrade pip
\`\`\`

### Why do we upgrade pip?

pip is the package installer. An older installer may have compatibility or package-resolution issues.

### Understand the command

- \`python -m pip\` runs pip using the active Python interpreter.
- \`install\` tells pip to install a package.
- \`--upgrade\` requests a newer version if one is available.
- \`pip\` is the package being upgraded.

The exact version number shown in the terminal can change over time.

Verify:

\`\`\`powershell
python -m pip --version
\`\`\`

The displayed path should point inside \`.venv\`.

## 27. Step 9: Install the course Django version

We will install the pinned course version:

\`\`\`powershell
python -m pip install "Django==5.2.19"
\`\`\`

### 27.1 Why do we pin the version?

A version pin makes the classroom environment reproducible.

Without a pin:

\`\`\`powershell
python -m pip install django
\`\`\`

pip installs the latest compatible release available at that time.

The version may change between student installations.

With a pin:

\`\`\`powershell
python -m pip install "Django==5.2.19"
\`\`\`

we explicitly request version 5.2.19.

### 27.2 What does == mean?

In a package version requirement:

- \`==\` means an exact version match.
- \`5.2.19\` is the version requested.

The quotation marks protect the requirement as one command argument in PowerShell and other shells.

### 27.3 What does pip do during installation?

At a high level:

1. Reads the requested package and version.
2. Contacts the configured package index if required.
3. Finds a compatible distribution.
4. Resolves required dependencies.
5. Downloads packages.
6. Installs them into the active environment.
7. Reports the installation result.

A successful installation normally ends with a message indicating that Django and its dependencies were installed.

The exact dependency list and terminal output may vary.

## 28. Step 10: Verify Django installation

Run:

\`\`\`powershell
python -m django --version
\`\`\`

Expected output:

\`\`\`text
5.2.19
\`\`\`

If the output is 5.2.19, the Django command is available to the active Python interpreter.

### 28.1 Verify using Python code

Run:

\`\`\`powershell
python -c "import django; print(django.get_version())"
\`\`\`

Expected output:

\`\`\`text
5.2.19
\`\`\`

### 28.2 Verify the Django package location

Run:

\`\`\`powershell
python -c "import django; print(django.__file__)"
\`\`\`

The output should point inside the \`.venv\` directory.

This is a useful debugging check when a computer has multiple Python installations.

### 28.3 Inspect package metadata

Run:

\`\`\`powershell
python -m pip show Django
\`\`\`

Look for:

- Name.
- Version.
- Location.
- Requires.

The Location should point to the active virtual environment's package directory.

## 29. Step 11: Save the installed dependencies

A project should record the packages it depends on.

Run:

\`\`\`powershell
python -m pip freeze
\`\`\`

This displays installed packages and versions.

For the current environment, create a requirements file:

\`\`\`powershell
python -m pip freeze > requirements.txt
\`\`\`

The \`>\` operator redirects command output into a file.

Open \`requirements.txt\` in VS Code.

You should see Django and its installed dependencies listed with versions.

### 29.1 Why is requirements.txt useful?

Imagine another student receives your project.

They do not need to guess which Django version you used.

They can create a virtual environment and install the recorded requirements:

\`\`\`powershell
python -m pip install -r requirements.txt
\`\`\`

This installs the listed dependencies into the active environment.

### 29.2 Important note about pip freeze

\`pip freeze\` records installed packages in the environment. If you have installed unrelated packages in the same environment, they may also appear in the file.

For this course, keep the environment dedicated to the Backend Developer project.

## 30. Step 12: Verify the environment one final time

Run these commands one by one:

\`\`\`powershell
python --version
python -m pip --version
python -m django --version
python -c "import sys; print(sys.executable)"
python -c "import django; print(django.__file__)"
Get-Location
Get-ChildItem -Force
\`\`\`

You should be able to confirm:

1. The intended Python version is active.
2. pip belongs to the active environment.
3. Django reports version 5.2.19.
4. The Python executable is inside \`.venv\`.
5. Django's package path is inside \`.venv\`.
6. The current folder is the intended workspace.
7. The environment folder and requirements file exist.

**Stop here if any verification points to the wrong Python installation.**

---

# PART 5 — OTHER OPERATING SYSTEM COMMANDS

## 31. If a learner uses Windows Command Prompt

The following sequence is for cmd.exe.

Create and enter the workspace using File Explorer or:

\`\`\`cmd
mkdir D:\TechPhile\Backend_Developer
cd /d D:\TechPhile\Backend_Developer
\`\`\`

Create the environment:

\`\`\`cmd
py -m venv .venv
\`\`\`

Activate:

\`\`\`cmd
.venv\Scripts\activate.bat
\`\`\`

Install:

\`\`\`cmd
python -m pip install --upgrade pip
python -m pip install "Django==5.2.19"
\`\`\`

Verify:

\`\`\`cmd
python -m django --version
python -m pip freeze > requirements.txt
\`\`\`

The commands are similar, but the activation command is different.

## 32. If a learner uses Linux or macOS

Create a workspace and enter it:

\`\`\`bash
mkdir -p ~/TechPhile/Backend_Developer
cd ~/TechPhile/Backend_Developer
\`\`\`

Create a virtual environment:

\`\`\`bash
python3 -m venv .venv
\`\`\`

Activate it:

\`\`\`bash
source .venv/bin/activate
\`\`\`

Install:

\`\`\`bash
python -m pip install --upgrade pip
python -m pip install "Django==5.2.19"
\`\`\`

Verify:

\`\`\`bash
python -m django --version
python -m pip freeze > requirements.txt
\`\`\`

The environment's executable paths differ from Windows.

## 33. How to deactivate the environment

When you finish working, run:

\`\`\`powershell
deactivate
\`\`\`

The \`(.venv)\` label should disappear from the terminal prompt.

This does not delete the environment. It only deactivates it for the current terminal session.

To work again, activate it using the command for your terminal.

## 34. How to delete and recreate a virtual environment

Sometimes an environment becomes inconsistent.

For example:

- Wrong packages were installed.
- The wrong Python interpreter was used.
- Package installation was interrupted.
- The environment was created with an incompatible Python version.

If you have confirmed that you are in the correct project folder and have no important data stored inside \`.venv\`, you can remove the environment and recreate it.

PowerShell:

\`\`\`powershell
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
\`\`\`

**Warning:** The Remove-Item command deletes the .venv folder. Check the current directory before running it. Do not use it on a folder whose path you have not verified.

The project source code and requirements file should be outside \`.venv\`.

---

# PART 6 — DJANGO INSTALLATION TROUBLESHOOTING

## 35. Problem: No module named django

Example:

\`\`\`text
ModuleNotFoundError: No module named 'django'
\`\`\`

### Meaning

The Python interpreter running your command cannot find Django in its installed packages.

### Possible causes

1. Django was not installed.
2. Django was installed in another Python environment.
3. The virtual environment is not activated.
4. VS Code is using a different Python interpreter.
5. The terminal is running another Python executable.

### Diagnosis

Run:

\`\`\`powershell
python -c "import sys; print(sys.executable)"
python -m pip show Django
\`\`\`

If pip cannot find Django, install it after confirming the correct environment:

\`\`\`powershell
python -m pip install "Django==5.2.19"
\`\`\`

Then verify:

\`\`\`powershell
python -m django --version
\`\`\`

Do not solve this by installing Django globally without understanding which interpreter is being used.

## 36. Problem: Django version is different

Suppose you expected:

\`\`\`text
5.2.19
\`\`\`

but the command shows another version.

### Check installed metadata

\`\`\`powershell
python -m pip show Django
\`\`\`

### Check the executable

\`\`\`powershell
python -c "import sys; print(sys.executable)"
\`\`\`

### Reinstall the course version in the active environment

\`\`\`powershell
python -m pip install --force-reinstall "Django==5.2.19"
\`\`\`

The \`--force-reinstall\` option tells pip to reinstall the requested package even if it is already installed.

Use this only after confirming that the active interpreter is the intended virtual environment.

Verify again:

\`\`\`powershell
python -m django --version
\`\`\`

## 37. Problem: pip is not recognized

Instead of:

\`\`\`text
pip is not recognized as an internal or external command
\`\`\`

use:

\`\`\`powershell
python -m pip --version
\`\`\`

If that works, use \`python -m pip\` for installation.

If Python cannot import pip, repair or install pip for the selected Python installation using the official Python guidance. Do not download random pip executables.

## 38. Problem: Could not find a version that satisfies the requirement

Possible causes:

- Python version is not compatible with the requested Django release.
- Package index access is blocked.
- Internet connection or proxy configuration is incorrect.
- The requested version was typed incorrectly.
- pip is too old to handle the environment correctly.

Check:

\`\`\`powershell
python --version
python -m pip --version
python -m pip config list
\`\`\`

Then compare the Python version with the official Django compatibility table.

Do not randomly switch between Django releases until the compatibility issue is understood.

## 39. Problem: PowerShell activation is blocked

Check the current policy:

\`\`\`powershell
Get-ExecutionPolicy -List
\`\`\`

Use the organization's approved approach.

If permitted, use the temporary current-process policy explained in Section 25.3, or activate using Command Prompt.

Never change machine-wide execution policy just to avoid understanding the restriction.

## 40. Problem: VS Code uses the wrong interpreter

Symptoms:

- Terminal can import Django, but editor shows import warnings.
- Running a Python file uses another interpreter.
- The selected environment differs from the terminal environment.

Steps:

1. Open the workspace folder in VS Code.
2. Open the Command Palette.
3. Search for **Python: Select Interpreter**.
4. Select the interpreter inside the project's \`.venv\`.
5. Open a new terminal.
6. Run the verification commands again.

The selected interpreter should point to:

\`\`\`text
<workspace>\.venv\Scripts\python.exe
\`\`\`

on Windows.

## 41. Problem: The virtual environment is active but Django is missing

Activation does not install packages.

Run:

\`\`\`powershell
python -m pip list
\`\`\`

If Django is absent, install it:

\`\`\`powershell
python -m pip install "Django==5.2.19"
\`\`\`

Then verify the version.

## 42. Problem: Installation fails because of internet or proxy restrictions

Check:

- Whether the browser can access the package index.
- Whether the institute network requires a proxy.
- Whether a firewall blocks package downloads.
- Whether the terminal reports certificate or connection errors.

Use the institute's approved network and package-index configuration.

Do not disable TLS certificate verification as a quick fix. That weakens the security of package downloads.

## 43. Problem: The wrong folder contains .venv

Run:

\`\`\`powershell
Get-Location
Get-ChildItem -Force
\`\`\`

If the environment was created in the wrong location:

1. Stop using that environment.
2. Navigate to the intended project workspace.
3. Create a new environment there.
4. Activate it.
5. Install the requirements.
6. Verify the executable path.

Avoid moving an existing virtual environment between folders. Recreating it in the correct location is usually clearer.

---

# PART 7 — PROJECT SETUP QUALITY AND GOOD PRACTICES

## 44. Recommended workspace structure after today's lesson

At the end of Day 27, the workspace may look like:

\`\`\`text
Backend_Developer/
│
├── .venv/
│
└── requirements.txt
\`\`\`

We have not created a Django project yet. That is Day 28.

### Why not create every folder now?

Each day introduces a new responsibility.

Today:

- Understand Django.
- Prepare Python.
- Create a virtual environment.
- Install Django.
- Verify installation.

Day 28:

- Create a Django project.
- Create a Django application.
- Understand manage.py.
- Inspect generated project files.

This separation lets beginners understand one new idea at a time.

## 45. Create a .gitignore file

A virtual environment should not normally be committed to Git.

Create a file named \`.gitignore\` in the workspace:

\`\`\`gitignore
# Python bytecode
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/

# Local environment secrets
.env

# Editor settings (team policy may differ)
.vscode/

# Test and coverage artifacts
.pytest_cache/
.coverage
htmlcov/
\`\`\`

### Understand why .venv is ignored

The virtual environment contains local executable files and installed packages.

It can be recreated from the dependency file.

Committing it:

- Makes the repository unnecessarily large.
- Can include machine-specific paths.
- Does not provide a portable environment.
- Makes collaboration harder.

### Understand why .env is ignored

A future Django application may store private configuration in environment variables or a local \`.env\` file.

A private configuration file can contain secrets. It should not be committed.

A later lesson will explain environment configuration properly.

## 46. What is requirements.txt?

It is a text file that records Python package requirements.

Example for this lesson:

\`\`\`text
Django==5.2.19
\`\`\`

The actual \`pip freeze\` output may contain additional packages required by Django.

### Install from requirements.txt

A new developer can run:

\`\`\`powershell
python -m pip install -r requirements.txt
\`\`\`

The \`-r\` option tells pip to read package requirements from a file.

### Why is it useful in a team?

Imagine three developers work on one Django project.

Without a dependency file:

- Developer A may use Django 5.2.
- Developer B may install a newer version.
- Developer C may use an older version.

They can see different behavior.

A dependency file makes the intended package environment explicit.

## 47. Development environment versus production environment

Do not confuse local development with production deployment.

| Development | Production |
|---|---|
| Used while building and testing | Used by real users |
| Django development server is convenient | Use a production-ready server setup |
| Debugging tools may be enabled locally | Debug mode must be disabled |
| Local SQLite may be used for learning | This pathway targets PostgreSQL |
| Local configuration | Secure environment-specific configuration |
| Test data | Real application data with backup and security requirements |

The Django development server is not designed to be a production server.

We will learn production deployment in Phase 7.

## 48. Security habits from the first day

Start following these habits immediately:

1. Do not commit passwords.
2. Do not commit API keys.
3. Do not publish a Django secret key.
4. Do not expose database credentials.
5. Do not use DEBUG mode on a public production deployment.
6. Do not disable security checks just to make an error disappear.
7. Install packages from trusted sources.
8. Use supported software versions.
9. Keep dependencies recorded.
10. Read warnings instead of ignoring them.

Django provides security mechanisms, but developers are responsible for correct configuration and application design.

---

# PART 8 — DAY 27 PRACTICAL MINI-PROJECT

## 49. Project: Django Environment Setup

**Approved project title:** Django Environment Setup

### 49.1 Business / technical scenario

A new junior developer joins a team that maintains a Django-based employee portal.

Before writing application code, the developer must prepare a local environment that other team members can reproduce.

The developer must:

- Use a compatible Python version.
- Create a virtual environment.
- Install the agreed Django version.
- Verify the installation.
- Record dependencies.
- Avoid committing local environment files.

This is a real first step in a backend development workflow.

### 49.2 Project objective

Prepare a clean, documented and verifiable Django environment.

At the end of the project, another learner should be able to follow the README and recreate the environment.

### 49.3 Functional requirements

| No. | Requirement | Evidence |
|---:|---|---|
| 1 | Check Python version | Terminal output |
| 2 | Create workspace folder | Folder visible in VS Code |
| 3 | Create virtual environment | .venv directory |
| 4 | Activate virtual environment | Prompt shows (.venv) |
| 5 | Install pinned Django version | pip installation result |
| 6 | Verify Django version | 5.2.19 output |
| 7 | Verify Python executable | Path inside .venv |
| 8 | Generate requirements.txt | File visible in workspace |
| 9 | Add .gitignore | .venv and .env excluded |
| 10 | Document setup | README.md |

### 49.4 Required folder structure

\`\`\`text
day_27_django_environment/
│
├── .venv/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
\`\`\`

Do not upload the \`.venv\` directory as part of the project submission.

### 49.5 Implementation tasks

**Task 1 — Check Python**

Run:

\`\`\`powershell
python --version
python -c "import sys; print(sys.executable)"
\`\`\`

Write down the version and executable path.

**Task 2 — Create the workspace**

Create the project folder and open it in VS Code.

**Task 3 — Create the environment**

\`\`\`powershell
python -m venv .venv
\`\`\`

**Task 4 — Activate**

\`\`\`powershell
.\.venv\Scripts\Activate.ps1
\`\`\`

**Task 5 — Upgrade pip**

\`\`\`powershell
python -m pip install --upgrade pip
\`\`\`

**Task 6 — Install Django**

\`\`\`powershell
python -m pip install "Django==5.2.19"
\`\`\`

**Task 7 — Verify**

\`\`\`powershell
python -m django --version
python -c "import django; print(django.get_version())"
python -c "import sys; print(sys.executable)"
\`\`\`

**Task 8 — Record dependencies**

\`\`\`powershell
python -m pip freeze > requirements.txt
\`\`\`

**Task 9 — Create .gitignore**

Add:

\`\`\`gitignore
.venv/
__pycache__/
*.py[cod]
.env
.pytest_cache/
\`\`\`

**Task 10 — Write README**

The README must contain:

- Project title.
- Python version used.
- Django version used.
- Environment creation command.
- Activation command for Windows PowerShell.
- Installation command.
- Verification command.
- Dependency installation command for another learner.
- Common errors and their solutions.

### 49.6 How to verify the project

Before marking the project complete, demonstrate the following to yourself and capture the output in your README or evidence file: 

1. The active terminal.
2. The active virtual environment.
3. The Python version.
4. The Django version.
5. The Django package location.
6. The requirements file.
7. The Git ignore rules.
8. The README setup instructions.

A screenshot of a successful installation alone is not enough. The learner must explain what the commands did.

### 49.7 Project test cases

| Test | Action | Expected result |
|---|---|---|
| 1 | Run python --version | Compatible Python version shown |
| 2 | Activate .venv | Prompt shows environment label |
| 3 | Print sys.executable | Path points inside .venv |
| 4 | Run Django version command | 5.2.19 |
| 5 | Run pip show Django | Location points inside .venv |
| 6 | Inspect requirements.txt | Django requirement is recorded |
| 7 | Inspect .gitignore | .venv and .env are ignored |
| 8 | Deactivate and reactivate | Environment can be activated again |
| 9 | Recreate in a clean environment | Requirements install successfully |
| 10 | Explain the setup | Learner can explain each major step |

### 49.8 What is not required today?

Do not add these features to Day 27:

- Django project creation.
- Django application creation.
- URL configuration.
- Views.
- Templates.
- Models.
- Database migrations.
- Admin registration.
- Authentication.
- REST APIs.

These topics have their own approved days.

This is intentional. We want a clean foundation before building the application.

---

# PART 9 — GUIDED LEARNING AND INDEPENDENT PRACTICE

## 50. Self-paced demonstration sequence

Do not run every command as one large block. Run one step, inspect its result, and explain what changed before continuing.

| Step | You do | Ask yourself / verify |
|---:|---|---|
| 1 | Check Python version | Which Python version is installed? |
| 2 | Print Python executable | Which interpreter is running? |
| 3 | Create workspace | Where will project files be stored? |
| 4 | Create virtual environment | Why isolate dependencies? |
| 5 | Activate environment | What changes in this terminal? |
| 6 | Check pip path | Will packages install inside this environment? |
| 7 | Install Django | Which exact version is being installed? |
| 8 | Verify Django | Does the reported version match the course baseline? |
| 9 | Create requirements file | Can another learner reproduce this setup? |
| 10 | Create .gitignore | Which generated or secret files must not be committed? |

If a check fails, stop and use the troubleshooting section. Do not copy the next command in the hope that the problem disappears.

## 51. Questions to ask during the lesson

1. Is Django a programming language?
2. What is the difference between Python and Django?
3. Why do developers use frameworks?
4. What is a web application?
5. What is the role of a backend?
6. What happens when a browser sends a request?
7. What is a Django view responsible for?
8. What is a Django model responsible for?
9. What is a Django template responsible for?
10. What is a virtual environment?
11. Why do we use pip?
12. Why do we use python -m pip?
13. What happens when a virtual environment is activated?
14. Does activation install Django?
15. Why do we pin a Django version?
16. Why do we save requirements?
17. Why should .venv not be committed?
18. Is runserver a production server?
19. What is the difference between a Django project and app?
20. What should you verify after installation?

## 52. Independent exercises

### Beginner exercises

1. Explain Django in three sentences.
2. Explain the difference between a language, library and framework.
3. Write the command used to create a virtual environment.
4. Write the PowerShell command used to activate it.
5. Write the command used to install Django 5.2.19.
6. Write the command used to verify the Django version.
7. Explain why requirements.txt is needed.
8. Explain why .venv is ignored by Git.

### Intermediate exercises

1. Create a second virtual environment in a separate practice folder.
2. Install Django into the second environment.
3. Compare the Python executable paths of both environments.
4. Deactivate one environment and verify the prompt.
5. Activate the first environment again.
6. Recreate an environment from requirements.txt.
7. Diagnose a deliberately incorrect Python interpreter selection.
8. Explain how a package can be installed in one environment but unavailable in another.

### Explain-without-code exercises

Ask the learner to explain:

1. Why a Django framework is useful.
2. What happens between a browser request and a response.
3. Why a database is usually accessed through backend logic.
4. Why a project may contain multiple applications.
5. Why framework features do not remove the need for business logic.

---

# PART 10 — INTERVIEW PREPARATION

## 53. Beginner interview questions

### Q1. What is Django?

**Answer:** Django is a high-level Python web framework used to develop web applications. It provides reusable components for URL routing, views, templates, database access, forms, authentication and security.

**Example:** We can use Django to build an employee portal that stores employee information and displays it through web pages.

**Follow-up:** Does Django replace Python?

**Answer:** No. Django is built with Python, and developers write Django application code using Python.

### Q2. Why do developers use Django?

**Answer:** Django provides common web-development components and an organized project structure. This reduces the need to build standard functionality from scratch and helps developers focus on application requirements.

**Follow-up:** Does Django automatically implement company business rules?

**Answer:** No. Developers must implement and test the business rules.

### Q3. What is the difference between a framework and a library?

**Answer:** A library provides functionality that our code calls. A framework provides an application structure and controls important parts of the execution flow, calling our code at defined points.

**Follow-up:** Give one example of each.

**Answer:** Python's json module is a library; Django is a web framework.

### Q4. What is a Django project?

**Answer:** A Django project is the overall website configuration and collection of applications.

**Follow-up:** Can a project contain multiple applications?

**Answer:** Yes. A project can contain applications for employees, accounts, inventory and other features.

### Q5. What is a Django application?

**Answer:** A Django application is a Python package that provides a particular set of features within a project.

**Follow-up:** Can an application be reusable?

**Answer:** Yes. An application can be designed as a reusable component and used in more than one project.

### Q6. What is Django's MTV architecture?

**Answer:** MTV stands for Model-Template-View. Model handles data, Template handles presentation and View handles request processing and application logic.

**Follow-up:** What is the rough relation to MVC?

**Answer:** Django's Template is similar to the presentation View in general MVC terminology, while Django's View performs much of the controller responsibility. It is a conceptual comparison, not a strict one-to-one mapping.

### Q7. What is a virtual environment?

**Answer:** A virtual environment is an isolated Python environment that allows a project to manage its own installed packages.

**Follow-up:** Why should each project have its own environment?

**Answer:** It reduces dependency conflicts between projects and makes setup more reproducible.

### Q8. What is pip?

**Answer:** pip is Python's package installer. It installs and manages packages in the selected Python environment.

**Follow-up:** Why use python -m pip?

**Answer:** It runs pip using the selected Python interpreter, helping avoid confusion when multiple Python installations exist.

### Q9. Why do we use requirements.txt?

**Answer:** It records package requirements so another developer can install the same dependencies in a new environment.

**Follow-up:** How do you install from it?

**Answer:** Run python -m pip install -r requirements.txt after activating the intended virtual environment.

### Q10. Is Django's development server suitable for production?

**Answer:** No. It is intended for local development and testing. Production deployment requires a production-ready server configuration.

**Follow-up:** Where will we study production deployment?

**Answer:** In Phase 7 of this pathway.

## 54. Scenario-based interview questions

### Scenario 1 — Django works in one terminal but not another

**Question:** You installed Django and it works in one terminal. In a new terminal, Python reports that Django cannot be imported. What do you check?

**Answer:**

1. Check whether the virtual environment is active.
2. Print sys.executable.
3. Run python -m pip show Django.
4. Confirm the selected interpreter.
5. Activate the correct environment or install dependencies into the intended environment.

**Follow-up:** Why is a global installation not the first solution?

**Answer:** It may hide the environment mismatch and make project setup less reproducible.

### Scenario 2 — Two developers have different Django versions

**Question:** Two developers see different behavior because they installed different Django versions. What should the team do?

**Answer:**

1. Agree on a supported project version.
2. Record the dependency in requirements.txt.
3. Recreate environments from the dependency file.
4. Verify the installed version.
5. Update dependencies through a reviewed change.

**Follow-up:** Should the team blindly install the latest Django release?

**Answer:** No. The team should select a version compatible with its Python version, dependencies and support requirements.

### Scenario 3 — The student committed .venv to GitHub

**Question:** A learner accidentally pushed the virtual environment to GitHub. What should be done?

**Answer:**

1. Add .venv to .gitignore.
2. Stop tracking the generated environment directory in the repository.
3. Remove the tracked environment files from the repository in a reviewed change.
4. Recreate the environment locally from requirements.txt.
5. Check whether any secrets were included.

**Follow-up:** Does .gitignore remove files that are already tracked?

**Answer:** No. A file already tracked by Git needs to be removed from tracking separately.

### Scenario 4 — A learner wants to use Django without understanding Python

**Question:** Can a beginner skip Python and directly memorize Django commands?

**Answer:** The learner should understand Python variables, functions, modules, classes, exceptions and OOP basics first. Django uses those concepts throughout its models, views, forms and application structure.

**Follow-up:** Which earlier phase teaches those foundations?

**Answer:** Phase 1 and Phase 1B.

---

# PART 11 — DAILY MCQs WITH EXPLANATIONS

## 55. MCQ 1

**What is Django?**

A. A Python web framework  
B. A programming language  
C. A database server  
D. A browser

<details>
<summary>Answer and explanation</summary>

**Correct answer: A — A Python web framework.**

Django is a framework written in Python. It provides components used to build web applications.

Why the other options are incorrect:

- B: Python is the programming language.
- C: Django is not a database server.
- D: Django is not a browser.
</details>

## 56. MCQ 2

**Which component is mainly responsible for presenting HTML using backend-provided data?**

A. Model  
B. Template  
C. Database  
D. Virtual environment

<details>
<summary>Answer and explanation</summary>

**Correct answer: B — Template.**

Django templates generate presentation output, commonly HTML.

- A: Model represents data and database behavior.
- C: Database stores persistent data.
- D: Virtual environment isolates Python packages.
</details>

## 57. MCQ 3

**Why do we create a virtual environment?**

A. To create a database table  
B. To start the browser  
C. To isolate project dependencies  
D. To replace Python

<details>
<summary>Answer and explanation</summary>

**Correct answer: C — To isolate project dependencies.**

A virtual environment keeps a project's installed packages separate from other Python environments.

- A: Database tables are created through database tools or migrations.
- B: A virtual environment does not start a browser.
- D: A virtual environment uses Python; it does not replace it.
</details>

## 58. MCQ 4

**Which command verifies the Django version using the active Python interpreter?**

A. python -m django --version  
B. python --install django  
C. django --create version  
D. pip --python django

<details>
<summary>Answer and explanation</summary>

**Correct answer: A — python -m django --version.**

This runs Django's command-line module using the selected Python interpreter and displays the version.

</details>

## 59. MCQ 5

**Which file is commonly used to record Python package dependencies?**

A. index.html  
B. requirements.txt  
C. manage.py  
D. urls.py

<details>
<summary>Answer and explanation</summary>

**Correct answer: B — requirements.txt.**

It records the package requirements needed to recreate a Python environment.

- index.html is an HTML page.
- manage.py is a Django project command-line utility generated when a project is created.
- urls.py contains URL configuration.
</details>

---

# PART 12 — COMPLETION AND TEACHER VALIDATION

## 60. Student completion checklist

A student should be able to check every item below.

### Concept understanding

- [ ] I can explain what Django is.
- [ ] I can explain why a web framework is useful.
- [ ] I can distinguish a language, library and framework.
- [ ] I can identify Django's main features.
- [ ] I can explain the high-level request-response lifecycle.
- [ ] I can explain Model, Template and View.
- [ ] I can distinguish a Django project from a Django application.
- [ ] I can explain what a virtual environment does.

### Practical setup

- [ ] I checked the Python version.
- [ ] I identified the Python executable.
- [ ] I created the workspace folder.
- [ ] I created a virtual environment.
- [ ] I activated the virtual environment.
- [ ] I checked the pip location.
- [ ] I installed Django 5.2.19.
- [ ] I verified the Django version.
- [ ] I checked the Django package location.
- [ ] I created requirements.txt.
- [ ] I created .gitignore.

### Independent explanation

- [ ] I can explain every command I ran.
- [ ] I can explain why the virtual environment is required.
- [ ] I can explain why the Django version is pinned.
- [ ] I can explain how another developer recreates the environment.
- [ ] I can troubleshoot a missing Django installation.

## 61. Independent completion checklist

Mark each item only after you personally perform it and inspect the result:

| Area | Evidence you must see |
|---|---|
| Python | Correct interpreter and supported version |
| Virtual environment | .venv exists inside the intended workspace |
| Activation | PowerShell prompt shows the active environment |
| pip | \`python -m pip --version\` points inside .venv |
| Django | Version 5.2.19 is reported |
| Import | \`python -c \"import django; print(django.get_version())\"\` succeeds |
| Package path | Django module path is inside .venv |
| Dependencies | requirements.txt contains the pinned Django requirement |
| Git hygiene | .venv and .env are ignored |
| Understanding | You can explain each command without reading the explanation aloud |
| Troubleshooting | You can diagnose one deliberately introduced environment error |

A screenshot alone is not proof. Re-run the commands and explain the output in your own words.

## 62. Suggested assessment rubric

| Assessment area | Marks |
|---|---:|
| Django and framework concepts | 20 |
| Architecture explanation | 20 |
| Environment setup correctness | 25 |
| Dependency and Git hygiene | 15 |
| Troubleshooting ability | 10 |
| Verbal explanation and evidence | 10 |
| **Total** | **100** |

Suggested completion threshold: 70/100, with all critical setup checks passed.

## 63. What should you be able to explain to another student?

Without reading the notes, explain this in your own words:

1. Django is a Python web framework.
2. A framework provides reusable components and an application structure.
3. A browser sends an HTTP request to a server.
4. Django processes the request and returns a response.
5. URL configuration selects the view.
6. The view handles request logic.
7. A model represents data.
8. A template generates presentation output.
9. A virtual environment isolates dependencies.
10. requirements.txt helps reproduce the environment.

If you can explain these ideas and demonstrate your environment, you have completed the learning objective for Day 27.

---

# 64. Preview of Day 28 — Creating Django Projects and Applications

Today we installed Django. We did not create the Django project yet.

In Day 28, we will:

1. Create a Django project using \`django-admin startproject\`.
2. Understand the generated folder structure.
3. Understand the role of \`manage.py\`.
4. Understand the project package.
5. Create a Django application using \`startapp\`.
6. Understand the files generated inside an application.
7. Register an application in \`INSTALLED_APPS\`.
8. Understand the difference between project-level and app-level files.
9. Build the approved **Personal Profile Django Project**.

**Do not skip Day 28.** The next lesson builds directly on the environment created today.

---

# 65. Official documentation and references

Use documentation that matches the version used in class.

1. Django 5.2 installation guide: https://docs.djangoproject.com/en/5.2/topics/install/
2. Django 5.2 installation FAQ: https://docs.djangoproject.com/en/5.2/faq/install/
3. Django 5.2 release notes: https://docs.djangoproject.com/en/5.2/releases/5.2/
4. Django supported releases: https://www.djangoproject.com/download/
5. Python virtual environments: https://docs.python.org/3/library/venv.html
6. Python package installation guide: https://packaging.python.org/en/latest/tutorials/installing-packages/

**Version note:** This lesson pins Django 5.2.19 for a consistent classroom environment. Before a new cohort begins, the course owner should check the official Django release and security information and update the course baseline deliberately. If the baseline changes, test the commands and lesson examples against that version before publishing the update.

---

**Day 27 outcome:** A beginner understands what Django is, understands the high-level architecture, has installed the agreed Django version in an isolated Python environment, can verify the installation and can explain the setup to another developer.
