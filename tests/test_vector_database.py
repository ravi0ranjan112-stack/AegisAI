from aegis.embedding.model import Embedding
from aegis.vectordb.database import VectorDatabase


def test_vector_database() -> None:
    db = VectorDatabase()

    db.add(Embedding("python", [1.0, 2.0]))
    db.add(Embedding("rust", [3.0]))

    items = db.all()

    assert len(items) == 2
    assert items[0].text == "python"
    assert items[1].vector == [3.0]
