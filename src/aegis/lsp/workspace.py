from pathlib import Path

from aegis.lsp.document import Document


class Workspace:
    def open(self, path: str) -> Document:
        return Document(
            path=path,
            text=Path(path).read_text(encoding="utf-8"),
        )
