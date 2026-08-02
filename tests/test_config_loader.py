from aegis.config.loader import ConfigLoader


def test_config_loader():
    loader = ConfigLoader()
    assert loader.execute("set model llama") == "OK"
    assert loader.execute("get model") == "llama"
