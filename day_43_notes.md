# Day 43: Advanced Django ORM — Filtering, Searching, Sorting and Selecting Data

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Duration:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–42 — Django project structure, models, migrations, views, URLs, templates, ModelForms and basic ORM  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django and the configured project database  
**Approved mini-project:** Advanced Product Search

> **Self-learning method:** Complete each checkpoint before moving forward. You will create a separate `catalog` app so the Employee and Student features from Phase 3 remain untouched. Day 44 will reuse this Product model.

---

## 1. What you will build

A small online store has hundreds of products. Customers need to search by product name, filter by category and price, and sort the results.

You will build an Advanced Product Search page using Django ORM.

At the end, a user can:
- Search product names without matching letter case.
- Filter by category.
- Set a minimum and maximum price.
- Sort by name, price or newest product.
- Open one product's detail page.
- See a useful empty result message when no product matches.

### Final request flow

~~~text
Browser sends GET /products/?q=mouse&min_price=300
                         |
                         v
                  catalog/views.py
                         |
                         v
              Validate search parameters
                         |
                         v
                 Build Product QuerySet
                         |
                         v
                 Database SELECT query
                         |
                         v
                products.html template
                         |
                         v
              Matching products displayed
~~~

## 2. Learning outcomes

By the end, you should be able to:

1. Explain what a QuerySet is.
2. Use `filter()`, `exclude()`, `get()`, `order_by()` and `values()`.
3. Use field lookups such as `icontains`, `gte`, `lte`, `in` and `range`.
4. Combine conditions with `Q` objects.
5. Explain QuerySet laziness and evaluation.
6. Handle `DoesNotExist` and `MultipleObjectsReturned`.
7. Build a browser search page using GET parameters.
8. Verify query results with known sample records.

## 3. Check your starting project

Open your Phase 3 Django project — the folder containing `manage.py`.

The existing structure should include your `config` project and `profiles` app. Do not replace them.

~~~text
student_portal/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── profiles/
    ├── models.py
    ├── forms.py
    ├── views.py
    └── urls.py
~~~

Activate your virtual environment. If it is named `.venv`, use PowerShell:

~~~powershell
.\.venv\Scripts\Activate.ps1
python --version
python -m django --version
python manage.py check
~~~

Expected: Django is available and the system check reports no issues.

**Checkpoint 1**
- [ ] Terminal is in the folder containing `manage.py`.
- [ ] Virtual environment is active.
- [ ] Existing Phase 3 project still works.
- [ ] `python manage.py check` passes.

## 4. Understand QuerySets

A QuerySet is a Django object that represents a collection of database records.

Example:

~~~python
Product.objects.all()
~~~

This means: "Prepare a query that can return all Product records."

A QuerySet is not the same as a Python list. Django normally delays running the database query until the results are needed.

### 4.1 QuerySet versus list

~~~python
products = Product.objects.all()  # QuerySet; query is normally not run yet
product_list = list(products)     # Evaluates the QuerySet and loads results
~~~

- `products` is a QuerySet.
- `product_list` is a Python list.
- Iterating over a QuerySet normally evaluates it.
- A QuerySet caches its results after evaluation when the same QuerySet object is reused.

### 4.2 Why QuerySets matter

A search page should not load every product and then filter the records in Python. Let the database filter and sort the records.

Prefer:

~~~python
Product.objects.filter(category="Electronics")
~~~

Avoid retrieving every row and manually looping through them to find matching records.

## 5. Create a separate catalog app

We will create a new app named `catalog`. This keeps the product search feature separate from the Phase 3 `profiles` app.

Run:

~~~powershell
python manage.py startapp catalog
~~~

Expected new folder:

~~~text
catalog/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
└── views.py
~~~

### 5.1 Register the app

Open `config/settings.py`.

Find `INSTALLED_APPS`. Add `catalog` without removing the existing applications:

~~~python
INSTALLED_APPS = [
    # Keep the existing Django applications.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Keep your existing Phase 3 apps.
    "profiles",

    # New app for Day 43 onward.
    "catalog",
]
~~~

Your settings may contain additional apps. Preserve them. Do not paste a second `INSTALLED_APPS` list over the existing one.

