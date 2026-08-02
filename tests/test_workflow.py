from aegis.workflow.runner import WorkflowRunner


def test_workflow():
    runner = WorkflowRunner()
    assert runner.execute("create demo") == "OK"
    assert runner.execute("add demo step1") == "OK"
    assert "step1" in runner.execute("show demo")
