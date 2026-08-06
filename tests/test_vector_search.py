from aegis.vector.search import VectorSearch
from aegis.vector.store import VectorStore


def test_vector_search() -> None:
    store = VectorStore()

    store.add("python", "language")
    store.add("rust", "systems")
    store.add("java", "enterprise")

    search = VectorSearch(store)

    assert search.search("py") == ["python"]
    assert search.search("rust") == ["rust"]
