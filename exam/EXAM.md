# Python Exam — (Basics + OOP + Algorithmic Thinking)
**Duration:** 3 hours  
**Total:** 100 points  

## Rules
- You may use **Python 3.10+**.
- Allowed imports: `math`, `typing`, `dataclasses` (optional). No external libraries.
- Edit **only**: `src/solutions.py` and `exam/THEORY_ANSWERS.md`.
- Your code must pass `pytest` public tests. Additional hidden tests may be used for grading.

---

## Part I — Theory & Output Prediction (15p, ~20 min)

### I.1 Output prediction (10p, 2p each)
Write the exact output for each snippet in `exam/THEORY_ANSWERS.md`.

1)
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

2)
```python
def f(a, lst=[]):
    lst.append(a)
    return lst

print(f(1))
print(f(2))
```

3)
```python
s = "abc"
print(s[::-1], s[1:])
```

4)
```python
d = {"a": 1}
print(d.get("b", 7), "b" in d)
```

5)
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```

### I.2 Short questions (5p, 1p each)
Answer in `exam/THEORY_ANSWERS.md`:
1. Difference between `list` and `tuple`?
2. What is a side effect in a function?
3. What does time complexity **O(n)** mean?
4. What is the role of `__init__` in a class?
5. When do you use `try/except`?

---

## Part II — Implementation Problems (40p, ~75 min)

### Problem 1: Transactions parsing & aggregation (20p)
You receive a list of strings with format:
`"name;category;amount"`

Example:
```python
[
  "Ana;food;12.5",
  "Ion;transport;8",
  "Ana;food;3.5",
  "Mara;books;50",
  "Ion;food;10"
]
```

Implement in `src/solutions.py`:

1) `parse_transactions(lines) -> list[dict]` (8p)  
Return a list of dicts: `{"name": str, "category": str, "amount": float}`.  
If a line is invalid (not 3 fields or amount not a number), ignore it.

2) `totals_by_category(transactions) -> dict[str, float]` (7p)  
Return totals by category, rounded to 2 decimals.

3) `top_spender(transactions) -> tuple[str|None, float]` (5p)  
Return `(name, total)` for the person with the biggest total spend.  
Ties: choose the lexicographically smaller name.  
If empty: return `(None, 0.0)`.

---

### Problem 2: Algorithmic — max length subarray with sum k (20p)
Given `nums: list[int]` and `k: int`, find the **maximum length** of a contiguous subarray with sum exactly `k`.

Examples:
- `nums = [1, -1, 5, -2, 3], k = 3` → `4`
- `nums = [-2, -1, 2, 1], k = 1` → `2`

Implement:
- `max_len_subarray_sum_k(nums, k) -> int`

Scoring:
- Correct O(n^2) solution can earn partial credit.
- Full credit expects O(n) using prefix sums + dict.

---

## Part III — Debugging & Tests (20p, ~30 min)

In `src/solutions.py`, fix the function `average_per_student(records)`.

Tasks:
- (8p) Identify at least 6 issues (write them as comments above the function).
- (8p) Provide a corrected implementation.
- (4p) Provide 3 meaningful tests (add them in `tests/test_public.py` under the provided section OR describe them in comments).

**Provided buggy code** is inside `src/solutions.py`.

---

## Part IV — OOP mini-project (25p, ~50 min)
Implement a small library system.

### 1) Class `Book` (8p)
Attributes:
- `title: str`
- `author: str`
- `year: int`
- `is_borrowed: bool` (initially `False`)

Methods:
- `__init__` validates:
  - `title` and `author` are non-empty after `.strip()`
  - `year` is between **1450 and 2026** (inclusive)
- `__str__` returns:
  - `"Title - Author (Year) [AVAILABLE]"` or `[BORROWED]`

### 2) Class `Library` (12p)
Attribute:
- `books: list[Book]` (starts empty)

Methods:
- `add_book(book) -> None`  
Add only if there is no existing book with same `(title, author, year)`.

- `find_by_author(author) -> list[Book]`  
Case-insensitive match.

- `borrow(title) -> bool`  
Mark the **first** matching title (case-insensitive) as borrowed if available.

- `return_book(title) -> bool`  
Mark the **first** matching title as available **only if it was borrowed**.

- `available_books() -> list[Book]`  
Return available books.

### 3) Function `library_summary(lib) -> dict` (5p)
Return:
```python
{"total": X, "borrowed": Y, "available": Z}
```

---

## Submission
- Commit and push your final version OR upload a ZIP with:
  - `src/solutions.py`
  - `exam/THEORY_ANSWERS.md`

Good luck.
