from aegis.vector.index import VectorIndex
from aegis.vector.search import VectorSearch


def test_vector_search():
    index = VectorIndex()

    index.add("python", "python language")
    index.add("java", "java language")

    result = VectorSearch(index).search("python")

    assert len(result) == 2
    assert "python" in result
