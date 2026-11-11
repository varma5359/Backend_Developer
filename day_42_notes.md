# Day 42: CRUD Operations — Create, Read, Update and Delete

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–41 — Django setup, URLs, views, templates, Employee model, migrations, ORM, ModelForms, validation and CSRF  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Continuous project:** student_portal / config / profiles  
**Approved mini-project:** Employee CRUD Application

> **Self-learning promise:** Complete this lesson without a trainer. Read one section, perform the action, compare your result with the expected result, and only then continue. Do not skip checkpoints.

---

## 1. What you will build

You will extend the Django project from Phase 3. The Employee model already exists. Today you will build four operations:

1. **Create:** register a new employee.
2. **Read:** display all employees and view one employee.
3. **Update:** edit an existing employee.
4. **Delete:** remove an employee only after a confirmation page and a POST request.

### Business situation

A small company has 30 employees. An administrator needs to add employees, view the directory, correct details and remove test or obsolete records. The database stores the information. Django views decide what operation to perform. Forms validate input. Templates display the pages.

### Final browser journey

~~~text
Employee directory
  |
  +-- Add employee ----> Blank form ----> Save ----> Directory
  |
  +-- View employee ---> Detail page
  |
  +-- Edit employee ---> Pre-filled form ----> Save ----> Directory
  |
  +-- Delete employee -> Confirmation page
                              |
                              +-- Cancel ----> Directory
                              |
                              +-- Confirm (POST) -> Delete -> Directory
~~~

**Important boundary:** This lesson teaches CRUD mechanics. Authentication and authorization are taught from Day 46. Do not expose this local exercise publicly as a production employee-management system.

## 2. Learning outcomes

By the end, you should be able to:

- Define CRUD with a business example.
- Explain how a browser URL reaches a Django view.
- Build a ModelForm from the existing Employee model.
- Create and list records using the Django ORM.
- Retrieve one record safely using get_object_or_404().
- Update an existing record using instance=employee.
- Explain why deletion must use POST, not GET.
- Verify changes in the browser and database.
- Diagnose common CRUD errors independently.

## 3. Confirm your project and environment

### 3.1 Open the correct folder

Open VS Code and open the Django project you created in Phase 3. The project folder must contain manage.py.

~~~text
student_portal/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── profiles/
~~~

Your project may contain extra files. Do not delete them.

The repository folder phase3_reference is a quality-assurance reference project. It is not a replacement for the project you built by following the lessons. Use your own Phase 3 project as the working project.

### 3.2 Confirm the terminal location

In VS Code select Terminal → New Terminal.

~~~powershell
Get-Location
Get-ChildItem
~~~

Expected observation:
- The current path is your Django project directory.
- manage.py appears in the file list.

If manage.py is missing, move into the correct folder. Do not run Django management commands from an unrelated directory.

### 3.3 Activate the virtual environment

If your environment folder is named .venv:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

Confirm Python and Django:

~~~powershell
python --version
python -m django --version
python manage.py check
~~~

Expected: Django is installed and the system check reports no issues. The reference environment uses Python 3.12 and Django 5.2.19. Follow the version pinned by your project requirements if it differs.

If PowerShell blocks activation, follow the Windows environment instructions from Day 2. Do not change machine-wide execution policy blindly.

**Checkpoint 1**
- [ ] I can see manage.py.
- [ ] My virtual environment is active.
- [ ] Django is installed.
- [ ] python manage.py check completes without errors.

Do not continue until this checkpoint passes.

## 4. Understand CRUD

CRUD is an abbreviation:

| Letter | Operation | Meaning | Employee example |
|---|---|---|---|
| C | Create | Insert a new record | Add EMP101 |
| R | Read | Retrieve data | Display employee directory |
| U | Update | Change an existing record | Correct EMP101 email |
| D | Delete | Remove a record | Remove a test employee |

### 4.1 CRUD and SQL

You learned SQL in Phase 2. The database operations are conceptually similar:

| CRUD | SQL idea | Django ORM idea |
|---|---|---|
| Create | INSERT | Employee.objects.create() or form.save() |
| Read | SELECT | Employee.objects.all() |
| Update | UPDATE | Change an instance and call save() |
| Delete | DELETE | Call delete() on an authorized instance |

