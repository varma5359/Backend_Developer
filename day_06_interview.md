# Day 6: Interview Questions — Loops: for, while, break and continue

**Phase:** 1 — Python Programming Foundations

## 1. Core questions

### Q1. What is a loop?
**Answer:**
- A loop repeats a block of code.
- It reduces duplicate instructions.
- It can process lists, records and repeated tasks.
- Python provides for and while loops.

**Follow-up:** Give an example of a loop in a backend application.

### Q2. Compare for and while.
**Answer:**
- for iterates through a sequence or iterable.
- while repeats while a condition is true.
- for is convenient for processing list items.
- while is useful when repetition depends on a condition.

**Follow-up:** What must you check to avoid an infinite while loop?

### Q3. What does range() do?
**Answer:**
- It produces a sequence of integers.
- It commonly controls a for loop.
- The stop value is excluded.
- It can accept start, stop and step values.

**Follow-up:** What does range(2, 10, 2) produce?

### Q4. What is break?
**Answer:**
- It immediately exits the nearest enclosing loop.
- It is useful when a stopping condition is met.
- It does not automatically exit every outer loop.
- It should be used only when early termination is intended.

**Follow-up:** What happens when break is inside a nested loop?

### Q5. What is continue?
**Answer:**
- It skips the rest of the current iteration.
- The loop proceeds with the next iteration.
- It is useful for ignoring selected records.
- It does not terminate the loop.

**Follow-up:** What is the difference between continue and break?

## 2. Scenario-based questions

### Q6. A transaction loop calculates a total that is too high because failed transactions are included. What do you do?
**Answer:**
- Check each transaction's status before adding its amount.
- Add only records that meet the success rule.
- Count other statuses separately.
- Test with known expected totals.

**Follow-up:** Would you use continue or an if/else structure?

### Q7. A while loop runs forever. What do you inspect?
**Answer:**
- The condition.
- The variable used in the condition.
- Whether the variable is updated.
- Whether the update can actually make the condition false.
- Any continue statement that skips the update.

**Follow-up:** How could you make a loop safe with a maximum attempt count?

## 3. Project questions

### Q8. Explain Transaction Processing Simulator.
**Answer:**
- I iterated through a list of transaction dictionaries.
- I classified each status.
- I counted successful, pending and failed records.
- I added only successful transaction amounts.
- I checked the totals with expected test data.

**Follow-up:** How would you handle an unknown status?

### Q9. How do you test a loop?
**Answer:**
- Test an empty collection.
- Test one item.
- Test multiple items.
- Test boundary values and skipped records.
- Compare actual totals with expected results.

**Follow-up:** Why is an empty-list test important?

## 4. Rapid revision
- for: sequence iteration.
- while: condition-based repetition.
- range: integer sequence.
- break: exit nearest loop.
- continue: skip current iteration.
- Infinite loop: loop condition never becomes false.
- Nested loop: loop inside another loop.
