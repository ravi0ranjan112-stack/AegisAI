from dataclasses import dataclass


@dataclass(slots=True)
class Event:
    name: str
    value: str