Django ORM gives Python developers an object-oriented interface to database operations. Django translates ORM operations into database queries.

### 4.2 Why use a ModelForm?

A normal HTML form sends values from the browser. A Django ModelForm connects form fields to a Django model.

A ModelForm:
- Generates fields from model fields.
- Runs form and model validation.
- Can create a new model record.
- Can update an existing model record when an instance is supplied.

A ModelForm does not remove the need for server-side validation. Browser-side validation alone is not sufficient.

### 4.3 Create and update are different

Create:

~~~python
form = EmployeeForm(request.POST)
~~~

Update:

~~~python
employee = get_object_or_404(Employee, pk=pk)
form = EmployeeForm(request.POST, instance=employee)
~~~

The instance argument tells the form which existing object to update. Without it, a valid form normally creates a new record.

### 4.4 Read many and read one

Read many:

~~~python
employees = Employee.objects.all()
~~~

Read one safely:

~~~python
employee = get_object_or_404(Employee, pk=pk)
~~~

Use a QuerySet for a directory and one model instance for a detail, edit or delete page.

## 5. Confirm the existing Employee model

Open profiles/models.py. The Employee model introduced earlier contains:

~~~python
class Employee(models.Model):
    employee_code = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_code} - {self.full_name}"
~~~

| Field | Type | Purpose |
|---|---|---|
| employee_code | CharField | Human-readable identifier |
| full_name | CharField | Employee name |
| email | EmailField | Email address |
| salary | DecimalField | Decimal salary value |
| joining_date | DateField | Joining date |
| is_active | BooleanField | Current active status |
| created_at | DateTimeField | Automatically records creation time |

employee_code and email are unique. They cannot be repeated. created_at uses auto_now_add=True, so the form should not ask the user to enter it.

**Do not create a second Employee model.** The model already exists from Phase 3. Duplicate model definitions can cause migration and import problems.

### 5.1 Inspect records in Django shell

Run:

~~~powershell
python manage.py shell
~~~

Then:

~~~python
from profiles.models import Employee
Employee.objects.count()
Employee.objects.all()
~~~

The first expression returns the number of Employee rows. The second returns a QuerySet representing all employees.

Exit:

~~~python
exit()
~~~

If you see ModuleNotFoundError for profiles:
1. Confirm you are in the folder containing manage.py.
2. Confirm profiles exists.
3. Confirm profiles is listed in INSTALLED_APPS.
4. Check the app name spelling.

## 6. Step 1 — Create EmployeeForm

Open profiles/forms.py.

**Do not delete StudentRegistrationForm from Day 39.** Add EmployeeForm below your existing form. Your file should retain the complete StudentRegistrationForm and its validation methods.

Add the Employee import:

~~~python
from .models import Student, Employee
~~~

Add this class:

~~~python
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "employee_code",
            "full_name",
            "email",
            "salary",
            "joining_date",
            "is_active",
        ]
        widgets = {
            "joining_date": forms.DateInput(attrs={"type": "date"}),
            "salary": forms.NumberInput(attrs={"step": "0.01"}),
        }
~~~

### 6.1 Understand the code

- EmployeeForm inherits from forms.ModelForm.
- The inner Meta class configures the form.
- model = Employee connects it to the Employee model.
- fields is an explicit allow-list of fields accepted from the browser.
- created_at is excluded because Django sets it automatically.
- DateInput with type=date asks the browser to display a date input where supported.
- NumberInput with step=0.01 allows decimal salary steps in the browser.

### 6.2 Why use an explicit fields list?

An explicit allow-list prevents internal or sensitive model fields from accidentally becoming editable if the model changes later. Avoid fields="__all__" for user-controlled forms unless every model field has been reviewed.

### 6.3 Checkpoint

Save the file and run:

~~~powershell
python manage.py check
~~~

Expected: no import or syntax errors.

If Employee cannot be imported, confirm that Employee is defined in profiles/models.py and that capitalization matches.

## 7. Step 2 — Employee list view (READ many)

Open profiles/views.py. Preserve your Student views. Add Employee and EmployeeForm to the imports if they are not already imported.

~~~python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Employee
from .forms import StudentRegistrationForm, EmployeeForm
~~~

Do not duplicate imports already present in the file.

Add:

~~~python
def employee_list(request):
    employees = Employee.objects.order_by("full_name")
    return render(
        request,
        "profiles/employee_list.html",
        {"employees": employees},
    )
~~~

### 7.1 Line-by-line explanation

1. employee_list(request) defines a view. Django passes the incoming HttpRequest object.
2. Employee.objects is the model manager and starting point for ORM queries.
3. order_by("full_name") sorts rows by full_name in ascending order.
4. The QuerySet is stored in employees.
5. render() loads a template and returns an HTTP response.
6. The template path identifies the HTML file to load.
7. The context dictionary sends the QuerySet to the template.
8. The key employees is the name used by the template.

### 7.2 Three query examples

Example 1 — retrieve all employees:

~~~python
Employee.objects.all()
~~~

Example 2 — sort A to Z:

~~~python
Employee.objects.order_by("full_name")
~~~

Example 3 — newest employees first:

~~~python
Employee.objects.order_by("-created_at")
~~~

The minus prefix means descending order. A QuerySet is lazy: constructing it does not necessarily execute SQL immediately. It is evaluated when iterated, converted to a list, or otherwise consumed.

## 8. Step 3 — Employee create view (CREATE)

Add this view:

~~~python
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()

    return render(
        request,
        "profiles/employee_form.html",
        {"form": form, "page_title": "Add Employee"},
    )
~~~

### 8.1 Understand GET and POST

GET means the browser is requesting the blank form. The view creates an unbound form.

POST means the browser submitted values. The view binds the submitted values to the form using request.POST.

### 8.2 Bound and unbound forms

Bound form:

~~~python
form = EmployeeForm(request.POST)
~~~

A bound form contains submitted data. Django can validate it and redisplay submitted values and errors.

Unbound form:

~~~python
form = EmployeeForm()
~~~

An unbound form has no submitted data and is used to display a blank form.

### 8.3 Why call is_valid()?

is_valid() runs validation and returns True or False. Do not call save() before checking it.

### 8.4 What does save() do?

Because EmployeeForm is a ModelForm, save() creates an Employee database row from validated values.

### 8.5 Why redirect after save?

This follows Post/Redirect/Get:

~~~text
POST form -> Save record -> Redirect response -> New GET -> Employee list
~~~

Refreshing the list page repeats a GET rather than resubmitting the original form POST.

### 8.6 What if validation fails?

The form remains bound. The final render() displays the same submitted values and errors. Do not redirect after invalid submission, because the bound form and its errors would be lost.

## 9. Step 4 — Employee detail view (READ one)

Add:

~~~python
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(
        request,
        "profiles/employee_detail.html",
        {"employee": employee},
    )
~~~

### 9.1 What is pk?

Every Django model has a primary key unless configured otherwise. Django normally creates an integer primary key automatically.

Example:

| id | employee_code | full_name |
|---:|---|---|
| 1 | EMP101 | Asha Rao |
| 2 | EMP102 | Ravi Kumar |

The URL parameter pk identifies the primary key. It is not necessarily the same as employee_code.

### 9.2 Why get_object_or_404()?

Employee.objects.get(pk=pk) raises Employee.DoesNotExist when no row matches. get_object_or_404(Employee, pk=pk) returns the object or an HTTP 404 response. This is useful for browser pages.

Three examples:

~~~python
employee = get_object_or_404(Employee, pk=1)
employee = get_object_or_404(Employee, employee_code="EMP101")
employee = get_object_or_404(Employee, email="asha@example.com")
~~~

Each example retrieves one employee using a different lookup field. The lookup field should uniquely identify one record.

## 10. Step 5 — Employee update view (UPDATE)

Add:

~~~python
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "profiles/employee_form.html",
        {
            "form": form,
            "page_title": "Update Employee",
            "employee": employee,
        },
    )
~~~

### 10.1 Understand the update flow

