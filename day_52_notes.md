# Day 52: Django Messages Framework and Application Feedback

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–53 — Django fundamentals, ORM, forms, users and access control  
**Tools:** Python, Django, VS Code, terminal, browser and configured database  
**Approved mini-project:** User Notification Application

> **Trainer guidance:** Explain the relationship between each file and the user journey. Show the learner how to verify the behavior using separate test accounts and sample records.

## 1. Learning objectives

- Explain django messages framework and application feedback.
- Identify the Django components and settings involved.
- Implement the example step by step.
- Test normal, invalid and unauthorized cases.
- Explain one design or security decision.
- Complete User Notification Application.

## 2. Concept introduction

The messages framework lets a Django application display one-time feedback after an action, such as a successful save or an error. Messages are commonly stored using session or cookie-based storage and displayed in templates. They are useful for user feedback but are not a replacement for persistent notifications.

## 3. File-by-file implementation

### profiles/views.py

```python
from django.contrib import messages
from django.shortcuts import redirect

def save_profile(request):
    if request.method == "POST":
        # Perform validated save here
        messages.success(request, "Profile saved successfully.")
        return redirect("profile_detail")

    messages.info(request, "Submit the form to update your profile.")
    return redirect("profile_detail")
```

### profiles/templates/base.html

```python
{% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li class="{{ message.tags }}">{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
```

## 4. Understand the important statements

### profiles/views.py

1. `from django.contrib import messages` — Imports Django components or the active user model setting.
2. `from django.shortcuts import redirect` — Imports Django components or the active user model setting.
3. ` ` — Part of the implementation; explain its role in the overall workflow.
4. `def save_profile(request):` — Defines a view function.
5. `    if request.method == "POST":` — Part of the implementation; explain its role in the overall workflow.
6. `        # Perform validated save here` — Part of the implementation; explain its role in the overall workflow.
7. `        messages.success(request, "Profile saved successfully.")` — Queues one-time user feedback.
8. `        return redirect("profile_detail")` — Part of the implementation; explain its role in the overall workflow.
9. ` ` — Part of the implementation; explain its role in the overall workflow.
10. `    messages.info(request, "Submit the form to update your profile.")` — Queues one-time user feedback.
11. `    return redirect("profile_detail")` — Part of the implementation; explain its role in the overall workflow.

### profiles/templates/base.html

1. `{% if messages %}` — Part of the implementation; explain its role in the overall workflow.
2. `    <ul class="messages">` — Part of the implementation; explain its role in the overall workflow.
3. `        {% for message in messages %}` — Part of the implementation; explain its role in the overall workflow.
4. `            <li class="{{ message.tags }}">{{ message }}</li>` — Part of the implementation; explain its role in the overall workflow.
5. `        {% endfor %}` — Part of the implementation; explain its role in the overall workflow.
6. `    </ul>` — Part of the implementation; explain its role in the overall workflow.
7. `{% endif %}` — Part of the implementation; explain its role in the overall workflow.

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

The messages framework lets a Django application display one-time feedback after an action, such as a successful save or an error. Messages are commonly stored using session or cookie-based storage and displayed in templates. They are useful for user feedback but are not a replacement for persistent notifications.

## 8. Approved mini-project — User Notification Application

**Objective:** User Notification Application.

### Required tasks

1. Confirm messages app and middleware are configured.
2. Import django.contrib.messages in the view.
3. Add success, info, warning or error messages after relevant actions.
4. Redirect after successful POST.
5. Loop through messages in a shared base template.
6. Use message tags to style feedback.
7. Test that messages appear once and then disappear.
8. Do not store permanent business notifications only in messages.

### Suggested structure

```text
projects/day_52/
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

- [ ] A success message appears after a successful save.
- [ ] An error or warning message appears for the appropriate case.
- [ ] Messages are rendered in the base template.
- [ ] Messages do not persist as permanent notification records.
- [ ] The redirect flow works.

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

**Planning prompt:** "Help me plan User Notification Application. Identify the models, forms, views, URLs, templates, permissions, migrations and test cases. Do not write the full project."

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

**Q1. Explain django messages framework and application feedback.**  
**Answer:** The messages framework lets a Django application display one-time feedback after an action, such as a successful save or an error. Messages are commonly stored using session or cookie-based storage and displayed in templates. They are useful for user feedback but are not a replacement for persistent notifications.

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
- [ ] Complete User Notification Application.
- [ ] Verify database state.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 53.
