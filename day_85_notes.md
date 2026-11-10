# Day 85: Linux Fundamentals, Terminal Commands and Server Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–86 — Django, Linux basics, production settings and application testing  
**Tools:** Linux terminal or VM, Python, Django, Gunicorn/Nginx or Docker as appropriate  
**Approved mini-project:** Linux Backend Deployment Preparation

> **Trainer guidance:** Deployment commands affect real infrastructure. Practice in a disposable VM or local container environment first. Never run commands copied from the internet without understanding their target and effect.

## 1. Learning objectives

- Explain linux fundamentals, terminal commands and server basics.
- Identify the server or container components.
- Execute the example in a safe environment.
- Verify the application and inspect logs.
- Explain configuration and security requirements.
- Complete Linux Backend Deployment Preparation.

## 2. Concept introduction

A Django application deployed to a Linux server is operated through shell commands, processes, users, file permissions, environment variables and logs. Developers should understand how to navigate the filesystem, inspect processes and disk usage, manage permissions and troubleshoot service output.

## 3. File-by-file or command implementation

### Essential commands

```bash
pwd
ls -la
cd /var/www/backend
mkdir -p logs
touch deployment-notes.txt
cp source.txt source-backup.txt
mv old-name.txt new-name.txt
grep -n "ERROR" application.log
tail -f application.log
```

### Process and system inspection

```bash
whoami
id
ps aux
top
df -h
free -h
ss -tulpn
```

### Permissions overview

```bash
ls -l
chmod 640 .env
chmod 750 deploy.sh
```

## 4. Explain the important commands and configuration

### Essential commands

1. `pwd` — Part of the configuration; explain how it contributes to deployment.
2. `ls -la` — Part of the configuration; explain how it contributes to deployment.
3. `cd /var/www/backend` — Part of the configuration; explain how it contributes to deployment.
4. `mkdir -p logs` — Part of the configuration; explain how it contributes to deployment.
5. `touch deployment-notes.txt` — Part of the configuration; explain how it contributes to deployment.
6. `cp source.txt source-backup.txt` — Part of the configuration; explain how it contributes to deployment.
7. `mv old-name.txt new-name.txt` — Part of the configuration; explain how it contributes to deployment.
8. `grep -n "ERROR" application.log` — Part of the configuration; explain how it contributes to deployment.
9. `tail -f application.log` — Part of the configuration; explain how it contributes to deployment.

### Process and system inspection

1. `whoami` — Part of the configuration; explain how it contributes to deployment.
2. `id` — Part of the configuration; explain how it contributes to deployment.
3. `ps aux` — Part of the configuration; explain how it contributes to deployment.
4. `top` — Part of the configuration; explain how it contributes to deployment.
5. `df -h` — Part of the configuration; explain how it contributes to deployment.
6. `free -h` — Part of the configuration; explain how it contributes to deployment.
7. `ss -tulpn` — Part of the configuration; explain how it contributes to deployment.

### Permissions overview

1. `ls -l` — Part of the configuration; explain how it contributes to deployment.
2. `chmod 640 .env` — Part of the configuration; explain how it contributes to deployment.
3. `chmod 750 deploy.sh` — Part of the configuration; explain how it contributes to deployment.

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

A Django application deployed to a Linux server is operated through shell commands, processes, users, file permissions, environment variables and logs. Developers should understand how to navigate the filesystem, inspect processes and disk usage, manage permissions and troubleshoot service output.

## 9. Approved mini-project — Linux Backend Deployment Preparation

**Objective:** Linux Backend Deployment Preparation.

### Required tasks

1. Open a Linux terminal or approved virtual machine.
2. Identify the current user using whoami and id.
3. Navigate folders using pwd, ls and cd.
4. Create and inspect directories and files.
5. Inspect logs using grep and tail.
6. Inspect processes using ps and top.
7. Inspect disk and memory using df and free.
8. Understand file permission notation and least privilege.
9. Explain why deployment commands should be run with the minimum required privileges.

### Suggested structure

```text
projects/day_85/
├── README.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
└── deployment/
    └── nginx.conf
```

### Validation checklist

- [ ] Learner can navigate directories.
- [ ] Learner can inspect files and logs.
- [ ] Learner can identify a running process.
- [ ] Learner can inspect disk and memory usage.
- [ ] Learner understands read/write/execute permissions.
- [ ] No destructive command is run without understanding its target.

### Submission evidence

- Configuration files.
- Build and startup command output.
- Container/service status.
- Browser or API verification.
- Logs for one successful and one failed case.
- README with setup and teardown commands.
- No secrets in Git or the container image.

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Linux Backend Deployment Preparation. Identify services, ports, configuration files, startup commands, security controls and verification checks."

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

**Q1. Explain linux fundamentals, terminal commands and server basics.**  
**Answer:** A Django application deployed to a Linux server is operated through shell commands, processes, users, file permissions, environment variables and logs. Developers should understand how to navigate the filesystem, inspect processes and disk usage, manage permissions and troubleshoot service output.

**Q2. What is one common deployment failure?**  
**Answer:** Learner can navigate directories. Explain how you would isolate the issue.

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
- [ ] Complete Linux Backend Deployment Preparation.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and safe evidence.

**Next lesson:** Day 86.
