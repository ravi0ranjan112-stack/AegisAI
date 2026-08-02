from unittest.mock import MagicMock

from aegis.agent.autonomous import AutonomousLoop


def test_autonomous_loop() -> None:
    loop = AutonomousLoop(
        ai=MagicMock(),
        executor=MagicMock(),
    )

    result = loop.run("Build AI")

    assert result.handled
    assert "Build AI" in result.result
