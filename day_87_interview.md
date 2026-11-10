# Day 87: Interview Questions — Docker Fundamentals and Dockerizing Django Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 87 class notes](day_87_notes.md)  
**Approved mini-project:** Dockerized Django Backend

## Core technical questions

### Q1. Explain docker fundamentals and dockerizing django applications.
**Answer:** Docker packages an application and its dependencies into an image that can run as a container. A Dockerfile describes how to build the image. Docker Compose can run multiple services such as Django and PostgreSQL. Containers should use environment configuration, persistent volumes where required and non-root users where practical.

### Q2. Which commands or configuration files are involved?
**Answer:** Dockerfile, .dockerignore, compose.yaml. Explain the role of each.

### Q3. What is one common failure?
**Answer:** Docker image builds successfully. Explain how to inspect the relevant logs or configuration.

### Q4. How do you verify the deployment?
**Answer:** Inspect process/container status, application response, logs, database connection and persistent data.

### Q5. What is one security concern?
**Answer:** Keep secrets protected, restrict network exposure, use HTTPS and run services with least privilege.

## Scenario questions

### Q6. The application works locally but fails on the server. What do you inspect?
**Suggested answer:** Environment variables, dependencies, working directory, allowed hosts, database connectivity, service logs and proxy configuration.

### Q7. What evidence would you provide?
**Suggested answer:** Startup commands, service status, logs, successful HTTP response and a README with reproducible setup steps.

## Project viva — Dockerized Django Backend

1. What does the project deploy or prepare?
2. Which services or processes are involved?
3. Which ports are exposed?
4. How are secrets configured?
5. How is persistent data protected?
6. How did you verify the service?
7. What would you improve?

## Rapid revision

- **1.** Explain image, container, Dockerfile, port mapping and volume.
- **2.** Create a Dockerfile for the Django application.
- **3.** Create a .dockerignore file.
- **4.** Create a Compose file with web and database services.
- **5.** Keep local credentials in an ignored .env file.
- **6.** Build the image using docker compose build.
- **7.** Start services using docker compose up.
- **8.** Run migrations inside the web container.
- **9.** Inspect logs and test the application URL.
- **10.** Stop services and explain what data is preserved in the volume.

## Readiness checklist
- [ ] Explain the deployment flow.
- [ ] Explain the configuration files.
- [ ] Demonstrate startup and verification.
- [ ] Explain one failure case.
- [ ] Present Dockerized Django Backend.
