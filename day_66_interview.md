# Day 66: Interview Questions — API Filtering, Searching, Ordering and Pagination

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 66 class notes](day_66_notes.md)  
**Approved mini-project:** Product Search and Filtering API

## Core technical questions

### Q1. Explain api filtering, searching, ordering and pagination.
**Answer:** DRF filter backends let clients narrow, search, sort and paginate API results using query parameters. django-filter provides structured field filtering. SearchFilter supports search fields, OrderingFilter controls sort order and pagination classes limit the number of results returned in one response.

### Q2. Which DRF classes or settings are involved?
**Answer:** settings.py — DRF defaults, profiles/api_views.py. Explain how the configuration affects incoming requests.

### Q3. What is one common security mistake?
**Answer:** Exposing tokens, failing to scope querysets or relying only on frontend access controls. Explain the specific risk.

### Q4. How do you verify the implementation?
**Answer:** Test with local accounts and safe test tokens, then exercise valid, invalid and unauthorized requests. Inspect status codes and result records.

### Q5. What should not be included in a public repository?
**Answer:** Passwords, API tokens, JWTs, session cookies, private keys and real personal data.

## Scenario questions

### Q6. A user can retrieve another user's record. What do you inspect?
**Suggested answer:** Queryset scoping, object-level permission checks and ownership relationships. Test direct API requests as different users.

### Q7. An API returns too many records. What do you add?
**Suggested answer:** Appropriate filters and pagination, with explicit searchable and orderable fields.

## Project viva — Product Search and Filtering API

1. What is the purpose?
2. Which authentication/permission/filter components are used?
3. How are credentials supplied?
4. How are unauthorized requests handled?
5. How are result sets restricted?
6. How did you test the behavior?
7. What would you improve?

## Rapid revision

- **1.** Install django-filter into the active environment.
- **2.** Add django_filters to INSTALLED_APPS.
- **3.** Configure DjangoFilterBackend, SearchFilter and OrderingFilter.
- **4.** Set filterset_fields for exact field filters.
- **5.** Set search_fields for text search.
- **6.** Set ordering_fields to an explicit allowlist.
- **7.** Configure page-number pagination and a page size.
- **8.** Test filtering, search, ordering and page navigation.
- **9.** Check that invalid or unsupported ordering fields are not accepted.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the configuration.
- [ ] Demonstrate valid and invalid requests.
- [ ] Explain the security boundary.
- [ ] Present Product Search and Filtering API with safe evidence.
