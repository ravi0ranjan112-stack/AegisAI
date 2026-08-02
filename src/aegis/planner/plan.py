from dataclasses import dataclass, field


@dataclass(slots=True)
class Plan:
    goal: str
    steps: list[str] = field(default_factory=list)

    def add(self, step: str) -> None:
        self.steps.append(step)
