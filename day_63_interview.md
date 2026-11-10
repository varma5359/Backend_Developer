# Day 63: Interview Questions — API Authentication and Permission Classes

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 63 class notes](day_63_notes.md)  
**Approved mini-project:** Protected Employee API

## Core technical questions

### Q1. Explain api authentication and permission classes.
**Answer:** Authentication identifies the API client or user. Permission classes decide whether the request is allowed to proceed. DRF supports permissions such as AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly. Authentication and permissions are separate: successful authentication does not automatically grant access.

### Q2. Which DRF classes or components are involved?
**Answer:** profiles/api_views.py, settings.py — default API permission, Custom permission example. Explain how the request is routed and handled.

### Q3. What is one common mistake?
**Answer:** Anonymous request is denied where authentication is required. Test with direct API requests, not just the frontend.

### Q4. How do you verify the implementation?
**Answer:** Test each endpoint and method, inspect status codes and compare anonymous versus authenticated users where applicable.

### Q5. What is one production concern?
**Answer:** Queryset scoping, least-privilege access, clear route design and automated permission tests.

## Scenario questions

### Q6. A user can access records they should not see. What do you inspect?
**Suggested answer:** Check queryset scoping, get_queryset(), permission classes and object-level permission checks. Authentication alone is not enough.

### Q7. Why choose a generic view or ViewSet?
**Suggested answer:** Use generic views for common patterns with focused control. Use ViewSets when grouping a resource's related actions provides a clearer API design.

## Project viva — Protected Employee API

1. Which view style did you choose?
2. Why did you choose it?
3. Which routes were generated?
4. Which permissions are required?
5. How did you test anonymous access?
6. How did you verify allowed access?
7. What would you improve?

## Rapid revision

- **1.** Explain authentication versus permission checks.
- **2.** Protect an API view with IsAuthenticated.
- **3.** Compare AllowAny, IsAuthenticated, IsAdminUser and IsAuthenticatedOrReadOnly.
- **4.** Configure a default permission class where appropriate.
- **5.** Create a custom permission based on group membership.
- **6.** Test anonymous, authenticated normal and HR users.
- **7.** Verify that the API denies direct requests without permission.
- **8.** Explain why hiding frontend buttons is not sufficient security.

## Readiness checklist
- [ ] Explain the DRF view style.
- [ ] Explain routing.
- [ ] Explain permissions.
- [ ] Demonstrate the project.
- [ ] Show direct API access tests.
