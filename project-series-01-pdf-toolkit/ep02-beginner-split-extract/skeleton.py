"""Episode 2 (Beginner) — PDF splitter + page extractor. SKELETON.

The star of this episode is parse_pages(). Fill in the TODOs, then
compare with solution.py.
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_pages(spec, total):
    """Turn "1-3, 5" into 0-based indexes. Friendly ValueErrors only."""
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            # TODO 1: split on "-", convert both ends to int (friendly error if not),
            # check start <= end, then extend pages with range(start, end + 1).
            pass
        else:
            # TODO 2: convert part to int (friendly error if not) and append it.
            pass
    # TODO 3: raise a friendly error if pages is empty.
    # TODO 4: raise a friendly error if any page is < 1 or > total.
    # TODO 5: return the list converted to 0-based indexes.
    return []


def extract_pages(path, spec, output):
    reader = PdfReader(path)
    indexes = parse_pages(spec, len(reader.pages))
    writer = PdfWriter()
    # TODO 6: add reader.pages[idx] for each index, then write to output.
    return len(indexes)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: python skeleton.py input.pdf "1-3, 5" output.pdf')
        raise SystemExit(1)
    n = extract_pages(sys.argv[1], sys.argv[2], sys.argv[3])
    print(f"Extracted {n} page(s) -> {sys.argv[3]}")
