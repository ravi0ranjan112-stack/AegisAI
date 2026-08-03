from dataclasses import dataclass

from aegis.planner.task import Task


@dataclass(slots=True)
class Observation:
    tool: str
    command: str
    result: str


class Plan:
    def __init__(self, goal: str = "") -> None:
        self.goal = goal
        self.steps: list[Task] = []
        self.observations: list[Observation] = []

    def add(self, title: str) -> None:
        self.steps.append(Task(title=title, id=len(self.steps) + 1))

    def add_observation(
        self,
        tool: str,
        command: str,
        result: str,
    ) -> None:
        self.observations.append(Observation(tool=tool, command=command, result=result))
