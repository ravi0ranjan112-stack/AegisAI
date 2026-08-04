from aegis.workflow.engine import WorkflowEngine


class WorkflowManager:
    def __init__(self) -> None:
        self._engine = WorkflowEngine()

    def execute(self, name: str):
        return self._engine.create(name)
