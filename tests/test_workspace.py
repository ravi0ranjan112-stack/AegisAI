from aegis.workspace.manager import WorkspaceManager


def test_workspace_creation():
    manager = WorkspaceManager("temp_workspace")

    manager.create_project("calculator")

    assert manager.exists("calculator")
