# Ep 3 (Intermediate) — Harness Engineering: Keep Your Coding Agent Honest

**What you build:** the harness around MiniCRM's agent: a pytest suite the agent must keep green, a CI workflow that runs it on every push, and a one-command local check (`check.py`) that refuses to call anything "done" while a test fails.

**The one key idea:** you don't scale by reviewing every line an agent writes — you scale by building the harness that catches bad lines automatically. The harness is the senior engineer; the agent is the fast junior inside it.

**Worth knowing:**
- A test the agent wrote *and* graded is no harness at all — you read the tests; the machine runs them.
- CI is the harness with no mood: it doesn't get tired at 6 PM or wave a change through because the demo is tomorrow.
- When the agent fails the same check twice, the fix is a better check (or a rule in CLAUDE.md), not a sterner prompt.

**Try this:** copy `ci.yml` into your repo's `.github/workflows/` and `check.py` beside your tests, then deliberately break one behavior and watch every layer catch it. Hint: if any layer *doesn't* catch it, you've found the hole your next bug will use.
