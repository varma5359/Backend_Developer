# Day 49: Django Sessions, Cookies and Session Management

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 4 — Django ORM, Forms and Authentication  
**Estimated time:** 4–5 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 27–48 — Django project structure, authentication, registration, login, logout and password management  
**Environment:** Windows, VS Code, PowerShell, Python virtual environment, Django 5.2.19  
**Project continuity:** student_portal / config / profiles; catalog app and Product model from Day 43  
**Approved mini-project:** Session-Based Shopping Cart

> **Self-learning promise:** You will understand how a browser remembers a visitor between requests, how Django sessions work, and how to build a small shopping cart. You will store only product identifiers and quantities in the session, read prices from the database, and use POST for cart changes.

---

# PART 1 — WHY SESSIONS EXIST

## 1. The problem: HTTP requests are separate

A browser sends a request to a server. The server sends a response.

Then the browser may send another request.

HTTP is designed as a stateless protocol. A later request does not automatically contain all the application state from the previous request.

Imagine a student opens a portal:
1. The student signs in.
2. Opens the profile page.
3. Opens the course page.
4. Opens the dashboard.

The application needs a way to associate these requests with the same signed-in user.

A shopping cart has a similar requirement:
1. A visitor adds a keyboard.
2. Opens another product page.
3. Adds a mouse.
4. Opens the cart.
5. The cart should still contain both products.

Sessions help maintain this state between requests.

## 2. Learning outcomes

By the end of this lesson, you should be able to:

1. Explain why HTTP is described as stateless.
2. Explain what a browser cookie is.
3. Explain what a Django session is.
4. Distinguish cookie data from server-side session data.
5. Explain how Django identifies a session.
6. Identify SessionMiddleware and session settings.
7. Read and write request.session values.
8. Set and remove session keys.
9. Explain session expiry.
10. Explain cookie security attributes.
11. Build a session-based shopping cart.
12. Store product IDs and quantities rather than trusting client prices.
13. Update session dictionaries safely.
14. Test cart add, update, remove and clear operations.
15. Diagnose session and cookie problems.
16. Complete Session-Based Shopping Cart.

## 3. Vocabulary

| Word | Simple meaning |
|---|---|
| HTTP | Protocol used for browser-server communication |
| Stateless | Each request is independent unless state is added |
| Cookie | Small piece of data stored by the browser |
| Session | Server-managed state associated with a visitor/browser |
| Session key | Identifier used to find a session |
| Session data | Values associated with a session |
| Middleware | Django component that processes requests/responses around views |
| Expiry | Time or event after which a session is no longer valid |
| SameSite | Cookie attribute that controls when browsers send a cookie in cross-site contexts |
| Secure cookie | Cookie sent only over secure HTTPS connections when the Secure flag is enabled |
| HttpOnly | Cookie attribute that prevents ordinary JavaScript access |
| Cart | Collection of products selected by a shopper |

## 4. What is a cookie?

A cookie is a small value stored by the browser for a website.

The browser can send the cookie back with later requests that match its domain, path and security rules.

Cookies are often used for:
- Session identifiers.
- Preferences.
- Non-sensitive interface settings.
- Some security-related values.

A cookie is not a database table and is not automatically private from the person using the browser.

## 5. What is a session?

A session is a way for an application to associate data with a visitor across multiple requests.

In Django's standard database-backed session setup:
- Session data is stored on the server side in the database.
- The browser normally stores a session identifier in a cookie.
- The browser sends that cookie with later requests.
- Django uses the identifier to retrieve the session data.

The browser cookie is usually an identifier, not the entire shopping cart.

## 6. Cookie versus session

| Cookie | Session |
|---|---|
| Stored in the browser | Session data is stored using the configured session backend |
| Sent with matching requests | Accessed through Django's request.session |
| Can be read or changed by the browser user | Server-side data is controlled by the application |
| Has attributes such as Secure, HttpOnly and SameSite | Has expiry and storage behavior |
| Often stores a session identifier | Can store cart IDs, preferences or temporary workflow state |

Important: Django supports multiple session backends. Do not assume every project stores session data in the database. This lesson uses the standard database-backed session configuration.

## 7. Session request flow

~~~text
Browser
   |
   | Request with session cookie (if available)
   v
Django SessionMiddleware
   |
   v
Load session data for the session identifier
   |
   v
AuthenticationMiddleware can identify request.user
   |
   v
Django view reads request.session
   |
   v
View updates session data
   |
   v
Django saves changed session data
   |
   v
Response sent to browser
~~~

This is a simplified flow. Middleware order matters.

## 8. Why not put everything in a cookie?

A browser cookie is controlled by the browser and can be inspected by the person using it.

Do not place sensitive information such as:
- Raw passwords.
- Password reset tokens.
- Payment card numbers.
- Secret API keys.
- Private account data.

Django's signed-cookie session backend signs data to detect tampering, but signing does not make arbitrary client-side data secret. The standard database session backend keeps session data on the server.

