from aegis.embedding.api import EmbeddingAPI


class EmbeddingManager:
    def __init__(self) -> None:
        self.api = EmbeddingAPI()

    def create(self, text: str) -> list[float]:
        return self.api.embed(text)
