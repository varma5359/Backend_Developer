# Phase 3 Beginner Usability Pilot

**Purpose:** Determine whether a beginner can complete Django Phase 3 (Days 27–41) using only the TechPhile notes, without verbal instruction.

This is a learner-usability check, not a coding interview and not a test of how quickly someone can memorize Django syntax.

## 1. Who should participate?

Choose 2–3 learners who:
- Know basic Python syntax and have used a terminal/editor.
- Have not previously built a Django project independently.
- Have access to a Windows laptop and can install the course's Python/Django versions.
- Agree to attempt the notes without a trainer explaining the next step.

One learner can reveal obvious blockers; multiple learners provide stronger evidence. Do not describe one successful pilot as proof that every beginner will succeed.

## 2. Pilot rules

1. Give the learner the Phase 3 README, class notes and interview guides.
2. Explain only how to access the files and where to report an issue.
3. Do not explain Django concepts or dictate the next command during the attempt.
4. If the learner asks for help, record the exact question before giving any hint.
5. Ask the learner to use the note's troubleshooting section and compare expected results.
6. Record the exact heading, command, file or code line where the learner became stuck.
7. Do not silently fix the learner's files. Let them make the correction so the notes can be evaluated.
8. Record time and friction, but prioritize successful independent completion over speed.

## 3. Daily observation sheet

Copy one row per learner per day.

| Day | Topic | Started independently? | Finished task independently? | Needed verbal help? | Exact blocker / note section | Revision required |
|---:|---|---|---|---|---|---|
| 27 | Django setup | | | | | |
| 28 | Project and app setup | | | | | |
| 29 | Settings and development server | | | | | |
| 30 | URL routing | | | | | |
| 31 | Views and request/response | | | | | |
| 32 | Templates and template tags | | | | | |
| 33 | Inheritance and static files | | | | | |
| 34 | Models and field types | | | | | |
| 35 | Migrations | | | | | |
| 36 | Django admin | | | | | |
| 37 | ORM and querying | | | | | |
| 38 | Model relationships | | | | | |
| 39 | Forms and ModelForms | | | | | |
| 40 | Validation and CSRF | | | | | |
| 41 | Integrated Student Management Website | | | | | |

Use **Yes / Partially / No**. If verbal help was required, copy the exact question and the hint that was given.

## 4. Capstone acceptance test

The learner should complete these without a trainer telling them what to type:

- [ ] Create and activate the project virtual environment.
- [ ] Install the pinned Django version and confirm the interpreter.
- [ ] Run `python manage.py check`.
- [ ] Generate and apply migrations.
- [ ] Open the home and student-list pages.
- [ ] Open the registration page using GET.
- [ ] Submit an invalid student code and confirm it is rejected.
- [ ] Submit an email containing the normalized full student name and confirm the cross-field rule is displayed.
- [ ] Confirm invalid data is not saved.
- [ ] Submit a valid student and confirm redirect to the list.
- [ ] Confirm the student appears in the list and admin.
- [ ] Demonstrate ForeignKey, OneToOneField and ManyToManyField queries.
- [ ] Explain a student without a profile and handle the missing reverse OneToOne relation.
- [ ] Explain the GET, POST, validation, save and redirect flow.
- [ ] Diagnose one controlled URL, template or migration error using the notes.

## 5. How to classify a blocker

| Severity | Meaning | Required action |
|---|---|---|
| Critical | Learner cannot continue or risks damaging existing project/data | Fix the lesson before the next learner uses it |
| High | Learner can continue only after an unexplained guess or external hint | Add exact steps, expected output and troubleshooting |
| Medium | Learner finishes but spends significant time interpreting ambiguous instructions | Clarify wording, file path or code explanation |
| Low | Minor typo or formatting issue that does not block completion | Correct in the next content pass |

## 6. Pilot completion decision

Do not approve the mentor-free claim until:

- All critical capstone tasks are completed independently by every pilot learner.
- No critical blocker remains in any daily lesson.
- Every high-severity blocker has been corrected and retested.
- Learners can explain the main implementation flow, not merely copy code.
- The updated notes pass the documentation and Django runtime CI checks again.

A successful pilot supports the claim that the pathway is usable independently for the tested learners. Continue collecting feedback after launch; no finite pilot guarantees that every learner will have the same experience.

## 7. Feedback template

For each blocker, record:

- Learner ID or anonymous label:
- Day and lesson heading:
- Exact action attempted:
- Expected result from the notes:
- Actual result:
- Error message or screenshot:
- What the learner tried from the troubleshooting section:
- Hint or external help required:
- Proposed note correction:
- Retest result after correction:
