from aegis.tools.workflow import WorkflowTool


def test_workflow_tool():
    tool = WorkflowTool()
    assert tool.run("create test") == "OK"
