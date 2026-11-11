# Python Backend Developer Career Pathway — Lesson Index

**Source roadmap:** [09_Backend_Developer.md](09_Backend_Developer.md)  
**Primary stack:** Python, Django, Django REST Framework and PostgreSQL  
**Duration:** 96 learning days  
**Audience:** Freshers and candidates with 0–1 year of experience

This index tracks the self-paced class notes and interview practice guides. The syllabus file is the authority for the approved topics, projects and phase order.

## Phase 1 — Python Programming Foundations (Days 1–12)

| Day | Approved topic | Class notes | Interview |
|---:|---|---|---|
| 1 | Introduction to backend development, Python and its real-world applications | [Notes](day_01_notes.md) | [Interview](day_01_interview.md) |
| 2 | Python installation, environment setup, interpreter, VS Code and Jupyter basics | [Notes](day_02_notes.md) | [Interview](day_02_interview.md) |
| 3 | Variables, data types, type conversion and operators | [Notes](day_03_notes.md) | [Interview](day_03_interview.md) |
| 4 | Input/output, string formatting and user interaction | [Notes](day_04_notes.md) | [Interview](day_04_interview.md) |
| 5 | Conditional statements and decision-making | [Notes](day_05_notes.md) | [Interview](day_05_interview.md) |
| 6 | Loops: for, while, break and continue | [Notes](day_06_notes.md) | [Interview](day_06_interview.md) |
| 7 | Strings, string methods and formatting | [Notes](day_07_notes.md) | [Interview](day_07_interview.md) |
| 8 | Lists, tuples, sets and dictionaries | [Notes](day_08_notes.md) | [Interview](day_08_interview.md) |
| 9 | Functions, parameters, arguments and return values | [Notes](day_09_notes.md) | [Interview](day_09_interview.md) |
| 10 | Modules, packages and Python imports | [Notes](day_10_notes.md) | [Interview](day_10_interview.md) |
| 11 | File handling: reading, writing and working with CSV and JSON | [Notes](day_11_notes.md) | [Interview](day_11_interview.md) |
| 12 | Exception handling, debugging and basic logging | [Notes](day_12_notes.md) | [Interview](day_12_interview.md) |

**Phase 1 assessment:** Python Employee Management System — see [Day 12 notes](day_12_notes.md).

## Phase 1B — Object-Oriented Programming (Days 13–18)

| Day | Approved topic | Class notes | Interview |
|---:|---|---|---|
| 13 | Introduction to OOP, classes and objects | [Notes](day_13_notes.md) | [Interview](day_13_interview.md) |
| 14 | Constructors, `__init__`, `self` and instance variables | [Notes](day_14_notes.md) | [Interview](day_14_interview.md) |
| 15 | Instance methods, class methods and static methods | [Notes](day_15_notes.md) | [Interview](day_15_interview.md) |
| 16 | Inheritance and method overriding | [Notes](day_16_notes.md) | [Interview](day_16_interview.md) |
| 17 | Encapsulation, abstraction and polymorphism | [Notes](day_17_notes.md) | [Interview](day_17_interview.md) |
| 18 | Complete OOP integration and revision | [Notes](day_18_notes.md) | [Interview](day_18_interview.md) |

**Phase 1B assessment:** Library Management System — see [Day 18 notes](day_18_notes.md).

## Phase 2 — Web Fundamentals, SQL and Development Tools (Days 19–26)

