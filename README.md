# Code with me — channel code

All the code from the **Code with me** YouTube channel
([@codewithmeyt](https://www.youtube.com/@codewithmeyt)): Python for AI,
agentic AI with Claude, and project series that build real software
from beginner to expert.

## How this repo is organized

| Folder | What it is |
|---|---|
| `season-1-python-for-ai/` | Code from Season 1 of the daily Python-for-AI tutorial series, one folder per episode (`ep01`…`ep19`). |
| `project-series-01-pdf-toolkit/` | Project Series 01: build a complete **Private PDF Toolkit** across 6 episodes — CLI tools → desktop app → packaged software. Start at its README. |

## How each series folder works

Every episode folder contains:

- **`skeleton.py`** — the starting file from the video, with the key
  parts left as TODOs. **Write your code here first.**
- **`solution.py`** (or the named app file) — the complete, tested
  code from the end of the video. Use it to check your work, not
  instead of it.
- **`README.md`** — the episode notes: why we're building it, the key
  idea, real pitfalls, and a "Try this" challenge.

## Setup

```bash
git clone <this repo>
cd codewithme
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Then generate the sample PDFs for Project Series 01:

```bash
cd project-series-01-pdf-toolkit
python make_samples.py
```

## A note on privacy

The PDF toolkit in Project Series 01 exists because online PDF tools
upload your contracts, invoices and bank statements to someone else's
server. Everything in that series runs **100% on your own computer** —
no uploads, no accounts, no tracking.

## License / using this code

Written for learners following the channel. Use it, modify it, and
build on it for your own projects and learning.
