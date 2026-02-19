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

## Ollama local tutor (optional) — locked behavior

If allowed by the instructor, you may use a local tutor model via Ollama. It must NOT generate full solutions.


This is an optional setup that may be allowed by the instructor: a local LLM used as a tutor.
It is designed to help with explanations, hints, pseudocode, and debugging — not full solutions.

## What you get (locked behavior)
The repository includes a custom model definition:
- ollama/Modelfile.exam-tutor

This creates a model called:
- exam-tutor

The rules are enforced by the model "SYSTEM" prompt + short output + stop sequences.

## Setup

1) Install Ollama (macOS / Windows / Linux)
Install from the official Ollama installer.

2) Pull the base model (small/old)
From the repository root:
ollama pull tinyllama:1.1b-chat-v1-q2_K

3) Create the locked tutor model using the Modelfile
ollama create exam-tutor -f ollama/Modelfile.exam-tutor

4) Run the tutor
ollama run exam-tutor

Exit the interactive prompt with:
- /exit  or  Ctrl+D

## Allowed prompts (examples)
- Explain how prefix sums work and how to apply them (no full code).
- Suggest 3 edge cases and expected outputs for my function.
- Review my approach and point out logic mistakes (no full solution).

## Forbidden prompts
- Generate full implementations for required functions/classes.
- Generate the complete src/solutions.py file.
- Provide final answers directly.

