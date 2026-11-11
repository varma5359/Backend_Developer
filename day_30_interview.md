# Day 30: Interview Guide — URL Routing, Path Converters and URL Patterns

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 30 notes](day_30_notes.md)  
**Mini-project:** Multi-Page Routing Application

## 1. Technical questions with model answers

### Q1. What is URL routing?

**Model answer:** URL routing maps an incoming URL path to a view. Django checks URL patterns in order and calls the matching view.

### Q2. What is path() used for?

**Model answer:** path() defines a route pattern, the view that handles it, optional defaults and a route name.

### Q3. What is a path converter?

**Model answer:** A converter captures part of the URL and converts it to a Python value. For example, int captures an integer and str captures a non-empty string segment.

### Q4. Why use include()?

**Model answer:** It delegates a URL prefix to another URLconf, allowing each app to manage its own routes.

### Q5. Why give a URL a name?

**Model answer:** A named route lets templates and views reverse the route without hardcoding the URL string. This makes route changes safer.

### Q6. What causes a 404?

**Model answer:** No URL pattern matches the requested path, or the view deliberately raises Http404. Check trailing slashes, prefixes, route order and root include configuration.

## 2. Scenario-based interview question

**Scenario:** The /profile/25/ URL returns 404, but the view exists. What do you inspect?

**Model answer:** Check that profiles/urls.py defines the matching pattern, the root config/urls.py includes profiles.urls, the path uses the expected converter and parameter name, and the browser URL matches exactly including prefix and trailing slash.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Create home/about/profile/member routes, connect them to views, include the app URLconf in the root URLconf, test each URL and explain a 404 diagnosis.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Multi-Page Routing Application

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
- [ ] I can present Multi-Page Routing Application with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding section in [Day 30 class notes](day_30_notes.md), repeat the steps and record the output.