1. The URL provides a primary key.
2. Django retrieves the matching Employee.
3. On GET, the form receives instance=employee and displays current values.
4. On POST, the form receives submitted values and the existing instance.
5. If valid, save() updates that row.
6. The browser is redirected to the list.

### 10.2 Why instance=employee is necessary

Create a new employee:

~~~python
form = EmployeeForm(request.POST)
~~~

Update an existing employee:

~~~python
form = EmployeeForm(request.POST, instance=employee)
~~~

The second form is connected to an existing object. If you forget instance=employee, Django may create a new Employee instead of updating the selected one.

### 10.3 Verify update behavior

Before editing, note the employee's primary key and employee_code. Change only the name or salary. Submit the form.

Expected:
- The same primary key remains.
- The changed value is visible.
- The employee count has not increased.

If the count increases, inspect whether instance=employee is present in the POST form.

## 11. Step 6 — Delete safely (DELETE)

Add:

~~~python
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return render(
        request,
        "profiles/employee_confirm_delete.html",
        {"employee": employee},
    )
~~~

### 11.1 Why does GET not delete?

GET is intended to retrieve a page. Browsers, crawlers, previews and link checkers may follow GET links automatically. If opening a URL deletes a record, an accidental visit can destroy data.

Therefore:
- GET displays the confirmation page.
- POST performs the deletion after confirmation.
- The HTML form includes a CSRF token.

### 11.2 Safe delete journey

~~~text
GET delete URL
    |
    v
Confirmation page
    |
    +-- Cancel --> Employee list
    |
    +-- Confirm (POST + CSRF token)
                 |
                 v
            employee.delete()
                 |
                 v
            Redirect to list
~~~

### 11.3 Use only a test employee

Create a clearly marked test employee and use it for deletion practice. Do not use production or shared data. Deletion is a real database change.

## 12. Step 7 — Connect URL patterns

Open profiles/urls.py. Preserve the Student routes from Day 41 and add the Employee routes.

~~~python
from django.urls import path
from . import views

urlpatterns = [
    # Keep your existing Student routes here.

    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_create, name="employee_create"),
    path("employees/<int:pk>/", views.employee_detail, name="employee_detail"),
    path("employees/<int:pk>/edit/", views.employee_update, name="employee_update"),
    path("employees/<int:pk>/delete/", views.employee_delete, name="employee_delete"),
]
~~~

### 12.1 Route table

| URL | View | Purpose |
|---|---|---|
| /employees/ | employee_list | List all employees |
| /employees/add/ | employee_create | Display and process create form |
| /employees/1/ | employee_detail | Display employee with pk 1 |
| /employees/1/edit/ | employee_update | Display and process edit form |
| /employees/1/delete/ | employee_delete | Confirm and process delete |

### 12.2 Understand the integer path converter

<int:pk> captures an integer from the URL and passes it to the view as pk. The parameter name in the URL pattern and the view must match.

Correct:

~~~python
path("employees/<int:pk>/edit/", views.employee_update)
def employee_update(request, pk):
    ...
~~~

Incorrect:

~~~python
path("employees/<int:id>/edit/", views.employee_update)
def employee_update(request, pk):
    ...
~~~

The names are inconsistent.

## 13. Step 8 — Create the templates

Create this folder if it does not exist:

~~~text
profiles/
└── templates/
    └── profiles/
        ├── employee_list.html
        ├── employee_form.html
        ├── employee_detail.html
        └── employee_confirm_delete.html
~~~

### 13.1 Employee list template

Create profiles/templates/profiles/employee_list.html:

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Employee Directory</title>
</head>
<body>
    <h1>Employee Directory</h1>
    <p><a href="{% url 'employee_create' %}">Add employee</a></p>

    {% if employees %}
        <table border="1" cellpadding="8">
            <thead>
                <tr>
                    <th>Code</th><th>Name</th><th>Email</th>
                    <th>Salary</th><th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for employee in employees %}
                    <tr>
                        <td>{{ employee.employee_code }}</td>
                        <td>{{ employee.full_name }}</td>
                        <td>{{ employee.email }}</td>
                        <td>{{ employee.salary }}</td>
                        <td>
                            <a href="{% url 'employee_detail' employee.pk %}">View</a>
                            <a href="{% url 'employee_update' employee.pk %}">Edit</a>
                            <a href="{% url 'employee_delete' employee.pk %}">Delete</a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>No employees found. Add the first employee.</p>
    {% endif %}
