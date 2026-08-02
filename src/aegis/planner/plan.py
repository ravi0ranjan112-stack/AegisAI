from dataclasses import dataclass, field

from aegis.planner.step import Step


@dataclass(slots=True)
class Plan:
    goal: str
    steps: list[Step] = field(default_factory=list)

    def add(
        self,
        description: str,
        *,
        priority: int = 0,
        depends_on: list[int] | None = None,
    ) -> Step:
        step = Step(
            id=len(self.steps) + 1,
            description=description,
            priority=priority,
            depends_on=depends_on or [],
        )
        self.steps.append(step)
        return step

    def pending(self) -> list[Step]:
        return [s for s in self.steps if not s.completed]

    def completed(self) -> list[Step]:
        return [s for s in self.steps if s.completed]
