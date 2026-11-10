# Day 1: Introduction to Backend Development, Python and Its Real-World Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** None  
**Required tools:** Computer, browser, VS Code (optional for this first lesson)  
**Approved mini-project:** Backend Development Concept Explorer

## 1. Learning objectives
By the end of this lesson, you should be able to:
- Explain what frontend and backend development mean.
- Describe how a browser communicates with a backend.
- Identify the main responsibilities of a Python backend developer.
- Explain where Python and Django fit in a web application.
- Sketch a basic request-response flow for a common business application.

## 2. What is backend development?
A web application has parts that users interact with and parts that work behind the scenes.

- **Frontend:** The screens and controls visible to a user.
- **Backend:** The server-side code that processes requests, applies business rules, accesses data and returns responses.
- **Database:** Stores application information.
- **API:** A defined way for one application to request data or actions from another.

Example: When a user signs in, the frontend collects the email and password. The backend validates the request, checks the stored account data and returns an appropriate response.

## 3. Frontend, backend and database

| Component | Main responsibility | Example |
|---|---|---|
| Frontend | Displays information and collects user input | Login form |
| Backend | Processes rules and requests | Validate login |
| Database | Stores persistent information | User account record |
| API | Defines request/response contract | POST /login |

**Flow:**

```text
User
  ↓
Browser / Mobile App (Frontend)
  ↓ HTTP Request
Backend Application (Python / Django)
  ↓ Database Query
Database (PostgreSQL)
  ↑ Result
Backend Application
  ↑ HTTP Response / JSON
Frontend
  ↓
User sees result
```

The frontend should not connect directly to the production database with database credentials. The backend mediates access and enforces permissions.

## 4. What does a backend developer build?
Typical responsibilities include:
1. Receive and process HTTP requests.
2. Implement business logic.
3. Read and write database records.
4. Create APIs for web and mobile clients.
5. Validate input and handle errors.
6. Implement authentication and authorization.
7. Integrate external services.
8. Test, deploy and maintain applications.

## 5. Where Python and Django fit
Python is the programming language used to write backend logic. Django is a Python web framework that provides common building blocks such as URL routing, views, models, forms, authentication and an admin interface.

The pathway uses:
- Python for programming fundamentals.
- Django for web application development.
- Django REST Framework (DRF) for REST APIs.
- PostgreSQL as the primary relational database.
- Git/GitHub for version control.
- Postman and automated tests for API verification.
- Docker and deployment tools for release preparation.

A framework helps organize common web tasks; it does not remove the need to understand HTTP, Python, SQL or application design.

## 6. Real-world example: employee portal
Imagine a company employee portal.

**User action:** An employee opens the leave page and submits a leave request.

**Backend work:**
1. Receive the request.
2. Verify the user is signed in.
3. Validate dates and leave type.
4. Apply company rules.
5. Save the request in the database.
6. Return a success or validation response.

**Expected outcome:** The employee sees confirmation, and an authorized manager can review the request.

## 7. What is an HTTP request and response?
A request is sent by a client to a server. A response is returned by the server.

A request commonly includes:
- Method, such as GET or POST.
- URL or path.
- Headers.
- Optional body.

A response commonly includes:
- Status code.
- Headers.
- Optional response body.

Example concept (not a live service):

```http
GET /employees/ HTTP/1.1
Host: example.com
Accept: application/json
```

Possible response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

