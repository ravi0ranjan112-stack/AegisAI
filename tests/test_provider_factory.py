from aegis.providers.factory import ProviderFactory


def test_provider_factory() -> None:
    registry = ProviderFactory.create_registry()

    assert registry.has("mock")
    assert registry.has("ollama")

    assert set(registry.names()) == {"mock", "ollama"}
