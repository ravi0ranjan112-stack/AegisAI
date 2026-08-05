from aegis.memory.store import MemoryStore


def test_memory_store() -> None:
    store = MemoryStore()

    store.save("language", "Python")

    assert store.get("language") == "Python"
    assert store.get("unknown") is None
