# Day 52: Django Messages Framework and Application Feedback

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 3–4 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–51 — Django views, templates, forms, redirects, authentication, sessions, permissions and profiles  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config / profiles  
**Approved mini-project:** User Notification Application

> **Self-learning promise:** You will learn how to give users clear feedback after an action. You will use Django's messages framework to show success, information, warning and error messages across redirects. You will understand middleware, template rendering, message consumption and tests.

---

# PART 1 — WHY APPLICATION FEEDBACK MATTERS

## 1. The problem

Imagine a student updates their profile and clicks Save.

The server saves the record and redirects to the account page.

What should the student see?

Without feedback:
- The page opens again.
- The student is unsure whether the save worked.
- They may submit the form repeatedly.
- They may contact support unnecessarily.

With feedback:
- "Profile updated successfully."
- The user understands what happened.
- The application feels more predictable.

This is application feedback.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain why user feedback is important.
2. Explain the Django messages framework.
3. Identify required apps and middleware.
4. Understand message levels.
5. Add messages from a view.
6. Display messages in a template.
7. Understand why messages are useful with redirects.
8. Understand how messages are consumed.
9. Explain the difference between temporary messages and persistent notifications.
10. Use success, info, warning, error and debug levels.
11. Customize message tags.
12. Avoid duplicate or stale feedback.
13. Test message behavior.
14. Complete User Notification Application.

## 3. Important words

| Term | Simple meaning |
|---|---|
| Feedback | Information shown after a user action |
| Message | A short piece of temporary feedback |
| Message level | Category describing the importance/type of a message |
| Middleware | Component that processes requests and responses |
| Redirect | Response that sends browser to another URL |
| Template | File that renders HTML |
| Message storage | Mechanism Django uses to keep messages temporarily |
| Message tag | CSS-friendly label associated with a message level |
| Persistent notification | Notification saved for later viewing |
| Flash message | Temporary message shown once or for a short period |

## 4. Feedback examples

| User action | Appropriate feedback |
|---|---|
| Account created | Your account has been created |
| Profile saved | Profile updated successfully |
| Invalid form | Please correct the highlighted fields |
| Password changed | Your password has been updated |
| Item removed | Product removed from cart |
| Permission denied | You do not have permission to perform this action |
| Search has no results | No matching records were found |

A message should be clear and truthful. Do not say "Saved successfully" before the database operation succeeds.

---

# PART 2 — UNDERSTAND THE MESSAGES FRAMEWORK

## 5. What is Django messages?

Django's messages framework lets a view create a short message that can be displayed to the user in a later response.

It is especially useful when a view:
1. Receives a POST request.
2. Performs an action.
3. Adds a message.
4. Redirects to another page.
5. The next page displays the message.

This is commonly called a flash-message pattern.

## 6. Why not just pass a context variable?

A context variable is passed to the template for the current response.

Example:

~~~python
return render(
    request,
    "profiles/profile.html",
    {"message": "Profile saved"},
)
~~~

If the view redirects instead of rendering that template, the context dictionary is not automatically carried to the next request.

Django messages provide temporary cross-request feedback.

## 7. Message flow

~~~text
Browser submits form
       |
       v
Django view validates input
       |
       v
Database operation succeeds
       |
       v
messages.success(request, "Saved")
       |
       v
redirect("account_summary")
       |
       v
Browser requests account summary
       |
       v
Template reads messages
       |
       v
User sees feedback
~~~

## 8. Where messages are stored

Django uses a configured message storage backend.

The default setup commonly uses session-backed message storage with cookie/session support.

The messages framework does not mean messages are permanently stored in a notification database table.

Messages are temporary feedback, not a replacement for a notification model.

## 9. Required app

Open config/settings.py.

Confirm:

~~~python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
]
~~~

The messages app must be installed.

## 10. Required middleware

Confirm MessageMiddleware is present:

~~~python
"django.contrib.messages.middleware.MessageMiddleware",
~~~

