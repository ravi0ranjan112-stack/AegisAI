from aegis.vectordb.similarity import Similarity


def test_similarity() -> None:
    score = Similarity.cosine([1.0, 2.0], [1.0, 2.0])

    assert round(score, 5) == 1.0


def test_similarity_invalid() -> None:
    assert Similarity.cosine([], []) == 0.0
    assert Similarity.cosine([1.0], [1.0, 2.0]) == 0.0
