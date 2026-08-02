from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    id: int
    text: str
