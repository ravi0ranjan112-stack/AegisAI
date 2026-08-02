from aegis.agent.history import AgentHistory


def test_history_render():
    history = AgentHistory()

    history.add("tool: pwd")
    history.add("result: /tmp")

    assert history.render() == "tool: pwd\n\nresult: /tmp"