</body>
</html>
~~~

The Delete link opens the confirmation page using GET. It does not delete the record.

### 13.2 Employee form template

Create profiles/templates/profiles/employee_form.html:

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>{{ page_title }}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.non_field_errors }}

        {% for field in form %}
            <p>
                {{ field.label_tag }}
                {{ field }}
                {{ field.errors }}
            </p>
        {% endfor %}

        <button type="submit">Save employee</button>
    </form>
    <p><a href="{% url 'employee_list' %}">Cancel</a></p>
</body>
</html>
~~~

### 13.3 Employee detail template

Create profiles/templates/profiles/employee_detail.html:

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Employee Details</title>
</head>
<body>
    <h1>{{ employee.full_name }}</h1>
    <dl>
        <dt>Employee code</dt><dd>{{ employee.employee_code }}</dd>
        <dt>Email</dt><dd>{{ employee.email }}</dd>
        <dt>Salary</dt><dd>{{ employee.salary }}</dd>
        <dt>Joining date</dt><dd>{{ employee.joining_date }}</dd>
        <dt>Active</dt><dd>{{ employee.is_active }}</dd>
    </dl>
    <a href="{% url 'employee_update' employee.pk %}">Edit</a>
    <a href="{% url 'employee_list' %}">Back to employees</a>
</body>
</html>
~~~

### 13.4 Delete confirmation template

Create profiles/templates/profiles/employee_confirm_delete.html:

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Confirm Employee Deletion</title>
</head>
<body>
    <h1>Delete employee?</h1>
    <p>
        You are about to delete
        <strong>{{ employee.employee_code }} — {{ employee.full_name }}</strong>.
    </p>
    <p>This action cannot be undone from this page.</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete employee</button>
    </form>

    <a href="{% url 'employee_list' %}">Cancel</a>
</body>
</html>
~~~

### 13.5 Why csrf_token is required

Django's CSRF protection checks that a browser form submission is associated with a page generated by your application. The template tag inserts the token into the form.

For internal POST forms, include {% csrf_token %}. Do not remove CSRF middleware to make a form work. Fix the template and request instead.

## 14. Step 9 — Check the root URL configuration

Open config/urls.py. Preserve the admin route and include the app routes.

~~~python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
]
~~~

Merge these entries into the existing urlpatterns. Do not create a second list that overwrites the earlier routes.

## 15. Step 10 — Run the application

Run from the folder containing manage.py:

~~~powershell
python manage.py check
python manage.py showmigrations
python manage.py migrate
python manage.py runserver
~~~

Open:

http://127.0.0.1:8000/employees/

Expected first observation when there are no Employee rows:

~~~text
Employee Directory
Add employee
No employees found. Add the first employee.
~~~

If earlier exercises created employees, the table should show them.

**Migration note:** Today's lesson adds a form, views, URLs and templates. It does not add or change model fields. Normally, no new migration is required. Do not run makemigrations just because you added a view or template.

## 16. Step 11 — Test Create

Open /employees/, select Add employee and enter unique test data.

| Field | Example |
|---|---|
| Employee code | EMP901 |
| Full name | Asha Rao |
| Email | asha.rao901@example.com |
| Salary | 45000.00 |
| Joining date | 2026-01-15 |
| Is active | Checked |

Select Save employee.

Expected:
- The browser returns to the employee directory.
- One employee with code EMP901 appears.

If you repeat the exercise, choose a new code and email because both fields are unique.

### Invalid create tests

Try:
- Invalid email such as asha.example.com.
- Empty required field.
- Existing employee code.
- Existing email.
- Text where decimal salary is expected.

Expected: the bound form is redisplayed with errors. No invalid record is saved.

## 17. Step 12 — Test Read

Open /employees/ and verify that the directory lists Employee records.

Select View for EMP901. The detail page should show its code, name, email, salary, joining date and active status.

