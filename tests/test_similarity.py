from aegis.embedding.similarity import Similarity


def test_similarity() -> None:
    similarity = Similarity()

    assert similarity.score([1.0, 2.0], [1.0, 2.0]) == 5.0
    assert similarity.score([], [1.0]) == 0.0
    assert similarity.score([1.0], []) == 0.0
