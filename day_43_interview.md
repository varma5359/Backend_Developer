# Day 43: Interview Guide — Advanced Django ORM

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related class notes:** [Day 43 class notes](day_43_notes.md)  
**Approved mini-project:** Advanced Product Search

> Answer aloud first. Then compare your explanation with the model answer. Demonstrate the query in Django shell whenever possible.

## 1. Core technical questions

### Q1. What is Django ORM?

**Model answer:** Django ORM is the object-relational mapping layer that lets Python code query and update relational database records through model classes and QuerySets. Django translates ORM expressions into SQL for the configured database.

### Q2. What is a QuerySet?

**Model answer:** A QuerySet represents a database query and its potential result rows. It supports filtering, sorting and other query operations. QuerySets are lazy in most common cases, meaning Django delays database execution until results are needed.

### Q3. What is the difference between filter() and get()?

**Model answer:** filter() returns a QuerySet and can return zero, one or many records. get() returns one model instance and expects exactly one match. It raises DoesNotExist if there is no match and MultipleObjectsReturned if there is more than one.

### Q4. Explain exclude().

**Model answer:** exclude() returns a QuerySet containing records that do not match the supplied conditions. For example, Product.objects.exclude(stock=0) returns products whose stock is not zero.

### Q5. Explain order_by().

**Model answer:** order_by() sorts a QuerySet. A field name sorts ascending by default. A minus prefix requests descending order, such as order_by("-price").

### Q6. What does values() return?

**Model answer:** values() returns a QuerySet of dictionaries containing the requested fields rather than full model instances. It is useful when only a small set of columns is required.

### Q7. Explain icontains, gte, lte, in and range.

**Model answer:**
- icontains performs a case-insensitive substring search.
- gte means greater than or equal to.
- lte means less than or equal to.
- in matches any value in a supplied collection.
- range matches values between two inclusive boundaries.

### Q8. What is QuerySet laziness?

**Model answer:** Django usually delays executing a QuerySet until the results are consumed. Iteration, list conversion and several other operations evaluate it. This allows multiple filters and ordering operations to be combined before a query is sent to the database.

### Q9. What are Q objects?

**Model answer:** Q objects allow complex boolean conditions. The pipe operator combines conditions with OR, while the ampersand combines them with AND. They are useful when search requirements allow alternative matches.

Example:

~~~python
from django.db.models import Q
Product.objects.filter(
    Q(name__icontains="mouse") | Q(sku__icontains="mouse")
)
~~~

### Q10. How do you handle a missing object in a browser detail view?

**Model answer:** I use get_object_or_404() so Django returns a 404 response if the object does not exist. In shell or service code, I can catch the model's DoesNotExist exception where appropriate.

## 2. Code-reading questions

### Q11. Explain this query.

~~~python
Product.objects.filter(price__gte=500).order_by("-price")
~~~

**Model answer:** It selects products whose price is at least 500 and sorts them from highest price to lowest price. It returns a QuerySet.

### Q12. Explain this query.

~~~python
Product.objects.values("sku", "name", "price")
~~~

**Model answer:** It selects only the SKU, name and price fields and returns dictionary-like rows in a QuerySet. It does not return full Product model instances.

### Q13. What is the difference between these two expressions?

~~~python
Product.objects.filter(category="Audio")
Product.objects.get(category="Audio")
~~~

**Model answer:** The first returns all matching records as a QuerySet. The second requires exactly one record and can raise DoesNotExist or MultipleObjectsReturned.

### Q14. Why validate query-string input?

**Model answer:** Query-string values arrive as text and may be malformed. A Django form can convert decimal values, validate choices and display errors. The view should use cleaned_data rather than trusting raw request.GET values.

### Q15. Why use a sort allow-list?

**Model answer:** A browser should not be able to choose arbitrary model fields or ORM expressions. The view maps a small set of approved sort options to known field expressions.

## 3. Scenario-based questions

### Q16. A get() call raises DoesNotExist. What do you do?

**Model answer:** I verify the lookup value and confirm the record exists. If absence is an expected result, I handle the exception or use get_object_or_404() in a browser view. I do not silently assume the object exists.

### Q17. A get() call raises MultipleObjectsReturned. What does it mean?

**Model answer:** The lookup condition matched more than one row. I use filter() if multiple results are valid, or I choose a field protected by a uniqueness rule if the business requirement expects exactly one object.

### Q18. A product search crashes when min_price contains text. How do you fix it?

**Model answer:** I do not compare the raw string with a DecimalField. I define a DecimalField in a Django search form, validate request.GET and read the converted value from cleaned_data. Invalid values are displayed as form errors.

### Q19. The search page returns too many rows. How do you investigate?

**Model answer:** I inspect each filter condition, check whether the correct lookup and field are used, verify whether the conditions are combined with AND or OR, and reproduce the query with known sample data. I inspect the generated SQL if necessary.

### Q20. A developer loads every Product row and filters them in Python. What is a better approach?

**Model answer:** Apply filter(), exclude() and ordering in the ORM so the database performs the filtering. This avoids loading unnecessary rows into application memory.

## 4. Practical coding round

### Task 1 — Case-insensitive search

**Requirement:** Find products whose names contain "mouse", regardless of case.

**Expected code:**

~~~python
Product.objects.filter(name__icontains="mouse")
~~~

### Task 2 — Price interval

**Requirement:** Find products priced from 500 to 2000, including both limits.

**Expected code:**

~~~python
Product.objects.filter(price__range=(500, 2000))
~~~

### Task 3 — Alternative search fields

**Requirement:** Match the search term in either product name or SKU.

**Expected code:**

~~~python
from django.db.models import Q

Product.objects.filter(
    Q(name__icontains="mouse") | Q(sku__icontains="mouse")
)
~~~

### Task 4 — Selected fields

**Requirement:** Return only SKU, name and price.

**Expected code:**

~~~python
Product.objects.values("sku", "name", "price")
~~~

## 5. Project viva — Advanced Product Search

### Q21. What business problem does your project solve?

**Suggested answer:** It lets a customer find products using name, category and price filters, then sort the matching results and open a product detail page.

### Q22. Why did you create a separate catalog app?

**Suggested answer:** It keeps product-search responsibilities separate from the existing profiles app, which already manages Student and Employee features. It also gives Day 44 and Day 45 a shared Product model to extend.

### Q23. How did you test search correctness?

**Suggested answer:** I inserted known sample products and checked the expected matching records for text, category, price and sorting conditions. I also tested invalid numeric input and empty results.

### Q24. What did you do when no product matched?

**Suggested answer:** The search view returns an empty QuerySet. The template uses the empty branch of the for loop to display a helpful message.

### Q25. What would you improve before production?

**Suggested answer:** Add pagination, indexes based on measured query patterns, appropriate access rules for product management, stronger tests and query-performance measurement.

## 6. Self-check

- [ ] I can explain QuerySet and laziness.
- [ ] I can distinguish filter() from get().
- [ ] I can explain get() exceptions.
- [ ] I can use field lookups without guessing.
- [ ] I can combine OR conditions using Q.
- [ ] I can validate GET parameters.
- [ ] I can demonstrate Advanced Product Search without copying the notes.

**Readiness rule:** Move to Day 44 only after the search page works with known test records and you can explain the output of your ORM queries.
