from aegis.conversation.context import ConversationContext
from aegis.conversation.session import ConversationSession


class ConversationManager:
    def __init__(self) -> None:
        self._session = ConversationSession()

    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "user":
            self._session.add_user(rest)
            return "OK"

        if action == "assistant":
            self._session.add_assistant(rest)
            return "OK"

        if action == "context":
            return ConversationContext(self._session).build()

        if action == "clear":
            self._session.clear()
            return "OK"

        return "Unknown command"
