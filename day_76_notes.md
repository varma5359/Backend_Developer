# Day 76: Caching Concepts and Django Cache Framework

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate to Advanced  
**Prerequisites:** Days 27–77 — Django, ORM, APIs, background tasks and deployment concepts  
**Tools:** Python, Django, database, VS Code and terminal  
**Approved mini-project:** Cached Product Catalog API

> **Trainer guidance:** Explain what problem the feature solves and when it should be used. Measure behavior where relevant. Avoid adding caching, locking or middleware without a clear requirement.

## 1. Learning objectives

- Explain caching concepts and django cache framework.
- Identify the Django APIs and files involved.
- Implement the example step by step.
- Explain the reliability or performance implications.
- Test normal and failure cases.
- Complete Cached Product Catalog API.

## 2. Concept introduction

Caching stores the result of expensive work so repeated requests can be served faster. Django provides a cache API and multiple cache backends. Cache keys should include the data context, cached data should have a sensible timeout and updates should invalidate or refresh stale values.

## 3. File-by-file implementation

### config/settings.py — local development cache

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "product-catalog-cache",
        "TIMEOUT": 60,
    }
}
```

### profiles/services.py

```python
from django.core.cache import cache
from .models import Product

def get_active_products():
    cache_key = "catalog:active-products"
    products = cache.get(cache_key)

    if products is None:
        products = list(
            Product.objects.filter(is_active=True).values(
                "id", "name", "price"
            )
        )
        cache.set(cache_key, products, timeout=60)

    return products

def clear_product_cache():
    cache.delete("catalog:active-products")
```

### View cache decorator

```python
from django.views.decorators.cache import cache_page

@cache_page(60)
def public_catalog_page(request):
    ...
