# Day 44: Django ORM Query Optimization — select_related() and prefetch_related()

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Duration:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–43 — Django models, migrations, relationships, QuerySets and Advanced Product Search  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment and the same Django project  
**Approved mini-project:** Optimized Order Management System

> **Self-learning method:** Today you will create an orders app that reuses the Product model from Day 43. You will first reproduce an N+1 query problem, measure it, optimize it and measure again. Never claim a query is faster just because the code looks shorter.

---

## 1. What you will build

An online store needs an order management page. Each order belongs to a customer and contains one or more order items. Each item refers to a Product.

The page must display:

- Order number and customer.
- Order date.
- Product names in each order.
- Quantity and unit price.
- Calculated line totals.

A naive page can make repeated database queries when it accesses related objects. You will learn to avoid unnecessary queries.

### Relationship diagram

~~~text
Order
  |
  | one Order has many OrderItems
  v
OrderItem
  |
  | each OrderItem refers to one Product
  v
Product (catalog app from Day 43)
~~~

### Learning outcomes

By the end, you can:
1. Explain the N+1 query problem.
2. Identify single-valued and multi-valued model relationships.
3. Use select_related() for ForeignKey and OneToOneField.
4. Use prefetch_related() for ManyToManyField and reverse relationships.
5. Measure query counts with assertNumQueries().
6. Compare results before and after optimization.
7. Explain why optimization must preserve output and business behavior.

## 2. Check your Day 43 work

Open the project folder containing manage.py. Confirm that the catalog app and Product model from Day 43 exist.

~~~powershell
python manage.py check
python manage.py showmigrations
~~~

Expected: no system-check errors. The catalog migration should be applied.

If you skipped Day 43, complete its Product model and migration first. Day 44 depends on it.

## 3. Understand the N+1 query problem

Imagine the order page displays 10 orders. For each order, the template accesses its order items, and for each item it accesses the product name.

A naive implementation may execute:
- 1 query to retrieve the orders.
- 10 queries to retrieve each order's items.
- 30 more queries to retrieve products for 30 items.

That can become 41 database queries for one page. The exact number depends on relationships, caching and how the code is written. This pattern is called the N+1 query problem: one initial query plus repeated queries for related data.

### 3.1 What is a database query?

A database query is a request to retrieve or change data. Django ORM creates SQL queries for you. You can measure the number of queries executed while a page or code block runs.

### 3.2 Relationship types determine the tool

| Relationship | Example | Typical optimization |
|---|---|---|
| ForeignKey | OrderItem → Product | select_related("product") |
| OneToOneField | User → Profile | select_related("profile") |
| ManyToManyField | Student ↔ Course | prefetch_related("courses") |
| Reverse ForeignKey | Order → OrderItems | prefetch_related("items") |

**Rule of thumb:** select_related() follows single-valued relationships using SQL JOINs. prefetch_related() loads related collections with additional queries and joins the results in Python.

## 4. Create the orders app

Run from the folder containing manage.py:

~~~powershell
python manage.py startapp orders
~~~

Register it in config/settings.py. Preserve all existing applications:

~~~python
INSTALLED_APPS = [
    # Keep existing Django applications.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Existing Phase 3 app and Day 43 app.
    "profiles",
    "catalog",

    # Day 44 app.
    "orders",
]
~~~

If your file uses AppConfig paths, retain the existing style. Add the orders AppConfig rather than replacing other entries.

## 5. Create the order models

Open orders/models.py:

~~~python
from django.db import models
from catalog.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="order_items",
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.order_number} - {self.product.name}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price
~~~

### 5.1 Explain the Order model

- order_number is a unique business identifier.
- customer_name stores the customer display name for this learning example.
- created_at is set automatically when an order is created.
- __str__() gives the object a readable representation.

### 5.2 Explain the OrderItem model

