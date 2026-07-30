from aegis.tools.base import BaseTool
from aegis.tools.registry import ToolRegistry


class DummyTool(BaseTool):
    name = "dummy"
    description = "Test tool"

    def execute(self):
        return "OK"


def test_tool_registry():
    registry = ToolRegistry()

    registry.register(DummyTool())

    assert registry.get("dummy") is not None
    assert registry.list_tools() == ["dummy"]
