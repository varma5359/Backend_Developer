# Phase 3 — Self-Learning Quality Audit

**Pathway:** Python Backend Developer (Django)  
**Scope:** Days 27–41, including class notes and interview guides  
**Audit branch:** `phase-3-self-learning-audit`  
**Baseline commit:** `afab97a0f1011b39816778bff2fee270f1b563fe`  
**Audit status:** Initial content audit; runtime validation is not yet complete.

## 1. Purpose and pass standard

TechPhile Phase 3 is intended to be completed by a beginner without depending on a human mentor. A lesson is not self-learning ready merely because it contains explanations or code. A learner must be able to:

1. Understand the business problem and the concept from a beginner starting point.
2. Identify the exact project folder and file to open or create.
3. Follow commands in the correct order, from the correct terminal location and active environment.
4. Build a complete working example without guessing missing imports, routes, settings or templates.
5. Understand important code lines and why they are needed.
6. Compare their terminal, browser and database results with explicit expected results.
7. Diagnose common errors using actionable steps, not only error names.
8. Complete a guided mini-project and a separate independent challenge.
9. Check their understanding using exercises with answers, hints or a reliable self-check.
10. Explain how today's work carries into the next lesson.

### Rating definitions

- **Pass:** Evidence is explicit, usable and sufficiently complete for an independent beginner.
- **Partial:** The element exists but leaves meaningful gaps, relies on assumptions, or is not sufficiently actionable.
- **Fail:** The element is absent, contradictory, misleading, or likely to block independent progress.
- **Not runtime-verified:** Static review cannot prove that the complete project executes successfully.

## 2. Initial day-by-day audit

This is a content audit of the repository at the baseline commit. It is not a claim that the Django application was executed.

| Day | Topic | Initial rating | Evidence / issue to address |
|---|---|---|---|
| 27 | Django introduction, architecture and installation | **Partial** | Extensive concept coverage and setup material, but the lesson explicitly labels itself trainer-led. Replace trainer dependency with a self-paced route, checkpoints and a learner self-test. |
| 28 | Project/app setup and structure | **Partial / promising** | Exact Windows commands, file map, implementation and verification headings exist. Strengthen the independent completion and troubleshooting path; inspect code against the next lesson's actual state. |
| 29 | Development server and settings | **Partial / promising** | Explains settings and server operation with ordered commands. Make expected browser/terminal observations and configuration safety checks unambiguous. |
| 30 | URL routing and converters | **Partial / promising** | Good file-by-file implementation and URL examples. Add a complete route-to-view verification table and specific failure diagnosis. |
| 31 | Function-based views and request/response | **Partial / promising** | Good request/response concepts and code steps. Ensure expected HTTP/browser results and a separate independent task are explicit. |
| 32 | Templates and template tags | **Partial** | File map, implementation and troubleshooting exist. Verify the page can be reproduced from the prior day's project state and add exact expected page behavior. |
| 33 | Template inheritance and static files | **Partial / promising** | Child-template routes were added and a verification checklist exists. Confirm the exact settings, template names, static paths and browser network checks form one complete path. |
| 34 | Models and field types | **Partial** | Model concepts and an Employee example exist. Explain how this first schema is intentionally extended by the later Student Portal schema and keep migration boundaries clear. |
| 35 | Migrations | **Partial / promising** | Ordered migration commands and explanations exist. Add a more explicit safe workflow for reading migration output and handling existing data without guessing defaults. |
| 36 | Django admin | **Fail — coherence** | The continuous project is labelled Student Portal, but the code and mini-project use Employee / Inventory. Prerequisite text also points to Days 27–37, including future days. Align the lesson to the approved project and its actual point in the sequence. |
| 37 | ORM fundamentals | **Fail — coherence** | Uses Employee and Product Query Explorer while the pathway's continuous project is Student Portal. Prerequisite text includes its own day and later content. Use the existing schema consistently and teach reproducible query output. |
| 38 | Model relationships | **Fail — depth / continuity** | The relationship schema is relevant, but the lesson is compressed compared with neighboring lessons. It needs guided, line-by-line explanation, exact terminal location, migration verification, predictable sample data/output, missing-profile handling and an independent challenge with checks. |
| 39 | Forms and ModelForms | **Partial — self-learning flow** | The GET/POST and ModelForm flow is present. Remove trainer-directed language, fix circular prerequisite wording, separate Python and HTML code blocks, and provide exact invalid/valid submission observations and a self-check. |
| 40 | Validation and CSRF | **Partial — self-learning flow** | Field and form validation are explained. Remove trainer-directed language, fix prerequisite wording, distinguish validation failures from CSRF failures, and show exactly how to test and observe each case. |
| 41 | Complete request-response integration | **Partial — self-learning flow** | A useful end-to-end student list/registration flow exists. Remove trainer-directed language, fix prerequisite wording, make the clean setup/re-run path deterministic, and provide a complete acceptance test and independent extension. |

