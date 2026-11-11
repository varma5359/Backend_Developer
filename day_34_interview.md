# Day 34: Interview Guide — Django Models and Database Field Types

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 3 — Django Fundamentals  
**Related class notes:** [Day 34 notes](day_34_notes.md)  
**Mini-project:** Employee Management Model

## 1. Technical questions with model answers

### Q1. What is a Django model?

**Model answer:** A model is a Python class that subclasses models.Model. Django uses its fields and metadata to map Python objects to database tables and columns.

### Q2. What is the difference between a model instance and a database row?

**Model answer:** A model instance is a Python object representing a record. Saving it persists its field values as a database row.

### Q3. What is a primary key?

**Model answer:** A primary key uniquely identifies a row. Django normally adds an automatic primary-key field when one is not declared.

### Q4. When should you use DecimalField rather than FloatField for money?

**Model answer:** DecimalField stores fixed-precision decimal values using max_digits and decimal_places. Binary floating point can introduce representation rounding, so it is generally unsuitable for exact monetary values.

### Q5. What is the difference between null and blank?

**Model answer:** null controls whether the database column may store NULL. blank controls whether Django validation/forms allow an empty value. They affect different layers.

### Q6. What does unique=True do?

**Model answer:** It asks the database to enforce that no two rows share the same value for that field. Form validation may also surface the constraint before save, but the database remains the final integrity boundary.

## 2. Scenario-based interview question

**Scenario:** An HR system stores salary in a FloatField and sometimes sees rounding differences. What model change would you recommend?

**Model answer:** Use DecimalField with a deliberate max_digits and decimal_places appropriate to the business domain, create a migration and inspect how existing values will be converted. Do not silently change a production schema without a backup and migration plan.

**What the interviewer is checking:** Whether you can connect the concept to a real project, identify the relevant file or command, verify the result and explain the reason for your debugging steps.

## 3. Practical demonstration

Define Employee fields with appropriate types and constraints, explain every field choice, run check, inspect the model and predict which invalid values should be rejected.

Before the interview, be able to:
- Explain the feature without reading the notes.
- Identify the exact file or command involved.
- Demonstrate the behavior in a terminal or browser.
- Predict one result before running the code.
- Explain one common failure and how to fix it.

## 4. Mini-project viva — Employee Management Model

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
- [ ] I can present Employee Management Model with real evidence.

**Readiness rule:** If you cannot reproduce the demonstration, return to the corresponding class notes, repeat the steps and record the output.