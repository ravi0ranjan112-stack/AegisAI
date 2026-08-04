from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    provider: str = "ollama"
    model: str = "llama3"
