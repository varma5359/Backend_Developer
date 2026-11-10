# Day 21: HTTP Status Codes, Headers, Request Body and Response Body

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Days 19–20 — Client-server architecture and HTTP methods  
**Tools:** Python 3.10+, VS Code, terminal, browser and Postman (optional)  
**Approved mini-project:** HTTP Response Analyzer

---

## 1. Learning objectives

By the end of this lesson, you can:
1. Explain why HTTP status codes exist.
2. Identify the five status-code categories.
3. Recognize common success, redirect, client-error and server-error codes.
4. Explain HTTP headers.
5. Distinguish request headers from response headers.
6. Explain request body and response body.
7. Inspect status, headers and body using Python.
8. Diagnose common API responses.
9. Build an HTTP Response Analyzer.

## 2. Why do status codes matter?

Imagine a mobile application requests an employee record.

Several outcomes are possible:
- The record is found.
- The record is not found.
- The user is not logged in.
- The user is logged in but does not have permission.
- The request body is invalid.
- The backend has an unexpected error.

The client needs a standard way to understand the result. HTTP status codes provide that signal.

## 3. Five categories of status codes

| Range | Category | Simple meaning |
|---|---|---|
| 100–199 | Informational | Request processing continues |
| 200–299 | Success | Request succeeded |
| 300–399 | Redirection | Further action or another location is involved |
| 400–499 | Client error | Problem with the request or client context |
| 500–599 | Server error | Server failed to complete a valid-looking request |

The first digit identifies the broad category.

## 4. Important 2xx success codes

| Code | Name | Common use |
|---:|---|---|
| 200 | OK | Request succeeded |
| 201 | Created | New resource created |
| 202 | Accepted | Request accepted for later processing |
| 204 | No Content | Request succeeded with no response body |

Examples:
- GET employee succeeds: 200.
- POST creates an employee: 201.
- DELETE succeeds without a response body: 204 can be appropriate.

The API design determines the exact response code.

## 5. Important 3xx redirect codes

| Code | Name | Meaning |
|---:|---|---|
| 301 | Moved Permanently | Resource has a permanent new location |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cached representation may be reused |

A redirect tells the client that another action or cached representation may be relevant. Redirect semantics can vary by code and method; do not treat every redirect as identical.

## 6. Important 4xx client-error codes

| Code | Name | Common meaning |
|---:|---|---|
| 400 | Bad Request | Request is malformed or invalid |
| 401 | Unauthorized | Authentication is missing or invalid |
| 403 | Forbidden | Server refuses the action, often due to permissions |
| 404 | Not Found | Requested resource/route not found |
| 405 | Method Not Allowed | Method is not supported for this resource |
| 409 | Conflict | Request conflicts with current resource state |
| 415 | Unsupported Media Type | Body media type is not supported |
| 422 | Unprocessable Content | Request content is understood but cannot be processed semantically |
| 429 | Too Many Requests | Rate limit exceeded |

Important distinction:
- 401 usually means the client must authenticate.
- 403 means the server understood the request but refuses it.
- 404 means the requested resource or route was not found.

## 7. Important 5xx server-error codes

| Code | Name | Meaning |
|---:|---|---|
| 500 | Internal Server Error | Unexpected server failure |
| 501 | Not Implemented | Server does not support the required functionality |
| 502 | Bad Gateway | Gateway/proxy received an invalid upstream response |
| 503 | Service Unavailable | Service temporarily unavailable |
| 504 | Gateway Timeout | Gateway/proxy did not receive a timely upstream response |

If you receive 500, inspect server logs. Do not expose internal stack traces or secrets to public API clients.

## 8. Status code examples in an employee API

| Scenario | Possible status |
|---|---:|
| Employee list returned | 200 |
| Employee created | 201 |
| Employee deleted with no body | 204 |
| Invalid JSON | 400 |
| Missing/invalid login credentials | 401 |
| User lacks permission | 403 |
| Employee ID does not exist | 404 |
| Unsupported HTTP method | 405 |
| Duplicate employee number conflict | 409 |
| Too many requests | 429 |
| Unexpected backend exception | 500 |

These are common design choices, not a guarantee that every API uses exactly the same mapping.

## 9. What are HTTP headers?

Headers are metadata fields sent with HTTP requests and responses.

