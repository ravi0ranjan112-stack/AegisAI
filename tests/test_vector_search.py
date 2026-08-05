from aegis.vector.search import VectorSearch
from aegis.vector.store import VectorStore


def test_vector_search() -> None:
    store = VectorStore()

    store.add("python", "Python language")
    store.add("java", "Java language")

    search = VectorSearch(store)

    result = search.search("python")

    assert len(result) == 1
    assert result[0] == "python"
