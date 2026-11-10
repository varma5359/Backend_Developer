# Day 86: Gunicorn, Nginx and Production Django Configuration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–86 — Django, Linux basics, production settings and application testing  
**Tools:** Linux terminal or VM, Python, Django, Gunicorn/Nginx or Docker as appropriate  
**Approved mini-project:** Production Server Configuration

> **Trainer guidance:** Deployment commands affect real infrastructure. Practice in a disposable VM or local container environment first. Never run commands copied from the internet without understanding their target and effect.

## 1. Learning objectives

- Explain gunicorn, nginx and production django configuration.
- Identify the server or container components.
- Execute the example in a safe environment.
- Verify the application and inspect logs.
- Explain configuration and security requirements.
- Complete Production Server Configuration.

## 2. Concept introduction

Django's development server is not intended for production. Gunicorn is a WSGI application server that runs the Django application. Nginx can act as a reverse proxy, terminate TLS and serve static assets. Production settings, process management, firewall rules and logs must be configured deliberately.

## 3. File-by-file or command implementation

### Run Gunicorn

```bash
# Run from the folder containing manage.py
gunicorn config.wsgi:application --bind 127.0.0.1:8000
```

### Nginx site configuration example

```nginx
server {
    listen 80;
    server_name backend.example.com;

    location /static/ {
        alias /var/www/backend/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Static files command

```bash
python manage.py collectstatic --noinput
```

## 4. Explain the important commands and configuration

### Run Gunicorn

1. `# Run from the folder containing manage.py` — Comment describing the command or setting.
2. `gunicorn config.wsgi:application --bind 127.0.0.1:8000` — Starts the Django WSGI application using Gunicorn.

### Nginx site configuration example

1. `server {` — Part of the configuration; explain how it contributes to deployment.
2. `    listen 80;` — Part of the configuration; explain how it contributes to deployment.
3. `    server_name backend.example.com;` — Part of the configuration; explain how it contributes to deployment.
4. ` ` — Part of the configuration; explain how it contributes to deployment.
5. `    location /static/ {` — Part of the configuration; explain how it contributes to deployment.
6. `        alias /var/www/backend/staticfiles/;` — Part of the configuration; explain how it contributes to deployment.
7. `    }` — Part of the configuration; explain how it contributes to deployment.
8. ` ` — Part of the configuration; explain how it contributes to deployment.
9. `    location / {` — Part of the configuration; explain how it contributes to deployment.
10. `        proxy_pass http://127.0.0.1:8000;` — Part of the configuration; explain how it contributes to deployment.
11. `        proxy_set_header Host $host;` — Part of the configuration; explain how it contributes to deployment.
12. `        proxy_set_header X-Real-IP $remote_addr;` — Part of the configuration; explain how it contributes to deployment.
13. `        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;` — Part of the configuration; explain how it contributes to deployment.
14. `        proxy_set_header X-Forwarded-Proto $scheme;` — Part of the configuration; explain how it contributes to deployment.
15. `    }` — Part of the configuration; explain how it contributes to deployment.
16. `}` — Part of the configuration; explain how it contributes to deployment.

### Static files command

1. `python manage.py collectstatic --noinput` — Part of the configuration; explain how it contributes to deployment.

## 5. Deployment flow

```text
Client / browser
      ↓
Nginx (reverse proxy / TLS / static files)
      ↓
Gunicorn (WSGI application server)
      ↓
Django application
      ↓
Database / cache / external services
```

For Docker Compose, the web and database services run in separate containers and communicate over the Compose network.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Gunicorn cannot import config.wsgi | Working directory, project package and virtual environment |
| Nginx returns 502 | Gunicorn process, bind address and proxy_pass |
| Static files missing | collectstatic, STATIC_ROOT and Nginx alias |
| Container exits immediately | docker compose logs and startup command |
| Database connection refused | Service name, port, credentials and startup readiness |
| Data disappears after container recreation | Named volume configuration |
| Secret appears in image | Docker build context, COPY rules and .dockerignore |

## 7. Security checklist

- Keep DEBUG=False in production.
- Use a protected secret key and database credentials.
- Restrict firewall ports.
- Use HTTPS.
- Run processes with least privilege.
- Keep database storage persistent and backed up.
- Do not bake secrets into Docker images.
- Inspect logs without exposing credentials or personal data.

