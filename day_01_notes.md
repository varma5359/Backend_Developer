# Day 1: Introduction to Backend Development, Python and Its Real-World Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** None  
**Required tools:** Computer, browser and a text editor  
**Approved mini-project:** Backend Development Concept Explorer

> **Before you start:** You do not need to know programming to understand this lesson. Read each small section in order. Imagine the examples happening in a college, shopping website or office. The purpose of today is to understand what backend development means before writing backend code.

## 1. What will you learn today?

By the end of this lesson, you should be able to explain, in your own words:

1. What a web application is.
2. What frontend and backend mean.
3. What a server, request and response are.
4. What a database does.
5. What an API is.
6. How Python and Django are used in backend development.
7. What a backend developer does in a real company.

You are not expected to build a Django application today. First understand the parts of an application and how they communicate.

## 2. Start with a real-life example: ordering food online

Imagine that you open a food delivery website on your mobile phone.

You can see:
- Restaurant names.
- Food images.
- Prices.
- Add-to-cart buttons.
- Your order details.

You select a biryani, add it to your cart and click **Place Order**.

Now think about these questions:

- Who displays the restaurant names?
- Who checks whether the food is available?
- Who calculates the final amount?
- Who saves your order?
- Who tells you that the order was successful?

One part of the application displays the screen. Another part works behind the screen and processes your order. The stored order information must also be kept somewhere.

This gives us the first three important ideas:

| Part | Simple meaning | Food-order example |
|---|---|---|
| Frontend | What the user sees and interacts with | Restaurant page and Place Order button |
| Backend | The part that processes the work | Checks availability and creates the order |
| Database | Where application information is stored | Customer, food and order records |

**Remember:** Frontend, backend and database work together. They are not three different names for the same thing.

## 3. What is a web application?

A web application is a software program that people use through a web browser or another internet-connected application.

Examples:
- Gmail — send and receive email.
- Online shopping — search and purchase products.
- Banking websites — view balances and transfer money.
- College portals — view attendance and results.
- Employee portals — apply for leave and view salary details.

A normal website may mainly display information. A web application usually lets the user perform actions, submit information and receive results. In practice, websites and web applications can overlap.

**Check your understanding:** When a student logs into a college portal and views attendance, is the application only displaying a page? No. It must identify the student, retrieve the correct attendance records and return them.

## 4. What is the frontend?

The **frontend** is the part of an application that the user directly sees and uses.

For example, on a college registration page, the frontend may contain:
- A name input box.
- An email input box.
- A phone number input box.
- A Submit button.
- A message such as "Registration completed".

The frontend collects information and sends it to the backend. It also displays the result received from the backend.

A frontend can be built using HTML, CSS and JavaScript, or using a frontend framework. You do not need to learn those technologies today.

**Important:** A frontend check is helpful for the user, but it is not enough to protect the application. A user can sometimes send a request without using your normal screen. The backend must check the information again.

## 5. What is the backend?

The **backend** is the server-side part of an application. It receives requests, checks information, applies business rules, communicates with databases or other services, and sends responses.

Think about a college student registration.

The student enters:
- Name: Asha
- Email: asha@example.com
- Course: Python

When the student clicks Submit, the backend may:
1. Receive the submitted information.
2. Check whether the name is present.
3. Check whether the email is in an acceptable format.
4. Check whether the course exists.
5. Check whether the student is already registered.
6. Save the registration if the rules are satisfied.
7. Send a success or error response.

These checks and actions are examples of **business logic**. Business logic means the rules that decide how an application should behave.

For example, "a student cannot register for a course that is closed" is a business rule.

### What does a backend developer do?

A Python backend developer commonly:
- Writes Python code to process requests.
- Builds application features.
- Reads and saves database information.
- Creates APIs for websites and mobile applications.
- Checks user identity and permissions.
- Validates incoming data.
- Handles errors.
- Writes tests to check that features work correctly.
- Helps deploy and maintain the application.

A backend developer does not simply write database queries. The role includes application logic, communication, security and reliability.

## 6. What is a server? Understand it with an example

A **server** is a computer or software process that provides a service to another program.

Imagine that your browser asks a college application for your attendance. The browser is acting as a client. The application running on the server receives the request and prepares a response.

