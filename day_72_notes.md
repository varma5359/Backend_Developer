# Day 72: Third-Party API Integration and Consuming External APIs

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 6 — Advanced Backend Development  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 27–69 — Django, ORM, forms, authentication and REST APIs  
**Tools:** Python, Django, VS Code, terminal and local test data  
**Approved mini-project:** Weather Information Backend

> **Trainer guidance:** Treat external files, email addresses and API responses as untrusted input. Use local test data and fake credentials. Explain configuration and failure handling before connecting a real external service.

## 1. Learning objectives

- Explain third-party api integration and consuming external apis.
- Identify the Django files, settings and libraries involved.
- Implement the example step by step.
- Handle invalid input and external failures.
- Explain the security and reliability considerations.
- Complete Weather Information Backend.

## 2. Concept introduction

A backend may consume an external API to retrieve data from another service. The integration should define timeouts, check HTTP status, validate the response shape, handle network failures and protect API keys. Never trust a third-party response or let an external service hang a web request indefinitely.

## 3. File-by-file implementation

### services/weather_client.py

```python
import os
import requests

def get_weather(city):
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("WEATHER_API_KEY is not configured")

    response = requests.get(
        "https://api.example.test/weather",
        params={"city": city, "key": api_key},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    return {
        "city": data["city"],
        "temperature": data["temperature"],
        "condition": data["condition"],
    }
```

### Example view

```python
from django.http import JsonResponse
from requests.exceptions import RequestException
from services.weather_client import get_weather

def weather_view(request):
    city = request.GET.get("city", "Hyderabad")
    try:
        result = get_weather(city)
    except (RequestException, KeyError, RuntimeError):
        return JsonResponse(
            {"error": "Weather service is temporarily unavailable"},
            status=502,
        )
    return JsonResponse(result)
```

## 4. Explain the important statements

### services/weather_client.py

1. `import os` — Part of the example; explain how it supports the complete workflow.
2. `import requests` — Part of the example; explain how it supports the complete workflow.
3. ` ` — Part of the example; explain how it supports the complete workflow.
4. `def get_weather(city):` — Defines a reusable service or view function.
5. `    api_key = os.environ.get("WEATHER_API_KEY")` — Part of the example; explain how it supports the complete workflow.
6. `    if not api_key:` — Part of the example; explain how it supports the complete workflow.
7. `        raise RuntimeError("WEATHER_API_KEY is not configured")` — Part of the example; explain how it supports the complete workflow.
8. ` ` — Part of the example; explain how it supports the complete workflow.
9. `    response = requests.get(` — Sends an HTTP request to an external service.
10. `        "https://api.example.test/weather",` — Part of the example; explain how it supports the complete workflow.
11. `        params={"city": city, "key": api_key},` — Part of the example; explain how it supports the complete workflow.
12. `        timeout=10,` — Limits how long the external request waits.
13. `    )` — Part of the example; explain how it supports the complete workflow.
14. `    response.raise_for_status()` — Raises an exception for unsuccessful HTTP status codes.
15. `    data = response.json()` — Part of the example; explain how it supports the complete workflow.
16. ` ` — Part of the example; explain how it supports the complete workflow.
17. `    return {` — Part of the example; explain how it supports the complete workflow.
18. `        "city": data["city"],` — Part of the example; explain how it supports the complete workflow.
19. `        "temperature": data["temperature"],` — Part of the example; explain how it supports the complete workflow.
20. `        "condition": data["condition"],` — Part of the example; explain how it supports the complete workflow.
21. `    }` — Part of the example; explain how it supports the complete workflow.

### Example view

1. `from django.http import JsonResponse` — Imports Django, Python or external library functionality.
2. `from requests.exceptions import RequestException` — Imports Django, Python or external library functionality.
3. `from services.weather_client import get_weather` — Imports Django, Python or external library functionality.
4. ` ` — Part of the example; explain how it supports the complete workflow.
5. `def weather_view(request):` — Defines a reusable service or view function.
6. `    city = request.GET.get("city", "Hyderabad")` — Part of the example; explain how it supports the complete workflow.
7. `    try:` — Part of the example; explain how it supports the complete workflow.
8. `        result = get_weather(city)` — Part of the example; explain how it supports the complete workflow.
9. `    except (RequestException, KeyError, RuntimeError):` — Part of the example; explain how it supports the complete workflow.
10. `        return JsonResponse(` — Part of the example; explain how it supports the complete workflow.
11. `            {"error": "Weather service is temporarily unavailable"},` — Part of the example; explain how it supports the complete workflow.
12. `            status=502,` — Part of the example; explain how it supports the complete workflow.
13. `        )` — Part of the example; explain how it supports the complete workflow.
14. `    return JsonResponse(result)` — Part of the example; explain how it supports the complete workflow.

