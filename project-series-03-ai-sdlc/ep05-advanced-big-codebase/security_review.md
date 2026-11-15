# Security + behavior review — legacy_report.py (Ep 5)

## Findings on the BEFORE state
1. **Personal data in output (high):** the report prints every contact's name *and email* — reports get forwarded; emails leak. Fix: names only, or masked emails.
2. **Bare `except:` (medium):** a corrupt data file and a missing file both become "no data" — real errors are silently swallowed. Fix: catch the specific errors, report the rest.
3. **No input validation (medium):** a deal missing `value` or `stage` crashes mid-report. Fix: validate at load, skip-and-count bad rows.
4. **String-built output (low):** fine at this size, but it's why the format drifts. Fix: build a list of lines, join once.

## Invariants the refactor must keep (pinned by tests first)
- Won total equals the sum of values of deals at stage `won` — exactly as today.
- A missing data file still produces a clear "no data" outcome (but now via an explicit check, not a swallowed exception).
- Contact lines keep the same order as the data file.

## Refactor brief (what the agent is told)
Fix findings 1–4 in `legacy_report.py` only. Keep the function name and return type. All invariant tests must pass unchanged; show the diff and the test output.
