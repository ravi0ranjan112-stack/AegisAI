from dataclasses import dataclass


@dataclass(slots=True)
class AISettings:
    provider: str = "ollama"
    model: str = "qwen2.5:3b"
    temperature: float = 0.7
    max_tokens: int = 1024
    offline: bool = True
