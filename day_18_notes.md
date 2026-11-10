# Day 18: Complete OOP Integration and Revision

**Pathway:** Python Backend Developer Career Pathway (Django)  
**Phase:** 1B — Object-Oriented Programming  
**Time:** 2–3 hours | **Level:** Beginner to Intermediate  
**Prerequisites:** Days 13–17 — OOP foundations  
**Tools:** Python 3.10+, VS Code and terminal  
**Approved mini-project:** Library Management System

---

## 1. What you will learn

By the end of this revision lesson, you can:
1. Identify classes, objects, attributes and methods in a requirement.
2. Initialize objects using __init__.
3. Distinguish instance, class and static methods.
4. Apply inheritance and overriding where an is-a relationship exists.
5. Use super() to reuse parent initialization and behavior.
6. Apply encapsulation and validation to protect object state.
7. Use abstraction and polymorphism through a common interface.
8. Choose composition for has-a relationships.
9. Build a small multi-class Library Management System.
10. Explain your design decisions during an interview.

## 2. OOP in one picture

```text
Business requirement
       |
       v
Identify real-world entities
       |
       v
Define classes
       |
       v
Create objects with __init__
       |
       v
Store state in instance attributes
       |
       v
Define methods for behavior
       |
       v
Use inheritance only for genuine is-a relationships
       |
       v
Use encapsulation and validation for state changes
       |
       v
Use abstraction/polymorphism for common operations
       |
       v
Test normal and invalid behavior
```

This is a design-thinking flow, not a fixed sequence required for every small program.

## 3. OOP concept revision

| Concept | Meaning | Example from this pathway |
|---|---|---|
| Class | Definition for objects | Student |
| Object | One instance | student1 |
| Attribute | Data associated with an object/class | student.name |
| Method | Function defined in a class | display_profile() |
| __init__ | Initializes a new instance | Set employee name |
| self | Current instance | self.name |
| Instance method | Works with one object's state | calculate_salary() |
| Class method | Receives the class as cls | change_company() |
| Static method | No automatic self or cls | validate_code() |
| Inheritance | Reuse/extend a parent class | Developer(Employee) |
| Overriding | Child supplies its own method | Developer.work() |
| Encapsulation | Group and control state changes | BankAccount.deposit() |
| Abstraction | Expose an essential contract | Payment.pay() |
| Polymorphism | Different objects support a common operation | Card.pay(), UPI.pay() |
| Composition | One object contains another | Library has Books |

## 4. Design before coding

A library needs to manage books and members.

Ask:
1. What information belongs to a book?
2. What information belongs to a member?
3. What does a library manage?
4. Who can borrow a book?
5. How do we know whether a book is available?
6. What should happen when someone borrows an unavailable book?
7. What should happen when a member returns a book they did not borrow?

Possible classes:
- Book
- Member
- Library

Relationship:
- A Library has books.
- A Library has members.
- A Member can borrow books.
- A Book has an availability state.

The library is not a book. It manages book objects. This is a composition relationship, not inheritance.

## 5. Class design: Book

A book needs an ID, title and author. It also needs to track availability.

```python
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def mark_borrowed(self):
        if not self.is_available:
            raise ValueError("Book is already borrowed")
        self.is_available = False

    def mark_returned(self):
        if self.is_available:
            raise ValueError("Book is already available")
        self.is_available = True
```

Explanation:
- The initializer prepares the book.
- Every new book starts as available.
- mark_borrowed changes availability to False.
- mark_returned changes availability to True.
- Invalid transitions are rejected.

## 6. Class design: Member

```python
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_book_ids = []

    def borrow_book(self, book):
        self.borrowed_book_ids.append(book.book_id)

    def return_book(self, book):
        self.borrowed_book_ids.remove(book.book_id)
```

The list belongs to each member. It records the IDs of books that member has borrowed.

This simple version assumes the library validates whether the book is available before calling these methods. We will improve the workflow in the Library class.

## 7. Why the Library class is needed

If every member independently changes book availability, the rules can become scattered. The Library class can coordinate the operation:

1. Find the requested book.
2. Check availability.
3. Change the book state.
4. Record the borrowed book against the member.
5. Report success.

