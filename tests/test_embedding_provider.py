from aegis.embedding.provider import EmbeddingProvider


class DummyEmbeddingProvider(EmbeddingProvider):
    def embed(self, text: str) -> list[float]:
        return [float(len(text))]


def test_embedding_provider() -> None:
    provider = DummyEmbeddingProvider()

    assert provider.embed("hello") == [5.0]
