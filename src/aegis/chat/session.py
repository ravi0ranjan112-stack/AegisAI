from aegis.chat.message import Message


class ChatSession:
    def __init__(self) -> None:
        self.messages: list[Message] = []

    def add(self, role: str, content: str) -> None:
        self.messages.append(Message(role, content))
