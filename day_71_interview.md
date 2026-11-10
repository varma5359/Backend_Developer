# Day 71: Interview Questions — Email Integration and Sending Application Notifications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 71 class notes](day_71_notes.md)  
**Approved mini-project:** Email Notification Service

## Core technical questions

### Q1. Explain email integration and sending application notifications.
**Answer:** Backend applications send emails for account events, status updates and workflow notifications. Django provides send_mail() and EmailMessage. Email configuration should be externalized and environment-specific. In development, the console email backend can display messages in the terminal without sending real email.

### Q2. Which Django files or libraries are involved?
**Answer:** config/settings.py — local development, profiles/email_service.py, Call from a view or service. Explain their role in the workflow.

### Q3. What is one common security or reliability mistake?
**Answer:** Local console backend prints the message. Explain the consequence and the safe approach.

### Q4. How do you verify the implementation?
**Answer:** Use local test data, mocked external responses and explicit success/failure cases. Inspect the saved file, email output or API response.

### Q5. What should never be committed?
**Answer:** API keys, SMTP passwords, private file data, access tokens and customer personal information.

## Scenario questions

### Q6. An integration works on your machine but fails in production. What do you inspect?
**Suggested answer:** Environment configuration, dependency versions, network access, permissions, storage settings, timeouts and provider responses.

### Q7. Why should an external service call have a timeout?
**Suggested answer:** To prevent the backend request from waiting indefinitely and consuming server resources.

## Project viva — Email Notification Service

1. What does the integration do?
2. Which settings and dependencies are required?
3. How are secrets configured?
4. How are invalid inputs handled?
5. What happens when the external service fails?
6. How did you test success and failure?
7. What would you improve for production?

## Rapid revision

- **1.** Explain email use cases in backend systems.
- **2.** Configure the console email backend for local development.
- **3.** Create a service function that calls send_mail().
- **4.** Use DEFAULT_FROM_EMAIL from settings.
- **5.** Call the service from an appropriate business workflow.
- **6.** Inspect the email output in the terminal.
- **7.** Configure a real provider only through protected environment settings.
- **8.** Handle delivery failures and avoid logging sensitive content.

## Readiness checklist
- [ ] Explain the integration.
- [ ] Explain the security controls.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure case.
- [ ] Present Email Notification Service with safe evidence.