Headers communicate information such as:
- Content format.
- Accepted response format.
- Authentication information.
- Caching rules.
- Cookies.
- Request tracing.
- Server metadata.

Example request:

```http
GET /employees HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer example-token
User-Agent: EmployeeClient/1.0
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
X-Request-ID: abc123

{"employees":[]}
```

Do not use real access tokens in screenshots or teaching examples. The token above is a placeholder.

## 10. Common request headers

| Header | Purpose |
|---|---|
| Host | Target hostname in HTTP/1.1 |
| Accept | Response media types the client can accept |
| Content-Type | Format of the body being sent |
| Authorization | Credentials or authorization information |
| User-Agent | Identifies the client software |
| Cookie | Sends stored cookies to the server |
| Origin | Indicates the origin of a browser request |
| If-None-Match | Conditional request using an entity tag |

## 11. Common response headers

| Header | Purpose |
|---|---|
| Content-Type | Format of the response body |
| Content-Length | Body length in bytes, when supplied |
| Cache-Control | Caching instructions |
| Set-Cookie | Asks the client to store a cookie |
| Location | Target location for certain redirects or resource creation responses |
| ETag | Identifier for a representation version |
| Retry-After | Suggests when a client may retry |
| Access-Control-Allow-Origin | CORS response header controlling permitted browser origins |

Headers have precise semantics. Do not copy security-related headers into production without understanding the policy they implement.

## 12. Request body

A request body carries data from the client to the server.

Example:

```http
POST /employees HTTP/1.1
Content-Type: application/json

{
  "name": "Asha",
  "department": "IT"
}
```

The body is JSON text in this example. The server must parse and validate it.

A body is commonly used with POST, PUT and PATCH. GET requests generally use the URL and query parameters for retrieval criteria.

## 13. Response body

A response body contains the content returned by the server.

Example:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "employee_id": 101,
  "name": "Asha",
  "department": "IT"
}
```

A response body can contain:
- JSON.
- HTML.
- Plain text.
- An image or other binary data.
- No body, such as a 204 response.

The Content-Type header tells the client how to interpret the body.

## 14. Inspect a response using Python

Create `inspect_response.py`:

```python
from urllib.request import urlopen

url = "https://httpbin.org/get"

with urlopen(url, timeout=10) as response:
    print("Status:", response.status)
    print("Reason:", response.reason)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("All headers:")
    for name, value in response.headers.items():
        print(name, ":", value)

    body = response.read().decode("utf-8")
    print("Response body:")
    print(body)
```

Run:

```powershell
python inspect_response.py
```

The example requires internet access. The exact headers and body may vary.

### 14.1 Explanation

- urlopen sends the request.
- response.status is the HTTP status.
- response.reason is a reason phrase where provided by the client library.
- response.headers provides response metadata.
- items() iterates through header name/value pairs.
- response.read() reads the body as bytes.
- decode("utf-8") converts the body to text.

## 15. Handle HTTP errors

Some Python HTTP client functions raise an HTTPError for error status responses.

```python
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

url = "https://httpbin.org/status/404"

try:
    with urlopen(url, timeout=10) as response:
        print("Status:", response.status)
        print(response.read().decode("utf-8"))
except HTTPError as error:
    print("HTTP status:", error.code)
    print("Reason:", error.reason)
except URLError as error:
    print("Connection problem:", error.reason)
except TimeoutError:
    print("Request timed out")
```

Expected behavior: the program reports HTTP status 404 instead of crashing with an unhandled traceback.

## 16. Request headers with Python

```python
from urllib.request import Request, urlopen

request = Request(
    "https://httpbin.org/headers",
    headers={
        "Accept": "application/json",
        "User-Agent": "TechPhile-Learning-Client/1.0"
    }
)

with urlopen(request, timeout=10) as response:
    print(response.read().decode("utf-8"))
```

The test endpoint returns the headers it received. This lets you inspect the request metadata.

## 17. Build a simple response analyzer

Create a helper function:

```python
def explain_status(status_code):
    if 200 <= status_code <= 299:
        return "Success response"
    elif 300 <= status_code <= 399:
        return "Redirection response"
    elif 400 <= status_code <= 499:
        return "Client error response"
    elif 500 <= status_code <= 599:
        return "Server error response"
    else:
        return "Informational or non-standard response"