## 8. Industry scenario

Django's development server is not intended for production. Gunicorn is a WSGI application server that runs the Django application. Nginx can act as a reverse proxy, terminate TLS and serve static assets. Production settings, process management, firewall rules and logs must be configured deliberately.

## 9. Approved mini-project — Production Server Configuration

**Objective:** Production Server Configuration.

### Required tasks

1. Explain why runserver is not used in production.
2. Install Gunicorn in the server's virtual environment.
3. Run the WSGI application through Gunicorn bound to localhost.
4. Configure Nginx as a reverse proxy to Gunicorn.
5. Configure static file collection and serving.
6. Configure a process manager such as systemd.
7. Set production environment variables and DEBUG=False.
8. Configure HTTPS and firewall rules.
9. Inspect Gunicorn and Nginx logs and verify the public URL.

### Suggested structure

```text
projects/day_86/
├── README.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
└── deployment/
    └── nginx.conf
```

### Validation checklist

- [ ] Gunicorn starts the Django WSGI application.
- [ ] Nginx proxies requests to the correct local port.
- [ ] Static files are collected and served.
- [ ] DEBUG is False and ALLOWED_HOSTS is correct.
- [ ] Service starts and restarts through the process manager.
- [ ] HTTPS and firewall configuration are reviewed.

### Submission evidence

- Configuration files.
- Build and startup command output.
- Container/service status.
- Browser or API verification.
- Logs for one successful and one failed case.
- README with setup and teardown commands.
- No secrets in Git or the container image.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Production Server Configuration. Identify services, ports, configuration files, startup commands, security controls and verification checks."

**Guided prompt:** "Guide me through one deployment file at a time. Explain the effect before I execute the command."

**Debugging prompt:** "Here are sanitized service logs and configuration. Trace the request path and identify whether the failure is at proxy, application or database level."

**Review prompt:** "Review the deployment for secrets, ports, persistent data, permissions, logs and restart behavior."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Run and operate a backend application in a controlled server/container environment.  
B. Replace Python.  
C. Disable logging.  
D. Remove the database.  
**Answer: A.** Production operations package and run the application reliably.

**Q2. What should be checked when Nginx returns 502?**  
A. Browser font.  
B. Gunicorn process and proxy target.  
C. Git commit message.  
D. Django template title.  
**Answer: B.** A 502 often indicates an upstream application server problem.

**Q3. Why use a Docker volume for database data?**  
A. To style the page.  
B. To create a URL.  
C. To persist data beyond a container lifecycle.  
D. To hide the database.  
**Answer: C.** Named volumes persist database files.

**Q4. Where should production secrets be stored?**  
A. Dockerfile.  
B. Git commit.  
C. Public README.  
D. Protected environment or secret manager.  
**Answer: D.** Do not bake secrets into source or images.

**Q5. What is the strongest evidence of completion?**  
A. Services start, the app responds and logs/health checks are verified.  
B. A Dockerfile exists.  
C. A server name is written.  
D. A screenshot of the terminal only.  
**Answer: A.** Verify the running deployment.

## 12. Interview preparation

**Q1. Explain gunicorn, nginx and production django configuration.**  
**Answer:** Django's development server is not intended for production. Gunicorn is a WSGI application server that runs the Django application. Nginx can act as a reverse proxy, terminate TLS and serve static assets. Production settings, process management, firewall rules and logs must be configured deliberately.

**Q2. What is one common deployment failure?**  
**Answer:** Gunicorn starts the Django WSGI application. Explain how you would isolate the issue.

**Q3. How do you verify deployment?**  
**Answer:** Check service/container status, logs, browser/API response, database connection and persistence.

**Follow-up:** Why should the development server not be used as a production server?  
**Answer:** It is intended for local development and lacks the operational characteristics of a production application server.

## 13. Completion checklist

- [ ] Explain the deployment components.
- [ ] Implement the configuration.
- [ ] Run the startup commands.
- [ ] Verify the application.
- [ ] Inspect logs.
- [ ] Complete Production Server Configuration.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 87.
