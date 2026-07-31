from dataclasses import dataclass


@dataclass(slots=True)
class Observation:
    tool: str
    command: str
    result: str
