"""
Student solutions file.

IMPORTANT:
- Do not change function names/signatures.
- You may add helper functions/classes, but keep required API intact.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any


# ----------------------------
# Part II — Problem 1
# ----------------------------

def parse_transactions(lines: list[str]) -> list[dict]:
    """
    Parse lines of format "name;category;amount" into dicts:
    {"name": str, "category": str, "amount": float}

    Invalid lines are ignored:
    - not exactly 3 fields
    - amount not a number
    """
    transactions: list[dict] = []
    for line in lines:
        if not isinstance(line, str):
            continue
        parts = line.split(";")
        if len(parts) != 3:
            continue
        name = parts[0].strip()
        category = parts[1].strip()
        amount_str = parts[2].strip()
        if name == "" or category == "":
            # you may choose to ignore empty name/category
            continue
        try:
            amount = float(amount_str)
        except ValueError:
            continue
        transactions.append({"name": name, "category": category, "amount": amount})
    return transactions


def totals_by_category(transactions: list[dict]) -> dict[str, float]:
    """
    Sum amounts by category.
    Output values are rounded to 2 decimals.
    """
    totals: dict[str, float] = {}
    for t in transactions:
        cat = t.get("category")
        amt = t.get("amount")
        if not isinstance(cat, str):
            continue
        try:
            val = float(amt)
        except (TypeError, ValueError):
            continue
        totals[cat] = totals.get(cat, 0.0) + val
    # round to 2 decimals
    return {k: round(v, 2) for k, v in totals.items()}


def top_spender(transactions: list[dict]) -> tuple[str | None, float]:
    """
    Return (name, total_spent) for the biggest spender.
    Ties: lexicographically smaller name wins.
    Empty input: (None, 0.0)
    """
    totals: dict[str, float] = {}
    for t in transactions:
        name = t.get("name")
        amt = t.get("amount")
        if not isinstance(name, str):
            continue
        try:
            val = float(amt)
        except (TypeError, ValueError):
            continue
        totals[name] = totals.get(name, 0.0) + val

    if not totals:
        return (None, 0.0)

    best_name = None
    best_total = None
    for name, total in totals.items():
        if best_total is None or total > best_total or (total == best_total and name < best_name):
            best_name = name
            best_total = total
    return (best_name, round(float(best_total), 2))


# ----------------------------
# Part II — Problem 2
# ----------------------------

def max_len_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the maximum length of a contiguous subarray with sum exactly k.
    Expected full-credit solution: O(n) using prefix sums and a dict of first occurrences.

    Works with negative numbers.
    """
    first_index: dict[int, int] = {0: -1}  # prefix_sum -> earliest index
    prefix = 0
    best = 0
    for i, x in enumerate(nums):
        prefix += int(x)
        # store earliest occurrence only
        if prefix not in first_index:
            first_index[prefix] = i
        target = prefix - int(k)
        if target in first_index:
            best = max(best, i - first_index[target])
    return best


# ----------------------------
# Part III — Debugging
# ----------------------------

# Original buggy code (kept here for reference):
# def average_per_student(records):
#     # records: list of (name, grade) grade is int 1..10
#     totals = {}
#     counts = {}
#     for name, grade in records:
#         totals[name] = totals.get(name, 0) + int(grade)
#         counts[name] = counts.get(name, 0)
#         counts[name] += 1
#
#     averages = []
#     for name in totals:
#         averages.append((name, totals[name] / counts[name]))
#
#     averages.sort()
#     return averages[-1]  # should return (name, average) with highest avg

def average_per_student(records: list[tuple[str, int]]) -> tuple[str | None, float]:
    """
    Return (name, average) for the student with the highest average.
    Ties: choose lexicographically smaller name.
    Empty records: (None, 0.0)

    NOTE: Write at least 6 issues of the original buggy code as comments above your final solution
    during the exam. (Instructor may grade this section manually.)
    """
    totals: dict[str, int] = {}
    counts: dict[str, int] = {}

    for name, grade in records:
        if not isinstance(name, str):
            continue
        try:
            g = int(grade)
        except (TypeError, ValueError):
            continue
        totals[name] = totals.get(name, 0) + g
        counts[name] = counts.get(name, 0) + 1

    if not totals:
        return (None, 0.0)

    best_name: str | None = None
    best_avg: float | None = None

    for name in totals:
        avg = totals[name] / counts[name]
        if best_avg is None or avg > best_avg or (avg == best_avg and name < best_name):
            best_name = name
            best_avg = avg

    return (best_name, round(float(best_avg), 2))


# ----------------------------
# Part IV — OOP mini-project
# ----------------------------

class Book:
    def __init__(self, title: str, author: str, year: int):
        title = title.strip() if isinstance(title, str) else ""
        author = author.strip() if isinstance(author, str) else ""
        if not title:
            raise ValueError("title must be non-empty")
        if not author:
            raise ValueError("author must be non-empty")
        y = int(year)
        if y < 1450 or y > 2026:
            raise ValueError("year out of range")
        self.title = title
        self.author = author
        self.year = y
        self.is_borrowed = False

    def __str__(self) -> str:
        status = "BORROWED" if self.is_borrowed else "AVAILABLE"
        return f"{self.title} - {self.author} ({self.year}) [{status}]"


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        for b in self.books:
            if (b.title, b.author, b.year) == (book.title, book.author, book.year):
                return
        self.books.append(book)

    def find_by_author(self, author: str) -> list[Book]:
        a = author.strip().lower()
        return [b for b in self.books if b.author.lower() == a]

    def borrow(self, title: str) -> bool:
        t = title.strip().lower()
        for b in self.books:
            if b.title.lower() == t and not b.is_borrowed:
                b.is_borrowed = True
                return True
        return False

    def return_book(self, title: str) -> bool:
        t = title.strip().lower()
        for b in self.books:
            if b.title.lower() == t and b.is_borrowed:
                b.is_borrowed = False
                return True
        return False

    def available_books(self) -> list[Book]:
        return [b for b in self.books if not b.is_borrowed]


def library_summary(lib: Library) -> dict[str, int]:
    total = len(lib.books)
    borrowed = sum(1 for b in lib.books if b.is_borrowed)
    available = total - borrowed
    return {"total": total, "borrowed": borrowed, "available": available}
