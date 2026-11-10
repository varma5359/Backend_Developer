# Day 64: Token Authentication and JWT Authentication Concepts

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 5 — REST API Development with Django REST Framework  
**Estimated time:** 2–3 hours | **Level:** Intermediate  
**Prerequisites:** Days 55–65 — DRF serializers, views, routers and permissions  
**Tools:** Python, Django, DRF, Postman, VS Code and terminal  
**Approved mini-project:** JWT Authentication API

> **Security reminder:** Use test accounts and fake tokens. Never paste real API tokens, JWTs, passwords or session cookies into a public repository or screenshot.

## 1. Learning objectives

- Explain token authentication and jwt authentication concepts.
- Configure the relevant DRF component.
- Implement the example step by step.
- Test valid and invalid requests.
- Explain security, privacy and API behavior.
- Complete JWT Authentication API.

## 2. Concept introduction

Token authentication lets a client prove its identity by sending a token with requests. JSON Web Tokens (JWT) are signed tokens containing claims and an expiry. A token is not the user's password. Tokens must be protected, transmitted over HTTPS and given appropriate expiry and rotation/revocation strategies.

## 3. File-by-file implementation

### settings.py — DRF token authentication

```python
INSTALLED_APPS = [
    # ...
    "rest_framework.authtoken",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}
```

### Create a token for a local test user

```python
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
user = User.objects.get(username="api_test_user")
token, created = Token.objects.get_or_create(user=user)
print(token.key)  # Display only in a local test environment
```

### JWT configuration example using Simple JWT

```python
# Install in the virtual environment:
# python -m pip install djangorestframework-simplejwt

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}
```

## 4. Explain the important statements

### settings.py — DRF token authentication

1. `INSTALLED_APPS = [` — Part of the API configuration; explain its effect on the request.
2. `    # ...` — Part of the API configuration; explain its effect on the request.
3. `    "rest_framework.authtoken",` — Part of the API configuration; explain its effect on the request.
4. `]` — Part of the API configuration; explain its effect on the request.
5. ` ` — Part of the API configuration; explain its effect on the request.
6. `REST_FRAMEWORK = {` — Part of the API configuration; explain its effect on the request.
7. `    "DEFAULT_AUTHENTICATION_CLASSES": [` — Configures how API clients are authenticated.
8. `        "rest_framework.authentication.TokenAuthentication",` — Part of the API configuration; explain its effect on the request.
9. `    ],` — Part of the API configuration; explain its effect on the request.
10. `}` — Part of the API configuration; explain its effect on the request.

### Create a token for a local test user

1. `from django.contrib.auth import get_user_model` — Imports DRF, Django or model components.
2. `from rest_framework.authtoken.models import Token` — Imports DRF, Django or model components.
3. ` ` — Part of the API configuration; explain its effect on the request.
4. `User = get_user_model()` — Part of the API configuration; explain its effect on the request.
5. `user = User.objects.get(username="api_test_user")` — Part of the API configuration; explain its effect on the request.
6. `token, created = Token.objects.get_or_create(user=user)` — Part of the API configuration; explain its effect on the request.
7. `print(token.key)  # Display only in a local test environment` — Part of the API configuration; explain its effect on the request.

### JWT configuration example using Simple JWT

1. `# Install in the virtual environment:` — Part of the API configuration; explain its effect on the request.
2. `# python -m pip install djangorestframework-simplejwt` — Part of the API configuration; explain its effect on the request.
3. ` ` — Part of the API configuration; explain its effect on the request.
4. `REST_FRAMEWORK = {` — Part of the API configuration; explain its effect on the request.
5. `    "DEFAULT_AUTHENTICATION_CLASSES": [` — Configures how API clients are authenticated.
6. `        "rest_framework_simplejwt.authentication.JWTAuthentication",` — Part of the API configuration; explain its effect on the request.
7. `    ],` — Part of the API configuration; explain its effect on the request.
8. `}` — Part of the API configuration; explain its effect on the request.

## 5. Important distinctions

| Concept | Meaning |
|---|---|
| Authentication | Establishes who is making the request |
| Token | Credential sent by the client to authenticate |
| JWT | Signed token format with claims and expiry |
| Role | User grouping that represents a set of responsibilities |
| Model permission | Permission for an action on a model |
| Object permission | Permission decision for a specific object |
| Filtering | Restricts records using structured conditions |
| Searching | Matches text across configured fields |
| Ordering | Sorts results |
| Pagination | Splits results into pages |

## 6. Common errors and troubleshooting

| Symptom | What to inspect |
|---|---|
| 401 Unauthorized | Authentication class and Authorization header |
| 403 Forbidden | Permission class, user role and object ownership |
| User sees too many records | get_queryset() scoping |
| Search returns unexpected values | search_fields and query parameter |
| Ordering rejected | ordering_fields allowlist |
| Pagination missing | DEFAULT_PAGINATION_CLASS and page size |
| Token leaked | Revoke/rotate token and remove secret from future exposure |

