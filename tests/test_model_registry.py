from aegis.models.model import Model
from aegis.models.registry import ModelRegistry


def test_model_registry() -> None:
    registry = ModelRegistry()

    registry.register(
        Model(
            name="llama3",
            provider="ollama",
        )
    )

    model = registry.get("llama3")

    assert model.name == "llama3"
    assert model.provider == "ollama"
    assert registry.names() == ["llama3"]
