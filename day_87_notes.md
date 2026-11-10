# Day 87: Docker Fundamentals and Dockerizing Django Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–86 — Django, Linux basics, production settings and application testing  
**Tools:** Linux terminal or VM, Python, Django, Gunicorn/Nginx or Docker as appropriate  
**Approved mini-project:** Dockerized Django Backend

> **Trainer guidance:** Deployment commands affect real infrastructure. Practice in a disposable VM or local container environment first. Never run commands copied from the internet without understanding their target and effect.

## 1. Learning objectives

- Explain docker fundamentals and dockerizing django applications.
- Identify the server or container components.
- Execute the example in a safe environment.
- Verify the application and inspect logs.
- Explain configuration and security requirements.
- Complete Dockerized Django Backend.

## 2. Concept introduction

Docker packages an application and its dependencies into an image that can run as a container. A Dockerfile describes how to build the image. Docker Compose can run multiple services such as Django and PostgreSQL. Containers should use environment configuration, persistent volumes where required and non-root users where practical.

## 3. File-by-file or command implementation

### Dockerfile

```dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### .dockerignore

```gitignore
.git
.venv
__pycache__
*.pyc
.env
media
staticfiles
.pytest_cache
```

### compose.yaml

```yaml
services:
  web:
    build: .
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: backend_db
      POSTGRES_USER: backend_user
      POSTGRES_PASSWORD: change-this-local-password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## 4. Explain the important commands and configuration

### Dockerfile

1. `FROM python:3.12-slim` — Selects the base container image.
2. ` ` — Part of the configuration; explain how it contributes to deployment.
3. `ENV PYTHONDONTWRITEBYTECODE=1` — Part of the configuration; explain how it contributes to deployment.
4. `ENV PYTHONUNBUFFERED=1` — Part of the configuration; explain how it contributes to deployment.
5. ` ` — Part of the configuration; explain how it contributes to deployment.
6. `WORKDIR /app` — Sets the working directory inside the image.
7. ` ` — Part of the configuration; explain how it contributes to deployment.
8. `COPY requirements.txt .` — Copies files into the image build context.
9. `RUN pip install --no-cache-dir -r requirements.txt` — Executes a command during image build.
10. ` ` — Part of the configuration; explain how it contributes to deployment.
11. `COPY . .` — Copies files into the image build context.
12. ` ` — Part of the configuration; explain how it contributes to deployment.
13. `EXPOSE 8000` — Part of the configuration; explain how it contributes to deployment.
14. ` ` — Part of the configuration; explain how it contributes to deployment.
15. `CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]` — Defines the default container startup command.

### .dockerignore

1. `.git` — Part of the configuration; explain how it contributes to deployment.
2. `.venv` — Part of the configuration; explain how it contributes to deployment.
3. `__pycache__` — Part of the configuration; explain how it contributes to deployment.
4. `*.pyc` — Part of the configuration; explain how it contributes to deployment.
5. `.env` — Part of the configuration; explain how it contributes to deployment.
6. `media` — Part of the configuration; explain how it contributes to deployment.
7. `staticfiles` — Part of the configuration; explain how it contributes to deployment.
8. `.pytest_cache` — Part of the configuration; explain how it contributes to deployment.

### compose.yaml

1. `services:` — Starts the Docker Compose service definitions.
2. `  web:` — Part of the configuration; explain how it contributes to deployment.
3. `    build: .` — Part of the configuration; explain how it contributes to deployment.
4. `    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000` — Starts the Django WSGI application using Gunicorn.
5. `    ports:` — Part of the configuration; explain how it contributes to deployment.
6. `      - "8000:8000"` — Part of the configuration; explain how it contributes to deployment.
7. `    env_file:` — Part of the configuration; explain how it contributes to deployment.
8. `      - .env` — Part of the configuration; explain how it contributes to deployment.
9. `    depends_on:` — Part of the configuration; explain how it contributes to deployment.
10. `      - db` — Part of the configuration; explain how it contributes to deployment.
11. ` ` — Part of the configuration; explain how it contributes to deployment.
12. `  db:` — Part of the configuration; explain how it contributes to deployment.
13. `    image: postgres:16` — Part of the configuration; explain how it contributes to deployment.
14. `    environment:` — Part of the configuration; explain how it contributes to deployment.
15. `      POSTGRES_DB: backend_db` — Part of the configuration; explain how it contributes to deployment.
16. `      POSTGRES_USER: backend_user` — Part of the configuration; explain how it contributes to deployment.
17. `      POSTGRES_PASSWORD: change-this-local-password` — Part of the configuration; explain how it contributes to deployment.
18. `    volumes:` — Part of the configuration; explain how it contributes to deployment.
19. `      - postgres_data:/var/lib/postgresql/data` — Part of the configuration; explain how it contributes to deployment.
20. ` ` — Part of the configuration; explain how it contributes to deployment.
21. `volumes:` — Part of the configuration; explain how it contributes to deployment.
22. `  postgres_data:` — Part of the configuration; explain how it contributes to deployment.

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

Docker packages an application and its dependencies into an image that can run as a container. A Dockerfile describes how to build the image. Docker Compose can run multiple services such as Django and PostgreSQL. Containers should use environment configuration, persistent volumes where required and non-root users where practical.

## 9. Approved mini-project — Dockerized Django Backend

**Objective:** Dockerized Django Backend.

### Required tasks

1. Explain image, container, Dockerfile, port mapping and volume.
2. Create a Dockerfile for the Django application.
3. Create a .dockerignore file.
4. Create a Compose file with web and database services.
5. Keep local credentials in an ignored .env file.
6. Build the image using docker compose build.
7. Start services using docker compose up.
8. Run migrations inside the web container.
9. Inspect logs and test the application URL.
10. Stop services and explain what data is preserved in the volume.

### Suggested structure

```text
projects/day_87/
├── README.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
└── deployment/
    └── nginx.conf
```

### Validation checklist

- [ ] Docker image builds successfully.
- [ ] Web and database containers start.
- [ ] Web container can reach the database service by service name.
- [ ] Migrations can run in the container.
- [ ] Application responds on the mapped port.
- [ ] Database data persists in the named volume.
- [ ] Secrets are not included in the image or repository.

### Submission evidence

- Configuration files.
- Build and startup command output.
- Container/service status.
- Browser or API verification.
- Logs for one successful and one failed case.
- README with setup and teardown commands.
- No secrets in Git or the container image.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Dockerized Django Backend. Identify services, ports, configuration files, startup commands, security controls and verification checks."

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

**Q1. Explain docker fundamentals and dockerizing django applications.**  
**Answer:** Docker packages an application and its dependencies into an image that can run as a container. A Dockerfile describes how to build the image. Docker Compose can run multiple services such as Django and PostgreSQL. Containers should use environment configuration, persistent volumes where required and non-root users where practical.

**Q2. What is one common deployment failure?**  
**Answer:** Docker image builds successfully. Explain how you would isolate the issue.

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
- [ ] Complete Dockerized Django Backend.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 88.
