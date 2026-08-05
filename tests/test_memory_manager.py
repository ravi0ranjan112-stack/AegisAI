from aegis.memory.manager import MemoryManager


def test_memory_manager() -> None:
    manager = MemoryManager()

    manager.remember("language", "Python")

    assert manager.recall("language") == "Python"
    assert manager.recall("unknown") is None
