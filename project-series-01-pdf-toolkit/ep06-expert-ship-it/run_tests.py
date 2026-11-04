"""Episode 6 (Expert) — test suite for core.py.

Runs with plain python3, no test framework needed:

    python run_tests.py

It first generates the sample PDFs if they don't exist yet, then runs
every check against core.py and prints PASS/FAIL per test. Exit code
is 0 only when everything passes — that's what makes it safe to ship.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
SERIES = HERE.parent
sys.path.insert(0, str(HERE))

from pypdf import PdfReader  # noqa: E402

import core  # noqa: E402

SAMPLES = SERIES / "samples"
SCAN = SERIES / "ep04-intermediate-compress-rotate" / "samples" / "scanned_contract.pdf"

FAILURES = []


def check(name, fn):
    try:
        fn()
        print(f"PASS  {name}")
    except Exception as e:  # noqa: BLE001 — a test harness should report, not crash
        FAILURES.append(name)
        print(f"FAIL  {name}: {type(e).__name__}: {e}")


def expect_value_error(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError("expected a friendly ValueError, got none")


def ensure_samples():
    if not (SAMPLES / "invoice.pdf").exists():
        subprocess.run([sys.executable, str(SERIES / "make_samples.py")], check=True)
    if not SCAN.exists():
        subprocess.run([sys.executable, str(SERIES / "ep04-intermediate-compress-rotate" / "make_scan.py")],
                       check=True)


def main():
    ensure_samples()
    tmp = Path(tempfile.mkdtemp(prefix="toolkit-tests-"))
    invoice = str(SAMPLES / "invoice.pdf")
    receipts = str(SAMPLES / "receipts.pdf")
    contract = str(SAMPLES / "rental_contract.pdf")

    def t_merge_order_and_count():
        out = tmp / "merged.pdf"
        n = core.merge_pdfs([invoice, receipts, contract], str(out))
        assert n == 7, n
        assert len(PdfReader(str(out)).pages) == 7
    check("merge: 3 samples merge to exactly 7 pages", t_merge_order_and_count)

    def t_parse_pages():
        assert core.parse_pages("1-3, 5", 7) == [0, 1, 2, 4]
        assert core.parse_pages("2", 7) == [1]
    check('parse_pages: "1-3, 5" -> [0, 1, 2, 4]', t_parse_pages)

    def t_parse_pages_errors():
        expect_value_error(lambda: core.parse_pages("9", 7))
        expect_value_error(lambda: core.parse_pages("3-1", 7))
        expect_value_error(lambda: core.parse_pages("abc", 7))
        expect_value_error(lambda: core.parse_pages("", 7))
    check("parse_pages: bad input raises friendly ValueError", t_parse_pages_errors)

    def t_extract():
        out = tmp / "key.pdf"
        core.extract_pages(contract, "1, 4", str(out))
        assert len(PdfReader(str(out)).pages) == 2
    check("extract: pages 1 and 4 of the contract -> 2 pages", t_extract)

    def t_split():
        outdir = tmp / "pages"
        n = core.split_pdf(contract, str(outdir))
        assert n == 4
        assert len(list(outdir.glob("*.pdf"))) == 4
    check("split: 4-page contract -> 4 single-page PDFs", t_split)

    def t_compress():
        out = tmp / "small.pdf"
        before, after = core.compress_pdf(str(SCAN), str(out), "medium")
        assert after < before, (before, after)
        print(f"      (scan {before:,} -> {after:,} bytes)")
    check("compress: medium level makes the scan smaller", t_compress)

    def t_rotate():
        out = tmp / "rot.pdf"
        core.rotate_pages(str(SCAN), "3", 90, str(out))
        assert PdfReader(str(out)).pages[2].get("/Rotate") == 90
    check("rotate: page 3 ends up with /Rotate == 90", t_rotate)

    def t_protect_roundtrip():
        out = tmp / "locked.pdf"
        core.protect_pdf(contract, str(out), "test-password-123")
        assert PdfReader(str(out)).is_encrypted
        expect_value_error(lambda: core.open_reader(str(out), "wrong"))
        expect_value_error(lambda: core.open_reader(str(out)))
        assert len(core.open_reader(str(out), "test-password-123").pages) == 4
    check("protect: AES-256 lock, wrong password rejected, right one opens", t_protect_roundtrip)

    print()
    if FAILURES:
        print(f"{len(FAILURES)} test(s) FAILED: {', '.join(FAILURES)}")
        return 1
    print("ALL TESTS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
