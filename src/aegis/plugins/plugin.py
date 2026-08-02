from dataclasses import dataclass


@dataclass(slots=True)
class Plugin:
    name: str
    enabled: bool = True
