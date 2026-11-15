# Ep 5 (Advanced) — Build Your Own MCP Server in Python

**What you build:** a real MCP (Model Context Protocol) server in Python that gives Claude Code three new tools — `add_note`, `list_notes`, `read_note` — backed by a JSON file on your disk. Your notes never leave your machine.

**The one key idea:** MCP is a USB port for AI. Build a tool once, in the open protocol, and any MCP-capable agent (Claude Code included) can plug into it.

**Worth knowing:**
- A tool is just a typed Python function — the docstring becomes the description the model reads, so write it like instructions, not comments.
- Keep tools small and honest: one job each, plain-text answers, friendly errors ("No note titled X") instead of exceptions.
- Your server runs locally over stdio — no ports, no hosting, nothing to secure beyond your own machine.

**Run it:** `pip install mcp` (the current 2.x SDK — the server class is `MCPServer`) then `python test_server.py` — it starts the server, calls all three tools through a real MCP client, and prints ALL MCP TESTS PASS. Verified working Nov 14, 2026. To use it in Claude Code, register the server command (`python /path/to/server.py`) in your MCP settings.

**Try this:** add a `delete_note` tool. Hint: it's `_load()`, `pop()`, `_save()` — and a friendly message when the title doesn't exist.
