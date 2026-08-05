from dataclasses import dataclass


@dataclass(slots=True)
class Memory:
    key: str
    value: str