## 3. Interview-guide audit

The interview guides generally provide core questions, scenario prompts, practical discussion and project-viva questions. They are useful revision material, but several guides contain generic answers that repeat the same debugging and verification advice without teaching the learner how to answer the specific day's technical questions.

The guides also contain trainer-only notes such as asking the learner to predict results. For mentor-free delivery, replace these with a student self-practice instruction and a model answer or self-check rubric. A viva question without an answer key is not fully self-checking.

Priority: revise Days 36–41 interview guides alongside their class notes; then normalize trainer-directed wording and add topic-specific model answers across Days 27–41.

## 4. Revision order

1. **Day 27:** remove trainer-led assumptions; add a self-paced learning contract, checkpoints and a self-test.
2. **Days 36–37:** correct project continuity and prerequisite errors; use the approved Student Portal data model where appropriate.
3. **Day 38:** expand the relationships lesson into a complete beginner walkthrough with outputs, reverse-access examples and an independent build.
4. **Days 39–41:** remove trainer-only instructions, fix prerequisite wording, separate code by language/file, and strengthen validation and end-to-end acceptance tests.
5. **Days 28–35:** perform targeted consistency and verification improvements without changing the approved day sequence.
6. **Interview guides 27–41:** remove mentor-dependent notes and add self-checkable topic-specific answers.

## 5. Project continuity rules

- Preserve the approved Phase 3 order and the existing `config` project / `profiles` app unless a correction is necessary and documented.
- Explain when a lesson extends an existing model and when it introduces a new model.
- Do not silently switch the core project between Employee, Product and Student.
- Keep the Employee model from earlier lessons if it is already part of the student's database; introduce Student, Department, Course and StudentProfile explicitly as the next coherent domain schema.
- Do not instruct learners to delete migration files or reset a database to make a lesson work.
- Make all code blocks copyable into the named file. Use separate Python, HTML and PowerShell blocks.
- For sample database operations, state whether they create new records and how to avoid duplicate unique values when repeating the exercise.

## 6. Evidence and validation limits

- Source review is based on the files in the repository at the baseline commit.
- A GitHub file fetch and static content review do not execute Django.
- The complete project has **not** yet been tested in a clean Windows environment as part of this audit.
- Do not mark a lesson runtime-verified until the commands and browser/database acceptance tests have actually been run.
- A final mentor-free readiness claim requires both the content checklist and a clean-environment execution of the integrated Student Portal workflow.

## 7. Final readiness decision

**Initial decision: Phase 3 is not yet approved for a mentor-free readiness claim.**

The existing notes provide a useful foundation, especially Days 28–35 and the integration work in Days 39–41. However, the inconsistencies and missing self-check support identified above mean TechPhile should not yet promise that a beginner can complete all of Phase 3 independently. Revisions and runtime verification are required before changing that decision.


## 8. Revision work completed on the audit branch

