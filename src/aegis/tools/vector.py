from aegis.tools.base import BaseTool
from aegis.vector.manager import VectorManager


class VectorTool(BaseTool):
    def __init__(self) -> None:
        self._manager = VectorManager()

    @property
    def name(self) -> str:
        return "vector"

    def run(self, command: str) -> str:
        return self._manager.execute(command)
