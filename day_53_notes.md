# Day 53: Pagination, Search and Filtering in Django Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–53 — Django fundamentals, ORM, forms, users and access control  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** Paginated Product Catalog

> **Trainer guidance:** Explain the relationship between each file and the user journey. Show the learner how to verify the behavior using separate test accounts and sample records.

## 1. Learning objectives

- Explain pagination, search and filtering in django applications.
- Identify the Django components and settings involved.
- Implement the example step by step.
- Test normal, invalid and unauthorized cases.
- Explain one design or security decision.
- Complete Paginated Product Catalog.

## 2. Concept introduction

Pagination divides a large result set into manageable pages. Django's Paginator works with QuerySets and other sliceable data. Search and filtering can be implemented using validated GET parameters and ORM lookups. Query parameters should be handled safely and predictable ordering should be used.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Employee

def employee_search(request):
    query = request.GET.get("q", "").strip()
    employees = Employee.objects.all().order_by("full_name")

    if query:
        employees = employees.filter(
            Q(full_name__icontains=query) |
            Q(employee_code__icontains=query)
        )

    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "profiles/employee_search.html",
        {"page_obj": page_obj, "query": query}
    )
```

### profiles/templates/profiles/employee_search.html

```python
<form method="get">
    <input name="q" value="{{ query }}" placeholder="Search employees">
    <button type="submit">Search</button>
</form>

{% for employee in page_obj %}
    <p>{{ employee.full_name }} — {{ employee.employee_code }}</p>
{% empty %}
    <p>No employees found.</p>
{% endfor %}

{% if page_obj.has_previous %}
    <a href="?q={{ query }}&page={{ page_obj.previous_page_number }}">Previous</a>
{% endif %}
<span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
{% if page_obj.has_next %}
    <a href="?q={{ query }}&page={{ page_obj.next_page_number }}">Next</a>
{% endif %}
```

## 4. Understand the important statements

### profiles/views.py

1. `from django.core.paginator import Paginator` — Imports Django components or the active user model setting.
2. `from django.db.models import Q` — Imports Django components or the active user model setting.
3. `from django.shortcuts import render` — Imports Django components or the active user model setting.
4. `from .models import Employee` — Imports Django components or the active user model setting.
5. ` ` — Part of the implementation; explain its role in the overall workflow.
6. `def employee_search(request):` — Defines a view function.
7. `    query = request.GET.get("q", "").strip()` — Part of the implementation; explain its role in the overall workflow.
8. `    employees = Employee.objects.all().order_by("full_name")` — Part of the implementation; explain its role in the overall workflow.
9. ` ` — Part of the implementation; explain its role in the overall workflow.
10. `    if query:` — Part of the implementation; explain its role in the overall workflow.
11. `        employees = employees.filter(` — Part of the implementation; explain its role in the overall workflow.
12. `            Q(full_name__icontains=query) |` — Builds a composable query condition.
13. `            Q(employee_code__icontains=query)` — Builds a composable query condition.
14. `        )` — Part of the implementation; explain its role in the overall workflow.
15. ` ` — Part of the implementation; explain its role in the overall workflow.
16. `    paginator = Paginator(employees, 10)` — Creates page-based navigation for a result set.
17. `    page_number = request.GET.get("page")` — Part of the implementation; explain its role in the overall workflow.
18. `    page_obj = paginator.get_page(page_number)` — Part of the implementation; explain its role in the overall workflow.
19. ` ` — Part of the implementation; explain its role in the overall workflow.
20. `    return render(` — Part of the implementation; explain its role in the overall workflow.
21. `        request,` — Part of the implementation; explain its role in the overall workflow.
22. `        "profiles/employee_search.html",` — Part of the implementation; explain its role in the overall workflow.
23. `        {"page_obj": page_obj, "query": query}` — Part of the implementation; explain its role in the overall workflow.
24. `    )` — Part of the implementation; explain its role in the overall workflow.

### profiles/templates/profiles/employee_search.html

1. `<form method="get">` — Part of the implementation; explain its role in the overall workflow.
2. `    <input name="q" value="{{ query }}" placeholder="Search employees">` — Part of the implementation; explain its role in the overall workflow.
3. `    <button type="submit">Search</button>` — Part of the implementation; explain its role in the overall workflow.
4. `</form>` — Part of the implementation; explain its role in the overall workflow.
5. ` ` — Part of the implementation; explain its role in the overall workflow.
6. `{% for employee in page_obj %}` — Part of the implementation; explain its role in the overall workflow.
7. `    <p>{{ employee.full_name }} — {{ employee.employee_code }}</p>` — Part of the implementation; explain its role in the overall workflow.
8. `{% empty %}` — Part of the implementation; explain its role in the overall workflow.
9. `    <p>No employees found.</p>` — Part of the implementation; explain its role in the overall workflow.
10. `{% endfor %}` — Part of the implementation; explain its role in the overall workflow.
11. ` ` — Part of the implementation; explain its role in the overall workflow.
12. `{% if page_obj.has_previous %}` — Part of the implementation; explain its role in the overall workflow.
13. `    <a href="?q={{ query }}&page={{ page_obj.previous_page_number }}">Previous</a>` — Part of the implementation; explain its role in the overall workflow.
14. `{% endif %}` — Part of the implementation; explain its role in the overall workflow.
15. `<span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>` — Part of the implementation; explain its role in the overall workflow.
16. `{% if page_obj.has_next %}` — Part of the implementation; explain its role in the overall workflow.
17. `    <a href="?q={{ query }}&page={{ page_obj.next_page_number }}">Next</a>` — Part of the implementation; explain its role in the overall workflow.
18. `{% endif %}` — Part of the implementation; explain its role in the overall workflow.

## 5. Integration flow

```text
Browser request
   ↓
