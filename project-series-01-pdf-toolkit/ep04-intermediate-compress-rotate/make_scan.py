"""Generate a realistic 'scanned' contract PDF for Episode 4.

Real scans are just big photographs of pages inside a PDF. So this
script photographs (renders) four contract-like pages as large JPEGs
and embeds them. Page 3 was fed into the 'scanner' sideways — exactly
the kind of file the Compress and Rotate tools exist to fix.

Run:  python make_scan.py   ->  samples/scanned_contract.pdf
Uses reportlab + Pillow; the contract text is fictional.
"""
import random
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

OUT = Path(__file__).parent / "samples"
OUT.mkdir(exist_ok=True)

PAGE_W, PAGE_H = 1700, 2200  # ~200 dpi scan of a letter page

TITLES = [
    "STORAGE UNIT RENTAL AGREEMENT",
    "2. TERM AND PAYMENTS",
    "3. ACCESS AND SECURITY",
    "4. SIGNATURES",
]
BODIES = [
    "This fictional agreement is between Harbor Lane Storage LLC and tenant Alex Moreau for unit B-114 at 88 Dockside Road (a made-up address).",
    "Rent is $120 per month, due on the first. The gate code is personal and must never be shared with anyone else, ever, for any reason.",
    "Access hours are 6 AM to 10 PM daily. The tenant keeps the unit clean, stores nothing flammable, and insures their own belongings.",
    "Landlord: Harbor Lane Storage LLC ____________   Tenant: Alex Moreau ____________   Signed on a fictional date in 2026.",
]


def render_page(title, body, seed):
    """Draw one 'scanned' page: off-white paper, text lines, scanner noise."""
    rng = random.Random(seed)
    img = Image.new("RGB", (PAGE_W, PAGE_H), (246, 243, 235))
    draw = ImageDraw.Draw(img)
    draw.text((150, 150), title, fill=(30, 30, 30))
    # fake paragraph lines as soft grey bars, like blurred text at a glance
    y = 320
    words = body.split()
    line_len = 0
    for _ in words:
        w = rng.randint(60, 150)
        draw.rectangle([170, y, 170 + w, y + 16], fill=(90, 90, 90))
        line_len += w + 30
        if line_len > 1250:
            line_len = 0
            y += 52
    # scanner speckle noise — this is what makes the JPEG big, like a real scan
    px = img.load()
    for _ in range(260_000):
        x, y = rng.randrange(PAGE_W), rng.randrange(PAGE_H)
        shade = rng.randint(150, 235)
        px[x, y] = (shade, shade, shade - 12)
    # a coffee-ring 'stamp'
    draw.ellipse([1250, 1750, 1550, 2050], outline=(150, 40, 40), width=8)
    draw.text((1305, 1870), "PAID", fill=(150, 40, 40))
    return img


def main():
    path = OUT / "scanned_contract.pdf"
    c = canvas.Canvas(str(path), pagesize=LETTER)
    for i, (title, body) in enumerate(zip(TITLES, BODIES), start=1):
        img = render_page(title, body, seed=100 + i)
        if i == 3:
            img = img.rotate(-90, expand=True)  # fed into the scanner sideways
        buf = BytesIO()
        img.save(buf, "JPEG", quality=92)
        buf.seek(0)
        c.drawImage(ImageReader(buf), 0, 0, width=LETTER[0], height=LETTER[1],
                    preserveAspectRatio=True, anchor="c")
        c.showPage()
    c.save()
    size_kb = path.stat().st_size // 1024
    print(f"wrote {path} ({size_kb} KB, 4 pages, page 3 sideways)")


if __name__ == "__main__":
    main()
