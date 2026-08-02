from dataclasses import dataclass


@dataclass(slots=True)
class Symbol:
    name: str
    kind: str
    path: str
