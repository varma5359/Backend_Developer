# Day 20: HTTP, HTTPS, requests, responses and HTTP methods

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations (Days 1–12), Day 13  
**Tools:** Python 3, VS Code, terminal  
**Approved mini-project:** HTTP Request Explorer

## 1. Learning objectives
1. Define the central terms of http, https, requests, responses and http methods.
2. Explain how this concept supports backend applications.
3. Run and interpret a working example.
4. Diagnose a common mistake or failure.
5. Apply the concept in **HTTP Request Explorer**.

## 2. Concept and motivation
HTTP defines request/response messages. HTTPS is HTTP protected in transit by TLS. GET reads; POST submits; PUT replaces; PATCH partially updates; DELETE removes a resource according to API semantics.

**Why it matters:** Backend developers must reason about communication, data, and reproducible software changes. A correct implementation should produce observable evidence rather than rely on assumptions.

**Key vocabulary:** `HTTP`, `HTTPS`, `TLS`, `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

## 3. How it works
Input or request → validation/processing → result → inspection and verification.

**Use it when:** You need the relevant behavior in a web or data workflow. **Avoid:** Treating a successful example as proof that production concerns (authentication, error handling, scalability or concurrent use) are solved.

## 4. Step-by-step practical demonstration
Create a new folder named `day_20` in VS Code. Save this example in `demo.py`.

Run the code below in Python:

```python
import urllib.request

request = urllib.request.Request(
    "https://httpbin.org/get",
    method="GET",
    headers={"Accept": "application/json"}
)
with urllib.request.urlopen(request, timeout=10) as response:
    print("Status:", response.status)
    print("Type:", response.headers.get("Content-Type"))
```

**How to run:** python explore_http.py (requires internet access)

**Expected result:**
```text
Status: 200; Type: application/json (when service is available)
```

**Code walkthrough:**
- urllib.request.Request defines the URL, HTTP method and headers.\n- urlopen sends the request and waits for a response.\n- response.status is the HTTP status; headers carry response metadata.\n- A network or service failure can raise an exception.

## 5. Industry scenario
A frontend fetches products and submits a new order through an API. The developer should define the expected result, check failures, and communicate the outcome clearly to other team members.

## 6. Common mistakes and troubleshooting
| Problem | Check |
|---|---|
| Command or script fails | Verify interpreter/tool installation and current folder |
| Output differs | Inspect inputs, spelling, syntax and assumptions |
| Operation succeeds unexpectedly | Verify status, affected rows or actual saved state |
| Invalid or untrusted input | Validate before processing; never trust client data |
| Security concern | Use HTTPS for remote communication, parameterized SQL, and no secrets in source control |

## 7. Independent mini-project — HTTP Request Explorer

**Goal:** Demonstrate http, https, requests, responses and http methods with a small, testable application or workflow. **Estimated project time:** 30–75 minutes.

**Required deliverables:**
1. Write a short problem statement and input/output specification.
2. Create the project in `projects/day_20/`.
3. Implement the day's main concept using the demonstration as a reference, not a copied full project.
4. Include at least three realistic sample inputs or actions.
5. Capture terminal/browser/database evidence.
6. Write a short README with setup, run commands and limitations.

**Suggested structure:**
```text
projects/day_20/
├── README.md
├── main.py
└── evidence/
```

**Validation checklist:**
1. Inspect GET request and response.
2. Compare HTTP and HTTPS URL schemes.
3. Explain which method suits creating a record.

**Security and reliability:** Do not commit credentials, personal information or production secrets. Use local test data and handle errors explicitly.

**Optional extension:** Add one additional edge case and document how the implementation responds.

**Submission:** Source code or command transcript, README, sample outputs, test results and a short explanation of the result.

## 8. AI-assisted learning guide
| Level | Ask the AI mentor |
|---|---|
| Hint | Give one hint for HTTP Request Explorer; don't solve it |
| Plan | Break the project into input, process, output and tests |
| Example | Explain a tiny example of HTTP |
| Guided implementation | Help me implement only the first step, then wait |
| Explanation | Explain the demonstration line by line |
| Debugging | Analyze my exact error message and propose a minimal fix |
| Review | Check my implementation against the validation checklist |

**Planning prompt:** "Help me plan HTTP Request Explorer with requirements, sample inputs and test cases. Do not write the complete solution."

**Implementation prompt:** "Guide me through one step at a time. Explain each command or line before continuing."

**Debugging/review prompt:** "Review my output, identify the root cause of any failure and explain how to verify the correction."

## 9. Daily MCQs
**Q1. Which statement best describes HTTP?**  
A. HTTP defines request/response messages.  
B. It is only a Python variable  
C. It always requires Django  
D. It replaces all validation  
**Answer: A.** HTTP defines request/response messages. — this is the appropriate choice for the stated scenario.

**Q2. What is the most useful evidence that HTTP Request Explorer works?**  
A. A project name  
B. Observed output matching documented test cases  
C. A screenshot of the editor alone  
D. A file with no executable code  
**Answer: B.** Observed output matching documented test cases — this is the appropriate choice for the stated scenario.

**Q3. What should you do when the demonstration produces unexpected output?**  
A. Ignore it  
B. Copy another project  
C. Inspect inputs, errors and assumptions  
D. Delete the repository  
**Answer: C.** Inspect inputs, errors and assumptions — this is the appropriate choice for the stated scenario.

**Q4. Which practice is safest for backend development?**  
A. Trust all client input  
B. Store secrets in Git  
C. Skip validation  
D. Validate input and avoid exposing secrets  
**Answer: D.** Validate input and avoid exposing secrets — this is the appropriate choice for the stated scenario.

**Q5. What should the project README contain?**  
A. Setup, execution and validation instructions  
B. Only the student's name  
C. Only a picture  
D. No technical details  
**Answer: A.** Setup, execution and validation instructions — this is the appropriate choice for the stated scenario.

## 10. Interview practice
### Q1. How does HTTPS differ from HTTP?
**Answer:** HTTPS uses TLS to protect HTTP communication in transit, including confidentiality and integrity.

**Practical example:** A frontend fetches products and submits a new order through an API.

**Follow-up:** How would you verify this behavior in a real backend application?

### Q2. How do PUT and PATCH differ?
**Answer:** PUT generally replaces the target resource representation; PATCH applies a partial modification. Actual behavior is defined by the API.

**Practical example:** A frontend fetches products and submits a new order through an API.

**Follow-up:** How would you verify this behavior in a real backend application?

## 11. Completion checklist
- [ ] Explain the core terminology without notes.
- [ ] Run the demonstration and verify output.
- [ ] Explain important statements or commands.
- [ ] Complete HTTP Request Explorer.
- [ ] Validate at least three cases.
- [ ] Answer five MCQs and two interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 15.
