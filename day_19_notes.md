# Day 19: Client-server architecture and how websites work

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 2 — Web Fundamentals, SQL and Development Tools  
**Time:** 2–3 hours | **Level:** Beginner  
**Prerequisites:** Python foundations (Days 1–12)  
**Tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Client-Server Communication Simulator

## 1. Learning objectives
1. Define the central terms of client-server architecture and how websites work.
2. Explain how this concept supports backend applications.
3. Run and interpret a working example.
4. Diagnose a common mistake or failure.
5. Apply the concept in **Client-Server Communication Simulator**.

## 2. Concept and motivation
A client sends a request; a server processes it and returns a response. DNS resolves a domain to an address; a browser then connects to the service.

**Why it matters:** Backend developers must reason about communication, data, and reproducible software changes. A correct implementation should produce observable evidence rather than rely on assumptions.

**Key vocabulary:** `client`, `server`, `DNS`, `IP address`, `port`, `request-response`.

## 3. How it works
Browser → DNS lookup → network connection → HTTP request → server logic → HTTP response → browser rendering.

**Use it when:** You need the relevant behavior in a web or data workflow. **Avoid:** Treating a successful example as proof that production concerns (authentication, error handling, scalability or concurrent use) are solved.

## 4. Step-by-step practical demonstration
Create a new folder named `day_19` in VS Code. Save this example in `demo.py`.

Run the code below in Python:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello from the backend")

HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
```

**How to run:** python server.py

**Expected result:**
```text
Open http://127.0.0.1:8000 → Hello from the backend
```

**Code walkthrough:**
- Import statements load standard-library functionality.\n- Variables hold the input or intermediate data.\n- The processing statements implement the day's core concept.\n- print or the browser displays observable results.\n- Inspect each result before changing the example.

## 5. Industry scenario
An online shopping website loads product information from a backend. The developer should define the expected result, check failures, and communicate the outcome clearly to other team members.

## 6. Common mistakes and troubleshooting
| Problem | Check |
|---|---|
| Command or script fails | Verify interpreter/tool installation and current folder |
| Output differs | Inspect inputs, spelling, syntax and assumptions |
| Operation succeeds unexpectedly | Verify status, affected rows or actual saved state |
| Invalid or untrusted input | Validate before processing; never trust client data |
| Security concern | Use HTTPS for remote communication, parameterized SQL, and no secrets in source control |

## 7. Independent mini-project — Client-Server Communication Simulator

**Goal:** Demonstrate client-server architecture and how websites work with a small, testable application or workflow. **Estimated project time:** 30–75 minutes.

**Required deliverables:**
1. Write a short problem statement and input/output specification.
2. Create the project in `projects/day_19/`.
3. Implement the day's main concept using the demonstration as a reference, not a copied full project.
4. Include at least three realistic sample inputs or actions.
5. Capture terminal/browser/database evidence.
6. Write a short README with setup, run commands and limitations.

**Suggested structure:**
```text
projects/day_19/
├── README.md
├── main.py
└── evidence/
```

**Validation checklist:**
1. Open the local URL and verify the text.
2. Change the response message and reload.
3. Stop the server and observe the browser connection error.

**Security and reliability:** Do not commit credentials, personal information or production secrets. Use local test data and handle errors explicitly.

**Optional extension:** Add one additional edge case and document how the implementation responds.

**Submission:** Source code or command transcript, README, sample outputs, test results and a short explanation of the result.

## 8. AI-assisted learning guide
| Level | Ask the AI mentor |
|---|---|
| Hint | Give one hint for Client-Server Communication Simulator; don't solve it |
| Plan | Break the project into input, process, output and tests |
| Example | Explain a tiny example of client |
| Guided implementation | Help me implement only the first step, then wait |
| Explanation | Explain the demonstration line by line |
| Debugging | Analyze my exact error message and propose a minimal fix |
| Review | Check my implementation against the validation checklist |

**Planning prompt:** "Help me plan Client-Server Communication Simulator with requirements, sample inputs and test cases. Do not write the complete solution."

**Implementation prompt:** "Guide me through one step at a time. Explain each command or line before continuing."

**Debugging/review prompt:** "Review my output, identify the root cause of any failure and explain how to verify the correction."

## 9. Daily MCQs
**Q1. Which statement best describes client?**  
A. A client sends a request; a server processes it and returns a response.  
B. It is only a Python variable  
C. It always requires Django  
D. It replaces all validation  
**Answer: A.** A client sends a request; a server processes it and returns a response. — this is the appropriate choice for the stated scenario.

**Q2. What is the most useful evidence that Client-Server Communication Simulator works?**  
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
### Q1. What is a client-server architecture?
**Answer:** The client requests a resource or operation; the server receives, processes and responds. A browser and web backend are common examples.

**Practical example:** An online shopping website loads product information from a backend.

**Follow-up:** How would you verify this behavior in a real backend application?

### Q2. What does DNS do?
**Answer:** DNS resolves a hostname to network address records; it does not itself serve the webpage.

**Practical example:** An online shopping website loads product information from a backend.

**Follow-up:** How would you verify this behavior in a real backend application?

## 11. Completion checklist
- [ ] Explain the core terminology without notes.
- [ ] Run the demonstration and verify output.
- [ ] Explain important statements or commands.
- [ ] Complete Client-Server Communication Simulator.
- [ ] Validate at least three cases.
- [ ] Answer five MCQs and two interview questions.
- [ ] Submit source, README and evidence.

**Next lesson:** Day 14.
