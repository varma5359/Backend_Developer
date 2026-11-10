# Day 88: Cloud Deployment, Database Configuration, Logs and Deployment Verification

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–87 — Django, production settings, Linux, Gunicorn, Nginx and Docker  
**Tools:** Cloud account or lab VM, Linux terminal, Django, PostgreSQL and deployment logs  
**Approved mini-project:** Deployed Django REST API

> **Trainer guidance:** Use a controlled lab account and a small test application. Cloud deployment can create costs. Review the provider's pricing, firewall and cleanup instructions before creating resources.

## 1. Learning objectives

- Explain the main steps in deploying a Django API to a cloud environment.
- Configure production environment variables.
- Connect Django to a PostgreSQL database.
- Apply migrations safely.
- Configure logs and a health check.
- Verify public access over HTTPS.
- Explain backup, rollback and cost considerations.
- Complete the Deployed Django REST API project.

## 2. Concept introduction

A cloud deployment makes the backend accessible from an external network. A typical architecture includes:
- A cloud virtual machine or container service to run the Django application.
- A production application server such as Gunicorn.
- A reverse proxy or load balancer.
- A PostgreSQL database, often managed separately.
- Environment variables and secret storage.
- Logs, monitoring and backups.
- HTTPS and firewall/network rules.

The application should not depend on files or secrets that exist only on a developer's laptop.

## 3. Example deployment architecture

```text
Browser / Postman
      ↓ HTTPS
Cloud DNS / Load Balancer / Nginx
      ↓
Gunicorn / Django API
      ↓
Managed PostgreSQL database
      ↓
Logs, backups and monitoring
```

A managed database can reduce the operational work of database maintenance, but the team remains responsible for access rules, credentials, backups and application-level data integrity.

## 4. Deployment preparation checklist

Before deployment:
1. Confirm the project starts locally.
2. Run the full test suite.
3. Confirm DEBUG=False in production settings.
4. Configure ALLOWED_HOSTS.
5. Move SECRET_KEY and database credentials to protected configuration.
6. Confirm requirements.txt contains required packages.
7. Confirm migrations are committed.
8. Confirm static and media file strategy.
9. Confirm the database is backed up before schema changes.
10. Prepare a rollback plan.

## 5. Production database configuration

Example environment variable names:

```text
DJANGO_SECRET_KEY=provided-by-secret-manager
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=api.example.com
DB_NAME=backend_db
DB_USER=backend_user
DB_PASSWORD=provided-by-secret-manager
DB_HOST=database.internal.example
DB_PORT=5432
```

These are placeholder names and values. Do not commit real values.

Django settings can read the values using os.environ or a configuration library. Use the database URL or individual fields consistently. The database host should be reachable only from approved application networks.

## 6. Apply database migrations carefully

On the deployment environment:
1. Confirm the database backup or snapshot exists.
2. Confirm the release's migration files are included.
3. Run python manage.py check --deploy.
4. Run python manage.py showmigrations.
5. Apply python manage.py migrate during the planned release.
6. Verify the expected tables and application health.
7. Do not delete migration history to fix a deployment issue.

A migration can change production schema. Review destructive or long-running migrations before applying them.

## 7. Static files and application startup

Depending on the deployment architecture:
- Run python manage.py collectstatic --noinput.
- Start Gunicorn using the project's WSGI application.
- Ensure the reverse proxy forwards requests to the application server.
- Ensure HTTPS is configured.
- Confirm health-check routes do not expose sensitive data.

## 8. Logs and monitoring

Useful Linux commands:

```bash
# Inspect a systemd service
sudo systemctl status gunicorn

# Inspect recent service logs
sudo journalctl -u gunicorn -n 100 --no-pager

# Follow logs
sudo journalctl -u gunicorn -f

# Inspect Nginx logs
sudo tail -n 100 /var/log/nginx/error.log
sudo tail -n 100 /var/log/nginx/access.log
```

Logs should help identify failures without exposing passwords, tokens, session cookies or unnecessary personal information.

## 9. Deployment verification checklist

| Check | Expected result |
|---|---|
| DNS / public hostname | Resolves to the intended deployment |
| HTTPS | Certificate is valid |
| Health endpoint | Returns expected healthy status |
| Authentication | Protected endpoint denies anonymous access |
| API behavior | Expected request and response work |
| Database | Application can read/write intended test data |
| Logs | Errors and request events are observable |
| Static files | Served from configured storage/proxy |
| Backup | Database backup process is configured |
| Firewall | Only required ports are reachable |

## 10. Common deployment errors

