# Day 43: Advanced Django ORM: filter, exclude, get, order_by and values

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–43 — Django fundamentals, models, forms and ORM basics  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Advanced Product Search

> **Trainer guidance:** Explain the database effect of every operation. Ask students to verify records before and after each action. Never demonstrate destructive operations on important data.

## 1. Learning objectives

- Explain advanced django orm: filter, exclude, get, order_by and values.
- Identify the ORM or view methods involved.
- Implement the example step by step.
- Explain the database result.
- Test normal, invalid and missing-record cases.
- Complete Advanced Product Search.

## 2. Concept introduction

Django ORM QuerySets support filtering, excluding, retrieving one record, sorting and selecting fields. Field lookups such as __icontains, __gte, __in and __range express common query conditions. QuerySets are lazy until evaluated, so developers should understand when database queries actually run.

## 3. File-by-file or shell implementation

### Django shell

```bash
python manage.py shell
```

### Query examples

```python
from profiles.models import Employee

Employee.objects.filter(department="ENG")
Employee.objects.exclude(is_active=False)
Employee.objects.get(employee_code="EMP101")
Employee.objects.filter(full_name__icontains="ash")
Employee.objects.filter(salary__gte=50000)
Employee.objects.filter(department__in=["ENG", "FIN"])
Employee.objects.order_by("-salary", "full_name")
Employee.objects.values("employee_code", "full_name", "salary")
```

## 4. Understand the code

### Django shell

1. `python manage.py shell` — Part of the example; explain its role in the complete workflow.

### Query examples

1. `from profiles.models import Employee` — Imports Django helpers or the model.
2. ` ` — Part of the example; explain its role in the complete workflow.
3. `Employee.objects.filter(department="ENG")` — Builds or evaluates a database query.
4. `Employee.objects.exclude(is_active=False)` — Builds or evaluates a database query.
5. `Employee.objects.get(employee_code="EMP101")` — Builds or evaluates a database query.
6. `Employee.objects.filter(full_name__icontains="ash")` — Builds or evaluates a database query.
7. `Employee.objects.filter(salary__gte=50000)` — Builds or evaluates a database query.
8. `Employee.objects.filter(department__in=["ENG", "FIN"])` — Builds or evaluates a database query.
9. `Employee.objects.order_by("-salary", "full_name")` — Builds or evaluates a database query.
10. `Employee.objects.values("employee_code", "full_name", "salary")` — Builds or evaluates a database query.

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

Django ORM QuerySets support filtering, excluding, retrieving one record, sorting and selecting fields. Field lookups such as __icontains, __gte, __in and __range express common query conditions. QuerySets are lazy until evaluated, so developers should understand when database queries actually run.

## 8. Approved mini-project — Advanced Product Search

**Objective:** Advanced Product Search.

### Required tasks

1. Open Django shell and import Employee.
2. Use filter() for exact matching.
3. Use exclude() to remove matching records.
4. Use get() when exactly one record is expected.
5. Use field lookups such as icontains, gte and in.
6. Use order_by() with a minus prefix for descending order.
7. Use values() to select fields as dictionaries.
8. Inspect querysets and evaluate them using list() or iteration.
9. Handle DoesNotExist and MultipleObjectsReturned where appropriate.

### Suggested structure

```text
projects/day_43/
├── README.md
├── application/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── tests/
```

### Validation checklist

- [ ] Each lookup returns expected records.
- [ ] Case-insensitive search works.
- [ ] Numeric comparison uses the correct field type.
- [ ] Descending sort is correct.
- [ ] get() exceptions are understood.
- [ ] Selected values contain only requested fields.

### Submission evidence

- Source code and URLs.
- Sample database records.
- Browser screenshots or query output.
- Test cases and results.
- README explaining the operation and its risks.
- Query count comparison where relevant.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Advanced Product Search. Identify the views, ORM methods, URL patterns, test data and validation cases. Do not provide the complete project."

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

**Q1. Explain advanced django orm: filter, exclude, get, order_by and values.**  
**Answer:** Django ORM QuerySets support filtering, excluding, retrieving one record, sorting and selecting fields. Field lookups such as __icontains, __gte, __in and __range express common query conditions. QuerySets are lazy until evaluated, so developers should understand when database queries actually run.

**Q2. What is one common failure?**  
**Answer:** Each lookup returns expected records. Explain how you would reproduce and diagnose it.

**Q3. How do you verify the result?**  
**Answer:** Inspect the database, run the relevant query or view and test normal and invalid cases.

**Follow-up:** What production concern is important?  
**Answer:** Authorization, data integrity, transaction safety and performance must be considered.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Verify database behavior.
- [ ] Test normal and invalid cases.
- [ ] Complete Advanced Product Search.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 44.
