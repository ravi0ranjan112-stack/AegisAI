from aegis.providers.base import BaseAIProvider
from aegis.providers.registry import ProviderRegistry


class ProviderRouter:
    def __init__(
        self,
        registry: ProviderRegistry,
        default_provider: str,
    ) -> None:
        self._registry = registry
        self._active = default_provider

    @property
    def active(self) -> str:
        return self._active

    def set_active(self, name: str) -> None:
        if not self._registry.has(name):
            raise KeyError(f"Unknown provider: {name}")

        self._active = name

    def provider(self) -> BaseAIProvider:
        return self._registry.get(self._active)
