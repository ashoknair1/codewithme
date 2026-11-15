# CLAUDE.md — template (Ep 2). Copy to your project root and edit.

## What this project is
One or two sentences: what it does, who uses it, the stack.
Example: "LinkSaver — a personal link-saving web app. Python + Flask, one template, JSON file storage."

## Commands
- Run the app: `python app.py` (serves on http://localhost:5000)
- Run the tests: `python -m pytest -q`
- Install deps: `pip install -r requirements.txt`

## Rules Claude must follow
- Small changes only; explain the plan before editing more than one file.
- Never delete or rewrite the data file; migrate it if the format changes.
- After any code change, run the tests and show me the result.
- No new dependencies without asking me first.

## Style
- Plain, readable code over clever code. Comments explain *why*, not *what*.
- Match the existing naming and layout; don't reorganize files unasked.
