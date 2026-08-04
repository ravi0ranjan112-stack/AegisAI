from aegis.services.service import Service
from aegis.services.service_registry import ServiceRegistry


def test_service_registry() -> None:
    registry = ServiceRegistry()

    registry.register(Service("memory"))

    assert registry.get("memory") is not None
    assert len(registry.services) == 1
