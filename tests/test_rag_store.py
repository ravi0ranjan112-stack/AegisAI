from aegis.rag.store import RAGStore


def test_rag_store() -> None:
    store = RAGStore()

    store.add("python", [1.0, 0.0])
    store.add("java", [0.0, 1.0])

    assert store.retrieve([0.9, 0.1]) == "python"
