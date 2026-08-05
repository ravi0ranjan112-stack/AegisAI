from aegis.runtime.runtime import Runtime
from aegis.tools.base import BaseTool


class RuntimeTool(BaseTool):
    def __init__(self) -> None:
        self._runtime = Runtime()

    @property
    def name(self) -> str:
        return "runtime"

    def run(self, command: str) -> str:
        return self._runtime.execute(command)
