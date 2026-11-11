# Day 42: Interview Guide — CRUD Operations: Create, Read, Update and Delete

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 42 class notes](day_42_notes.md)  
**Approved mini-project:** Employee CRUD Application

> Use this guide after completing the class notes and building the project. Try answering aloud before reading the model answer. Interview readiness means you can explain and demonstrate the code, not memorize definitions.

---

## 1. Core concepts

### Q1. What is CRUD?

**Model answer:** CRUD stands for Create, Read, Update and Delete. These are the four basic operations performed on persistent data. In a Django employee application, Create adds an employee, Read displays employee records, Update changes an existing employee and Delete removes an employee record.

**Follow-up:** Which CRUD operation is performed by Employee.objects.all()?

**Answer:** Read. It builds a QuerySet for retrieving Employee records.

### Q2. How do you create a database record using a Django ModelForm?

**Model answer:** I create a ModelForm connected to the Employee model. In the view, I bind submitted data using EmployeeForm(request.POST). I call is_valid() to validate the data. If it is valid, I call form.save() to create the database record. Then I redirect the browser to the employee list.

### Q3. What is the difference between a bound form and an unbound form?

**Model answer:** A bound form has submitted data attached to it, for example EmployeeForm(request.POST). Django validates that data and can display submitted values and errors. An unbound form, such as EmployeeForm(), has no submitted data and is normally used to display a blank form.

### Q4. How does a ModelForm know which model to save?

**Model answer:** Its inner Meta class declares model = Employee. The fields list identifies which model fields are included. After successful validation, form.save() creates or updates an Employee instance depending on whether an existing instance was supplied.

### Q5. How do you update an existing record using a ModelForm?

**Model answer:** First, I retrieve the existing object, usually with get_object_or_404(Employee, pk=pk). For GET, I create EmployeeForm(instance=employee) so current values are displayed. For POST, I use EmployeeForm(request.POST, instance=employee). If valid, form.save() updates that same object.

### Q6. What happens if you forget instance=employee during an update?

**Model answer:** The ModelForm is no longer connected to the existing Employee object. A valid submission may create a new row instead of updating the selected employee. I verify this by checking whether the primary key and total record count remain unchanged after an update.

### Q7. What is the difference between get() and get_object_or_404()?

**Model answer:** get() returns one matching object but raises the model's DoesNotExist exception if no record is found. get_object_or_404() returns the object or converts the missing-object case into an HTTP 404 response, which is useful in browser views.

### Q8. Why use named URL patterns?

**Model answer:** Named URL patterns allow Django to reverse a URL by its name using redirect() or the template url tag. This reduces hardcoded paths and makes route changes easier to maintain.

### Q9. Why should a delete operation not be triggered by GET?

**Model answer:** GET is intended to retrieve information and may be triggered by crawlers, previews or accidental link visits. A destructive operation should require a POST request from a confirmation form, with CSRF protection enabled.

### Q10. What is the Post/Redirect/Get pattern?

**Model answer:** After a successful POST, the view returns a redirect. The browser then makes a new GET request. This helps prevent the user from repeating the original form submission when refreshing the result page.

---

## 2. Code-reading questions

### Q11. Explain this code.

~~~python
employees = Employee.objects.order_by("full_name")
~~~

**Model answer:** Employee.objects accesses the model manager. order_by("full_name") creates a QuerySet ordered by full_name in ascending order. The QuerySet can be passed to a template and evaluated when it is iterated.

### Q12. Explain this code.

~~~python
employee = get_object_or_404(Employee, pk=pk)
~~~

**Model answer:** Django looks for an Employee whose primary key matches the URL parameter. If it exists, the view receives the Employee instance. If it does not exist, Django returns an HTTP 404 response.

### Q13. Explain this code.

~~~python
if request.method == "POST":
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
~~~

**Model answer:** The view checks whether the request submitted data using POST. It binds that data to EmployeeForm. If validation succeeds, the ModelForm saves a new Employee record and the browser is redirected to the employee list. If validation fails, the view should render the bound form with errors.

### Q14. What does {% csrf_token %} do?

**Model answer:** It inserts a CSRF token into the HTML form. Django's CSRF middleware checks the token on protected requests such as POST. It is an important part of protecting browser-based form submissions against cross-site request forgery.

### Q15. Why exclude created_at from EmployeeForm?

**Model answer:** The Employee model uses auto_now_add=True for created_at. Django sets the timestamp when the object is created. A user should not manually supply or change this internal creation timestamp through the form.

---

## 3. Scenario-based questions

### Q16. An edit form creates a new employee instead of updating the selected employee. What do you inspect?

**Model answer:**
1. Inspect the employee update view.
2. Confirm the selected employee is retrieved using the URL primary key.
3. Confirm GET uses EmployeeForm(instance=employee).
4. Confirm POST uses EmployeeForm(request.POST, instance=employee).
5. Submit a test update.
6. Compare the primary key and record count before and after.

The likely cause is a missing instance=employee argument in the POST form.

### Q17. A user opens a delete URL and the employee is immediately removed. What is wrong?

**Model answer:** The view is performing a destructive operation on GET. I change the flow so GET retrieves the employee and renders a confirmation page. The confirmation form submits POST with a CSRF token. Only POST calls employee.delete().

### Q18. A duplicate employee code causes an IntegrityError. How should the application handle it?

**Model answer:** The model's unique constraint is protecting data integrity. The form should validate uniqueness and display a useful field error. I should not remove the unique constraint to hide the error. I would test the duplicate case and verify that the existing record remains unchanged.

### Q19. A detail URL returns 404. Is this always a bug?