It normally appears after SessionMiddleware.

The messages framework uses request/response processing to load and store temporary messages.

## 11. Required template context processor

In TEMPLATES OPTIONS context_processors, confirm:

~~~python
"django.contrib.messages.context_processors.messages",
~~~

This makes the messages collection available to templates.

Do not add the same context processor twice.

## 12. Standard configuration summary

| Component | Expected configuration |
|---|---|
| App | django.contrib.messages |
| Middleware | MessageMiddleware |
| Context processor | messages |
| Session support | django.contrib.sessions |
| Template | Iterates over messages |

If any part is missing, the message may not be available where expected.

---

# PART 3 — MESSAGE LEVELS

## 13. What is a message level?

A message level describes the type or importance of feedback.

Django provides levels such as:
- DEBUG
- INFO
- SUCCESS
- WARNING
- ERROR

## 14. Success message

Use success when an operation completes successfully.

~~~python
from django.contrib import messages

messages.success(
    request,
    "Your profile was updated successfully.",
)
~~~

Examples:
- Profile saved.
- Product added.
- Account created.
- Password changed.

Do not use success before the database save succeeds.

## 15. Info message

Use info for a neutral update.

~~~python
messages.info(
    request,
    "Your account settings are ready to review.",
)
~~~

Examples:
- A page has been refreshed.
- A new step is available.
- A user should review a setting.

## 16. Warning message

Use warning when the action can continue but the user should pay attention.

~~~python
messages.warning(
    request,
    "Your profile is missing an optional contact number.",
)
~~~

Examples:
- A field is incomplete.
- A session will expire soon.
- Some results are unavailable.

## 17. Error message

Use error when an operation failed.

~~~python
messages.error(
    request,
    "The profile could not be saved.",
)
~~~

Examples:
- A server-side operation failed.
- An action could not be completed.
- A resource is unavailable.

Do not expose stack traces or internal database errors to the user.

## 18. Debug message

DEBUG is intended for development-level information.

~~~python
messages.debug(
    request,
    "Profile validation completed.",
)
~~~

Debug messages may be filtered by the configured message level. They should not be used to expose secrets or sensitive implementation details.

## 19. Level comparison

| Level | Purpose | Example |
|---|---|---|
| DEBUG | Diagnostic detail | Validation branch completed |
| INFO | Neutral information | Review your account settings |
| SUCCESS | Completed action | Profile saved |
| WARNING | Attention needed | Optional information missing |
| ERROR | Operation failed | Could not update profile |

## 20. Use the constants directly

Django exposes message level constants through messages.

Example:

~~~python
messages.add_message(
    request,
    messages.SUCCESS,
    "Profile saved.",
)
~~~

The shortcut is:

~~~python
messages.success(request, "Profile saved.")
~~~

Both approaches add a message. The shortcut is usually easier to read.

---

# PART 4 — ADD MESSAGES TO A VIEW

## 21. Import messages

In profiles/views.py:

~~~python
from django.contrib import messages
~~~

Do not confuse:
- messages: the imported framework module.
- message: one item displayed to the user.

## 22. Add a success message after saving

Example profile update view:

~~~python
@login_required
def edit_student_profile(request):
    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = StudentProfileForm(
            request.POST,
            instance=profile,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile was updated successfully.",
            )
            return redirect("account_summary")
    else:
        form = StudentProfileForm(instance=profile)

    return render(
        request,
        "profiles/edit_student_profile.html",
        {"form": form},
    )
~~~

This example assumes StudentProfile and StudentProfileForm already exist from the previous lesson.

## 23. Why add the message after form.save()?

Correct order:
1. Validate the form.
2. Save the form.
3. Add success message.
4. Redirect.

If the save operation fails, the success message should not be shown.

## 24. Add an error message

Example:

~~~python
if form.is_valid():
    form.save()
    messages.success(request, "Profile saved.")
    return redirect("account_summary")

