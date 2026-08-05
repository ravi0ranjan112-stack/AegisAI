from aegis.embedding.embedder import Embedder
from aegis.embedding.similarity import Similarity


class EmbeddingManager:
    def __init__(self) -> None:
        self.embedder = Embedder()
        self.similarity = Similarity()

    def compare(self, left: str, right: str) -> float:
        left_vector = self.embedder.embed(left)
        right_vector = self.embedder.embed(right)

        return self.similarity.score(left_vector, right_vector)
