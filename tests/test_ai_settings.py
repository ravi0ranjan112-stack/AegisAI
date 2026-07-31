from aegis.ai.settings import AISettings


def test_default_settings():
    settings = AISettings()

    assert settings.provider == "ollama"
    assert settings.model == "qwen2.5:3b"
    assert settings.offline is True
