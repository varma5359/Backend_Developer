# Day 44: Query Optimization Basics: select_related and prefetch_related

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–43 — Django fundamentals, models, forms and ORM basics  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Optimized Order Management System

> **Trainer guidance:** Explain the database effect of every operation. Ask students to verify records before and after each action. Never demonstrate destructive operations on important data.

## 1. Learning objectives

- Explain query optimization basics: select_related and prefetch_related.
- Identify the ORM or view methods involved.
- Implement the example step by step.
- Explain the database result.
- Test normal, invalid and missing-record cases.
- Complete Optimized Order Management System.

## 2. Concept introduction

A page that loops through related objects can accidentally execute one query per row (the N+1 query problem). select_related() uses SQL joins for single-valued relationships such as ForeignKey and OneToOneField. prefetch_related() performs additional queries and joins results in Python, which is useful for many-to-many and reverse relationships.

## 3. File-by-file or shell implementation

### profiles/views.py

```python
from django.shortcuts import render
from .models import Employee

def employee_directory(request):
    employees = (
        Employee.objects
        .select_related("department")
        .order_by("full_name")
    )
    return render(
        request,
        "profiles/employee_directory.html",
        {"employees": employees}
    )
```

### ORM comparison

```python
# May cause repeated queries when accessing a related department
employees = Employee.objects.all()

# Fetch single-valued related department with a SQL join
employees = Employee.objects.select_related("department")

# For a many-to-many or reverse relationship
students = Student.objects.prefetch_related("courses")
```

## 4. Understand the code

### profiles/views.py

1. `from django.shortcuts import render` — Imports Django helpers or the model.
2. `from .models import Employee` — Imports Django helpers or the model.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `def employee_directory(request):` — Defines a view function.
5. `    employees = (` — Part of the example; explain its role in the complete workflow.
6. `        Employee.objects` — Part of the example; explain its role in the complete workflow.
7. `        .select_related("department")` — Fetches a single-valued relation using a SQL join.
8. `        .order_by("full_name")` — Part of the example; explain its role in the complete workflow.
9. `    )` — Part of the example; explain its role in the complete workflow.
10. `    return render(` — Part of the example; explain its role in the complete workflow.
11. `        request,` — Part of the example; explain its role in the complete workflow.
12. `        "profiles/employee_directory.html",` — Part of the example; explain its role in the complete workflow.
13. `        {"employees": employees}` — Part of the example; explain its role in the complete workflow.
14. `    )` — Part of the example; explain its role in the complete workflow.

### ORM comparison

1. `# May cause repeated queries when accessing a related department` — Part of the example; explain its role in the complete workflow.
2. `employees = Employee.objects.all()` — Builds or evaluates a database query.
3. ` ` — Part of the example; explain its role in the complete workflow.
4. `# Fetch single-valued related department with a SQL join` — Part of the example; explain its role in the complete workflow.
5. `employees = Employee.objects.select_related("department")` — Builds or evaluates a database query.
6. ` ` — Part of the example; explain its role in the complete workflow.
7. `# For a many-to-many or reverse relationship` — Part of the example; explain its role in the complete workflow.
8. `students = Student.objects.prefetch_related("courses")` — Builds or evaluates a database query.

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

A page that loops through related objects can accidentally execute one query per row (the N+1 query problem). select_related() uses SQL joins for single-valued relationships such as ForeignKey and OneToOneField. prefetch_related() performs additional queries and joins results in Python, which is useful for many-to-many and reverse relationships.

## 8. Approved mini-project — Optimized Order Management System

**Objective:** Optimized Order Management System.

### Required tasks

1. Identify a page that accesses related objects in a loop.
2. Inspect model relationships to determine whether they are single-valued or multi-valued.
3. Use select_related() for ForeignKey and OneToOneField access.
4. Use prefetch_related() for ManyToManyField and reverse relations.
5. Compare the number of database queries using Django Debug Toolbar or assertNumQueries in tests.
6. Verify that the output is unchanged after optimization.
7. Avoid adding optimization methods without measuring the query behavior.

### Suggested structure

```text
projects/day_44/
├── README.md
├── application/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── tests/
```

### Validation checklist

- [ ] The related fields used in the template are identified.
- [ ] select_related() is used for appropriate single-valued relationships.
- [ ] prefetch_related() is used for multi-valued relationships.
- [ ] Query count is compared before and after.
- [ ] The optimized page returns the same correct data.

### Submission evidence

- Source code and URLs.
- Sample database records.
- Browser screenshots or query output.
- Test cases and results.
- README explaining the operation and its risks.
- Query count comparison where relevant.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Optimized Order Management System. Identify the views, ORM methods, URL patterns, test data and validation cases. Do not provide the complete project."

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

**Q1. Explain query optimization basics: select_related and prefetch_related.**  
**Answer:** A page that loops through related objects can accidentally execute one query per row (the N+1 query problem). select_related() uses SQL joins for single-valued relationships such as ForeignKey and OneToOneField. prefetch_related() performs additional queries and joins results in Python, which is useful for many-to-many and reverse relationships.

**Q2. What is one common failure?**  
**Answer:** The related fields used in the template are identified. Explain how you would reproduce and diagnose it.

**Q3. How do you verify the result?**  
**Answer:** Inspect the database, run the relevant query or view and test normal and invalid cases.

**Follow-up:** What production concern is important?  
**Answer:** Authorization, data integrity, transaction safety and performance must be considered.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Verify database behavior.
- [ ] Test normal and invalid cases.
- [ ] Complete Optimized Order Management System.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 45.
