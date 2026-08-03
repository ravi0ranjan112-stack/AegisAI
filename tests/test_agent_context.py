from aegis.agent.context import AgentContext


def test_agent_context() -> None:
    ctx = AgentContext("Build AI")

    assert ctx.goal == "Build AI"
    assert ctx.state.goal == "Build AI"
    assert not ctx.state.finished
