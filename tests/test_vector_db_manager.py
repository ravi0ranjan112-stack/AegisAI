from aegis.vectordb.manager import VectorDBManager


def test_vector_db_manager() -> None:
    manager = VectorDBManager()

    manager.add("python", [1.0, 0.0])
    manager.add("rust", [0.0, 1.0])

    assert manager.search([1.0, 0.0]) == "python"
    assert manager.search([0.0, 1.0]) == "rust"
