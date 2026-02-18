"""
Student solutions file.

IMPORTANT:
- Do not change function names/signatures.
- You may add helper functions/classes, but keep required API intact.
"""

from __future__ import annotations


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
    # TODO: implement
    raise NotImplementedError


def totals_by_category(transactions: list[dict]) -> dict[str, float]:
    """
    Sum amounts by category.
    Output values are rounded to 2 decimals.
    """
    # TODO: implement
    raise NotImplementedError


def top_spender(transactions: list[dict]) -> tuple[str | None, float]:
    """
    Return (name, total_spent) for the biggest spender.
    Ties: lexicographically smaller name wins.
    Empty input: (None, 0.0)
    """
    # TODO: implement
    raise NotImplementedError


# ----------------------------
# Part II — Problem 2
# ----------------------------

def max_len_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the maximum length of a contiguous subarray with sum exactly k.
    Full-credit solution: O(n) using prefix sums and a dict of first occurrences.
    """
    # TODO: implement
    raise NotImplementedError


# ----------------------------
# Part III — Debugging
# ----------------------------

def average_per_student(records: list[tuple[str, int]]) -> tuple[str | None, float]:
    """
    Return (name, average) for the student with the highest average.
    Ties: choose lexicographically smaller name.
    Empty records: (None, 0.0)

    Task:
    - Write at least 6 issues of the original buggy code as comments here.
    - Then implement the corrected version.
    """
    # TODO: implement
    raise NotImplementedError


# ----------------------------
# Part IV — OOP mini-project
# ----------------------------

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Validate:
        - title and author are non-empty after strip
        - year in [1450, 2026]
        Set is_borrowed = False initially.
        """
        # TODO: implement
        raise NotImplementedError

    def __str__(self) -> str:
        """
        "Title - Author (Year) [AVAILABLE]" or [BORROWED]
        """
        # TODO: implement
        raise NotImplementedError


class Library:
    def __init__(self):
        # books: list[Book]
        self.books = []

    def add_book(self, book: Book) -> None:
        # TODO: implement
        raise NotImplementedError

    def find_by_author(self, author: str) -> list[Book]:
        # TODO: implement
        raise NotImplementedError

    def borrow(self, title: str) -> bool:
        # TODO: implement
        raise NotImplementedError

    def return_book(self, title: str) -> bool:
        # TODO: implement
        raise NotImplementedError

    def available_books(self) -> list[Book]:
        # TODO: implement
        raise NotImplementedError


def library_summary(lib: Library) -> dict[str, int]:
    """
    Return {"total": X, "borrowed": Y, "available": Z}
    """
    # TODO: implement
    raise NotImplementedError
