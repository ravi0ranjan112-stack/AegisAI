from dataclasses import dataclass, field

from aegis.conversation.session import Message


@dataclass(slots=True)
class AIRequest:
    prompt: str
    messages: list[Message] = field(default_factory=list)
    system_prompt: str | None = None
    temperature: float = 0.7
    max_tokens: int = 1024
