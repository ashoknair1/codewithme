"""Episode 4 (Intermediate) — PDF compressor + page rotator. SOLUTION.

Usage:
    python solution.py compress scanned_contract.pdf --level medium -o small.pdf
    python solution.py rotate scanned_contract.pdf "3" --degrees 270 -o fixed.pdf

Compress works on scanned PDFs because a scan is just a big photo inside
a PDF: shrink the photo, re-encode it at a lower JPEG quality, and the
whole file shrinks. Rotate only changes each page's /Rotate flag — the
pixels are untouched, so there is zero quality loss.
"""
import argparse
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter

# level name -> (max image dimension in px, JPEG quality)
LEVELS = {
    "low": (2400, 85),     # barely smaller, safest quality
    "medium": (1600, 65),  # the sweet spot for emailing scans
    "high": (1100, 40),    # smallest file, visibly softer text
}


def parse_pages(spec, total):
    """Same friendly "1-3, 5" parser from Episode 2."""
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
    return [p - 1 for p in pages]


def open_writer(path):
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError(f"'{path}' is password-protected. Unlock it first (Episode 5 shows how).")
    writer = PdfWriter()
    writer.append(reader)
    return writer


def compress_pdf(path, output, level="medium"):
    """Shrink embedded images. Returns (bytes_before, bytes_after)."""
    max_dim, quality = LEVELS[level]
    writer = open_writer(path)
    for page in writer.pages:
        for img in page.images:
            if img.image is None:
                continue
            new_img = img.image.copy()
            if new_img.mode not in ("RGB", "L"):
                new_img = new_img.convert("RGB")
            new_img.thumbnail((max_dim, max_dim), Image.LANCZOS)
            img.replace(new_img, quality=quality)
        page.compress_content_streams()
    with open(output, "wb") as f:
        writer.write(f)
    return Path(path).stat().st_size, Path(output).stat().st_size


def rotate_pages(path, spec, degrees, output):
    """Rotate the chosen pages. degrees must be 90, 180 or 270."""
    if degrees not in (90, 180, 270):
        raise ValueError("Rotation must be 90, 180 or 270 degrees.")
    writer = open_writer(path)
    indexes = parse_pages(spec, len(writer.pages))
    for idx in indexes:
        # rotate() only sets the page's /Rotate flag — no pixels change,
        # so rotating can never reduce quality.
        writer.pages[idx].rotate(degrees)
    with open(output, "wb") as f:
        writer.write(f)
    return len(indexes)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compress or rotate PDFs — privately, on your computer.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_c = sub.add_parser("compress", help="shrink a scanned PDF")
    p_c.add_argument("input")
    p_c.add_argument("--level", choices=list(LEVELS), default="medium")
    p_c.add_argument("-o", "--output", default="compressed.pdf")

    p_r = sub.add_parser("rotate", help="rotate pages like \"3\" or \"1-2\"")
    p_r.add_argument("input")
    p_r.add_argument("pages")
    p_r.add_argument("--degrees", type=int, default=90)
    p_r.add_argument("-o", "--output", default="rotated.pdf")

    args = parser.parse_args(argv)
    if not Path(args.input).is_file():
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        return 1
    try:
        if args.command == "compress":
            before, after = compress_pdf(args.input, args.output, args.level)
            saved = 100 * (1 - after / before)
            print(f"Compressed ({args.level}): {before:,} -> {after:,} bytes ({saved:.0f}% smaller) -> {args.output}")
        else:
            n = rotate_pages(args.input, args.pages, args.degrees, args.output)
            print(f"Rotated {n} page(s) by {args.degrees} degrees -> {args.output}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
