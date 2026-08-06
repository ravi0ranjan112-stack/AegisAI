from aegis.embedding.model import Embedding


class VectorDatabase:
    def __init__(self) -> None:
        self._data: list[Embedding] = []

    def add(self, embedding: Embedding) -> None:
        self._data.append(embedding)

    def all(self) -> list[Embedding]:
        return list(self._data)