For this lesson, use the database-backed session store.

---

# PART 2 — DJANGO SESSION CONFIGURATION

## 9. Open the existing project

Open the student_portal folder.

Activate the existing virtual environment:

~~~powershell
.\.venv\Scripts\Activate.ps1
python -m django --version
~~~

Confirm the version used by the course.

## 10. Check installed apps

Open config/settings.py.

Confirm:

~~~python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "profiles.apps.ProfilesConfig",
    "catalog.apps.CatalogConfig",
]
~~~

Your actual file may contain more apps. Add catalog only if the Day 43 app is part of the same project and it is not already registered.

## 11. Check SessionMiddleware

Find MIDDLEWARE.

Confirm this entry exists:

~~~python
"django.contrib.sessions.middleware.SessionMiddleware",
~~~

It must appear before AuthenticationMiddleware in the normal generated configuration.

SessionMiddleware makes request.session available to views.

## 12. Understand the session engine

Django's default session engine is database-backed.

The setting can be written explicitly:

~~~python
SESSION_ENGINE = "django.contrib.sessions.backends.db"
~~~

This is the standard database-backed session engine.

Do not change to a different session backend unless the application has a reason and the implications are understood.

## 13. Check session migrations

Run:

~~~powershell
python manage.py showmigrations sessions
~~~

If the session migrations are not applied, run:

~~~powershell
python manage.py migrate
~~~

The sessions app uses a database table to store session records.

Do not delete the session table as a normal troubleshooting step.

## 14. Important session settings

| Setting | Purpose |
|---|---|
| SESSION_ENGINE | Selects how session data is stored |
| SESSION_COOKIE_NAME | Name of the browser cookie holding the session identifier |
| SESSION_COOKIE_AGE | Default session cookie age in seconds |
| SESSION_EXPIRE_AT_BROWSER_CLOSE | Whether the browser-close behavior is requested for the session cookie |
| SESSION_COOKIE_SECURE | Sends the cookie only over HTTPS when enabled |
| SESSION_COOKIE_HTTPONLY | Prevents ordinary JavaScript from reading the cookie |
| SESSION_COOKIE_SAMESITE | Controls cross-site cookie sending behavior |
| SESSION_SAVE_EVERY_REQUEST | Controls whether the session is saved on every request |

These settings should be chosen for the deployment environment. Do not blindly copy production security settings into a local HTTP-only development environment without understanding why a secure cookie may not be sent over plain HTTP.

## 15. Inspect the standard session cookie

After a session is created, inspect the browser developer tools:
1. Open the browser.
2. Open Developer Tools.
3. Select Application or Storage.
4. Open Cookies.
5. Select the local site.
6. Look for the session cookie, commonly named sessionid.

Do not share the cookie value in screenshots or messages. It is a credential-like identifier.

---

# PART 3 — WORK WITH request.session

## 16. What is request.session?

Django attaches a session object to the request when SessionMiddleware is enabled.

Example:

~~~python
request.session
~~~

It behaves similarly to a dictionary for many common operations.

You can:
- Store a value.
- Read a value.
- Change a value.
- Delete a value.
- Clear session data.
- Set an expiry time.

## 17. Store a value

Example:

~~~python
request.session["preferred_language"] = "en"
~~~

Explanation:
- request is the current HTTP request.
- session is the session object.
- ["preferred_language"] selects one key.
- The value "en" is stored for the session.

The data is available to later requests associated with the same session.

## 18. Read a value

~~~python
language = request.session.get("preferred_language", "en")
~~~

get() returns the stored value if the key exists.

If the key does not exist, it returns the default value "en".

This avoids a KeyError.

## 19. Update a value

~~~python
request.session["preferred_language"] = "te"
~~~

The value for that key is replaced.

## 20. Delete one key

~~~python
request.session.pop("preferred_language", None)
~~~

pop() removes the key.

The second argument None means that no error is raised if the key is missing.

## 21. Clear session data

~~~python
request.session.clear()
~~~

This removes all values from the current session.

Be careful: clearing a session can remove other session state, not just a shopping cart. Do not use clear() when the goal is to remove one cart key only.

## 22. Nested dictionary update behavior

Suppose the session contains:

~~~python
request.session["cart"] = {
    "12": 2,
    "18": 1,
}
~~~

A common beginner mistake is:

~~~python
request.session["cart"]["12"] = 3
~~~

Django may not detect a change inside the nested dictionary automatically.

Safer approach:

~~~python
cart = request.session.get("cart", {})
cart["12"] = 3
request.session["cart"] = cart
~~~

Reassigning the updated dictionary marks the session as modified.

You can also set:

~~~python
request.session.modified = True
~~~

Prefer a clear update pattern and understand why it is needed.

## 23. Session expiry

A session can expire after a configured period.

Example:

~~~python
request.session.set_expiry(900)
~~~

The value is seconds.

900 seconds = 15 minutes.