## 6. Create the Product model

Open `catalog/models.py` and add:

~~~python
from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"
~~~

### 6.1 Understand every field

| Field | Meaning | Example |
|---|---|---|
| `sku` | Stock keeping identifier | KB-101 |
| `name` | Product name | Wireless Keyboard |
| `category` | Product group | Accessories |
| `price` | Decimal selling price | 799.00 |
| `stock` | Available units | 25 |
| `is_active` | Whether product is shown | True |
| `created_at` | Creation timestamp | Set by Django |

The Product model is new. It does not replace the Employee model. Day 45 will add stronger data-integrity rules to this same Product model.

### 6.2 Create and apply migrations

~~~powershell
python manage.py makemigrations catalog
python manage.py migrate
python manage.py check
~~~

Expected:
- Django creates a migration for Product.
- `migrate` creates the catalog_product database table.
- The system check reports no issues.

A migration is Django's record of a database schema change. A view or template change alone does not require a migration.

## 7. Add sample products

Open the Django shell:

~~~powershell
python manage.py shell
~~~

Enter the following code. These sample SKUs are used throughout this lesson. If you already created them, choose different SKUs or remove only your own test rows.

~~~python
from decimal import Decimal
from catalog.models import Product

Product.objects.create(
    sku="KB-101",
    name="Wireless Keyboard",
    category="Accessories",
    price=Decimal("799.00"),
    stock=25,
)

Product.objects.create(
    sku="MS-102",
    name="Wireless Mouse",
    category="Accessories",
    price=Decimal("499.00"),
    stock=40,
)

Product.objects.create(
    sku="MN-103",
    name="HD Monitor",
    category="Displays",
    price=Decimal("8500.00"),
    stock=12,
)

Product.objects.create(
    sku="HD-104",
    name="USB Headphones",
    category="Audio",
    price=Decimal("1299.00"),
    stock=0,
)
~~~

Inspect the records:

~~~python
Product.objects.count()
Product.objects.all()
~~~

Expected count: 4 if this is the first time you inserted these sample records.

Exit:

~~~python
exit()
~~~

**Checkpoint 2**
- [ ] catalog app exists.
- [ ] catalog is registered in INSTALLED_APPS.
- [ ] Product migration was applied.
- [ ] Four sample products can be inspected in Django shell.

## 8. The five core ORM methods

### 8.1 filter() — return matching records

Use `filter()` when zero, one or many records may match.

~~~python
Product.objects.filter(category="Accessories")
~~~

Meaning: return products whose category is Accessories.

Expected with our sample data: Wireless Keyboard and Wireless Mouse.

Another example:

~~~python
Product.objects.filter(is_active=True)
~~~

This returns products where is_active is True.

**Remember:** `filter()` returns a QuerySet, even if only one row matches.

### 8.2 exclude() — leave out matching records

Use `exclude()` when you want all records except those matching a condition.

~~~python
Product.objects.exclude(category="Accessories")
~~~

Expected: HD Monitor and USB Headphones.

Another example:

~~~python
Product.objects.exclude(stock=0)
~~~

This leaves out products whose stock is zero.

### 8.3 get() — retrieve exactly one record

Use `get()` when you expect exactly one matching object.

~~~python
product = Product.objects.get(sku="KB-101")
product.name
~~~

Expected:

~~~text
'Wireless Keyboard'
~~~

Unlike `filter()`, `get()` returns one model instance.

Two important exceptions:

- `Product.DoesNotExist`: no record matched.
- `Product.MultipleObjectsReturned`: more than one record matched.

Example:

~~~python
try:
    product = Product.objects.get(sku="UNKNOWN")
except Product.DoesNotExist:
    print("Product was not found.")
~~~

Expected:

~~~text
Product was not found.
~~~

Do not use `get()` for a search where multiple products can match. Use `filter()` for that.

### 8.4 order_by() — sort records

Ascending price:

~~~python
Product.objects.order_by("price")
~~~

Descending price:

~~~python
Product.objects.order_by("-price")
~~~

Sort by category and then product name:

~~~python
Product.objects.order_by("category", "name")
~~~

A minus sign before a field means descending order.

### 8.5 values() — select specific fields

