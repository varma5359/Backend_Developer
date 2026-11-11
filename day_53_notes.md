# Day 53: Pagination, Search and Filtering in Django Applications

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–5 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–52 — Django views, templates, models, QuerySets, Q objects, sessions and messages  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / catalog app / Product model from Day 43  
**Approved mini-project:** Paginated Product Catalog

> **Self-learning promise:** You will build a product catalog that can search, filter, sort and paginate database records. You will understand GET query parameters, validate filter values, keep pagination efficient, preserve filters between pages and test empty or invalid input.

---

# PART 1 — WHY PAGINATION IS NEEDED

## 1. The problem

Imagine an online store has 25,000 products.

If one page tries to display every product:
- The HTML response becomes large.
- The database may return many rows.
- The browser must render a large page.
- Users must scroll through too much information.
- The page may become slow.

Pagination divides a large result set into smaller pages.

Example:
- Page 1: products 1–20.
- Page 2: products 21–40.
- Page 3: products 41–60.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain pagination.
2. Explain why large QuerySets should not all be rendered at once.
3. Use Django's Paginator.
4. Understand Page objects.
5. Use page numbers from GET parameters.
6. Handle invalid and out-of-range page numbers.
7. Build search using GET parameters.
8. Build category and price filters.
9. Use QuerySet filter() and Q objects.
10. Validate user-supplied filter values.
11. Sort results safely using an allowlist.
12. Preserve filters when moving between pages.
13. Use stable ordering for pagination.
14. Understand the limitations of offset-based pagination.
15. Test pagination, search and filtering.
16. Complete Paginated Product Catalog.

## 3. Important vocabulary

| Term | Simple meaning |
|---|---|
| Pagination | Dividing results into pages |
| Page | One subset of the complete result |
| Paginator | Django helper that divides an object list or QuerySet into pages |
| Page object | Object representing one selected page |
| QuerySet | Django representation of a database query |
| Search | Finding records that match a text or term |
| Filter | Restricting records by conditions |
| Sort/order | Arranging records in a particular sequence |
| GET parameter | Value sent as part of the URL query string |
| Offset | Number of rows skipped before returning a result set |
| Limit | Maximum number of rows returned |
| Stable ordering | Predictable ordering with a unique tie-breaker |
| Allowlist | Explicit list of accepted values |

## 4. What is pagination?

Suppose the database has 100 products and the page size is 10.

~~~text
100 matching products
       |
       v
Paginator (10 per page)
       |
       +---- Page 1: 1 to 10
       |
       +---- Page 2: 11 to 20
       |
       +---- Page 3: 21 to 30
       |
       ...
       |
       +---- Page 10: 91 to 100
~~~

The application fetches and displays the selected page rather than rendering every product.

## 5. Pagination and database queries

Django QuerySets are lazy. They do not normally retrieve every matching row immediately when the QuerySet is created.

Paginator works with QuerySets and can request a count and a slice for the selected page.

The database can perform the limit/offset operation rather than the application loading all rows into memory.

Do not convert a large QuerySet to a Python list before pagination unless there is a specific reason.

---

# PART 2 — UNDERSTAND GET PARAMETERS

## 6. What is a query string?

A URL can contain a path and a query string.

Example:

~~~text
/catalog/?q=keyboard&category=Accessories&page=2
~~~

Path:
- /catalog/

Query parameters:
- q=keyboard
- category=Accessories
- page=2

The query string begins after the question mark.

## 7. Read GET parameters

In a Django view:

~~~python
request.GET
~~~

This is a QueryDict containing query-string values.

Read a value:

~~~python
search_term = request.GET.get("q", "")
~~~

The second argument is the default value if q is missing.

## 8. Why GET is appropriate for search

Search and filtering normally read data rather than changing server state.

GET is useful because:
- The URL can be bookmarked.
- The result can be shared.
- Browser refresh repeats the same search.
- Browser navigation can move between search states.

Do not use GET for deleting records or changing a cart.

## 9. Example search URLs

| URL | Meaning |
|---|---|
| /catalog/ | All active products |
| /catalog/?q=keyboard | Search for keyboard |
| /catalog/?category=Accessories | Filter category |
| /catalog/?min_price=100 | Minimum price |
| /catalog/?max_price=1000 | Maximum price |
| /catalog/?page=2 | Second result page |
| /catalog/?q=mouse&category=Accessories&page=3 | Combined search and page |

---

# PART 3 — DJANGO Paginator

## 10. Import Paginator

~~~python
from django.core.paginator import Paginator
~~~

Paginator is a Django helper that divides a collection into pages.

## 11. Basic example

~~~python
from django.core.paginator import Paginator

products = Product.objects.all()

paginator = Paginator(products, 10)

page_obj = paginator.get_page(1)
~~~