Test a missing primary key:

http://127.0.0.1:8000/employees/999999/

Expected: HTTP 404. This is correct when the requested record does not exist.

## 18. Step 13 — Test Update

1. Return to the employee list.
2. Select Edit for EMP901.
3. Confirm the form is pre-filled.
4. Change the name to Asha Rao Kumar.
5. Submit the form.
6. Return to the directory.

Expected:
- The name changes.
- Employee code remains EMP901.
- The primary key remains unchanged.
- Employee count remains unchanged.

Test an invalid email update. The form should show an error and the database should retain the previous valid email.

**Common update bug:** If a second row is created, inspect both GET and POST forms. Both must receive instance=employee.

## 19. Step 14 — Test Delete

Use only a test employee.

1. Select Delete for the test employee.
2. Confirm that a confirmation page appears.
3. Select Cancel. The employee must still exist.
4. Open the confirmation page again.
5. Select Yes, delete employee.
6. Confirm that the browser returns to the list and the test employee is absent.

Verify in Django shell:

~~~powershell
python manage.py shell
~~~

~~~python
from profiles.models import Employee
Employee.objects.filter(employee_code="EMP901").exists()
~~~

Expected after deletion:

~~~text
False
~~~

This confirms that no Employee with that code remains.

## 20. Complete request-response flow

### Create

~~~text
Browser GET /employees/add/
       |
       v
employee_create()
       |
       v
EmployeeForm() — blank form
       |
       v
employee_form.html
       |
       v
Browser displays form

Browser POST form data
       |
       v
EmployeeForm(request.POST)
       |
       v
form.is_valid()
       |
       +-- Invalid --> Render form with errors
       |
       +-- Valid --> form.save()
                         |
                         v
                    Database INSERT
                         |
                         v
                    redirect()
                         |
                         v
                    Employee list
~~~

### Update

~~~text
GET edit URL -> Retrieve employee -> EmployeeForm(instance=employee)
     -> Pre-filled form -> POST -> Validate -> save()
     -> Database UPDATE -> Redirect
~~~

### Delete

~~~text
GET delete URL -> Retrieve employee -> Confirmation page
     -> POST + CSRF token -> employee.delete()
     -> Database DELETE -> Redirect
~~~

## 21. Important methods

| Method / attribute | Purpose | Example |
|---|---|---|
| objects.all() | Query all rows | Employee.objects.all() |
| order_by() | Sort records | order_by("full_name") |
| get_object_or_404() | Get object or return 404 | get_object_or_404(Employee, pk=pk) |
| request.method | Check HTTP method | request.method == "POST" |
| request.POST | Read submitted data | EmployeeForm(request.POST) |
| is_valid() | Validate form | form.is_valid() |
| save() | Create or update row | form.save() |
| redirect() | Return redirect response | redirect("employee_list") |
| render() | Render template | render(request, template, context) |
| delete() | Delete model instance | employee.delete() |

Remember:
- Employee.objects.all() returns a QuerySet.
- get_object_or_404() returns one model instance.
- employee.delete() deletes one instance.
- QuerySet.delete() can delete multiple matching rows. Do not use bulk deletion casually.

## 22. Common errors and troubleshooting

| Symptom | Likely reason | What to do |
|---|---|---|
| TemplateDoesNotExist | Wrong folder or filename | Check profiles/templates/profiles/ and exact spelling |
| NoReverseMatch | URL name or pk argument is wrong | Compare URL names with redirect() and {% url %} |
| NameError: EmployeeForm | Form not imported | Import EmployeeForm from profiles.forms |
| ImportError: Employee | Model name or import is wrong | Check profiles/models.py |
| IntegrityError | Duplicate unique code or email | Use unique test values and display validation errors |
| DoesNotExist | Direct get() found no row | Use get_object_or_404() for browser views |
| 404 | Missing primary key or wrong route | Confirm record ID and URL pattern |
| Form not pre-filled | Missing instance on GET | Use EmployeeForm(instance=employee) |
| Update creates new row | Missing instance on POST | Use EmployeeForm(request.POST, instance=employee) |
| CSRF failure | Missing token or cookie issue | Keep middleware, add token and reload form |
| Delete does not happen on link click | Link opens confirmation GET | Submit the confirmation form using POST |
| Delete happens on GET | Destructive GET design | Make GET show confirmation and POST delete |
| no such table | Migrations not applied or wrong DB | Check settings and showmigrations, then migrate |
| Syntax/import error | Typo or code in wrong file | Read final traceback line and inspect named file |

