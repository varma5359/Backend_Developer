# Day 20: HTTP, HTTPS, Requests, Responses and HTTP Methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Day 19 — Client-Server Architecture  
**Tools:** Python 3.10+, VS Code, terminal and browser  
**Approved mini-project:** HTTP Request Explorer

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain HTTP and HTTPS.
2. Describe the structure and purpose of an HTTP request.
3. Describe the structure and purpose of an HTTP response.
4. Identify common HTTP methods.
5. Explain GET, POST, PUT, PATCH and DELETE.
6. Understand safe and idempotent method concepts at a beginner level.
7. Send HTTP requests using Python.
8. Inspect method, URL, headers, status and response body.
9. Build an HTTP Request Explorer.

## 2. Why HTTP matters

On Day 19, we saw a browser sending a request to a local Python server.

But what exactly is sent?

The browser and server need a common communication protocol. For web applications, that protocol is HTTP.

HTTP defines how a client and server exchange request and response messages.

Examples:
- Browser requests a product page.
- Mobile app sends login details.
- Frontend submits a new order.
- Backend returns a list of employees.
- Client requests deletion of a resource.

## 3. What is HTTP?

**HTTP** stands for Hypertext Transfer Protocol.

It is an application-layer protocol used for communication between clients and servers.

A typical HTTP interaction:

```text
Client
  |
  | HTTP request
  v
Server
  |
  | HTTP response
  v
Client
```

HTTP does not decide your business rules. It defines the message exchange used to communicate those requests and responses.

## 4. What is HTTPS?

**HTTPS** is HTTP communication protected using TLS (Transport Layer Security).

TLS helps provide:
- Confidentiality: others on the network should not be able to read protected traffic.
- Integrity: tampering with traffic can be detected.
- Authentication of the server through certificates.

Use HTTPS for websites and APIs accessed over networks. Do not send passwords or sensitive data over plain HTTP on an untrusted network.

Important:
- HTTP is the application protocol.
- TLS protects the connection.
- HTTPS is HTTP over TLS.

## 5. HTTP request structure

A request commonly contains:

1. Request method.
2. Request target/path.
3. HTTP version.
4. Headers.
5. Optional body.

Simplified example:

```http
GET /products/10 HTTP/1.1
Host: example.com
Accept: application/json
User-Agent: DemoClient/1.0
```

Explanation:

| Part | Meaning |
|---|---|
| GET | Method |
| /products/10 | Resource path |
| HTTP/1.1 | Protocol version |
| Host | Hostname being requested |
| Accept | Content types the client can process |
| User-Agent | Client software information |

GET requests commonly have no body, although protocol details can allow bodies in some cases. API design should follow clear conventions.

## 6. HTTP response structure

A response commonly contains:

1. HTTP version.
2. Status code.
3. Reason phrase (in HTTP/1.1 textual form).
4. Headers.
5. Optional response body.

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 32

{"id":10,"name":"Keyboard"}
```

Explanation:
- 200 indicates successful processing.
- Content-Type describes the body format.
- Content-Length gives the body length in bytes for this example.
- The body contains JSON data.

## 7. HTTP methods

An HTTP method communicates the intended action.

| Method | Common API meaning | Example |
|---|---|---|
| GET | Retrieve a resource | Read product 10 |
| POST | Submit data / create a subordinate resource | Create an order |
| PUT | Replace a resource representation | Replace employee 10 |
| PATCH | Partially update a resource | Change employee 10's department |
| DELETE | Delete a resource | Delete product 10 |
| HEAD | Get response headers without the usual response body | Check resource metadata |
| OPTIONS | Ask about communication options | Inspect allowed methods |

The exact business behavior is defined by the API. The method communicates the intended operation.

## 8. GET — retrieve information

Example:

```http
GET /employees/101
```

A backend may return:

```json
{
  "employee_id": 101,
  "name": "Anil",
  "department": "IT"
}
```

GET should be safe: it is intended to retrieve information without requesting a business-state change.

GET is often idempotent: repeating the same request should have the same intended effect on server state. The response can still differ if data changes between requests.

## 9. POST — submit or create

Example:

```http
POST /employees
Content-Type: application/json

{
  "name": "Anil",
  "department": "IT"
}
```

The backend may validate the input, create an employee and return the created resource.

POST is not generally idempotent. Repeating a create request may create multiple records unless the API implements duplicate protection or idempotency handling.

## 10. PUT — replace a resource

Example:

```http
PUT /employees/101
Content-Type: application/json

