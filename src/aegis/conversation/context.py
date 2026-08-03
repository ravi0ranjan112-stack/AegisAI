from aegis.conversation.history import ConversationHistory
from aegis.conversation.session import ConversationSession


class ConversationContext:
    def __init__(self, session: ConversationSession) -> None:
        self._history = ConversationHistory(session)

    def build(self, limit: int = 10) -> str:
        return "\n".join(f"{m.role}: {m.content}" for m in self._history.last(limit))
