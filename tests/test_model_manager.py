from aegis.models.manager import ModelManager
from aegis.models.model import Model


def test_model_manager() -> None:
    manager = ModelManager()

    manager.register(
        Model(
            name="llama3",
            provider="ollama",
        ),
        task="chat",
    )

    model = manager.resolve("chat")

    assert model.name == "llama3"
    assert model.provider == "ollama"