[{"id": 1, "name": "Asha"}]
```

You will study HTTP methods and status codes in Phase 2.

## 8. Where is Python used in backend development?
Python can be used for:
- Web applications and REST APIs.
- Business automation.
- Database-backed applications.
- Background processing.
- Integrations with payment, email and external services.

Django is one possible framework. The approved pathway focuses on Django and DRF rather than trying to cover every Python web framework.

## 9. Industry scenario
A training institute manages students, batches and fee payments in spreadsheets. Staff need a central application where authorized users can register students, assign batches and track payments.

A backend application can provide:
- Student and batch records.
- Business validation.
- Role-based access.
- APIs for a future mobile application.
- Consistent database storage.

The backend is responsible for enforcing rules even when requests come from different clients.

## 10. Approved mini-project — Backend Development Concept Explorer

**Objective:** Explain the parts of a backend application by designing a simple request flow for a business use case.

**Skills practiced:** Frontend/backend/database/API concepts, request-response reasoning and technical communication.

### Requirements
1. Select one scenario: student registration, employee portal or product ordering.
2. Identify the frontend screens or user actions.
3. Identify at least five backend responsibilities.
4. Identify the data that must be stored.
5. Draft two example API actions.
6. Draw the client → backend → database → response flow.
7. Explain one access-control rule.

### Example deliverable outline
```text
backend_concept_explorer/
└── backend_concept_notes.md
```

Example API action names (concept only):
- POST /students/
- GET /students/

Do not implement a real server today. Focus on identifying responsibilities and explaining the flow.

### Validation checklist
- Does each user action connect to a backend operation?
- Have you identified what data must be stored?
- Have you separated frontend and backend responsibilities?
- Does the design explain who is allowed to perform each action?

### Submission criteria
Submit a diagram and a one-page explanation of the application flow. Be ready to explain it without reading the document.

## 11. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint to distinguish frontend and backend in my chosen example." |
| 2 — Plan | "Help me organize the Backend Development Concept Explorer into sections. Do not write the finished submission." |
| 3 — Example | "Show a small example of a login request moving from browser to backend to database." |
| 4 — Guided implementation | "Ask me questions to help me draw the request-response flow one step at a time." |
| 5 — Explanation | "Explain the role of an API in simple language using my student registration example." |
| 6 — Debugging | "Review my flow and point out where I have confused frontend, backend or database responsibilities." |
| 7 — Review | "Review my mini-project for completeness, clear responsibilities and access-control reasoning." |

**Planning prompt:** "Help me break my chosen business scenario into user actions, backend responsibilities, stored data and API operations. Do not provide the complete answer."

**Implementation prompt:** "Guide me to create the flow diagram one component at a time. Ask me to confirm each component before continuing."

**Debugging/review prompt:** "Review my diagram and explanation. Identify missing request steps, database responsibilities or security checks without rewriting the whole submission."

## 12. Daily quiz

**Q1. Which part of a web application processes server-side business rules?**  
A. Browser layout  
B. Backend  
C. Monitor  
D. Keyboard  
**Correct answer: B.** The backend processes application logic and requests on the server side.

**Q2. What is the primary role of a database?**  
A. Display web pages  
B. Store and retrieve application data  
C. Style buttons  
D. Send browser keystrokes  
**Correct answer: B.** A database stores persistent information and supports queries.

**Q3. Which component commonly defines how a frontend requests backend functionality?**  
A. API  
B. CSS theme  
C. Monitor driver  
D. Text editor  
**Correct answer: A.** An API defines a contract for communication between software components.

**Q4. In a secure design, where should production database credentials normally be used?**  
A. Public browser JavaScript  
B. A controlled backend environment  
C. A public README  
D. A screenshot  
**Correct answer: B.** The backend should mediate database access and protect credentials.

**Q5. What does Django provide?**  
A. A Python web framework with common application features  
B. A replacement for every database  
C. A browser operating system  
D. A programming language unrelated to Python  
**Correct answer: A.** Django provides web development building blocks for Python applications.

## 13. Interview preparation

### Q1. What is backend development?
**Answer:** Backend development is the server-side part of an application. It handles requests, business logic, database operations, authentication, permissions, integrations and responses. For example, in an employee portal, the backend validates and stores leave requests and controls who can approve them.

**Follow-up:** What is the difference between backend logic and database storage?

### Q2. Explain how a browser communicates with a backend.
**Answer:** The browser sends an HTTP request to a server endpoint. The backend receives it, validates the request, performs required business logic and database operations, then sends an HTTP response. The frontend uses the response to update what the user sees.

**Follow-up:** What information can an HTTP request contain?

## 14. Completion checklist
- [ ] Explain frontend, backend, database and API.
- [ ] Draw a request-response flow.
- [ ] Identify backend responsibilities in a business example.
- [ ] Complete Backend Development Concept Explorer.
- [ ] Answer all five quiz questions.
- [ ] Explain at least two interview questions.

**Next lesson:** Day 2 — Python installation, environment setup, interpreter, VS Code and Jupyter basics.
