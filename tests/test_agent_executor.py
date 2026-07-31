from aegis.agent.executor import AgentExecutor
from aegis.agent.types import ToolCall
from aegis.tools.factory import ToolFactory
from aegis.tools.manager import ToolManager


def test_executor_shell():
    registry = ToolFactory.create_registry()
    tools = ToolManager(registry)

    executor = AgentExecutor(tools)

    result = executor.execute(
        ToolCall(
            tool="shell",
            command="pwd",
        )
    )

    assert isinstance(result, str)
    assert result
