# Day 39: Interview Guide — Django Forms and ModelForms

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 39 notes](day_39_notes.md)  
**Mini-project:** Student Registration Form

## 1. Technical questions with model answers

### Q1. What is a Django Form?

**Model answer:** It defines expected input fields, converts submitted values to Python types and validates them. It can be used without a database model.

### Q2. What is a ModelForm?

**Model answer:** It is a form tied to a model. Its Meta class selects the model and fields, and save() can create or update a model instance after validation.

### Q3. What is a bound form?

**Model answer:** A form instantiated with submitted data, such as StudentRegistrationForm(request.POST). It can be validated and displays submitted values and errors.

### Q4. Why must is_valid() be called before save()?

**Model answer:** It runs field and form validation and populates cleaned_data. Only valid data should be persisted.

### Q5. What is the GET/POST pattern in a registration view?

**Model answer:** GET creates and displays an empty form. POST binds submitted data, validates it, saves if valid and redirects; invalid POST re-renders the bound form with errors.

### Q6. Why redirect after a successful POST?

**Model answer:** It follows Post/Redirect/Get, reducing accidental duplicate submissions when the user refreshes the resulting page.

## 2. Scenario-based interview question

**Scenario:** The form is visible, but submitting it does not create a Student. What do you inspect?

**Model answer:** Confirm the form uses method=post, includes the CSRF token, the view handles request.method == 'POST', the form is bound to request.POST, is_valid() returns True, save() executes and the database uses the expected model/table. Inspect form.errors and the server traceback.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Implement StudentRegistrationForm, GET/POST view, named URL and template. Test one valid record and one invalid submission and verify the database.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Student Registration Form

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
- [ ] I can present Student Registration Form with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is a bound form?
**Answer:** A form with submitted data attached, such as StudentForm(request.POST), which can be validated.

### Q6. What does cleaned_data contain?
**Answer:** Validated Python values after form.is_valid() succeeds.

### Q7. What is a widget?
**Answer:** It controls how a form field is rendered in HTML, such as a text input or select.

### Q8. What is the difference between clean_fieldname() and clean()?
**Answer:** clean_fieldname validates one field. clean() validates rules involving multiple fields.

### Q9. Why explicitly list ModelForm fields?
**Answer:** It ensures only approved fields are exposed and prevents newly added model fields from becoming editable automatically.

### Q10. What does save(commit=False) do?
**Answer:** It returns an unsaved model instance so the view can assign server-controlled values before saving.

### Q11. Scenario: update creates a duplicate record.
**Answer:** Pass the existing model object using instance=existing_object when constructing the ModelForm.

### Q12. Scenario: invalid form errors disappear.
**Answer:** The view probably created a new unbound form. Render the same bound form instance after validation fails.

