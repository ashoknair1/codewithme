"""Episode 1 (Beginner) — Command-line PDF merger. SKELETON.

Fill in the TODOs, then compare with solution.py.
Run: python skeleton.py file1.pdf file2.pdf -o merged.pdf
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        # TODO 1: if reader.is_encrypted, raise a ValueError with a friendly message.
        # TODO 2: append the reader to the writer (writer.append(reader)).
        pass
    # TODO 3: open output_path in "wb" mode and writer.write(...) into it.
    # TODO 4: return the number of pages in the merged file.
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Merge PDFs privately, on your own computer.")
    parser.add_argument("inputs", nargs="+", help="PDF files to merge, in order")
    parser.add_argument("-o", "--output", default="merged.pdf")
    args = parser.parse_args(argv)

    # TODO 5: for each input, check it exists and ends in .pdf;
    # print an error to sys.stderr and return 1 if not.
    pages = merge_pdfs(args.inputs, args.output)
    print(f"Merged {len(args.inputs)} files -> {args.output} ({pages} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
