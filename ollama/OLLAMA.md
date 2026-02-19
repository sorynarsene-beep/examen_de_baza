# Ollama local tutor (optional)

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
