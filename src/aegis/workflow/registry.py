from aegis.workflow.workflow import Workflow


class WorkflowRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Workflow] = {}

    def create(self, name: str) -> str:
        self._items[name] = Workflow(name)
        return "OK"

    def get(self, name: str) -> Workflow | None:
        return self._items.get(name)
