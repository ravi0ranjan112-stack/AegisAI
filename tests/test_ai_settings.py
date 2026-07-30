from aegis.ai.settings import AISettings


def test_default_settings():
    settings = AISettings()

    assert settings.provider == "mock"
    assert settings.model == "mock-v1"
    assert settings.offline is True
