from aegis.workflow.manager import WorkflowManager


def test_workflow_manager() -> None:
    manager = WorkflowManager()

    wf = manager.execute("Build AI")

    assert wf.name == "Build AI"
    assert len(wf.steps) == 3
    assert wf.steps[2].name == "Finish"
