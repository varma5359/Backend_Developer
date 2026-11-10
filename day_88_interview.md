# Day 88: Interview Questions — Cloud Deployment, Database Configuration, Logs and Deployment Verification

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 88 class notes](day_88_notes.md)  
**Approved mini-project:** Deployed Django REST API

## Core technical questions

### Q1. Explain how a Django API is deployed to a cloud environment.
**Answer:** Configure production settings and secrets, provision the application runtime and database, deploy the code, apply migrations, configure HTTPS and reverse proxy, then verify logs and API behavior.

### Q2. Why use a managed PostgreSQL database?
**Answer:** It can reduce operational tasks such as database maintenance and backups, but the application team must still configure network access, credentials, permissions and data integrity.

### Q3. What is the purpose of ALLOWED_HOSTS?
**Answer:** It controls which host/domain values Django accepts for incoming requests.

### Q4. What should be checked after applying migrations?
**Answer:** Migration status, expected schema, application health and a safe read/write operation.

### Q5. What should deployment logs contain?
**Answer:** Useful operational metadata and error details without passwords, tokens, session cookies or unnecessary personal data.

## Scenario questions

### Q6. The deployed API returns 502. What do you inspect?
**Suggested answer:** Gunicorn service state, application logs, reverse-proxy configuration, port/socket and network reachability.

### Q7. The app cannot connect to PostgreSQL. What do you inspect?
**Suggested answer:** Host, port, credentials, network rules, database status, TLS settings and database user permissions.

## Project viva — Deployed Django REST API

1. Which cloud resources did you use?
2. Where does the database run?
3. How are secrets configured?
4. How is HTTPS enabled?
5. How are migrations applied?
6. How are logs inspected?
7. How is the deployment verified?
8. How can the release be rolled back?
9. How did you control lab cost?

## Rapid revision

- **Production settings:** DEBUG, ALLOWED_HOSTS, secret key and database configuration.
- **Gunicorn:** WSGI application server.
- **Nginx:** reverse proxy and static-file server.
- **PostgreSQL:** relational database.
- **HTTPS:** encrypted client-server communication.
- **Logs:** operational evidence for diagnosis.
- **Backup:** recovery point for data.
- **Health check:** safe service availability verification.

## Readiness checklist

- [ ] Explain the deployment architecture.
- [ ] Explain database network access.
- [ ] Demonstrate a live health check.
- [ ] Show sanitized logs.
- [ ] Explain backup and rollback.
- [ ] Present Deployed Django REST API.