~~~python
Product.objects.values("sku", "name", "price")
~~~

This returns a QuerySet of dictionaries rather than full Product model instances.

Example output shape:

~~~python
[
    {"sku": "KB-101", "name": "Wireless Keyboard", "price": Decimal("799.00")},
    {"sku": "MS-102", "name": "Wireless Mouse", "price": Decimal("499.00")},
]
~~~

Use `values()` when you only need selected columns. The actual output order depends on the database query and ordering you apply.

### 8.6 Quick comparison

| Method | Result | Use it when |
|---|---|---|
| `filter()` | QuerySet | Zero, one or many matches are possible |
| `exclude()` | QuerySet | You want to omit matching rows |
| `get()` | One model instance | Exactly one row should match |
| `order_by()` | QuerySet | Results need sorting |
| `values()` | QuerySet of dictionaries | Only selected fields are required |

## 9. Field lookups — search conditions

Django uses double underscores to describe field lookups.

### 9.1 Case-insensitive text search: icontains

~~~python
Product.objects.filter(name__icontains="mouse")
~~~

Expected: Wireless Mouse.

`icontains` means the field contains the supplied text without case-sensitive matching.

Compare:
- `name__contains="Mouse"` is case-sensitive on many database backends.
- `name__icontains="mouse"` is case-insensitive.

### 9.2 Greater than or equal: gte

~~~python
Product.objects.filter(price__gte=1000)
~~~

Expected: HD Monitor and USB Headphones.

`gte` means greater than or equal to.

### 9.3 Less than or equal: lte

~~~python
Product.objects.filter(price__lte=1000)
~~~

Expected: Wireless Keyboard and Wireless Mouse.

### 9.4 In a list: in

~~~python
Product.objects.filter(category__in=["Accessories", "Audio"])
~~~

Expected: Keyboard, Mouse and Headphones.

### 9.5 Between two values: range

~~~python
Product.objects.filter(price__range=(500, 2000))
~~~

Expected: Wireless Keyboard and USB Headphones.

The range lookup includes both boundary values.

### 9.6 Useful lookup reference

| Lookup | Meaning | Example |
|---|---|---|
| `exact` | Exact match | `category__exact="Audio"` |
| `iexact` | Case-insensitive exact match | `name__iexact="wireless mouse"` |
| `contains` | Case-sensitive contains | `name__contains="Mouse"` |
| `icontains` | Case-insensitive contains | `name__icontains="mouse"` |
| `gt` | Greater than | `price__gt=1000` |
| `gte` | Greater than or equal | `price__gte=1000` |
| `lt` | Less than | `price__lt=1000` |
| `lte` | Less than or equal | `price__lte=1000` |
| `in` | Matches any value in a collection | `category__in=["Audio", "Displays"]` |
| `range` | Between two inclusive values | `price__range=(500, 2000)` |

## 10. Combine conditions with Q objects

A normal filter with multiple keyword arguments uses AND:

~~~python
Product.objects.filter(category="Accessories", price__lt=1000)
~~~

Meaning: category must be Accessories AND price must be below 1000.

For OR conditions, use `Q`:

~~~python
from django.db.models import Q

Product.objects.filter(
    Q(category="Audio") | Q(category="Displays")
)
~~~

Meaning: category is Audio OR category is Displays.

Another example:

~~~python
Product.objects.filter(
    Q(name__icontains="mouse") | Q(sku__icontains="mouse")
)
~~~

This searches the product name or SKU.

Use parentheses when combining OR and AND conditions so the intended logic is clear.

## 11. QuerySet evaluation and query inspection

### 11.1 QuerySets are lazy

~~~python
products = Product.objects.filter(category="Accessories")
~~~

This constructs a QuerySet. It normally does not immediately fetch all matching rows.

These actions evaluate the QuerySet:

~~~python
list(products)
for product in products:
    print(product.name)
len(products)
bool(products)
~~~

### 11.2 Useful inspection methods

Count matching rows:

~~~python
Product.objects.filter(category="Accessories").count()
~~~

Check whether any row exists:

~~~python
Product.objects.filter(stock=0).exists()
~~~

Get the first matching row:

~~~python
Product.objects.order_by("price").first()
~~~

Get the last matching row:

~~~python
Product.objects.order_by("price").last()
~~~

### 11.3 Inspect the SQL Django prepares

~~~python
queryset = Product.objects.filter(price__gte=500).order_by("-price")
print(queryset.query)
~~~

This prints the SQL representation of the QuerySet. It is useful for learning and debugging. Do not build SQL by concatenating untrusted user input.

## 12. Build the browser search form

The shell examples teach the ORM. Now connect the same queries to a real browser page.

### 12.1 Create catalog/forms.py

Create a new file named `catalog/forms.py`:

~~~python
from django import forms


class ProductSearchForm(forms.Form):
    q = forms.CharField(required=False, label="Product name")
    category = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)

    SORT_CHOICES = [
        ("name", "Name: A to Z"),
        ("price_low", "Price: low to high"),
        ("price_high", "Price: high to low"),
        ("newest", "Newest first"),
    ]

    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        initial="name",
    )
~~~

Explanation:
- `forms.Form` is used because this form filters data; it does not create or update a Product row.
- `required=False` means the user may leave a search field empty.
- `DecimalField` validates that price input is numeric and decimal-compatible.
- `min_value=0` rejects negative search prices.
- `ChoiceField` restricts sorting to known options. Do not pass arbitrary user input directly into `order_by()`.

### 12.2 Create the search view

Open `catalog/views.py`:

~~~python
from django.shortcuts import get_object_or_404, render

from .forms import ProductSearchForm
from .models import Product


def product_search(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.filter(is_active=True)

    if form.is_valid():
        q = form.cleaned_data["q"]
        category = form.cleaned_data["category"]
        min_price = form.cleaned_data["min_price"]
        max_price = form.cleaned_data["max_price"]
        sort = form.cleaned_data["sort"]

        if q:
            products = products.filter(name__icontains=q)

        if category:
            products = products.filter(category__iexact=category)

        if min_price is not None:
            products = products.filter(price__gte=min_price)

        if max_price is not None:
            products = products.filter(price__lte=max_price)

        sort_options = {
            "name": "name",
            "price_low": "price",
            "price_high": "-price",
            "newest": "-created_at",
        }
        products = products.order_by(sort_options[sort or "name"])

    return render(
        request,
        "catalog/product_search.html",
        {"form": form, "products": products},
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(
        request,
        "catalog/product_detail.html",
        {"product": product},
    )
~~~

### 12.3 Understand the view

1. `request.GET` contains query-string values from the URL.
2. `ProductSearchForm(request.GET or None)` binds the search parameters to the form.
3. `Product.objects.filter(is_active=True)` starts with active products only.
4. `form.is_valid()` validates the search inputs.
5. `cleaned_data` contains validated Python values.
6. Each `if` adds a filter only when the user supplied that value.
7. `sort_options` is an allow-list. The browser cannot choose arbitrary database field names.
8. `order_by()` applies the selected sort order.
9. `render()` sends the form and matching QuerySet to the template.
10. `get_object_or_404()` displays one active product or returns 404.

If the form is invalid, the view does not apply user-supplied filter values. The template can show the form errors.

### 12.4 Create catalog/urls.py

~~~python
from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_search, name="product_search"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
]
~~~

### 12.5 Connect catalog URLs

Open `config/urls.py`. Preserve the admin and profiles routes. Add the catalog include:

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profiles.urls")),
    path("", include("catalog.urls")),
]
~~~

If your current file already has imports or routes, merge these entries. Do not overwrite existing routes.

### 12.6 Create the templates folder

Create:

~~~text
catalog/
└── templates/
    └── catalog/
        ├── product_search.html
        └── product_detail.html
~~~

### 12.7 Create product_search.html

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Advanced Product Search</title>
</head>
<body>
    <h1>Advanced Product Search</h1>

    <form method="get">
        {{ form.as_p }}
        <button type="submit">Search</button>
        <a href="{% url 'product_search' %}">Clear filters</a>
    </form>

    {% if form.errors %}
        <p>Please correct the search values.</p>
    {% endif %}

    <h2>Matching products</h2>

    {% for product in products %}
        <article>
            <h3>
                <a href="{% url 'product_detail' product.pk %}">
                    {{ product.name }}
                </a>
            </h3>
            <p>SKU: {{ product.sku }}</p>
            <p>Category: {{ product.category }}</p>
            <p>Price: {{ product.price }}</p>
            <p>Available stock: {{ product.stock }}</p>
        </article>
    {% empty %}
        <p>No products match your search.</p>
    {% endfor %}
