# Episode 1 (Beginner) — Merge PDFs from the command line

## Why build this?

You have an invoice, two receipts and a contract, and an online tool
wants you to upload all of them to merge them. For private documents,
that's a bad trade. This episode builds the merger yourself — and it's
the foundation the whole series stands on.

## The output

```bash
python make_samples.py        # once, from the series folder — creates samples/
python solution.py ../samples/invoice.pdf ../samples/receipts.pdf ../samples/rental_contract.pdf -o merged.pdf
# Merged 3 files -> merged.pdf (7 pages)
```

## What you'll learn

- Reading command-line arguments with `argparse` (inputs + `-o`)
- Checking files exist (and really are PDFs) before doing work
- `PdfWriter.append()` vs adding pages one by one
- Detecting password-protected files with `reader.is_encrypted`

## The key idea

**A PDF writer is a bucket.** You open each input PDF with
`PdfReader`, tip it into a `PdfWriter` with `append()`, and pour the
bucket into one output file. Order matters: files merge in exactly the
order you list them.

## Worth knowing

- `append()` preserves bookmarks and form fields better than looping
  `add_page()` over every page — prefer it for whole-file merges.
- An encrypted PDF will happily sit in the bucket and then fail at
  write time or produce a broken file. Check `is_encrypted` up front
  and fail with a message a human understands.
- Always write in binary mode (`"wb"`) — PDFs are not text.

## Run it

```bash
python skeleton.py ../samples/invoice.pdf ../samples/receipts.pdf -o test.pdf
```

## Try this

Make the tool refuse to overwrite an existing output file unless a
`--force` flag is given.
*Hint: `pathlib.Path(output).exists()` plus one more `add_argument`.*

## Verified output

`solution.py` merged invoice (1) + receipts (2) + rental contract (4)
into **exactly 7 pages**. ✔
