# Day 66: API Filtering, Searching, Ordering and Pagination

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–65 — DRF serializers, views, routers and permissions  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** Product Search and Filtering API

> **Security reminder:** Use test accounts and fake tokens. Never paste real API tokens, JWTs, passwords or session cookies into a public repository or screenshot.

## 1. Learning objectives

- Explain api filtering, searching, ordering and pagination.
- Configure the relevant DRF component.
- Implement the example step by step.
- Test valid and invalid requests.
- Explain security, privacy and API behavior.
- Complete Product Search and Filtering API.

## 2. Concept introduction

DRF filter backends let clients narrow, search, sort and paginate API results using query parameters. django-filter provides structured field filtering. SearchFilter supports search fields, OrderingFilter controls sort order and pagination classes limit the number of results returned in one response.

## 3. File-by-file implementation

### settings.py — DRF defaults

```python
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
```

### profiles/api_views.py

```python
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["category", "is_active"]
    search_fields = ["name", "sku", "description"]
    ordering_fields = ["name", "price", "created_at"]
    ordering = ["name"]
```

## 4. Explain the important statements

### settings.py — DRF defaults

1. `REST_FRAMEWORK = {` — Part of the API configuration; explain its effect on the request.
2. `    "DEFAULT_FILTER_BACKENDS": [` — Configures query filtering backends.
3. `        "django_filters.rest_framework.DjangoFilterBackend",` — Part of the API configuration; explain its effect on the request.
4. `        "rest_framework.filters.SearchFilter",` — Part of the API configuration; explain its effect on the request.
5. `        "rest_framework.filters.OrderingFilter",` — Part of the API configuration; explain its effect on the request.
6. `    ],` — Part of the API configuration; explain its effect on the request.
7. `    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",` — Part of the API configuration; explain its effect on the request.
8. `    "PAGE_SIZE": 10,` — Part of the API configuration; explain its effect on the request.
9. `}` — Part of the API configuration; explain its effect on the request.

### profiles/api_views.py

1. `from rest_framework.viewsets import ReadOnlyModelViewSet` — Imports DRF, Django or model components.
2. `from .models import Product` — Imports DRF, Django or model components.
3. `from .serializers import ProductSerializer` — Imports DRF, Django or model components.
4. ` ` — Part of the API configuration; explain its effect on the request.
5. `class ProductViewSet(ReadOnlyModelViewSet):` — Defines an authentication, permission or API view class.
6. `    queryset = Product.objects.all()` — Part of the API configuration; explain its effect on the request.
7. `    serializer_class = ProductSerializer` — Defines an authentication, permission or API view class.
8. `    filterset_fields = ["category", "is_active"]` — Part of the API configuration; explain its effect on the request.
9. `    search_fields = ["name", "sku", "description"]` — Defines which fields are searchable.
10. `    ordering_fields = ["name", "price", "created_at"]` — Defines the allowed ordering fields.
11. `    ordering = ["name"]` — Part of the API configuration; explain its effect on the request.

## 5. Important distinctions

| Concept | Meaning |
|---|---|
| Authentication | Establishes who is making the request |
| Token | Credential sent by the client to authenticate |
| JWT | Signed token format with claims and expiry |
| Role | User grouping that represents a set of responsibilities |
| Model permission | Permission for an action on a model |
| Object permission | Permission decision for a specific object |
| Filtering | Restricts records using structured conditions |
| Searching | Matches text across configured fields |
| Ordering | Sorts results |
| Pagination | Splits results into pages |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| 401 Unauthorized | Authentication class and Authorization header |
| 403 Forbidden | Permission class, user role and object ownership |
| User sees too many records | get_queryset() scoping |
| Search returns unexpected values | search_fields and query parameter |
| Ordering rejected | ordering_fields allowlist |
| Pagination missing | DEFAULT_PAGINATION_CLASS and page size |
| Token leaked | Revoke/rotate token and remove secret from future exposure |

## 7. Industry scenario

