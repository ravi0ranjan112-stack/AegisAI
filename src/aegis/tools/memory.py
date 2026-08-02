from aegis.memory.vector import MemoryIndex
from aegis.tools.base import BaseTool

_INDEX = MemoryIndex()


class MemoryTool(BaseTool):
    @property
    def name(self) -> str:
        return "memory"

    def run(self, command: str) -> str:
        action, _, value = command.partition(" ")

        if action == "add":
            _INDEX.add(value)
            return "OK"

        if action == "search":
            return _INDEX.query(value)

        return "Usage: add/search"
