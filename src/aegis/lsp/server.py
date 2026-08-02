from aegis.lsp.client import LSPClient


class LSPServer:
    def __init__(self) -> None:
        self._client = LSPClient()

    def execute(self, command: str) -> str:
        action, _, arg = command.partition(" ")

        if action == "open":
            return self._client.open(arg)

        if action == "diagnostics":
            result = self._client.diagnostics(arg)
            return "\n".join(result) if result else "OK"

        return "Unknown command"