</body>
</html>
~~~

### 12.8 Create product_detail.html

~~~html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>SKU: {{ product.sku }}</p>
    <p>Category: {{ product.category }}</p>
    <p>Price: {{ product.price }}</p>
    <p>Stock: {{ product.stock }}</p>
    <a href="{% url 'product_search' %}">Back to search</a>
</body>
</html>
~~~

## 13. Run and test the search page

Run:

~~~powershell
python manage.py check
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/products/
~~~

Try these URLs:

| URL | Expected behavior |
|---|---|
| `/products/` | Show all active products |
| `/products/?q=mouse` | Show Wireless Mouse |
| `/products/?category=Accessories` | Show keyboard and mouse |
| `/products/?min_price=500` | Show products priced at least 500 |
| `/products/?max_price=1000` | Show products priced at most 1000 |
| `/products/?min_price=500&max_price=2000` | Show products in that price interval |
| `/products/?sort=price_high` | Sort highest price first |
| `/products/?q=not-a-product` | Show the empty-state message |

The examples assume the four sample products were inserted and remain active.

### Invalid input test

Open:

~~~text
http://127.0.0.1:8000/products/?min_price=abc
~~~

Expected: the search form shows a validation error. The application should not crash.

## 14. Common errors and troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `No module named catalog` | App not created or registered | Check folder and INSTALLED_APPS |
| `no such table: catalog_product` | Migration not applied | Run makemigrations catalog and migrate |
| `FieldError` | Lookup uses a field that does not exist | Compare lookup with Product model field names |
| `DoesNotExist` | get() found no row | Handle Product.DoesNotExist or use get_object_or_404 in a view |
| `MultipleObjectsReturned` | get() matched more than one row | Use filter() or a truly unique lookup |
| Search ignores a field | Form name and cleaned_data key differ | Match input names to ProductSearchForm fields |
| Invalid price crashes view | Raw request.GET used without validation | Use DecimalField and cleaned_data |
| Sort parameter causes an error | Untrusted or unsupported sort field | Use the sort_options allow-list |
| TemplateDoesNotExist | Wrong template path | Check catalog/templates/catalog/ |
| NoReverseMatch | URL name differs | Compare name= with template url tags |
| Duplicate sample rows | Shell seed code was run twice | Check existing SKUs before inserting |

### Safe repeatable sample insertion

Before adding sample data again:

~~~python
Product.objects.filter(sku="KB-101").exists()
~~~

If it returns True, do not insert the same sample again. Day 45 adds the database uniqueness rule for SKU.

## 15. Independent mini-project — Advanced Product Search

**Business requirement:** Build a search page for an online store so a customer can find products using multiple criteria.

### Required features

- Display active products.
- Search by product name.
- Filter by category.
- Filter by minimum and maximum price.
- Sort by name, price ascending, price descending and newest.
- Open one product detail page.
- Display an empty state.
- Validate invalid search values.

### Required ORM methods

- `filter()`
- `exclude()`
- `get()`
- `order_by()`
- `values()`
- Field lookups: `icontains`, `gte`, `lte`, `in`, `range`
- At least one `Q` query.

### Acceptance tests

- [ ] Search is case-insensitive.
- [ ] Category filter returns only matching products.
- [ ] Minimum and maximum price filters work together.
- [ ] Sorting options produce the correct order.
- [ ] Empty results show a message, not an error.
- [ ] Invalid numeric search input shows a form error.
- [ ] Detail page displays the selected product.
- [ ] Unknown product primary key returns 404.
- [ ] get() exceptions are understood.
- [ ] Existing Phase 3 Student and Employee pages still work.

### Evidence to submit

- Product list screenshot.
- Search result screenshot.
- Price-filter screenshot.
- Product detail screenshot.
- Output of at least five shell queries.
- README with setup instructions and tested URLs.
- One debugging note explaining a problem and its solution.