**Model answer:** No. If the primary key does not exist, a 404 is the correct result. I check whether the ID exists and whether the route passes the correct primary key. If the record exists but the page still returns 404, I inspect the URL pattern and lookup condition.

### Q20. The list page shows no employees after a successful create. How do you debug it?

**Model answer:**
1. Check whether the form was valid.
2. Confirm the save line was reached.
3. Check whether the browser was redirected to the correct named route.
4. Inspect the list view's QuerySet.
5. Confirm the template uses the same context key passed by the view.
6. Confirm the application is using the expected database.
7. Query the record in Django shell.

I would identify the first point where observed behavior differs from expected behavior.

### Q21. Why is client-side validation not enough?

**Model answer:** Browser validation can be bypassed by sending a request directly. Server-side validation is required because the backend is responsible for accepting or rejecting data. Django forms and model/database constraints provide validation and integrity checks on the server.

---

## 4. Practical coding round

### Task 1 — Create a list view

**Requirement:** Display all employees ordered by full name.

**Expected core code:**

~~~python
def employee_list(request):
    employees = Employee.objects.order_by("full_name")
    return render(
        request,
        "profiles/employee_list.html",
        {"employees": employees},
    )
~~~

**What to explain:** QuerySet, ordering, context dictionary and template rendering.

### Task 2 — Create an employee

**Requirement:** Accept form input, validate it and save a new record.

**Expected core code:**

~~~python
if request.method == "POST":
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
else:
    form = EmployeeForm()
~~~

**What to explain:** GET versus POST, bound versus unbound form, validation and redirect.

### Task 3 — Update an employee

**Requirement:** Edit the employee identified by the URL primary key.

**Expected core code:**

~~~python
employee = get_object_or_404(Employee, pk=pk)
form = EmployeeForm(request.POST, instance=employee)
if request.method == "POST" and form.is_valid():
    form.save()
    return redirect("employee_list")
~~~

**What to explain:** Existing instance and why the update does not create another row.

### Task 4 — Delete an employee safely

**Requirement:** Display a confirmation page and delete only on POST.

**Expected core code:**

~~~python
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

**What to explain:** Safe HTTP method semantics, confirmation, CSRF token and destructive action.

---

## 5. Mini-project viva — Employee CRUD Application

### Q22. What business problem does your project solve?

**Suggested answer structure:** It provides a simple employee directory where records can be created, viewed, edited and removed. The database stores employee details, Django views coordinate each operation, ModelForms validate input and templates provide the browser interface.

### Q23. Which files did you create or update?

| File | Responsibility |
|---|---|
| profiles/models.py | Existing Employee database model |
| profiles/forms.py | EmployeeForm |
| profiles/views.py | CRUD view functions |
| profiles/urls.py | Named route definitions |
| employee_list.html | Employee directory |
| employee_form.html | Create/update form |
| employee_detail.html | One employee's details |
| employee_confirm_delete.html | Delete confirmation |
| config/urls.py | Includes app URL configuration |

### Q24. How did you verify Create?

**Expected answer:** I submitted a valid employee and checked that it appeared in the list and database. I also submitted invalid data and confirmed that it was rejected.

### Q25. How did you verify Update?

**Expected answer:** I recorded the primary key before editing, changed a field and submitted the form. The same primary key remained and the record count did not increase.

### Q26. How did you verify Delete?

**Expected answer:** I opened the confirmation page and cancelled first to confirm GET did not delete the record. Then I submitted the POST form and checked that the test record no longer existed.

### Q27. What security limitation remains?

**Expected answer:** The lesson demonstrates CRUD mechanics but does not yet restrict operations to authenticated users or authorized roles. Authentication and permissions are addressed in later Phase 4 lessons. The local exercise must not be exposed publicly as a production employee-management system.

---

## 6. Common mistakes

| Mistake | Correct understanding |
|---|---|
| Calling save before is_valid | Validate before saving |
| Forgetting instance during update | Supply the existing object to the ModelForm |
| Deleting on GET | Use confirmation page and POST |
| Removing CSRF middleware to fix a form | Keep protection and add the token correctly |
| Hardcoding redirect paths everywhere | Prefer named URL reversing |
| Including internal fields in a public form | Use an explicit fields allow-list |
| Treating 404 as always a failure | Missing records should return 404 |
| Testing delete on real data | Use a dedicated test record |

---

## 7. Self-assessment

| Skill | Not yet | With notes | Independently |
|---|---:|---:|---:|
| Explain CRUD | [ ] | [ ] | [ ] |
| Build a ModelForm | [ ] | [ ] | [ ] |
| Create and list records | [ ] | [ ] | [ ] |
| Retrieve one record safely | [ ] | [ ] | [ ] |
| Update without duplicate rows | [ ] | [ ] | [ ] |
| Delete only through POST | [ ] | [ ] | [ ] |
| Debug a form or URL error | [ ] | [ ] | [ ] |
| Demonstrate the project | [ ] | [ ] | [ ] |

**Readiness rule:** You are ready to move on when you can complete the CRUD demonstration from a fresh server start, explain the important lines and show evidence that each operation changed or read the expected database record.

## 8. Five-minute revision

- CRUD means Create, Read, Update and Delete.
- A ModelForm connects form fields to a model.
- is_valid() validates submitted data.
- save() creates or updates the model instance.
- instance=employee is essential for updating an existing object.
- get_object_or_404() handles missing records with HTTP 404.
- GET displays pages; POST submits changes.
- A delete action should require POST and CSRF protection.
- Named URLs make redirects and template links maintainable.
- Always verify the actual database state.

**Final instruction:** Demonstrate the Employee CRUD Application using your own code. If you cannot explain a line or reproduce a result, revisit the matching section in [Day 42 class notes](day_42_notes.md).
