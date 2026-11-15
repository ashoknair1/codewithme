# MiniCRM — AI SDLC map (Ep 2)

| Stage | Produces | Owner | Exit test |
|---|---|---|---|
| Plan | intent.md, spec.md, plan.md | Human (agent drafts, human approves) | Spec's "done when" list is testable |
| Design | Data shapes (contact, deal, stages) + the four endpoints | Human judgment, agent options | Every spec line maps to an endpoint or a test |
| Build | app.py against the plan, step by step | Agent | Each plan step's success test passes before the next starts |
| Test | pytest suite + CI (Ep 3) | Agent writes, human reads | Suite green from a clean checkout |
| Deploy | One-command start + pinned requirements (Ep 6) | Human | A fresh machine/session runs it from the README alone |
| Maintain | Reviews, refactors, security passes (Ep 5) | Human accountable | No change merges without tests + review |
