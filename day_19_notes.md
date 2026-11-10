# Day 19: Client-Server Architecture and How Websites Work

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations and OOP (Days 1–18)  
**Tools:** Python 3.10+, VS Code, terminal and a web browser  
**Approved mini-project:** Client-Server Communication Simulator

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain what a client and server are.
2. Describe how a browser loads a website.
3. Identify frontend, backend and database responsibilities.
4. Explain DNS, IP address, port and web server.
5. Describe the request-response cycle.
6. Run a local Python HTTP server.
7. Create a simple client that sends an HTTP request.
8. Inspect the request and response.
9. Diagnose common connection errors.

## 2. Start with a familiar website

Imagine opening an online shopping website.

You see:
- Product names and images.
- Search box.
- Login button.
- Cart icon.
- Product prices.

You click a product and see its details. You add it to the cart and place an order.

The browser displays the page, but it does not do every job itself. It communicates with another application that processes requests, checks information and may store or retrieve data.

This leads to the client-server model.

## 3. What is a client?

A **client** is an application or device that requests a service or resource from another system.

Examples:
- A web browser.
- A mobile shopping application.
- A desktop application.
- A Python script calling an API.

The client starts a communication by sending a request.

## 4. What is a server?

A **server** is a program or computer system that receives requests and provides responses or services.

A web server may:
- Receive HTTP requests.
- Route a request to application code.
- Run business logic.
- Read or update a database.
- Return an HTTP response.

A server is not necessarily one physical machine. In modern systems, several services may work together.

## 5. Client and server comparison

| Client | Server |
|---|---|
| Requests resources or actions | Receives and processes requests |
| Often displays the user interface | Often contains business logic |
| May run in browser or mobile app | Runs as a service or application |
| Sends input | Validates and processes input |
| Displays the response | Returns the response |

A client and server are roles in communication. A computer can act as a client in one interaction and a server in another.

## 6. Frontend, backend and database

A typical web application has three important areas:

### 6.1 Frontend

The frontend is the part users interact with.

Examples:
- HTML structure.
- CSS styling.
- JavaScript interactions.
- React or other frontend frameworks.

### 6.2 Backend

The backend handles server-side work.

Examples:
- Login validation.
- Order calculation.
- Business rules.
- API endpoints.
- Permission checks.
- Database operations.

Python and Django are used to build backend applications in this pathway.

### 6.3 Database

A database stores information so it can be retrieved later.

Examples:
- Users.
- Products.
- Orders.
- Payments.
- Employee records.

A simplified architecture:

```text
Browser / Mobile App
        |
        | HTTP request
        v
Python Backend (Django)
        |
        | SQL query
        v
Database (PostgreSQL)
        |
        | Query result
        v
Python Backend
        |
        | HTTP response
        v
Browser / Mobile App
```

The browser usually does not connect directly to the application's private database. The backend mediates access and applies business rules.

## 7. How a website loads: step by step

Suppose the user enters `https://example.com/products`.

A simplified flow:

1. The browser reads the URL.
2. It determines the scheme, hostname and path.
3. DNS helps resolve the hostname to an IP address.
4. The browser establishes a network connection to the server.
5. For HTTPS, TLS is used to secure the connection.
6. The browser sends an HTTP request.
7. The server receives the request.
8. The backend selects the appropriate route or handler.
9. Application logic may query a database.
10. The backend creates an HTTP response.
11. The browser receives the response.
12. The browser renders the page or processes returned data.

Real production networking includes more details such as caches, proxies, load balancers, connection reuse and content delivery networks. This flow is a beginner-friendly model.

## 8. Important networking terms

| Term | Simple meaning |
|---|---|
| URL | Address used to identify a resource |
| Domain name | Human-readable hostname, such as example.com |
| DNS | System that resolves domain names to network records |
| IP address | Network address used to locate a host/interface |
| Port | Number identifying a service endpoint on a host |
| Server | Program/system providing a service |
| Request | Message sent by the client |
| Response | Message returned by the server |
| HTTP | Protocol used for web request-response communication |
| HTTPS | HTTP protected by TLS |

## 9. What is DNS?

Humans prefer names such as `example.com`. Network communication uses IP addresses.

DNS (Domain Name System) helps resolve a domain name to records that provide network information.

A simplified view:

```text
Browser needs example.com
          |
          v
DNS lookup
          |
          v
IP address information
          |
          v
Browser connects to the service
```

DNS does not render the website and does not itself process the application's business logic.

## 10. What is an IP address?

An IP address identifies a network interface or endpoint for communication.

Examples of IPv4 addresses:
- 127.0.0.1
- 192.168.1.10
- 8.8.8.8

