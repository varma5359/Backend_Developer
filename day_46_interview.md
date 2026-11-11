# Day 46: Interview Guide — Django Authentication System and User Model

**Related class notes:** [Day 46 notes](day_46_notes.md)  
**Approved mini-project:** User Account Management  
**Level:** Beginner to Intermediate

## How to use this guide
Try to answer each question aloud before reading the model answer. Explain the concept, show the related code, and describe how you would test it. Do not memorize answers word for word.

## 1. Core technical questions

### Q1. What is authentication?
**Answer:** Authentication verifies the identity associated with a request. In a web application, a user commonly submits credentials such as a username and password. Django checks those credentials through its authentication backend. If they are accepted, Django can associate the request with the authenticated account.

**Follow-up:** Is authentication the same as authorization?  
**Answer:** No. Authentication answers who the user is. Authorization decides what that user may do.

### Q2. What is Django's user model?
**Answer:** It is the model representing user accounts. The default user model includes fields and behavior for usernames, passwords, names, email, account status, staff status, superuser status and permissions.

**Follow-up:** Does the user model render a login page?  
**Answer:** No. A form, view, URL and template provide the login workflow.

### Q3. What is the purpose of get_user_model()?
**Answer:** It returns the user model configured for the active Django project. It avoids hard-coding an assumption that the project always uses Django's default User class.

**Example:**
```python
from django.contrib.auth import get_user_model
User = get_user_model()
```

### Q4. When should settings.AUTH_USER_MODEL be used?
**Answer:** Use it as the target when declaring a model relationship to the configured user model, for example a ForeignKey or OneToOneField. Runtime Python code normally uses get_user_model().

### Q5. What does request.user represent?
**Answer:** It is the user associated with the current HTTP request. If the visitor is not signed in, it represents an anonymous user. If the visitor is signed in, it represents the authenticated account.

### Q6. What is AnonymousUser?
**Answer:** It is Django's representation of an unauthenticated visitor. It allows views and templates to check authentication status without treating the user as a missing object.

### Q7. What is the difference between is_active, is_staff and is_superuser?
**Answer:** is_active indicates whether an account is active. is_staff marks eligibility to access the Django admin site, subject to permissions. is_superuser grants all permissions by default. These flags have different responsibilities and should not be treated as interchangeable.

### Q8. Why must passwords not be stored as plain text?
**Answer:** If a database is exposed, plain-text passwords can be read immediately. Django stores a password hash and verifies submitted candidates using password-checking APIs. Application code should never display or log the stored password field.

### Q9. Why use create_user()?
**Answer:** The user manager's create_user() method uses Django's password-setting workflow. Directly assigning a raw password string to user.password bypasses the intended hashing process.

### Q10. What does check_password() return?
**Answer:** It returns a Boolean. True means the candidate matches the stored hash; False means it does not. It does not reveal the original password.

### Q11. What does login_required do?
**Answer:** It protects a view from anonymous access. An unauthenticated visitor is redirected to the configured login URL. It does not check whether a user owns a particular object or has a particular permission.

### Q12. Which middleware makes request.user available?
**Answer:** AuthenticationMiddleware. It relies on session middleware, which must appear earlier in the standard middleware ordering.

## 2. Code and debugging questions

### Q13. What is wrong with this code?
```python
user = User(username="student1", password="MyPassword")
user.save()
```
**Answer:** The raw password is assigned directly to the password field. Use User.objects.create_user() or user.set_password() followed by save().

### Q14. Why might User.objects.get(username="student1") fail?
**Answer:** The record may not exist, the wrong database/environment may be active, or the username may be misspelled. get() raises DoesNotExist when there is no match and MultipleObjectsReturned when more than one row matches.

### Q15. Why does request.user raise an attribute/configuration error?
**Answer:** Check that django.contrib.auth is installed, AuthenticationMiddleware is enabled, SessionMiddleware appears before it, and the view is receiving a Django HttpRequest.

### Q16. Why can an anonymous redirect fail with NoReverseMatch?
**Answer:** login_required needs a valid LOGIN_URL. If LOGIN_URL refers to a route name that has not been created or is misspelled, Django cannot reverse the destination. Day 47 creates the application login route.

## 3. Scenario questions

### Q17. A student can open another student's profile by changing an ID in the URL. What is wrong?
**Answer:** The view is trusting an object identifier without checking ownership. For the current account page, use request.user. For another object, query it within the current user's allowed scope or check the relevant permission.

### Q18. A developer made every registered user a superuser so pages work. Is this acceptable?
**Answer:** No. It grants all permissions and defeats access control. Create ordinary users and assign only the required permissions or groups.

### Q19. A developer wants to add a phone number to an already migrated application. Must they create a custom user model?
**Answer:** Not necessarily. If the phone number is optional profile information, a separate profile model may be more appropriate. Changing the user model after migrations can be complex.

### Q20. A learner sees a long string in the password field. Is the password corrupted?
**Answer:** Not necessarily. Django stores an encoded password hash rather than the original readable password. Verify it with check_password().

## 4. Mini-project discussion — User Account Management

Be ready to demonstrate:
1. The configured user model API.
2. A fictional test account.
3. The account summary view.
4. request.user and is_authenticated.
5. login_required behavior after Day 47 is complete.
6. Why the password is never displayed.
7. The tests for authenticated access.

## 5. Quick practical tasks

- Create a test user using create_user().
- Verify correct and incorrect passwords.
- Query active users.
- Explain is_staff versus is_superuser.
- Protect a view using login_required.
- Explain why a separate profile model may be useful.

## 6. Readiness checklist

- [ ] I can explain authentication versus authorization.
- [ ] I can explain the user model and status flags.
- [ ] I can use get_user_model() and AUTH_USER_MODEL correctly.
- [ ] I can explain request.user.
- [ ] I can explain password hashing.
- [ ] I can protect a page.
- [ ] I can diagnose a missing login URL.
- [ ] I can demonstrate User Account Management.

**Related notes:** [Day 46 class notes](day_46_notes.md)
