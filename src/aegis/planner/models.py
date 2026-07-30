from dataclasses import dataclass, field


@dataclass(slots=True)
class Task:
    id: int
    title: str
    status: str = "pending"


@dataclass(slots=True)
class Plan:
    goal: str
    tasks: list[Task] = field(default_factory=list)
