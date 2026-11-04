# Episode 4 (Intermediate) — Compress scans and fix sideways pages

## Why build this?

Two everyday annoyances: a scanned contract that's 8 MB — too big to
email — and one page that came out of the scanner sideways. This
episode adds both fixes, plus the test file to prove them on.

## The output

First, manufacture a realistic scan (big embedded JPEG pages, page 3
fed in sideways):

```bash
python make_scan.py
# wrote samples/scanned_contract.pdf (8165 KB, 4 pages, page 3 sideways)

python solution.py compress samples/scanned_contract.pdf --level medium -o small.pdf
# Compressed (medium): 8,360,974 -> 1,067,333 bytes (87% smaller) -> small.pdf

python solution.py rotate samples/scanned_contract.pdf "3" --degrees 90 -o turned.pdf
```

## What you'll learn

- Why scans are huge: a scanned page is a **photograph** inside a PDF
- Shrinking images with Pillow `thumbnail()` and swapping them back
  with `image.replace(quality=...)`
- Three sensible compression levels instead of one magic setting
- Rotating pages by changing the `/Rotate` flag — no pixel surgery

## The key idea

**Compress the photo, not the PDF.** `page.images` hands you the
embedded pictures; shrink each one, re-encode it as a lower-quality
JPEG, and the file deflates. Rotation is the opposite philosophy:
`page.rotate(90)` only edits a metadata flag that tells viewers how
to display the page — the pixels are untouched, so rotating can
**never** lose quality.

## Worth knowing

- Compressing a text-born PDF (like our invoice) does almost nothing —
  there are no big images to shrink. Compression is a scans tool.
- `image.replace()` only works on images belonging to a `PdfWriter`
  (build the writer with `append()` first), and `thumbnail()` shrinks
  in place while keeping the aspect ratio.
- Levels are a trade: Medium (1600 px, quality 65) is the sweet spot
  for email; High is for "just make it send".

## Run it

```bash
python skeleton.py samples/scanned_contract.pdf
```

## Try this

Add a `--report` flag that prints the size of every embedded image
before compressing, sorted largest first.
*Hint: `len(img.data)` gives an image's stored size; collect
`(size, img.name)` pairs per page and sort descending.*

## Verified output

Generated scan: **8,360,974 bytes**. Medium compress → **1,067,333
bytes (87% smaller)**. Rotating page 3 by 90° → that page's `/Rotate`
is **90**, other pages untouched (0). ✔
