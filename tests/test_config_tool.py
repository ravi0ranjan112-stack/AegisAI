from aegis.tools.config import ConfigTool


def test_config_tool():
    tool = ConfigTool()
    assert tool.run("set temp 0.7") == "OK"
    assert tool.run("get temp") == "0.7"
