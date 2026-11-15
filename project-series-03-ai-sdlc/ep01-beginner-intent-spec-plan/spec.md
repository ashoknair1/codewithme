# SPEC — MiniCRM v1 (Ep 1). Approved before any code was written.

## What it does
- Contacts: add a contact (name required, email optional); list count.
- Deals: add a deal (title, non-negative value, optional contact); every deal starts at stage `lead`.
- Pipeline: move a deal between stages — lead, qualified, proposal, won, lost.
- Summary: one view showing contact count, deal count, and the money total per stage.

## Stack
- Python + Flask, JSON file storage on local disk, no database, no accounts, no external services.

## Must never
- Never lose data on restart; never accept a negative deal value or an unknown stage.
- Never expose a stack trace or internal path in an error response.

## Done when
- The pytest suite in `project/tests/` passes.
- Add a contact, add a deal, move it to `won`, restart the app — the summary still shows it, with the won total correct.
