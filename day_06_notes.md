# Day 6: Loops — for, while, break and continue

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–5; data types, collections basics and conditions  
**Required tools:** Python 3, VS Code, terminal  
**Approved mini-project:** Transaction Processing Simulator

## 1. Learning objectives
- Explain why loops are used.
- Iterate through a sequence with for.
- Repeat work with while.
- Control loops using break and continue.
- Process a small list of transaction records and calculate totals.

## 2. Why loops?
Loops repeat instructions without copying the same code many times.

Backend examples:
- Process a list of order records.
- Validate several input fields.
- Generate reports for many employees.
- Read rows from a file.
- Apply a task to many database records.

## 3. for loop
A for loop iterates over items in a sequence.

```python
employees = ["Asha", "Ravi", "John"]

for employee in employees:
    print(employee)
```

Expected output:
```text
Asha
Ravi
John
```

The variable employee receives one list item during each iteration.

## 4. range()
```python
for number in range(1, 6):
    print(number)
```

Output:
```text
1
2
3
4
5
```

range(1, 6) includes 1 and stops before 6.

## 5. while loop
A while loop repeats while its condition remains true.

```python
count = 1

while count <= 3:
    print("Attempt", count)
    count += 1
```

Output:
```text
Attempt 1
Attempt 2
Attempt 3
```

Always ensure the loop condition eventually becomes false, unless an intentional continuous service loop is required.

## 6. break
break exits the nearest loop immediately.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Output:
```text
1
2
```

## 7. continue
continue skips the rest of the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:
```text
1
2
4
5
```

## 8. Loop through dictionaries
```python
transaction = {
    "transaction_id": 101,
    "amount": 2500,
    "status": "success"
}

for key, value in transaction.items():
    print(key, ":", value)
```

This is useful when inspecting named fields in a record.

## 9. Nested loops
A nested loop is a loop inside another loop.

```python
departments = ["HR", "IT"]
employees = ["Asha", "Ravi"]

for department in departments:
    for employee in employees:
        print(department, employee)
```

Nested loops can be useful for combinations, but large nested loops may be inefficient. Choose a data-processing approach appropriate to the data size.

## 10. Common loop mistakes
- Forgetting to update the while loop variable.
- Creating an infinite loop accidentally.
- Using break when only one iteration should be skipped.
- Using continue when the whole loop should stop.
- Off-by-one errors with range().
- Modifying a collection while iterating over it without a safe plan.

## 11. Industry scenario
A payment reconciliation backend receives a batch of transaction records. It needs to count successful transactions, ignore pending records and stop or flag invalid records according to a defined processing policy.

## 12. Approved mini-project — Transaction Processing Simulator

**Objective:** Process a small in-memory set of transaction records and summarize results.

### Sample data
```python
transactions = [
    {"id": 101, "amount": 2500, "status": "success"},
    {"id": 102, "amount": 1200, "status": "pending"},
    {"id": 103, "amount": 800, "status": "success"},
    {"id": 104, "amount": 500, "status": "failed"}
]
```

### Requirements
1. Loop through each transaction.
2. Print the transaction ID and status.
3. Count successful transactions.
4. Calculate total amount of successful transactions.
5. Count pending and failed transactions separately.
6. Use continue to skip adding non-successful amounts, or explain an equivalent design.
7. Display a final summary.

**Suggested structure**
```text
transaction_processing_simulator/
└── transactions.py
```

### Expected summary for the sample
- Successful transactions: 2
- Successful amount total: 3300
- Pending transactions: 1
- Failed transactions: 1

### Validation
- Add a transaction with zero amount.
- Add a second successful transaction.
- Ensure pending and failed amounts do not enter successful total.
- Confirm the loop processes every record.

## 13. AI-assisted implementation guide
| Level | Prompt |
|---|---|
| 1 — Hint | "Give me one hint to count successful transactions in a loop." |
| 2 — Plan | "Break Transaction Processing Simulator into iteration, classification and summary steps." |
| 3 — Example | "Show a tiny for loop that adds only successful amounts." |
| 4 — Guided implementation | "Help me implement the successful transaction count, then wait." |
| 5 — Explanation | "Explain the difference between break and continue using transactions." |
| 6 — Debugging | "My while loop never ends. Help me inspect the condition and counter update." |
| 7 — Review | "Review my transaction summary against all required sample cases." |

**Planning prompt:** "Help me define loop operations and expected totals for the transaction sample. Do not write the complete implementation."

**Implementation prompt:** "Guide me through processing one transaction record and then generalize the logic."

**Debugging/review prompt:** "Review my loop for skipped records, incorrect totals and infinite-loop risks."

## 14. Daily quiz

**Q1. Which loop iterates through items in a list?**  
A. for  
B. try  
C. class  
D. import  
**Correct: A.** A for loop iterates over sequence items.

**Q2. What is the output of range(1, 4)?**  
A. 1, 2, 3, 4  
B. 1, 2, 3  
C. 0, 1, 2, 3  
D. 4 only  
**Correct: B.** The stop value 4 is excluded.

**Q3. What does break do?**  
A. Skips only the current iteration  
B. Exits the nearest loop  
C. Restarts Python  
D. Converts a value  
**Correct: B.** break stops the nearest enclosing loop.

**Q4. What does continue do?**  
A. Stops the entire program  
B. Skips the current iteration and continues with the next  
C. Exits all functions  
D. Creates an empty list  
**Correct: B.** continue moves directly to the next loop iteration.

**Q5. What is a common cause of an accidental infinite while loop?**  
A. Updating the condition variable correctly  
B. Never changing a variable used in the loop condition  
C. Printing a string  
D. Using a for loop  
**Correct: B.** If the condition never becomes false, the loop can continue indefinitely.

## 15. Interview preparation

### Q1. What is the difference between for and while?
**Answer:** for is commonly used to iterate through a sequence or a known set of items. while repeats as long as a condition is true, often when the number of repetitions depends on runtime state.

**Follow-up:** Which loop would you use to process every record in a list?

### Q2. Explain break and continue.
**Answer:** break exits the nearest enclosing loop. continue skips the remaining statements in the current iteration and moves to the next iteration.

**Follow-up:** What happens if break is used inside a nested loop?

## 16. Completion checklist
- [ ] Use for and range().
- [ ] Use while with a changing condition.
- [ ] Explain break and continue.
- [ ] Process transaction records.
- [ ] Verify transaction counts and totals.
- [ ] Complete Transaction Processing Simulator.

**Next lesson:** Day 7 — Strings, string methods and formatting.
