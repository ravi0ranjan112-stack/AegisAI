from aegis.embedding.provider import EmbeddingProvider


class SimpleEmbeddingProvider(EmbeddingProvider):
    def embed(self, text: str) -> list[float]:
        return [float(len(word)) for word in text.split()]


class EmbeddingManager:
    def __init__(self) -> None:
        self.provider = SimpleEmbeddingProvider()

    def create(self, text: str) -> list[float]:
        return self.provider.embed(text)