Other options include:
- 0: expire the session cookie when the browser is closed.
- None: use the configured default session age.
- A datetime or timedelta: set a specific expiry time.

Do not confuse cookie expiry with every possible server-side cleanup policy. Expired database sessions may be removed by Django's cleanup command.

## 24. Read expiry information

Django provides session methods to inspect expiry behavior.

Examples:

~~~python
request.session.get_expiry_age()
request.session.get_expiry_date()
request.session.get_expire_at_browser_close()
~~~

These methods help inspect the current session's expiry configuration.

## 25. Session key

A session has a key used by the configured session backend.

Example:

~~~python
request.session.session_key
~~~

The key may be None before a session is saved.

Do not display or log session keys in a public page.

## 26. Session security reminder

Session data is not a replacement for authorization.

If a session contains a value such as:

~~~python
request.session["is_admin"] = True
~~~

Do not treat that value as proof of administrative permission.

Use Django's authenticated user and permission system for access decisions.

---

# PART 4 — BUILD A SESSION-BASED SHOPPING CART

## 27. What will the cart do?

A visitor can:
- View active products.
- Add a product to a cart.
- Increase its quantity.
- View cart items.
- Update a quantity.
- Remove one item.
- Empty the cart.

The cart will use session data to remember the selected product IDs and quantities.

## 28. Why store IDs and quantities only?

A session cart can contain:

~~~python
{
    "12": 2,
    "18": 1,
}
~~~

Meaning:
- Product with primary key 12: quantity 2.
- Product with primary key 18: quantity 1.

Do not store the product price as a trusted session value.

A user may be able to alter client-controlled data. Even if the session backend is server-side, price and stock can change in the database.

Always read the current product price from the database when displaying or calculating a cart.

## 29. Project app and model continuity

Day 43 introduced the catalog app and Product model.

The example Product fields are:
- sku
- name
- category
- price
- stock
- is_active
- created_at

Confirm that your actual model matches the fields used by the view. If the earlier lesson uses a different field name, adapt the code to the approved model rather than creating a duplicate Product class.

## 30. Files used today

You will create or update:

- catalog/views.py
- catalog/urls.py
- catalog/templates/catalog/product_list.html
- catalog/templates/catalog/cart_detail.html
- config/urls.py
- catalog/tests.py

Keep the existing catalog model and product-search views.

## 31. Add the product list view

Open catalog/views.py.

Add imports if they are not already present:

~~~python
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Product
~~~

Add:

~~~python
def product_list(request):
    products = Product.objects.filter(
        is_active=True
    ).order_by("name")

    return render(
        request,
        "catalog/product_list.html",
        {"products": products},
    )
~~~

This view shows active products. It does not change session data.

## 32. Add the cart add view

~~~python
@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(
        Product,
        pk=product_id,
        is_active=True,
    )

    try:
        quantity = int(request.POST.get("quantity", "1"))
    except (TypeError, ValueError):
        quantity = 1

    if quantity < 1:
        quantity = 1

    cart = request.session.get("cart", {})
    product_key = str(product.pk)

    current_quantity = int(cart.get(product_key, 0))
    cart[product_key] = current_quantity + quantity

    request.session["cart"] = cart

    return redirect("cart_detail")
~~~

## 33. Explain cart_add line by line

require_POST:
- Restricts the view to POST requests.
- Adding an item changes cart state.
- GET should not add an item.

get_object_or_404:
- Looks up the product.
- Returns a 404 response if the product does not exist.
- The is_active condition prevents adding an inactive product.

request.POST.get:
- Reads the quantity from submitted form data.
- Uses "1" when the value is missing.

int():
- Converts the submitted string to an integer.

try/except:
- Handles invalid numeric input.
- Prevents an invalid value from crashing the view.

cart:
- Reads the current session cart.
- Uses an empty dictionary when the cart key does not exist.

product_key:
- Converts the primary key to a string.
- Session JSON-like structures use string dictionary keys consistently.

current_quantity:
- Reads the quantity already in the cart.

Reassignment:
- Saves the updated cart dictionary back into the session.

## 34. Why validate quantity?

A browser can submit unexpected values.

Examples:
- Empty string.
- "abc".
- 0.
- -4.
- Very large numbers.

A real store also needs:
- Maximum quantity limits.
- Stock checks.
- Availability checks.
- Business rules for bulk orders.

This lesson introduces safe integer parsing. Add stock enforcement as an extension and validate it again at checkout.

## 35. Add the cart detail view

~~~python
from decimal import Decimal

def cart_detail(request):
    cart = request.session.get("cart", {})
    product_ids = list(cart.keys())

    products = Product.objects.filter(
        pk__in=product_ids,
        is_active=True,
    )

    items = []
    total = Decimal("0.00")

    for product in products:
        quantity = int(cart.get(str(product.pk), 0))

        if quantity < 1:
            continue

        line_total = product.price * quantity
        total += line_total

        items.append({
            "product": product,
            "quantity": quantity,
            "line_total": line_total,
        })

    return render(
        request,
        "catalog/cart_detail.html",
        {
            "items": items,
            "total": total,
        },
    )
