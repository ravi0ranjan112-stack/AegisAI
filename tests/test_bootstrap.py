from aegis.integration.bootstrap import bootstrap


def test_bootstrap() -> None:
    kernel = bootstrap()

    assert kernel.agent is not None
    assert kernel.memory is not None
    assert kernel.workflow is not None
