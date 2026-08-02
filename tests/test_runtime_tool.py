from aegis.tools.runtime import RuntimeTool


def test_runtime_tool():
    tool = RuntimeTool()
    assert tool.run("set mode auto") == "OK"
    assert tool.run("get mode") == "auto"
