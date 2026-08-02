from aegis.rag.store import RAGStore


class Retriever:
    def __init__(self) -> None:
        self._store = RAGStore()

    def add(self, doc_id: str, embedding: list[float]) -> None:
        self._store.add(doc_id, embedding)

    def retrieve(self, embedding: list[float]) -> str:
        return self._store.retrieve(embedding)
