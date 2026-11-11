# Day 31: Interview Guide — Django Views: Function-Based Views and Request-Response Cycle

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 31 notes](day_31_notes.md)  
**Mini-project:** Dynamic Welcome Application

## 1. Technical questions with model answers

### Q1. What is a Django view?

**Model answer:** A view is a Python callable that receives an HttpRequest and returns an HttpResponse. It contains the request-handling logic for a route.

### Q2. What is HttpRequest?

**Model answer:** It represents the incoming browser request and exposes information such as method, GET data, POST data, headers, path and user.

### Q3. What is HttpResponse?

**Model answer:** It is an HTTP response object returned by a view. It can contain text, HTML or another response body.

### Q4. What does render() do?

**Model answer:** It loads a template, combines it with a context dictionary and returns an HttpResponse containing the rendered output.

### Q5. What is the difference between request.GET and request.POST?

**Model answer:** GET contains query-string values. POST contains submitted form data in a POST request. Both are client-controlled and must be validated.

### Q6. Why should a view not return None?

**Model answer:** Django expects an HTTP response. Returning None causes an error because the request cannot be completed with a valid response.

## 2. Scenario-based interview question

**Scenario:** The /welcome/?name=Asha URL displays the default name instead of Asha. What do you check?

**Model answer:** Inspect request.GET.get('name'), confirm the query parameter is spelled name, ensure the view passes the value in its context dictionary, and ensure the template reads the same context key. Verify the route points to the intended view.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Implement a welcome view, read a query-string value safely with a default, pass it to a template, connect the URL and test both with and without the query parameter.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Dynamic Welcome Application

1. What user or business problem does this project solve?
2. What did you build and what did you deliberately leave out?
3. Which files and commands were required?
4. Explain the execution flow from input to output.
5. What result did you verify?
6. What was the most useful debugging check?
7. What would you improve if this became a production feature?

**Model viva answer structure:** State the requirement → explain the design → identify the files → describe the implementation → show the observed result → explain one limitation or improvement. Use your own project evidence; do not invent results.

## 5. Self-check

- [ ] I can answer all six technical questions without memorizing paragraphs.
- [ ] I can explain the scenario and justify each debugging step.
- [ ] I can demonstrate the feature from a fresh terminal/browser session.
- [ ] I can explain one alternative design and why I did not choose it.
- [ ] I can present Dynamic Welcome Application with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding section in [Day 31 class notes](day_31_notes.md), repeat the steps and record the output.