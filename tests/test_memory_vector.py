from aegis.memory.document import Document
from aegis.memory.vector_store import VectorStore


def test_vector_store() -> None:
    store = VectorStore()

    store.add(Document(id=1, text="Python"))
    store.add(Document(id=2, text="AI"))

    docs = store.all()

    assert len(docs) == 2
    assert docs[0].text == "Python"
    assert docs[1].id == 2
