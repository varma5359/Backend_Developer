# Day 32: Interview Guide — Django Templates, Template Variables and Template Tags

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 32 notes](day_32_notes.md)  
**Mini-project:** Dynamic Employee Profile Website

## 1. Technical questions with model answers

### Q1. What is a Django template?

**Model answer:** A template is a text file, commonly HTML, that Django renders with context data. It separates page presentation from the Python view logic.

### Q2. What is a context dictionary?

**Model answer:** It maps names to values that a template can access. For example, {'employee': employee} lets the template read employee.full_name.

### Q3. How do you display a variable?

**Model answer:** Use double curly braces, such as {{ employee.full_name }}. Django resolves the expression against the context and applies autoescaping by default.

### Q4. What are template tags?

**Model answer:** Tags use {% %} syntax to control template behavior, such as if, for, url and load. They are not general-purpose Python statements.

### Q5. What is a template filter?

**Model answer:** A filter transforms a value for display, such as {{ name|upper }}. Filters should format presentation, not replace business logic in the view.

### Q6. Why use {% empty %} in a for loop?

**Model answer:** It provides a message or fallback markup when the iterable has no items, improving the empty-state experience.

## 2. Scenario-based interview question

**Scenario:** The view loads successfully but the template displays a blank employee name. What do you inspect?

**Model answer:** Check that the view passes the context key expected by the template, that the template uses the correct attribute name from the Employee model, that the URL points to the intended view and that the record has a value. Inspect the rendered HTML and server log rather than guessing.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Build an employee list template using context variables, a conditional, a loop, an empty state and a filter. Test with at least one employee and with an empty queryset.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Dynamic Employee Profile Website

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
- [ ] I can present Dynamic Employee Profile Website with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.
## Additional technical and scenario questions

### Q5. What is template context?
**Answer:** It is the data made available to a template, usually through a dictionary passed by the view.

### Q6. What does a template filter do?
**Answer:** It transforms a value for display, such as changing case, formatting a date or shortening text.

### Q7. What is the difference between for and if?
**Answer:** for repeats content for each item in a collection. if conditionally displays content based on a value.

### Q8. What does the empty tag do?
**Answer:** It displays fallback content when a for loop has no items.

### Q9. Why use the url template tag?
**Answer:** It generates a URL from a named route and arguments rather than hard-coding a path.

### Q10. What is autoescaping?
**Answer:** Django escapes unsafe characters in template output so untrusted text is not interpreted as HTML or script.

### Q11. Scenario: a variable appears blank.
**Answer:** Check whether the view passes the correct context key and whether the template uses the same spelling.

### Q12. Scenario: user-submitted HTML executes.
**Answer:** Check whether autoescaping was disabled or the safe filter was applied to untrusted content. Render untrusted text safely.

