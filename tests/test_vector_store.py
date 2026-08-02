from aegis.vector.store import VectorStore


def test_vector_store():
    store = VectorStore()

    store.add("python", "python language")
    store.add("java", "java language")

    result = store.search("python")

    assert "python" in result
