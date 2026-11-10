# Day 60: PUT, PATCH and DELETE Operations

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–59 — DRF setup, serializers and API basics  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** Complete CRUD REST API

> **Trainer guidance:** Teach HTTP methods with real request examples. Learners should inspect the method, URL, headers, body, status code and response body for every test.

## 1. Learning objectives

- Explain put, patch and delete operations.
- Implement the endpoint using DRF.
- Connect API URLs to views.
- Understand request.data and Response.
- Return suitable status codes.
- Test successful and failed requests.
- Complete Complete CRUD REST API.

## 2. Concept introduction

PUT generally replaces the target resource representation. PATCH applies a partial modification. DELETE removes a resource. API behavior should be consistent, permission-protected and explicit about success and missing records. PATCH uses partial=True in serializers so omitted fields are not treated as missing required values.

## 3. API request flow

```text
Postman / frontend client
       ↓ HTTP method + URL + headers + body
Django URL routing
       ↓
DRF API view
       ↓
Authentication / permissions
       ↓
Serializer / ORM
       ↓
Response data + status code
```

## 4. File-by-file implementation

### profiles/api_views.py

```python
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=(request.method == "PATCH")
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

## 5. Explain the code

### profiles/api_views.py

1. `from django.shortcuts import get_object_or_404` — Imports DRF or Django components.
2. `from rest_framework.decorators import api_view` — Imports DRF or Django components.
3. `from rest_framework.response import Response` — Imports DRF or Django components.
4. `from rest_framework import status` — Imports DRF or Django components.
5. `from .models import Employee` — Imports DRF or Django components.
6. `from .serializers import EmployeeSerializer` — Imports DRF or Django components.
7. ` ` — Part of the endpoint; explain its place in the request flow.
8. `@api_view(["GET", "PUT", "PATCH", "DELETE"])` — Declares allowed HTTP methods for a function-based API view.
9. `def employee_detail(request, pk):` — Defines a view function or method.
10. `    employee = get_object_or_404(Employee, pk=pk)` — Retrieves a record or returns a 404 response.
11. ` ` — Part of the endpoint; explain its place in the request flow.
12. `    if request.method == "GET":` — Part of the endpoint; explain its place in the request flow.
13. `        serializer = EmployeeSerializer(employee)` — Part of the endpoint; explain its place in the request flow.
14. `        return Response(serializer.data)` — Builds an HTTP response, optionally with a status code.
15. ` ` — Part of the endpoint; explain its place in the request flow.
16. `    if request.method in ["PUT", "PATCH"]:` — Part of the endpoint; explain its place in the request flow.
17. `        serializer = EmployeeSerializer(` — Part of the endpoint; explain its place in the request flow.
18. `            employee,` — Part of the endpoint; explain its place in the request flow.
19. `            data=request.data,` — Reads parsed incoming request body data.
20. `            partial=(request.method == "PATCH")` — Part of the endpoint; explain its place in the request flow.
21. `        )` — Part of the endpoint; explain its place in the request flow.
22. `        if serializer.is_valid():` — Validates incoming data.
23. `            serializer.save()` — Creates or updates a model instance after validation.
24. `            return Response(serializer.data)` — Builds an HTTP response, optionally with a status code.
25. `        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)` — Builds an HTTP response, optionally with a status code.
26. ` ` — Part of the endpoint; explain its place in the request flow.
27. `    employee.delete()` — Part of the endpoint; explain its place in the request flow.
28. `    return Response(status=status.HTTP_204_NO_CONTENT)` — Builds an HTTP response, optionally with a status code.

## 6. HTTP methods and expected behavior

| Method | Common use | Typical successful status |
|---|---|---|
| GET | Retrieve a resource | 200 OK |
| POST | Create a resource | 201 Created |
| PUT | Replace/update a resource | 200 OK or 204 No Content |
| PATCH | Partially update a resource | 200 OK |
| DELETE | Delete a resource | 204 No Content |

Actual API behavior should be documented consistently. A server may return a different successful code depending on the design.

## 7. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| 405 Method Not Allowed | Allowed methods in @api_view or APIView |
| 400 Bad Request | Serializer errors and request payload |
| 404 Not Found | URL path and primary key |
| 415 Unsupported Media Type | Content-Type header |
| 500 Server Error | Server traceback and unexpected exception |
| POST creates duplicate records | Business rules and database constraints |
| PATCH requires omitted fields | partial=True and serializer configuration |

## 8. Industry scenario

PUT generally replaces the target resource representation. PATCH applies a partial modification. DELETE removes a resource. API behavior should be consistent, permission-protected and explicit about success and missing records. PATCH uses partial=True in serializers so omitted fields are not treated as missing required values.

## 9. Approved mini-project — Complete CRUD REST API

**Objective:** Complete CRUD REST API.

### Required tasks

1. Create a detail endpoint with an integer primary key.
2. Retrieve the object using get_object_or_404().
3. Implement GET to return one serialized record.
4. Implement PUT using a full update payload.
5. Implement PATCH using partial=True.
6. Validate input before saving changes.
7. Implement DELETE and return 204 No Content after success.
8. Test missing IDs and invalid update data.
9. Protect write operations using authentication and permissions when appropriate.

### Suggested structure

```text
projects/day_60/
├── README.md
├── config/
└── profiles/
    ├── api_views.py
    ├── api_urls.py
    ├── serializers.py
    ├── models.py
    └── tests/
