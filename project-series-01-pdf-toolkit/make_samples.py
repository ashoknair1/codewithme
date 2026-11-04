"""Generate the three fictional sample PDFs used across the series.

Run once:  python make_samples.py
Creates samples/invoice.pdf (1 page), samples/receipts.pdf (2 pages)
and samples/rental_contract.pdf (4 pages). All names, companies and
amounts are fictional — invented for this tutorial series.
"""
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

OUT = Path(__file__).parent / "samples"
OUT.mkdir(exist_ok=True)


def header(c, title, page_no):
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 720, title)
    c.setFont("Helvetica", 10)
    c.drawString(72, 60, f"Page {page_no} — fictional sample document")


def make_invoice():
    path = OUT / "invoice.pdf"
    c = canvas.Canvas(str(path), pagesize=LETTER)
    header(c, "INVOICE #INV-2041 — Maple & Main Design Studio", 1)
    c.setFont("Helvetica", 12)
    lines = [
        "Billed to: Jordan Alvarez (fictional client)",
        "",
        "Website refresh deposit ............ $1,200.00",
        "Logo touch-up ...................... $  350.00",
        "Hosting setup ...................... $   95.00",
        "",
        "TOTAL DUE .......................... $1,645.00",
        "",
        "Payment terms: net 14 days. Thank you for your business!",
    ]
    y = 680
    for line in lines:
        c.drawString(72, y, line)
        y -= 24
    c.showPage()
    c.save()
    print(f"wrote {path} (1 page)")


def make_receipts():
    path = OUT / "receipts.pdf"
    c = canvas.Canvas(str(path), pagesize=LETTER)
    receipts = [
        ("RECEIPT — Corner Grocery (fictional)", ["Milk, eggs, bread", "Total: $18.42", "Paid by card •••• 4021"]),
        ("RECEIPT — City Transit Pass (fictional)", ["Monthly pass — November", "Total: $75.00", "Paid online, ref TX-88123"]),
    ]
    for i, (title, lines) in enumerate(receipts, start=1):
        header(c, title, i)
        c.setFont("Helvetica", 12)
        y = 680
        for line in lines:
            c.drawString(72, y, line)
            y -= 24
        c.showPage()
    c.save()
    print(f"wrote {path} (2 pages)")


def make_contract():
    path = OUT / "rental_contract.pdf"
    c = canvas.Canvas(str(path), pagesize=LETTER)
    sections = [
        ("1. Parties and Property", "This fictional lease is between Priya Nair (landlord) and Sam Whitfield (tenant) for the apartment at 412 Willow Lane, Unit 3 (a made-up address)."),
        ("2. Term and Rent", "The term is 12 months. Monthly rent is $1,450, due on the first day of each month. A late fee of $50 applies after the fifth day."),
        ("3. Deposit and Utilities", "Security deposit: $1,450, refundable per local law. The tenant pays electricity and internet; the landlord pays water and trash."),
        ("4. Signatures", "Landlord: Priya Nair ____________   Tenant: Sam Whitfield ____________   Date: a fictional date in 2026."),
    ]
    for i, (title, body) in enumerate(sections, start=1):
        header(c, f"RENTAL AGREEMENT — Section {title}", i)
        c.setFont("Helvetica", 12)
        # wrap the body text crudely into lines of ~78 chars
        words, line, y = body.split(), "", 660
        for word in words:
            if len(line) + len(word) + 1 > 78:
                c.drawString(72, y, line)
                y -= 22
                line = word
            else:
                line = f"{line} {word}".strip()
        if line:
            c.drawString(72, y, line)
        c.showPage()
    c.save()
    print(f"wrote {path} (4 pages)")


if __name__ == "__main__":
    make_invoice()
    make_receipts()
    make_contract()
    print("Done — 7 pages total across the three files.")
