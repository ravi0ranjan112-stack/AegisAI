from aegis.tools.memory import MemoryTool


def test_memory_tool():
    tool = MemoryTool()

    assert tool.run("add hello") == "OK"
    assert "hello" in tool.run("search hello")
