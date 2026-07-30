from aegis.ai.manager import AIManager
from aegis.providers.mock.provider import MockProvider
from aegis.providers.registry import ProviderRegistry
from aegis.providers.router import ProviderRouter


def test_ai_manager():
    registry = ProviderRegistry()
    registry.register(MockProvider())

    router = ProviderRouter(
        registry=registry,
        default_provider="mock",
    )

    manager = AIManager(router)

    assert manager.active_provider == "mock"

    result = manager.ask("Hello")

    assert result == "Mock response: Hello"
