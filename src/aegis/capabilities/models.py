from dataclasses import dataclass


@dataclass(slots=True)
class Capability:
    name: str
    available: bool
    description: str = ""
