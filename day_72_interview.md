# Day 72: Interview Questions — Third-Party API Integration and Consuming External APIs

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 72 class notes](day_72_notes.md)  
**Approved mini-project:** Weather Information Backend

## Core technical questions

### Q1. Explain third-party api integration and consuming external apis.
**Answer:** A backend may consume an external API to retrieve data from another service. The integration should define timeouts, check HTTP status, validate the response shape, handle network failures and protect API keys. Never trust a third-party response or let an external service hang a web request indefinitely.

### Q2. Which Django files or libraries are involved?
**Answer:** services/weather_client.py, Example view. Explain their role in the workflow.

### Q3. What is one common security or reliability mistake?
**Answer:** API key is read from environment configuration. Explain the consequence and the safe approach.

### Q4. How do you verify the implementation?
**Answer:** Use local test data, mocked external responses and explicit success/failure cases. Inspect the saved file, email output or API response.

### Q5. What should never be committed?
**Answer:** API keys, SMTP passwords, private file data, access tokens and customer personal information.

## Scenario questions

### Q6. An integration works on your machine but fails in production. What do you inspect?
**Suggested answer:** Environment configuration, dependency versions, network access, permissions, storage settings, timeouts and provider responses.

### Q7. Why should an external service call have a timeout?
**Suggested answer:** To prevent the backend request from waiting indefinitely and consuming server resources.

## Project viva — Weather Information Backend

1. What does the integration do?
2. Which settings and dependencies are required?
3. How are secrets configured?
4. How are invalid inputs handled?
5. What happens when the external service fails?
6. How did you test success and failure?
7. What would you improve for production?

## Rapid revision

- **1.** Choose an external API and read its documentation.
- **2.** Install requests in the active environment.
- **3.** Store the API key in an environment variable.
- **4.** Set a request timeout.
- **5.** Check HTTP status using raise_for_status().
- **6.** Parse JSON and validate required fields.
- **7.** Handle network, status and parsing failures.
- **8.** Return a controlled response to the frontend.
- **9.** Test with a mocked response rather than relying only on a live service.

## Readiness checklist
- [ ] Explain the integration.
- [ ] Explain the security controls.
- [ ] Demonstrate a successful case.
- [ ] Demonstrate a failure case.
- [ ] Present Weather Information Backend with safe evidence.
