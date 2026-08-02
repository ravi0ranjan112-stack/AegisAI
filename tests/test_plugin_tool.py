from aegis.tools.plugin import PluginTool


def test_plugin_tool():
    tool = PluginTool()
    assert tool.run("load demo") == "OK"
    assert "demo" in tool.run("list")
