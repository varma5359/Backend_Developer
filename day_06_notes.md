# Day 6: Loops — for, while, break and continue

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1 — Python Programming Foundations  
**Estimated time:** 2–3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Days 1–5 — variables, conditions and basic collections  
**Required tools:** Python 3, VS Code and terminal  
**Approved mini-project:** Transaction Processing Simulator

> **Beginner note:** Imagine that a company has 500 orders. Should a developer write the same calculation 500 times? No. A loop lets Python repeat instructions. Today you will learn how to control that repetition.

## 1. Learning objectives

You should be able to:
- Explain why loops are needed.
- Use a for loop to process each item.
- Use range() to repeat a known number of times.
- Use a while loop when repetition depends on a condition.
- Control loops using break and continue.
- Calculate simple totals and counts from records.

## 2. What is a loop?

A loop repeats a block of code. Without loops, you may need to write the same statement again and again.

Without a loop:
```python
print("Asha")
print("Ravi")
print("Meera")
```

With a loop:
```python
students = ["Asha", "Ravi", "Meera"]

for student in students:
    print(student)
```

Output:
```text
Asha
Ravi
Meera
```

The loop takes one student name at a time and runs the indented statement. This is called an **iteration**. One pass through the loop is one iteration.

## 3. The for loop

A for loop is useful when you want to process each item in a collection or sequence.

Syntax:
```python
for variable in sequence:
    statements
```

Beginner example:
```python
fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:
```text
Apple
Mango
Orange
```

Understand each part:
- `fruits` is a list containing three items.
- `for` starts the loop.
- `fruit` is the loop variable.
- `in` means Python takes values from the collection.
- The indented print statement runs once for every item.

First iteration: fruit is Apple.  
Second iteration: fruit is Mango.  
Third iteration: fruit is Orange.  
After all three items are processed, the loop finishes.

## 4. Use range() to repeat a known number of times

The built-in `range()` function produces a sequence of integers. It is commonly used with for loops.

### Example 1: range(5)

```python
for number in range(5):
    print(number)
```

Output:
```text
0
1
2
3
4
```

Why does it stop at 4? The stop value is excluded. `range(5)` starts at zero and produces five values: 0 through 4.

### Example 2: range(start, stop)

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

The start value 1 is included; the stop value 6 is excluded.

### Example 3: range(start, stop, step)

```python
for number in range(2, 11, 2):
    print(number)
```

Output:
```text
2
4
6
8
10
```

The third argument is the step. Here Python increases the number by 2 each time.

Remember:
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

## 5. Add numbers using a loop

Suppose you want to calculate the total of five amounts.

```python
amounts = [100, 200, 150, 50, 300]
total = 0

for amount in amounts:
    total = total + amount

print("Total:", total)
```

Output:
```text
Total: 800
```

Understand the variable `total`:
- Initially total is 0.
- First amount 100: total becomes 100.
- Next amount 200: total becomes 300.
- Next amount 150: total becomes 450.
- Next amount 50: total becomes 500.
- Last amount 300: total becomes 800.

This pattern is called an **accumulator**: a variable that collects a running result.

## 6. Count matching items

You can use a counter variable to count how many records meet a condition.

```python
statuses = ["success", "failed", "success", "pending", "success"]
success_count = 0

for status in statuses:
    if status == "success":
        success_count = success_count + 1

print("Successful transactions:", success_count)
```

Output: `Successful transactions: 3`

The counter increases only when the condition is true.

## 7. The while loop

A while loop repeats as long as its condition is true.

Syntax:
```python
while condition:
    statements
```

Beginner example:
```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Output:
```text
1
2
3
```

Read it step by step:
1. count starts at 1.
2. Python checks whether count is less than or equal to 3.
3. It prints count.
4. It increases count by 1.
5. Python checks the condition again.
6. When count becomes 4, the condition is false and the loop stops.

**Important:** If you forget to update count, the condition may remain true forever. This creates an infinite loop.

## 8. Difference between for and while

| for loop | while loop |
|---|---|
| Commonly processes items in a collection | Repeats while a condition is true |
| Useful when the sequence is available | Useful when the number of repetitions depends on a condition |
| Often used with range() | Requires careful condition updates |