## 7. Industry scenario

Token authentication lets a client prove its identity by sending a token with requests. JSON Web Tokens (JWT) are signed tokens containing claims and an expiry. A token is not the user's password. Tokens must be protected, transmitted over HTTPS and given appropriate expiry and rotation/revocation strategies.

## 8. Approved mini-project — JWT Authentication API

**Objective:** JWT Authentication API.

### Required tasks

1. Explain what a token represents and why it is used.
2. Configure DRF TokenAuthentication for a local demonstration.
3. Add rest_framework.authtoken to INSTALLED_APPS and migrate.
4. Create a token for a local test user.
5. Send Authorization: Token <key> in a Postman request.
6. Understand JWT structure at a conceptual level: header, payload and signature.
7. Install and configure Simple JWT in a separate test configuration if required.
8. Test missing, invalid and valid tokens.
9. Never expose real tokens in screenshots, logs or Git.

### Suggested structure

```text
projects/day_64/
├── README.md
├── config/
└── application/
    ├── permissions.py
    ├── api_views.py
    ├── serializers.py
    └── tests/
```

### Validation checklist

- [ ] Token authentication is configured.
- [ ] A local test token can be created.
- [ ] Protected endpoint rejects a missing token.
- [ ] Valid token authenticates the test user.
- [ ] Authorization header format is correct.
- [ ] JWT and DRF token authentication differences are understood.

### Postman test matrix

| Request | Expected result |
|---|---|
| Missing/invalid credentials | 401 or configured authentication error |
| Authenticated but no permission | 403 |
| Authorized user | 200/201 as appropriate |
| Search/filter query | Only matching results |
| Unsupported order field | Rejected or ignored according to configuration |
| Page navigation | Correct page metadata and result count |

## 9. AI-assisted implementation

**Planning prompt:** "Help me plan JWT Authentication API. Identify authentication, permission, filtering and test cases. Do not provide real credentials or tokens."

**Guided prompt:** "Guide me through one configuration or permission step. Explain the security effect and wait for my test result."

**Debugging prompt:** "Here is the request method, URL, headers without secrets, response status and relevant code. Diagnose the authentication or permission issue."

**Review prompt:** "Review the API for token handling, queryset scoping, object-level permissions and safe filtering/order fields."

## 10. Five daily MCQs

**Q1. What is the main purpose of today's concept?**  
A. Secure API access or control which records are returned.  
B. Replace Django.  
C. Disable HTTP.  
D. Store tokens in source code.  
**Answer: A.** These features control identity, access and API result size.

**Q2. What should never be committed?**  
A. Public serializer code.  
B. Real access tokens or JWTs.  
C. A test fixture with fake data.  
D. A README.  
**Answer: B.** Tokens are credentials and must be protected.

**Q3. What is object-level permission?**  
A. Sorting all records.  
B. Installing DRF.  
C. Deciding whether a user can access a specific record.  
D. Changing a template.  
**Answer: C.** It evaluates access for an individual object.

**Q4. Why use pagination?**  
A. To return every record at once.  
B. To disable search.  
C. To remove filters.  
D. To limit result size and support page navigation.  
**Answer: D.** Pagination improves usability and resource control.

**Q5. Why explicitly configure ordering_fields?**  
A. To allow only intended sort fields.  
B. To expose every model field.  
C. To remove authentication.  
D. To change database schema.  
**Answer: A.** An allowlist gives predictable API behavior.

## 11. Interview preparation

**Q1. Explain token authentication and jwt authentication concepts.**  
**Answer:** Token authentication lets a client prove its identity by sending a token with requests. JSON Web Tokens (JWT) are signed tokens containing claims and an expiry. A token is not the user's password. Tokens must be protected, transmitted over HTTPS and given appropriate expiry and rotation/revocation strategies.

**Q2. What is one security risk?**  
**Answer:** Explain the risk of leaked tokens, overbroad querysets or missing object-level permissions.

**Q3. How do you verify the implementation?**  
**Answer:** Use test accounts and requests with valid, missing and invalid credentials. Test own and other users' records and verify filter/search/order/page results.

**Follow-up:** Why is queryset scoping important even when object permissions exist?  
**Answer:** Queryset scoping limits which records can be listed or retrieved and reduces the chance of exposing unauthorized objects.

## 12. Completion checklist

- [ ] Explain the concept.
- [ ] Configure the relevant DRF components.
- [ ] Test valid and invalid requests.
- [ ] Verify access and result boundaries.
- [ ] Complete JWT Authentication API.
- [ ] Complete five MCQs.
- [ ] Answer interview questions.
- [ ] Submit safe evidence without secrets.

**Next lesson:** Day 65.
