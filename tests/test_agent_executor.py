from unittest.mock import MagicMock

from aegis.agent.executor import AgentExecutor
from aegis.agent.parser import ToolCall


def test_executor() -> None:
    manager = MagicMock()
    manager.execute.return_value = "HELLO"

    executor = AgentExecutor(manager)

    result = executor.execute(
        ToolCall(
            tool="echo",
            command="hello",
        )
    )

    assert result == "HELLO"
    manager.execute.assert_called_once_with("echo", "hello")
