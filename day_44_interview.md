# Day 44: Interview Guide — Django ORM Query Optimization

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Related notes:** [Day 44 class notes](day_44_notes.md)  
**Approved mini-project:** Optimized Order Management System

## 1. Core technical questions

### Q1. What is the N+1 query problem?

**Model answer:** It happens when an application executes one query to retrieve a list and then executes another query for each row to retrieve related data. For example, retrieving 20 orders and then querying order items for every order can produce many unnecessary queries.

### Q2. What does select_related() do?

**Model answer:** select_related() uses SQL JOINs to retrieve related objects for single-valued relationships such as ForeignKey and OneToOneField. It is useful when code will access those related objects for each row.

### Q3. What does prefetch_related() do?

**Model answer:** prefetch_related() performs additional queries for related collections and joins the results in Python. It is useful for ManyToManyField and reverse ForeignKey relationships.

### Q4. What is the main difference between select_related() and prefetch_related()?

**Model answer:** select_related() follows single-valued relationships using SQL joins in one query. prefetch_related() loads multi-valued relationships using separate queries and associates the results in Python.

### Q5. What is related_name?

**Model answer:** related_name defines the reverse accessor used to reach related objects. In the lesson, OrderItem.order has related_name="items", so an Order instance can access its items with order.items.all().

### Q6. Why is unit_price stored on OrderItem?

**Model answer:** Product prices can change. An order should retain the price that applied when the customer placed it. The order item stores a historical price snapshot rather than relying on the current Product.price.

### Q7. How do you measure query count?

**Model answer:** In development, I can inspect connection.queries when DEBUG is enabled. In automated tests, I can use Django's assertNumQueries() to verify the number of queries executed by a code block.

### Q8. Why should optimization be measured?

**Model answer:** An optimization should solve an observed performance issue. Adding ORM methods without measuring can add complexity without benefit. I compare query counts and ensure the returned data remains correct.

## 2. Code-reading questions

### Q9. Explain this query.

~~~python
OrderItem.objects.select_related("order", "product")
~~~

**Model answer:** It retrieves OrderItem rows and joins each row's single related Order and Product. Accessing item.order and item.product should not require separate queries for each item.

### Q10. Explain this query.

~~~python
Order.objects.prefetch_related("items__product")
~~~

**Model answer:** It retrieves orders, then prefetches their related items and each item's product. The lookup path uses the related_name "items" from Order to OrderItem and then follows the product ForeignKey.

### Q11. Why does this use prefetch_related()?

~~~python
orders = Order.objects.prefetch_related("items")
for order in orders:
    for item in order.items.all():
        print(item.quantity)
~~~

**Model answer:** An order can have multiple items. This is a collection, so prefetch_related() is appropriate. It avoids querying the item collection separately for every order.

### Q12. What does assertNumQueries(2) mean?

**Model answer:** It asserts that the code inside the test context executes exactly two database queries. It helps prevent accidental query-count regressions, although the expected count depends on the query and test setup.

## 3. Scenario-based questions

### Q13. An order list page is slow when there are many orders. How do you investigate?

**Model answer:**
1. Reproduce the page with a realistic number of orders.
2. Identify related objects accessed by the template.
3. Measure database query count.
4. Determine which relations are single-valued and which are collections.
5. Apply select_related() or prefetch_related() as appropriate.
6. Measure again.
7. Confirm the rendered order data is unchanged.

### Q14. A developer uses select_related("items") where items is a reverse ForeignKey. What is wrong?

**Model answer:** A reverse ForeignKey represents a collection, not one object. select_related() is for single-valued relationships. Use prefetch_related("items").

### Q15. Query count decreases, but some product names are missing. Is the optimization successful?

**Model answer:** No. Performance does not override correctness. I compare the optimized result with the original expected result, inspect the prefetch path and verify that the template accesses the correct related_name and fields.

### Q16. Why might connection.queries be empty?

**Model answer:** Query logging depends on DEBUG and database connection configuration. In production, DEBUG should remain disabled. For automated measurement, use assertNumQueries() in Django tests.

## 4. Practical coding round

### Task 1 — Load order and product with each item

**Expected code:**

~~~python
OrderItem.objects.select_related("order", "product")
~~~

### Task 2 — Load each order's items

**Expected code:**

~~~python
Order.objects.prefetch_related("items")
~~~

### Task 3 — Load orders, items and products

**Expected code:**

~~~python
Order.objects.prefetch_related("items__product")
~~~

### Task 4 — Combine prefetch with a customized item queryset

**Expected code:**

~~~python
from django.db.models import Prefetch

item_queryset = OrderItem.objects.select_related("product")
orders = Order.objects.prefetch_related(
    Prefetch("items", queryset=item_queryset)
)
~~~

## 5. Project viva — Optimized Order Management System

### Q17. What business problem does the project solve?

**Suggested answer:** It displays orders, customers, products and quantities in an order management page while avoiding unnecessary database queries for related data.

### Q18. Which relationships did you create?

**Suggested answer:** One Order has many OrderItems. Each OrderItem refers to one Product. OrderItem.order uses a ForeignKey with related_name="items"; OrderItem.product uses a ForeignKey with related_name="order_items".

### Q19. How did you prove optimization?

**Suggested answer:** I measured query counts for the naive nested access and the optimized prefetch query. I compared the results and verified that the same order and product information was displayed.

### Q20. What would you improve for a production system?

**Suggested answer:** I would profile real workloads, add pagination, inspect indexes, test transaction behavior and apply object-level access control. I would not add optimization blindly.

## 6. Self-check

- [ ] I can explain N+1 queries.
- [ ] I can identify single-valued relationships.
- [ ] I can identify multi-valued relationships.
- [ ] I can choose select_related() or prefetch_related().
- [ ] I can measure query count.
- [ ] I can demonstrate that output remains correct.

**Readiness rule:** Move to Day 45 after you can explain and demonstrate the query-count comparison in your own project.
