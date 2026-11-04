"""Episode 1 (Beginner) — Command-line PDF merger. SOLUTION.

Usage:
    python solution.py invoice.pdf receipts.pdf rental_contract.pdf -o merged.pdf

Merges PDFs in the order you list them. Nothing is uploaded anywhere —
everything happens on your own computer.
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def merge_pdfs(input_paths, output_path):
    """Merge input_paths (in order) into output_path. Returns page count."""
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        if reader.is_encrypted:
            raise ValueError(f"'{path}' is password-protected. Unlock it first (Episode 5 shows how).")
        writer.append(reader)  # append() keeps bookmarks/form fields better than add_page loops
    with open(output_path, "wb") as f:
        writer.write(f)
    return len(writer.pages)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Merge PDFs privately, on your own computer.")
    parser.add_argument("inputs", nargs="+", help="PDF files to merge, in order")
    parser.add_argument("-o", "--output", default="merged.pdf", help="output file (default: merged.pdf)")
    args = parser.parse_args(argv)

    for path in args.inputs:
        if not Path(path).is_file():
            print(f"Error: file not found: {path}", file=sys.stderr)
            return 1
        if Path(path).suffix.lower() != ".pdf":
            print(f"Error: not a PDF file: {path}", file=sys.stderr)
            return 1

    try:
        pages = merge_pdfs(args.inputs, args.output)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(f"Merged {len(args.inputs)} files -> {args.output} ({pages} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
