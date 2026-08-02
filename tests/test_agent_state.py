from aegis.agent.state import AgentState


def test_state_counts_steps():
    state = AgentState(max_steps=2)

    assert not state.finished

    state.next_step()
    assert state.steps == 1
    assert not state.finished

    state.next_step()
    assert state.finished
