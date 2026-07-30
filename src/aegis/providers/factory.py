from aegis.providers.mock.provider import MockProvider
from aegis.providers.ollama.provider import OllamaProvider
from aegis.providers.registry import ProviderRegistry


class ProviderFactory:
    @staticmethod
    def create_registry() -> ProviderRegistry:
        registry = ProviderRegistry()

        registry.register(MockProvider())

        try:
            registry.register(OllamaProvider())
        except Exception:
            # Ignore provider registration failures during startup.
            pass

        return registry