Explanation:
- products is the QuerySet.
- Paginator(products, 10) defines 10 objects per page.
- get_page(1) returns the first page.
- page_obj contains the selected page's objects and page information.

## 12. Important Paginator properties

| Property | Meaning |
|---|---|
| paginator.count | Total number of objects |
| paginator.num_pages | Total number of pages |
| paginator.page_range | Range of page numbers |
| page_obj.number | Current page number |
| page_obj.object_list | Objects on this page |
| page_obj.has_previous() | Whether an earlier page exists |
| page_obj.has_next() | Whether a later page exists |
| page_obj.previous_page_number() | Previous page number |
| page_obj.next_page_number() | Next page number |
| page_obj.start_index() | One-based index of first item on page |
| page_obj.end_index() | One-based index of last item on page |

## 13. get_page() versus page()

Paginator provides page() and get_page().

get_page():
- Accepts a page number.
- Handles invalid input by returning a sensible page.
- Returns the first page for invalid values.
- Returns the last page for an out-of-range number.

page():
- Raises exceptions for invalid or out-of-range values.
- Gives the developer more direct control over error handling.

For a beginner-facing catalog, get_page() is often convenient.

## 14. Page size

Example:

~~~python
paginator = Paginator(products, 20)
~~~

This sets a page size of 20.

Do not allow a browser parameter to request an unlimited page size.

If users can choose a page size, validate it against an allowlist such as 10, 20 or 50.

## 15. Stable ordering

Pagination needs predictable ordering.

Use:

~~~python
products.order_by("name", "pk")
~~~

The primary key provides a tie-breaker when multiple products have the same name.

Without stable ordering, rows with equal sort values may appear in inconsistent positions across page requests.

---

# PART 4 — BUILD THE PAGINATED PRODUCT CATALOG

## 16. Existing Product model

Day 43 introduced the catalog.Product model.

The example fields are:

| Field | Meaning |
|---|---|
| sku | Unique stock identifier |
| name | Product name |
| category | Product category |
| price | Decimal price |
| stock | Available stock |
| is_active | Whether the product is active |
| created_at | Creation timestamp |

Before coding:
1. Open catalog/models.py.
2. Confirm the Product model exists.
3. Confirm field names.
4. Do not create a duplicate Product model.
5. Keep the search feature from Day 43 if it already exists.

## 17. Files used

- catalog/views.py
- catalog/urls.py
- catalog/forms.py (optional structured filter form)
- catalog/templates/catalog/product_catalog.html
- catalog/tests.py

## 18. Start with a simple paginated view

In catalog/views.py:

~~~python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def product_catalog(request):
    products = Product.objects.filter(
        is_active=True
    ).order_by("name", "pk")

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "catalog/product_catalog.html",
        {"page_obj": page_obj},
    )
~~~

## 19. Understand the view step by step

1. Query active products.
2. Order them predictably.
3. Create a Paginator with 20 records per page.
4. Read the page number from the URL.
5. Ask Paginator for that page.
6. Pass the Page object to the template.

## 20. Create the catalog template

Create catalog/templates/catalog/product_catalog.html:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Catalog</title>
</head>
<body>
    <main>
        <h1>Product Catalog</h1>

        <p>
            Showing {{ page_obj.start_index }}
            to {{ page_obj.end_index }}
            of {{ page_obj.paginator.count }} products
        </p>

        {% for product in page_obj %}
            <article>
                <h2>{{ product.name }}</h2>
                <p>SKU: {{ product.sku }}</p>
                <p>Category: {{ product.category }}</p>
                <p>Price: {{ product.price }}</p>
            </article>
        {% empty %}
            <p>No products found.</p>
        {% endfor %}

        <nav aria-label="Product pages">
            {% if page_obj.has_previous %}
                <a href="?page=1">First</a>
                <a href="?page={{ page_obj.previous_page_number }}">
                    Previous
                </a>
            {% endif %}

            <span>
                Page {{ page_obj.number }}
                of {{ page_obj.paginator.num_pages }}
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">
                    Next
                </a>
                <a href="?page={{ page_obj.paginator.num_pages }}">
                    Last
                </a>
            {% endif %}
        </nav>
    </main>
</body>
</html>
~~~

## 21. Understand the template loop

page_obj is iterable.

The template loops through the objects on the selected page, not the entire database QuerySet.

The empty block displays a message when the page contains no products.

## 22. Add the URL

In catalog/urls.py, add:

~~~python
path(
    "catalog-page/",
    views.product_catalog,
    name="product_catalog",
),
~~~

If catalog routes are included under /catalog/, the browser path will include that prefix.

Do not create a duplicate urlpatterns list.

## 23. Test page navigation

Start the server:

~~~powershell
python manage.py check
python manage.py runserver
~~~

Open the catalog page.

