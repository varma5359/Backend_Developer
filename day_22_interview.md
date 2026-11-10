# Day 22: Interview Questions — JSON, XML basics and data exchange between applications

**Pathway:** Python Backend Developer (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools

## 1. Core technical questions

### Q1. What is serialization?
**Answer:**
- Converting in-memory data into a transferable or storable representation, such as JSON text.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A logistics system exports parcel information to another application.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q2. How do JSON and XML differ?
**Answer:**
- JSON uses object/array syntax and is common in APIs; XML uses tagged elements and attributes and is useful in document-oriented integrations.
- The concept should be demonstrated with observable output.
- In production, verify input validation, error handling and security.

**Example:** A logistics system exports parcel information to another application.

**Follow-up:** How would you test the explanation with a real request, command or query?

### Q3. What is the main purpose of serialization?
**Answer:** JSON represents objects, arrays, strings, numbers, booleans and null. XML represents structured documents with elements and attributes. APIs frequently exchange JSON.

**Follow-up:** What would go wrong if the concept were misunderstood?

### Q4. Which tools are appropriate for this lesson?
**Answer:** Python and VS Code for demonstrations, terminal commands for execution, and HTTP/browser inspection or structured data tools as appropriate.

**Follow-up:** What would change in a deployed Django service?

### Q5. How do you verify the implementation?
**Answer:** Define expected inputs and outputs, run normal and edge cases, inspect actual responses or database state, and document failures.

**Follow-up:** Why is a successful command not always proof of correct business behavior?

## 2. Scenario-based interview questions

### Q6. A logistics system exports parcel information to another application. What should the developer verify?
**Answer:**
- Define the expected result before implementation.
- Check that the chosen serialization behavior matches the requirement.
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

### Q8. Explain your JSON Data Exchange Tool.
**Answer:**
- I defined the inputs, operations and expected outputs.
- I implemented a small demonstration of json, xml basics and data exchange between applications.
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
- **serialization:** explain its role in json, xml basics and data exchange between applications.
- **deserialization:** explain its role in json, xml basics and data exchange between applications.
- **JSON object:** explain its role in json, xml basics and data exchange between applications.
- **JSON array:** explain its role in json, xml basics and data exchange between applications.
- **XML element:** explain its role in json, xml basics and data exchange between applications.
- **schema:** explain its role in json, xml basics and data exchange between applications.

**Interview preparation tip:** Give a definition, show a small practical example, explain a failure mode, and state how you would verify it.
