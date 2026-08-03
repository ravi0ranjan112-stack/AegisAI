from dataclasses import dataclass


@dataclass(slots=True)
class AgentState:
    goal: str = ""
    running: bool = False
    completed: bool = False
    max_steps: int = 10
    current_step: int = 0

    @property
    def steps(self) -> int:
        return self.current_step

    @property
    def finished(self) -> bool:
        return self.completed or self.current_step >= self.max_steps

    def next_step(self) -> None:
        self.current_step += 1