`127.0.0.1` is a loopback address. It refers to the local computer.

When a development server listens on 127.0.0.1, it is normally accessible only from the same machine.

## 11. What is a port?

A port identifies a particular service endpoint on a host.

For example:
- A development web server may use port 8000.
- Another local service may use port 5000.
- HTTP commonly uses port 80.
- HTTPS commonly uses port 443.

A port is not the same as an IP address. The IP address identifies the host/interface; the port identifies the service endpoint.

A local address such as `http://127.0.0.1:8000` means:
- HTTP scheme.
- Local machine.
- Port 8000.

## 12. What is localhost?

`localhost` is a hostname that resolves to the local machine, usually a loopback address.

These are common local addresses:
- `http://localhost:8000`
- `http://127.0.0.1:8000`

They are useful when developing and testing applications on your own computer.

## 13. What is request-response communication?

The client sends a request. The server processes it and returns a response.

Example:

Client asks: "Give me the product with ID 10."

Server:
1. Receives the request.
2. Checks the requested route.
3. Validates the input.
4. Retrieves the product.
5. Returns the result or an error.

The detailed HTTP message format will be covered on Day 20 and Day 21.

## 14. Build a tiny local server using Python

We will create a server without Django first. This helps you understand the basic server role.

Create `day_19/server.py`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from the Python backend"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


server = HTTPServer(("127.0.0.1", 8000), RequestHandler)

print("Server is running at http://127.0.0.1:8000")
server.serve_forever()
```

### 14.1 Run the server

Open terminal in the day_19 folder:

```powershell
python server.py
```

Expected terminal message:

```text
Server is running at http://127.0.0.1:8000
```

Keep the terminal open. The server is running and waiting for requests.

### 14.2 Open the browser

Open:

`http://127.0.0.1:8000`

The browser should display:

`Hello from the Python backend`

You have just sent a request from a browser to a local Python server.

### 14.3 Stop the server

Return to the terminal and press Ctrl+C.

The server process stops. Refresh the browser. The browser should now report that it cannot connect.

This demonstrates that a browser needs a running server to receive a response.

## 15. Understand the server code line by line

| Code | Explanation |
|---|---|
| `from http.server import ...` | Imports Python's basic HTTP server classes |
| `class RequestHandler(...)` | Defines how the server handles requests |
| `def do_GET(self)` | Handles an HTTP GET request |
| `message = ...` | Stores the response text |
| `send_response(200)` | Sets the HTTP status code |
| `send_header(...)` | Adds a response header |
| `end_headers()` | Ends the response headers |
| `message.encode("utf-8")` | Converts text to bytes |
| `wfile.write(...)` | Writes response bytes to the client |
| `HTTPServer(...)` | Creates the local HTTP server |
| `serve_forever()` | Keeps waiting for requests |

This Python standard-library server is for learning and local experiments. It is not a production Django deployment server.

## 16. Build a client using Python

A browser is one kind of client. A Python program can also send a request.

Keep the server running. Create another file named `client.py`:

```python
from urllib.request import urlopen

url = "http://127.0.0.1:8000"

with urlopen(url, timeout=5) as response:
    body = response.read().decode("utf-8")

    print("Status:", response.status)
    print("Response:", body)
```

Run in a second terminal:

```powershell
python client.py
```

Expected output:

```text
Status: 200
Response: Hello from the Python backend
```

What happened:
1. urlopen sent an HTTP request.
2. The server handled GET.
3. The server returned status 200 and a text body.
4. The client read the response bytes.
5. decode converted the bytes to a string.
6. The client printed the status and body.

## 17. Change the server response

Change:

```python
message = "Hello from the Python backend"
```

to:

```python
message = "Welcome to the Employee API"
```

Stop the server with Ctrl+C and start it again. Run the client again.

This proves that the response is generated by the server program.

## 18. What happens if the port is already in use?

If another program is already listening on port 8000, the server may fail to start with an address-in-use error.

Try changing:

```python
HTTPServer(("127.0.0.1", 8000), RequestHandler)
```

to:

```python
HTTPServer(("127.0.0.1", 8001), RequestHandler)
```

Then use port 8001 in the browser and client.

Only the port needs to match between the server address and the client URL.

## 19. Common client-server errors

| Symptom | Possible reason | What to check |
|---|---|---|
| Connection refused | Server is not running or wrong port | Start server; verify port |
| Address already in use | Another process uses the port | Choose another port or stop the other process |
| Browser waits indefinitely | Server handler is stuck or not responding | Inspect server terminal and handler |
| 404 Not Found | Requested route does not exist | Check path and routing |
| 500 Internal Server Error | Server-side code failed | Read server traceback/log |
| Name resolution error | Hostname could not be resolved | Check hostname and DNS/network |
| Timeout | Server/network did not respond in time | Check server, firewall and timeout |
| Browser cannot access local service | Wrong host/port or server stopped | Verify URL and server state |

