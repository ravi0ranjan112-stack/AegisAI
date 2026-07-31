from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


def test_tool_manager_pwd():
    registry = ToolFactory.create_registry()
    manager = ToolManager(registry)

    result = manager.execute("shell", "pwd")

    assert result
    assert isinstance(result, str)


def test_tool_manager_invalid():
    registry = ToolFactory.create_registry()
    manager = ToolManager(registry)

    result = manager.execute("shell", "rm -rf /")

    assert "Command not allowed" in result
