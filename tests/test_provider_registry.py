from aegis.providers.mock.provider import MockProvider
from aegis.providers.registry import ProviderRegistry


def test_provider_registry():
    registry = ProviderRegistry()

    provider = MockProvider()
    registry.register(provider)

    assert registry.has("mock")
    assert registry.get("mock") is provider
    assert registry.names() == ["mock"]
