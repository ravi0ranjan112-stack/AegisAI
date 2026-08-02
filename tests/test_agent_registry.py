from aegis.agents.registry import AgentRegistry


def test_agent_registry():
    registry = AgentRegistry()
    assert registry.execute("add coder WriteCode") == "OK"
    assert registry.execute("show coder") == "WriteCode"
