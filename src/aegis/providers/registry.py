from aegis.providers.base import BaseAIProvider


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, BaseAIProvider] = {}

    def register(self, provider: BaseAIProvider) -> None:
        self._providers[provider.name] = provider

    def get(self, name: str) -> BaseAIProvider:
        if name not in self._providers:
            raise KeyError(f"Provider '{name}' not registered.")
        return self._providers[name]

    def has(self, name: str) -> bool:
        return name in self._providers

    def names(self) -> list[str]:
        return sorted(self._providers.keys())
