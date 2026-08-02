from aegis.memory.store import MemoryStore


def test_memory_store():
    store = MemoryStore()
    store.add("hello world")
    assert store.search("hello") == ["hello world"]
