"""Episode 3 (Intermediate) — Private PDF Toolkit desktop app. SKELETON.

Same window as the solution, with the wiring left as TODOs. The PDF
logic functions are complete (they came from Episodes 1 & 2) — your
job is the GUI: tabs, buttons, and the command=/lambda rules.
"""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
from pypdf import PdfReader, PdfWriter


def parse_pages(spec, total):
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


def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()
    for path in input_paths:
        writer.append(PdfReader(path))
    with open(output_path, "wb") as f:
        writer.write(f)
    return len(writer.pages)


def split_pdf(path, outdir):
    reader = PdfReader(path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(path).stem
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        with open(outdir / f"{stem}_page_{i}.pdf", "wb") as f:
            writer.write(f)
    return len(reader.pages)


class PdfToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Private PDF Toolkit")
        self.geometry("640x460")
        self.merge_files = []
        # TODO 1: create a CTkTabview, pack it, and add "Merge" and "Split" tabs.
        # TODO 2: call your _build_merge_tab / _build_split_tab on each tab.

    def _build_merge_tab(self, tab):
        # TODO 3: an "Add PDFs…" button with command=self._add_files (NO parentheses!).
        # TODO 4: a label showing the chosen file names.
        # TODO 5: a "Merge" button with command=self._do_merge.
        pass

    def _add_files(self):
        # TODO 6: filedialog.askopenfilenames, extend self.merge_files, refresh the label.
        pass

    def _do_merge(self):
        # TODO 7: warn if fewer than 2 files; asksaveasfilename; merge_pdfs();
        # showinfo on success, showerror with the ValueError message on failure.
        pass

    def _build_split_tab(self, tab):
        # TODO 8: a path entry + Browse button (use a lambda to set the path).
        # TODO 9: "Split into single pages" button: command=lambda: self._do_split("split")
        # TODO 10: a pages entry + "Extract pages" button using mode "extract".
        pass

    def _do_split(self, mode):
        # TODO 11: implement both modes like the solution: dialogs + split_pdf/extract.
        pass


if __name__ == "__main__":
    PdfToolkit().mainloop()
