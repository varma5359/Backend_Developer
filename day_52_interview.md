# Day 52: Interview Questions — Django Messages Framework and Application Feedback

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 52 class notes](day_52_notes.md)  
**Approved mini-project:** User Notification Application

## Core technical questions

### Q1. Explain django messages framework and application feedback.
**Answer:** The messages framework lets a Django application display one-time feedback after an action, such as a successful save or an error. Messages are commonly stored using session or cookie-based storage and displayed in templates. They are useful for user feedback but are not a replacement for persistent notifications.

### Q2. Which Django components are involved?
**Answer:** profiles/views.py, profiles/templates/base.html. Explain how each component contributes to the feature.

### Q3. What is one common implementation mistake?
**Answer:** A success message appears after a successful save. Test the feature with realistic data and verify the database result.

### Q4. How do you verify the user workflow?
**Answer:** Use separate test accounts, submit valid and invalid inputs, inspect the response and verify the stored records.

### Q5. What production concern should you mention?
**Answer:** Data integrity, permissions, privacy, secure configuration and integration test coverage.

## Scenario questions

### Q6. A feature works for one user but fails for another. What do you inspect?
**Suggested answer:** Check the active user model, group membership, permissions, session, request context and database ownership rules.

### Q7. How do you prevent the browser from choosing a protected owner field?
**Suggested answer:** Exclude the field from the user-facing form and assign it server-side from request.user.

## Project viva — User Notification Application

1. What is the business problem?
2. Which models and relationships are used?
3. Which form fields are exposed?
4. How is authentication or ownership handled?
5. Which database constraints are important?
6. How are valid and invalid journeys tested?
7. What would you improve for production?

## Rapid revision

- **1.** Confirm messages app and middleware are configured.
- **2.** Import django.contrib.messages in the view.
- **3.** Add success, info, warning or error messages after relevant actions.
- **4.** Redirect after successful POST.
- **5.** Loop through messages in a shared base template.
- **6.** Use message tags to style feedback.
- **7.** Test that messages appear once and then disappear.
- **8.** Do not store permanent business notifications only in messages.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Identify connected Django components.
- [ ] Demonstrate a complete workflow.
- [ ] Explain validation and permissions.
- [ ] Present User Notification Application and evidence.
