# Day 53: Interview Guide — Pagination, Search and Filtering in Django Applications

**Related class notes:** [Day 53 notes](day_53_notes.md)  
**Approved mini-project:** Paginated Product Catalog  
**Level:** Beginner to Intermediate

## 1. Core technical questions

### Q1. What is pagination?
**Answer:** Pagination divides a large result set into smaller pages. It reduces the number of records displayed in one response and helps keep pages manageable.

### Q2. What is Django's Paginator?
**Answer:** It is a helper that divides a list or QuerySet into pages and provides page metadata such as total count, page range and previous/next information.

### Q3. What is a Page object?
**Answer:** It represents the selected page and provides the objects for that page along with navigation methods.

### Q4. What is the difference between page() and get_page()?
**Answer:** page() raises exceptions for invalid or out-of-range values. get_page() handles those cases and returns a fallback page.

### Q5. Why should a large QuerySet not be converted to a list before pagination?
**Answer:** Converting it to a list loads all matching records into application memory. Passing the QuerySet directly allows database slicing for the requested page.

### Q6. Why is GET appropriate for search?
**Answer:** Search reads data. GET makes the search URL shareable and bookmarkable and allows the browser to repeat the same query.

### Q7. What does name__icontains mean?
**Answer:** It is a Django ORM lookup that matches a case-insensitive substring in the name field.

### Q8. What is a Q object?
**Answer:** It represents a query condition and supports complex logic such as OR and NOT. For example, search can match product name or SKU.

### Q9. How are multiple filter() keyword conditions combined?
**Answer:** They are normally combined with AND. Q objects can be used to express OR conditions.

### Q10. Why use Decimal for price filters?
**Answer:** Decimal is appropriate for decimal monetary values. Binary floating-point can represent some decimal fractions imprecisely.

### Q11. Why use an allowlist for sorting?
**Answer:** It restricts browser input to known supported ordering choices. Do not pass arbitrary sort expressions from the URL directly into order_by().

### Q12. Why is stable ordering important?
**Answer:** It gives predictable page boundaries. Add a unique tie-breaker such as the primary key when sorting by a non-unique field.

### Q13. Why preserve query parameters in pagination links?
**Answer:** Otherwise the next page may lose the user's search and filters and show a different result set.

### Q14. What is offset-based pagination?
**Answer:** It skips a number of rows and returns the next subset. It is simple but deep offsets can become expensive on very large datasets.

## 2. Debugging questions

### Q15. Page 2 shows all products instead of filtered results.
**Answer:** The pagination link probably includes only the page parameter. Preserve the existing GET parameters and update only page.

### Q16. Invalid price crashes the view.
**Answer:** Parse the value with Decimal inside a try/except for InvalidOperation and show a validation message.

### Q17. User submits an unsupported sort field.
**Answer:** Use an allowlist dictionary and fall back to a safe default.

### Q18. Products move between pages unexpectedly.
**Answer:** Use stable ordering with a unique tie-breaker. Concurrent inserts and updates can still affect offset-based pages.

## 3. Scenario questions

### Q19. A catalog has 500,000 records and page 10,000 is slow.
**Answer:** Measure the query and consider cursor/keyset pagination or another strategy suited to the access pattern. Do not assume changing the template alone will solve it.

### Q20. A user requests 1,000,000 items per page.
**Answer:** Do not trust a client-supplied page size. Use a fixed size or an allowlist of small values.

## 4. Mini-project discussion — Paginated Product Catalog

Demonstrate:
1. Active product QuerySet.
2. Paginator with a fixed page size.
3. Search by name or SKU.
4. Category and price filters.
5. Sort allowlist.
6. Filter preservation in page links.
7. Empty and invalid result behavior.
8. Tests.

## 5. Readiness checklist

- [ ] I can explain Paginator and Page.
- [ ] I can explain GET search parameters.
- [ ] I can use ORM lookups and Q objects.
- [ ] I can validate filters.
- [ ] I can sort using an allowlist.
- [ ] I can preserve filters across pages.
- [ ] I can demonstrate Paginated Product Catalog.

**Related notes:** [Day 53 class notes](day_53_notes.md)