{
  "name": "Anil Kumar",
  "department": "Engineering"
}
```

PUT is generally used to replace the target resource representation. API-specific behavior may define fields and defaults.

PUT is defined as idempotent in HTTP semantics: repeating the same intended replacement should not keep creating additional effects.

## 11. PATCH — partially update a resource

Example:

```http
PATCH /employees/101
Content-Type: application/json

{
  "department": "Engineering"
}
```

PATCH applies a partial modification. It is useful when the client only needs to change selected fields.

Do not assume every PATCH request is idempotent. It depends on the patch operation and API design.

## 12. DELETE — remove a resource

Example:

```http
DELETE /employees/101
```

The server processes the deletion request. A successful response might use 200 or 204 depending on the API design.

DELETE is defined as idempotent in its intended effect: deleting the same resource repeatedly should leave it absent. The response status may differ between attempts.

## 13. Safe and idempotent: beginner explanation

These terms describe HTTP method semantics.

**Safe:** the method is intended not to change server state.

**Idempotent:** making the same request one or more times has the same intended effect on server state as making it once.

| Method | Safe? | Idempotent? | Typical intention |
|---|---|---|---|
| GET | Yes | Yes | Read |
| HEAD | Yes | Yes | Read metadata |
| OPTIONS | Yes | Yes | Discover options |
| POST | No | Not generally | Submit/create |
| PUT | No | Yes | Replace |
| PATCH | No | Not guaranteed | Partial update |
| DELETE | No | Yes | Remove |

Do not confuse idempotency with identical response text. The server state effect is the important point.

## 14. Query parameters

A URL may contain query parameters.

Example:

`/products?category=electronics&limit=10`

- category is a parameter name.
- electronics is its value.
- limit is another parameter.
- 10 is its value.

Query parameters are commonly used for filtering, searching, sorting and pagination.

They are part of the URL, not the request body.

## 15. Request body

A request body carries data sent by the client, often for POST, PUT or PATCH.

Example JSON body:

```json
{
  "name": "Priya",
  "department": "HR"
}
```

The backend should validate all client-provided data. Never assume a frontend validation rule is sufficient.

## 16. Build an HTTP request using Python

We will use Python's standard library so no external package is required.

Create `day_20/get_request.py`:

```python
from urllib.request import Request, urlopen

url = "https://httpbin.org/get"

request = Request(
    url,
    method="GET",
    headers={"Accept": "application/json"}
)

with urlopen(request, timeout=10) as response:
    body = response.read().decode("utf-8")

    print("Status:", response.status)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Response body:")
    print(body)
```

Run:

```powershell
python get_request.py
```

This example needs internet access and the external test service to be available. The response body may include request metadata, so do not expect every character to be identical every time.

### 16.1 Understand the code

- Request and urlopen are imported from urllib.request.
- url stores the target address.
- Request creates a request object with method and headers.
- urlopen sends the request.
- timeout limits how long the client waits.
- response.status reads the status code.
- response.headers reads response headers.
- response.read() returns bytes.
- decode("utf-8") converts bytes to text.

## 17. Send POST JSON with Python

Create `post_request.py`:

```python
import json
from urllib.request import Request, urlopen

url = "https://httpbin.org/post"

payload = {
    "name": "Asha",
    "course": "Backend Development"
}

body = json.dumps(payload).encode("utf-8")

request = Request(
    url,
    data=body,
    method="POST",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
)

with urlopen(request, timeout=10) as response:
    print("Status:", response.status)
    print(response.read().decode("utf-8"))
```

What is happening?

1. payload is a Python dictionary.
2. json.dumps converts it into JSON text.
3. encode converts the text into bytes.
4. Request receives the bytes as its body.
5. Content-Type tells the server that the body is JSON.
6. Accept tells the server which response format the client prefers.
7. urlopen sends the request.

## 18. Understand Content-Type and Accept

These headers are easy to confuse.

| Header | Direction / purpose |
|---|---|
| Content-Type | Describes the format of the body being sent in this message |
| Accept | Communicates the response media types the client can accept |

Example:
- A client sends JSON: Content-Type: application/json.
- A client wants JSON back: Accept: application/json.

## 19. HTTP Request Explorer mini-project

### Requirements

Build a small command-line program that:
1. Sends a GET request to a test endpoint.
2. Prints the response status.
3. Prints Content-Type.
4. Sends a POST request with a JSON payload.
5. Displays the returned JSON.
6. Handles network errors and timeouts.

Suggested structure:

```text
projects/day_20_http_request_explorer/
├── get_request.py
├── post_request.py
├── main.py
└── README.md
```

### Add error handling

```python
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

