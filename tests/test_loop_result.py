from aegis.agent.history import AgentHistory
from aegis.agent.result import LoopResult


def test_loop_result():
    result = LoopResult(
        handled=True,
        result="ok",
        history=AgentHistory(),
    )

    assert result.handled
    assert result.result == "ok"
