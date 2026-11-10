# Day 6: Loops — for, while, break and continue

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–5 — data types, conditions and basic collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Transaction Processing Simulator

## 1. Learning objectives

- Explain why loops are used.
- Iterate through sequences using `for`.
- Repeat work using `while`.
- Use `range()` to generate a sequence of numbers.
- Control execution using `break` and `continue`.
- Process transaction records and calculate summary values.

## 2. Why do we need loops?

A loop repeats a block of code. Without loops, you might write the same instruction separately for every employee, order or transaction.

Backend examples:

- Process each record in an imported file.
- Calculate totals for a batch of orders.
- Validate multiple input records.
- Generate a report for many employees.
- Retry an operation a limited number of times.

## 3. for loop

A `for` loop takes items from an iterable one at a time.

```python
employees = ["Asha", "Ravi", "John"]

for employee in employees:
    print(employee)
```

Output:

```text
Asha
Ravi
John
```

During each iteration, `employee` refers to the next item. The loop ends after all items have been processed.

## 4. range()

`range()` generates a sequence of integers, often used when you want to repeat an operation a known number of times.

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

The stop value is excluded. Therefore, `range(1, 6)` produces 1 through 5.

Common forms:

- `range(5)` produces 0, 1, 2, 3, 4.
- `range(2, 6)` produces 2, 3, 4, 5.
- `range(2, 10, 2)` produces 2, 4, 6, 8.

## 5. while loop

A `while` loop repeats as long as its condition remains true.

```python
attempt = 1

while attempt <= 3:
    print("Attempt", attempt)
    attempt += 1
```

Output:

```text
Attempt 1
Attempt 2
Attempt 3
```

The line `attempt += 1` changes the value used by the condition. Without an update, this example would continue indefinitely.

Use `while` when repetition depends on a condition rather than simply visiting each item in a sequence.

## 6. break

`break` exits the nearest enclosing loop immediately.

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

When number becomes 3, the loop stops. The remaining values are not processed.

## 7. continue

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

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

Use `continue` when one record should be skipped but processing should continue with the others.

## 8. Loop through dictionaries

A dictionary represents one record using key-value pairs. Use `.items()` to access both.

```python
transaction = {
    "transaction_id": 101,
    "amount": 2500,
    "status": "success"
}

for key, value in transaction.items():
    print(key, ":", value)
```

Output:

```text
transaction_id : 101
amount : 2500
status : success
```

This is useful for inspecting fields in a record. Later, you will use collections and loops together to process business data.

## 9. Nested loops

A nested loop is a loop inside another loop.

```python
departments = ["HR", "IT"]
employees = ["Asha", "Ravi"]

for department in departments:
    for employee in employees:
        print(department, employee)
```

The inner loop runs fully for each outer-loop value. Nested loops are useful for combinations, but they can perform many operations when collections are large. Choose a more efficient approach when processing large datasets.

## 10. Choosing the right loop

| Requirement | Common choice |
|---|---|
| Process every item in a list | `for` |
| Repeat a known number of times | `for` with `range()` |
| Repeat until a condition changes | `while` |
| Stop processing immediately | `break` |
| Skip one item and continue | `continue` |

## 11. Common mistakes

- Forgetting to update a variable used in a `while` condition.
- Creating an accidental infinite loop.
- Assuming the stop value in `range()` is included.
- Using `break` when only one iteration should be skipped.
- Using `continue` when the entire loop should stop.
- Changing a collection while iterating over it without a safe approach.
- Miscounting records because a counter is updated in the wrong branch.

## 12. Industry scenario

A payment reconciliation process receives a batch of transaction records. It must count successful, pending and failed transactions. Only successful transactions should contribute to the successful payment total.

The loop processes one transaction at a time and applies a consistent rule to each record.

## 13. Approved mini-project — Transaction Processing Simulator

**Objective:** Process a small in-memory list of transaction records and produce a summary.

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

1. Loop through every transaction.
2. Display its ID and status.
3. Count successful transactions.
4. Calculate the amount of successful transactions only.
5. Count pending and failed transactions separately.
6. Use `continue` to skip adding non-successful amounts, or explain an equivalent structure.
7. Display a final summary.

### Expected summary

- Successful transactions: 2
- Successful amount total: 3300
- Pending transactions: 1
- Failed transactions: 1

### Validation

Add another successful transaction and verify that the count and total both change. Add a pending transaction and verify that it does not affect the successful amount total.

## 14. Key takeaways

- A loop repeats code.
- `for` is useful for processing items in an iterable.
- `range()` generates integer sequences; its stop value is excluded.
- `while` repeats while a condition is true.
- `break` exits a loop; `continue` skips the current iteration.
- Always check loop conditions and counters to avoid incorrect results or infinite loops.

**Next lesson:** Day 7 — Strings, string methods and formatting.