This is a business workflow that coordinates multiple objects.

## 8. Complete Library Management System

Create a folder:

```text
day_18_library_management/
├── main.py
└── README.md
```

Save the following as main.py.

```python
class Book:
    def __init__(self, book_id, title, author):
        if book_id <= 0:
            raise ValueError("Book ID must be positive")
        if not title.strip():
            raise ValueError("Book title cannot be empty")

        self.book_id = book_id
        self.title = title.strip()
        self.author = author.strip()
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        print(self.book_id, self.title, self.author, status)


class Member:
    def __init__(self, member_id, name):
        if member_id <= 0:
            raise ValueError("Member ID must be positive")
        if not name.strip():
            raise ValueError("Member name cannot be empty")

        self.member_id = member_id
        self.name = name.strip()
        self.borrowed_book_ids = []


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError("Book ID already exists")
        self.books[book.book_id] = book

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists")
        self.members[member.member_id] = member

    def display_books(self):
        print("BOOK CATALOG")
        for book in self.books.values():
            book.display()

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]

        if not book.is_available:
            raise ValueError("Book is already borrowed")

        book.is_available = False
        member.borrowed_book_ids.append(book_id)
        print(member.name, "borrowed", book.title)

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed_book_ids:
            raise ValueError("This member has not borrowed this book")

        member.borrowed_book_ids.remove(book_id)
        book.is_available = True
        print(member.name, "returned", book.title)

    def display_member_borrowings(self, member_id):
        if member_id not in self.members:
            raise ValueError("Member not found")

        member = self.members[member_id]
        print("Borrowed books for", member.name)

        if not member.borrowed_book_ids:
            print("No books borrowed")
            return

        for book_id in member.borrowed_book_ids:
            print(self.books[book_id].title)


library = Library("TechPhile Library")

library.add_book(Book(1, "Python Basics", "A. Kumar"))
library.add_book(Book(2, "Django Guide", "S. Rao"))
library.add_book(Book(3, "SQL Fundamentals", "M. Das"))

library.register_member(Member(101, "Asha"))
library.register_member(Member(102, "Ravi"))

library.display_books()

library.borrow_book(101, 1)
library.display_member_borrowings(101)

print("BOOKS AFTER BORROWING")
library.display_books()

library.return_book(101, 1)

print("BOOKS AFTER RETURN")
library.display_books()
```

## 9. Understand the project flow

When the program calls `library.borrow_book(101, 1)`:

1. The method checks whether member 101 exists.
2. It checks whether book 1 exists.
3. It retrieves the Member object from the members dictionary.
4. It retrieves the Book object from the books dictionary.
5. It checks the book's availability.
6. It changes the book state to borrowed.
7. It appends the book ID to the member's borrowed list.
8. It prints a confirmation.

When the member returns the book, the workflow verifies that this member actually borrowed it before updating the state.

## 10. Expected behavior

The program should:
- Display three books as available at the beginning.
- Display Asha borrowing Python Basics.
- Show Python Basics as borrowed.
- Show Python Basics in Asha's borrowing list.
- Display the book as available after the return.

Exact spacing is not important. The state changes and messages are.

## 11. Important design discussion

### 11.1 Why use dictionaries for books and members?

The dictionaries use IDs as keys:

```python
self.books[book.book_id] = book
self.members[member.member_id] = member
```

This allows direct lookup by ID rather than scanning every item in a list.

### 11.2 Why is Library not a child of Book?

A library is not a specialized book. A library contains and manages books. That is a has-a relationship, so composition is appropriate.

### 11.3 Why is this not a database application?

The objects exist only while the Python program runs. When the program stops, the data disappears. Later Django and SQL lessons will teach persistent storage.

### 11.4 What production features are missing?

- Database persistence.
- User authentication.
- Borrowing due dates.
- Late-return fines.
- Transaction safety for simultaneous users.
- Audit history.
- API endpoints.
- Automated unit tests.

These are extensions, not prerequisites for understanding today's OOP integration.

## 12. Validation and test cases

