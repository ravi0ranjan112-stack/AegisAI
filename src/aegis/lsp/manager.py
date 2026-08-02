from pathlib import Path

from aegis.lsp.diagnostic import DiagnosticEngine
from aegis.lsp.workspace import Workspace


class LSPManager:
    def open(self, path: str) -> str:
        return Workspace().open(path).text

    def diagnostics(self, path: str) -> list[str]:
        source = Path(path).read_text(encoding="utf-8")
        return DiagnosticEngine().check(source)
