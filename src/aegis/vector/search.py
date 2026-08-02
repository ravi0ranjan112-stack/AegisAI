from aegis.vector.embedding import Embedder
from aegis.vector.index import VectorIndex


class VectorSearch:
    def __init__(self, index: VectorIndex) -> None:
        self._index = index

    @staticmethod
    def _score(a: list[float], b: list[float]) -> float:
        return sum(x * y for x, y in zip(a, b, strict=False))

    def search(self, query: str) -> list[str]:
        q = Embedder().embed(query)

        ranked = sorted(
            ((key, self._score(q, vec)) for key, vec in self._index._items.items()),
            key=lambda item: item[1],
            reverse=True,
        )

        return [key for key, _ in ranked]