```

### Validation checklist

- [ ] GET returns the selected record.
- [ ] PUT requires a complete valid representation according to serializer rules.
- [ ] PATCH updates only supplied fields.
- [ ] Invalid update returns 400.
- [ ] DELETE removes the intended record and returns 204.
- [ ] Missing ID returns 404.
- [ ] Write operations are protected in the production-ready version.

### Postman test matrix

| Test | Method | Expected result |
|---|---|---|
| Retrieve collection or record | GET | JSON representation |
| Create with valid payload | POST | 201 and created data |
| Create with invalid payload | POST | 400 and field errors |
| Update existing record | PUT | Updated representation |
| Partially update one field | PATCH | Only supplied field changes |
| Delete existing record | DELETE | 204 |
| Request missing ID | GET/PUT/PATCH/DELETE | 404 |

## 10. AI-assisted implementation

**Planning prompt:** "Help me plan Complete CRUD REST API. List endpoints, HTTP methods, payloads, status codes and test cases. Do not provide the complete implementation."

**Guided prompt:** "Help me implement one endpoint at a time. Explain the request and response and wait for my Postman result."

**Debugging prompt:** "Here is my request method, URL, headers, payload, response status and server traceback. Trace the failure and suggest the smallest fix."

**Review prompt:** "Review the endpoint for method semantics, validation, permissions, status codes and error handling."

## 11. Five daily MCQs

**Q1. What is the main purpose of today's API operations?**  
A. Handle resource requests and changes through HTTP methods.  
B. Replace the Django ORM.  
C. Disable JSON.  
D. Remove serializers.  
**Answer: A.** API methods define resource operations.

**Q2. Which method is commonly used to create a resource?**  
A. GET  
B. POST  
C. HEAD  
D. OPTIONS  
**Answer: B.** POST commonly submits data to create a resource.

**Q3. Which serializer option supports partial updates?**  
A. many=True  
B. read_only=True  
C. partial=True  
D. allow_null=True  
**Answer: C.** partial=True allows omitted fields during PATCH.

**Q4. What does 404 indicate?**  
A. Created.  
B. Successful update.  
C. Server started.  
D. Requested resource was not found.  
**Answer: D.** 404 is Not Found.

**Q5. What should be verified after DELETE?**  
A. The record is removed and the response status is correct.  
B. The editor theme.  
C. The URL name only.  
D. The Python version.  
**Answer: A.** Verify the database state and response.

## 12. Interview preparation

**Q1. Explain put, patch and delete operations.**  
**Answer:** PUT generally replaces the target resource representation. PATCH applies a partial modification. DELETE removes a resource. API behavior should be consistent, permission-protected and explicit about success and missing records. PATCH uses partial=True in serializers so omitted fields are not treated as missing required values.

**Q2. What is the difference between PUT and PATCH?**  
**Answer:** PUT generally replaces the target representation; PATCH applies a partial update.

**Q3. Why should a view return an appropriate status code?**  
**Answer:** It communicates the outcome to API clients consistently and lets clients handle success and failure correctly.

**Follow-up:** What do you test for a missing ID?  
**Answer:** The endpoint should return a 404 response rather than an unhandled server error.

## 13. Completion checklist

- [ ] Explain the HTTP methods.
- [ ] Implement the endpoint.
- [ ] Test each method in Postman.
- [ ] Verify status codes and response bodies.
- [ ] Test invalid and missing-record cases.
- [ ] Complete Complete CRUD REST API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman evidence and README.

**Next lesson:** Day 61.
