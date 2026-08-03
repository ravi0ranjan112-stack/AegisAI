from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    title: str
    done: bool = False
    id: int = 1

    @property
    def description(self) -> str:
        return self.title
