# PLAN — MiniCRM v1 (Ep 1). Each step has a success test; the agent stops when one fails.

1. **Skeleton + storage** — Flask app with load/save of the JSON data file. ✅ Test: app starts, GET / returns zero counts.
2. **Contacts** — POST /contacts with name validation. ✅ Test: empty name → 400; valid name → 201 and persisted.
3. **Deals + stages** — POST /deals (value ≥ 0, stage starts at lead) and POST /deals/<id>/stage with the fixed stage list. ✅ Tests: bad value → 400, unknown stage → 400, unknown deal → 404.
4. **Summary** — GET / returns counts + per-stage money totals. ✅ Test: full flow (contact → deal → won) shows won total equal to the deal value.
5. **Suite green** — `python -m pytest -q` all passing from a clean checkout.
