from dataclasses import dataclass


@dataclass(slots=True)
class Prompt:
    name: str
    text: str