messages.error(
    request,
    "Please correct the errors shown below.",
)
~~~

The bound form must still be rendered so field-level validation errors remain visible.

A message should not replace the actual field errors.

## 25. Add an info message

~~~python
messages.info(
    request,
    "You can update your profile information at any time.",
)
~~~

Use this when the information is helpful but not a success or failure.

## 26. Add a warning message

~~~python
if not profile.phone_number:
    messages.warning(
        request,
        "Adding a phone number can help with account recovery.",
    )
~~~

Do not show repeated warnings on every request without a reason. Repeated messages can annoy users.

## 27. Use a generic error message

Do not do this:

~~~python
messages.error(request, str(database_exception))
~~~

Database exceptions may expose internal table names, SQL, paths or implementation details.

Prefer a safe message:

~~~python
messages.error(
    request,
    "We could not complete your request. Please try again.",
)
~~~

Log technical details securely on the server when needed.

---

# PART 5 — DISPLAY MESSAGES IN A TEMPLATE

## 28. Create a reusable message area

A message area can be placed in a base template so that every page using the base template can display messages.

Open the shared base template, if your project has one.

Add this block near the top of the main content:

~~~django
{% if messages %}
    <div class="messages" aria-live="polite">
        {% for message in messages %}
            <div class="message {{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}
~~~

## 29. Explain the template

{% if messages %}:
- Checks whether the collection contains messages.

{% for message in messages %}:
- Loops over every message.

message.tags:
- Provides a CSS-friendly tag for the message level.

{{ message }}:
- Displays the message text.

aria-live="polite":
- Helps assistive technologies announce updates without interrupting the user abruptly.

## 30. What happens after a message is displayed?

Django's message storage is designed for temporary messages.

As messages are iterated and the response completes, the storage marks them for removal according to the storage backend's behavior.

This is why messages are commonly displayed once after a redirect.

Do not expect a message to remain permanently visible on every later page.

## 31. Display message tags

The message tag can be used for CSS styling.

Common tags correspond to levels:
- debug
- info
- success
- warning
- error

The exact tag behavior can be customized.

## 32. Add simple CSS

If the project has a static CSS file, add:

~~~css
.messages {
    margin: 1rem 0;
}

.message {
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
    border: 1px solid #cccccc;
    border-radius: 4px;
}

.message.success {
    border-left-width: 4px;
}

.message.error {
    border-left-width: 4px;
}

.message.warning {
    border-left-width: 4px;
}

.message.info {
    border-left-width: 4px;
}
~~~

This is a simple demonstration. A production design should provide clear visual contrast and accessible text.

## 33. Do not rely only on color

A success or error state should also have readable text.

Users with color-vision differences or screen readers must be able to understand the message.

Use clear words such as:
- Saved successfully.
- Could not save.
- Attention required.

---

# PART 6 — MESSAGE TAGS AND LEVELS

## 34. Set a minimum message level

Django supports a configured minimum message level.

Messages below that level may not be stored.

This is useful when DEBUG messages should not appear to ordinary users.

## 35. Configure MESSAGE_LEVEL

In config/settings.py:

~~~python
from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.INFO
~~~

This means messages at INFO and higher levels are eligible.

Do not add imports in the middle of settings.py if the project already groups imports at the top. Keep settings organized.

## 36. Understand level ordering

Django message levels are numeric values.

Higher levels represent more important messages.

A minimum level filters lower-priority messages.

For example, if the minimum is INFO:
- DEBUG may be filtered.
- INFO is included.
- SUCCESS is included.
- WARNING is included.
- ERROR is included.

## 37. Customize tags

Django allows MESSAGE_TAGS to map levels to CSS tags.

Example:

~~~python
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.DEBUG: "debug",
    message_constants.INFO: "notice",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "error",
}
~~~

If you customize tags, update your CSS to use the new names.

## 38. Why tags are not security controls

A CSS class such as error does not enforce any permission.

