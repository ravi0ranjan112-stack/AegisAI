from dataclasses import dataclass


@dataclass(slots=True)
class AISettings:
    provider: str = "mock"
    model: str = "mock-v1"
    temperature: float = 0.7
    max_tokens: int = 1024
    offline: bool = True
