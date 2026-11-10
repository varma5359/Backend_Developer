# Day 1: Interview Questions — Introduction to Backend Development, Python and Its Real-World Applications

**Phase:** 1 — Python Programming Foundations  
**Target audience:** Freshers and candidates with 0–1 year of experience

## 1. Core questions

### Q1. What is backend development?
**Answer:**
- Backend development focuses on server-side application behavior.
- It receives client requests and applies business logic.
- It interacts with databases and external services.
- It validates input and controls access.
- It returns responses to frontend or other clients.

**Practical example:** In a student registration application, backend code validates student details and stores an accepted registration.

**Follow-up:** What happens between receiving a request and returning a response?

### Q2. What is the difference between frontend and backend?
**Answer:**
- Frontend is the user-facing interface.
- Backend handles server-side processing and data access.
- Frontend collects and displays information.
- Backend enforces business rules and permissions.
- They communicate through HTTP requests and responses, often using APIs.

**Practical example:** A login screen is frontend; checking credentials and creating a session is backend work.

**Follow-up:** Can a mobile application use the same backend API as a website?

### Q3. What is an API?
**Answer:**
- API means Application Programming Interface.
- It defines how one software component can interact with another.
- A web API commonly exposes endpoints that accept HTTP requests.
- It defines expected inputs and outputs.

**Practical example:** A mobile app sends a request to retrieve employee details from a backend endpoint.

**Follow-up:** What is the difference between an endpoint and an API?

### Q4. What is the role of a database in backend development?
**Answer:**
- It stores persistent application information.
- It supports inserting, retrieving, updating and deleting records.
- It helps maintain relationships and data integrity.
- The backend controls access to stored data.

**Practical example:** An employee management system stores employee, department and project details in relational tables.

**Follow-up:** Why should the browser not receive production database credentials?

### Q5. Why is Python used for backend development?
**Answer:**
- Python has readable syntax.
- It has a large ecosystem of libraries.
- Frameworks such as Django support common web application features.
- It can be used for APIs, automation and integrations.
- The project still needs good design, testing and security.

**Follow-up:** What is Django, and how does it relate to Python?

## 2. Scenario-based questions

### Q6. A user clicks "Submit Leave Request". Explain the backend flow.
**Answer:**
1. The frontend sends an HTTP request.
2. The backend identifies the route and handler.
3. It verifies authentication and permission.
4. It validates dates and request details.
5. It applies business rules.
6. It saves the request if valid.
7. It returns a success or error response.

**Follow-up:** At which step should the backend check whether the user is signed in?

### Q7. A website displays employee data. Which component should retrieve it from the database?
**Answer:**
- The backend should query the database.
- It should verify that the requester is allowed to see the records.
- It should return only the required fields.
- The frontend should display the response.

**Follow-up:** Why is checking permissions only in the frontend insufficient?

### Q8. A developer places database credentials in public JavaScript. What is the problem?
**Answer:**
- Browser code is visible to users.
- Credentials can be copied and misused.
- Attackers may access or modify data.
- Credentials should be protected in a controlled backend environment and rotated if exposed.

**Follow-up:** What other information should never be committed to a public repository?

## 3. Project and communication questions

### Q9. Explain your Backend Development Concept Explorer.
**Answer:**
- I selected a business application scenario.
- I identified frontend actions and backend responsibilities.
- I listed the data that must be stored.
- I drafted API operations.
- I drew the request-response flow and identified an access-control rule.

**Follow-up:** How would you extend the design into a working Django project?

### Q10. What does a backend developer do in a typical project?
**Answer:**
- Understand requirements.
- Design application logic and data structures.
- Develop endpoints and database operations.
- Validate inputs and implement permissions.
- Write tests, fix defects and support deployment.
- Maintain documentation and troubleshoot production issues.

**Follow-up:** Which of these responsibilities would you perform before writing code?

## 4. Rapid revision
- Frontend: user interface.
- Backend: server-side logic.
- Database: persistent data storage.
- API: software communication contract.
- HTTP: request-response protocol used by web applications.
- Django: Python web framework.
- Authentication: confirming identity.
- Authorization: deciding what an identity may do.
