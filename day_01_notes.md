# Day 1: Introduction to Backend Development, Python and Its Real-World Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** None  
**Required tools:** Computer, browser and a text editor  
**Approved mini-project:** Backend Development Concept Explorer

## 1. Learning objectives

By the end of this lesson, you should be able to:

- Explain frontend, backend, database and API in simple terms.
- Describe the responsibilities of a Python backend developer.
- Trace a basic request from a browser to a backend and back.
- Explain where Python, Django and PostgreSQL fit in a backend application.
- Identify basic security and reliability responsibilities of backend code.

## 2. What is a web application?

A web application is software that users access through a browser or another client. Examples include an online shopping website, banking portal, learning platform and employee management system.

A typical application contains several cooperating parts:

| Part | Responsibility | Example |
|---|---|---|
| Frontend | Displays screens and collects user actions | Login form |
| Backend | Applies rules and processes requests | Verify login details |
| Database | Stores information for later use | User account record |
| API | Defines how software components communicate | Employee data endpoint |

These are logical responsibilities. In a small application, some components may run on the same server; in a large system, they may run on separate services.

## 3. Frontend versus backend

### Frontend

The frontend is the part with which the user directly interacts.

Typical responsibilities:

- Display pages, forms, buttons and messages.
- Collect values entered by the user.
- Send requests to the backend.
- Display the response returned by the backend.

### Backend

The backend runs on the server and performs work that should not be trusted to the user's browser.

Typical responsibilities:

- Receive and validate requests.
- Apply business rules.
- Authenticate users and check permissions.
- Read and update database records.
- Communicate with external services.
- Return an appropriate response.
- Record useful operational information and handle failures.

**Example — employee leave request**

1. The employee selects dates in a frontend form.
2. The frontend sends the leave request to the backend.
3. The backend checks whether the employee is signed in.
4. It validates the dates and applies leave rules.
5. It saves an accepted request in the database.
6. It returns success or a validation message.
7. The frontend displays the result.

The backend must validate the request even if the frontend already checks the dates. A user can send a request without using the normal screen.

## 4. What is a server?

A server is a computer or software process that provides a service to clients. In web development, a web server or application server receives requests and helps deliver responses.

- **Client:** The browser, mobile app or another program making a request.
- **Server:** The system receiving and processing that request.
- **Request:** A message asking the server to perform an action or provide information.
- **Response:** The server's reply.

A server is not necessarily a physical machine in the office. It may run on a cloud virtual machine or a managed hosting platform.

## 5. What is an API?

API stands for Application Programming Interface. It is a defined contract that allows one software component to use another component's functionality.

A web API commonly uses HTTP. For example:

- `GET /employees/` — request a list of employees.
- `GET /employees/15/` — request one employee.
- `POST /employees/` — submit data to create an employee.

These are illustrative endpoint examples. You will learn HTTP methods, request bodies and status codes in Phase 2.

An endpoint is one address or route exposed by an API. An API may contain many endpoints.

## 6. Understand the request-response flow

```text
User action
    ↓
Browser / Mobile App
    ↓ HTTP request
Backend application
    ↓ business rules and database query
Database
    ↓ query result
Backend application
    ↓ HTTP response
Browser / Mobile App
    ↓
Result displayed to user
```

The backend is the controlled layer between external clients and protected data. Production database credentials should not be placed in browser code.

## 7. Where Python and Django fit

**Python** is the programming language used to write application logic.

**Django** is a Python web framework. It provides building blocks for URL routing, request handling, views, models, forms, authentication and an administrative interface.

**Django REST Framework (DRF)** is an extension used to build REST APIs with Django.

**PostgreSQL** is the primary relational database in this pathway. It stores structured application data.

**Git and GitHub** help developers track code changes and collaborate.

**Postman** helps send API requests and inspect responses. Automated tests check expected behavior repeatedly.

A framework does not replace the need to understand Python, HTTP, SQL, security or application design. It provides an organized way to implement common web application tasks.

## 8. Example: student registration system

Imagine an institute wants a system to register students.

| User action | Backend responsibility | Data involved |
|---|---|---|
| Submit registration | Validate required fields | Name, email, phone |
| View student list | Check permission and retrieve records | Student records |
| Update contact details | Validate and update selected fields | Student ID, phone |
| Delete a record | Check permission and apply deletion policy | Student ID |

A useful design question is: *Who is allowed to perform this action?* For example, a student may view their own profile, while an administrator may manage multiple student records.

## 9. Basic idea of an HTTP request and response

An HTTP request commonly contains a method, path, headers and sometimes a body.

Illustrative request:

```http
GET /employees/ HTTP/1.1
Host: example.com
Accept: application/json
```

Illustrative response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

[{"id": 1, "name": "Asha"}]
```

- `GET` describes the requested operation.
- `/employees/` identifies the resource path.
- `200 OK` indicates that the request succeeded.
- JSON is one common format for exchanging structured data.

Do not memorize these details yet. The purpose today is to recognize that clients and servers exchange structured messages.

## 10. Why backend validation and security matter

Never assume that incoming data is safe just because it came from your own frontend.

A backend developer should:

- Validate required fields and allowed values.
- Check the identity of the user.
- Check whether that user is allowed to perform the action.
- Avoid exposing passwords, API keys or database credentials.
- Return useful errors without exposing internal secrets.
- Avoid trusting IDs or prices supplied by a client without checking them.

For example, an online store must calculate or verify the price on the server. It should not blindly trust a total amount sent by the browser.

## 11. Common misunderstandings

| Misunderstanding | Correct understanding |
|---|---|
| Backend means only the database | Backend includes request handling, business logic, validation, security and data access. |
| An API is the database | An API is a communication contract; it may use a database internally. |
| Hiding a button secures an operation | The backend must enforce permissions on every protected operation. |
| Django is a programming language | Django is a Python web framework. |
| The server is always one physical computer | A server can be a process or cloud-hosted system. |

## 12. Industry scenario

A training institute currently stores student, batch and fee information in spreadsheets. Staff members sometimes create duplicate student records and cannot easily control who may change fee details.

A backend application can centralize the records, validate registration data, apply staff permissions and provide APIs for a future mobile application.

The important design principle is that business rules must be enforced by the backend, not only by the screen.

## 13. Connection to the approved mini-project

**Backend Development Concept Explorer**

Use one scenario such as student registration, employee management or product ordering. Identify:

- The user action and frontend screen.
- The backend operation required.
- The information that must be stored.
- The relevant API action.
- One permission rule.
- The request → backend → database → response flow.

The project is a design and explanation exercise; a running Django server is not expected on Day 1.

## 14. Key takeaways

- Frontend presents the interface; backend processes requests and business rules.
- A database stores persistent data.
- An API defines how software components communicate.
- Python is the language; Django is the framework used later in this pathway.
- The backend must validate input and enforce access permissions.
- A typical web interaction follows a request → processing → response cycle.

**Next lesson:** Day 2 — Python installation, environment setup, interpreter, VS Code and Jupyter basics.
