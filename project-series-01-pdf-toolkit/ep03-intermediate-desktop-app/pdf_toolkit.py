"""Episode 3 (Intermediate) — Private PDF Toolkit desktop app. SOLUTION.

A CustomTkinter window with Merge and Split tabs, built on the exact
logic from Episodes 1 and 2. Run it:

    python pdf_toolkit.py

Two rules of GUI programming to notice:
  * command= takes the FUNCTION NAME — no parentheses. command=merge
    means "run merge when clicked"; command=merge() would run it NOW,
    while the window is still being built.
  * To pass arguments, wrap the call in a lambda: command=lambda: ...
"""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk
from pypdf import PdfReader, PdfWriter


# ---------- PDF logic (from Episodes 1 & 2) ----------

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


def open_reader(path):
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError("That PDF is password-protected. Episode 5 adds unlocking.")
    return reader


def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()
    for path in input_paths:
        writer.append(open_reader(path))
    with open(output_path, "wb") as f:
        writer.write(f)
    return len(writer.pages)


def split_pdf(path, outdir):
    reader = open_reader(path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(path).stem
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        with open(outdir / f"{stem}_page_{i}.pdf", "wb") as f:
            writer.write(f)
    return len(reader.pages)


def extract_pages(path, spec, output):
    reader = open_reader(path)
    writer = PdfWriter()
    for idx in parse_pages(spec, len(reader.pages)):
        writer.add_page(reader.pages[idx])
    with open(output, "wb") as f:
        writer.write(f)


# ---------- The app ----------

class PdfToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Private PDF Toolkit")
        self.geometry("640x460")
        self.merge_files = []

        tabs = ctk.CTkTabview(self)
        tabs.pack(fill="both", expand=True, padx=12, pady=12)
        self._build_merge_tab(tabs.add("Merge"))
        self._build_split_tab(tabs.add("Split"))

    # ----- Merge tab -----
    def _build_merge_tab(self, tab):
        ctk.CTkButton(tab, text="Add PDFs…", command=self._add_files).pack(pady=(12, 6))
        self.merge_list = ctk.CTkLabel(tab, text="No files yet — add PDFs in merge order.")
        self.merge_list.pack(pady=4)
        # command=self._do_merge — NO parentheses. The button stores the
        # function and calls it on click, inside mainloop().
        ctk.CTkButton(tab, text="Merge", command=self._do_merge).pack(pady=10)

    def _add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        self.merge_files.extend(files)
        names = "\n".join(Path(f).name for f in self.merge_files) or "No files yet."
        self.merge_list.configure(text=names)

    def _do_merge(self):
        if len(self.merge_files) < 2:
            messagebox.showwarning("Merge", "Add at least two PDFs first.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".pdf",
                                           filetypes=[("PDF files", "*.pdf")])
        if not out:
            return
        try:
            pages = merge_pdfs(self.merge_files, out)
            messagebox.showinfo("Merge", f"Done — {pages} pages written to {Path(out).name}.")
        except ValueError as e:
            messagebox.showerror("Merge failed", str(e))

    # ----- Split tab -----
    def _build_split_tab(self, tab):
        self.split_path = tk.StringVar()
        row = ctk.CTkFrame(tab)
        row.pack(fill="x", pady=(12, 6))
        ctk.CTkEntry(row, textvariable=self.split_path, width=380).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Browse…", width=90,
                      command=lambda: self.split_path.set(
                          filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]) or self.split_path.get())
                      ).pack(side="left")
        # lambda lets us pass an argument ("split" / "extract") to one shared handler.
        ctk.CTkButton(tab, text="Split into single pages",
                      command=lambda: self._do_split("split")).pack(pady=6)
        self.pages_entry = ctk.CTkEntry(tab, placeholder_text="Pages to extract, e.g. 1-3, 5", width=300)
        self.pages_entry.pack(pady=4)
        ctk.CTkButton(tab, text="Extract pages",
                      command=lambda: self._do_split("extract")).pack(pady=6)

    def _do_split(self, mode):
        path = self.split_path.get()
        if not path:
            messagebox.showwarning("Split", "Choose a PDF first.")
            return
        try:
            if mode == "split":
                outdir = filedialog.askdirectory(title="Where should the pages go?")
                if not outdir:
                    return
                n = split_pdf(path, outdir)
                messagebox.showinfo("Split", f"Done — {n} single-page PDFs created.")
            else:
                out = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                   filetypes=[("PDF files", "*.pdf")])
                if not out:
                    return
                extract_pages(path, self.pages_entry.get(), out)
                messagebox.showinfo("Extract", f"Done — pages saved to {Path(out).name}.")
        except ValueError as e:
            messagebox.showerror("Split failed", str(e))


if __name__ == "__main__":
    # mainloop() hands control to the window: it waits for clicks and
    # calls your command= functions. Your code after this line runs
    # only when the window closes.
    PdfToolkit().mainloop()
