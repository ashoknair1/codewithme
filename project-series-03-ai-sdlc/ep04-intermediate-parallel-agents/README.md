# Ep 4 (Intermediate) — Parallel Agents: Ship One Feature with Three AIs

**What you build:** one real feature for MiniCRM — **follow-up reminders** (each deal can carry a follow-up date; the summary shows what's overdue) — delivered by three agents in parallel roles: one writes the endpoint, one writes the tests, one reviews the combined diff. You merge.

**The one key idea:** parallel agents multiply output *and* mistakes. The thing that makes it work isn't more agents — it's a feature spec tight enough that three agents build the same feature, plus a review pass that isn't the author.

**Worth knowing:**
- Split by *responsibility*, not by file: author / tester / reviewer beats three authors racing.
- The reviewer's prompt must forbid editing — a reviewer that quietly fixes things hides what it found.
- If the three outputs disagree, the spec was ambiguous. Fix the spec, not the agents.

**Try this:** run the protocol in `feature_spec.md` on a feature in your own project, and grade the reviewer: how many of its findings were real? Hint: a reviewer that finds nothing on a first pass isn't looking — tighten its checklist.