It only changes presentation.

Authorization belongs in the backend view.

---

# PART 7 — MESSAGES WITH REDIRECTS

## 39. What is the POST/Redirect/GET pattern?

A common browser workflow is:
1. Browser sends POST.
2. Server processes the form.
3. Server redirects to a GET URL.
4. Browser loads the result page.

This is commonly called Post/Redirect/Get.

It helps prevent accidental duplicate form submission when the user refreshes the result page.

## 40. Where messages fit

The message is added before the redirect.

The next request reads the message.

~~~text
POST /profile/edit/
      |
      v
Save profile
      |
      v
Add success message
      |
      v
302 Redirect to /account/
      |
      v
GET /account/
      |
      v
Render message in base template
~~~

## 41. Do not add the same message twice

A common beginner mistake is adding a message in both:
- The POST view.
- The redirected GET view.

The user may see duplicate messages.

Add the message at the point where the action succeeds or fails.

## 42. Do not add a success message before validation

Incorrect:

~~~python
messages.success(request, "Saved successfully.")

if form.is_valid():
    form.save()
~~~

This can show a false success message when the form is invalid.

Correct:

~~~python
if form.is_valid():
    form.save()
    messages.success(request, "Saved successfully.")
    return redirect("account_summary")
~~~

## 43. Use messages for authentication feedback

After successful registration:

~~~python
messages.success(
    request,
    "Your account has been created. You can now sign in.",
)
~~~

After successful login:

~~~python
messages.success(
    request,
    "You are now signed in.",
)
~~~

After logout:

~~~python
messages.success(
    request,
    "You have signed out.",
)
~~~

Do not reveal sensitive login details through messages.

---

# PART 8 — MESSAGE STORAGE AND LIMITATIONS

## 44. Temporary message versus persistent notification

A message is normally short-lived feedback.

A persistent notification is stored in a database and may remain available until the user reads or dismisses it.

Examples of persistent notifications:
- New assignment published.
- Fee due next week.
- New support response.
- Account approval completed.
- Important policy update.

Django messages are not designed to replace a full notification system.

## 45. When should you create a Notification model?

Use a database model when the application needs:
- Notification history.
- Unread/read state.
- User-specific notification list.
- Delivery timestamps.
- Expiry or archive rules.
- Notification preferences.

The Day 52 project focuses on the messages framework. A persistent notification model is an extension, not a requirement.

## 46. Message storage backends

Django includes different message storage options.

Common examples:
- SessionStorage.
- CookieStorage.
- FallbackStorage.

The default setup commonly uses FallbackStorage, which uses cookie storage where possible and session storage as needed.

Do not assume message contents are a permanent database record.

## 47. Message size and purpose

Messages should be short.

Do not use them to:
- Transfer large objects between pages.
- Store full reports.
- Store secrets.
- Persist application records.
- Replace a database model.

Use messages for concise feedback only.

---

# PART 9 — BUILD USER NOTIFICATION APPLICATION

## 48. Project scenario

A training institute wants users to receive clear feedback when they:
- Register.
- Sign in.
- Sign out.
- Update their profile.
- Submit invalid data.
- Attempt an action without permission.

The application will use Django messages for temporary feedback.

## 49. Files used

- config/settings.py
- profiles/views.py
- profiles/templates/profiles/base.html (if used)
- profiles/templates/profiles/account_summary.html
- profiles/templates/profiles/edit_student_profile.html
- profiles/tests.py
- profiles/static/profiles/messages.css (optional)

Do not create duplicate templates if your existing project already has a shared base template.

## 50. Create a base template if needed