~~~

## 36. Explain cart_detail

The view:
1. Reads the cart dictionary from the session.
2. Extracts product IDs.
3. Queries the database for active products.
4. Gets each quantity from the session.
5. Reads the current price from the Product model.
6. Calculates each line total.
7. Adds the line totals.
8. Sends the items and total to the template.

The price is read from the database. The browser does not get to decide the price.

## 37. Decimal values for money

Product.price is a DecimalField.

The example initializes the total using:

~~~python
total = Decimal("0.00")
~~~

Use Decimal for financial calculations rather than binary floating-point values.

A float such as 0.1 cannot always be represented exactly in binary floating-point. Decimal is designed for base-10 decimal arithmetic.

## 38. Add quantity update view

~~~python
@require_POST
def cart_update(request, product_id):
    product = get_object_or_404(
        Product,
        pk=product_id,
        is_active=True,
    )

    try:
        quantity = int(request.POST.get("quantity", "1"))
    except (TypeError, ValueError):
        quantity = 1

    cart = request.session.get("cart", {})
    product_key = str(product.pk)

    if quantity < 1:
        cart.pop(product_key, None)
    else:
        cart[product_key] = quantity

    request.session["cart"] = cart

    return redirect("cart_detail")
~~~

This example treats a quantity less than one as a request to remove the item. A different business design could reject the value and display an error.

## 39. Add remove item view

~~~python
@require_POST
def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    cart.pop(str(product_id), None)

    request.session["cart"] = cart

    return redirect("cart_detail")
~~~

This view removes one product key from the session dictionary.

The product may already have been removed or become inactive. The operation remains safe because pop() uses a default value.

## 40. Add clear cart view

~~~python
@require_POST
def cart_clear(request):
    request.session["cart"] = {}
    return redirect("cart_detail")
~~~

Do not use request.session.clear() here because that would remove unrelated session data such as other application state.

## 41. Complete cart views file — integration reminder

The snippets in this lesson are additions to the existing catalog/views.py.

Do not replace Day 43 product-search views.

Check that:
- There is one Product import.
- There is one Decimal import.
- There is one urlpatterns list in catalog/urls.py.
- Function names match URL references.
- Existing product search routes still work.

---

# PART 5 — CREATE CART TEMPLATES

## 42. Product list template

Create catalog/templates/catalog/product_list.html.

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
            <a href="{% url 'cart_detail' %}">View cart</a>
        </p>

        {% for product in products %}
            <article>
                <h2>{{ product.name }}</h2>
                <p>SKU: {{ product.sku }}</p>
                <p>Category: {{ product.category }}</p>
                <p>Price: {{ product.price }}</p>
                <p>Available stock: {{ product.stock }}</p>

                <form method="post"
                      action="{% url 'cart_add' product.pk %}">
                    {% csrf_token %}

                    <label for="quantity-{{ product.pk }}">
                        Quantity
                    </label>

                    <input
                        type="number"
                        id="quantity-{{ product.pk }}"
                        name="quantity"
                        value="1"
                        min="1"
                    >

                    <button type="submit">Add to cart</button>
                </form>
            </article>
        {% empty %}
            <p>No active products are available.</p>
        {% endfor %}
    </main>
</body>
</html>
~~~

## 43. Explain the template

for product in products:
- Loops through the QuerySet.

product.name:
- Displays the product name.

product.price:
- Displays the current database price.

url 'cart_add' product.pk:
- Builds the add-to-cart URL using the product primary key.

method="post":
- Sends a state-changing request.

csrf_token:
- Adds the CSRF protection token.

## 44. Cart detail template

Create catalog/templates/catalog/cart_detail.html.

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Shopping Cart</title>
</head>
<body>
    <main>
        <h1>Your Shopping Cart</h1>

        <p>
            <a href="{% url 'product_list' %}">Continue shopping</a>
        </p>

        {% if items %}
            {% for item in items %}
                <article>
                    <h2>{{ item.product.name }}</h2>
                    <p>Unit price: {{ item.product.price }}</p>
                    <p>Quantity: {{ item.quantity }}</p>
                    <p>Line total: {{ item.line_total }}</p>

                    <form method="post"
                          action="{% url 'cart_update' item.product.pk %}">
                        {% csrf_token %}
                        <label>
                            New quantity
                            <input
                                type="number"
                                name="quantity"
                                value="{{ item.quantity }}"
                                min="1"
                            >
                        </label>
                        <button type="submit">Update</button>
                    </form>

                    <form method="post"
                          action="{% url 'cart_remove' item.product.pk %}">
                        {% csrf_token %}
                        <button type="submit">Remove item</button>
                    </form>
                </article>
            {% endfor %}

            <h2>Cart total: {{ total }}</h2>

            <form method="post" action="{% url 'cart_clear' %}">
                {% csrf_token %}
                <button type="submit">Empty cart</button>
            </form>
        {% else %}
            <p>Your cart is empty.</p>
        {% endif %}
    </main>
