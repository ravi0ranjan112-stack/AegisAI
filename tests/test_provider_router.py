from aegis.providers.mock.provider import MockProvider
from aegis.providers.registry import ProviderRegistry
from aegis.providers.router import ProviderRouter


def test_provider_router():
    registry = ProviderRegistry()

    provider = MockProvider()
    registry.register(provider)

    router = ProviderRouter(
        registry=registry,
        default_provider="mock",
    )

    assert router.active == "mock"
    assert router.provider() is provider
