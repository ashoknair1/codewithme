# Deploy checklist — MiniCRM (Ep 6)

- [ ] Full suite green from a clean checkout (`python -m pytest -q`)
- [ ] requirements.txt pinned; fresh venv installs and runs from it
- [ ] One command starts the app, and the README says exactly what it is
- [ ] Debug mode off; no stack traces or file paths in error responses
- [ ] Data file location is explicit (MINICRM_DATA) and backed up before deploy
- [ ] The Ep 5 security review has no open high findings
- [ ] A fresh agent session, given only the README, can start the app — proof the docs are real
- [ ] Rollback is one sentence long: stop the process, restore the data file backup
