# Episode 6 (Expert) — Ship it: structure, tests, and a real app

## Why build this?

Everything works — on your machine, when you run it. The expert step
is making it work for *someone else*: code organized so it can be
tested automatically, a test suite that proves it still works after
every change, and a packaged app that runs without Python installed.

## The output

```
ep06-expert-ship-it/
├── core.py          # every PDF operation — no GUI code in here
├── pdf_toolkit.py   # the window; imports everything from core.py
├── run_tests.py     # python run_tests.py  ->  ALL TESTS PASS
└── PACKAGING.md     # exact PyInstaller steps for Windows and Mac
```

```bash
python run_tests.py
# PASS  merge: 3 samples merge to exactly 7 pages
# PASS  parse_pages: "1-3, 5" -> [0, 1, 2, 4]
# PASS  parse_pages: bad input raises friendly ValueError
# PASS  extract: pages 1 and 4 of the contract -> 2 pages
# PASS  split: 4-page contract -> 4 single-page PDFs
# PASS  compress: medium level makes the scan smaller
# PASS  rotate: page 3 ends up with /Rotate == 90
# PASS  protect: AES-256 lock, wrong password rejected, right one opens
# ALL TESTS PASS
```

## What you'll learn

- Splitting a program into an engine (`core.py`) and an interface
  (`pdf_toolkit.py`) — and why tests are the reason for the split
- Writing a real test suite with plain `assert`s (no framework needed)
- Packaging with PyInstaller: `--windowed`, `--name`, `--icon`, and
  the build-on-the-target-OS rule

## The key idea

**If it isn't tested, it's a rumor.** Every number this series has
claimed — 7 pages, `[0, 1, 2, 4]`, 87% smaller, `/Rotate == 90`,
wrong password rejected — is now an automated check. Change anything,
run `python run_tests.py`, and know in seconds whether you broke the
toolkit. That confidence is what "expert" actually means in practice.

## Worth knowing

- The tests generate their own fixtures (samples + scan) if missing,
  so the suite runs from a fresh clone.
- PyInstaller builds must happen **on the target OS** — no
  cross-compiling. See `PACKAGING.md` for the full steps and the
  antivirus/code-signing realities.
- Test the packaged app by clicking the Protect tab: `cryptography`
  must have been present at build time, and packaging bugs love to
  hide in features you didn't click.

## Run it

```bash
python run_tests.py      # the gate: never ship on a red suite
python pdf_toolkit.py    # the final app
```

## Try this

Add a regression test for a bug class from earlier episodes: merging
an encrypted PDF *without* its password must raise the friendly
error, and `parse_pages("2, 2", 7)` behavior must match whatever
Episode 2's solution does today.
*Hint: reuse `expect_value_error()` in run_tests.py; if your Ep 2
Try-This dedup changed the behavior, the test documents the new one.*

## Verified output

`run_tests.py` → **8/8 checks PASS, "ALL TESTS PASS"**, including
compress **8,360,974 → 1,067,333 bytes** inside the suite. ✔
