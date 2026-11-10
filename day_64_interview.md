# Day 64: Interview Questions — Token Authentication and JWT Authentication Concepts

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 64 class notes](day_64_notes.md)  
**Approved mini-project:** JWT Authentication API

## Core technical questions

### Q1. Explain token authentication and jwt authentication concepts.
**Answer:** Token authentication lets a client prove its identity by sending a token with requests. JSON Web Tokens (JWT) are signed tokens containing claims and an expiry. A token is not the user's password. Tokens must be protected, transmitted over HTTPS and given appropriate expiry and rotation/revocation strategies.

### Q2. Which DRF classes or settings are involved?
**Answer:** settings.py — DRF token authentication, Create a token for a local test user, JWT configuration example using Simple JWT. Explain how the configuration affects incoming requests.

### Q3. What is one common security mistake?
**Answer:** Exposing tokens, failing to scope querysets or relying only on frontend access controls. Explain the specific risk.

### Q4. How do you verify the implementation?
**Answer:** Test with local accounts and safe test tokens, then exercise valid, invalid and unauthorized requests. Inspect status codes and result records.

### Q5. What should not be included in a public repository?
**Answer:** Passwords, API tokens, JWTs, session cookies, private keys and real personal data.

## Scenario questions

### Q6. A user can retrieve another user's record. What do you inspect?
**Suggested answer:** Queryset scoping, object-level permission checks and ownership relationships. Test direct API requests as different users.

### Q7. An API returns too many records. What do you add?
**Suggested answer:** Appropriate filters and pagination, with explicit searchable and orderable fields.

## Project viva — JWT Authentication API

1. What is the purpose?
2. Which authentication/permission/filter components are used?
3. How are credentials supplied?
4. How are unauthorized requests handled?
5. How are result sets restricted?
6. How did you test the behavior?
7. What would you improve?

## Rapid revision

- **1.** Explain what a token represents and why it is used.
- **2.** Configure DRF TokenAuthentication for a local demonstration.
- **3.** Add rest_framework.authtoken to INSTALLED_APPS and migrate.
- **4.** Create a token for a local test user.
- **5.** Send Authorization: Token <key> in a Postman request.
- **6.** Understand JWT structure at a conceptual level: header, payload and signature.
- **7.** Install and configure Simple JWT in a separate test configuration if required.
- **8.** Test missing, invalid and valid tokens.
- **9.** Never expose real tokens in screenshots, logs or Git.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the configuration.
- [ ] Demonstrate valid and invalid requests.
- [ ] Explain the security boundary.
- [ ] Present JWT Authentication API with safe evidence.
