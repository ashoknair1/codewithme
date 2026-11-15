# Ep 3 (Intermediate) — Teach Claude Code a New Trick: Your First Agent Skill

**What you build:** a working Skill — a folder with a SKILL.md that Claude Code loads automatically when a task matches its description. Ours does a disciplined code review.

**The one key idea:** a Skill is a reusable *procedure*, not a fact sheet. Write the steps you'd want followed every time, and a description precise enough that Claude reaches for it on its own.

**Worth knowing:**
- The `description:` line is the trigger — write it like you'd brief a colleague: what it does AND when to use it.
- Keep the body to the steps; long background reading belongs in separate files the Skill can open.
- Test a Skill by asking for the task *without naming the Skill* — if it doesn't trigger, the description is wrong, not the steps.

**Try this:** copy `skills/code-review/` into your project's `.claude/skills/`, then ask Claude to "look over my changes" and watch it pick the Skill up. Hint: commit your changes first — the Skill reviews the diff.
