from aegis.embedding.embedder import Embedder


def test_embedder() -> None:
    embedder = Embedder()

    vector = embedder.embed("abc")

    assert vector == [97.0, 98.0, 99.0]
    assert embedder.embed("") == []
