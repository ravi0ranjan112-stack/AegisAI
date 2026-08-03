from aegis.memory.store import MemoryStore


class MemoryRetriever:
    def __init__(self, store: MemoryStore) -> None:
        self._store = store

    def retrieve(self, query: str) -> list[str]:
        return self._store.search(query)
