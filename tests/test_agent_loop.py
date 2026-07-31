from aegis.agent.executor import AgentExecutor
from aegis.agent.loop import AgentLoop
from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


def test_loop_normal_response():
    registry = ToolFactory.create_registry()
    tools = ToolManager(registry)
    executor = AgentExecutor(tools)
    loop = AgentLoop(executor)

    handled, result = loop.handle("Hello!")

    assert handled is False
    assert result == "Hello!"


def test_loop_tool_call():
    registry = ToolFactory.create_registry()
    tools = ToolManager(registry)
    executor = AgentExecutor(tools)
    loop = AgentLoop(executor)

    handled, result = loop.handle("<tool:shell>\npwd\n</tool>")

    assert handled is True
    assert isinstance(result, str)
    assert result