URL pattern
   ↓
Authentication / permission check
   ↓
View
   ↓
Form validation
   ↓
ORM and database
   ↓
Messages / redirect / template
   ↓
Browser response
```

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| User model import error | AUTH_USER_MODEL and app registration |
| Duplicate record | Database constraint and user feedback |
| Message not visible | Messages middleware, context processor and template |
| Pagination loses search | Preserve query parameters in page links |
| Search results are inconsistent | Ordering and Q conditions |
| User can perform restricted action | Server-side authorization |
| Form accepts untrusted ownership fields | Set owner/applicant in the view from request.user |

## 7. Industry scenario

Pagination divides a large result set into manageable pages. Django's Paginator works with QuerySets and other sliceable data. Search and filtering can be implemented using validated GET parameters and ORM lookups. Query parameters should be handled safely and predictable ordering should be used.

## 8. Approved mini-project — Paginated Product Catalog

**Objective:** Paginated Product Catalog.

### Required tasks

1. Create a queryset with predictable ordering.
2. Read the search term from request.GET.
3. Use Q objects to search multiple fields with OR logic.
4. Create a Paginator with a suitable page size.
5. Read the requested page number.
6. Use get_page() to handle invalid or missing page values safely.
7. Render page_obj and navigation controls.
8. Test empty search, matching search and out-of-range pages.

### Suggested structure

```text
projects/day_53/
├── manage.py
├── config/
└── jobs/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
```

### Validation checklist

- [ ] Results are sorted predictably.
- [ ] Search checks the intended fields.
- [ ] Pagination displays the correct page.
- [ ] Invalid page numbers are handled safely.
- [ ] Search term is preserved between pages.
- [ ] Empty results show a useful message.

### Test matrix

| User or input | Expected behavior |
|---|---|
| Anonymous visitor | Public pages load; protected action redirects or denies |
| Authenticated user | Allowed action succeeds |
| Invalid form | Errors display; no record is saved |
| Duplicate submission | Constraint prevents duplicate data |
| Missing or inactive record | Not found or denied as appropriate |
| Valid workflow | Database and browser state agree |

### Submission evidence

- Source code and migrations.
- Screenshots of the main user journey.
- Test results for positive and negative cases.
- README with setup and architecture.
- Explanation of authorization and data integrity.
- No real user credentials or personal data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Paginated Product Catalog. Identify the models, forms, views, URLs, templates, permissions, migrations and test cases. Do not write the full project."

**Guided prompt:** "Guide me through one component at a time. Explain the file path and wait for my test result."

**Debugging prompt:** "Trace my user journey from URL to view to form to database. Identify where the behavior differs from the requirement."

**Review prompt:** "Review the project for integration correctness, duplicate handling, permissions, validation and test coverage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Integrate multiple Django components into a complete user workflow.  
B. Replace the database.  
C. Remove authentication.  
D. Disable URL routing.  
**Answer: A.** Integration connects the individual components into a working feature.

**Q2. Where should the server get the identity of the logged-in applicant?**  
A. A hidden HTML field.  
B. request.user.  
C. A URL parameter supplied by the browser.  
D. A text box.  
**Answer: B.** Use the authenticated user supplied by Django.

**Q3. Why add a database uniqueness constraint?**  
A. To style a template.  
B. To create a URL.  
C. To enforce a rule even if multiple requests reach the database.  
D. To disable migrations.  
**Answer: C.** Database constraints protect integrity.

**Q4. What should an integration test cover?**  
A. Only one Python import.  
B. Only a screenshot.  
C. Only the model class.  
D. A realistic sequence across views, forms, authentication and database.  
**Answer: D.** Integration tests verify components working together.

**Q5. What is the strongest evidence of completion?**  
A. A tested end-to-end user journey with expected database state.  
B. A project folder only.  
C. A long code file.  
D. A list of planned features.  
**Answer: A.** Completion requires verified behavior.

## 11. Interview preparation

**Q1. Explain pagination, search and filtering in django applications.**  
**Answer:** Pagination divides a large result set into manageable pages. Django's Paginator works with QuerySets and other sliceable data. Search and filtering can be implemented using validated GET parameters and ORM lookups. Query parameters should be handled safely and predictable ordering should be used.

**Q2. What is one important design decision?**  
**Answer:** Explain the relationship, constraint or server-side value assignment used in the implementation.

**Q3. How do you verify the full application?**  
**Answer:** Test the end-to-end user journey with anonymous and authenticated users, valid and invalid inputs and expected database state.

**Follow-up:** Why are integration tests necessary if unit tests pass?  
**Answer:** Unit tests check individual components; integration tests verify that those components work together correctly.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Identify all connected components.
- [ ] Implement the example.
- [ ] Test valid and invalid user journeys.
- [ ] Complete Paginated Product Catalog.
- [ ] Verify database state.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 54.
