from aegis.rag.retriever import Retriever


class RagManager:
    def __init__(self) -> None:
        self._retriever = Retriever()

    def add(self, doc_id: str, embedding: list[float]) -> None:
        self._retriever.add(doc_id, embedding)

    def retrieve(self, embedding: list[float]) -> str:
        return self._retriever.retrieve(embedding)
