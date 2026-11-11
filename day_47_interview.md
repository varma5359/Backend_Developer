# Day 47: Interview Guide — User Registration, Login and Logout

**Related class notes:** [Day 47 notes](day_47_notes.md)  
**Approved mini-project:** User Authentication Application  
**Level:** Beginner to Intermediate

## How to use this guide
Answer aloud. For each answer, identify the API, explain the request flow and describe one test that proves it works.

## 1. Core technical questions

### Q1. What is user registration?
**Answer:** Registration creates a new user account after validating submitted account details. Django's UserCreationForm provides standard username and password confirmation behavior and saves the password through Django's user-creation workflow.

### Q2. What is login?
**Answer:** Login verifies credentials and establishes an authenticated session. It uses authentication backends to check the submitted username/password and associates the accepted user with the current request session.

### Q3. What is logout?
**Answer:** Logout ends the current authenticated session. Subsequent requests from that browser should be treated as anonymous unless the user signs in again.

### Q4. What is the difference between registration and login?
**Answer:** Registration creates an account. Login uses an existing account to establish an authenticated session.

### Q5. What does UserCreationForm provide?
**Answer:** It provides standard account creation fields, password confirmation and validation. It avoids manually implementing common password rules and password storage behavior.

### Q6. What is a bound form?
**Answer:** A bound form has submitted data attached to it, for example UserCreationForm(request.POST). It can be validated. An unbound form is commonly displayed before submission.

### Q7. What does form.is_valid() do?
**Answer:** It runs field and form validation. It returns True when the submitted data is valid and False when errors exist. Errors are available through the form for display in the template.

### Q8. What does form.save() do for UserCreationForm?
**Answer:** It creates and saves the user using the form's user-creation logic. Password handling is delegated to Django's password-setting workflow.

### Q9. What does authenticate() do?
**Answer:** It asks the configured authentication backends to verify the credentials. It returns a user object when authentication succeeds and None when the credentials are not accepted.

### Q10. What does login() do?
**Answer:** It associates the authenticated user with the current request session. It does not validate the password; authenticate() performs that responsibility.

### Q11. Why must authenticate() happen before login()?
**Answer:** The application must verify the credentials before establishing an authenticated session. Calling login() with an arbitrary user object would bypass the intended credential check.

### Q12. Why should login errors be generic?
**Answer:** A message such as "Invalid username or password" avoids revealing whether a username exists. Detailed messages can help attackers enumerate accounts.

### Q13. Why use POST for logout?
**Answer:** Logout changes server-side authentication state. GET requests should be safe and should not perform state-changing operations. Use a POST form with a CSRF token.

### Q14. What does require_POST do?
**Answer:** It restricts a view to POST requests. A GET request to a POST-only view normally receives HTTP 405 Method Not Allowed.

### Q15. What does the CSRF token do?
**Answer:** It helps Django verify that a state-changing browser form submission originated from a page that received the expected token. It does not replace authentication or authorization.

## 2. Code and debugging questions

### Q16. Why does form validation fail when passwords differ?
**Answer:** UserCreationForm checks that the password and confirmation match. The bound form contains the error and should be rendered again so the learner can see it.

### Q17. Why does login always return None?
**Answer:** Check the submitted field names, username, password, account active status and configured authentication backend. Also confirm the user was created through Django's password APIs.

### Q18. Why is a login page returning NoReverseMatch?
**Answer:** A template or redirect refers to a URL name that does not exist or is misspelled. Inspect profiles/urls.py and config/urls.py.

### Q19. Why does logout return 405?
**Answer:** The view is intentionally restricted to POST, but the browser sent GET. Use a POST form with {% csrf_token %}.

### Q20. Why does CSRF verification fail?
**Answer:** Check that the POST form includes {% csrf_token %}, CsrfViewMiddleware is enabled, and the request is submitted through the expected browser flow. Do not disable CSRF as a shortcut.

## 3. Scenario questions

### Q21. Registration succeeds but the user cannot log in.
**Answer:** Verify the username and password, account active status, authentication backend and password creation workflow. Confirm the form saved the account in the same database used by the login view.

### Q22. A developer logs the submitted password to debug login.
**Answer:** This is unsafe. Passwords must not be written to logs or screenshots. Log a safe event identifier and investigate the authentication flow without exposing credentials.

### Q23. A GET request logs a user out.
**Answer:** Replace the GET link with a POST form, add a CSRF token and restrict the view to POST.

### Q24. An anonymous visitor can open the account page.
**Answer:** Protect the view with login_required and verify the login URL exists. Test direct URL access, not only whether a link is hidden.

## 4. Mini-project discussion — User Authentication Application

Demonstrate:
1. Registration page.
2. Valid registration.
3. Duplicate username error.
4. Password mismatch error.
5. Valid login.
6. Invalid login.
7. Protected account page.
8. POST logout.
9. Attempt to access the account page after logout.

## 5. Readiness checklist

- [ ] I can explain UserCreationForm.
- [ ] I can explain bound and unbound forms.
- [ ] I can explain authenticate() and login().
- [ ] I can explain logout().
- [ ] I can explain CSRF protection.
- [ ] I can explain why logout is POST-only.
- [ ] I can test successful and failed authentication.
- [ ] I can demonstrate User Authentication Application.

**Related notes:** [Day 47 class notes](day_47_notes.md)
