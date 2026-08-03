from aegis.conversation.manager import ConversationManager
from aegis.tools.base import BaseTool


class ConversationTool(BaseTool):
    def __init__(self) -> None:
        self._manager = ConversationManager()

    @property
    def name(self) -> str:
        return "conversation"

    def run(self, command: str) -> str:
        return self._manager.execute(command)