```

## 4. Explain the important statements

### config/settings.py — local development cache

1. `CACHES = {` — Part of the configuration; explain how it affects the request or database.
2. `    "default": {` — Part of the configuration; explain how it affects the request or database.
3. `        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",` — Part of the configuration; explain how it affects the request or database.
4. `        "LOCATION": "product-catalog-cache",` — Part of the configuration; explain how it affects the request or database.
5. `        "TIMEOUT": 60,` — Part of the configuration; explain how it affects the request or database.
6. `    }` — Part of the configuration; explain how it affects the request or database.
7. `}` — Part of the configuration; explain how it affects the request or database.

### profiles/services.py

1. `from django.core.cache import cache` — Imports Django or Python components.
2. `from .models import Product` — Imports Django or Python components.
3. ` ` — Part of the configuration; explain how it affects the request or database.
4. `def get_active_products():` — Defines a service function or middleware method.
5. `    cache_key = "catalog:active-products"` — Part of the configuration; explain how it affects the request or database.
6. `    products = cache.get(cache_key)` — Attempts to retrieve a cached value.
7. ` ` — Part of the configuration; explain how it affects the request or database.
8. `    if products is None:` — Part of the configuration; explain how it affects the request or database.
9. `        products = list(` — Part of the configuration; explain how it affects the request or database.
10. `            Product.objects.filter(is_active=True).values(` — Part of the configuration; explain how it affects the request or database.
11. `                "id", "name", "price"` — Part of the configuration; explain how it affects the request or database.
12. `            )` — Part of the configuration; explain how it affects the request or database.
13. `        )` — Part of the configuration; explain how it affects the request or database.
14. `        cache.set(cache_key, products, timeout=60)` — Stores a value in the cache for a period.
15. ` ` — Part of the configuration; explain how it affects the request or database.
16. `    return products` — Part of the configuration; explain how it affects the request or database.
17. ` ` — Part of the configuration; explain how it affects the request or database.
18. `def clear_product_cache():` — Defines a service function or middleware method.
19. `    cache.delete("catalog:active-products")` — Invalidates a cached value.

### View cache decorator

1. `from django.views.decorators.cache import cache_page` — Imports Django or Python components.
2. ` ` — Part of the configuration; explain how it affects the request or database.
3. `@cache_page(60)` — Part of the configuration; explain how it affects the request or database.
4. `def public_catalog_page(request):` — Defines a service function or middleware method.
5. `    ...` — Part of the configuration; explain how it affects the request or database.

## 5. Important design considerations

| Concept | Consideration |
|---|---|
| Cache key | Include the data context and avoid collisions |
| Cache timeout | Decide how long stale data may be acceptable |
| Cache invalidation | Clear or refresh cached values after writes |
| Atomic transaction | Group related writes into one commit/rollback unit |
| Row locking | Use when concurrent writes require coordination |
| Middleware order | Earlier middleware wraps later middleware |
| Logging | Record safe metadata, not secrets or request bodies |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Cache remains stale | Cache invalidation and key design |
| Cache never hits | Key mismatch or backend configuration |
| Transaction partially updates | Operations outside atomic block |
| Deadlock or lock timeout | Lock order and transaction duration |
| Middleware import error | Module path and settings registration |
| Middleware blocks request | get_response call and exception handling |
| Sensitive information in logs | Log format and fields being recorded |

## 7. Industry scenario

Caching stores the result of expensive work so repeated requests can be served faster. Django provides a cache API and multiple cache backends. Cache keys should include the data context, cached data should have a sensible timeout and updates should invalidate or refresh stale values.

## 8. Approved mini-project — Cached Product Catalog API

**Objective:** Cached Product Catalog API.

### Required tasks

1. Explain cache hit and cache miss.
2. Configure a local memory cache for development.
3. Read a value using cache.get().
4. On a miss, query the database and cache the result.
5. Set an explicit timeout.
6. Invalidate the cache after a product update.
7. Compare behavior before and after cache invalidation.
8. Explain why production may use Redis or another shared cache backend.

### Suggested structure

```text
projects/day_76/
├── README.md
├── config/
└── application/
    ├── services.py
    ├── middleware.py
    └── tests/
```

### Validation checklist

- [ ] First request populates the cache.
- [ ] Repeated request can use cached data.
- [ ] Cache has an explicit timeout.
- [ ] Product update invalidates or refreshes cached data.
- [ ] Cache key includes relevant context.
- [ ] Learner understands that cache is not the source of truth.

### Submission evidence

- Source files and configuration.
- Test output for normal and failure cases.
- Query or cache evidence where relevant.
- Safe logs showing request timing or status.
- README explaining trade-offs and limitations.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Cached Product Catalog API. Identify the components, data flow, configuration, failure cases and test plan. Do not write the complete solution."

**Guided prompt:** "Help me implement the smallest working example. Explain how to verify it and wait for my output."

**Debugging prompt:** "Here is my configuration, code and observed behavior. Explain whether the issue is key design, transaction scope or middleware order."

**Review prompt:** "Review the implementation for stale data, atomicity, concurrency, middleware order and safe logging."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Improve or coordinate backend request/data behavior.  
B. Replace Django.  
C. Disable database constraints.  
D. Remove HTTP.  
**Answer: A.** The feature addresses performance or request/data consistency.

**Q2. What should be tested after a data change?**  
A. Only the code length.  
B. Cache/database state and expected output.  
C. Only the project title.  
D. Nothing.  
**Answer: B.** Verify the resulting state.

**Q3. What does transaction.atomic() provide?**  
A. CSS styling.  
B. A new URL.  
C. Commit/rollback behavior for grouped database operations.  
D. Email delivery.  
**Answer: C.** Operations in the atomic block succeed or roll back together.

**Q4. Why does middleware order matter?**  
A. It changes the editor theme.  
B. It determines database table names.  
C. It creates Git commits.  
D. Middleware wraps request and response processing in order.  
**Answer: D.** Ordering affects how requests and responses are processed.

**Q5. What is a safe logging practice?**  
A. Log method, path, status and timing while excluding secrets.  
B. Log passwords.  
C. Log all authorization headers.  
D. Log complete private request bodies.  
**Answer: A.** Keep logs useful without exposing sensitive information.

## 11. Interview preparation

**Q1. Explain caching concepts and django cache framework.**  
**Answer:** Caching stores the result of expensive work so repeated requests can be served faster. Django provides a cache API and multiple cache backends. Cache keys should include the data context, cached data should have a sensible timeout and updates should invalidate or refresh stale values.

**Q2. What is one common failure?**  
**Answer:** First request populates the cache. Explain how to reproduce and resolve it.

**Q3. How do you verify the implementation?**  
**Answer:** Compare behavior before and after the change, inspect the database/cache/logs and test a failure case.

**Follow-up:** What is one trade-off?  
**Answer:** Caching can return stale data; transactions can hold locks; middleware adds work to every request. Choose based on measured need.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Run the required checks.
- [ ] Test failure behavior.
- [ ] Complete Cached Product Catalog API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit README and evidence.

**Next lesson:** Day 77.
