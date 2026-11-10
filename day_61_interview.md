# Day 61: Interview Questions — Generic Views and Mixins

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Related notes:** [Day 61 class notes](day_61_notes.md)  
**Approved mini-project:** Generic Product Management API

## Core technical questions

### Q1. Explain generic views and mixins.
**Answer:** DRF generic views combine common API behavior such as listing, creating, retrieving, updating and deleting. Mixins provide reusable operation methods, while generic view classes combine the mixins with APIView behavior. They reduce repetitive code while allowing developers to customize queryset, serializer and permissions.

### Q2. Which DRF classes or components are involved?
**Answer:** profiles/api_views.py, profiles/api_urls.py. Explain how the request is routed and handled.

### Q3. What is one common mistake?
**Answer:** Collection endpoint lists products. Test with direct API requests, not just the frontend.

### Q4. How do you verify the implementation?
**Answer:** Test each endpoint and method, inspect status codes and compare anonymous versus authenticated users where applicable.

### Q5. What is one production concern?
**Answer:** Queryset scoping, least-privilege access, clear route design and automated permission tests.

## Scenario questions

### Q6. A user can access records they should not see. What do you inspect?
**Suggested answer:** Check queryset scoping, get_queryset(), permission classes and object-level permission checks. Authentication alone is not enough.

### Q7. Why choose a generic view or ViewSet?
**Suggested answer:** Use generic views for common patterns with focused control. Use ViewSets when grouping a resource's related actions provides a clearer API design.

## Project viva — Generic Product Management API

1. Which view style did you choose?
2. Why did you choose it?
3. Which routes were generated?
4. Which permissions are required?
5. How did you test anonymous access?
6. How did you verify allowed access?
7. What would you improve?

## Rapid revision

- **1.** Identify repeated list/create/retrieve/update/delete view behavior.
- **2.** Create a ListCreateAPIView for product collection operations.
- **3.** Create a RetrieveUpdateDestroyAPIView for one product.
- **4.** Set queryset and serializer_class.
- **5.** Connect each class using as_view() in URL patterns.
- **6.** Test GET and POST on the collection route.
- **7.** Test GET, PUT, PATCH and DELETE on the detail route.
- **8.** Explain when overriding get_queryset() or perform_create() is useful.

## Readiness checklist
- [ ] Explain the DRF view style.
- [ ] Explain routing.
- [ ] Explain permissions.
- [ ] Demonstrate the project.
- [ ] Show direct API access tests.