Example:
- Print every name in a list → for.
- Keep asking for a command until the user enters "exit" → while.

## 9. The break statement — stop the loop

`break` immediately exits the nearest loop.

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

What happened?
- Python prints 1.
- Python prints 2.
- When number becomes 3, the if condition is true.
- break exits the loop, so 3, 4 and 5 are not printed.

Use break when the task should stop completely after a condition is met.

## 10. The continue statement — skip this iteration

`continue` skips the remaining statements in the current iteration and moves to the next item.

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

When number is 3, Python skips the print statement for that iteration. The loop itself continues.

Difference:
- break stops the entire loop.
- continue skips only the current iteration.

## 11. Loop through dictionaries

A dictionary stores key-value pairs. Use `.items()` when you need both the key and value.

```python
employee = {
    "id": 101,
    "name": "Asha",
    "department": "IT"
}

for key, value in employee.items():
    print(key, ":", value)
```

Output:
```text
id : 101
name : Asha
department : IT
```

Explanation:
- `items()` provides each key-value pair.
- `key` receives the key.
- `value` receives the value.
- The loop runs once for each pair.

You will learn dictionaries in more detail on Day 8.

## 12. Nested loops

A nested loop is a loop inside another loop.

```python
departments = ["HR", "IT"]
shifts = ["Morning", "Evening"]

for department in departments:
    for shift in shifts:
        print(department, shift)
```

Output:
```text
HR Morning
HR Evening
IT Morning
IT Evening
```

For each department, the inner loop processes both shifts. Nested loops are useful for combinations, but large nested loops can perform many operations.

## 13. Common beginner mistakes

| Mistake | Why it happens | Correction |
|---|---|---|
| Infinite while loop | Condition variable never changes | Update the variable or use a valid stopping condition |
| Expecting range stop to be included | Stop value is exclusive | Use one more than the final number |
| Using break to skip one item | Confusing break and continue | Use continue to skip an iteration |
| Incorrect indentation | Loop body is not clearly defined | Indent loop statements consistently |
| Counter updated in wrong place | Count changes for every item instead of matching items | Update counter inside the condition |
| Changing a list during iteration | Items can be skipped or behavior becomes confusing | Build a new list or use a safe approach |

## 14. Industry scenario

A payment system receives a batch of transactions. It needs to count successful, pending and failed payments. It should add only successful payment amounts to the successful total.

A loop processes one record at a time. A condition decides how that record should be counted.

## 15. Interview preparation

**Q1. What is a loop?**

Answer: A loop is a control structure that repeatedly executes a block of code. It helps process collections and repeat tasks without writing the same statements many times.

Follow-up: What is an iteration?  
Answer: One complete pass through the loop body.

**Q2. What is the difference between for and while?**

Answer: A for loop commonly iterates over items in a sequence. A while loop repeats as long as its condition is true.

Follow-up: Which loop can create an infinite loop if the condition is not updated?  
Answer: A while loop can continue indefinitely if its condition never becomes false.

**Q3. Difference between break and continue?**

Answer: break exits the loop. continue skips the current iteration and proceeds to the next one.

## 16. Approved mini-project — Transaction Processing Simulator

**Objective:** Process a small list of transaction records and display a summary.

Sample data:
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
2. Display transaction ID and status.
3. Count successful transactions.
4. Calculate the total amount of successful transactions only.
5. Count pending and failed transactions separately.
6. Use conditions to classify each transaction.
7. Display a final summary.

### Expected summary
- Successful transactions: 2
- Successful amount total: 3300
- Pending transactions: 1
- Failed transactions: 1

### Validation
Add another successful transaction and verify that the count and total both change. Add a pending transaction and verify that it does not affect the successful amount total.

## 17. Daily practice and completion check

1. Print numbers 1 to 10 using range().
2. Print all names in a list.
3. Calculate the total of five prices.
4. Count how many numbers are greater than 10.
5. Use break to stop when a value is found.
6. Use continue to skip a chosen value.
7. Explain how a while loop stops.

You have completed Day 6 when you can trace a loop iteration by iteration and explain why it stops.

**Next lesson:** Day 7 — Strings, string methods and formatting.
