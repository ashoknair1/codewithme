"""Episode 4 (Intermediate) — PDF compressor + rotator. SKELETON.

Fill in the TODOs, then compare with solution.py. You'll need a scanned
PDF to practise on: run make_scan.py first.
"""
import sys
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter

LEVELS = {
    "low": (2400, 85),
    "medium": (1600, 65),
    "high": (1100, 40),
}


def compress_pdf(path, output, level="medium"):
    max_dim, quality = LEVELS[level]
    reader = PdfReader(path)
    writer = PdfWriter()
    writer.append(reader)
    for page in writer.pages:
        for img in page.images:
            # TODO 1: copy img.image; convert to RGB if it isn't RGB/L.
            # TODO 2: thumbnail it to (max_dim, max_dim) with Image.LANCZOS.
            # TODO 3: img.replace(new_image, quality=quality).
            pass
        # TODO 4: page.compress_content_streams() — squeezes text streams too.
    # TODO 5: write the writer to output; return (size_before, size_after).
    return 0, 0


def rotate_pages(path, spec_indexes, degrees, output):
    reader = PdfReader(path)
    writer = PdfWriter()
    writer.append(reader)
    # TODO 6: for each 0-based index, call writer.pages[idx].rotate(degrees).
    # TODO 7: write to output and return how many pages were rotated.
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python skeleton.py scanned_contract.pdf")
        raise SystemExit(1)
    before, after = compress_pdf(sys.argv[1], "compressed.pdf", "medium")
    print(f"{before:,} -> {after:,} bytes")
