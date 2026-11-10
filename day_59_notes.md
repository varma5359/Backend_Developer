# Day 59: GET and POST Requests Using Django REST Framework

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–59 — DRF setup, serializers and API basics  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** Student Registration API

> **Trainer guidance:** Teach HTTP methods with real request examples. Learners should inspect the method, URL, headers, body, status code and response body for every test.

## 1. Learning objectives

- Explain get and post requests using django rest framework.
- Implement the endpoint using DRF.
- Connect API URLs to views.
- Understand request.data and Response.
- Return suitable status codes.
- Test successful and failed requests.
- Complete Student Registration API.

## 2. Concept introduction

GET retrieves a representation of a resource. POST submits data, commonly to create a new resource. In DRF, request.data parses supported request bodies, serializers validate the payload and Response returns structured data with an appropriate HTTP status code.

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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(["GET", "POST"])
def employee_collection(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### profiles/api_urls.py

```python
from django.urls import path
from .api_views import employee_collection

urlpatterns = [
    path("employees/", employee_collection, name="employee_collection"),
]
```

## 5. Explain the code

### profiles/api_views.py

1. `from rest_framework.decorators import api_view` — Imports DRF or Django components.
2. `from rest_framework.response import Response` — Imports DRF or Django components.
3. `from rest_framework import status` — Imports DRF or Django components.
4. `from .models import Employee` — Imports DRF or Django components.
5. `from .serializers import EmployeeSerializer` — Imports DRF or Django components.
6. ` ` — Part of the endpoint; explain its place in the request flow.
7. `@api_view(["GET", "POST"])` — Declares allowed HTTP methods for a function-based API view.
8. `def employee_collection(request):` — Defines a view function or method.
9. `    if request.method == "GET":` — Part of the endpoint; explain its place in the request flow.
10. `        employees = Employee.objects.all()` — Part of the endpoint; explain its place in the request flow.
11. `        serializer = EmployeeSerializer(employees, many=True)` — Part of the endpoint; explain its place in the request flow.
12. `        return Response(serializer.data)` — Builds an HTTP response, optionally with a status code.
13. ` ` — Part of the endpoint; explain its place in the request flow.
14. `    serializer = EmployeeSerializer(data=request.data)` — Reads parsed incoming request body data.
15. `    if serializer.is_valid():` — Validates incoming data.
16. `        serializer.save()` — Creates or updates a model instance after validation.
17. `        return Response(serializer.data, status=status.HTTP_201_CREATED)` — Builds an HTTP response, optionally with a status code.
18. ` ` — Part of the endpoint; explain its place in the request flow.
19. `    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)` — Builds an HTTP response, optionally with a status code.

### profiles/api_urls.py

1. `from django.urls import path` — Imports DRF or Django components.
2. `from .api_views import employee_collection` — Imports DRF or Django components.
3. ` ` — Part of the endpoint; explain its place in the request flow.
4. `urlpatterns = [` — Part of the endpoint; explain its place in the request flow.
5. `    path("employees/", employee_collection, name="employee_collection"),` — Part of the endpoint; explain its place in the request flow.
6. `]` — Part of the endpoint; explain its place in the request flow.

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

GET retrieves a representation of a resource. POST submits data, commonly to create a new resource. In DRF, request.data parses supported request bodies, serializers validate the payload and Response returns structured data with an appropriate HTTP status code.

## 9. Approved mini-project — Student Registration API

**Objective:** Student Registration API.

### Required tasks

1. Create a collection endpoint for employees.
2. Implement GET to retrieve all employee records.
3. Serialize the queryset using many=True.
4. Implement POST to read request.data.
5. Pass the payload to EmployeeSerializer(data=...).
6. Call is_valid() before save().
7. Return 201 Created after successful creation.
8. Return 400 Bad Request with serializer.errors for invalid data.
9. Test both methods using Postman.

### Suggested structure

```text
projects/day_59/
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

- [ ] GET returns a JSON list.
- [ ] POST with valid data creates a record.
- [ ] Successful POST returns 201.
- [ ] Invalid POST returns 400 with field errors.
- [ ] Unsupported methods are rejected.
- [ ] The database contains only validated records.

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

**Planning prompt:** "Help me plan Student Registration API. List endpoints, HTTP methods, payloads, status codes and test cases. Do not provide the complete implementation."

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

**Q1. Explain get and post requests using django rest framework.**  
**Answer:** GET retrieves a representation of a resource. POST submits data, commonly to create a new resource. In DRF, request.data parses supported request bodies, serializers validate the payload and Response returns structured data with an appropriate HTTP status code.

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
- [ ] Complete Student Registration API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman evidence and README.

**Next lesson:** Day 60.
