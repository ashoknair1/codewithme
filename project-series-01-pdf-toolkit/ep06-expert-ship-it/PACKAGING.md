# Packaging the Private PDF Toolkit into a real app (Episode 6)

PyInstaller turns your Python project into a double-clickable app that
runs on machines **without Python installed**. One rule before anything
else:

> **Build on the target OS.** A Windows `.exe` must be built on Windows,
> a Mac app on a Mac. PyInstaller does not cross-compile.

## 1. Set up a clean environment

```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac:      source venv/bin/activate
pip install pypdf pillow customtkinter cryptography pyinstaller
```

## 2. Test before you package

```bash
python run_tests.py     # must end with: ALL TESTS PASS
python pdf_toolkit.py   # click through every tab once
```

Never package code you haven't just run — packaging freezes your bugs
in place and makes them harder to debug.

## 3. Build

From this folder (`ep06-expert-ship-it/`):

```bash
pyinstaller --windowed --name "Private PDF Toolkit" --icon app.ico pdf_toolkit.py
```

- `--windowed` — no console window pops up behind the app (on Mac this
  produces a `.app` bundle).
- `--name` — the app's display name; spaces are fine inside quotes.
- `--icon app.ico` — Windows wants `.ico`, Mac wants `.icns`
  (`--icon app.icns`). Skip the flag if you don't have an icon yet.
- The entry point is `pdf_toolkit.py`; PyInstaller follows its import
  of `core.py` automatically.

## 4. Find and test the output

```
dist/Private PDF Toolkit/     <- the folder you ship (Windows)
dist/Private PDF Toolkit.app  <- the bundle you ship (Mac)
```

Copy it to a machine (or user account) **without** your dev setup and
run every tab there. First launch is slow — that's normal for
PyInstaller apps, which unpack themselves on start.

## 5. Worth knowing

- **Antivirus false positives (Windows):** freshly built PyInstaller
  exes are sometimes flagged by Windows Defender. It's a known
  annoyance for unsigned apps; code-signing is the real fix and is
  beyond this episode.
- **`cryptography` must be installed at build time** or the Protect tab
  will fail on AES-256 inside the packaged app — and it fails only when
  a user clicks it, which is why step 2's click-through matters.
- **One-folder vs one-file:** adding `--onefile` gives a single exe but
  starts slower and trips antivirus more often. Ship the one-folder
  build unless you have a reason not to.
- **Version your builds:** name the zip you share
  `Private-PDF-Toolkit-v1.0.zip` and keep the source commit it was
  built from. Future-you will ask.
