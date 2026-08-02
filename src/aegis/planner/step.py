from dataclasses import dataclass


@dataclass(slots=True)
class PlanStep:
    id: int = 0
    description: str = ""
    priority: int = 0
    depends_on: list[int] | None = None
    completed: bool = False


# Backward compatibility
Step = PlanStep
