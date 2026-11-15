# Ep 1 (Beginner) — Intent, Spec, Plan: Stop Prompting, Start Directing

**What you build:** MiniCRM v1 — but the real work is the three documents written *before* any code: `intent.md` (one paragraph: what and why), `spec.md` (what it must do, must never do, and how we'll know), `plan.md` (ordered steps with success criteria the agent builds against).

**The one key idea:** prompting is chatting; directing is documents. An approved spec turns a coding agent from a slot machine into a contractor with a contract.

**Worth knowing:**
- Write the intent yourself, always. If you can't say what you want in one paragraph, the agent can't build it in fifty files.
- The spec's MUST NEVER list is where quality lives — most bugs are things nobody said not to do.
- Approve documents in order (intent → spec → plan) and never let the agent start building against an unapproved plan.

**Try this:** write a one-paragraph intent for a tool you personally need, then ask an agent for the spec — and count how many of *your* assumptions it had to guess. Hint: every guess it makes is a line your intent forgot.
