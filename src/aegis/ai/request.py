from dataclasses import dataclass


@dataclass(slots=True)
class AIRequest:
    prompt: str
    system_prompt: str | None = None
    temperature: float = 0.7
    max_tokens: int = 1024