- order is a ForeignKey to Order: one order can have many items.
- on_delete=models.CASCADE means deleting an order deletes its order items.
- related_name="items" lets you access the items using order.items.
- product is a ForeignKey to Product.
- on_delete=models.PROTECT prevents deleting a product that is referenced by an order item.
- related_name="order_items" allows product.order_items to retrieve related order items.
- quantity is a positive integer field.
- unit_price stores the price captured for this order line.
- line_total is a Python property, not a database field. It multiplies quantity by unit_price.

**Why store unit_price on OrderItem?** Product prices can change later. An old order should retain the price agreed when that order was placed. This example stores a snapshot of the unit price.

## 6. Create and apply migrations

~~~powershell
python manage.py makemigrations orders
python manage.py migrate
python manage.py check
~~~

Expected: Django creates the orders tables and reports no system-check errors.

If Django says it cannot import Product, confirm:
- catalog is in INSTALLED_APPS.
- catalog/models.py defines Product.
- the import is exactly from catalog.models import Product.

## 7. Create known sample orders

Open shell:

~~~powershell
python manage.py shell
~~~

Run this repeatable seed example. It checks whether the order already exists before creating it:

~~~python
from decimal import Decimal
from catalog.models import Product
from orders.models import Order, OrderItem

keyboard = Product.objects.get(sku="KB-101")
mouse = Product.objects.get(sku="MS-102")
monitor = Product.objects.get(sku="MN-103")

order, created = Order.objects.get_or_create(
    order_number="ORD-1001",
    defaults={"customer_name": "Asha Rao"},
)

if created:
    OrderItem.objects.create(
        order=order,
        product=keyboard,
        quantity=1,
        unit_price=Decimal("799.00"),
    )
    OrderItem.objects.create(
        order=order,
        product=mouse,
        quantity=2,
        unit_price=Decimal("499.00"),
    )

order, created = Order.objects.get_or_create(
    order_number="ORD-1002",
    defaults={"customer_name": "Ravi Kumar"},
)

if created:
    OrderItem.objects.create(
        order=order,
        product=monitor,
        quantity=1,
        unit_price=Decimal("8500.00"),
    )
~~~

Inspect:

~~~python
Order.objects.count()
OrderItem.objects.count()
~~~

Expected on a fresh database: 2 orders and 3 order items.

Exit the shell with exit().

## 8. Understand the naive query

Create a basic order list query:

~~~python
orders = Order.objects.all()

for order in orders:
    print(order.order_number)
    for item in order.items.all():
        print(item.product.name, item.quantity)
~~~

This code is logically correct. The problem is how many queries may be executed.

- The first query retrieves orders.
- Accessing order.items.all() can execute another query for each order.
- Accessing item.product can execute another query for each item unless the product is already loaded.

This is a performance problem, not a correctness problem. The displayed values can be correct while the database workload is wasteful.

## 9. Optimize single-valued relationships with select_related()

Use select_related() when following ForeignKey or OneToOneField from the current model to one related object.

Example:

~~~python
items = OrderItem.objects.select_related("order", "product")

for item in items:
    print(
        item.order.order_number,
        item.product.name,
        item.quantity,
    )
~~~

Django uses SQL joins to retrieve OrderItem, Order and Product in one query for this example.

### 9.1 Understand each part

- OrderItem.objects starts a QuerySet from the OrderItem model.
- select_related("order", "product") asks Django to join the two single-valued relations.
- Iterating through items evaluates the QuerySet.
- item.order and item.product use related objects already loaded by the query.

### 9.2 When is select_related appropriate?

Use it for:
- ForeignKey.
- OneToOneField.

Do not use it for a many-to-many collection or reverse ForeignKey collection. Those can contain multiple related rows.

## 10. Optimize collections with prefetch_related()

Use prefetch_related() when retrieving a collection of related objects.

~~~python
orders = Order.objects.prefetch_related("items")

for order in orders:
    print(order.order_number)
    for item in order.items.all():
        print(item.quantity)
~~~

Django executes a query for orders and another query for the related items, then matches the objects in Python.

### 10.1 Prefetch products for the items too

~~~python
orders = Order.objects.prefetch_related("items__product")