| Word | Beginner-friendly meaning |
|---|---|
| Client | The application asking for something, such as a browser |
| Server | The system that receives and processes the request |
| Request | The message asking the server to do something |
| Response | The message sent back by the server |

A server does not have to be a large physical computer in a company office. It can run on a cloud computer.

### Small flow to remember

```text
Student
   |
   | Opens college portal
   v
Browser (Client)
   |
   | Sends request
   v
Server (Backend application)
   |
   | Processes request
   v
Response sent back
   |
   v
Browser displays attendance
```

Read the flow from top to bottom. The browser asks; the server processes; the browser displays the answer.

## 7. What is a database?

A **database** is an organized place to store information so an application can retrieve and manage it later.

Imagine a college stores thousands of student records. Each record may contain:
- Student ID.
- Student name.
- Email.
- Course.
- Joining date.

A database keeps this information organized. The backend application communicates with the database when it needs to save, read, update or delete records.

These four common operations are often called CRUD:

| Letter | Full form | Simple meaning | College example |
|---|---|---|---|
| C | Create | Add new information | Register a student |
| R | Read | View information | Display student details |
| U | Update | Change existing information | Update phone number |
| D | Delete | Remove information | Remove an obsolete record |

You will learn SQL and database operations in Phase 2, and Django models and ORM later. For today, remember that the database stores information and the backend controls how the application uses it.

## 8. What is an API? Start with a simple example

API stands for **Application Programming Interface**.

Do not worry about the long name. Think of an API as a defined way for one software application to ask another application for information or an action.

Example: A mobile application wants to display a student's profile. It sends a request to the backend API. The API provides a defined route through which the application can ask for that profile.

A restaurant analogy can help:
- You are the customer.
- The menu tells you what you can order.
- The waiter carries your order to the kitchen and brings the result.
- The kitchen prepares the food.

The waiter is not exactly a technical API, but the analogy helps you understand the idea of a defined communication point between two sides.

A web API may have routes such as:

| Example route | Intended action |
|---|---|
| `GET /students/` | Ask for a list of students |
| `GET /students/101/` | Ask for student 101 |
| `POST /students/` | Send information to create a student |

You do not need to implement these routes today. The words GET and POST will be taught properly in Phase 2.

**New word — endpoint:** An endpoint is a particular API route that a client can use. An API can provide many endpoints.

## 9. Understand one complete request from beginning to end

Let's follow a student registration request.

**Step 1 — Student enters information**

The student fills in a registration form in the browser.

**Step 2 — Browser sends a request**

When Submit is clicked, the frontend sends the entered information to the backend.

**Step 3 — Backend receives the request**

The backend reads the submitted values. It must not assume that the values are correct.

**Step 4 — Backend checks the rules**

It checks required fields, course availability and whether the student is already registered.

**Step 5 — Backend communicates with the database**

If the information is acceptable, the backend asks the database to save the student record.

**Step 6 — Backend prepares a response**

The backend prepares a message such as "Registration successful" or an explanation of what needs to be corrected.

**Step 7 — Browser displays the result**

The student sees the message on the screen.

Complete flow:

```text
Student fills registration form
              |
              v
       Frontend / Browser
              |
         HTTP Request
              |
              v
       Backend (Python)
              |
       Validate the data
              |
       Apply business rules
              |
              v
           Database
              |
       Save / retrieve data
              |
              v
       Backend prepares response
              |
         HTTP Response
              |
              v
       Browser displays result
```

This request → processing → response pattern is one of the most important ideas in backend development.

## 10. Where does Python fit?

Python is a programming language. A developer writes instructions in Python to tell the computer what work to perform.

For example, a very small Python program can display a message:

```python
print("Welcome to Backend Development")
```

Expected output:

```text
Welcome to Backend Development
```

Let's understand this tiny example:

- `print` is a built-in Python function. A function is a reusable operation.
- Parentheses `()` are used to call the function.
- The text inside quotation marks is a string.
- Python displays that string in the output.

You will learn how to write and run Python programs from Day 2 onward. This example is only to show that Python code contains instructions that the computer executes.

Python can be used to write backend logic. In this pathway, you will learn Python first and then use it with Django.

## 11. Where does Django fit?

Django is a **web framework written in Python**.

A framework provides ready-made structure and tools so developers do not need to build every common web feature from the beginning.

