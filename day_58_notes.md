# Day 58: Function-Based API Views and APIView

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–59 — DRF setup, serializers and API basics  
**Tools:** Python, Django, Django REST Framework, VS Code, terminal and Postman  
**Approved mini-project:** Employee REST API

> **Trainer guidance:** Teach HTTP methods with real request examples. Learners should inspect the method, URL, headers, body, status code and response body for every test.

## 1. Learning objectives

- Explain function-based api views and apiview.
- Implement the endpoint using DRF.
- Connect API URLs to views.
- Understand request.data and Response.
- Return suitable status codes.
- Test successful and failed requests.
- Complete Employee REST API.

## 2. Concept introduction

DRF supports function-based API views using @api_view and class-based API views using APIView. These abstractions provide request parsing, response rendering, authentication and permission integration. Choose a style that fits the endpoint and keep business logic understandable.

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

@api_view(["GET"])
def api_home(request):
    return Response({
        "message": "Employee API",
        "version": "v1"
    })
```

### APIView example

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HealthAPIView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
```

### profiles/api_urls.py

```python
from django.urls import path
from . import api_views

urlpatterns = [
    path("", api_views.api_home, name="api_home"),
]
```

## 5. Explain the code

### profiles/api_views.py

1. `from rest_framework.decorators import api_view` — Imports DRF or Django components.
2. `from rest_framework.response import Response` — Imports DRF or Django components.
3. ` ` — Part of the endpoint; explain its place in the request flow.
4. `@api_view(["GET"])` — Declares allowed HTTP methods for a function-based API view.
5. `def api_home(request):` — Defines a view function or method.
6. `    return Response({` — Builds an HTTP response, optionally with a status code.
7. `        "message": "Employee API",` — Part of the endpoint; explain its place in the request flow.
8. `        "version": "v1"` — Part of the endpoint; explain its place in the request flow.
9. `    })` — Part of the endpoint; explain its place in the request flow.

### APIView example

1. `from rest_framework.views import APIView` — Imports DRF or Django components.
2. `from rest_framework.response import Response` — Imports DRF or Django components.
3. ` ` — Part of the endpoint; explain its place in the request flow.
4. `class HealthAPIView(APIView):` — Part of the endpoint; explain its place in the request flow.
5. `    def get(self, request):` — Defines a view function or method.
6. `        return Response({"status": "ok"})` — Builds an HTTP response, optionally with a status code.

### profiles/api_urls.py

1. `from django.urls import path` — Imports DRF or Django components.
2. `from . import api_views` — Imports DRF or Django components.
3. ` ` — Part of the endpoint; explain its place in the request flow.
4. `urlpatterns = [` — Part of the endpoint; explain its place in the request flow.
5. `    path("", api_views.api_home, name="api_home"),` — Part of the endpoint; explain its place in the request flow.
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

DRF supports function-based API views using @api_view and class-based API views using APIView. These abstractions provide request parsing, response rendering, authentication and permission integration. Choose a style that fits the endpoint and keep business logic understandable.

## 9. Approved mini-project — Employee REST API

**Objective:** Employee REST API.

### Required tasks

1. Create a separate api_views.py file or organize API views clearly.
2. Create a simple function-based endpoint using @api_view.
3. Return a DRF Response object.
4. Restrict allowed HTTP methods in the decorator.
5. Create a small APIView class with a get() method.
6. Connect the view through an API URL configuration.
7. Open the endpoint in a browser or Postman.
8. Compare the structure of function-based and class-based API views.

### Suggested structure

```text
projects/day_58/
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

- [ ] Endpoint returns JSON.
- [ ] Unsupported HTTP method is rejected.
- [ ] URL points to the correct API view.
- [ ] Function-based view works.
- [ ] APIView method handler works.
- [ ] The learner can explain when each style is useful.

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

**Planning prompt:** "Help me plan Employee REST API. List endpoints, HTTP methods, payloads, status codes and test cases. Do not provide the complete implementation."

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

**Q1. Explain function-based api views and apiview.**  
**Answer:** DRF supports function-based API views using @api_view and class-based API views using APIView. These abstractions provide request parsing, response rendering, authentication and permission integration. Choose a style that fits the endpoint and keep business logic understandable.

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
- [ ] Complete Employee REST API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit Postman evidence and README.

**Next lesson:** Day 59.
