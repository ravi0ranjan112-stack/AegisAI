from aegis.memory.index import MemoryIndex
from aegis.memory.search import MemorySearch
from aegis.memory.vector_store import VectorStore


class MemoryManagerV2:
    def __init__(self) -> None:
        self.index = MemoryIndex()
        self.store = VectorStore()
        self.search = MemorySearch(self.index)

    def remember(self, text: str) -> None:
        self.index.add(text)
        self.store.add(self.index.documents[-1])
