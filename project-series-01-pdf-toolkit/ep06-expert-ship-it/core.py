"""Episode 6 (Expert) — the toolkit's engine, with no GUI in it.

Every PDF operation lives here, separate from the window code, so it
can be imported and tested on its own (see run_tests.py). This split —
logic in one module, interface in another — is what turns a script
into a project.
"""
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter


def parse_pages(spec, total):
    """Turn "1-3, 5" into 0-based page indexes, with friendly errors."""
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


def open_reader(path, password=None):
    """Open a PDF. If it's encrypted you must pass the password —
    a wrong or missing password raises a friendly ValueError."""
    reader = PdfReader(path)
    if reader.is_encrypted:
        if password is None:
            raise ValueError("That PDF is password-protected — a password is needed to open it.")
        # decrypt() returns 0 when the password is wrong; it does NOT raise.
        if reader.decrypt(password) == 0:
            raise ValueError("Wrong password for that PDF. Nothing was changed.")
    return reader


def open_writer(path, password=None):
    reader = open_reader(path, password)
    writer = PdfWriter()
    writer.append(reader)
    return writer


def merge_pdfs(input_paths, output_path, passwords=None):
    passwords = passwords or {}
    writer = PdfWriter()
    for path in input_paths:
        writer.append(open_reader(path, passwords.get(path)))
    with open(output_path, "wb") as f:
        writer.write(f)
    return len(writer.pages)


def split_pdf(path, outdir, password=None):
    reader = open_reader(path, password)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(path).stem
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        with open(outdir / f"{stem}_page_{i}.pdf", "wb") as f:
            writer.write(f)
    return len(reader.pages)


def extract_pages(path, spec, output, password=None):
    reader = open_reader(path, password)
    writer = PdfWriter()
    for idx in parse_pages(spec, len(reader.pages)):
        writer.add_page(reader.pages[idx])
    with open(output, "wb") as f:
        writer.write(f)


LEVELS = {"low": (2400, 85), "medium": (1600, 65), "high": (1100, 40)}


def compress_pdf(path, output, level="medium", password=None):
    max_dim, quality = LEVELS[level]
    writer = open_writer(path, password)
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


def rotate_pages(path, spec, degrees, output, password=None):
    if degrees not in (90, 180, 270):
        raise ValueError("Rotation must be 90, 180 or 270 degrees.")
    writer = open_writer(path, password)
    for idx in parse_pages(spec, len(writer.pages)):
        writer.pages[idx].rotate(degrees)
    with open(output, "wb") as f:
        writer.write(f)


def protect_pdf(path, output, password):
    """Copy a PDF and lock the copy with AES-256 encryption."""
    if not password:
        raise ValueError("Choose a password first — an empty password protects nothing.")
    writer = open_writer(path)
    # algorithm="AES-256" is the strong modern option; it requires the
    # `cryptography` package. The default (RC4-128) is weak and outdated.
    writer.encrypt(user_password=password, algorithm="AES-256")
    with open(output, "wb") as f:
        writer.write(f)

