from dataclasses import dataclass


@dataclass(slots=True)
class Document:
    id: str
    text: str
