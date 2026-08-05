from aegis.vector.store import VectorStore


def test_vector_store() -> None:
    store = VectorStore()

    store.add("1", "Hello")
    store.add("2", "World")

    doc1 = store.get("1")
    doc2 = store.get("2")

    assert doc1 is not None
    assert doc2 is not None

    assert doc1.text == "Hello"
    assert doc2.text == "World"
    assert store.get("3") is None
    assert len(store.all()) == 2