try:
    with urlopen("https://httpbin.org/get", timeout=5) as response:
        print("Status:", response.status)
        print(response.read().decode("utf-8"))
except HTTPError as error:
    print("HTTP error:", error.code)
except URLError as error:
    print("Network error:", error.reason)
except TimeoutError:
    print("The request timed out")
```

### Test plan

| Test | Action | Expected |
|---|---|---|
| 1 | Send GET | Successful response if service available |
| 2 | Send POST JSON | Response includes submitted JSON |
| 3 | Print status | Numeric status appears |
| 4 | Print Content-Type | Media type appears |
| 5 | Disconnect internet | Network error is handled |
| 6 | Use an invalid endpoint | HTTP or URL error is handled |

## 20. Common mistakes

| Mistake | Why it matters | Correction |
|---|---|---|
| Using POST to read everything | Method semantics become unclear | Use GET for retrieval |
| Sending JSON without Content-Type | Server may not know the body format | Set application/json |
| Confusing Accept and Content-Type | Request/response expectations become incorrect | Remember what body each header describes |
| Treating PUT and PATCH as identical | Full replacement and partial modification differ | Choose based on API contract |
| Assuming POST is idempotent | Repeated requests can create duplicates | Use API idempotency strategy where required |
| Ignoring status codes | A response may represent an error | Inspect status and body |
| No timeout | Client may wait too long | Set a reasonable timeout |
| Trusting frontend validation | Requests can be sent by any client | Validate on the backend |

## 21. Interview questions

**1. What is HTTP?**  
An application-layer protocol used for request-response communication between clients and servers.

**2. What is HTTPS?**  
HTTP protected using TLS.

**3. What is an HTTP request?**  
A message sent by a client containing a method, target, headers and optionally a body.

**4. What is an HTTP response?**  
A message returned by the server containing a status, headers and optionally a body.

**5. Difference between GET and POST?**  
GET is intended to retrieve information; POST submits data for processing or resource creation according to the API.

**6. Difference between PUT and PATCH?**  
PUT generally replaces the resource representation; PATCH applies a partial modification.

**7. Is GET safe?**  
Yes, it is intended not to change server state.

**8. What does idempotent mean?**  
Repeating the same request has the same intended effect on server state as performing it once.

**9. What is Content-Type?**  
A header describing the media type of the message body.

**10. What is Accept?**  
A request header indicating response media types the client can process.

## 22. MCQs

**Q1. Which protocol protects HTTP using TLS?**  
A. HTTPS  
B. FTP  
C. SMTP  
D. SQL  
**Answer: A.** HTTPS is HTTP over TLS.

**Q2. Which method is commonly used to retrieve a resource?**  
A. GET  
B. POST  
C. DELETE  
D. PATCH  
**Answer: A.** GET is intended for retrieval.

**Q3. Which method is commonly used for partial modification?**  
A. HEAD  
B. PATCH  
C. OPTIONS  
D. GET  
**Answer: B.** PATCH applies partial changes.

**Q4. Which header describes the format of the body being sent?**  
A. Accept  
B. Content-Type  
C. Host only  
D. User-Agent  
**Answer: B.** Content-Type describes the message body.

**Q5. Which method is defined as safe?**  
A. GET  
B. POST  
C. DELETE  
D. PATCH  
**Answer: A.** GET is intended not to change server state.

**Q6. What does idempotent describe?**  
A. Same intended server-state effect when repeated  
B. Identical response text always  
C. Faster network speed  
D. Database indexing  
**Answer: A.** Idempotency concerns the intended effect on server state.

## 23. Completion checklist

- [ ] I can explain HTTP and HTTPS.
- [ ] I can identify request and response parts.
- [ ] I can explain GET, POST, PUT, PATCH and DELETE.
- [ ] I understand safe and idempotent.
- [ ] I can explain query parameters and request body.
- [ ] I can distinguish Accept from Content-Type.
- [ ] I sent GET and POST requests with Python.
- [ ] I handled network and HTTP errors.

**Next lesson:** Day 21 — HTTP Status Codes, Headers, Request Body and Response Body.
