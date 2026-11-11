# Day 52: Interview Guide — Django Messages Framework and Application Feedback

**Related class notes:** [Day 52 notes](day_52_notes.md)  
**Approved mini-project:** User Notification Application  
**Level:** Beginner to Intermediate

## 1. Core technical questions

### Q1. What is Django's messages framework?
**Answer:** It provides temporary feedback that can be added during one request and displayed in a later response. It is commonly used after a form submission and redirect.

### Q2. Why are messages useful after redirects?
**Answer:** A context dictionary belongs to the current response and is not automatically carried to the next request. Messages provide temporary cross-request feedback.

### Q3. Which app must be installed?
**Answer:** django.contrib.messages.

### Q4. Which middleware is required?
**Answer:** MessageMiddleware. It participates in loading and storing messages during request/response processing.

### Q5. Which context processor makes messages available to templates?
**Answer:** django.contrib.messages.context_processors.messages.

### Q6. What are the common message levels?
**Answer:** DEBUG, INFO, SUCCESS, WARNING and ERROR.

### Q7. What does messages.success() do?
**Answer:** It adds a success-level message to the current request's message storage.

### Q8. What does message.tags provide?
**Answer:** It provides a CSS-friendly tag associated with the message level. A template can use it to select styling.

### Q9. Why should success feedback be added after saving?
**Answer:** The application should not tell the user that an operation succeeded before the operation has actually completed. Add the success message after a successful save.

### Q10. Are messages a replacement for form field errors?
**Answer:** No. A message can provide general feedback, but field errors explain exactly which values need correction. Render the bound form with its errors.

### Q11. Are messages persistent notifications?
**Answer:** No. They are intended for temporary feedback. A notification history with read/unread state should use a suitable persistent model or notification service.

### Q12. What is Post/Redirect/Get?
**Answer:** The browser submits POST, the server processes the action and redirects, and the browser makes a new GET request. This helps avoid accidental duplicate form submissions on refresh.

## 2. Debugging questions

### Q13. Message does not appear.
**Answer:** Check the installed app, MessageMiddleware, messages context processor, view helper call, template loop and redirect flow.

### Q14. Message appears twice.
**Answer:** The message may be added in both the POST and GET views, or the template may render the message collection more than once.

### Q15. Message disappears before the intended page.
**Answer:** Inspect whether an earlier response iterated over the messages, whether the message storage was consumed, and whether middleware and context processor are configured.

## 3. Scenario questions

### Q16. A success message appears even though the database save failed.
**Answer:** The message is added too early. Add it only after validation and save succeed.

### Q17. A developer displays the full database exception to the user.
**Answer:** This may reveal internal details. Display a safe user-facing message and record technical details securely in server logs without secrets.

### Q18. The product needs notifications that remain visible for weeks.
**Answer:** Django messages are not the right storage. Create a persistent notification model with ownership, timestamps and read/unread state.

## 4. Mini-project discussion — User Notification Application

Demonstrate:
1. Message configuration.
2. Reusable base-template message block.
3. Success after a saved profile.
4. Error after invalid input.
5. Warning and info examples.
6. Message behavior after redirect and refresh.
7. Accessible message markup.
8. Tests.

## 5. Readiness checklist

- [ ] I can explain messages and message levels.
- [ ] I know the required app, middleware and context processor.
- [ ] I can add and display messages.
- [ ] I understand message consumption.
- [ ] I can distinguish temporary messages from persistent notifications.
- [ ] I can demonstrate User Notification Application.

**Related notes:** [Day 52 class notes](day_52_notes.md)