</body>
</html>
~~~

## 45. Why use separate forms?

Each form has one clear operation:
- Update quantity.
- Remove one product.
- Clear the cart.

A separate POST endpoint makes the behavior explicit and testable.

## 46. Empty cart behavior

The template uses:

~~~django
{% if items %}
...
{% else %}
    <p>Your cart is empty.</p>
{% endif %}
~~~

If items is empty, the learner sees a useful message rather than a blank page.

---

# PART 6 — URL CONFIGURATION

## 47. Create catalog/urls.py

Create the file if it does not exist.

~~~python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path(
        "cart/add/<int:product_id>/",
        views.cart_add,
        name="cart_add",
    ),
    path(
        "cart/update/<int:product_id>/",
        views.cart_update,
        name="cart_update",
    ),
    path(
        "cart/remove/<int:product_id>/",
        views.cart_remove,
        name="cart_remove",
    ),
    path("cart/clear/", views.cart_clear, name="cart_clear"),
]
~~~

If the app already has product-search routes, keep them in the same urlpatterns list.

## 48. Include catalog routes in config/urls.py

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("", include("profiles.urls")),
]
~~~

If you already use the root path for another app, choose a consistent prefix and update the template URLs accordingly.

## 49. Route reference

| Path | Name | Method | Purpose |
|---|---|---|---|
| /catalog/ | product_list | GET | Show active products |
| /catalog/cart/ | cart_detail | GET | Show cart |
| /catalog/cart/add/12/ | cart_add | POST | Add product 12 |
| /catalog/cart/update/12/ | cart_update | POST | Update product 12 quantity |
| /catalog/cart/remove/12/ | cart_remove | POST | Remove product 12 |
| /catalog/cart/clear/ | cart_clear | POST | Empty cart |

The exact URL for a product depends on its database primary key.

---

# PART 7 — SESSION BEHAVIOR AND SECURITY

## 50. A session cart is not an order

A shopping cart is temporary selection state.

An order is a persistent business record.

A production checkout must:
- Re-read product details from the database.
- Verify current stock.
- Recalculate price.
- Apply tax and discount rules on the server.
- Create an order and order items.
- Use a database transaction where appropriate.
- Avoid trusting the browser's submitted total.

Never treat the session cart total as the final amount to charge.

## 51. Product price must come from the database

Unsafe design:
- Store price in the browser.
- Accept the submitted price.
- Calculate final amount using the submitted price.

Safer design:
- Session stores product ID and quantity.
- Server queries Product.
- Server reads current price.
- Server calculates line total.

This is why the lesson stores only IDs and quantities in the session.

## 52. Stock must be checked again

A product may have 5 units when added to the cart.

Another shopper may purchase those 5 units before checkout.

At checkout:
- Query the product again.
- Check current stock.
- Reject or adjust unavailable quantities according to business rules.
- Do not assume the cart's earlier stock display is still current.

## 53. Session fixation and login

Django's login handling rotates or cycles session state as appropriate to reduce session fixation risks.

Do not manually preserve an untrusted session identifier across authentication.

Use Django's login() and logout() APIs.

## 54. Cookie Secure

SESSION_COOKIE_SECURE=True tells the browser to send the session cookie only over HTTPS.

Use this in a correctly configured HTTPS deployment.

If you set it in a local plain-HTTP development environment, the browser may not send the cookie over HTTP and the session may appear to disappear.

## 55. Cookie HttpOnly

SESSION_COOKIE_HTTPONLY=True prevents ordinary JavaScript from reading the cookie.

This reduces exposure to some client-side script attacks.

It does not prevent all cross-site scripting and does not replace output escaping or other security controls.

## 56. Cookie SameSite

SameSite controls when the browser sends a cookie in cross-site contexts.

Django supports values such as:
- Lax
- Strict
- None

The correct choice depends on application flows such as external identity providers and cross-site integrations.

SameSite=None requires Secure in modern browser behavior.

Do not change this setting without testing the login, payment or external authentication flows.

## 57. Session expiry

A shopping cart may expire after a configured time.

A short expiry can be appropriate for temporary state, but do not set a tiny value without a business reason.

If the session expires:
- The cart may disappear.
- The visitor may need to add products again.
- The application should show an understandable empty-cart state.

For a long-lived persistent cart, store cart data in database models associated with an account rather than relying only on a temporary anonymous session.

## 58. Never store sensitive information in a cart session

Do not store:
- Card numbers.
- CVV.
- Raw passwords.
- Authentication tokens.
- API keys.
- Private customer data that is not required.

The cart stores product identifiers and quantities only.

---

# PART 8 — TEST THE CART

## 59. Prepare sample products

The Day 43 catalog Product model should exist.

