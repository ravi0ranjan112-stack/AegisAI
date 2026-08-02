from aegis.tools.prompt import PromptTool


def test_prompt_tool():
    tool = PromptTool()
    assert tool.run("add test Hello") == "OK"
    assert tool.run("show test") == "Hello"
