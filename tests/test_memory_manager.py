from aegis.memory.manager import MemoryManager


def test_memory_manager():
    manager = MemoryManager()

    assert manager.execute("add hello world") == "OK"
    assert "hello world" in manager.execute("search hello")
    assert manager.execute("clear") == "OK"
