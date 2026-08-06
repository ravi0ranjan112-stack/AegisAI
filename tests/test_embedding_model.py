from aegis.embedding.model import Embedding


def test_embedding_model() -> None:
    embedding = Embedding("hello", [0.1, 0.2, 0.3])

    assert embedding.text == "hello"
    assert embedding.vector == [0.1, 0.2, 0.3]
