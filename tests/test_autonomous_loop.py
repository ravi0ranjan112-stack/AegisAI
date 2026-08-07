from unittest.mock import Mock

from aegis.agent.autonomous import AutonomousLoop
from aegis.agent.types import ToolCall


def test_autonomous_loop_executes_tool_call() -> None:
    ai = Mock()
    ai.ask.return_value = "<tool:shell>pwd</tool>"

    executor = Mock()
    executor.execute.return_value = "/home/ravi/Workspace/AegisAI"

    loop = AutonomousLoop(ai=ai, executor=executor)

    result = loop.run("Show current directory")

    assert result.handled
    assert "/home/ravi/Workspace/AegisAI" in result.result
    ai.ask.assert_called_once()
    executor.execute.assert_called_once_with(ToolCall(tool="shell", command="pwd"))
