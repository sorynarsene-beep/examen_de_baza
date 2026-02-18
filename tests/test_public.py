import pytest

from src.solutions import (
    parse_transactions,
    totals_by_category,
    top_spender,
    max_len_subarray_sum_k,
    average_per_student,
    Book,
    Library,
    library_summary,
)


# ----------------------------
# Part II — Problem 1 tests
# ----------------------------

def test_parse_transactions_ignores_invalid():
    lines = [
        "Ana;food;12.5",
        "Ion;transport;8",
        "bad_line",
        "Mara;books;xx",
        " ;food;10",
        "Ion;food;10",
    ]
    tx = parse_transactions(lines)
    assert tx == [
        {"name": "Ana", "category": "food", "amount": 12.5},
        {"name": "Ion", "category": "transport", "amount": 8.0},
        {"name": "Ion", "category": "food", "amount": 10.0},
    ]


def test_totals_by_category_rounding():
    tx = [
        {"name": "Ana", "category": "food", "amount": 12.555},
        {"name": "Ion", "category": "food", "amount": 3.333},
        {"name": "Ana", "category": "transport", "amount": 8},
    ]
    totals = totals_by_category(tx)
    assert totals["food"] == round(12.555 + 3.333, 2)
    assert totals["transport"] == 8.0


def test_top_spender_tie_break():
    tx = [
        {"name": "Ion", "category": "x", "amount": 10},
        {"name": "Ana", "category": "y", "amount": 10},
    ]
    # tie in totals -> lexicographically smaller name wins => "Ana"
    assert top_spender(tx) == ("Ana", 10.0)


def test_top_spender_empty():
    assert top_spender([]) == (None, 0.0)


# ----------------------------
# Part II — Problem 2 tests
# ----------------------------

def test_max_len_subarray_sum_k_examples():
    assert max_len_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4
    assert max_len_subarray_sum_k([-2, -1, 2, 1], 1) == 2


def test_max_len_subarray_sum_k_edge():
    assert max_len_subarray_sum_k([], 0) == 0
    assert max_len_subarray_sum_k([0, 0, 0], 0) == 3
    assert max_len_subarray_sum_k([1, 2, 3], 7) == 0


# ----------------------------
# Part III — Debugging tests
# ----------------------------

def test_average_per_student_basic():
    records = [("Ana", 10), ("Ana", 8), ("Ion", 9)]
    # Ana avg 9.0, Ion avg 9.0 -> tie => "Ana"
    assert average_per_student(records) == ("Ana", 9.0)


def test_average_per_student_empty():
    assert average_per_student([]) == (None, 0.0)


# ----------------------------
# Part IV — OOP tests
# ----------------------------

def test_book_validation_and_str():
    b = Book("Dune", "Frank Herbert", 1965)
    assert b.is_borrowed is False
    assert str(b) == "Dune - Frank Herbert (1965) [AVAILABLE]"

    b.is_borrowed = True
    assert "[BORROWED]" in str(b)

    with pytest.raises(ValueError):
        Book("   ", "A", 2000)

    with pytest.raises(ValueError):
        Book("X", "   ", 2000)

    with pytest.raises(ValueError):
        Book("X", "Y", 1200)


def test_library_flow():
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", 1965))
    lib.add_book(Book("Dune", "Frank Herbert", 1965))  # duplicate ignored
    lib.add_book(Book("Foundation", "Isaac Asimov", 1951))

    assert library_summary(lib) == {"total": 2, "borrowed": 0, "available": 2}

    assert lib.borrow("dune") is True
    assert lib.borrow("Dune") is False  # already borrowed

    assert library_summary(lib) == {"total": 2, "borrowed": 1, "available": 1}

    assert lib.return_book("Dune") is True
    assert lib.return_book("Dune") is False

    assert len(lib.available_books()) == 2


def test_find_by_author_case_insensitive():
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", 1965))
    lib.add_book(Book("Dune Messiah", "Frank Herbert", 1969))
    lib.add_book(Book("Foundation", "Isaac Asimov", 1951))

    res = lib.find_by_author("frank herbert")
    assert len(res) == 2
