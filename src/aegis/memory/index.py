from aegis.memory.document import Document


class MemoryIndex:
    def __init__(self) -> None:
        self._docs: list[Document] = []

    def add(self, text: str) -> None:
        self._docs.append(Document(id=len(self._docs) + 1, text=text))

    @property
    def documents(self) -> list[Document]:
        return self._docs