for order in orders:
    for item in order.items.all():
        print(order.order_number, item.product.name)
~~~

The lookup path is:
- items: the reverse relation from Order to OrderItem.
- items__product: the Product related to each OrderItem.

### 10.2 Combine prefetch_related() and select_related()

You can use both when a page needs collections and single-valued relations:

~~~python
from django.db.models import Prefetch
from orders.models import Order, OrderItem

item_queryset = OrderItem.objects.select_related("product")

orders = Order.objects.prefetch_related(
    Prefetch("items", queryset=item_queryset)
)
~~~

This means:
1. Retrieve the Order records.
2. Retrieve related OrderItems using a queryset that joins Product.
3. Attach the loaded items to their orders.

Use this when you need the item collection and each item's product details.

## 11. Create an order summary view

Open orders/views.py:

~~~python
from django.shortcuts import get_object_or_404, render

from .models import Order, OrderItem


def order_list(request):
    orders = (
        Order.objects
        .prefetch_related("items__product")
        .order_by("-created_at")
    )
    return render(
        request,
        "orders/order_list.html",
        {"orders": orders},
    )


def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.prefetch_related("items__product"),
        pk=pk,
    )
    return render(
        request,
        "orders/order_detail.html",
        {"order": order},
    )


def order_item_report(request):
    items = OrderItem.objects.select_related("order", "product")
    return render(
        request,
        "orders/order_item_report.html",
        {"items": items},
    )
~~~

### 11.1 Explain the view

- order_list retrieves orders and prefetches their items and products.
- order_by("-created_at") sorts newest orders first.
- order_detail retrieves one order or returns 404.
- order_item_report starts from OrderItem and joins its single-valued order and product relations.
- render() sends the QuerySet or object to the selected template.

## 12. Create URLs

Create orders/urls.py:

~~~python
from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path("order-items/", views.order_item_report, name="order_item_report"),
]
~~~

Add this to config/urls.py, preserving all existing routes:

~~~python
path("", include("orders.urls")),
~~~

The root URL configuration should include admin, profiles, catalog and orders.

## 13. Create templates

Create:

~~~text
orders/
└── templates/
    └── orders/
        ├── order_list.html
        ├── order_detail.html
        └── order_item_report.html
~~~

### 13.1 order_list.html

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Order Management</title>
</head>
<body>
    <h1>Order Management</h1>

    {% for order in orders %}
        <section>
            <h2>
                <a href="{% url 'order_detail' order.pk %}">
                    {{ order.order_number }}
                </a>
            </h2>
            <p>Customer: {{ order.customer_name }}</p>
            <p>Created: {{ order.created_at }}</p>

            <ul>
                {% for item in order.items.all %}
                    <li>
                        {{ item.product.name }} —
                        Quantity: {{ item.quantity }} —
                        Unit price: {{ item.unit_price }} —
                        Line total: {{ item.line_total }}
                    </li>
                {% empty %}
                    <li>This order has no items.</li>
                {% endfor %}
            </ul>
        </section>
    {% empty %}
        <p>No orders found.</p>
    {% endfor %}
</body>
</html>
~~~

### 13.2 order_detail.html

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ order.order_number }}</title>
</head>
<body>
    <h1>Order {{ order.order_number }}</h1>
    <p>Customer: {{ order.customer_name }}</p>

    <h2>Items</h2>
    <ul>
        {% for item in order.items.all %}
            <li>
                {{ item.product.name }} |
                {{ item.quantity }} x {{ item.unit_price }} =
                {{ item.line_total }}
            </li>
        {% empty %}
            <li>No items in this order.</li>
        {% endfor %}
    </ul>

    <a href="{% url 'order_list' %}">Back to orders</a>
</body>
</html>
~~~

