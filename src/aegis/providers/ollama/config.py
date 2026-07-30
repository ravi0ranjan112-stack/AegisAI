from dataclasses import dataclass


@dataclass(slots=True)
class OllamaConfig:
    host: str = "http://127.0.0.1:11434"
    model: str = "llama3.2"
    timeout: int = 120
