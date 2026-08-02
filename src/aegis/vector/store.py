from aegis.vector.index import VectorIndex
from aegis.vector.search import VectorSearch


class VectorStore:
    def __init__(self) -> None:
        self._index = VectorIndex()

    def add(self, key: str, text: str) -> None:
        self._index.add(key, text)

    def search(self, query: str) -> list[str]:
        return VectorSearch(self._index).search(query)
