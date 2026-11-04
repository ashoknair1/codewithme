# Episode 3 (Intermediate) — Turn it into a desktop app

## Why build this?

The command line is powerful, but nobody else in your house will ever
use it. This episode wraps Episodes 1–2 in a real window with buttons
— the moment the toolkit becomes something you can give to a person.

## The output

```bash
python pdf_toolkit.py
```

A "Private PDF Toolkit" window with two tabs — **Merge** (add PDFs,
click Merge, save) and **Split** (pick a file, split into single pages
or extract a page range like `1-3, 5`).

## What you'll learn

- Building a window with **CustomTkinter** and organizing it with tabs
- The `command=` rule: pass the function, **not** a function call
- Using `lambda` to pass arguments to a button handler
- How `mainloop()` changes the way your program flows
- File dialogs and message boxes (`filedialog`, `messagebox`)

## The key idea

**GUI programs don't run top-to-bottom — they wait.** `mainloop()` is
an event loop: it sits idle until a click happens, then calls the
function you registered with `command=`. That's why
`command=self._do_merge` (no parentheses) is correct and
`command=self._do_merge()` is a classic beginner bug — with
parentheses, Python runs the function *while building the window* and
hands the button its return value (`None`) instead.

## Worth knowing

- Buttons can't take arguments directly. `command=lambda: self._do_split("split")`
  wraps the call so the argument travels with it.
- Keep the PDF logic (imported from Episodes 1–2, unchanged) separate
  from the window code. The button handler's only jobs: gather inputs,
  call the logic, report the result.
- Catch your friendly `ValueError`s at the handler and show them with
  `messagebox.showerror` — that's the GUI version of Episode 2's
  friendly errors.

## Run it

```bash
python skeleton.py     # fill in the TODOs, then run your version
python pdf_toolkit.py  # the solution
```

## Try this

Add a "Clear list" button to the Merge tab, and show the total page
count of the merged file in the success message.
*Hint: `merge_pdfs()` already returns the page count — and for Clear,
a lambda that empties the list and resets the label is enough.*

## Verified output

`pdf_toolkit.py` passes `python3 -m py_compile` (checked headless; the
window itself needs a desktop to open). Its merge/split functions are
the Episode 1–2 code, verified there. ✔
