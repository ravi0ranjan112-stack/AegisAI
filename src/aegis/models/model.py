from dataclasses import dataclass


@dataclass(slots=True)
class Model:
    name: str
    provider: str
