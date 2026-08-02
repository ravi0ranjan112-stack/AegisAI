from aegis.lsp.server import LSPServer
from aegis.tools.base import BaseTool


class LSPTool(BaseTool):
    @property
    def name(self) -> str:
        return "lsp"

    def run(self, command: str) -> str:
        return LSPServer().execute(command)
