from aegis.rag.manager import RagManager
from aegis.tools.base import BaseTool


class RagTool(BaseTool):
    @property
    def name(self) -> str:
        return "rag"

    def run(self, command: str) -> str:
        return RagManager().execute(command)
