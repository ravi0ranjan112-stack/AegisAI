from aegis.memory.store import MemoryStore


def test_memory_store() -> None:
    store = MemoryStore()

    store.save("name", "Aegis")

    assert store.get("name") == "Aegis"
    assert store.get("missing") is None
