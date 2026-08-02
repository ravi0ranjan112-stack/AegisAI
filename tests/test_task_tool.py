from aegis.tools.task import TaskTool


def test_task_tool():
    tool = TaskTool()
    assert tool.run("add hello") == "OK"
    assert "hello" in tool.run("list")