| Day | Approved topic | Class notes | Interview |
|---:|---|---|---|
| 19 | Client-server architecture and how websites work | [Notes](day_19_notes.md) | [Interview](day_19_interview.md) |
| 20 | HTTP, HTTPS, requests, responses and HTTP methods | [Notes](day_20_notes.md) | [Interview](day_20_interview.md) |
| 21 | HTTP status codes, headers, request body and response body | [Notes](day_21_notes.md) | [Interview](day_21_interview.md) |
| 22 | JSON, XML basics and data exchange between applications | [Notes](day_22_notes.md) | [Interview](day_22_interview.md) |
| 23 | Relational database concepts, tables, primary keys and foreign keys | [Notes](day_23_notes.md) | [Interview](day_23_interview.md) |
| 24 | SQL fundamentals: CREATE, INSERT, SELECT, UPDATE and DELETE | [Notes](day_24_notes.md) | [Interview](day_24_interview.md) |
| 25 | SQL filtering, sorting, joins, grouping and aggregate functions | [Notes](day_25_notes.md) | [Interview](day_25_interview.md) |
| 26 | Git, GitHub, repositories, commits, branches and merge basics | [Notes](day_26_notes.md) | [Interview](day_26_interview.md) |

**Phase 2 assessment:** Web-Connected Employee Database Workflow — see [Day 26 notes](day_26_notes.md).

## Class-notes quality revision — Days 13–25 and Django Phase 3

The class-note manuscripts for Days 13–25 have been rewritten as detailed, beginner-first lessons. Each lesson includes concept explanations, worked examples, runnable demonstrations where applicable, code walkthroughs, expected behavior, practical exercises, troubleshooting, mini-project guidance, interview questions and MCQs.

| Day range | Coverage | Class-note status |
|---|---|---|
| 13–18 | OOP foundations and integration | Revised |
| 19–22 | Client-server, HTTP, status codes, JSON and XML | Revised |
| 23–25 | Relational database design and SQL | Revised |

**Important:** This status refers to the class-note manuscripts. The separate interview-guide files have not been quality-rewritten as part of this class-notes revision.

## Django Phase 3 self-learning quality audit

The initial Phase 3 audit and revision log are maintained in [PHASE_3_SELF_LEARNING_AUDIT.md](PHASE_3_SELF_LEARNING_AUDIT.md). The current revision work is on the `phase-3-self-learning-audit` branch. It is not a claim of final mentor-free readiness or runtime validation.

## Django Phase 3 quality revision

Phase 3 (Days 27–41) is undergoing a self-learning quality revision. The initial audit found trainer-dependent wording, inconsistent project examples, weak coverage in Day 38 and code-formatting issues in the forms lessons. Revisions are being applied on the `phase-3-self-learning-audit` branch. Day 38 has been substantially rewritten; Days 27–41 have had self-practice language and targeted continuity fixes applied. The existing Employee model exercises (Days 34–37) and the Student / Department / Course relationship workflow (Days 38–41) are being made explicit within the same `profiles` app.

**Readiness status:** Not yet approved for a mentor-free claim. The integrated project still requires clean-environment runtime verification and a beginner usability test. See [PHASE_3_SELF_LEARNING_AUDIT.md](PHASE_3_SELF_LEARNING_AUDIT.md) for the day-by-day findings and revision log.

## Remaining phases

| Phase | Days | Module | Authoring status |
|---|---:|---|---|
| 3 | 27–41 | Django fundamentals | Revised — class notes, interview guides and cumulative assessment |
| 4 | 42–54 | Django ORM, forms and authentication | Existing files; quality review and revision pending |
| 5 | 55–69 | REST API development with Django REST Framework | Existing files; quality review and revision pending |
| 6 | 70–81 | Advanced backend development | Existing files; quality review and revision pending |
| 7 | 82–88 | Testing, deployment and production readiness | Existing files; quality review and revision pending |
| 8 | 89–96 | End-to-end backend capstone | Not yet authored |

## Authoring conventions

Each completed day should include:
- A beginner-friendly class-notes manuscript with concepts, worked examples, commands, explanations and expected outputs.
- A separate interview guide with direct answers, scenarios and follow-up questions.
- Five day-specific MCQs with explanations.
- An independent mini-project using the approved title.
- An AI-assisted implementation guide.
- A validation and completion checklist.

Use the approved roadmap for exact day titles and project names. A file link in this index means the file exists; it does not imply that future lessons have been authored.