| Area | Revision made | Remaining verification |
|---|---|---|
| Day 27 class notes | Converted trainer-led material to self-paced instructions, added learner checks and corrected Markdown code formatting. | Confirm the setup on a learner's Windows machine. |
| Days 28–35 class notes | Preserved the day sequence and added independent verification and debugging steps. | Beginner usability test. |
| Days 36–37 class notes and guides | Aligned admin and ORM practice to the Employee model, corrected project names and added expected browser/shell results. | Beginner usability test. |
| Day 38 class notes | Rebuilt as a detailed beginner walkthrough for relationship design, migrations, repeatable sample data, forward/reverse queries, troubleshooting and independent practice. | Beginner usability test. |
| Days 39–41 class notes | Corrected prerequisites, separated Python/HTML blocks and aligned the Student registration workflow to the model introduced on Day 38. Fixed Day 40 cross-field validation so names with spaces are compared correctly to email local parts. | Beginner usability test on Windows. |
| Interview guides Days 27–41 | Rewritten with topic-specific model answers, scenario answers, practical demonstrations, project viva questions and learner self-checks. | Review against local employer interview expectations. |
| Documentation quality gate | Added a static audit script and GitHub Actions workflow for required files, balanced code fences, local Markdown links and self-learning sections. | Continue to run on every PR/push. |
| Reference Django project | Added a runnable Django 5.2.19 reference app in `phase3_reference/` with routes, templates, static CSS, Employee and Student models, relationships, forms, admin and CSRF protection. | Run on a learner's Windows environment as part of pilot testing. |
| Runtime test suite | Added **27 automated Django tests** covering routing, templates, static files, models, relationships, admin, form validation, valid/invalid submissions and CSRF. | Extend tests if new lesson requirements are added. |

## 9. Project continuity clarified

The lessons use a deliberate progression of examples:

- Days 27–31: environment, project structure, settings, URL routing and basic views.
- Days 32–33: employee-page template examples for template variables, inheritance and static assets.
- Days 34–37: Employee model, admin registration and ORM queries in the existing `profiles` app.
- Day 38: Student, Department, Course and StudentProfile are introduced as a second domain to teach all three relationship types. The Employee model is retained.
- Days 39–41: Student registration, validation and the integrated Student Management Website use the Student model introduced on Day 38.

The change of domain at Day 38 is explicitly explained in the lesson. Do not remove the Employee model or create duplicate Student models when continuing to Day 41.

## 10. Validation results

**Documentation gate: PASS.** GitHub Actions checked all 15 class-note files and 15 interview guides for required files, balanced Markdown code fences and valid local links.

**Django reference runtime gate: PASS.** GitHub Actions installed Django 5.2.19 on Python 3.12, ran `manage.py check`, generated and applied migrations, verified static-file discovery and ran **27 tests successfully**. See [the successful workflow run](https://github.com/varma5359/Backend_Developer/actions/runs/42971206328).

The tests cover:
- URL routing, integer and string path converters, and query-string handling.
- Template inheritance, template variables, filters, loops and CSS static path generation.
- Employee and Student model behavior.
- ForeignKey, OneToOneField and ManyToManyField in both directions.
- PROTECT and CASCADE deletion behavior.
- Admin model registration and admin login page.
- ModelForm normalization, field validation, cross-field validation and duplicate unique values.
- Valid and invalid registration submissions.
- CSRF rejection without a token and acceptance with a valid token.

**Important scope limit:** the runtime result proves that the checked-in reference project works in the GitHub Linux/Python 3.12 CI environment. It does not prove that every student's local Windows environment is configured correctly or that every student can independently follow the notes.

## 11. Final readiness decision

Phase 3 is **documentation- and reference-runtime-verified**.

Phase 3 is **not yet certified as fully mentor-free** because a real beginner usability test has not been conducted. A learner must complete the daily tasks and capstone using only the notes, without verbal intervention. Every point where the learner gets stuck should be recorded and the relevant lesson revised before TechPhile advertises a guaranteed mentor-free outcome.
