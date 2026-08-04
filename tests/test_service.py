from aegis.services.service import Service


def test_service() -> None:
    svc = Service("memory")

    assert svc.name == "memory"
    assert svc.enabled is True