### Debugging routine

1. Read the final error line in the terminal.
2. Identify the file and line number.
3. Check spelling of the imported class or function.
4. Check URL name and path parameter.
5. Check template path.
6. Run python manage.py check.
7. Repeat only the action that failed.

Do not randomly change multiple files at once.

## 23. Practical exercises

### Exercise 1 — Newest employees first

Display newest employees first.

Hint: use order_by() and a minus prefix.

~~~python
Employee.objects.order_by("-created_at")
~~~

### Exercise 2 — Active employees only

Update the list view to show active employees only.

~~~python
Employee.objects.filter(is_active=True).order_by("full_name")
~~~

### Exercise 3 — Add salary

Add salary to the list table and verify the DecimalField value.

### Exercise 4 — Add a Back link

Add a link on the detail page to return to the employee directory.

### Exercise 5 — Avoid duplicate test records

Before creating EMP901, check whether it already exists. Explain why the unique constraint is useful.

### Exercise 6 — Explain the difference

Explain why create uses EmployeeForm(request.POST) while update uses EmployeeForm(request.POST, instance=employee).

## 24. Independent mini-project — Employee CRUD Application

### Business requirement

A small company needs an internal employee directory. A user should be able to add, view, edit and remove employee records.

### Required fields

Use the existing Employee model:
- Employee code
- Full name
- Email
- Salary
- Joining date
- Active status

### Required pages

| Page | Required behavior |
|---|---|
| Employee list | Show employees and an Add link |
| Employee create | Blank form, validate and save |
| Employee detail | Show one employee |
| Employee update | Show existing values and save changes |
| Employee delete confirmation | Ask for confirmation; delete only after POST |

### Technical rules

1. Use the existing Employee model.
2. Use a Django ModelForm.
3. Use named URL patterns.
4. Use get_object_or_404() for single-record pages.
5. Use server-side validation.
6. Include CSRF tokens in POST forms.
7. Redirect after successful create, update and delete.
8. Never delete on GET.
9. Preserve Student views and forms from Phase 3.
10. Do not add authentication code before the authentication lessons.

### Acceptance tests

- [ ] Employee list page loads.
- [ ] Empty state appears when no records exist.
- [ ] A valid employee can be created.
- [ ] Invalid email is rejected.
- [ ] Duplicate employee code is rejected.
- [ ] Duplicate email is rejected.
- [ ] Detail page displays the correct employee.
- [ ] Missing primary key returns 404.
- [ ] Edit page is pre-filled.
- [ ] Update changes the existing row, not a new row.
- [ ] Delete page does not delete on GET.
- [ ] Cancel leaves the record unchanged.
- [ ] Confirmed POST deletes the test employee.
- [ ] Student routes from Day 41 still work.

### Evidence to submit

- Screenshot of employee list.
- Screenshot of create form.
- Screenshot of detail page.
- Screenshot of update form with existing values.
- Screenshot of delete confirmation.
- Terminal output from python manage.py check.
- Short README explaining routes and CRUD flow.
- One error encountered and how you solved it.

## 25. Knowledge check — answer before reading

1. What does CRUD stand for?
2. Which ORM method returns all employee rows?
3. What is a ModelForm?
4. What is the difference between a bound and unbound form?
5. Why call is_valid() before save()?
6. What does instance=employee do?
7. Why use get_object_or_404()?
8. What does <int:pk> do?
9. Why should deletion not run on GET?
10. What does the CSRF template tag do?
11. Why redirect after successful POST?
12. Why exclude created_at from EmployeeForm?
13. What does unique=True protect?
14. What should happen when a form is invalid?
15. How do you confirm an update changed the same row?

### Answer key

