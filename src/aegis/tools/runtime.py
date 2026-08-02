from aegis.runtime.runtime import Runtime
from aegis.tools.base import BaseTool


class RuntimeTool(BaseTool):
    @property
    def name(self) -> str:
        return "runtime"

    def run(self, command: str) -> str:
        return Runtime().execute(command)