### 13.3 order_item_report.html

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Order Item Report</title>
</head>
<body>
    <h1>Order Item Report</h1>

    <table border="1" cellpadding="8">
        <thead>
            <tr>
                <th>Order</th>
                <th>Customer</th>
                <th>Product</th>
                <th>Quantity</th>
                <th>Unit price</th>
                <th>Line total</th>
            </tr>
        </thead>
        <tbody>
            {% for item in items %}
                <tr>
                    <td>{{ item.order.order_number }}</td>
                    <td>{{ item.order.customer_name }}</td>
                    <td>{{ item.product.name }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ item.unit_price }}</td>
                    <td>{{ item.line_total }}</td>
                </tr>
            {% empty %}
                <tr><td colspan="6">No order items found.</td></tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
~~~

## 14. Measure queries — do not guess

### 14.1 Compare querysets in Django shell

~~~python
from django.db import connection, reset_queries
from orders.models import Order

reset_queries()

orders = Order.objects.all()
for order in orders:
    for item in order.items.all():
        print(item.product.name)

print("Queries:", len(connection.queries))
~~~

Now compare:

~~~python
reset_queries()

orders = Order.objects.prefetch_related("items__product")
for order in orders:
    for item in order.items.all():
        print(item.product.name)

print("Queries:", len(connection.queries))
~~~

Expected: with the sample data, the optimized collection query should require fewer queries than the naive nested access. Exact counts can vary based on database backend, query shape and whether data was already cached.

**Important:** In Django settings, DEBUG must be True for connection.queries to collect SQL statements. Do not enable DEBUG in production just to inspect query counts.

### 14.2 Use assertNumQueries() in automated tests

A test can enforce a query budget:

~~~python
from django.test import TestCase
from orders.models import Order


class OrderQueryTests(TestCase):
    def test_order_list_prefetches_related_data(self):
        with self.assertNumQueries(2):
            orders = list(
                Order.objects.prefetch_related("items__product")
            )
            for order in orders:
                for item in order.items.all():
                    _ = item.product.name
~~~

The exact count assumes this simple two-query relationship and that the test setup has created the relevant records. If your query changes, inspect the SQL and adjust the test only after understanding the new behavior.

## 15. Run and verify the application

~~~powershell
python manage.py check
python manage.py migrate
python manage.py runserver
~~~

Open:

- http://127.0.0.1:8000/orders/
- http://127.0.0.1:8000/order-items/

Expected:
- Order list shows order numbers and customer names.
- Each order displays its item names and quantities.
- Item report displays order, customer and product data.
- An unknown order primary key returns 404.

## 16. Common errors and troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Cannot import Product | catalog app or model missing | Complete Day 43 and register catalog |
| No such table orders_order | Migration not applied | Run makemigrations orders and migrate |
| Cannot resolve keyword items | related_name mismatch | Check OrderItem.order related_name |
| select_related cannot follow relation | Tried to follow a collection | Use prefetch_related for multi-valued relation |
| Template causes many queries | Related object access not prefetched | Inspect template lookups and add suitable prefetch |
| Query count not lower | Wrong relation or no repeated access | Measure and inspect actual query pattern |
| Product deletion blocked | OrderItem uses PROTECT | This protects order history; handle intentionally |
| Empty order item list | No OrderItem rows created | Inspect sample data in shell |

## 17. Independent mini-project — Optimized Order Management System

**Business requirement:** Build an order dashboard that displays customer orders and their products efficiently.

### Required features

1. Order list with customer and date.
2. Order detail with item names, quantity and line totals.
3. Order item report.
4. Correct relationships between Order, OrderItem and Product.
5. select_related() for single-valued relationships.
6. prefetch_related() for order item collections.
7. A before-and-after query-count comparison.
8. Automated query-count test.
9. Output must remain identical before and after optimization.

### Acceptance checklist

- [ ] Orders and order items are stored in the database.
- [ ] Each item refers to one Product.
- [ ] Each order can contain multiple items.
- [ ] Product details display correctly.
- [ ] Order details display correctly.
- [ ] select_related() is used for OrderItem → Order and Product.
- [ ] prefetch_related() is used for Order → items.
- [ ] Query counts are measured.
- [ ] Optimized query output matches the naive query output.
- [ ] Existing Product Search and Phase 3 pages still work.

