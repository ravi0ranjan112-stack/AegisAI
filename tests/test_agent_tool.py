from aegis.tools.agent import AgentTool


def test_agent_tool():
    tool = AgentTool()
    assert tool.run("add helper HelpUsers") == "OK"
    assert tool.run("show helper") == "HelpUsers"
