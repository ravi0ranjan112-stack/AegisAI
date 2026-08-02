from aegis.rag.manager import RagManager
from aegis.tools.base import BaseTool


class RagTool(BaseTool):
    @property
    def name(self) -> str:
        return "rag"

    def run(self, command: str) -> str:
        action, _, value = command.partition(" ")

        if action == "add":
            self._manager.add(value, [1.0])
            return "OK"

        if action == "search":
            return self._manager.retrieve([1.0])

        return "Usage: add/search"

    def __init__(self) -> None:
        self._manager = RagManager()
