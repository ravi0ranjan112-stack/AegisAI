from aegis.config.settings import Settings


def test_settings() -> None:
    s = Settings()

    assert s.provider == "ollama"
    assert s.model == "llama3"
