from aegis.vector.store import VectorStore


class VectorSearch:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def search(self, query: str) -> list[str]:
        return self.store.search(query)