Test:
- No page parameter.
- ?page=2.
- ?page=999999.
- ?page=abc.
- ?page=-1.

Observe how get_page() handles invalid values.

---

# PART 5 — ADD SEARCH

## 24. What is search?

Search finds records that match a user-provided term.

Example:
- Search term: keyboard.
- Matching products: Wireless Keyboard, Mechanical Keyboard.

The database can perform text matching using ORM field lookups.

## 25. Understand icontains

Example:

~~~python
Product.objects.filter(name__icontains="keyboard")
~~~

Breakdown:
- name is the model field.
- double underscore introduces a lookup.
- icontains means case-insensitive containment.
- "keyboard" is the search term.

It can match:
- Keyboard.
- keyboard.
- WIRELESS KEYBOARD.

The exact database behavior can depend on database collation and backend details, but icontains is the intended ORM lookup.

## 26. Add search to the view

~~~python
search_term = request.GET.get("q", "").strip()

products = Product.objects.filter(
    is_active=True
)

if search_term:
    products = products.filter(
        name__icontains=search_term
    )
~~~

The search term is optional.

If the user does not enter a term, the base product list remains.

## 27. Add a search form

At the top of the catalog template:

~~~html
<form method="get">
    <label for="q">Search products</label>
    <input
        type="search"
        id="q"
        name="q"
        value="{{ search_term }}"
        placeholder="Enter product name"
    >
    <button type="submit">Search</button>
</form>
~~~

GET is suitable because search is a read operation.

The value attribute keeps the search term visible after the request.

## 28. Pass the search term to the template

In the view context:

~~~python
{
    "page_obj": page_obj,
    "search_term": search_term,
}
~~~

This allows the form to preserve the entered value.

## 29. Search empty result

If no product matches:
- The QuerySet is empty.
- The paginator still returns a page object.
- The template's empty block displays a message.

Do not show a server error for a normal no-results search.

---

# PART 6 — ADD CATEGORY FILTERING

## 30. What is filtering?

Filtering restricts the result set according to one or more conditions.

Example:
- Category equals Accessories.
- Price is at least 100.
- Product is active.

Filtering is different from text search, although they can be combined.

## 31. Read category from GET

~~~python
category = request.GET.get("category", "").strip()
~~~

## 32. Apply category filter

~~~python
if category:
    products = products.filter(category=category)
~~~

The category value comes from the browser, so validate it against allowed values.

## 33. Build available category choices

For a simple catalog:

~~~python
categories = (
    Product.objects
    .filter(is_active=True)
    .values_list("category", flat=True)
    .distinct()
    .order_by("category")
)
~~~

This returns distinct category values.

## 34. Add category select

~~~html
<label for="category">Category</label>
<select name="category" id="category">
    <option value="">All categories</option>

    {% for value in categories %}
        <option
            value="{{ value }}"
            {% if category == value %}selected{% endif %}
        >
            {{ value }}
        </option>
    {% endfor %}
</select>
~~~

The selected attribute keeps the chosen category visible after the request.

## 35. Category validation

A safer approach checks whether the selected category exists in the allowed category list.

If it does not:
- Ignore it.
- Or display a validation message.
- Do not build arbitrary SQL strings from user input.

Django ORM parameterizes query values. Do not concatenate raw query values into SQL.

---

# PART 7 — ADD PRICE FILTERS

## 36. Price range

A shopper may want products between 100 and 1000.

The filter parameters could be:
- min_price
- max_price

## 37. Why parse Decimal?

Product.price is a DecimalField.

Use Python's Decimal to parse money-like values.

~~~python
from decimal import Decimal, InvalidOperation
~~~

Do not use float for price comparisons.

## 38. Parse minimum price

~~~python
raw_min_price = request.GET.get("min_price", "").strip()
min_price = None

if raw_min_price:
    try:
        min_price = Decimal(raw_min_price)
    except InvalidOperation:
        min_price = None
~~~

This handles a non-decimal value.

## 39. Validate minimum price

Additional checks:
- Is the value finite?
- Is it non-negative?
- Is it within a reasonable business limit?
- Does the application permit that many decimal places?

A user may submit an extremely large number. Do not assume every syntactically valid Decimal is a sensible business value.

## 40. Apply minimum price

~~~python
if min_price is not None:
    products = products.filter(price__gte=min_price)
~~~

gte means greater than or equal to.

## 41. Apply maximum price

~~~python
if max_price is not None:
    products = products.filter(price__lte=max_price)
~~~

lte means less than or equal to.

## 42. Validate price range

If both values are provided and min_price is greater than max_price:
- Do not run a confusing search.
- Show a validation error.
- Or ignore the invalid range.

The chosen behavior should be consistent and explained to the learner.

---

# PART 8 — USE Q OBJECTS FOR COMBINED SEARCH

