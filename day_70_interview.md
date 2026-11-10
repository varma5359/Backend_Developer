# Day 70: Interview Questions — File Uploads, Media Files and Image Handling in Django

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 70 class notes](day_70_notes.md)  
**Approved mini-project:** Document Upload Management System

## Core technical questions

### Q1. Explain file uploads, media files and image handling in django.
**Answer:** Uploaded files are untrusted input. Django receives file data through request.FILES when a multipart/form-data request is used. FileField and ImageField store file references, while the file bytes are stored using the configured storage backend. Validate size and content, use safe filenames and restrict access to private documents.

### Q2. Which Django files or libraries are involved?
**Answer:** profiles/models.py, profiles/forms.py, config/settings.py, profiles/views.py, profiles/templates/profiles/upload.html. Explain their role in the workflow.

### Q3. What is one common security or reliability mistake?
**Answer:** The form includes multipart/form-data. Explain the consequence and the safe approach.

### Q4. How do you verify the implementation?
**Answer:** Use local test data, mocked external responses and explicit success/failure cases. Inspect the saved file, email output or API response.

### Q5. What should never be committed?
**Answer:** API keys, SMTP passwords, private file data, access tokens and customer personal information.

## Scenario questions

### Q6. An integration works on your machine but fails in production. What do you inspect?
**Suggested answer:** Environment configuration, dependency versions, network access, permissions, storage settings, timeouts and provider responses.

### Q7. Why should an external service call have a timeout?
**Suggested answer:** To prevent the backend request from waiting indefinitely and consuming server resources.

## Project viva — Document Upload Management System

1. What does the integration do?
2. Which settings and dependencies are required?
3. How are secrets configured?
4. How are invalid inputs handled?
5. What happens when the external service fails?
6. How did you test success and failure?
7. What would you improve for production?

## Rapid revision

- **1.** Create a Document model with FileField.
- **2.** Configure MEDIA_ROOT and MEDIA_URL for local development.
- **3.** Create a ModelForm and validate file size.
- **4.** Pass request.POST and request.FILES to the form.
- **5.** Set enctype=multipart/form-data in the HTML form.
- **6.** Run makemigrations and migrate.
- **7.** Upload a small test document.
- **8.** Verify the saved file path and metadata.
- **9.** Explain why production media storage and access control need additional configuration.

## Readiness checklist
- [ ] Explain the integration.
- [ ] Explain the security controls.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure case.
- [ ] Present Document Upload Management System with safe evidence.
