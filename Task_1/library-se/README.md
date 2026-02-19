# Library Book Management System  
**Software Engineering Assignment – Task 1 (CS2042)**

## 📌 Overview
This project implements a **Library Book Management System** using a **three-sprint Agile development process**.  
The focus of the assignment is **software engineering discipline**, not just functionality.

The system is developed using:
- **Agile (Sprint-based) workflow**
- **Git branching, merging, and tagging**
- **Unit Testing with Python `unittest`**
- **Test-Driven Development (TDD)**

All data is stored using **in-memory data structures** (no database).

---

## 🎯 Objectives
- Practice **Agile Software Development**
- Follow **Git discipline** (feature branches, merges, tags)
- Apply **Test-Driven Development (RED → GREEN → REFACTOR)**
- Maintain **traceability** between requirements, code, tests, and releases

---

## 🛠️ Technology Stack
- **Language:** Python 3
- **Testing Framework:** unittest
- **Version Control:** Git & GitHub
- **Platform:** Ubuntu (Linux)

---

## 📂 Project Structure
library-se/
├── src/
│ ├── init.py
│ └── library.py
├── tests/
│ ├── init.py
│ └── test_library.py
├── docs/
│ ├── USER_STORIES.md
│ └── TRACEABILITY.md
├── README.md
└── .gitignore


---

## 🚀 Sprint-wise Implementation

### 🟢 Sprint 1 – Book Registration (`v0.1`)
**Goal:** Add and store books in the library.

**Features:**
- Add a book (Book ID, Title, Author)
- Prevent duplicate Book IDs

**Key Methods:**
- `add_book()`

**Tests:**
- Successful book addition
- Duplicate book rejection

---

### 🟡 Sprint 2 – Borrow & Return Book (`v0.2`)
**Goal:** Manage borrowing status of books.

**Features:**
- Borrow a book
- Return a book
- Prevent borrowing an already borrowed book

**Key Methods:**
- `borrow_book()`
- `return_book()`

**Tests:**
- Borrow available book
- Reject unavailable book
- Return book updates status

---

### 🔵 Sprint 3 – Library Report (`v0.3`)
**Goal:** Generate library status report.

**Features:**
- Generate report with:
  - Book ID
  - Title
  - Author
  - Status (Available / Borrowed)

**Key Methods:**
- `generate_report()`

**Tests:**
- Report contains header
- Report contains book entries

---

## 🧪 Running Unit Tests
All tests must be run from the project root directory.

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v

Expected Output
Ran X tests in ...
OK
🔀 Git Workflow Followed

No direct commits to main

Each sprint developed in:

feature/sprint-X


Each sprint:

Includes unit tests

Is merged into main

Is tagged after merge

Tags Used

v0.1 → Sprint 1

v0.2 → Sprint 2

v0.3 → Sprint 3

📌 Traceability

Traceability between:

User Stories

Source Code

Unit Tests

Git Tags

is maintained in:

docs/TRACEABILITY.md


✅ Key Learnings

Importance of process over just code

Value of unit testing and TDD

Proper Git discipline using branches and tags

How Agile development improves reliability and maintainability

📎 Submission Details

Course: CS2042 – Software Engineering

Assignment: Agile Development with Git and Unit Testing

Repository:
https://github.com/sharadpal8055/Software_engineering_assignments

🏁 Conclusion

This project demonstrates a complete software engineering lifecycle using Agile practices, TDD, and Git.
It emphasizes maintainability, correctness, and traceability, aligning with industry-standard development practices.