Create profiles/templates/profiles/base.html:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Student Portal{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Student Portal</h1>
    </header>

    {% if messages %}
        <section class="messages" aria-live="polite">
            {% for message in messages %}
                <div class="message {{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        </section>
    {% endif %}

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
~~~

## 51. Extend the base template

A page can use:

~~~django
{% extends "profiles/base.html" %}

{% block title %}My Account{% endblock %}

{% block content %}
    <h2>My Account</h2>
    <p>Welcome to your account page.</p>
{% endblock %}
~~~

This avoids repeating the message loop on every page.

If your project already has a base template, add the message block to it instead.

## 52. Add a success message to profile update

Use the profile view from Day 51.

After form.save():

~~~python
messages.success(
    request,
    "Your profile was updated successfully.",
)
~~~

Then redirect to the account page.

## 53. Add an error message for invalid submission

If the form is invalid:

~~~python
messages.error(
    request,
    "Please review the form errors and try again.",
)
~~~

Return the bound form to the template so the exact field errors remain visible.

## 54. Add an informational message

Example:

~~~python
messages.info(
    request,
    "You can update your profile whenever your details change.",
)
~~~

This message can be displayed when a user opens a page or completes a workflow.

Use it sparingly.

## 55. Add a warning message

Example:

~~~python
if not profile.phone_number:
    messages.warning(
        request,
        "Add a contact number if your institute requires one.",
    )
~~~

Avoid showing the same warning on every page request. Consider showing it only after a relevant action or on the profile page.

## 56. Add a message after permission denial

A permission-denied response may be handled by Django's 403 error page.

If you redirect instead, use a safe message:

~~~python
messages.error(
    request,
    "You do not have permission to perform this action.",
)
return redirect("account_summary")
~~~

Do not reveal internal permission names to ordinary users.

---

# PART 10 — TEST THE MESSAGES FRAMEWORK

## 57. Manual test plan

| Test | Action | Expected result |
|---|---|---|
| Success message | Save a valid profile | Success feedback appears after redirect |
| Invalid form | Submit invalid values | Field errors remain visible |
| Error message | Trigger a handled failure | Safe error feedback appears |
| Warning message | Open a page with missing optional data | Warning appears according to the view logic |
| Info message | Complete the relevant workflow | Informational feedback appears |
| One-time behavior | Refresh after message was consumed | Same message does not keep reappearing |
| Multiple messages | Add two messages before redirect | Both display in order |
| Message level | Set minimum INFO and add DEBUG | DEBUG may be filtered |

## 58. Add automated tests

Django provides the test client and message storage access.

In profiles/tests.py, add or merge:

~~~python
from django.contrib import messages
from django.contrib.messages import get_messages
from django.test import TestCase, RequestFactory


class MessageFrameworkTests(TestCase):
    def test_success_message_is_added(self):
        request = RequestFactory().get("/")
        request.session = {}
        request._messages = messages.storage.default_storage(request)

        messages.success(request, "Profile saved successfully.")

        stored = list(get_messages(request))

        self.assertEqual(len(stored), 1)
        self.assertEqual(
            str(stored[0]),
            "Profile saved successfully.",
        )
        self.assertEqual(
            stored[0].level,
            messages.SUCCESS,
        )
~~~

This is a focused storage test. RequestFactory does not automatically install session and message middleware, so the test explicitly prepares the storage dependencies. In request-level integration tests, use Django's test client and the real middleware configuration.

## 59. Test a view response with messages

If the profile update route exists, use the test client to:
1. Create a user.
2. Create or retrieve their profile.
3. Sign in using force_login().
4. Submit valid form values.
5. Check the redirect.
6. Follow the redirect.
7. Inspect response.context["messages"] or the rendered message text.

The exact form fields must match StudentProfileForm in your project.

## 60. Run tests

~~~powershell
python manage.py check
python manage.py test profiles
~~~

Read the output and correct import or configuration errors.

---

# PART 11 — COMMON ERRORS

## 61. Message does not appear

Check:
- django.contrib.messages is installed.
- MessageMiddleware is enabled.
- The messages context processor is enabled.
- The view uses messages.success() or another message helper.
- The template iterates over messages.
- The response follows the expected request flow.

## 62. Message appears twice

Check:
- Is the message added in both POST and GET views?
- Does a redirect chain cause the same action to run again?
- Is the template rendering the message block twice?
- Is the browser refreshing a response unexpectedly?

Add the message once at the correct point.

## 63. Message disappears immediately

Possible reasons:
- The message was consumed by an earlier response.
- A template iterated over messages before the expected page.
- Middleware or context processor configuration is missing.
- A redirect or request flow consumed the message.

Inspect the full sequence of requests.

## 64. Template cannot find messages

Check:
- messages context processor.
- Correct template inheritance.
- Correct block placement.
- Correct TEMPLATES setting.
- The template is rendered through a normal Django request.

## 65. CSS class is not applied

Check:
- message.tags output.
- MESSAGE_TAGS custom mapping.
- CSS selector names.
- Static file path and load.
- Browser cache.

A tag mismatch affects styling, not message storage.

## 66. Message is too technical

Do not display:
- Traceback.
- SQL statement.
- Python exception class.
- Database table names.
- Internal file paths.
- Tokens or session identifiers.

Use a clear user-facing message and log technical information securely on the server.

---

# PART 12 — APPROVED MINI-PROJECT

## 67. User Notification Application

### Business problem

A student portal must provide clear feedback after important actions.

### Functional requirements

1. Display messages in a reusable base template.
2. Show success after profile update.
3. Show an error after invalid submission.
4. Show info when useful.
5. Show warning when attention is needed.
6. Display messages after redirects.
7. Avoid duplicate messages.
8. Use accessible markup.
9. Keep messages concise.
10. Do not expose internal errors or secrets.
11. Test message level and text.
12. Explain why messages are temporary rather than persistent notifications.

### Acceptance criteria

- [ ] Messages app is installed.
- [ ] MessageMiddleware is enabled.
- [ ] Context processor is enabled.
- [ ] Base template displays messages.
- [ ] Success feedback appears after a successful action.
- [ ] Invalid form errors remain visible.
- [ ] Multiple messages display correctly.
- [ ] Message behavior after refresh is understood.
- [ ] Tests pass.
- [ ] No secret or traceback is shown to users.

### Submission evidence

- Updated settings.
- Updated views.
- Base template.
- Browser screenshot of success feedback.
- Browser screenshot of validation feedback.
- Automated test output.
- README describing the message flow.

---

# PART 13 — SELF-ASSESSMENT

## 68. Short-answer questions

1. Why does an application need user feedback?
2. What is the Django messages framework?
3. Why are messages useful after redirects?
4. Which app must be installed?
5. Which middleware is required?
6. Which context processor exposes messages to templates?
7. Name the five common message levels.
8. What does messages.success() do?
9. What does message.tags provide?
10. Why should a success message be added after save?
11. Why should messages not replace field-level form errors?
12. Why should messages not be used as a permanent notification database?
13. What is the POST/Redirect/GET pattern?
14. Why can duplicate messages appear?
15. Why should technical exceptions not be displayed to users?

## 69. Self-check answers

1. It tells users what happened after an action.
2. It provides temporary messages that can be displayed across requests.
3. Context data does not automatically survive a redirect; messages do.
4. django.contrib.messages.
5. MessageMiddleware.
6. django.contrib.messages.context_processors.messages.
7. DEBUG, INFO, SUCCESS, WARNING and ERROR.
8. It adds a success-level message to the request.
9. It provides a CSS-friendly level tag.
10. Otherwise the application may claim success when saving failed.
11. Field errors explain exactly which values need correction.
12. Messages are temporary and are not designed for long-term history.
13. Submit POST, process it, redirect, then render a GET page.
14. The view may add the same message in more than one request or template.
15. Exceptions can expose internal details and sensitive data.

## 70. MCQ assessment

### Question 1
Which Django helper adds a success message?

- A. messages.success()
- B. messages.save()
- C. messages.redirect()
- D. messages.user()

**Answer: A.** It adds a success-level message.

### Question 2
Which middleware supports the messages framework?

- A. AuthenticationMiddleware
- B. MessageMiddleware
- C. SecurityMiddleware only
- D. CommonMiddleware only

**Answer: B.** MessageMiddleware loads and stores messages during request/response processing.

### Question 3
Where should messages normally be displayed?

- A. In a reusable template area
- B. In the database password field
- C. In settings.py only
- D. In the URL path

**Answer: A.** A shared base template can display messages consistently.

### Question 4
What is a success message for?

- A. An action that completed successfully
- B. An exception traceback
- C. A password hash
- D. A database migration file

**Answer: A.** It should be added only after the action succeeds.

### Question 5
Are Django messages a replacement for a persistent notification model?

- A. Yes, always
- B. No
- C. Only on Windows
- D. Only when using PostgreSQL

**Answer: B.** Messages are temporary feedback; persistent notification history needs a suitable model or service.

---

# PART 14 — INTERVIEW PREPARATION

## 71. What is Django's messages framework?

**Answer:** It provides temporary feedback that can be added in one request and displayed in a later response, commonly after a redirect. It supports levels such as success, info, warning and error.

**Follow-up:** Which middleware is required?

**Answer:** MessageMiddleware.

## 72. Why use messages with redirects?

**Answer:** A redirect starts another browser request. A normal context dictionary is not automatically carried to that request. Django messages provide temporary cross-request feedback.

**Follow-up:** Does a message remain permanently?

**Answer:** No. Messages are temporary and are normally consumed when displayed.

## 73. What is the difference between messages and notifications?

**Answer:** Messages are short-lived feedback such as "Profile saved". Persistent notifications are stored as application data and may have read/unread state and history.

**Follow-up:** Which should be used for a new assignment alert that must remain visible?

**Answer:** A persistent notification model or notification service is more appropriate.

## 74. Scenario: success message appears even when saving fails

**Answer:** The message is added before the save or validation completes. Add it only after the operation succeeds.

## 75. Scenario: the same message appears twice

**Answer:** Check whether the message is added in both the POST and redirected GET view, or whether the template renders the message collection twice.

---

# PART 15 — INDEPENDENT COMPLETION

## 76. Draw the message lifecycle

Include:
1. User action.
2. View validation.
3. Database operation.
4. Add message.
5. Redirect.
6. Next request.
7. Template reads message.
8. Message is consumed.

## 77. Controlled debugging

In a local copy:
- Remove MessageMiddleware and inspect the configuration failure.
- Restore it.
- Remove the context processor and inspect template behavior.
- Restore it.
- Add a message before validation and observe why it is misleading.
- Move the success message after save.
- Render the message block twice and identify duplicate output.

Do not leave intentional mistakes in the final branch.

## 78. Final checklist

- [ ] I understand why feedback is needed.
- [ ] I understand the messages framework.
- [ ] I configured the app, middleware and context processor.
- [ ] I can add success, info, warning and error messages.
- [ ] I can display messages in a template.
- [ ] I understand messages after redirects.
- [ ] I understand message consumption.
- [ ] I know when to use persistent notifications instead.
- [ ] I tested message behavior.
- [ ] I completed User Notification Application.
- [ ] I ran automated tests.
- [ ] I completed the MCQ and interview assessment.

**Next lesson:** Day 53 — Pagination, Search and Filtering in Django Applications.

---

## 79. Official references

1. Django messages framework: https://docs.djangoproject.com/en/5.2/ref/contrib/messages/
2. Django messages settings: https://docs.djangoproject.com/en/5.2/ref/settings/
3. Django templates: https://docs.djangoproject.com/en/5.2/topics/templates/
4. Django testing: https://docs.djangoproject.com/en/5.2/topics/testing/tools/

**Version reminder:** This lesson targets Django 5.2.19. Check the project's existing middleware and base template before adding duplicate configuration.
