from aegis.memory.vector import VectorStore
from aegis.tools.base import BaseTool

_INDEX = VectorStore()


class MemoryTool(BaseTool):
    @property
    def name(self) -> str:
        return "memory"

    def run(self, command: str) -> str:
        action, _, value = command.partition(" ")

        if action == "add":
            _INDEX.add(value, [1.0])
            return "OK"

        if action == "search":
            return _INDEX.search([1.0])

        return "Usage: add/search"
