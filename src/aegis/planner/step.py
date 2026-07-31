from dataclasses import dataclass


@dataclass(slots=True)
class PlanStep:
    description: str
    completed: bool = False