Open the shell:

~~~powershell
python manage.py shell
~~~

Create fictional products if they do not already exist:

~~~python
from decimal import Decimal
from catalog.models import Product

Product.objects.get_or_create(
    sku="CART-KB-01",
    defaults={
        "name": "Practice Keyboard",
        "category": "Accessories",
        "price": Decimal("799.00"),
        "stock": 10,
        "is_active": True,
    },
)

Product.objects.get_or_create(
    sku="CART-MS-01",
    defaults={
        "name": "Practice Mouse",
        "category": "Accessories",
        "price": Decimal("399.00"),
        "stock": 20,
        "is_active": True,
    },
)
~~~

These values are fictional training data.

## 60. Start the server

~~~powershell
python manage.py check
python manage.py runserver
~~~

Open:

~~~text
http://127.0.0.1:8000/catalog/
~~~

## 61. Test add to cart

1. Select Practice Keyboard.
2. Set quantity to 2.
3. Click Add to cart.
4. Open the cart.

Expected:
- Keyboard appears.
- Quantity is 2.
- Unit price comes from the Product record.
- Line total is calculated by the server.

## 62. Test multiple products

Add:
- Keyboard quantity 2.
- Mouse quantity 1.

Expected cart:
- Two different product rows.
- Correct quantities.
- Total equal to the sum of database prices multiplied by quantities.

## 63. Test quantity update

Change keyboard quantity from 2 to 3.

Expected:
- Quantity becomes 3.
- Line total is recalculated.
- Cart total changes.

## 64. Test remove item

Remove the mouse.

Expected:
- Mouse disappears.
- Keyboard remains.
- Cart total includes only the keyboard.

## 65. Test clear cart

Click Empty cart.

Expected:
- Cart has no items.
- The page displays Your cart is empty.
- Other session values should not be cleared by this operation.

## 66. Test invalid quantity

Submit:
- 0
- -3
- abc
- empty value

The example converts invalid text to quantity 1 and treats values less than 1 according to the view logic. Review whether this behavior is appropriate for your business requirements.

For a production cart, a form with explicit validation and an error message is preferable.

## 67. Test inactive product

Set a sample product's is_active field to False in the local database.

Try to add it.

Expected:
- The view returns a 404 because the lookup requires an active product.
- The inactive product is not added.

---

# PART 9 — AUTOMATED TESTS

## 68. Add a session cart test

Open catalog/tests.py.

Keep existing tests. Add the class below and merge imports.

~~~python
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Product


class SessionCartTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            sku="TEST-CART-01",
            name="Test Cart Product",
            category="Testing",
            price=Decimal("100.00"),
            stock=10,
            is_active=True,
        )

    def test_product_list_loads(self):
        response = self.client.get(
            reverse("product_list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Cart Product")

    def test_add_product_requires_post(self):
        response = self.client.get(
            reverse("cart_add", args=[self.product.pk])
        )

        self.assertEqual(response.status_code, 405)

    def test_add_product_stores_quantity_in_session(self):
        response = self.client.post(
            reverse("cart_add", args=[self.product.pk]),
            {"quantity": "2"},
        )

        self.assertRedirects(
            response,
            reverse("cart_detail"),
        )

        cart = self.client.session.get("cart")
        self.assertEqual(
            cart[str(self.product.pk)],
            2,
        )

    def test_cart_detail_displays_product(self):
        session = self.client.session
        session["cart"] = {str(self.product.pk): 2}
        session.save()

        response = self.client.get(
            reverse("cart_detail")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Cart Product")
        self.assertContains(response, "200.00")

    def test_remove_product(self):
        session = self.client.session
        session["cart"] = {str(self.product.pk): 2}
        session.save()

        response = self.client.post(
            reverse("cart_remove", args=[self.product.pk])
        )

        self.assertRedirects(
            response,
            reverse("cart_detail"),
        )

        self.assertNotIn(
            str(self.product.pk),
            self.client.session.get("cart", {}),
        )

    def test_clear_cart(self):
        session = self.client.session
        session["cart"] = {str(self.product.pk): 2}
        session["unrelated_preference"] = "en"
        session.save()

        self.client.post(reverse("cart_clear"))

        self.assertEqual(
            self.client.session.get("cart"),
            {},
        )
        self.assertEqual(
            self.client.session.get("unrelated_preference"),
            "en",
        )
~~~

## 69. Run the tests

~~~powershell
python manage.py check
python manage.py test catalog
~~~

The test suite uses Django's test database.

Do not run test setup against production data.

## 70. What if the money assertion differs?

The rendered decimal format can depend on template formatting.

If the test output does not contain the exact string 200.00:
- Inspect the response content.
- Confirm the price is Decimal("100.00").
- Confirm quantity is 2.
- Adjust the assertion to match the intended output format without weakening the business check.

---

# PART 10 — COMMON ERRORS

## 71. request.session attribute error

Check:
- SessionMiddleware exists.
- It appears in MIDDLEWARE.
- django.contrib.sessions is installed.
- Session migrations are applied.
- The view receives a Django HttpRequest.

## 72. Cart disappears on every request

Check:
- Browser accepts cookies.
- The session cookie is sent back.
- SessionMiddleware is enabled.
- You did not clear the session on every request.
- The session expiry has not passed.
- Secure cookie settings are appropriate for local HTTP.

## 73. Nested cart update is not saved

Cause:
- A nested dictionary was mutated without marking the session modified.

Fix:

~~~python
cart = request.session.get("cart", {})
cart["12"] = 3
request.session["cart"] = cart
~~~

Or set request.session.modified = True after the nested update.

## 74. NoReverseMatch for cart route

Check:
- catalog/urls.py exists.
- The route name is spelled correctly.
- catalog.urls is included.
- The correct product_id argument is passed.

## 75. Product DoesNotExist or 404

Check:
- The sample product exists.
- The primary key is correct.
- The product is active.
- The product is in the database used by the current environment.

## 76. TypeError when calculating totals

Check:
- Product.price is Decimal.
- The quantity is an integer.
- The total begins with Decimal("0.00").
- You are not adding a float to a Decimal.

## 77. Cart total is incorrect

Check:
- The view reads current prices from Product.
- The quantity is read from the correct session key.
- The product primary key is converted consistently to string for the session dictionary.
- Inactive or deleted products are handled.
- The line total is price multiplied by quantity.

## 78. CSRF verification failed

Check:
- Every cart POST form contains csrf_token.
- CsrfViewMiddleware is enabled.
- The form submits to the correct same-site URL.

Do not disable CSRF protection.

---

# PART 11 — APPROVED MINI-PROJECT

## 79. Session-Based Shopping Cart

### Business problem

A small online store wants visitors to add products to a cart before signing in or checking out.

### Functional requirements

1. Display active products.
2. Add a product using POST.
3. Store product IDs and quantities in request.session.
4. Display cart items.
5. Calculate line totals from current database prices.
6. Calculate the cart total on the server.
7. Update item quantity.
8. Remove one item.
9. Clear the cart without clearing unrelated session data.
10. Reject or safely handle invalid product IDs.
11. Prevent inactive products from being added.
12. Include CSRF tokens in state-changing forms.
13. Add automated tests.

### Security requirements

- Never trust a submitted price.
- Never store payment card data in the session.
- Never use GET for cart mutations.
- Do not assume a cart is a confirmed order.
- Recheck stock and prices at checkout.
- Use database transactions when converting a cart into an order.

### Acceptance criteria

- [ ] Product list loads.
- [ ] Add item works.
- [ ] Multiple products can be stored.
- [ ] Quantity update works.
- [ ] Remove item works.
- [ ] Clear cart works.
- [ ] Unrelated session data remains.
- [ ] Cart total uses database prices.
- [ ] Inactive products cannot be added.
- [ ] GET cannot mutate cart.
- [ ] Tests pass.
- [ ] Learner explains cookie and session differences.

### Submission evidence

- Updated views and URLs.
- Product list and cart templates.
- Test output.
- Screenshots with fictional product data.
- README with setup and manual test steps.
- Short explanation of why price is not stored as trusted cart data.

---

# PART 12 — SELF-ASSESSMENT

## 80. Short-answer questions

1. Why is HTTP called stateless?
2. What is a cookie?
3. What is a session?
4. What is stored in the browser for a standard database-backed Django session?
5. What does SessionMiddleware do?
6. What does request.session.get() do?
7. How do you remove one session key?
8. What does set_expiry() do?
9. Why should you not store a raw password in a session?
10. Why should the cart store product IDs and quantities?
11. Why should product prices come from the database?
12. Why should cart updates use POST?
13. Why is CSRF protection required?
14. What is the purpose of HttpOnly?
15. What is the purpose of Secure?
16. What does SameSite control?
17. Why should a cart not be treated as an order?
18. Why must stock be checked again at checkout?

## 81. Self-check answers

1. HTTP requests do not automatically remember application state from previous requests.
2. A small value stored by the browser and sent with matching requests.
3. Server-managed state associated with a visitor or browser.
4. Normally a session identifier cookie.
5. It loads and saves session state around request processing.
6. It returns a session value or a default.
7. Use pop() with a default.
8. It sets the session expiry behavior.
9. Session data is not a safe place for credentials.
10. They identify selected products and requested quantities without trusting client prices.
11. Prices can change and client data can be manipulated.
12. Adding, updating and removing cart data changes server state.
13. It helps protect state-changing requests against cross-site request forgery.
14. It prevents ordinary JavaScript from reading the cookie.
15. It sends the cookie only over HTTPS.
16. When cookies are sent in cross-site contexts.
17. A cart is temporary selection state, not a committed transaction.
18. Stock may change after the product was added.

## 82. MCQ assessment

### Question 1
What is the primary purpose of a session?

- A. Store CSS
- B. Maintain state across requests
- C. Compile Python
- D. Create a database table automatically

**Answer: B.** Sessions associate data with a visitor across multiple requests.

### Question 2
In the standard database-backed Django session, what does the browser normally hold?

- A. The complete database
- B. The raw password
- C. A session identifier cookie
- D. The entire product catalog

**Answer: C.** Django uses the identifier to retrieve server-side session data.

### Question 3
Which object is used to read session values in a view?

- A. request.session
- B. request.cookies_table
- C. settings.session
- D. Product.session

**Answer: A.** Django exposes the current session through request.session.

### Question 4
Why should cart price be read from the database?

- A. Database fields are always free
- B. The browser should not be trusted to set the price
- C. It removes the need for stock
- D. It automatically charges a card

**Answer: B.** Server-side price lookup prevents client-submitted prices from becoming authoritative.

### Question 5
Which method is appropriate for removing one session key?

- A. pop()
- B. makemigrations()
- C. authenticate()
- D. order_by()

**Answer: A.** pop() removes one key and can return a default if it is absent.

---

# PART 13 — INTERVIEW PREPARATION

## 83. Explain Django sessions

**Answer:** HTTP is stateless, so a later request does not automatically remember earlier application state. Django sessions associate data with a visitor across requests. In the standard database-backed configuration, Django stores session data server-side and the browser holds a session identifier cookie.

**Follow-up:** Where does a view access the session?

**Answer:** Through request.session.

## 84. What is the difference between a cookie and a session?

**Answer:** A cookie is stored by the browser and sent with matching requests. A session is server-managed state associated with a browser session. In Django's database-backed session setup, the browser usually stores a session identifier rather than the full session data.

**Follow-up:** Is a cookie automatically secret?

**Answer:** No. It is stored by the browser and should be protected with appropriate attributes.

## 85. Why should a cart store product IDs rather than prices?

**Answer:** Prices are business data that must be read from the server's database. A client-controlled value must not decide the amount charged. The session can store product identifiers and quantities; the server recalculates prices and totals.

**Follow-up:** Is the cart total the amount to charge?

**Answer:** Not by itself. Checkout must revalidate price, stock, discounts and taxes.

## 86. What is the purpose of SESSION_COOKIE_SECURE?

**Answer:** It instructs the browser to send the session cookie only over HTTPS. It should be enabled for an HTTPS production deployment.

**Follow-up:** Why might local HTTP testing stop working if it is enabled?

**Answer:** The browser may not send the secure cookie over plain HTTP.

## 87. Scenario: cart disappears after every request

**Answer:** Check whether the browser accepts and sends the session cookie, SessionMiddleware is configured, session migrations are applied, and session expiry or cookie security settings are correct.

## 88. Scenario: nested cart changes do not persist

**Answer:** Django may not detect a mutation inside a nested dictionary. Reassign the modified dictionary to request.session or set request.session.modified = True.

---

# PART 14 — INDEPENDENT COMPLETION

## 89. Draw the session lifecycle

Include:
1. Browser request.
2. Session cookie.
3. SessionMiddleware.
4. Session data lookup.
5. View reads and updates request.session.
6. Middleware saves changes.
7. Browser receives response.

## 90. Controlled debugging exercise

In a local practice environment:
- Temporarily remove SessionMiddleware and inspect the failure.
- Restore it.
- Update a nested cart dictionary without reassignment and inspect the result.
- Fix it by reassigning the dictionary.
- Add an item using GET and observe the 405 response.
- Restore the POST form and test again.

Do not commit intentional mistakes.

## 91. Final checklist

- [ ] I can explain stateless HTTP.
- [ ] I can explain cookies.
- [ ] I can explain Django sessions.
- [ ] I can identify SessionMiddleware.
- [ ] I can read and write request.session.
- [ ] I understand session expiry.
- [ ] I understand cookie security attributes.
- [ ] I built the cart.
- [ ] I stored only product IDs and quantities.
- [ ] I calculated prices using the database.
- [ ] I tested add, update, remove and clear.
- [ ] I used POST and CSRF tokens.
- [ ] I ran automated tests.
- [ ] I completed Session-Based Shopping Cart.

**Next lesson:** Day 50 — Authorization, Permissions and Role-Based Access.

---

## 92. Official references

1. Django sessions: https://docs.djangoproject.com/en/5.2/topics/http/sessions/
2. Django session settings: https://docs.djangoproject.com/en/5.2/ref/settings/
3. Django CSRF protection: https://docs.djangoproject.com/en/5.2/howto/csrf/
4. Django QuerySets: https://docs.djangoproject.com/en/5.2/topics/db/queries/
5. Django testing tools: https://docs.djangoproject.com/en/5.2/topics/testing/tools/

**Version reminder:** This lesson targets Django 5.2.19. Check the existing Product model and project URL configuration before copying the examples. Do not replace earlier working catalog features.
