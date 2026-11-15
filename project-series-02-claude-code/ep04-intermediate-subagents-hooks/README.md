# Ep 4 (Intermediate) — Subagents & Hooks: Put Claude Code on Autopilot

**What you build:** a two-agent workflow — the main agent writes code, a `test-runner` subagent verifies it — plus a hook that runs the tests automatically after every file edit.

**The one key idea:** one agent writes, another checks. Subagents get their own context and a narrow job; hooks make the check happen *every* time, not just when someone remembers.

**Worth knowing:**
- A subagent that can edit everything is just a second chance to make the same mess — restrict its tools to what its job needs.
- Hooks run shell commands on events (like PostToolUse). Keep them fast and quiet; a slow hook trains you to bypass it.
- Start with ONE hook (tests after edits). Add more only when a mistake repeats.

**Try this:** install `settings-hooks.json` as your project's `.claude/settings.json` and the `agents/test-runner.md` into `.claude/agents/`, then ask Claude to change any small thing and watch the tests fire on their own. Hint: break a test on purpose once — the loop fixing itself is the whole point.
