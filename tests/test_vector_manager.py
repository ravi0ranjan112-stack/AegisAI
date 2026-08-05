from aegis.vector.manager import VectorManager


def test_vector_manager() -> None:
    manager = VectorManager()

    assert manager.execute("add python Python language") == "OK"
    assert "python" in manager.execute("search python")
