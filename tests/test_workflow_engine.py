from aegis.workflow.engine import WorkflowEngine


def test_workflow_engine() -> None:
    engine = WorkflowEngine()

    wf = engine.create("Build AI")

    assert wf.name == "Build AI"
    assert len(wf.steps) == 3
    assert wf.steps[0].name == "Start"
