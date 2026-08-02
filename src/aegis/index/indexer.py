from pathlib import Path

from aegis.index.document import Document


class ProjectIndexer:
    def build(self, root: str = ".") -> list[Document]:
        docs: list[Document] = []

        for path in Path(root).rglob("*.py"):
            try:
                docs.append(
                    Document(
                        path=str(path),
                        text=path.read_text(encoding="utf-8"),
                    )
                )
            except Exception:
                pass

        return docs
