from aegis.embedding.model import Embedding
from aegis.vector.store import VectorStore


def test_vector_store() -> None:
    store = VectorStore()

    store.add(Embedding("hello", [1.0, 2.0]))
    store.add(Embedding("world", [3.0]))

    items = store.all()

    assert len(items) == 2
    assert items[0].text == "hello"
    assert items[1].vector == [3.0]
