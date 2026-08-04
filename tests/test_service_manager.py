from aegis.services.service_manager import ServiceManager


def test_service_manager() -> None:
    manager = ServiceManager()

    manager.add("memory")

    assert manager.registry.get("memory") is not None
