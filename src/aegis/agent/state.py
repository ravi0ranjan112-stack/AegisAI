from dataclasses import dataclass


@dataclass(slots=True)
class AgentState:
    steps: int = 0
    max_steps: int = 5

    def next_step(self) -> None:
        self.steps += 1

    @property
    def finished(self) -> bool:
        return self.steps >= self.max_steps
