from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    line: int
    character: int
