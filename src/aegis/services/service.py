from dataclasses import dataclass


@dataclass(slots=True)
class Service:
    name: str
    enabled: bool = True
