from unittest.mock import Mock

from aegis.agent.loop import AgentLoop


def test_agent_loop() -> None:
    loop = AgentLoop()

    ctx = loop.run("Build AI", steps=3)

    assert ctx.goal == "Build AI"
    assert ctx.state.steps == 3
    assert ctx.state.completed


def test_agent_loop_executes_tool_call() -> None:
    llm = Mock()
    llm.ask.return_value = "<tool:shell>pwd</tool>"

    tools = Mock()
    tools.execute.return_value = "/home/ravi/Workspace/AegisAI"

    loop = AgentLoop(llm=llm, tools=tools)

    ctx = loop.run("Show current directory", steps=1)

    assert ctx.state.completed
    llm.ask.assert_called_once()
    tools.execute.assert_called_once_with("shell", "pwd")
