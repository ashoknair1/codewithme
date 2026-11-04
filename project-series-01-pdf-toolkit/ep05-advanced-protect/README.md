# Episode 5 (Advanced) — Password-protect PDFs (and open them again)

## Why build this?

The toolkit's last feature is the reason it exists: privacy. If you
must email a contract, you should be able to lock it first — and your
own tools shouldn't fall over the first time they meet a locked file.

## The output

The app gains a **Protect** tab: pick a PDF, type a password twice,
and get an AES-256-encrypted copy. And every other tab now handles
encrypted inputs gracefully: pick a locked file anywhere in the app
and a password dialog appears instead of a crash.

## What you'll learn

- `writer.encrypt(user_password=..., algorithm="AES-256")` — and why
  AES-256 needs the `cryptography` package installed
- `reader.is_encrypted` and the surprising contract of `decrypt()`:
  it returns `0` for a wrong password instead of raising
- Password UX: confirm fields, masked input (`show="•"`), and why
  there is no "forgot password" for PDFs you encrypt

## The key idea

**Check encryption at the door.** One helper — `open_reader(path,
password)` — is the only place files are opened. It detects
encryption, demands the password, verifies it via `decrypt()`'s
return value, and raises the same friendly `ValueError` style the
series has used since Episode 2. Every feature inherits the behavior
for free.

## Worth knowing

- pypdf's historic default encryption (RC4) is weak. Always pass
  `algorithm="AES-256"` explicitly — and note it silently requires
  `cryptography`; without it you get an error only when encrypting.
- An empty password "works" and protects nothing — the code refuses it.
- Encryption is not compression or editing protection: anyone *with*
  the password has the full document. That's the point of sharing it.

## Run it

```bash
python pdf_toolkit.py   # Protect tab is on the right
```

## Try this

Add an "Unlock" action: open an encrypted PDF with its password and
save an unencrypted copy.
*Hint: it's `open_reader(path, password)` feeding a plain
`PdfWriter` — if you don't call `encrypt()`, the copy is unlocked.*

## Verified output

Protecting the rental contract with a test password →
`reader.is_encrypted` is **True**; opening it with a wrong password
raises the friendly error *"Wrong password for that PDF."*; the
correct password opens all **4 pages** — and the locked file merges
successfully when its password is supplied. ✔
