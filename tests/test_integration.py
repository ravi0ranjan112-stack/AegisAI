from aegis.integration.manager import IntegrationManager


def test_integration() -> None:
    manager = IntegrationManager()

    assert manager.ready() is True
