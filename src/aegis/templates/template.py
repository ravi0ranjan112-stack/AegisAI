from dataclasses import dataclass


@dataclass(slots=True)
class Template:
    name: str
    text: str
