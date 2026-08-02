from aegis.memory.vector import VectorStore


def test_vector_store() -> None:
    store = VectorStore()

    store.add("a", [1.0, 0.0])
    store.add("b", [0.0, 1.0])

    assert store.get("a") == [1.0, 0.0]
    assert store.search([0.9, 0.1]) == "a"