## 43. What is a Q object?

Q objects allow complex query conditions.

They are useful for:
- OR conditions.
- AND combinations.
- NOT conditions.

Import:

~~~python
from django.db.models import Q
~~~

## 44. Search name OR SKU

A shopper may search by product name or SKU.

~~~python
products = products.filter(
    Q(name__icontains=search_term)
    | Q(sku__icontains=search_term)
)
~~~

The vertical bar means OR.

A product matches if either condition is true.

## 45. AND versus OR

Example:
- Name contains keyboard AND category is Accessories.
- Name contains keyboard OR SKU contains keyboard.

Django's filter calls are generally combined with AND.

Q objects can express OR.

## 46. NOT condition

Q objects can be negated using ~.

Example:

~~~python
products = products.exclude(
    Q(category="Discontinued")
)
~~~

Or:

~~~python
products = products.filter(
    ~Q(category="Discontinued")
)
~~~

Use readable conditions. Do not make a simple query unnecessarily complex.

---

# PART 9 — SORTING SAFELY

## 47. What is sorting?

Sorting arranges the result set.

Examples:
- Name A to Z.
- Price low to high.
- Price high to low.
- Newest first.

## 48. Read sort parameter

~~~python
sort_by = request.GET.get("sort", "name")
~~~

## 49. Why not accept arbitrary ordering fields?

Do not pass any arbitrary browser value directly into order_by() without validation.

Instead, define an allowlist.

~~~python
SORT_OPTIONS = {
    "name": ("name", "pk"),
    "price_low": ("price", "pk"),
    "price_high": ("-price", "pk"),
    "newest": ("-created_at", "-pk"),
}
~~~

Then:

~~~python
ordering = SORT_OPTIONS.get(
    sort_by,
    SORT_OPTIONS["name"],
)

products = products.order_by(*ordering)
~~~

The browser can select only the supported sort options.

## 50. Add sort selector

~~~html
<label for="sort">Sort by</label>
<select name="sort" id="sort">
    <option value="name">Name</option>
    <option value="price_low">Price: low to high</option>
    <option value="price_high">Price: high to low</option>
    <option value="newest">Newest</option>
</select>
~~~

To preserve selection, compare the current sort value in the template.

---

# PART 10 — PRESERVE FILTERS BETWEEN PAGES

## 51. The common pagination bug

Suppose the user searches:
- q=keyboard
- category=Accessories
- sort=price_low

They open page 2.

If the pagination link is only:

~~~html
<a href="?page=2">Next</a>
~~~

The search and filter values disappear.

The next page may show all products rather than the filtered results.

## 52. Preserve query parameters

One solution is to create a query-string helper or build the links in the view.

A simple template approach can use the current request GET values, but avoid complex mutation of QueryDict inside templates.

A reliable beginner approach is to construct pagination URLs in the view context.

## 53. Build pagination links in the view

Example:

~~~python
query_params = request.GET.copy()

pagination_links = {
    "previous": None,
    "next": None,
}

if page_obj.has_previous():
    query_params["page"] = page_obj.previous_page_number()
    pagination_links["previous"] = "?" + query_params.urlencode()

if page_obj.has_next():
    query_params["page"] = page_obj.next_page_number()
    pagination_links["next"] = "?" + query_params.urlencode()
~~~

This preserves search, category, price and sort parameters.

For first and last links, copy the same QueryDict and replace only page.

## 54. Why copy request.GET?

request.GET is a QueryDict designed for request parameters.

copy() returns a mutable copy.

This lets the view change the page value without changing the original request object.

## 55. Template pagination

~~~html
<nav aria-label="Product pages">
    {% if pagination_links.previous %}
        <a href="{{ pagination_links.previous }}">Previous</a>
    {% endif %}

    <span>
        Page {{ page_obj.number }}
        of {{ page_obj.paginator.num_pages }}
    </span>

    {% if pagination_links.next %}
        <a href="{{ pagination_links.next }}">Next</a>
    {% endif %}
</nav>
~~~

The values are query strings generated by Django's QueryDict encoding.

---

# PART 11 — COMPLETE VIEW DESIGN

## 56. Recommended view sequence

A clear view should follow this order:

1. Read GET parameters.
2. Normalize text input.
3. Validate category.
4. Parse and validate price values.
5. Build the base active-product QuerySet.
6. Apply search conditions.
7. Apply category filter.
8. Apply price filters.
9. Apply allowed sorting.
10. Create Paginator.
11. Select requested page.
12. Build pagination URLs that preserve filters.
13. Render the template with the Page object and selected filters.

This order makes the code easier to understand.

## 57. Example combined view

This example assumes the Product model has name, sku, category, price, is_active and created_at fields, as introduced in Day 43.

~~~python
from decimal import Decimal, InvalidOperation

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Product


