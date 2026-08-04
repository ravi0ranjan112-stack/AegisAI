from dataclasses import dataclass


@dataclass(slots=True)
class WorkflowStep:
    id: int
    name: str
    completed: bool = False
