# Ollama local tutor (optional)

This is an optional setup that may be allowed by the instructor: a local LLM used as a tutor.
It is designed to help with explanations, hints, pseudocode, and debugging — not full solutions.

## Create the locked tutor model
From the repository root:

1) Pull the base model (small/old):
```bash
ollama pull tinyllama:1.1b-chat-v1-q2_K
