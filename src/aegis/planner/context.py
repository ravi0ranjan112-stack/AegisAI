from dataclasses import dataclass, field

from aegis.planner.observation import Observation
from aegis.planner.step import PlanStep


@dataclass(slots=True)
class PlannerContext:
    goal: str
    steps: list[PlanStep] = field(default_factory=list)
    observations: list[Observation] = field(default_factory=list)

    def add_step(self, description: str) -> None:
        self.steps.append(PlanStep(description=description))

    def add_observation(
        self,
        tool: str,
        command: str,
        result: str,
    ) -> None:
        self.observations.append(
            Observation(
                tool=tool,
                command=command,
                result=result,
            )
        )
