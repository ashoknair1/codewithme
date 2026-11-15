---
name: code-review
description: Review the current code changes for bugs, risky patterns and missing tests. Use when the user asks to review, check, or look over code or a diff before committing or shipping.
---

# Code review procedure

1. Get the change set: `git diff HEAD` (and `git status` for new files). If there is no diff, say so and stop.
2. Read each changed file fully — never review a diff hunk without its surrounding function.
3. Check, in this order:
   - **Correctness:** logic errors, off-by-one, unhandled empty/None cases, wrong error handling.
   - **Safety:** secrets in code, unsanitized input, destructive operations without confirmation.
   - **Tests:** does the change break an existing test? Is new behavior covered?
   - **Simplicity:** duplicated logic, dead code, names that mislead.
4. Report as a short list, most serious first. For each finding: file, line, what's wrong, and a concrete fix.
5. End with one line: "Ship it" / "Fix first" / "Needs tests" — and why, in five words or fewer.
