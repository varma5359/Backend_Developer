# Day 62: Interview Questions — ViewSets and Routers

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 62 class notes](day_62_notes.md)  
**Approved mini-project:** Inventory Management API

## Core technical questions

### Q1. Explain viewsets and routers.
**Answer:** A ViewSet groups related resource operations into one class. ModelViewSet provides common CRUD actions when queryset and serializer_class are configured. A router automatically generates URL patterns for registered ViewSets, reducing repetitive URL declarations.

### Q2. Which DRF classes or components are involved?
**Answer:** profiles/api_views.py, profiles/api_urls.py. Explain how the request is routed and handled.

### Q3. What is one common mistake?
**Answer:** Router generates the collection route. Test with direct API requests, not just the frontend.

### Q4. How do you verify the implementation?
**Answer:** Test each endpoint and method, inspect status codes and compare anonymous versus authenticated users where applicable.

### Q5. What is one production concern?
**Answer:** Queryset scoping, least-privilege access, clear route design and automated permission tests.

## Scenario questions

### Q6. A user can access records they should not see. What do you inspect?
**Suggested answer:** Check queryset scoping, get_queryset(), permission classes and object-level permission checks. Authentication alone is not enough.

### Q7. Why choose a generic view or ViewSet?
**Suggested answer:** Use generic views for common patterns with focused control. Use ViewSets when grouping a resource's related actions provides a clearer API design.

## Project viva — Inventory Management API

1. Which view style did you choose?
2. Why did you choose it?
3. Which routes were generated?
4. Which permissions are required?
5. How did you test anonymous access?
6. How did you verify allowed access?
7. What would you improve?

## Rapid revision

- **1.** Create a ModelViewSet for Product.
- **2.** Set queryset and serializer_class.
- **3.** Create a DefaultRouter.
- **4.** Register the ViewSet with a resource prefix and basename.
- **5.** Connect router.urls to the project or app URL configuration.
- **6.** Inspect generated routes.
- **7.** Test list, create, retrieve, update, partial_update and destroy actions.
- **8.** Explain how a ViewSet differs from separate generic views.

## Readiness checklist
- [ ] Explain the DRF view style.
- [ ] Explain routing.
- [ ] Explain permissions.
- [ ] Demonstrate the project.
- [ ] Show direct API access tests.
