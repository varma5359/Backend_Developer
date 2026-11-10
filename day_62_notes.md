# Day 62: ViewSets and Routers

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–62 — DRF installation, serializers and API views  
**Tools:** Python, Django, DRF, VS Code, terminal and Postman  
**Approved mini-project:** Inventory Management API

> **Trainer guidance:** Compare the different DRF view styles using the same resource. Explain what code the framework provides automatically and what the developer still needs to configure.

## 1. Learning objectives

- Explain viewsets and routers.
- Identify the DRF class, mixin, router or permission involved.
- Implement the example step by step.
- Connect URL patterns to API behavior.
- Test valid and denied requests.
- Complete Inventory Management API.

## 2. Concept introduction

A ViewSet groups related resource operations into one class. ModelViewSet provides common CRUD actions when queryset and serializer_class are configured. A router automatically generates URL patterns for registered ViewSets, reducing repetitive URL declarations.

## 3. File-by-file implementation

### profiles/api_views.py

```python
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### profiles/api_urls.py

```python
from rest_framework.routers import DefaultRouter
from .api_views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")

urlpatterns = router.urls
```

## 4. Explain the important statements

### profiles/api_views.py

1. `from rest_framework.viewsets import ModelViewSet` — Imports DRF components or models.
2. `from .models import Product` — Imports DRF components or models.
3. `from .serializers import ProductSerializer` — Imports DRF components or models.
4. ` ` — Part of the API configuration; explain its effect.
5. `class ProductViewSet(ModelViewSet):` — Defines a view, ViewSet or permission class.
6. `    queryset = Product.objects.all()` — Part of the API configuration; explain its effect.
7. `    serializer_class = ProductSerializer` — Defines a view, ViewSet or permission class.

### profiles/api_urls.py

1. `from rest_framework.routers import DefaultRouter` — Imports DRF components or models.
2. `from .api_views import ProductViewSet` — Imports DRF components or models.
3. ` ` — Part of the API configuration; explain its effect.
4. `router = DefaultRouter()` — Part of the API configuration; explain its effect.
5. `router.register("products", ProductViewSet, basename="product")` — Registers a ViewSet and resource prefix with a router.
6. ` ` — Part of the API configuration; explain its effect.
7. `urlpatterns = router.urls` — Part of the API configuration; explain its effect.

## 5. Compare the DRF approaches

| Approach | Best use |
|---|---|
| Function-based API view | Small endpoint with explicit control |
| APIView | Class-based endpoint with explicit HTTP method handlers |
| Generic views | Common list/create/retrieve/update/delete patterns |
| Mixins | Reuse specific operations in custom combinations |
| ViewSet | Group related resource actions in one class |
| Router | Generate URL patterns for registered ViewSets |

More abstraction is not automatically better. Choose the clearest structure for the endpoint.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Method not allowed | View class or ViewSet actions |
| Router URL missing | Router registration and included router.urls |
| 401/403 response | Authentication and permission configuration |
| Queryset exposes too many records | get_queryset() and user scoping |
| Serializer mismatch | serializer_class and model |
| Custom permission always denies | User authentication, group name and permission method |

## 7. Industry scenario

A ViewSet groups related resource operations into one class. ModelViewSet provides common CRUD actions when queryset and serializer_class are configured. A router automatically generates URL patterns for registered ViewSets, reducing repetitive URL declarations.

## 8. Approved mini-project — Inventory Management API

**Objective:** Inventory Management API.

### Required tasks

1. Create a ModelViewSet for Product.
2. Set queryset and serializer_class.
3. Create a DefaultRouter.
4. Register the ViewSet with a resource prefix and basename.
5. Connect router.urls to the project or app URL configuration.
6. Inspect generated routes.
7. Test list, create, retrieve, update, partial_update and destroy actions.
8. Explain how a ViewSet differs from separate generic views.

### Suggested structure

```text
projects/day_62/
├── README.md
├── config/
└── profiles/
    ├── api_views.py
    ├── api_urls.py
    ├── serializers.py
    ├── permissions.py
    └── tests/
```

### Validation checklist

- [ ] Router generates the collection route.
- [ ] Router generates the detail route.
- [ ] CRUD actions work.
- [ ] Serializer validation is applied.
- [ ] The route names are understood.
- [ ] The learner can explain when a ViewSet is suitable.

### Postman evidence

- Successful list and detail request.
- Successful create/update request where applicable.
- Invalid request response.
- Anonymous request response.
- Authenticated user response.
- Custom permission test if applicable.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Inventory Management API. Compare the suitable DRF view styles, list routes, permissions and test cases. Do not generate the entire API."

**Guided prompt:** "Help me implement one view or permission class at a time. Explain what DRF provides automatically."

**Debugging prompt:** "Here is my view, URL configuration and status code. Trace the routing, authentication and permission flow."

**Review prompt:** "Review the API for overbroad querysets, missing permissions, duplicated code and incorrect route behavior."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Reuse common API operations or enforce access rules.  
B. Replace JSON.  
C. Disable URL routing.  
D. Remove serializers.  
**Answer: A.** DRF abstractions reduce repeated code or enforce permissions.

**Q2. What does a router do with a ViewSet?**  
A. Creates a database.  
B. Generates URL patterns for registered actions.  
C. Hashes passwords.  
D. Installs Django.  
**Answer: B.** Routers connect ViewSets to URL patterns.

**Q3. What is the purpose of IsAuthenticated?**  
A. Allow anonymous requests.  
B. Sort the queryset.  
C. Require an authenticated user.  
D. Delete a record.  
**Answer: C.** IsAuthenticated denies anonymous requests.

**Q4. Does authentication automatically grant every permission?**  
A. Yes.  
B. Only on GET.  
C. Only in Postman.  
D. No. Permission checks are separate.  
**Answer: D.** Authentication and authorization are separate.

**Q5. What is the strongest evidence of a protected API?**  
A. Anonymous and permitted user requests return the expected different results.  
B. A button is hidden in HTML.  
C. The route is not documented.  
D. The API returns 200 for every request.  
**Answer: A.** Test access directly at the API.

## 11. Interview preparation

**Q1. Explain viewsets and routers.**  
**Answer:** A ViewSet groups related resource operations into one class. ModelViewSet provides common CRUD actions when queryset and serializer_class are configured. A router automatically generates URL patterns for registered ViewSets, reducing repetitive URL declarations.

**Q2. What is the difference between generic views and ViewSets?**  
**Answer:** Generic views represent common API patterns through individual view classes. ViewSets group related resource actions, often with router-generated URLs.

**Q3. Why are permission classes needed?**  
**Answer:** They enforce access rules on the server for every request.

**Follow-up:** Why is frontend-only permission hiding unsafe?  
**Answer:** A client can call the API URL directly, so the server must enforce permissions.

## 12. Completion checklist

- [ ] Explain the DRF approach.
- [ ] Implement and connect the view.
- [ ] Test the routes.
- [ ] Verify permissions.
- [ ] Complete Inventory Management API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit code, README and Postman evidence.

**Next lesson:** Day 63.
