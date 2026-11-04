# Project Series 01 — The Private PDF Toolkit

**One real project, built progressively across six episodes, from your
first command-line tool to a packaged desktop app you could hand to a
friend.**

## Why build this?

Online PDF tools upload your contracts, invoices and bank statements
to someone else's server. This app does the same jobs — merge, split,
compress, rotate, protect — **entirely on your own computer**. Nothing
leaves your machine.

## Before Episode 1

```bash
pip install -r ../requirements.txt   # from the repo root, or see below
python make_samples.py               # creates the 3 fictional sample PDFs
```

This generates `samples/invoice.pdf` (1 page), `samples/receipts.pdf`
(2 pages) and `samples/rental_contract.pdf` (4 pages) — 7 pages total,
the number Episode 1 checks. See `samples/README.md`.

## The roadmap

| Episode | Level | What you build | Skills |
|---|---|---|---|
| [Ep 1](ep01-beginner-merge-cli/) | Beginner | Command-line PDF merger | `argparse`, file paths, `PdfWriter.append()`, error handling |
| [Ep 2](ep02-beginner-split-extract/) | Beginner | Splitter + page extractor | `parse_pages()` — turning `"1-3, 5"` into indexes, friendly errors, `add_page()` |
| [Ep 3](ep03-intermediate-desktop-app/) | Intermediate | Desktop app with Merge + Split tabs | CustomTkinter, `command=` without parentheses, `lambda`, the `mainloop()` event model |
| [Ep 4](ep04-intermediate-compress-rotate/) | Intermediate | Compress + Rotate | Shrinking embedded images with Pillow, `image.replace(quality=…)`, `/Rotate` flags, generating a realistic test scan |
| [Ep 5](ep05-advanced-protect/) | Advanced | Protect tab + encrypted-file handling | AES-256 encryption, `is_encrypted`, `decrypt()` return values, password UX |
| [Ep 6](ep06-expert-ship-it/) | Expert | Final app, test suite, packaging | Logic/UI separation (`core.py`), automated tests with plain asserts, PyInstaller for Windows/Mac |

Each episode ends where the next begins: the app grows a tab (or a
capability) every time, and Episodes 3–6 reuse the exact functions
written in Episodes 1–2.

## How to work through an episode

1. Open the episode's README — output first, then the key idea.
2. Code along in `skeleton.py`.
3. Compare with the solution when you're done (or stuck).
4. Do the **Try this** challenge before moving on.

## Verified output (this repo's code, actually run)

- Ep 1 merge of the three samples → **exactly 7 pages**
- Ep 2 extract `"1, 4"` from the rental contract → **2 pages**;
  `parse_pages("1-3, 5", 7)` → `[0, 1, 2, 4]`; page `9` → friendly error
- Ep 4 compress of the generated scan (Medium) → **8,360,974 → 1,067,333
  bytes (87% smaller)**; rotate page 3 → its `/Rotate` is **90**
- Ep 5 protect → `is_encrypted` is **True**; wrong password rejected
  with a friendly error, correct password opens all 4 pages
- Ep 6 `run_tests.py` → **ALL TESTS PASS** (8 checks)
