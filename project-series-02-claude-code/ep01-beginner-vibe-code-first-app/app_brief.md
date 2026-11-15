# App brief — hand this to Claude Code (Ep 1)

Build me a small web app called **LinkSaver**.

WHAT IT DOES
- One page listing my saved links: title, URL, and one-line note for each.
- A form at the top to add a link (title, URL, note) and a delete button per link.
- Links are stored in a JSON file on disk so they survive a restart.

STACK
- Python + Flask for the server, plain HTML/CSS in one template, no build tools, no database.

MUST NEVER
- No user accounts, no external APIs, no JavaScript frameworks.
- Never delete the data file when the app restarts.

DONE WHEN
- I can run it with one command, open it in a browser, add a link, restart the app, and the link is still there.
- You show me the run output and a screenshot-style summary of the page working.
