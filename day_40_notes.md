# Day 40: Form Validation, CSRF Protection and Error Messages

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Estimated time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–40 — Django setup, URLs, views, templates and models  
**Tools:** Python, Django, VS Code, terminal and browser  
**Approved mini-project:** Secure Form Validation Application

> **Trainer guidance:** Explain the browser request first, then show the file that handles it. Make students test GET and POST separately. A form should never save data before validation.

## 1. Learning objectives

- Explain form validation, csrf protection and error messages.
- Identify the file responsible for each part of the workflow.
- Implement the example step by step.
- Explain the difference between GET and POST handling.
- Validate normal and invalid input.
- Complete Secure Form Validation Application.

## 2. Concept introduction

Validation checks whether submitted data satisfies expected rules before it is accepted. Django forms provide field validation, clean_<field>() methods and a form-wide clean() method. CSRF protection helps prevent an attacker from causing a browser to submit an unwanted request using a user's authenticated session.

## 3. End-to-end flow

```text
Browser form
   ↓ POST request
Application URL pattern
   ↓
View receives HttpRequest
   ↓
Form binds request.POST
   ↓
form.is_valid()
   ↓
cleaned_data / validation errors
   ↓
ModelForm.save()
   ↓
Database
   ↓
Redirect or rendered response
```

## 4. File-by-file implementation

### File: `profiles/forms.py`

```python
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_code", "full_name", "email", "department", "salary", "joining_date"]

    def clean_employee_code(self):
        code = self.cleaned_data["employee_code"].strip().upper()
        if not code.startswith("EMP"):
            raise forms.ValidationError("Employee code must start with EMP")
        return code

    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data.get("salary")
        if salary is not None and salary <= 0:
            self.add_error("salary", "Salary must be greater than zero")
        return cleaned_data
```

### File: `profiles/templates/profiles/employee_form.html`

```html
<form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

## 5. Understand the important statements

### profiles/forms.py

1. `from django import forms` — Imports a Django component or local module.
2. `from .models import Employee` — Imports a Django component or local module.
3. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
4. `class EmployeeForm(forms.ModelForm):` — Defines a form or application component.
5. `    class Meta:` — Defines a form or application component.
6. `        model = Employee` — Part of the workflow; explain how it contributes to validation or response rendering.
7. `        fields = ["employee_code", "full_name", "email", "salary"]` — Part of the workflow; explain how it contributes to validation or response rendering.
8. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
9. `    def clean_employee_code(self):` — Defines a view or validation method.
10. `        code = self.cleaned_data["employee_code"].strip().upper()` — Reads values after field validation.
11. `        if not code.startswith("EMP"):` — Part of the workflow; explain how it contributes to validation or response rendering.
12. `            raise forms.ValidationError("Employee code must start with EMP")` — Part of the workflow; explain how it contributes to validation or response rendering.
13. `        return code` — Part of the workflow; explain how it contributes to validation or response rendering.
14. ` ` — Part of the workflow; explain how it contributes to validation or response rendering.
15. `    def clean(self):` — Defines a view or validation method.
16. `        cleaned_data = super().clean()` — Reads values after field validation.
17. `        salary = cleaned_data.get("salary")` — Reads values after field validation.
18. `        if salary is not None and salary <= 0:` — Part of the workflow; explain how it contributes to validation or response rendering.
19. `            self.add_error("salary", "Salary must be greater than zero")` — Part of the workflow; explain how it contributes to validation or response rendering.
20. `        return cleaned_data` — Reads values after field validation.

### profiles/templates/profiles/employee_form.html

1. `<form method="post">` — Part of the workflow; explain how it contributes to validation or response rendering.
2. `    {% csrf_token %}` — Adds the CSRF token to the POST form.
3. `    {{ form.non_field_errors }}` — Part of the workflow; explain how it contributes to validation or response rendering.
4. `    {{ form.as_p }}` — Part of the workflow; explain how it contributes to validation or response rendering.
5. `    <button type="submit">Save</button>` — Part of the workflow; explain how it contributes to validation or response rendering.
6. `</form>` — Part of the workflow; explain how it contributes to validation or response rendering.

## 6. GET and POST

| Method | Typical form behavior |
|---|---|
| GET | Display an empty form or retrieve the page |
| POST | Receive submitted values, validate and save when valid |

Do not use GET to change application state. A successful POST often redirects to a page that displays the saved record. This pattern is known as Post/Redirect/Get.

## 7. Validation and security rules

- Always call form.is_valid() before using cleaned_data or saving a ModelForm.
- Display field errors and non-field errors.
- Keep CSRF protection enabled for internal browser forms.
- Do not trust browser-side validation alone; server-side validation is required.
- Never place passwords or secret keys in form HTML or source code.
- Validate permissions before allowing a user to create or modify protected records.

## 8. Common errors

| Symptom | What to inspect |
|---|---|
| Form does not save | is_valid(), model constraints and database errors |
| CSRF verification failed | csrf_token in the form and CSRF middleware |
| Field not found | ModelForm Meta.fields and model field names |
| Form always invalid | Display form.errors and inspect field validation |
| Duplicate email/code | Unique model constraints and validation feedback |
| View handles only GET | Add correct POST branch |
| Redirect name does not resolve | URL pattern name and namespace |

## 9. Industry scenario

Validation checks whether submitted data satisfies expected rules before it is accepted. Django forms provide field validation, clean_<field>() methods and a form-wide clean() method. CSRF protection helps prevent an attacker from causing a browser to submit an unwanted request using a user's authenticated session.

## 10. Approved mini-project — Secure Form Validation Application

**Objective:** Secure Form Validation Application.

### Required tasks

1. Add a field-specific clean_employee_code() method.
2. Read the field value from cleaned_data.
3. Normalize the value and check the business rule.
4. Raise forms.ValidationError when the field value is invalid.
5. Use clean() for rules that involve multiple fields.
6. Call super().clean() and return cleaned_data.
7. Keep {% csrf_token %} inside every internal POST form.
8. Submit valid and invalid values and inspect displayed errors.

### Suggested structure

```text
projects/day_40/
├── manage.py
├── config/
└── profiles/
    ├── models.py
    ├── forms.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── profiles/