Django helps developers with:
- Receiving and routing web requests.
- Writing views that process requests.
- Connecting application code to database models.
- Handling forms.
- Managing users and authentication.
- Providing an administration interface.

Think of Python as the language and Django as a toolkit built using that language.

| Technology | Its role in this pathway |
|---|---|
| Python | Programming language |
| Django | Main backend web framework |
| Django REST Framework | Toolkit for building REST APIs with Django |
| PostgreSQL | Relational database |
| Git | Tracks changes in code |
| GitHub | Hosts repositories and supports collaboration |
| Postman | Helps send API requests and inspect responses |

Do not try to learn all these tools today. This table is a preview of what you will study in later phases.

## 12. Why are validation and security important?

Imagine that a shopping website displays a product price of ₹1,000. A user changes the amount sent from the browser to ₹10.

Should the backend accept ₹10 simply because the browser sent it? No.

The backend must check the actual product price and calculate the correct amount using trusted application data.

Two important terms:

- **Validation:** Checking whether supplied information follows the application's rules.
- **Authentication:** Checking who the user is.
- **Authorization:** Checking what that user is allowed to do.

Example:
- Authentication: Is this person a registered, signed-in employee?
- Authorization: Is this employee allowed to view the salary report?

These are different checks. A user can be signed in but still not have permission to access every feature.

## 13. Common beginner misunderstandings

| Incorrect understanding | Correct understanding |
|---|---|
| Backend means database only | Backend also handles requests, rules, validation and security. |
| Python and Django are the same | Python is a language; Django is a framework. |
| API means database | An API is a communication interface; it may use a database. |
| Frontend validation is enough | The backend must validate incoming data too. |
| A server is always a physical machine | A server can be software running on a cloud computer. |
| Authentication and authorization are the same | One checks identity; the other checks permissions. |

## 14. Interview connection: explain the concept, not just the definition

In an interview, do not only say "backend is the server side." Explain what it actually does.

A clear beginner-level explanation could be:

"A backend application receives requests from a frontend, validates the submitted data, applies business rules, communicates with a database when needed, and sends a response. In this pathway, I use Python and Django to develop that backend."

When an interviewer asks for an example, use student registration or employee management. Explain the request, validation, database operation and response in order.

The separate daily interview file is where you will practise complete interview questions and follow-up answers. These notes teach the concepts needed to answer them confidently.

## 15. Follow-along activity: identify the parts of an application

Consider a college portal with a login page.

Identify each part:

| Item | Your answer |
|---|---|
| Login form and Login button | Frontend |
| Checking the submitted login details | Backend |
| Stored student account information | Database |
| Defined route used to submit login information | API endpoint |
| Browser asking the application to log in | Client request |
| Message returned after processing | Response |

Try to explain why each answer is correct without looking at the table. If you cannot explain one, return to the related section and read the example again.

## 16. Approved mini-project — Backend Development Concept Explorer

**Project title must remain unchanged:** Backend Development Concept Explorer

**Goal:** Explain the parts of one real application and show how they work together. You are not expected to write a Django server on Day 1.

Choose one scenario:
- Student registration system.
- Employee management system.
- Online product ordering system.

Prepare a short explanation containing:

1. What the user does in the frontend.
2. What request the frontend needs to send.
3. What work the backend must perform.
4. What information the database stores.
5. One example of an API endpoint.
6. One validation rule.
7. One authentication or authorization rule.
8. What response the user sees after the operation.

**Example:** In a student registration system, the frontend collects a student's name and email. The backend checks that required information is present and that the course is available. The database stores the accepted registration. The backend returns a success or error response.

### Completion check

You have completed the activity when you can draw the request → backend → database → response flow and explain every box in your own words.

## 17. Revision: remember these seven points

1. A web application lets users interact with software through a browser or another client.
2. The frontend displays the interface and collects user actions.
3. The backend processes requests and applies business rules.
4. A database stores application information.
5. An API defines how software components communicate.
6. Python is the programming language; Django is the framework used in this pathway.
7. The backend must validate data and enforce access rules.

**Before moving to Day 2:** Explain the food-order example or student-registration example aloud. If you can describe frontend, backend, database, API, request and response without memorizing the table, you have understood the foundation.

**Next lesson:** Day 2 — Python installation, environment setup, interpreter, VS Code and Jupyter basics.
