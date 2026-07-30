from aegis.capabilities.models import Capability
from aegis.capabilities.registry import CapabilityRegistry


def test_capability_registry():
    registry = CapabilityRegistry()

    registry.register(Capability(name="python", available=True, description="Python Runtime"))

    cap = registry.get("python")

    assert cap is not None
    assert cap.available
    assert cap.name == "python"