SORT_OPTIONS = {
    "name": ("name", "pk"),
    "price_low": ("price", "pk"),
    "price_high": ("-price", "pk"),
    "newest": ("-created_at", "-pk"),
}


def product_catalog(request):
    search_term = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    sort_by = request.GET.get("sort", "name")

    raw_min_price = request.GET.get("min_price", "").strip()
    raw_max_price = request.GET.get("max_price", "").strip()

    min_price = None
    max_price = None
    errors = []

    if raw_min_price:
        try:
            min_price = Decimal(raw_min_price)
            if min_price < 0:
                errors.append("Minimum price cannot be negative.")
                min_price = None
        except InvalidOperation:
            errors.append("Enter a valid minimum price.")

    if raw_max_price:
        try:
            max_price = Decimal(raw_max_price)
            if max_price < 0:
                errors.append("Maximum price cannot be negative.")
                max_price = None
        except InvalidOperation:
            errors.append("Enter a valid maximum price.")

    if (
        min_price is not None
        and max_price is not None
        and min_price > max_price
    ):
        errors.append(
            "Minimum price cannot be greater than maximum price."
        )
        min_price = None
        max_price = None

    products = Product.objects.filter(is_active=True)

    if search_term:
        products = products.filter(
            Q(name__icontains=search_term)
            | Q(sku__icontains=search_term)
        )

    categories = (
        Product.objects
        .filter(is_active=True)
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    if category:
        if category in categories:
            products = products.filter(category=category)
        else:
            errors.append("Choose a valid category.")
            category = ""

    if min_price is not None:
        products = products.filter(price__gte=min_price)

    if max_price is not None:
        products = products.filter(price__lte=max_price)

    ordering = SORT_OPTIONS.get(
        sort_by,
        SORT_OPTIONS["name"],
    )
    products = products.order_by(*ordering)

    paginator = Paginator(products, 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    query_params = request.GET.copy()
    pagination_links = {"previous": None, "next": None}

    if page_obj.has_previous():
        previous_params = query_params.copy()
        previous_params["page"] = page_obj.previous_page_number()
        pagination_links["previous"] = (
            "?" + previous_params.urlencode()
        )

    if page_obj.has_next():
        next_params = query_params.copy()
        next_params["page"] = page_obj.next_page_number()
        pagination_links["next"] = (
            "?" + next_params.urlencode()
        )

    return render(
        request,
        "catalog/product_catalog.html",
        {
            "page_obj": page_obj,
            "search_term": search_term,
            "category": category,
            "categories": categories,
            "sort_by": sort_by,
            "min_price": raw_min_price,
            "max_price": raw_max_price,
            "errors": errors,
            "pagination_links": pagination_links,
        },
    )
~~~

Important learning note:
- This is a combined teaching example.
- Check field names against the actual Product model.
- A QuerySet is lazy; category membership evaluation may execute a query.
- For a larger application, validate category values through a dedicated form or a more efficient lookup.
- A production implementation should also cap input lengths and apply business-specific price bounds.

---

# PART 12 — CREATE THE FILTER FORM TEMPLATE

## 58. Search and filter form

In catalog/templates/catalog/product_catalog.html:

~~~html
<form method="get">
    <div>
        <label for="q">Search name or SKU</label>
        <input
            type="search"
            id="q"
            name="q"
            value="{{ search_term }}"
        >
    </div>

    <div>
        <label for="category">Category</label>
        <select name="category" id="category">
            <option value="">All categories</option>

            {% for value in categories %}
                <option
                    value="{{ value }}"
                    {% if category == value %}selected{% endif %}
                >
                    {{ value }}
                </option>
            {% endfor %}
        </select>
    </div>

    <div>
        <label for="min_price">Minimum price</label>
        <input
            type="number"
            step="0.01"
            min="0"
            id="min_price"
            name="min_price"
            value="{{ min_price }}"
        >
    </div>

    <div>
        <label for="max_price">Maximum price</label>
        <input
            type="number"
            step="0.01"
            min="0"
            id="max_price"
            name="max_price"
            value="{{ max_price }}"
        >
    </div>

    <div>
        <label for="sort">Sort by</label>
        <select name="sort" id="sort">
            <option value="name">Name</option>
            <option value="price_low">Price: low to high</option>
            <option value="price_high">Price: high to low</option>
            <option value="newest">Newest</option>
        </select>
    </div>

    <button type="submit">Apply filters</button>
    <a href="{% url 'product_catalog' %}">Clear filters</a>
</form>
~~~

## 59. Display validation errors

~~~html
{% if errors %}
    <ul role="alert">
        {% for error in errors %}
            <li>{{ error }}</li>
        {% endfor %}
    </ul>
{% endif %}
~~~

## 60. Display products

~~~html
{% for product in page_obj %}
    <article>
        <h2>{{ product.name }}</h2>
        <p>SKU: {{ product.sku }}</p>
        <p>Category: {{ product.category }}</p>
        <p>Price: {{ product.price }}</p>
    </article>
{% empty %}
    <p>No matching products were found.</p>
{% endfor %}
~~~

## 61. Display pagination links

~~~html
<nav aria-label="Product pages">
    {% if pagination_links.previous %}
        <a href="{{ pagination_links.previous }}">Previous</a>
    {% endif %}

    <span>
        Page {{ page_obj.number }}
        of {{ page_obj.paginator.num_pages }}
    </span>

    {% if pagination_links.next %}
        <a href="{{ pagination_links.next }}">Next</a>
    {% endif %}
</nav>
~~~

## 62. Preserve selected sort option

Add selected logic:

~~~html
<option value="price_low"
    {% if sort_by == "price_low" %}selected{% endif %}>
    Price: low to high
</option>
~~~

Repeat for the other sort choices.

---

# PART 13 — PAGINATION PERFORMANCE AND LIMITATIONS

## 63. Why stable ordering matters

If many products have the same price, sorting only by price can make their relative order unpredictable.

Add the primary key as a tie-breaker.

Example:
- price, pk
- -price, pk
- -created_at, -pk

## 64. Large offsets

Offset-based pagination is simple and useful for many catalogs.

However, very large page numbers may require the database to skip many rows.

For very large datasets, cursor/keyset pagination may be more efficient.

That is an advanced topic. Do not implement it before understanding normal Paginator behavior.

## 65. Count query cost

Paginator often needs to know the total number of objects.

For a large or complex QuerySet, count() may be expensive.

Production systems may:
- Cache counts where appropriate.
- Use a different pagination strategy.
- Limit available pages.
- Avoid displaying exact total counts when unnecessary.

## 66. Do not evaluate the full QuerySet too early

Avoid:

~~~python
all_products = list(Product.objects.filter(is_active=True))
paginator = Paginator(all_products, 20)
~~~

This loads every matching product into Python memory before pagination.

Prefer passing the QuerySet directly to Paginator.

## 67. Page size limits

Do not allow users to request a million rows per page.

If page size is user-selectable, validate against a small set:

~~~python
allowed_page_sizes = {10, 20, 50}
~~~

Use a safe default when the submitted value is not allowed.

---

# PART 14 — TEST THE CATALOG

## 68. Prepare sample products

Use the existing Product model from Day 43.

Create enough fictional products to test multiple pages.

For example, create 25 products with distinct SKUs and names.

Do not create duplicate SKUs if the model has a unique constraint.

## 69. Manual test matrix

| Test | URL/action | Expected |
|---|---|---|
| No filters | Catalog page | Active products |
| Search | q=keyboard | Matching name or SKU |
| Category | category=Accessories | Only selected category |
| Minimum price | min_price=100 | Price >= 100 |
| Maximum price | max_price=1000 | Price <= 1000 |
| Price range | min=100, max=1000 | Within range |
| Invalid decimal | min_price=abc | Safe validation message |
| Negative price | min_price=-1 | Validation message |
| Reversed range | min=1000, max=100 | Validation message |
| Sort low-high | sort=price_low | Lowest first |
| Sort high-low | sort=price_high | Highest first |
| Page 2 | page=2 | Next page |
| Invalid page | page=abc | Safe fallback |
| Too-large page | page=999999 | Last page |
| No matches | q=not-a-real-product | Empty message |
| Preserve filters | Move to page 2 | Search/filter values remain |

## 70. Add pagination test

In catalog/tests.py, add or merge:

~~~python
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductCatalogPaginationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for number in range(25):
            Product.objects.create(
                sku=f"PAGE-{number:03d}",
                name=f"Page Product {number:03d}",
                category="Testing",
                price=Decimal("100.00"),
                stock=10,
                is_active=True,
            )

    def test_first_page_contains_twenty_products(self):
        response = self.client.get(
            reverse("product_catalog")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["page_obj"]),
            20,
        )

    def test_second_page_contains_remaining_products(self):
        response = self.client.get(
            reverse("product_catalog"),
            {"page": "2"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["page_obj"]),
            5,
        )

    def test_invalid_page_does_not_crash(self):
        response = self.client.get(
            reverse("product_catalog"),
            {"page": "not-a-number"},
        )

        self.assertEqual(response.status_code, 200)

    def test_out_of_range_page_returns_last_page(self):
        response = self.client.get(
            reverse("product_catalog"),
            {"page": "9999"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["page_obj"].number,
            2,
        )
~~~

This test assumes 25 active products and 20 products per page in the test database.

## 71. Add search test

~~~python
def test_search_matches_product_name(self):
    response = self.client.get(
        reverse("product_catalog"),
        {"q": "Page Product 001"},
    )

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Page Product 001")
~~~

If the test file uses setUpTestData, add this method inside the same test class.

## 72. Add price filter test

~~~python
def test_minimum_price_filter(self):
    response = self.client.get(
        reverse("product_catalog"),
        {"min_price": "100.00"},
    )

    self.assertEqual(response.status_code, 200)
~~~

For a stronger test, create products with different prices and assert that excluded products are not in the Page object.

## 73. Run tests

~~~powershell
python manage.py check
python manage.py test catalog
~~~

If your app's tests already contain other test classes, keep them.

---

# PART 15 — COMMON ERRORS

## 74. Invalid page number

Use get_page() for a forgiving page selection.

If you use page(), catch PageNotAnInteger and EmptyPage.

## 75. Filters disappear on next page

The pagination link may contain only page=2.

Preserve the existing GET parameters and replace only the page value.

## 76. Search returns too many results

Check:
- Is the intended field used?
- Should search match name OR SKU?
- Is the search term stripped?
- Is the category filter applied?
- Are inactive products excluded?

## 77. Price filter raises InvalidOperation

The user submitted a value that Decimal cannot parse.

Catch InvalidOperation and show a clear validation message.

Do not silently crash.

## 78. Sort field error

The submitted sort value may be invalid.

Use an allowlist dictionary and a safe default.

Do not pass arbitrary ordering expressions from the browser into order_by().

## 79. Duplicate products across pages

Use stable ordering with a unique tie-breaker such as primary key.

Concurrent inserts and updates can still shift offset-based pages. Understand this limitation for high-change datasets.

## 80. Page loads slowly

Check:
- Is the full QuerySet converted to list?
- Are there related-object queries in the template?
- Is ordering indexed where appropriate?
- Is the filter query using useful indexes?
- Is the count query expensive?
- Is page size too large?

Pagination helps but does not automatically solve every database performance issue.

---

# PART 16 — APPROVED MINI-PROJECT

## 81. Paginated Product Catalog

### Business problem

An online store needs a product catalog that remains usable when the database contains thousands of records.

### Functional requirements

1. Display active products.
2. Show 20 products per page.
3. Search product name or SKU.
4. Filter by category.
5. Filter by minimum price.
6. Filter by maximum price.
7. Sort by name, price and creation date.
8. Validate submitted filter values.
9. Preserve filter values when navigating pages.
10. Handle empty results.
11. Handle invalid page numbers.
12. Use stable ordering.
13. Test pagination and filtering.

### Acceptance criteria

- [ ] Catalog page loads.
- [ ] Only active products appear.
- [ ] Page size is limited.
- [ ] Search works.
- [ ] Category filter works.
- [ ] Price filters work.
- [ ] Invalid price is handled safely.
- [ ] Sorting uses an allowlist.
- [ ] Pagination links preserve filters.
- [ ] Empty result message appears.
- [ ] Tests pass.
- [ ] Learner explains QuerySet laziness and stable ordering.

### Submission evidence

- Updated view and URL.
- Product catalog template.
- Test output.
- Screenshots of search and filter combinations.
- Screenshot of page navigation with filters preserved.
- README with manual test cases.

---

# PART 17 — SELF-ASSESSMENT

## 82. Short-answer questions

1. What is pagination?
2. Why is pagination useful for a large product table?
3. What is Paginator?
4. What is a Page object?
5. What does get_page() do?
6. What is the difference between page() and get_page()?
7. What is a GET parameter?
8. Why is GET appropriate for search?
9. What does icontains mean?
10. What is a Q object?
11. What is the difference between AND and OR conditions?
12. Why should price values be parsed with Decimal?
13. What is an allowlist?
14. Why should ordering be stable?
15. Why should filters be preserved in pagination links?
16. Why should a large QuerySet not be converted to a list before pagination?
17. What is offset-based pagination?
18. When might cursor pagination be useful?

## 83. Self-check answers

1. Dividing results into smaller pages.
2. It reduces the amount of data displayed and retrieved for one page.
3. Django helper that divides results into pages.
4. Object representing the selected page and its metadata.
5. It returns a valid page and handles invalid/out-of-range page values.
6. page() raises exceptions; get_page() provides forgiving fallback behavior.
7. A value sent in the URL query string.
8. Search reads data and should be shareable/bookmarkable.
9. Case-insensitive containment lookup.
10. Object for complex query conditions.
11. AND requires both conditions; OR requires either.
12. Decimal is appropriate for decimal money values.
13. A predefined set of accepted values.
14. It makes page ordering predictable.
15. Otherwise search/filter state is lost when moving pages.
16. It loads every matching row into memory.
17. Skipping a number of rows and returning the next subset.
18. For very large datasets or deep pages where offset cost is high.

## 84. MCQ assessment

### Question 1
Which Django helper divides results into pages?

- A. Paginator
- B. Permission
- C. Session
- D. Middleware

**Answer: A.** Paginator divides a collection or QuerySet into pages.

### Question 2
Which request attribute contains query-string parameters?

- A. request.POST
- B. request.GET
- C. request.user
- D. request.session only

**Answer: B.** GET parameters are available through request.GET.

### Question 3
What does name__icontains="key" do?

- A. Exact numeric match
- B. Case-insensitive text containment
- C. Delete a row
- D. Sort descending

**Answer: B.** It matches text containing the value without case-sensitive matching.

### Question 4
Why use an allowlist for sorting?

- A. To limit accepted sort options
- B. To create user accounts
- C. To store cookies
- D. To change passwords

**Answer: A.** It prevents arbitrary browser values from controlling ordering expressions.

### Question 5
Why preserve query parameters in page links?

- A. To keep the search and filters active
- B. To reset the database
- C. To log out the user
- D. To remove products

**Answer: A.** The next page should show the same filtered result set.

---

# PART 18 — INTERVIEW PREPARATION

## 85. Explain pagination in Django

**Answer:** Pagination divides a large result set into smaller pages. Django's Paginator can work with a QuerySet, calculate the number of pages and return the selected Page object. The template displays only the current page's records.

**Follow-up:** Why should you not convert a large QuerySet to a list first?

**Answer:** It loads all matching rows into application memory before pagination.

## 86. What is the difference between page() and get_page()?

**Answer:** page() raises exceptions for invalid or out-of-range values. get_page() handles those cases and returns a fallback page.

**Follow-up:** Which is convenient for a simple beginner catalog?

**Answer:** get_page().

## 87. Why use GET for search and filters?

**Answer:** Search and filters read data. GET makes the resulting URL shareable and bookmarkable and allows the browser to repeat the same query.

**Follow-up:** Should GET be used to delete a product?

**Answer:** No. Deletion changes state and should use a protected POST request.

## 88. Why use Q objects?

**Answer:** Q objects allow complex query expressions such as OR and NOT conditions. For example, search can match a product name or SKU.

**Follow-up:** What does filter() with two keyword arguments normally do?

**Answer:** It combines the conditions with AND.

## 89. Scenario: filters disappear on page 2

**Answer:** The pagination link probably includes only the page parameter. Preserve the existing GET parameters and update only the page number.

## 90. Scenario: page ordering changes between requests

**Answer:** Add stable ordering and a unique tie-breaker such as primary key. Concurrent database changes can still affect offset-based pagination.

## 91. Scenario: users can request a million rows per page

**Answer:** Do not trust a client-supplied page size. Use a fixed size or an allowlist of small supported sizes.

---

# PART 19 — INDEPENDENT COMPLETION

## 92. Draw the catalog request flow

Include:
1. Browser sends GET parameters.
2. View reads search/filter/sort/page values.
3. Values are validated.
4. QuerySet is filtered.
5. QuerySet is ordered.
6. Paginator selects a page.
7. Template displays results and navigation links.

## 93. Controlled debugging

In a local practice copy:
- Use an invalid page value.
- Use an out-of-range page.
- Submit an invalid decimal.
- Reverse the minimum and maximum prices.
- Use an unsupported sort value.
- Remove query parameters from a pagination link and observe the lost filters.
- Restore the link generation and test again.

## 94. Final checklist

- [ ] I understand pagination.
- [ ] I can use Paginator.
- [ ] I understand Page objects.
- [ ] I can read GET parameters.
- [ ] I can search with ORM lookups.
- [ ] I can use Q objects.
- [ ] I can filter categories and prices.
- [ ] I can validate filter input.
- [ ] I can sort using an allowlist.
- [ ] I can preserve filters across pages.
- [ ] I understand stable ordering.
- [ ] I tested invalid and empty cases.
- [ ] I completed Paginated Product Catalog.
- [ ] I ran automated tests.
- [ ] I completed interview and MCQ practice.

**Next lesson:** Day 54 — Complete Django Application Integration and Validation.

---

## 95. Official references

1. Django Paginator: https://docs.djangoproject.com/en/5.2/ref/paginator/
2. Django QuerySets: https://docs.djangoproject.com/en/5.2/topics/db/queries/
3. Django request and response: https://docs.djangoproject.com/en/5.2/ref/request-response/
4. Django model field lookups: https://docs.djangoproject.com/en/5.2/ref/models/querysets/
5. Django testing tools: https://docs.djangoproject.com/en/5.2/topics/testing/tools/

**Version reminder:** This lesson targets Django 5.2.19 and the Product model introduced in Day 43. Confirm model field names and URL prefixes before copying the examples.