DRF filter backends let clients narrow, search, sort and paginate API results using query parameters. django-filter provides structured field filtering. SearchFilter supports search fields, OrderingFilter controls sort order and pagination classes limit the number of results returned in one response.

## 8. Approved mini-project — Product Search and Filtering API

**Objective:** Product Search and Filtering API.

### Required tasks

1. Install django-filter into the active environment.
2. Add django_filters to INSTALLED_APPS.
3. Configure DjangoFilterBackend, SearchFilter and OrderingFilter.
4. Set filterset_fields for exact field filters.
5. Set search_fields for text search.
6. Set ordering_fields to an explicit allowlist.
7. Configure page-number pagination and a page size.
8. Test filtering, search, ordering and page navigation.
9. Check that invalid or unsupported ordering fields are not accepted.

### Suggested structure

```text
projects/day_66/
├── README.md
├── config/
└── application/
    ├── permissions.py
    ├── api_views.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] Exact field filtering works.
- [ ] Search checks the intended fields.
- [ ] Ordering uses only allowed fields.
- [ ] Pagination returns page metadata and results.
- [ ] Search/filter parameters are preserved where needed.
- [ ] Large result sets are not returned without pagination.

### Postman test matrix

| Request | Expected result |
|---|---|
| Missing/invalid credentials | 401 or configured authentication error |
| Authenticated but no permission | 403 |
| Authorized user | 200/201 as appropriate |
| Search/filter query | Only matching results |
| Unsupported order field | Rejected or ignored according to configuration |
| Page navigation | Correct page metadata and result count |

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Product Search and Filtering API. Identify authentication, permission, filtering and test cases. Do not provide real credentials or tokens."

**Guided prompt:** "Guide me through one configuration or permission step. Explain the security effect and wait for my test result."

**Debugging prompt:** "Here is the request method, URL, headers without secrets, response status and relevant code. Diagnose the authentication or permission issue."

**Review prompt:** "Review the API for token handling, queryset scoping, object-level permissions and safe filtering/order fields."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Secure API access or control which records are returned.  
B. Replace Django.  
C. Disable HTTP.  
D. Store tokens in source code.  
**Answer: A.** These features control identity, access and API result size.

**Q2. What should never be committed?**  
A. Public serializer code.  
B. Real access tokens or JWTs.  
C. A test fixture with fake data.  
D. A README.  
**Answer: B.** Tokens are credentials and must be protected.

**Q3. What is object-level permission?**  
A. Sorting all records.  
B. Installing DRF.  
C. Deciding whether a user can access a specific record.  
D. Changing a template.  
**Answer: C.** It evaluates access for an individual object.

**Q4. Why use pagination?**  
A. To return every record at once.  
B. To disable search.  
C. To remove filters.  
D. To limit result size and support page navigation.  
**Answer: D.** Pagination improves usability and resource control.

**Q5. Why explicitly configure ordering_fields?**  
A. To allow only intended sort fields.  
B. To expose every model field.  
C. To remove authentication.  
D. To change database schema.  
**Answer: A.** An allowlist gives predictable API behavior.

## 11. Interview preparation

**Q1. Explain api filtering, searching, ordering and pagination.**  
**Answer:** DRF filter backends let clients narrow, search, sort and paginate API results using query parameters. django-filter provides structured field filtering. SearchFilter supports search fields, OrderingFilter controls sort order and pagination classes limit the number of results returned in one response.

**Q2. What is one security risk?**  
**Answer:** Explain the risk of leaked tokens, overbroad querysets or missing object-level permissions.

**Q3. How do you verify the implementation?**  
**Answer:** Use test accounts and requests with valid, missing and invalid credentials. Test own and other users' records and verify filter/search/order/page results.

**Follow-up:** Why is queryset scoping important even when object permissions exist?  
**Answer:** Queryset scoping limits which records can be listed or retrieved and reduces the chance of exposing unauthorized objects.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Configure the relevant DRF components.
- [ ] Test valid and invalid requests.
- [ ] Verify access and result boundaries.
- [ ] Complete Product Search and Filtering API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 67.
