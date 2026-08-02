from aegis.capabilities.models import Capability


class CapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        self._items[capability.name] = capability

    def get(self, name: str) -> Capability | None:
        return self._items.get(name)

    def all(self) -> list[Capability]:
        return list(self._items.values())


registry = CapabilityRegistry()
