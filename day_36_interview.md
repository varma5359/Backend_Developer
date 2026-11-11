# Day 36: Interview Guide — Django Admin Panel and Model Registration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 36 notes](day_36_notes.md)  
**Mini-project:** Employee Admin Manager

## 1. Technical questions with model answers

### Q1. What is Django admin?

**Model answer:** It is a built-in authenticated management interface generated from registered models. It is useful for trusted staff but does not replace a public-facing application.

### Q2. How do you register a model?

**Model answer:** Import the model in profiles/admin.py and use admin.site.register(Employee) or the @admin.register(Employee) decorator.

### Q3. What does list_display control?

**Model answer:** It chooses the columns displayed in the admin changelist. Each name must refer to a valid model field or callable.

### Q4. What do search_fields and list_filter do?

**Model answer:** search_fields configures text search over selected fields. list_filter adds sidebar filters for fields suitable for filtering.

### Q5. What is the difference between staff and superuser?

**Model answer:** is_staff permits access to the admin login area, but model permissions still control actions. A superuser has all permissions. Use least privilege.

### Q6. Why should admin not be exposed as an unrestricted public CRUD interface?

**Model answer:** It is intended for trusted internal staff. Public workflows need purpose-built views, validation, authentication and authorization appropriate to the user.

## 2. Scenario-based interview question

**Scenario:** An HR assistant can log in to /admin/ but cannot edit Employee records. What should you inspect?

**Model answer:** Check that the account has is_staff=True and that the user has the relevant Employee change permission. Do not automatically make the account a superuser. Verify permissions in the admin or Django shell.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Register Employee, configure list_display/search_fields/list_filter/ordering, create a superuser, add records, test search and filters and explain least privilege.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Employee Admin Manager

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Employee Admin Manager with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.