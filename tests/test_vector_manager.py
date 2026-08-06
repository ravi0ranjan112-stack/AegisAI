from aegis.vector.manager import VectorManager


def test_vector_manager() -> None:
    manager = VectorManager()

    assert manager.execute("add python language") == "OK"
    assert "python" in manager.execute("search py")
    assert manager.execute("unknown") == "Unknown command"