## 16. Knowledge check — answer before reading

1. What is a QuerySet?
2. What is the difference between filter() and get()?
3. What happens when get() finds no record?
4. What does exclude() return?
5. What does the minus prefix in order_by("-price") mean?
6. What is the difference between values() and retrieving model instances?
7. What does icontains do?
8. What is the meaning of gte?
9. What does __in do?
10. Why are QuerySets called lazy?
11. Name two ways to evaluate a QuerySet.
12. When should Q objects be used?
13. Why should search inputs be validated?
14. Why is a sort allow-list useful?
15. Why should sample seed data be checked before inserting again?

### Answer key

1. A Django object representing a database query and its potential result rows.
2. filter() returns a QuerySet; get() expects exactly one object.
3. It raises DoesNotExist.
4. A QuerySet excluding rows matching the condition.
5. Descending order.
6. values() returns dictionaries containing selected fields; normal QuerySets return model instances.
7. Case-insensitive substring matching.
8. Greater than or equal to.
9. Match any value in a supplied collection.
10. The query is usually delayed until results are needed.
11. Iteration and list(); count(), exists() and other evaluation operations are also available.
12. To express OR and more complex boolean conditions.
13. To reject malformed input and avoid runtime errors.
14. It prevents arbitrary client input from becoming a database field expression.
15. To avoid duplicate sample records and keep tests predictable.

## 17. Five MCQs with explanations

### Q1. Which method returns a QuerySet of matching products?

A. get()  
B. filter()  
C. save()  
D. delete()

**Correct answer: B — filter().** It returns a QuerySet containing zero or more matching records.

### Q2. What happens if get() finds no matching record?

A. It returns an empty list.  
B. It returns None.  
C. It raises DoesNotExist.  
D. It creates a record.

**Correct answer: C — DoesNotExist.** A get() query expects exactly one object.

### Q3. Which lookup searches text without case sensitivity?

A. exact  
B. icontains  
C. gte  
D. range

**Correct answer: B — icontains.** It finds a substring regardless of letter case.

### Q4. What does order_by("-price") do?

A. Sorts price low to high  
B. Removes price  
C. Sorts price high to low  
D. Filters price equal to zero

**Correct answer: C — Sorts price high to low.** The minus prefix means descending order.

### Q5. Why use a sort allow-list in a search view?

A. To let users execute arbitrary SQL  
B. To restrict sorting to supported fields and expressions  
C. To delete old products  
D. To disable form validation

**Correct answer: B.** The server maps approved options to known ORM fields.

## 18. Interview preparation

Prepare to explain:
1. What is Django ORM?
2. What is a QuerySet?
3. Explain filter(), exclude() and get().
4. What is the difference between get() and filter()?
5. What is QuerySet laziness?
6. Explain order_by() with ascending and descending examples.
7. What does values() return?
8. Explain field lookups such as icontains, gte, in and range.
9. When do you use Q objects?
10. How do you handle DoesNotExist and MultipleObjectsReturned?
11. How do you validate query-string values?
12. How would you implement multi-field product search?

Use the separate Day 43 interview guide for model answers, code-reading and scenarios.

## 19. Completion checklist

- [ ] I created and registered the catalog app.
- [ ] I created the Product model and applied migrations.
- [ ] I inserted and inspected sample products.
- [ ] I can explain all five core ORM methods.
- [ ] I practised field lookups.
- [ ] I used a Q object.
- [ ] I understand lazy QuerySets.
- [ ] I built the browser search form and view.
- [ ] I tested valid and invalid search parameters.
- [ ] I completed Advanced Product Search.
- [ ] I can explain the result of each query without guessing.

## 20. Connection to Day 44

Day 43 teaches how to find the correct records. Day 44 teaches how to retrieve related records efficiently when a page displays orders, customers and products.

~~~text
Day 43: Find the right products
    |
    +-- filter and exclude
    +-- field lookups
    +-- sorting and selected fields
              |
              v
Day 44: Load related order data efficiently
    |
    +-- select_related()
    +-- prefetch_related()
    +-- measure database query count
~~~

**Day 43 is complete only when Advanced Product Search works with your own sample data and you can explain why each ORM method is used.**
