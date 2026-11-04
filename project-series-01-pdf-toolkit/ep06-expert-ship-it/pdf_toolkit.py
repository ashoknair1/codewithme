"""Episode 6 (Expert) — Private PDF Toolkit, final app. SOLUTION.

The window code from Episode 5, now importing every PDF operation from
core.py. Run it:  python pdf_toolkit.py
Package it into a double-clickable app: see PACKAGING.md.
"""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog

import customtkinter as ctk
from pypdf import PdfReader

from core import (LEVELS, compress_pdf, extract_pages, merge_pdfs,
                  protect_pdf, rotate_pages, split_pdf)


def ask_password(parent, path):
    """If the file is encrypted, pop a password dialog; else None."""
    if not PdfReader(path).is_encrypted:
        return None
    return simpledialog.askstring("Password needed",
                                  f"'{Path(path).name}' is password-protected.\nEnter its password:",
                                  show="•", parent=parent)


# ---------- The app ----------

class PdfToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Private PDF Toolkit")
        self.geometry("660x500")
        self.merge_files = []

        tabs = ctk.CTkTabview(self)
        tabs.pack(fill="both", expand=True, padx=12, pady=12)
        self._build_merge_tab(tabs.add("Merge"))
        self._build_split_tab(tabs.add("Split"))
        self._build_compress_tab(tabs.add("Compress"))
        self._build_rotate_tab(tabs.add("Rotate"))
        self._build_protect_tab(tabs.add("Protect"))

    def _pick(self, var):
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            var.set(path)

    def _passwords_for(self, *paths):
        """Ask (via dialog) for passwords for any encrypted inputs."""
        result = {}
        for p in paths:
            pw = ask_password(self, p)
            if pw:
                result[p] = pw
        return result

    # ----- Merge -----
    def _build_merge_tab(self, tab):
        ctk.CTkButton(tab, text="Add PDFs…", command=self._add_files).pack(pady=(12, 6))
        self.merge_list = ctk.CTkLabel(tab, text="No files yet — add PDFs in merge order.")
        self.merge_list.pack(pady=4)
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
        out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not out:
            return
        try:
            pages = merge_pdfs(self.merge_files, out, self._passwords_for(*self.merge_files))
            messagebox.showinfo("Merge", f"Done — {pages} pages written to {Path(out).name}.")
        except ValueError as e:
            messagebox.showerror("Merge failed", str(e))

    # ----- Split -----
    def _build_split_tab(self, tab):
        self.split_path = tk.StringVar()
        row = ctk.CTkFrame(tab)
        row.pack(fill="x", pady=(12, 6))
        ctk.CTkEntry(row, textvariable=self.split_path, width=400).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Browse…", width=90, command=lambda: self._pick(self.split_path)).pack(side="left")
        ctk.CTkButton(tab, text="Split into single pages", command=lambda: self._do_split("split")).pack(pady=6)
        self.pages_entry = ctk.CTkEntry(tab, placeholder_text="Pages to extract, e.g. 1-3, 5", width=300)
        self.pages_entry.pack(pady=4)
        ctk.CTkButton(tab, text="Extract pages", command=lambda: self._do_split("extract")).pack(pady=6)

    def _do_split(self, mode):
        path = self.split_path.get()
        if not path:
            messagebox.showwarning("Split", "Choose a PDF first.")
            return
        try:
            pw = ask_password(self, path)
            if mode == "split":
                outdir = filedialog.askdirectory(title="Where should the pages go?")
                if not outdir:
                    return
                n = split_pdf(path, outdir, pw)
                messagebox.showinfo("Split", f"Done — {n} single-page PDFs created.")
            else:
                out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if not out:
                    return
                extract_pages(path, self.pages_entry.get(), out, pw)
                messagebox.showinfo("Extract", f"Done — pages saved to {Path(out).name}.")
        except ValueError as e:
            messagebox.showerror("Split failed", str(e))

    # ----- Compress -----
    def _build_compress_tab(self, tab):
        self.compress_path = tk.StringVar()
        self.level = tk.StringVar(value="medium")
        row = ctk.CTkFrame(tab)
        row.pack(fill="x", pady=(12, 6))
        ctk.CTkEntry(row, textvariable=self.compress_path, width=400).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Browse…", width=90, command=lambda: self._pick(self.compress_path)).pack(side="left")
        ctk.CTkOptionMenu(tab, values=list(LEVELS), variable=self.level).pack(pady=6)
        ctk.CTkButton(tab, text="Compress", command=self._do_compress).pack(pady=8)

    def _do_compress(self):
        path = self.compress_path.get()
        if not path:
            messagebox.showwarning("Compress", "Choose a PDF first.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not out:
            return
        try:
            before, after = compress_pdf(path, out, self.level.get(), ask_password(self, path))
            messagebox.showinfo("Compress", f"Done — {before:,} -> {after:,} bytes "
                                            f"({100 * (1 - after / before):.0f}% smaller).")
        except ValueError as e:
            messagebox.showerror("Compress failed", str(e))

    # ----- Rotate -----
    def _build_rotate_tab(self, tab):
        self.rotate_path = tk.StringVar()
        self.degrees = tk.IntVar(value=90)
        row = ctk.CTkFrame(tab)
        row.pack(fill="x", pady=(12, 6))
        ctk.CTkEntry(row, textvariable=self.rotate_path, width=400).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Browse…", width=90, command=lambda: self._pick(self.rotate_path)).pack(side="left")
        self.rotate_pages_entry = ctk.CTkEntry(tab, placeholder_text="Pages, e.g. 3 or 1-2", width=300)
        self.rotate_pages_entry.pack(pady=4)
        ctk.CTkOptionMenu(tab, values=["90", "180", "270"],
                          command=lambda v: self.degrees.set(int(v))).pack(pady=4)
        ctk.CTkButton(tab, text="Rotate", command=self._do_rotate).pack(pady=8)

    def _do_rotate(self):
        path = self.rotate_path.get()
        if not path:
            messagebox.showwarning("Rotate", "Choose a PDF first.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not out:
            return
        try:
            rotate_pages(path, self.rotate_pages_entry.get(), self.degrees.get(), out,
                         ask_password(self, path))
            messagebox.showinfo("Rotate", f"Done — saved to {Path(out).name}.")
        except ValueError as e:
            messagebox.showerror("Rotate failed", str(e))

    # ----- Protect (new in Episode 5) -----
    def _build_protect_tab(self, tab):
        self.protect_path = tk.StringVar()
        row = ctk.CTkFrame(tab)
        row.pack(fill="x", pady=(12, 6))
        ctk.CTkEntry(row, textvariable=self.protect_path, width=400).pack(side="left", padx=4)
        ctk.CTkButton(row, text="Browse…", width=90, command=lambda: self._pick(self.protect_path)).pack(side="left")
        # show="•" hides the password while typing — never echo real passwords.
        self.pw_entry = ctk.CTkEntry(tab, placeholder_text="New password", show="•", width=300)
        self.pw_entry.pack(pady=4)
        self.pw_confirm = ctk.CTkEntry(tab, placeholder_text="Repeat the password", show="•", width=300)
        self.pw_confirm.pack(pady=4)
        ctk.CTkButton(tab, text="Protect with AES-256", command=self._do_protect).pack(pady=8)
        ctk.CTkLabel(tab, text="There is no recovery if you forget this password.").pack()

    def _do_protect(self):
        path = self.protect_path.get()
        if not path:
            messagebox.showwarning("Protect", "Choose a PDF first.")
            return
        if self.pw_entry.get() != self.pw_confirm.get():
            messagebox.showerror("Protect", "The two passwords don't match. Try again.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not out:
            return
        try:
            protect_pdf(path, out, self.pw_entry.get())
            messagebox.showinfo("Protect", f"Done — {Path(out).name} is now encrypted with AES-256.")
        except ValueError as e:
            messagebox.showerror("Protect failed", str(e))


if __name__ == "__main__":
    PdfToolkit().mainloop()
