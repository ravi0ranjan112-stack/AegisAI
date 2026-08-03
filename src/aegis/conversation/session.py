from aegis.conversation.message import Message


class ConversationSession:
    def __init__(self) -> None:
        self._messages: list[Message] = []

    @property
    def messages(self) -> list[Message]:
        return self._messages

    def add(self, role: str, content: str) -> None:
        self._messages.append(Message(role, content))

    def add_user(self, content: str) -> None:
        self.add("user", content)

    def add_assistant(self, content: str) -> None:
        self.add("assistant", content)

    def all(self) -> list[Message]:
        return list(self._messages)

    def clear(self) -> None:
        self._messages.clear()