## 5. Reliability and security checklist

- Validate file size and allowed content types.
- Do not trust file extensions alone.
- Use generated or sanitized filenames.
- Restrict access to private uploads.
- Configure email and API credentials outside source control.
- Set timeouts for external HTTP requests.
- Handle network and service errors.
- Avoid logging passwords, tokens, private file contents or unnecessary personal data.

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| Uploaded file is empty | Form enctype and request.FILES |
| File path not saved | MEDIA_ROOT, storage backend and model field |
| Email not visible | EMAIL_BACKEND and console output |
| Email provider rejects message | Sender/recipient configuration and provider response |
| External API times out | Timeout setting and service availability |
| 401 from external API | Credential configuration and API permissions |
| JSON key missing | Response schema and defensive validation |
| External service returns 5xx | Retry policy, fallback and user-facing error |

## 7. Industry scenario

A backend may consume an external API to retrieve data from another service. The integration should define timeouts, check HTTP status, validate the response shape, handle network failures and protect API keys. Never trust a third-party response or let an external service hang a web request indefinitely.

## 8. Approved mini-project — Weather Information Backend

**Objective:** Weather Information Backend.

### Required tasks

1. Choose an external API and read its documentation.
2. Install requests in the active environment.
3. Store the API key in an environment variable.
4. Set a request timeout.
5. Check HTTP status using raise_for_status().
6. Parse JSON and validate required fields.
7. Handle network, status and parsing failures.
8. Return a controlled response to the frontend.
9. Test with a mocked response rather than relying only on a live service.

### Suggested structure

```text
projects/day_72/
├── README.md
├── config/
├── services/
└── application/
    ├── models.py
    ├── forms.py
    └── views.py
```

### Validation checklist

- [ ] API key is read from environment configuration.
- [ ] Request has a timeout.
- [ ] HTTP errors are handled.
- [ ] JSON fields are checked before use.
- [ ] Failure returns a controlled response.
- [ ] Secrets are not logged or committed.

### Submission evidence

- Source files and configuration examples.
- Test output using local sample data.
- Error-handling evidence.
- README with setup and environment variable names.
- No real credentials, private files or customer data.

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan Weather Information Backend. List components, settings, failure cases, security checks and tests. Do not include real credentials."

**Guided prompt:** "Guide me through one file at a time. Explain the configuration and wait for my test output."

**Debugging prompt:** "Here is my code, sanitized response and error message. Identify the cause without asking for API keys or private data."

**Review prompt:** "Review the workflow for input validation, timeouts, secret handling, error responses and safe storage."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Connect a Django backend to files, email or external services safely.  
B. Replace the database.  
C. Disable validation.  
D. Store secrets in Git.  
**Answer: A.** Backend integrations need reliable and secure handling.

**Q2. What should be used for an external HTTP request?**  
A. No timeout.  
B. A reasonable timeout and error handling.  
C. A hardcoded secret.  
D. An infinite retry loop.  
**Answer: B.** Timeouts prevent requests from waiting indefinitely.

**Q3. Where should private API keys be stored?**  
A. Public README.  
B. HTML form.  
C. Protected environment configuration or secret manager.  
D. Git commit message.  
**Answer: C.** Keep secrets outside source control.

**Q4. What should happen when an external service fails?**  
A. Return raw traceback to the user.  
B. Ignore the failure.  
C. Pretend the response is successful.  
D. Handle the error and return a controlled response.  
**Answer: D.** Do not expose internal details.

**Q5. What is the strongest evidence of completion?**  
A. Normal and failure cases are tested and documented.  
B. A project title only.  
C. A copied code snippet.  
D. A screenshot of an editor.  
**Answer: A.** Verify the integration and its failure behavior.

## 11. Interview preparation

**Q1. Explain third-party api integration and consuming external apis.**  
**Answer:** A backend may consume an external API to retrieve data from another service. The integration should define timeouts, check HTTP status, validate the response shape, handle network failures and protect API keys. Never trust a third-party response or let an external service hang a web request indefinitely.

**Q2. What is one reliability concern?**  
**Answer:** Explain timeouts, validation, delivery failure, file restrictions or secret handling as appropriate.

**Q3. How do you test the integration?**  
**Answer:** Use mocked responses or local test backends, exercise success and failure cases and verify the resulting database or HTTP response.

**Follow-up:** Why should you not rely only on a live external API test?  
**Answer:** External services can be unavailable or change behavior. Mocked tests make application behavior repeatable.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Implement the example.
- [ ] Test valid and invalid cases.
- [ ] Verify error handling.
- [ ] Complete Weather Information Backend.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit source, README and safe evidence.

**Next lesson:** Day 73.
