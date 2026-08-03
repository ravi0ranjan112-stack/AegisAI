from aegis.tools.memory import MemoryTool


def test_memory_tool():
    tool = MemoryTool()

    assert tool.run("add hello world") == "OK"
    assert "hello world" in tool.run("search hello")
    assert tool.run("clear") == "OK"
