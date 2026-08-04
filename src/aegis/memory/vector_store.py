from aegis.memory.document import Document


class VectorStore:
    def __init__(self) -> None:
        self._docs: list[Document] = []

    def add(self, document: Document) -> None:
        self._docs.append(document)

    def all(self) -> list[Document]:
        return self._docs
