from aegis.vector.embedding import Embedder


class VectorIndex:
    def __init__(self) -> None:
        self._items: dict[str, list[float]] = {}

    def add(self, key: str, text: str) -> None:
        self._items[key] = Embedder().embed(text)

    def get(self, key: str) -> list[float]:
        return self._items[key]
