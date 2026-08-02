from aegis.workspace.context import WorkspaceContext


def test_workspace():
    ctx = WorkspaceContext()
    assert int(ctx.refresh()) >= 1
