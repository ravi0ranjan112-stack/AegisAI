from dataclasses import dataclass


@dataclass(slots=True)
class AIResponse:
    text: str
    provider: str = ""
    model: str = ""
