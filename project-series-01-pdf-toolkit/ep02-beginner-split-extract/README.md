# Episode 2 (Beginner) — Split a PDF and extract pages

## Why build this?

The flip side of merging: a 40-page contract arrives and you only need
pages 1 and 4 — the price and the signature. Uploading the whole thing
to a website to get two pages out is exactly what this toolkit avoids.

## The output

```bash
python solution.py extract ../samples/rental_contract.pdf "1, 4" -o key_pages.pdf
# Extracted 2 page(s) -> key_pages.pdf

python solution.py split ../samples/rental_contract.pdf --outdir pages/
# Split into 4 file(s) in pages/
```

## What you'll learn

- Writing one PDF per page with `PdfWriter.add_page()`
- **The episode's star:** `parse_pages()` — converting a human page
  spec like `"1-3, 5"` into 0-based indexes `[0, 1, 2, 4]`
- Raising friendly `ValueError`s instead of dumping tracebacks

## The key idea

**Humans count pages from 1; Python counts from 0.** Every page-range
bug in every PDF tool lives in that gap. `parse_pages()` is the one
place in the program that translates between the two worlds — and it
validates everything (backwards ranges, page 99 of a 7-page file,
letters instead of numbers) so the rest of the code can trust it.

## Worth knowing

- Quote the page spec in your terminal (`"1, 4"`) — otherwise the
  shell splits it into separate arguments.
- `reader.pages[i]` gives you a page object; a fresh `PdfWriter` per
  output file is the clean way to split.
- Friendly errors are a feature: "Page 9 doesn't exist — this PDF has
  7 page(s)" beats `IndexError: list index out of range` every time.

## Run it

```bash
python skeleton.py ../samples/rental_contract.pdf "1-3, 5" out.pdf
```

## Try this

Support an `all` keyword that selects every page, and make duplicate
pages (e.g. `"2, 2"`) collapse into one.
*Hint: handle the special case before the split(",") loop; use a set
for dedup, then sort.*

## Verified output

Extract `"1, 4"` from the rental contract → **2 pages**;
`parse_pages("1-3, 5", total=7)` → **`[0, 1, 2, 4]`**;
`parse_pages("9", 7)` → friendly error *"Page 9 doesn't exist — this
PDF has 7 page(s)."* ✔
