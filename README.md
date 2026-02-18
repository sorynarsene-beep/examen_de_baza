# Python Exam (3 hours)

This repository contains a ready-to-run exam package:
- **Exam statement**: `exam/EXAM.md`
- **Student work**: `src/solutions.py` (ONLY file students should edit)
- **Public tests**: `tests/test_public.py`
- **How to run**: see below

## Quick start

### 1) Create a virtual environment
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run public tests
```bash
pytest -q
```

## Instructor notes (recommended workflow)
- Keep the repo **private** during the exam.
- After the exam ends, you can open the repo or publish solutions.

## Files
- `exam/EXAM.md` — full statement + grading
- `src/solutions.py` — stubs + docstrings
- `tests/test_public.py` — sample tests (students can run)
- `GRADING.md` — suggested rubric
