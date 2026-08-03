from aegis.agent.loop import AgentLoop


def test_agent_loop() -> None:
    loop = AgentLoop()

    ctx = loop.run("Build AI", steps=3)

    assert ctx.goal == "Build AI"
    assert ctx.state.steps == 3
    assert ctx.state.completed