| Symptom | What to inspect |
|---|---|
| 502 Bad Gateway | Gunicorn process, socket/port and reverse proxy |
| 400 Bad Request | ALLOWED_HOSTS and forwarded host configuration |
| Database connection error | Host, port, credentials, network access and TLS |
| Static files missing | collectstatic, STATIC_ROOT and proxy/static storage |
| Migration failure | Migration order, schema state and database permissions |
| HTTPS redirect loop | Proxy SSL headers and Django security settings |
| Service repeatedly restarts | systemd logs and application traceback |
| Cloud access denied | Security group, firewall, IAM and network rules |

## 11. Approved mini-project — Deployed Django REST API

**Objective:** Deploy a small Django REST API to a controlled cloud environment and verify its behavior.

### Required tasks

1. Choose a cloud VM or container hosting environment.
2. Provision a PostgreSQL database or managed database service.
3. Configure network access so only the application can connect to the database.
4. Configure environment variables or secret storage.
5. Deploy the Django application using the production stack.
6. Run system checks and migrations.
7. Configure HTTPS and a public API hostname or approved test URL.
8. Verify a health endpoint.
9. Verify one authenticated API endpoint.
10. Inspect application and reverse-proxy logs.
11. Document the backup and rollback approach.
12. Stop or remove lab resources after the exercise if they are not needed.

### Suggested deployment evidence

- Architecture diagram.
- Deployment configuration with secrets removed.
- Successful health-check response.
- Successful authenticated API request.
- Database connection verification.
- Sanitized service logs.
- README with deployment and verification steps.

### Security and cost checklist

- [ ] Use least-privilege cloud permissions.
- [ ] Restrict inbound ports.
- [ ] Do not expose the database publicly.
- [ ] Use HTTPS.
- [ ] Keep secrets out of Git.
- [ ] Confirm backup strategy.
- [ ] Review resource pricing.
- [ ] Stop or delete unused lab resources.

## 12. AI-assisted deployment guide

**Planning prompt:** "Help me plan the deployment of my Django REST API. List cloud resources, network access, database configuration, environment variables, migration steps, logs and verification checks. Do not ask me to share secrets."

**Guided prompt:** "Guide me through one cloud deployment step at a time. Explain the cost and security impact before I create a resource."

**Debugging prompt:** "Here are sanitized service logs, HTTP status and configuration names. Trace the failure without asking for passwords or tokens."

**Review prompt:** "Review my deployment checklist for security, database access, backups, HTTPS, logs, cost and rollback."

## 13. Five daily MCQs

**Q1. What is the main purpose of deployment verification?**  
A. Confirm the live application behaves as expected.  
B. Rename the repository.  
C. Disable HTTPS.  
D. Delete the database.  
**Answer: A.** Verification checks the real deployment.

**Q2. Where should production credentials be stored?**  
A. Git repository.  
B. Protected environment configuration or secret manager.  
C. Public README.  
D. Browser URL.  
**Answer: B.** Credentials must remain protected.

**Q3. Why is a database backup important before a migration?**  
A. To change the browser.  
B. To remove Django.  
C. To provide a recovery point if a migration or release causes a problem.  
D. To avoid tests.  
**Answer: C.** Backups support recovery.

**Q4. What should be exposed publicly?**  
A. Database port to everyone.  
B. Admin credentials.  
C. Private storage.  
D. Only required application entry points.  
**Answer: D.** Restrict network exposure.

**Q5. What is a useful deployment health check?**  
A. A safe endpoint that confirms the service is responding.  
B. A public secret key.  
C. A database password.  
D. A server restart command.  
**Answer: A.** A health endpoint helps verify service availability.

## 14. Interview preparation

**Q1. Explain cloud deployment of a Django API.**  
**Answer:** A Django API is deployed to a cloud environment with production configuration, an application server, database connectivity, HTTPS, logging, monitoring and backups.

**Q2. What do you check when a deployment returns 502?**  
**Answer:** Check Gunicorn status, application logs, reverse-proxy target and port/socket configuration.

**Q3. Why should a database not be publicly accessible?**  
**Answer:** Restricting access reduces the attack surface. Only approved application networks and administrators should reach the database.

**Follow-up:** What evidence would you show in a deployment review?  
**Answer:** Health-check response, API test, sanitized logs, database verification, architecture and rollback/backup notes.

## 15. Completion checklist

- [ ] Explain the architecture.
- [ ] Configure production settings.
- [ ] Deploy the API.
- [ ] Apply migrations safely.
- [ ] Verify HTTPS and API behavior.
- [ ] Inspect logs.
- [ ] Complete Deployed Django REST API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence and cleanup unused resources.

**Phase 7 complete. Next: Phase 8 — End-to-End Backend Capstone (Day 89).**
