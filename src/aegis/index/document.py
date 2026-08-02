from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    path: str
    text: str
