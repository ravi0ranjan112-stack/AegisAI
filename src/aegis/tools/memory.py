from aegis.memory.manager import MemoryManager
from aegis.tools.base import BaseTool


class MemoryTool(BaseTool):
    def __init__(self) -> None:
        self._manager = MemoryManager()

    @property
    def name(self) -> str:
        return "memory"

    def run(self, command: str) -> str:
        return self._manager.execute(command)
