from aegis.agent.executor import AgentExecutor
from aegis.agent.loop import AgentLoop
from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


def make_loop():
    registry = ToolFactory.create_registry()
    manager = ToolManager(registry)
    return AgentLoop(AgentExecutor(manager))


def test_normal():
    handled, result, _ = make_loop().run("hello")
    assert handled is False
    assert result == "hello"


def test_pwd():
    handled, result, _ = make_loop().run("pwd")
    assert handled is True
    assert isinstance(result, str)
    assert result