## 20. Client-server architecture in Django

Django is a backend web framework. It provides routing, request objects, views, models, templates and response handling.

A simplified Django flow:

```text
Browser sends HTTP request
          |
          v
Django receives request
          |
          v
URL pattern selects a view
          |
          v
View runs application logic
          |
          v
View may query a model/database
          |
          v
Django creates HTTP response
          |
          v
Browser receives response
```

The Django module begins later in the pathway. Today you only need to understand the architecture.

## 21. Mini-project — Client-Server Communication Simulator

### Requirements

Create a local server that:
1. Responds to a GET request at the root path.
2. Returns a welcome message.
3. Returns a different message for a second path such as /about.
4. Returns a 404 response for an unknown path.
5. Can be tested from a browser and a Python client.

Suggested structure:

```text
projects/day_19/
├── server.py
├── client.py
└── README.md
```

### Extension: handle more than one path

In your handler, inspect `self.path`:

```python
def do_GET(self):
    if self.path == "/":
        status = 200
        message = "Home page"
    elif self.path == "/about":
        status = 200
        message = "About this backend"
    else:
        status = 404
        message = "Page not found"

    self.send_response(status)
    self.send_header("Content-Type", "text/plain; charset=utf-8")
    self.end_headers()
    self.wfile.write(message.encode("utf-8"))
```

Use this as the next step after you understand the first server. Run and test each path.

### Test plan

| Request path | Expected status | Expected body |
|---|---:|---|
| / | 200 | Home page |
| /about | 200 | About this backend |
| /missing | 404 | Page not found |

## 22. Interview questions

**1. What is client-server architecture?**  
A communication model in which a client requests a resource or operation and a server processes the request and returns a response.

**2. What is a client?**  
An application or device that requests a service, such as a browser or mobile app.

**3. What is a server?**  
A program or system that receives requests and provides services or responses.

**4. What is DNS?**  
The Domain Name System resolves domain names to network records, such as IP address records.

**5. What is localhost?**  
A hostname referring to the local machine.

**6. What is a port?**  
A number identifying a service endpoint on a host.

**7. What happens when you enter a website URL?**  
The browser resolves the hostname, establishes a connection, sends an HTTP request, receives a response and processes or renders it.

**8. What is the role of a backend?**  
It processes requests, applies business logic, validates data, interacts with databases and returns responses.

**9. Does the browser normally connect directly to a private application database?**  
No. The backend normally mediates access and applies business rules and authorization.

**10. Is Python's http.server suitable for production deployment?**  
It is useful for learning and simple local testing, but production Django deployments use appropriate production servers and infrastructure.

## 23. MCQs

**Q1. Which application is commonly a web client?**  
A. Browser  
B. PostgreSQL table  
C. Python class definition  
D. Database column  
**Answer: A.** A browser sends requests to web servers.

**Q2. What does DNS help resolve?**  
A. Domain names to network records  
B. Python syntax errors  
C. SQL joins  
D. HTML colors  
**Answer: A.** DNS resolves names such as example.com.

**Q3. What does 127.0.0.1 normally represent?**  
A. Loopback/local machine  
B. A public website  
C. A database table  
D. A port number  
**Answer: A.** It is a loopback IPv4 address.

**Q4. What does port 8000 identify in our example?**  
A. The local service endpoint  
B. The server's source code file  
C. The database username  
D. The HTTP method  
**Answer: A.** The port identifies the server endpoint.

**Q5. Which component usually applies backend business rules?**  
A. Backend application  
B. Browser address bar  
C. DNS resolver  
D. CSS file  
**Answer: A.** Business rules are normally implemented server-side.

**Q6. What happens if the local server is stopped?**  
A. The client cannot receive a response from that server  
B. The browser becomes a database  
C. DNS deletes the domain  
D. The port becomes an IP address  
**Answer: A.** No process is listening to handle the request.

## 24. Daily completion checklist

- [ ] I can explain client and server.
- [ ] I can distinguish frontend, backend and database.
- [ ] I can explain DNS, IP address, localhost and port.
- [ ] I can describe the request-response cycle.
- [ ] I ran the local Python server.
- [ ] I opened the server from a browser.
- [ ] I tested it using a Python client.
- [ ] I tested an unknown path.
- [ ] I can explain common connection errors.

**Next lesson:** Day 20 — HTTP, HTTPS, Requests, Responses and HTTP Methods.
