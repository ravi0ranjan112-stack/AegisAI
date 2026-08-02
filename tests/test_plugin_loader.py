from aegis.plugins.loader import PluginLoader


def test_loader():
    assert PluginLoader().load("demo").name == "demo"
