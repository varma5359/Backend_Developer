# Day 21: Interview Questions — HTTP status codes, headers, request body and response body

**Pathway:** Python Backend Developer (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools

## 1. Core technical questions

### Q1. What is the difference between 401 and 403?
**Answer:**
- 401 indicates missing or invalid authentication credentials; 403 indicates the server refuses the request, including when the authenticated user lacks permission.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A mobile client must distinguish an unauthorized request from a server error.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q2. What does Content-Type mean?
**Answer:**
- It identifies the media type of the representation, such as application/json.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A mobile client must distinguish an unauthorized request from a server error.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q3. What is the main purpose of 200?
**Answer:** Status codes describe outcomes: 2xx success, 3xx redirection, 4xx client-side request errors and 5xx server failures. Headers carry metadata; bodies carry content.

**Follow-up:** What would go wrong if the concept were misunderstood?

### Q4. Which tools are appropriate for this lesson?
**Answer:** Python and VS Code for demonstrations, terminal commands for execution, and HTTP/browser inspection or structured data tools as appropriate.

**Follow-up:** What would change in a deployed Django service?

### Q5. How do you verify the implementation?
**Answer:** Define expected inputs and outputs, run normal and edge cases, inspect actual responses or database state, and document failures.

**Follow-up:** Why is a successful command not always proof of correct business behavior?

## 2. Scenario-based interview questions

### Q6. A mobile client must distinguish an unauthorized request from a server error. What should the developer verify?
**Answer:**
- Define the expected result before implementation.
- Check that the chosen 200 behavior matches the requirement.
- Validate inputs and inspect actual results.
- Record reproducible test evidence.

**Follow-up:** What error case would you test first?

### Q7. A beginner's output differs from the expected result. How do you troubleshoot?
**Answer:**
- Reproduce the issue with the smallest sample.
- Check tool installation, file location and input.
- Inspect exceptions, response status or SQL result.
- Change one variable at a time and rerun.
- Document the fix and regression test.

**Follow-up:** How would you explain the root cause to a non-technical colleague?

## 3. Project and practical questions

### Q8. Explain your HTTP Response Analyzer.
**Answer:**
- I defined the inputs, operations and expected outputs.
- I implemented a small demonstration of http status codes, headers, request body and response body.
- I tested normal and edge cases.
- I captured evidence and documented limitations.
- I did not assume a learning exercise was production-ready.

**Follow-up:** Which part would you improve first for production use?

### Q9. What mistakes should you avoid in this project?
**Answer:**
- Skipping validation.
- Failing to verify observable results.
- Mixing unrelated responsibilities.
- Hardcoding secrets or private data.
- Ignoring error cases.

**Follow-up:** What is one automated test you would add?

## 4. Rapid revision
- **200:** explain its role in http status codes, headers, request body and response body.
- **201:** explain its role in http status codes, headers, request body and response body.
- **400:** explain its role in http status codes, headers, request body and response body.
- **401:** explain its role in http status codes, headers, request body and response body.
- **403:** explain its role in http status codes, headers, request body and response body.
- **404:** explain its role in http status codes, headers, request body and response body.
- **500:** explain its role in http status codes, headers, request body and response body.
- **Content-Type:** explain its role in http status codes, headers, request body and response body.

**Interview preparation tip:** Give a definition, show a small practical example, explain a failure mode, and state how you would verify it.
