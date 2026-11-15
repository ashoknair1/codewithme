"""A tiny MCP server in Python (Ep 5) — a private notes tool for your agent.

Gives any MCP-capable agent (e.g. Claude Code) three tools backed by a
JSON file on YOUR disk: add_note, list_notes, read_note.

Run:  pip install mcp   then   python server.py   (speaks MCP over stdio)
Test: python test_server.py
"""
import json
import os

from mcp.server.mcpserver import MCPServer

NOTES_FILE = os.environ.get("NOTES_FILE", "notes.json")

mcp = MCPServer("notes")


def _load() -> dict:
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save(notes: dict) -> None:
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)


@mcp.tool()
def add_note(title: str, body: str) -> str:
    """Save a note under a title, replacing any note with the same title."""
    notes = _load()
    notes[title] = body
    _save(notes)
    return f"Saved note '{title}'."


@mcp.tool()
def list_notes() -> list[str]:
    """List the titles of all saved notes."""
    return sorted(_load().keys())


@mcp.tool()
def read_note(title: str) -> str:
    """Read the full text of the note saved under this exact title."""
    notes = _load()
    if title not in notes:
        return f"No note titled '{title}'."
    return notes[title]


if __name__ == "__main__":
    mcp.run()  # stdio transport — the agent starts the server itself
