# Day 42: Interview Guide — CRUD Operations: Create, Read, Update and Delete

**Related class notes:** [Day 42 notes](day_42_notes.md)  
**Approved mini-project:** Employee CRUD Application  
**Level:** Beginner to Intermediate

## 1. Core questions

### Q1. What does CRUD mean?
**Answer:** CRUD means Create, Read, Update and Delete. These are the four basic operations used to manage records in a database-backed application.

### Q2. How does Django create a record?
**Answer:** A view receives a request, validates submitted data through a form, and saves a model instance. A ModelForm can use form.save() after is_valid() returns True.

### Q3. What is the difference between GET and POST in a CRUD workflow?
**Answer:** GET normally reads or displays data. POST submits data that changes server state, such as creating, updating or deleting a record.

### Q4. Why use get_object_or_404()?
**Answer:** It retrieves an object matching the lookup or returns an HTTP 404 response if no matching object exists. It avoids an unhandled DoesNotExist exception in the view.

### Q5. Why should delete use POST and a confirmation page?
**Answer:** Deletion changes data and should not be triggered by a safe GET request. A confirmation page helps prevent accidental deletion; the POST endpoint must still validate authorization and CSRF.

### Q6. What does ModelForm.save(commit=False) do?
**Answer:** It creates an unsaved model instance so the view can assign server-controlled fields before calling save().

### Q7. Why should the view not trust a primary key alone?
**Answer:** A user may change the ID in the URL. The view must check that the user is allowed to access or modify that specific record.

### Q8. What is the Post/Redirect/Get pattern?
**Answer:** After a valid POST, the view redirects to a GET page. This reduces accidental duplicate submissions when a user refreshes the result page.

## 2. Debugging and scenario questions

### Q9. Update view returns 404.
**Answer:** Check the URL converter, view parameter name, record primary key and database. Confirm the record exists in the active database.

### Q10. A form saves invalid data.
**Answer:** Check that the view calls is_valid() before save(), and that field and form-wide validation rules are implemented.

### Q11. A user can delete another employee by changing the URL ID.
**Answer:** Add authentication, permission and object ownership checks in the delete view. Hiding a delete button is not enough.

### Q12. Refreshing the page creates duplicate records.
**Answer:** The view may render a success page directly after POST. Redirect after a successful save and use an idempotency/uniqueness rule where the business operation requires it.

### Q13. A delete link removes a record through GET.
**Answer:** Replace it with a POST form containing a CSRF token and restrict the delete view to POST.

## 3. Practical demonstration

Be prepared to demonstrate:
1. Create an employee.
2. List employees.
3. Open one employee detail.
4. Update an employee.
5. Submit invalid form data.
6. Request a missing primary key.
7. Confirm deletion.
8. Prove that unauthorized deletion is blocked.

## 4. Readiness checklist

- [ ] I can explain each CRUD operation.
- [ ] I can explain ModelForm validation and save.
- [ ] I can explain GET versus POST.
- [ ] I can explain safe deletion.
- [ ] I can explain object ownership.
- [ ] I can demonstrate Employee CRUD Application.

**Related notes:** [Day 42 class notes](day_42_notes.md)
