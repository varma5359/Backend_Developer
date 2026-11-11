# Day 54: Interview Guide — Complete Django Application Integration and Validation

**Related class notes:** [Day 54 notes](day_54_notes.md)  
**Approved mini-project:** Job Portal Web Application  
**Level:** Intermediate

## How to use this guide
Prepare to explain one complete user journey, not only isolated Django definitions. Draw the request flow and identify the model, form, view, URL, template, authentication check, permission check and database rule involved.

## 1. Architecture and data model questions

### Q1. What does application integration mean?
**Answer:** It means connecting models, migrations, forms, views, URLs, templates, authentication, permissions and database operations into a complete workflow.

### Q2. Why create a separate jobs app?
**Answer:** It groups job-domain models and behavior together. This keeps the project organized and makes the feature easier to maintain.

### Q3. What does the Job model represent?
**Answer:** It represents one job opening, including title, company, description, location, employment type, salary range, active status and posting user.

### Q4. What does JobApplication represent?
**Answer:** It connects one applicant to one job and stores application information such as cover letter and submission timestamp.

### Q5. Why use settings.AUTH_USER_MODEL?
**Answer:** It points model relationships to the user model configured for the project, including a custom user model if one is configured.

### Q6. Why use a unique constraint on job and applicant?
**Answer:** It prevents the same applicant from applying to the same job more than once. The database constraint protects against concurrent requests that may pass an application-level check.

### Q7. Why use DecimalField for salary?
**Answer:** Salary is a decimal monetary value. DecimalField avoids binary floating-point representation issues and defines precision and decimal places.

### Q8. Why add both form validation and database constraints?
**Answer:** Form validation provides helpful user-facing errors. Database constraints protect stored data even when a write bypasses the form.

## 2. Forms and view questions

### Q9. Why is posted_by excluded from JobForm?
**Answer:** The server must assign the authenticated request.user as the owner. The browser must not choose another user as the job owner.

### Q10. Why are job and applicant excluded from JobApplicationForm?
**Answer:** The view should retrieve the job from the URL/database and assign the applicant from request.user. These identities must not be trusted from submitted form data.

### Q11. What does save(commit=False) do?
**Answer:** It creates a model instance without immediately saving it. The view can assign trusted fields such as job and applicant before calling save().

### Q12. Why use transaction.atomic()?
**Answer:** It groups database operations into a transaction. If an error occurs inside the block, the transaction can be rolled back.

### Q13. Why catch IntegrityError around the application save?
**Answer:** The database unique constraint may reject a duplicate application. The view catches the expected integrity failure and returns safe feedback instead of an unhandled server error.

### Q14. Why filter my_applications by request.user?
**Answer:** It ensures that each job seeker sees only their own application records. Without this filter, private applicant information could be exposed.

## 3. Authentication and authorization questions

### Q15. Why does apply_to_job require login?
**Answer:** Applying creates a user-specific record. The application must know which authenticated account is submitting the application.

### Q16. Why check job ownership in addition to change_job permission?
**Answer:** A model permission grants a general capability to change Job objects. The business rule may restrict the user to jobs they posted. The view must check the specific object's owner.

### Q17. Why is hiding the edit button not enough?
**Answer:** Users can manually request a URL. The backend view must enforce permission and ownership rules.

### Q18. Why close a job instead of deleting it?
**Answer:** Closing preserves the job and application history while preventing new applications. Deletion can remove related records depending on on_delete behavior.

## 4. Testing and debugging questions

### Q19. What should be tested in an end-to-end job seeker journey?
**Answer:** Registration, login, job browsing, search, filtering, job detail, valid application, duplicate application rejection, own application list and logout.

### Q20. What should be tested in the employer journey?
**Answer:** Permission assignment, job creation, server-side owner assignment, editing own job, denial when editing another user's job, closing a job and viewing only applications for owned jobs.

### Q21. What is an integration test?
**Answer:** It tests multiple components working together, such as a POST request passing through a URL, view, form, model and database and returning the expected response.

### Q22. Why run the full test suite?
**Answer:** A new feature can break existing apps. Running all tests helps detect regressions across profiles, catalog and jobs.

## 5. Scenario questions

### Q23. An employer changes the job ID in the URL and sees another employer's job.
**Answer:** The edit or applicants view is missing an ownership check. Retrieve the job and compare posted_by with request.user, while also checking the required permission.

### Q24. A closed job still accepts applications.
**Answer:** The application view is not filtering for is_active=True. Retrieve only an active job before validating and saving the application.

### Q25. Duplicate applications appear under simultaneous requests.
**Answer:** Add a database UniqueConstraint on job and applicant, keep application-level checks for user feedback and handle the expected IntegrityError.

### Q26. A developer marks the project production-ready after runserver works.
**Answer:** That is not enough. Run migrations, system checks, full automated tests, security review, permission tests and deployment-specific validation. Document features not implemented.

## 6. Mini-project discussion — Job Portal Web Application

Be ready to demonstrate:
1. Job and JobApplication models.
2. Salary and uniqueness constraints.
3. JobForm and JobApplicationForm.
4. Job list/search/filter/pagination.
5. Authenticated application submission.
6. Employer group permissions.
7. Ownership checks.
8. Messages and redirects.
9. Tests for success, invalid and denied cases.
10. Known limitations.

## 7. Final readiness checklist

- [ ] I can draw the complete request-response flow.
- [ ] I can explain both models and their relationships.
- [ ] I can explain form validation and server-assigned ownership.
- [ ] I can explain the duplicate application constraint.
- [ ] I can explain authentication, permissions and ownership.
- [ ] I can demonstrate the job seeker journey.
- [ ] I can demonstrate the employer journey.
- [ ] I can run and explain the full test suite.
- [ ] I can state what is not production-ready.

**Related notes:** [Day 54 class notes](day_54_notes.md)
