from aegis.vector.index import VectorIndex


def test_vector_index():
    index = VectorIndex()

    index.add("hello", "hello world")

    vec = index.get("hello")

    assert len(vec) == 32
    assert all(isinstance(x, float) for x in vec)