1. Create, Read, Update and Delete.
2. Employee.objects.all().
3. A form connected to a Django model that can validate and save model data.
4. A bound form contains submitted data; an unbound form is blank.
5. To validate submitted data before saving.
6. It connects the form to an existing model instance so save updates it.
7. It returns the object or an HTTP 404 response if missing.
8. It captures an integer from the URL and passes it to the view as pk.
9. GET should retrieve a page and may be triggered accidentally by browsers or crawlers.
10. It inserts the CSRF token required by Django's CSRF protection.
11. It follows Post/Redirect/Get and avoids accidental repeated form submission on refresh.
12. Django sets it automatically when the object is created.
13. It prevents duplicate values in that database field.
14. Re-render the bound form with errors and do not save.
15. Compare primary key before and after; it should remain the same.

## 26. Five MCQs with explanations

### Q1. Which operation adds a new employee record?

A. Read  
B. Create  
C. Update  
D. Delete

**Correct answer: B — Create.** Create inserts a new record into the database.

### Q2. What does EmployeeForm(request.POST, instance=employee) do after valid submission?

A. Creates a second employee  
B. Deletes the employee  
C. Updates the supplied employee instance  
D. Returns 404

**Correct answer: C — Updates the supplied employee instance.** The instance argument connects submitted values to an existing object.

### Q3. Which method retrieves one object or returns HTTP 404?

A. render()  
B. redirect()  
C. get_object_or_404()  
D. order_by()

**Correct answer: C — get_object_or_404().** It handles the missing-object case as a 404 response.

### Q4. Why should deletion use POST?

A. POST makes the page colorful  
B. GET should not perform destructive state changes  
C. POST removes validation  
D. GET cannot display templates

**Correct answer: B.** GET requests may be triggered unintentionally. Use a confirmation form with POST and CSRF protection.

### Q5. What should happen when is_valid() returns False?

A. Save anyway  
B. Delete the record  
C. Re-render the bound form with errors  
D. Show a blank form

**Correct answer: C.** The learner must see what needs correction, and invalid data must not be saved.

## 27. Interview preparation

Be ready to explain aloud:
1. What is CRUD in Django?
2. How do you create a record using a ModelForm?
3. How does Django distinguish create from update?
4. What is the purpose of instance in a ModelForm?
5. What is the difference between get() and get_object_or_404()?
6. Why should delete use POST?
7. What is CSRF protection?
8. Why redirect after successful POST?
9. How do you handle duplicate unique values?
10. How would you debug an update that creates a duplicate row?

Use the separate Day 42 interview guide for model answers and scenario practice.

## 28. Completion checklist

Do not mark Day 42 complete just because you read the notes.

- [ ] I understand Create, Read, Update and Delete.
- [ ] I confirmed the existing Employee model.
- [ ] I added EmployeeForm without breaking StudentRegistrationForm.
- [ ] I created list, create, detail, update and delete views.
- [ ] I added named URL patterns.
- [ ] I created all four templates.
- [ ] I ran the Django system check.
- [ ] I created a test employee.
- [ ] I displayed an employee detail page.
- [ ] I updated an existing employee without creating a duplicate.
- [ ] I tested an invalid form.
- [ ] I confirmed GET does not delete an employee.
- [ ] I deleted only a test employee through POST.
- [ ] I verified the database state.
- [ ] I completed the independent mini-project.
- [ ] I can explain the request-response flow without reading the notes.

If you cannot complete a checkpoint, return to the named section. Re-read the explanation, compare your file, run the command and inspect the expected result. Record the exact error. Do not skip the problem and move to Day 43.

## 29. Connection to Day 43

Today you built the four basic operations using Django views and ModelForms. Day 43 expands the Read side of CRUD. You will learn to search, filter, exclude, retrieve, sort and select fields using advanced Django ORM queries.

~~~text
Day 42: CRUD
  +-- Create
  +-- Read
  +-- Update
  +-- Delete
        |
        v
Day 43: Advanced ORM
  +-- filter()
  +-- exclude()
  +-- get()
  +-- order_by()
  +-- values()
~~~

**Day 42 is complete only when your Employee CRUD Application works and you can explain why each file is needed.**
