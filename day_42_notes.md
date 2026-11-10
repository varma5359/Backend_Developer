# Day 42: CRUD Operations: Create, Read, Update and Delete

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–43 — Django fundamentals, models, forms and ORM basics  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Employee CRUD Application

> **Trainer guidance:** Explain the database effect of every operation. Ask students to verify records before and after each action. Never demonstrate destructive operations on important data.

## 1. Learning objectives

- Explain crud operations: create, read, update and delete.
- Identify the ORM or view methods involved.
- Implement the example step by step.
- Explain the database result.
- Test normal, invalid and missing-record cases.
- Complete Employee CRUD Application.

## 2. Concept introduction

CRUD describes the four basic operations performed on stored records. Django views and forms can create a record, retrieve records, update an existing record and delete a record. A record should be identified using a stable primary key, and delete operations should be protected by authentication and authorization.

## 3. File-by-file or shell implementation

### profiles/views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "profiles/employee_list.html", {"employees": employees})

def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "profiles/employee_form.html", {"form": form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "profiles/employee_form.html", {"form": form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request, "profiles/employee_confirm_delete.html", {"employee": employee})
```

### profiles/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_create, name="employee_create"),
    path("employees/<int:pk>/edit/", views.employee_update, name="employee_update"),
    path("employees/<int:pk>/delete/", views.employee_delete, name="employee_delete"),
]
```

## 4. Understand the code

### profiles/views.py

1. `from django.shortcuts import render, redirect, get_object_or_404` — Imports Django helpers or the model.
2. `from .models import Employee` — Imports Django helpers or the model.
3. `from .forms import EmployeeForm` — Imports Django helpers or the model.
4. ` ` — Part of the example; explain its role in the complete workflow.
5. `def employee_list(request):` — Defines a view function.
6. `    employees = Employee.objects.all()` — Builds or evaluates a database query.
7. `    return render(request, "profiles/employee_list.html", {"employees": employees})` — Part of the example; explain its role in the complete workflow.
8. ` ` — Part of the example; explain its role in the complete workflow.
9. `def employee_create(request):` — Defines a view function.
10. `    form = EmployeeForm(request.POST or None)` — Part of the example; explain its role in the complete workflow.
11. `    if request.method == "POST" and form.is_valid():` — Part of the example; explain its role in the complete workflow.
12. `        form.save()` — Persists a validated model form.
13. `        return redirect("employee_list")` — Part of the example; explain its role in the complete workflow.
14. `    return render(request, "profiles/employee_form.html", {"form": form})` — Part of the example; explain its role in the complete workflow.
15. ` ` — Part of the example; explain its role in the complete workflow.
16. `def employee_update(request, pk):` — Defines a view function.
17. `    employee = get_object_or_404(Employee, pk=pk)` — Retrieves a record or returns an HTTP 404 response.
18. `    form = EmployeeForm(request.POST or None, instance=employee)` — Part of the example; explain its role in the complete workflow.
19. `    if request.method == "POST" and form.is_valid():` — Part of the example; explain its role in the complete workflow.
20. `        form.save()` — Persists a validated model form.
21. `        return redirect("employee_list")` — Part of the example; explain its role in the complete workflow.
22. `    return render(request, "profiles/employee_form.html", {"form": form})` — Part of the example; explain its role in the complete workflow.
23. ` ` — Part of the example; explain its role in the complete workflow.
24. `def employee_delete(request, pk):` — Defines a view function.
25. `    employee = get_object_or_404(Employee, pk=pk)` — Retrieves a record or returns an HTTP 404 response.
26. `    if request.method == "POST":` — Part of the example; explain its role in the complete workflow.
27. `        employee.delete()` — Part of the example; explain its role in the complete workflow.
28. `        return redirect("employee_list")` — Part of the example; explain its role in the complete workflow.
29. `    return render(request, "profiles/employee_confirm_delete.html", {"employee": employee})` — Part of the example; explain its role in the complete workflow.

### profiles/urls.py

1. `from django.urls import path` — Imports Django helpers or the model.
2. `from . import views` — Imports Django helpers or the model.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `urlpatterns = [` — Part of the example; explain its role in the complete workflow.
5. `    path("employees/", views.employee_list, name="employee_list"),` — Connects a URL pattern to a view.
6. `    path("employees/add/", views.employee_create, name="employee_create"),` — Connects a URL pattern to a view.
7. `    path("employees/<int:pk>/edit/", views.employee_update, name="employee_update"),` — Connects a URL pattern to a view.
8. `    path("employees/<int:pk>/delete/", views.employee_delete, name="employee_delete"),` — Connects a URL pattern to a view.
9. `]` — Part of the example; explain its role in the complete workflow.

## 5. Verify database behavior

1. Start from known sample records.
2. Execute one operation at a time.
3. Inspect the database or admin interface.
4. Confirm only the intended record changed.
5. Test an invalid or missing ID.
6. Record query output or query count where relevant.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Record not found | Primary key and query conditions |
| Wrong record updated | Instance passed to ModelForm and URL parameter |
| Delete happens on GET | Use POST confirmation for destructive action |
| Query returns too many records | Filter conditions and joins |
| QuerySet not evaluated | Iteration, list(), len() or template rendering |
| N+1 queries | Related-object access inside loops |
| Optimization changes output | Compare data and relationship behavior |

## 7. Industry scenario

CRUD describes the four basic operations performed on stored records. Django views and forms can create a record, retrieve records, update an existing record and delete a record. A record should be identified using a stable primary key, and delete operations should be protected by authentication and authorization.

## 8. Approved mini-project — Employee CRUD Application

**Objective:** Employee CRUD Application.

### Required tasks

1. Create a list view that retrieves employee records.
2. Create a form view for adding an employee.
3. Use get_object_or_404() to retrieve a record for editing.
4. Pass instance=employee to ModelForm so it updates the existing record.
5. Create a delete confirmation page and use POST for deletion.
6. Add URL patterns with an integer primary-key converter.
7. Test create, read, update and delete operations.
8. Verify database state after every operation.

### Suggested structure

```text
projects/day_42/
├── README.md
├── application/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── tests/
```

### Validation checklist

- [ ] Create adds one record.
- [ ] Read displays the saved record.
- [ ] Update changes the selected record only.
- [ ] Delete requires a POST confirmation.
- [ ] A missing primary key returns 404.
- [ ] Unauthenticated or unauthorized users cannot modify protected records.

### Submission evidence

- Source code and URLs.
- Sample database records.
- Browser screenshots or query output.
- Test cases and results.
- README explaining the operation and its risks.
- Query count comparison where relevant.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Employee CRUD Application. Identify the views, ORM methods, URL patterns, test data and validation cases. Do not provide the complete project."

**Guided prompt:** "Help me implement one operation at a time. Explain the database effect and wait for my verification output."

**Debugging prompt:** "Here are my model, view, query and exact result. Explain why the result differs from the expected behavior."

**Review prompt:** "Review correctness, query behavior, access control, error handling and test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Perform or optimize database-backed operations using Django's ORM.  
B. Replace HTTP.  
C. Remove the database.  
D. Disable validation.  
**Answer: A.** Django's ORM provides structured database operations.

**Q2. What should be checked after a database change?**  
A. Only the page title.  
B. Actual database state and affected records.  
C. Only the file name.  
D. Nothing.  
**Answer: B.** Verify the persisted result.

**Q3. Which practice is safest?**  
A. Allow all users to delete any record.  
B. Use GET for destructive changes.  
C. Validate input and protect write operations.  
D. Ignore missing records.  
**Answer: C.** Protect data changes and handle invalid cases.

**Q4. Why inspect query behavior?**  
A. To make code longer.  
B. To avoid using models.  
C. To disable SQL.  
D. To detect unnecessary database queries and preserve correct results.  
**Answer: D.** Query measurement helps target real performance problems.

**Q5. What is the best evidence of completion?**  
A. Verified database behavior and test results.  
B. A folder exists.  
C. A long file.  
D. A screenshot of code only.  
**Answer: A.** Completion requires observable behavior.

## 11. Interview preparation

**Q1. Explain crud operations: create, read, update and delete.**  
**Answer:** CRUD describes the four basic operations performed on stored records. Django views and forms can create a record, retrieve records, update an existing record and delete a record. A record should be identified using a stable primary key, and delete operations should be protected by authentication and authorization.

**Q2. What is one common failure?**  
**Answer:** Create adds one record. Explain how you would reproduce and diagnose it.

**Q3. How do you verify the result?**  
**Answer:** Inspect the database, run the relevant query or view and test normal and invalid cases.

**Follow-up:** What production concern is important?  
**Answer:** Authorization, data integrity, transaction safety and performance must be considered.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Verify database behavior.
- [ ] Test normal and invalid cases.
- [ ] Complete Employee CRUD Application.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 43.
