# Day 76: Interview Questions — Caching Concepts and Django Cache Framework

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Related notes:** [Day 76 class notes](day_76_notes.md)  
**Approved mini-project:** Cached Product Catalog API

## Core technical questions

### Q1. Explain caching concepts and django cache framework.
**Answer:** Caching stores the result of expensive work so repeated requests can be served faster. Django provides a cache API and multiple cache backends. Cache keys should include the data context, cached data should have a sensible timeout and updates should invalidate or refresh stale values.

### Q2. Which Django APIs or settings are involved?
**Answer:** config/settings.py — local development cache, profiles/services.py, View cache decorator. Explain their responsibility.

### Q3. What is one common failure?
**Answer:** First request populates the cache. Explain how the behavior is observed and corrected.

### Q4. How do you verify the implementation?
**Answer:** Compare the expected and actual behavior, inspect relevant database/cache/log output and test failure cases.

### Q5. What is one trade-off?
**Answer:** Explain stale cache data, transaction locks or middleware overhead as appropriate.

## Scenario questions

### Q6. A feature works in a small test but performs poorly or becomes inconsistent under load. What do you inspect?
**Suggested answer:** Measure the behavior, inspect cache hit rate/query count/transaction duration/middleware work and identify the actual bottleneck before changing the design.

### Q7. What should never be logged?
**Suggested answer:** Passwords, tokens, authorization headers, private request bodies and unnecessary personal information.

## Project viva — Cached Product Catalog API

1. What problem does it solve?
2. Which Django APIs are used?
3. How did you measure or verify behavior?
4. What failure case did you test?
5. What trade-off did you consider?
6. What would you improve for production?

## Rapid revision

- **1.** Explain cache hit and cache miss.
- **2.** Configure a local memory cache for development.
- **3.** Read a value using cache.get().
- **4.** On a miss, query the database and cache the result.
- **5.** Set an explicit timeout.
- **6.** Invalidate the cache after a product update.
- **7.** Compare behavior before and after cache invalidation.
- **8.** Explain why production may use Redis or another shared cache backend.

## Readiness checklist
- [ ] Explain the concept.
- [ ] Explain the implementation.
- [ ] Demonstrate normal and failure cases.
- [ ] Explain one trade-off.
- [ ] Present Cached Product Catalog API.
