"""Episode 5 (Advanced) — Protect tab + encrypted files. SKELETON.

The full app from Episode 4 is provided; your job is the new Protect
pieces, marked TODO. Compare with pdf_toolkit.py (the solution) after.
"""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog

import customtkinter as ctk
from pypdf import PdfReader, PdfWriter


def open_reader(path, password=None):
    reader = PdfReader(path)
    if reader.is_encrypted:
        # TODO 1: if password is None, raise a friendly ValueError.
        # TODO 2: call reader.decrypt(password) — it returns 0 on a WRONG
        # password instead of raising. Check for 0 and raise a friendly error.
        pass
    return reader


def protect_pdf(path, output, password):
    # TODO 3: refuse an empty password with a friendly ValueError.
    writer = PdfWriter()
    writer.append(PdfReader(path))
    # TODO 4: writer.encrypt(user_password=password, algorithm="AES-256")
    # (needs the `cryptography` package installed).
    # TODO 5: write the writer to output.
    pass


def ask_password(parent, path):
    # TODO 6: if PdfReader(path).is_encrypted is False, return None.
    # Otherwise return simpledialog.askstring(..., show="•", parent=parent).
    return None


# The rest of the window (Merge / Split / Compress / Rotate tabs) is the
# same as Episode 4's solution — see pdf_toolkit.py in this folder for
# the complete app with the Protect tab wired in.
