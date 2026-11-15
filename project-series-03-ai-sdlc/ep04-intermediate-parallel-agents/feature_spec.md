# Feature spec + parallel protocol (Ep 4) — Follow-up reminders for MiniCRM

## The feature (the contract all three agents share)
- A deal may carry `follow_up`: an ISO date string (YYYY-MM-DD) or null.
- POST /deals accepts it; POST /deals/<id>/follow-up sets or clears it.
- GET / summary gains `overdue`: titles of deals whose follow_up is before today and whose stage is not won/lost.
- Invalid date format → 400. Existing tests must stay green.

## The split
- **Agent A (author):** implements the feature in app.py only. No test edits.
- **Agent B (tester):** writes tests for every line of the contract above, including the 400 case and the won/lost exclusion. No app.py edits.
- **Agent C (reviewer):** reads the combined diff against this spec; reports findings most-serious-first; edits NOTHING.

## The merge (human)
1. Run the full suite. Red = send the failing test + diff back to the author, once.
2. Read the reviewer's findings; accept or consciously reject each in writing.
3. Only then commit — with the spec attached to the commit message.
