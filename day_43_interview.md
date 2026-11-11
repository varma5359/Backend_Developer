# Day 43: Interview Guide — Advanced Django ORM: Filtering, Searching, Sorting and Selecting Data

**Related class notes:** [Day 43 notes](day_43_notes.md)  
**Approved mini-project:** Advanced Product Search  
**Level:** Beginner to Intermediate

## 1. Core questions

### Q1. What is a QuerySet?
**Answer:** A QuerySet represents a database query and its results. QuerySets are lazy in many common operations, so the database is not necessarily queried when the QuerySet is first constructed.

### Q2. What is the difference between filter() and exclude()?
**Answer:** filter() returns records matching the conditions. exclude() returns records that do not match the conditions.

### Q3. What does get() do?
**Answer:** It retrieves exactly one object. It raises DoesNotExist if no row matches and MultipleObjectsReturned if more than one row matches.

### Q4. What does order_by() do?
**Answer:** It defines the ordering of QuerySet results. A field name sorts ascending; a leading minus sign sorts descending.

### Q5. What does values() return?
**Answer:** It returns dictionaries containing selected field values rather than full model instances. It is useful when only a subset of fields is needed.

### Q6. Explain __icontains.
**Answer:** It performs a case-insensitive substring match on a text field.

### Q7. Explain __gte, __lte and __in.
**Answer:** gte means greater than or equal, lte means less than or equal, and in matches a value contained in a supplied collection.

### Q8. What is a Q object?
**Answer:** Q objects allow complex query conditions, including OR and NOT. They are useful for searching multiple fields.

### Q9. What does QuerySet laziness mean?
**Answer:** Django builds a query representation first and evaluates it when results are needed, such as iteration, list conversion or certain aggregate operations.

### Q10. What is the difference between values() and values_list()?
**Answer:** values() returns dictionaries. values_list() returns tuples or a flat list for a single field when flat=True is used.

## 2. Debugging and scenario questions

### Q11. get() raises DoesNotExist.
**Answer:** No record matches the lookup. Verify the field value and active database. Use filter().first() or get_object_or_404() if the use case allows a missing result.

### Q12. get() raises MultipleObjectsReturned.
**Answer:** The lookup is not unique. Use a unique field or use filter() when multiple records are expected.

### Q13. Search returns unexpected records.
**Answer:** Check the lookup type, whitespace normalization, field name, case behavior and whether conditions are combined with AND or OR.

### Q14. A view runs the same QuerySet repeatedly.
**Answer:** Inspect where it is evaluated and whether the code performs duplicate queries. Reuse evaluated results where appropriate and measure query behavior before optimizing.

### Q15. User supplies an arbitrary sort field.
**Answer:** Validate sort values with an allowlist. Do not let arbitrary browser strings control ORM ordering.

## 3. Practical demonstration

Be prepared to:
1. Filter products by category.
2. Exclude inactive products.
3. Retrieve one product by unique SKU.
4. Search product names case-insensitively.
5. Filter by price range.
6. Sort by price in both directions.
7. Select only required fields.
8. Use Q for name OR SKU search.
9. Explain when the database query executes.

## 4. Readiness checklist

- [ ] I can explain QuerySet laziness.
- [ ] I can distinguish filter, exclude and get.
- [ ] I can use field lookups.
- [ ] I can use order_by, values and values_list.
- [ ] I can use Q objects.
- [ ] I can demonstrate Advanced Product Search.

**Related notes:** [Day 43 class notes](day_43_notes.md)
