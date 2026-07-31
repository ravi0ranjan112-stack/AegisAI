from dataclasses import dataclass


@dataclass(slots=True)
class OllamaConfig:
    host: str = "http://127.0.0.1:11434"
    model: str = "qwen2.5:3b"
    timeout: int = 120