### Evidence to submit

- Order list screenshot.
- Order detail screenshot.
- Order item report screenshot.
- Query count before optimization.
- Query count after optimization.
- Test output.
- README explaining the relationship diagram and optimization decision.

## 18. Knowledge check

1. What is the N+1 query problem?
2. What kind of relationship does select_related() optimize?
3. What kind of relationship does prefetch_related() optimize?
4. Why does select_related() use SQL JOINs?
5. How does prefetch_related() combine results?
6. What does related_name="items" allow you to write?
7. Why is unit_price stored on OrderItem?
8. What does assertNumQueries() test?
9. Why should output be compared before and after optimization?
10. Why should optimization be based on measurement?

### Answer key

1. One initial query plus repeated queries for related records.
2. Single-valued ForeignKey and OneToOneField relationships.
3. ManyToManyField and reverse relationships that return collections.
4. A join can retrieve the related single object in the same SQL query.
5. It runs additional queries and joins related objects in Python.
6. order.items to access the related OrderItem collection.
7. To preserve the historical price used for that order.
8. It asserts that a code block runs exactly the specified number of database queries.
9. To ensure performance changes do not change the data shown.
10. To avoid unnecessary complexity and target actual bottlenecks.

## 19. Five MCQs with explanations

### Q1. Which method is normally used for ForeignKey and OneToOneField access?

A. prefetch_related() only  
B. select_related()  
C. delete()  
D. values()

**Answer: B.** select_related() joins single-valued relationships.

### Q2. Which method is appropriate for a reverse ForeignKey collection?

A. select_related()  
B. get()  
C. prefetch_related()  
D. save()

**Answer: C.** prefetch_related() loads multi-valued related collections.

### Q3. What is an N+1 query issue?

A. One query is always enough  
B. A page runs repeated queries for related rows after an initial query  
C. Database has no tables  
D. A form has too many fields

**Answer: B.** Repeated related-object lookups can increase query count.

### Q4. What does assertNumQueries(2) verify?

A. Two products exist  
B. Two URLs exist  
C. The enclosed code executes exactly two database queries  
D. Two migrations are generated

**Answer: C.** It is a Django test assertion for query count.

### Q5. What must remain true after optimization?

A. The page can show different data  
B. The output and behavior remain correct  
C. The database is deleted  
D. All relationships are removed

**Answer: B.** Optimization must preserve correctness.

## 20. Interview preparation

Prepare to explain:
1. What is the N+1 query problem?
2. Explain select_related() and prefetch_related().
3. Which relationship types are supported by each?
4. What is the difference between SQL JOIN and Python-side prefetch?
5. How do you inspect query counts?
6. What does assertNumQueries() do?
7. Why can a correct page still be inefficient?
8. How do you decide which relation to optimize?
9. Why should query results be compared after optimization?
10. What is the purpose of related_name?

Use the separate Day 44 interview guide for model answers, scenarios and project viva.

## 21. Completion checklist

- [ ] I created the orders app.
- [ ] I created Order and OrderItem models.
- [ ] I applied migrations.
- [ ] I inserted sample orders.
- [ ] I can explain ForeignKey and related_name.
- [ ] I reproduced the naive query pattern.
- [ ] I used select_related().
- [ ] I used prefetch_related().
- [ ] I measured query counts.
- [ ] I wrote or ran an assertNumQueries() test.
- [ ] The optimized output matches the original output.
- [ ] I completed Optimized Order Management System.

## 22. Connection to Day 45

Day 43 taught you to find records. Day 44 taught you to load related records efficiently. Day 45 teaches you to protect the quality of the data being stored.

~~~text
Day 43: Search and filter Product records
             |
             v
Day 44: Connect Orders, Items and Products efficiently
             |
             v
Day 45: Enforce rules before invalid data enters the database
~~~

**Day 44 is complete only when you can show measured query improvement without changing the displayed order data.**
