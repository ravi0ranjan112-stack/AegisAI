from aegis.lsp.manager import LSPManager


class LSPClient:
    def __init__(self) -> None:
        self._manager = LSPManager()

    def open(self, path: str) -> str:
        return self._manager.open(path)

    def diagnostics(self, path: str) -> list[str]:
        return self._manager.diagnostics(path)
