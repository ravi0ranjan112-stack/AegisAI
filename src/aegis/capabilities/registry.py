from aegis.capabilities.models import Capability


class CapabilityRegistry:
    def __init__(self):
        self._items: dict[str, Capability] = {}

    def register(self, capability: Capability):
        self._items[capability.name] = capability

    def get(self, name: str):
        return self._items.get(name)

    def all(self):
        return list(self._items.values())
