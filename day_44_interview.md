# Day 44: Interview Guide — Django ORM Query Optimization: select_related() and prefetch_related()

**Related class notes:** [Day 44 notes](day_44_notes.md)  
**Approved mini-project:** Optimized Order Management System  
**Level:** Intermediate

## 1. Core questions

### Q1. What is the N+1 query problem?
**Answer:** It occurs when an initial query retrieves a set of records and the application then performs another query for each record to retrieve related data. Query count grows with the number of rows.

### Q2. What does select_related() do?
**Answer:** It uses SQL joins to retrieve related objects for single-valued relationships such as ForeignKey and OneToOneField. It can reduce repeated database queries when accessing those related objects.

### Q3. What does prefetch_related() do?
**Answer:** It performs separate queries for related collections and joins the results in Python. It is useful for many-to-many and reverse relationships.

### Q4. What is the key difference between select_related and prefetch_related?
**Answer:** select_related uses SQL joins for single-valued relations. prefetch_related uses additional queries and Python-side joining for collections and other supported relations.

### Q5. Why should you measure queries?
**Answer:** Code that looks shorter is not necessarily faster. Measure query count and response behavior with representative data before and after optimization.

### Q6. What is QuerySet evaluation?
**Answer:** It is when Django executes the database query to retrieve results, such as during iteration or list conversion.

### Q7. Can select_related() be used for a many-to-many relationship?
**Answer:** No. Use prefetch_related() for many-to-many collections.

### Q8. What is a reverse relationship?
**Answer:** It lets code access related records from the other side of a relationship, for example order.items.all() when OrderItem has a ForeignKey to Order and related_name="items".

## 2. Debugging and scenario questions

### Q9. A template runs one query per order item.
**Answer:** Inspect the relationship accessed in the loop. Use prefetch_related() for the collection and select_related() for single-valued relationships within the item query where appropriate.

### Q10. Query count does not improve after adding select_related().
**Answer:** Confirm the related field name, that the template actually uses that relation, and that the QuerySet being rendered is the optimized one. Measure the actual view.

### Q11. A developer adds both methods to every QuerySet.
**Answer:** Optimization should match the relationship access pattern. Unnecessary joins or prefetches can increase work and memory use.

### Q12. A page is slow despite fewer queries.
**Answer:** Query count is only one measure. Inspect query duration, result size, indexes, joins, template work and network/rendering costs.

## 3. Practical demonstration

Be prepared to:
1. Show the unoptimized order list.
2. Identify the N+1 query pattern.
3. Measure query count.
4. Add select_related for order.customer.
5. Add prefetch_related for order.items.
6. Measure again using the same dataset.
7. Explain why each optimization matches the relationship type.

## 4. Readiness checklist

- [ ] I can explain N+1 queries.
- [ ] I can choose select_related versus prefetch_related.
- [ ] I can explain relationship cardinality.
- [ ] I can measure query count.
- [ ] I can explain why fewer queries do not always mean faster response.
- [ ] I can demonstrate Optimized Order Management System.

**Related notes:** [Day 44 class notes](day_44_notes.md)
