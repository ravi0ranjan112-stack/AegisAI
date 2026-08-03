from aegis.agent.manager import AgentManager


def test_agent_manager() -> None:
    manager = AgentManager()

    ctx = manager.execute("Build AI")

    assert ctx.goal == "Build AI"
    assert ctx.state.steps == 3
    assert ctx.state.completed
