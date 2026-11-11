# Day 49: Interview Guide — Django Sessions, Cookies and Session Management

**Related class notes:** [Day 49 notes](day_49_notes.md)  
**Approved mini-project:** Session-Based Shopping Cart  
**Level:** Beginner to Intermediate

## How to use this guide
Explain the request lifecycle. Use the cart example to show what belongs in the session and what must come from the database.

## 1. Core technical questions

### Q1. Why is HTTP described as stateless?
**Answer:** Each HTTP request is independent by default. The protocol does not automatically remember application state from earlier requests. Cookies and sessions help an application associate requests with a visitor.

### Q2. What is a cookie?
**Answer:** A cookie is a small value stored by the browser and sent with matching requests according to its domain, path and security attributes.

### Q3. What is a Django session?
**Answer:** A session is server-managed state associated with a visitor or browser. In Django's standard database-backed setup, session data is stored server-side and the browser holds a session identifier cookie.

### Q4. What does SessionMiddleware do?
**Answer:** It loads session state for the request and saves changes as part of response processing. It makes request.session available to views.

### Q5. What is request.session?
**Answer:** It is a dictionary-like interface to the current request's session data. Views can store, read, update and remove values.

### Q6. What does request.session.get() do?
**Answer:** It reads a key and returns a default value if the key is missing. This avoids a KeyError.

### Q7. How do you remove one session key?
**Answer:** Use pop(key, default), for example request.session.pop("cart", None). Use clear() only when the entire session should be cleared.

### Q8. What is session expiry?
**Answer:** It controls how long session data remains valid. Django provides set_expiry() and settings such as SESSION_COOKIE_AGE.

### Q9. What is SESSION_COOKIE_SECURE?
**Answer:** It tells the browser to send the session cookie only over HTTPS. Enabling it on a local plain-HTTP site can make the browser stop sending the cookie.

### Q10. What is SESSION_COOKIE_HTTPONLY?
**Answer:** It prevents ordinary JavaScript from reading the cookie. It reduces some exposure but does not replace other security controls.

### Q11. What does SameSite control?
**Answer:** It controls when the browser sends a cookie in cross-site contexts. The right value depends on the application's authentication and integration flows.

### Q12. Why should a cart store product IDs and quantities rather than prices?
**Answer:** Prices are authoritative business data and must be read from the server-side database. The session stores selected product identifiers and quantities; the server recalculates totals from current Product records.

### Q13. Why should cart changes use POST?
**Answer:** Add, update, remove and clear operations change server state. They should not be triggered by safe GET requests and should include CSRF protection in browser forms.

### Q14. What is the difference between a cart and an order?
**Answer:** A cart is temporary selection state. An order is a persistent business transaction. Checkout must revalidate stock, prices, discounts, taxes and other business rules.

## 2. Debugging questions

### Q15. Cart disappears after every request.
**Answer:** Check browser cookies, SessionMiddleware, session migrations, expiry and secure-cookie settings. Confirm the browser sends the session identifier back.

### Q16. Nested dictionary updates are not saved.
**Answer:** Django may not detect a mutation inside a nested dictionary. Reassign the updated dictionary to request.session or set request.session.modified = True.

### Q17. Cart total is wrong.
**Answer:** Confirm the view reads the current Product price from the database, uses Decimal arithmetic, converts product IDs consistently and uses the correct quantity.

### Q18. A GET request adds a product.
**Answer:** Restrict the view to POST with require_POST and use a POST form containing csrf_token.

## 3. Scenario questions

### Q19. A developer stores card numbers in the session.
**Answer:** Do not store payment card data in a session. Use a compliant payment provider's secure flow and store only appropriate non-sensitive references.

### Q20. A user changes the price value in browser tools.
**Answer:** The server must ignore client-submitted prices and recalculate the amount using trusted database records.

### Q21. Cart data should remain available for months.
**Answer:** A temporary session may not be appropriate. Use a persistent cart model associated with a user, with a clear expiry and privacy policy.

## 4. Mini-project discussion — Session-Based Shopping Cart

Demonstrate:
1. Product list.
2. Add product.
3. Multiple products.
4. Quantity update.
5. Remove product.
6. Clear cart.
7. Cart total from database prices.
8. Invalid/inactive product behavior.
9. Session cookie inspection without revealing its value.

## 5. Readiness checklist

- [ ] I can explain stateless HTTP.
- [ ] I can distinguish cookies and sessions.
- [ ] I can use request.session.
- [ ] I understand expiry and cookie attributes.
- [ ] I can explain safe cart design.
- [ ] I can explain why prices must come from the database.
- [ ] I can demonstrate Session-Based Shopping Cart.

**Related notes:** [Day 49 class notes](day_49_notes.md)
