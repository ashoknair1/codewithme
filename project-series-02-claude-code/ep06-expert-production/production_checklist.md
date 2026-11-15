# Production checklist (Ep 6) — work it top to bottom before strangers use your app

## Correctness
- [ ] Test suite exists and passes from a clean checkout (`python -m pytest -q`)
- [ ] Tests cover the unhappy paths: empty input, missing file, bad data
- [ ] You read every generated test yourself — no assert-what-the-code-does decoration

## Safety
- [ ] No secrets in code or git history (API keys live in environment variables)
- [ ] Debug mode OFF in the shipped config
- [ ] Error pages/messages show the user nothing internal (no stack traces, no paths)
- [ ] User input is validated before it touches files, queries, or commands

## Operability
- [ ] One command starts the app, documented in the README
- [ ] Data is backed up or regenerable; a restart loses nothing
- [ ] Dependencies pinned in requirements.txt with versions

## The agent pass
- [ ] Code-review Skill run on the final diff; findings fixed or consciously accepted
- [ ] CLAUDE.md updated with anything the next session must know
- [ ] A fresh agent session, given only the README, can run the app — proof the docs are real
