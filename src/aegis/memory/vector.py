from math import sqrt


class VectorStore:
    def __init__(self) -> None:
        self._vectors: dict[str, list[float]] = {}

    def add(self, key: str, vector: list[float]) -> None:
        self._vectors[key] = vector

    def get(self, key: str) -> list[float]:
        return self._vectors[key]

    def search(self, vector: list[float]) -> str:
        best_key = ""
        best_score = float("-inf")

        for key, candidate in self._vectors.items():
            score = self._cosine(vector, candidate)

            if score > best_score:
                best_score = score
                best_key = key

        return best_key

    def _cosine(self, a: list[float], b: list[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b, strict=False))
        na = sqrt(sum(x * x for x in a))
        nb = sqrt(sum(y * y for y in b))

        if na == 0 or nb == 0:
            return 0.0

        return dot / (na * nb)
