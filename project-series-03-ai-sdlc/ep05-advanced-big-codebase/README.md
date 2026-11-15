# Ep 5 (Advanced) — Coding Agents in a Big Codebase: Refactor, Debug, Secure

**What you build:** a safe refactor of `project/legacy_report.py` — the deliberately messy module (bare except, magic values, prints personal emails into a report) — done by an agent under a written security + behavior review, with tests pinning the current behavior *before* anything changes.

**The one key idea:** agents are fearless in code they don't understand, and big codebases punish fearlessness. Your job is blast-radius control: pin behavior with tests, bound the change, review the diff like it came from a stranger.

**Worth knowing:**
- Characterize before you refactor: tests that describe what the messy code *does today* are the only safe starting line.
- "Make it better" is not a refactor brief. Name the smells (bare except, leaked emails, string-built output) and the invariants (same totals, same format).
- Security review is a checklist, not a feeling — secrets, input handling, personal data in output, error leakage. See `security_review.md`.

**Try this:** run the checklist on the legacy module yourself before watching the episode's agent pass — then compare findings. Hint: the email addresses in the report output are the finding most people miss.
