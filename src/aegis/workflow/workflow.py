from aegis.workflow.step import WorkflowStep


class Workflow:
    def __init__(self, name: str = "") -> None:
        self.name = name
        self._steps: list[WorkflowStep] = []

    @property
    def steps(self) -> list[WorkflowStep]:
        return self._steps

    def add(self, name: str) -> None:
        self._steps.append(
            WorkflowStep(
                id=len(self._steps) + 1,
                name=name,
            )
        )