```

### Validation checklist

- [ ] Invalid employee code is rejected.
- [ ] Valid employee code is normalized.
- [ ] Non-positive salary is rejected.
- [ ] Form errors are shown to the user.
- [ ] POST form contains a CSRF token.
- [ ] Valid data is saved only after is_valid().

### Test scenarios

| Scenario | Expected behavior |
|---|---|
| GET form page | Empty form is displayed |
| POST missing required field | Validation error is displayed |
| POST invalid field value | Field-specific error is displayed |
| POST valid values | Record is saved and user is redirected |
| Open list page | Saved record is visible |
| POST without CSRF token | Request is rejected when CSRF protection is enabled |

### Submission evidence

- Source files.
- Browser screenshots of GET and POST behavior.
- Database/admin evidence for a valid saved record.
- Invalid form submission evidence.
- README with exact commands and file paths.
- Short explanation of the request-response flow.

## 11. AI-assisted implementation

**Planning prompt:** "Help me plan Secure Form Validation Application. Identify the model, form, view, URL and template responsibilities. Give an ordered implementation plan, not the complete code."

**Guided prompt:** "Help me implement the form GET branch first. Explain the code and wait for my browser result before showing the POST branch."

**Debugging prompt:** "Here are my form class, view, template and form.errors output. Find the validation or request handling issue and explain the smallest fix."

**Review prompt:** "Review the workflow for server-side validation, CSRF, redirects, data persistence and clear user feedback."

## 12. Five daily MCQs

**Q1. What should happen before a ModelForm is saved?**  
A. Call form.is_valid().  
B. Delete the model.  
C. Disable CSRF.  
D. Ignore the submitted values.  
**Answer: A.** Validate the bound form before saving.

**Q2. Which method normally displays a blank form?**  
A. DELETE  
B. GET  
C. PATCH  
D. MERGE  
**Answer: B.** GET retrieves the page and displays the form.

**Q3. What does {% csrf_token %} provide?**  
A. A database primary key.  
B. A CSS file.  
C. A CSRF token for a protected form submission.  
D. A URL converter.  
**Answer: C.** It helps Django verify that the POST submission includes the expected token.

**Q4. Where should important server-side validation happen?**  
A. Only in browser JavaScript.  
B. Only in a README.  
C. In a screenshot.  
D. In Django form/model validation.  
**Answer: D.** Client-side checks can be bypassed; validate on the server.

**Q5. Why redirect after a successful POST?**  
A. To avoid accidental duplicate form submission on refresh and show the resulting page.  
B. To disable the database.  
C. To remove validation.  
D. To bypass URL routing.  
**Answer: A.** Post/Redirect/Get is a common browser workflow.

## 13. Interview preparation

**Q1. Explain form validation, csrf protection and error messages.**  
**Answer:** Validation checks whether submitted data satisfies expected rules before it is accepted. Django forms provide field validation, clean_<field>() methods and a form-wide clean() method. CSRF protection helps prevent an attacker from causing a browser to submit an unwanted request using a user's authenticated session.

**Q2. Why is is_valid() important?**  
**Answer:** It runs validation and populates cleaned_data or errors. Saving should happen only after the form is valid.

**Q3. What is CSRF protection?**  
**Answer:** It helps protect authenticated browser sessions from unwanted cross-site form submissions.

**Follow-up:** How do you verify a successful submission?  
**Answer:** Check the redirect, displayed list and actual saved database record.

## 14. Completion checklist

- [ ] Explain the form workflow.
- [ ] Identify model, form, view, URL and template files.
- [ ] Test GET and POST.
- [ ] Test invalid and valid data.
- [ ] Verify CSRF behavior.
- [ ] Complete Secure Form Validation Application.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 41.
