from aegis.embedding.manager import EmbeddingManager


def test_embedding_manager() -> None:
    manager = EmbeddingManager()

    assert manager.create("hello world") == [5.0, 5.0]
