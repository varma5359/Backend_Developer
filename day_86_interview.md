# Day 86: Interview Questions — Gunicorn, Nginx and Production Django Configuration

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 86 class notes](day_86_notes.md)  
**Approved mini-project:** Production Server Configuration

## Core technical questions

### Q1. Explain gunicorn, nginx and production django configuration.
**Answer:** Django's development server is not intended for production. Gunicorn is a WSGI application server that runs the Django application. Nginx can act as a reverse proxy, terminate TLS and serve static assets. Production settings, process management, firewall rules and logs must be configured deliberately.

### Q2. Which commands or configuration files are involved?
**Answer:** Run Gunicorn, Nginx site configuration example, Static files command. Explain the role of each.

### Q3. What is one common failure?
**Answer:** Gunicorn starts the Django WSGI application. Explain how to inspect the relevant logs or configuration.

### Q4. How do you verify the deployment?
**Answer:** Inspect process/container status, application response, logs, database connection and persistent data.

### Q5. What is one security concern?
**Answer:** Keep secrets protected, restrict network exposure, use HTTPS and run services with least privilege.

## Scenario questions

### Q6. The application works locally but fails on the server. What do you inspect?
**Suggested answer:** Environment variables, dependencies, working directory, allowed hosts, database connectivity, service logs and proxy configuration.

### Q7. What evidence would you provide?
**Suggested answer:** Startup commands, service status, logs, successful HTTP response and a README with reproducible setup steps.

## Project viva — Production Server Configuration

1. What does the project deploy or prepare?
2. Which services or processes are involved?
3. Which ports are exposed?
4. How are secrets configured?
5. How is persistent data protected?
6. How did you verify the service?
7. What would you improve?

## Rapid revision

- **1.** Explain why runserver is not used in production.
- **2.** Install Gunicorn in the server's virtual environment.
- **3.** Run the WSGI application through Gunicorn bound to localhost.
- **4.** Configure Nginx as a reverse proxy to Gunicorn.
- **5.** Configure static file collection and serving.
- **6.** Configure a process manager such as systemd.
- **7.** Set production environment variables and DEBUG=False.
- **8.** Configure HTTPS and firewall rules.
- **9.** Inspect Gunicorn and Nginx logs and verify the public URL.

## Readiness checklist
- [ ] Explain the deployment flow.
- [ ] Explain the configuration files.
- [ ] Demonstrate startup and verification.
- [ ] Explain one failure case.
- [ ] Present Production Server Configuration.
