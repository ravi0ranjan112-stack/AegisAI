from aegis.config.loader import SettingsLoader


def test_loader() -> None:
    loader = SettingsLoader()

    settings = loader.load()

    assert settings.provider == "ollama"
    assert settings.model == "llama3"
