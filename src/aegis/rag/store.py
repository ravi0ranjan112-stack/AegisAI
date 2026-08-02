from aegis.memory.vector import VectorStore


class RAGStore:
    def __init__(self) -> None:
        self._vectors = VectorStore()

    def add(self, doc_id: str, embedding: list[float]) -> None:
        self._vectors.add(doc_id, embedding)

    def retrieve(self, embedding: list[float]) -> str:
        return self._vectors.search(embedding)
