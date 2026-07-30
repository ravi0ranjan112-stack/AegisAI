from dataclasses import dataclass, field


@dataclass(slots=True)
class Message:
    role: str
    content: str


@dataclass(slots=True)
class ConversationSession:
    messages: list[Message] = field(default_factory=list)

    def add_user(self, text: str) -> None:
        self.messages.append(Message("user", text))

    def add_assistant(self, text: str) -> None:
        self.messages.append(Message("assistant", text))

    def clear(self) -> None:
        self.messages.clear()
