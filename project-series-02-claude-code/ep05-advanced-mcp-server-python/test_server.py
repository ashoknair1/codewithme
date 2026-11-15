"""End-to-end test (Ep 5): talks to server.py through a REAL MCP client.

Run: python test_server.py  ->  prints ALL MCP TESTS PASS
"""
import asyncio
import os
import sys
import tempfile

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = os.path.dirname(os.path.abspath(__file__))


def _text(result) -> str:
    return " ".join(getattr(c, "text", "") for c in result.content)


async def main() -> None:
    tmp = tempfile.mkdtemp()
    env = dict(os.environ, NOTES_FILE=os.path.join(tmp, "notes.json"))
    params = StdioServerParameters(
        command=sys.executable, args=[os.path.join(HERE, "server.py")], env=env
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            names = sorted(t.name for t in tools.tools)
            assert names == ["add_note", "list_notes", "read_note"], names

            r = await session.call_tool(
                "add_note", {"title": "groceries", "body": "milk, eggs, coffee"}
            )
            assert "Saved note 'groceries'" in _text(r), _text(r)

            r = await session.call_tool("list_notes", {})
            assert "groceries" in _text(r), _text(r)

            r = await session.call_tool("read_note", {"title": "groceries"})
            assert "milk, eggs, coffee" in _text(r), _text(r)

            r = await session.call_tool("read_note", {"title": "missing"})
            assert "No note titled 'missing'" in _text(r), _text(r)

    print("ALL MCP TESTS PASS")


if __name__ == "__main__":
    asyncio.run(main())
