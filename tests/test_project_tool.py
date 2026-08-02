from aegis.tools.project import ProjectTool


def test_project_tool():
    result = ProjectTool().run("summary")
    assert "Python files" in result