| Test | Action | Expected result |
|---|---|---|
| 1 | Add a book with a valid ID | Book stored |
| 2 | Add duplicate book ID | ValueError |
| 3 | Register a valid member | Member stored |
| 4 | Borrow an available book | Book marked borrowed |
| 5 | Borrow the same book again | ValueError |
| 6 | Return a book borrowed by the member | Book becomes available |
| 7 | Return a book not borrowed by the member | ValueError |
| 8 | Borrow using unknown member ID | ValueError |
| 9 | Borrow using unknown book ID | ValueError |
| 10 | Display empty borrowing list | No books borrowed |

## 13. Debugging checklist

1. Check class and method indentation.
2. Confirm object IDs are unique.
3. Confirm dictionaries store the expected object.
4. Check the member ID and book ID supplied to the method.
5. Inspect book availability before and after borrowing.
6. Inspect the member's borrowed_book_ids list.
7. Test one workflow at a time.
8. Read the final exception line and identify the failing condition.

## 14. OOP revision exercises

1. Add a maximum borrowing limit of two books per member.
2. Add a method to search books by title.
3. Add a method to list all available books.
4. Add a Librarian class that inherits from Member and has an additional responsibility.
5. Add an abstract Notification class and EmailNotification implementation for due-date reminders.
6. Explain which relationships use composition and which use inheritance.
7. Add tests for duplicate IDs and invalid returns.

## 15. Interview questions

**1. What is the difference between a class and an object?**  
A class defines structure and behavior; an object is an instance of that class.

**2. What is self?**  
It refers to the current instance in an instance method.

**3. What is __init__?**  
It initializes a newly created object with starting values.

**4. What is the difference between instance and class attributes?**  
Instance attributes belong to individual objects; class attributes are defined on the class and can be shared through instances.

**5. Difference between instance, class and static methods?**  
Instance methods receive self, class methods receive cls, and static methods receive neither automatically.

**6. What is inheritance?**  
A child class reuses and extends a parent class.

**7. What is method overriding?**  
A child class provides its own implementation of an inherited method.

**8. What is encapsulation?**  
Grouping data and behavior and controlling how object state is changed.

**9. What is abstraction?**  
Exposing essential operations while hiding implementation details.

**10. What is polymorphism?**  
Different object types can support the same operation with different behavior.

**11. What is composition?**  
Building an object using references to other objects; it commonly represents a has-a relationship.

**12. Why is the Library class composed of Book and Member objects?**  
A library manages books and members; it is not a specialized form of either.

## 16. MCQs

**Q1. Which relationship is represented by Library containing Book objects?**  
A. Has-a  
B. Is-a  
C. Overrides  
D. Imports  
**Answer: A.** A library has books.

**Q2. Which method initializes an object?**  
A. __init__  
B. __main__  
C. __loop__  
D. __start__  
**Answer: A.** Python invokes __init__ to initialize a new instance.

**Q3. Which method receives cls?**  
A. Instance method  
B. Class method  
C. Static method  
D. Local function  
**Answer: B.** A class method receives the class.

**Q4. What is method overriding?**  
A. Child implementation of an inherited method  
B. Deleting an object  
C. Creating a variable  
D. Opening a file  
**Answer: A.** The child customizes inherited behavior.

**Q5. What does encapsulation help with?**  
A. Grouping state and controlling changes  
B. Formatting a disk  
C. Installing Python  
D. Sorting a list only  
**Answer: A.** Encapsulation organizes data and related behavior.

**Q6. Which concept lets different payment classes provide pay()?**  
A. Polymorphism  
B. File handling  
C. Indexing  
D. Compilation  
**Answer: A.** Different objects support the same operation.

## 17. Final completion checklist

- [ ] I can identify classes and objects from a requirement.
- [ ] I can initialize objects.
- [ ] I understand instance, class and static methods.
- [ ] I can explain inheritance and overriding.
- [ ] I can use super().
- [ ] I can explain encapsulation, abstraction and polymorphism.
- [ ] I can distinguish inheritance and composition.
- [ ] I completed the Library Management System.
- [ ] I tested normal and invalid borrowing/return scenarios.
- [ ] I can explain the project without reading the code line by line.

**Next lesson:** Day 19 — Client-Server Architecture and How Websites Work.