print(explain_status(200))
print(explain_status(404))
print(explain_status(500))
```

Output:

```text
Success response
Client error response
Server error response
```

This function classifies the broad category. It does not replace handling the meaning of each individual status code.

## 18. Mini-project — HTTP Response Analyzer

### Requirements

Build a command-line tool that:
1. Requests a test endpoint.
2. Displays status code and category.
3. Displays response headers.
4. Displays the response body.
5. Handles 404 and other HTTP errors.
6. Handles connection failures and timeouts.
7. Allows the learner to test at least three URLs.

Suggested structure:

```text
projects/day_21_http_response_analyzer/
├── main.py
└── README.md
```

### Suggested URLs

- `https://httpbin.org/get`
- `https://httpbin.org/status/404`
- `https://httpbin.org/status/500`

These are public test endpoints; they require internet access and may occasionally be unavailable.

### Validation table

| Test | URL / situation | Expected observation |
|---|---|---|
| 1 | /get | Successful status and response |
| 2 | /status/404 | HTTP 404 handled |
| 3 | /status/500 | HTTP 500 handled |
| 4 | Invalid hostname | URL/network error |
| 5 | Slow/unreachable endpoint | Timeout handling |
| 6 | Inspect headers | Header names and values displayed |

## 19. Common mistakes

| Mistake | Correction |
|---|---|
| Treating all 4xx responses as the same | Understand 400, 401, 403, 404 and 409 separately |
| Treating 500 as a client error | 5xx indicates server-side failure |
| Confusing headers and body | Headers are metadata; body carries content |
| Confusing request and response headers | Identify which direction the message travels |
| Assuming every response has a body | 204 commonly has no response body |
| Printing secret authorization headers | Redact tokens and credentials |
| Exposing stack traces to users | Log internal detail securely; return safe error messages |
| Ignoring status codes | Check the status before assuming success |

## 20. Interview questions

**1. What is an HTTP status code?**  
A numeric value in an HTTP response that communicates the result category of the request.

**2. What are the five status-code categories?**  
1xx informational, 2xx success, 3xx redirection, 4xx client error and 5xx server error.

**3. Difference between 401 and 403?**  
401 indicates missing or invalid authentication credentials; 403 indicates the server refuses the action, often because the user lacks permission.

**4. Difference between 404 and 500?**  
404 means the requested resource or route was not found; 500 indicates an unexpected server failure.

**5. What is an HTTP header?**  
A metadata field in a request or response.

**6. What is a request body?**  
Data sent from the client to the server as part of the request.

**7. What is a response body?**  
Content returned by the server.

**8. What does Content-Type do?**  
It describes the media type of the message body.

**9. What does 204 mean?**  
The request succeeded and the response has no content body.

**10. Why should stack traces not be returned to public clients?**  
They can expose implementation details, file paths, queries or secrets. Detailed errors belong in protected logs.

## 21. MCQs

**Q1. Which status category represents success?**  
A. 2xx  
B. 3xx  
C. 4xx  
D. 5xx  
**Answer: A.** 2xx responses indicate success.

**Q2. Which code commonly means resource not found?**  
A. 200  
B. 301  
C. 404  
D. 500  
**Answer: C.** 404 is Not Found.

**Q3. Which code commonly indicates authentication is required or invalid?**  
A. 401  
B. 403  
C. 404  
D. 503  
**Answer: A.** 401 is an authentication-related response.

**Q4. Which code indicates an unexpected server error?**  
A. 201  
B. 302  
C. 400  
D. 500  
**Answer: D.** 500 is Internal Server Error.

**Q5. Which part contains the JSON employee record?**  
A. Response body  
B. Status code  
C. Port  
D. DNS record  
**Answer: A.** The response body carries the returned representation.

**Q6. Which header describes the body media type?**  
A. Content-Type  
B. Host  
C. User-Agent  
D. Location only  
**Answer: A.** Content-Type identifies the body format.

## 22. Completion checklist

- [ ] I can explain status-code categories.
- [ ] I can distinguish 401, 403, 404 and 500.
- [ ] I understand request and response headers.
- [ ] I understand request and response bodies.
- [ ] I can inspect status and headers using Python.
- [ ] I can handle HTTP and connection errors.
- [ ] I completed HTTP Response Analyzer.
- [ ] I can explain why sensitive details must not be exposed.

**Next lesson:** Day 22 — JSON, XML Basics and Data Exchange Between Applications.
