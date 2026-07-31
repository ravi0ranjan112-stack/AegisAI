from aegis.tools.base import BaseTool
from aegis.tools.registry import ToolRegistry


class DummyTool(BaseTool):
    @property
    def name(self) -> str:
        return "dummy"

    def run(self, command: str) -> str:
        return "OK"


def test_tool_registry():
    registry = ToolRegistry()

    registry.register(DummyTool())

    assert registry.has("dummy")
    assert registry.get("dummy").name == "dummy"
    assert registry.list_tools() == ["dummy"]
