from aegis.tools.workspace import WorkspaceTool


def test_workspace_tool():
    tool = WorkspaceTool()
    tool.run("refresh")
    assert tool.run("files")
