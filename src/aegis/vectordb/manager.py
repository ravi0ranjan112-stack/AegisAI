from aegis.embedding.model import Embedding
from aegis.vectordb.database import VectorDatabase
from aegis.vectordb.similarity import Similarity


class VectorDBManager:
    def __init__(self) -> None:
        self.database = VectorDatabase()

    def add(self, text: str, vector: list[float]) -> None:
        self.database.add(Embedding(text, vector))

    def search(self, vector: list[float]) -> str | None:
        best_text: str | None = None
        best_score = -1.0

        for item in self.database.all():
            score = Similarity.cosine(vector, item.vector)
            if score > best_score:
                best_score = score
                best_text = item.text

        return best_text
