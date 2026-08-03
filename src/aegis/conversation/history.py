from aegis.conversation.message import Message
from aegis.conversation.session import ConversationSession


class ConversationHistory:
    def __init__(self, session: ConversationSession) -> None:
        self._session = session

    def last(self, count: int) -> list[Message]:
        return self._session.messages[-count:]

    def text(self) -> str:
        return "\n".join(f"{m.role}: {m.content}" for m in self._session.messages)
