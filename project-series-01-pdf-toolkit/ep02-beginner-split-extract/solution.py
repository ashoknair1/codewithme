"""Episode 2 (Beginner) — PDF splitter + page extractor. SOLUTION.

Usage:
    python solution.py split rental_contract.pdf --outdir pages/
    python solution.py extract rental_contract.pdf "1, 4" -o key_pages.pdf

Page ranges are typed the way humans think: "1-3, 5" means pages 1, 2, 3 and 5.
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_pages(spec, total):
    """Turn "1-3, 5" into 0-based page indexes [0, 1, 2, 4].

    Raises ValueError with a friendly message for anything out of range
    or malformed — never a raw traceback for a typing mistake.
    """
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            try:
                start, end = int(start_s), int(end_s)
            except ValueError:
                raise ValueError(f"'{part}' is not a valid page range. Try something like 1-3.")
            if start > end:
                raise ValueError(f"'{part}' goes backwards — the first number must be the smaller one.")
            pages.extend(range(start, end + 1))
        else:
            try:
                pages.append(int(part))
            except ValueError:
                raise ValueError(f"'{part}' is not a page number. Use numbers and ranges like 1-3, 5.")
    if not pages:
        raise ValueError("No pages given. Try something like 1-3, 5.")
    for p in pages:
        if p < 1 or p > total:
            raise ValueError(f"Page {p} doesn't exist — this PDF has {total} page(s).")
    return [p - 1 for p in pages]  # humans count from 1; Python counts from 0


def open_reader(path):
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError(f"'{path}' is password-protected. Unlock it first (Episode 5 shows how).")
    return reader


def split_pdf(path, outdir):
    reader = open_reader(path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(path).stem
    written = []
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out = outdir / f"{stem}_page_{i}.pdf"
        with open(out, "wb") as f:
            writer.write(f)
        written.append(out)
    return written


def extract_pages(path, spec, output):
    reader = open_reader(path)
    indexes = parse_pages(spec, len(reader.pages))
    writer = PdfWriter()
    for idx in indexes:
        writer.add_page(reader.pages[idx])
    with open(output, "wb") as f:
        writer.write(f)
    return len(indexes)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Split a PDF or extract pages — privately, on your computer.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_split = sub.add_parser("split", help="split into one PDF per page")
    p_split.add_argument("input")
    p_split.add_argument("--outdir", default="pages")

    p_ext = sub.add_parser("extract", help="extract pages like \"1-3, 5\"")
    p_ext.add_argument("input")
    p_ext.add_argument("pages")
    p_ext.add_argument("-o", "--output", default="extracted.pdf")

    args = parser.parse_args(argv)
    if not Path(args.input).is_file():
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        return 1
    try:
        if args.command == "split":
            written = split_pdf(args.input, args.outdir)
            print(f"Split into {len(written)} file(s) in {args.outdir}/")
        else:
            n = extract_pages(args.input, args.pages, args.output)
            print(f"Extracted {n} page(s) -> {args.output}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
