# Day 85: Interview Questions — Linux Fundamentals, Terminal Commands and Server Basics

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 7 — Testing, Deployment and Production Readiness  
**Related notes:** [Day 85 class notes](day_85_notes.md)  
**Approved mini-project:** Linux Backend Deployment Preparation

## Core technical questions

### Q1. Explain linux fundamentals, terminal commands and server basics.
**Answer:** A Django application deployed to a Linux server is operated through shell commands, processes, users, file permissions, environment variables and logs. Developers should understand how to navigate the filesystem, inspect processes and disk usage, manage permissions and troubleshoot service output.

### Q2. Which commands or configuration files are involved?
**Answer:** Essential commands, Process and system inspection, Permissions overview. Explain the role of each.

### Q3. What is one common failure?
**Answer:** Learner can navigate directories. Explain how to inspect the relevant logs or configuration.

### Q4. How do you verify the deployment?
**Answer:** Inspect process/container status, application response, logs, database connection and persistent data.

### Q5. What is one security concern?
**Answer:** Keep secrets protected, restrict network exposure, use HTTPS and run services with least privilege.

## Scenario questions

### Q6. The application works locally but fails on the server. What do you inspect?
**Suggested answer:** Environment variables, dependencies, working directory, allowed hosts, database connectivity, service logs and proxy configuration.

### Q7. What evidence would you provide?
**Suggested answer:** Startup commands, service status, logs, successful HTTP response and a README with reproducible setup steps.

## Project viva — Linux Backend Deployment Preparation

1. What does the project deploy or prepare?
2. Which services or processes are involved?
3. Which ports are exposed?
4. How are secrets configured?
5. How is persistent data protected?
6. How did you verify the service?
7. What would you improve?

## Rapid revision

- **1.** Open a Linux terminal or approved virtual machine.
- **2.** Identify the current user using whoami and id.
- **3.** Navigate folders using pwd, ls and cd.
- **4.** Create and inspect directories and files.
- **5.** Inspect logs using grep and tail.
- **6.** Inspect processes using ps and top.
- **7.** Inspect disk and memory using df and free.
- **8.** Understand file permission notation and least privilege.
- **9.** Explain why deployment commands should be run with the minimum required privileges.

## Readiness checklist
- [ ] Explain the deployment flow.
- [ ] Explain the configuration files.
- [ ] Demonstrate startup and verification.
- [ ] Explain one failure case.
- [ ] Present Linux Backend Deployment Preparation.
