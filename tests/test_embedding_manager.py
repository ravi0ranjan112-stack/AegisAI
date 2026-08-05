from aegis.embedding.manager import EmbeddingManager


def test_embedding_manager() -> None:
    manager = EmbeddingManager()

    score = manager.compare("abc", "abc")

    assert score > 0
    assert manager.compare("", "") == 0.0
