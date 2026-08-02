from aegis.memory.store import MemoryStore


def test_memory_store() -> None:
    mem = MemoryStore()

    mem.add("hello world")
    mem.add("python")

    assert mem.search("hello") == ["hello world"]
    assert mem.search("python") == ["python"]

    mem.clear()
    assert mem.all() == []
