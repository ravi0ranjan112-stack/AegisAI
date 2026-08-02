from aegis.tools.git import GitTool


def test_status():
    tool = GitTool()
    result = tool.run("status")
    assert isinstance(result, str)


def test_log():
    tool = GitTool()
    result = tool.run("log --oneline -1")
    assert isinstance(result, str)


def test_branch():
    tool = GitTool()
    result = tool.run("branch")
    assert isinstance(result, str)
