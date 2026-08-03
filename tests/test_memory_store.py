from aegis.memory.store import MemoryStore


def test_memory_store():
    store = MemoryStore()

    store.add("name", "Aegis")

    assert store.get("name") == "Aegis"
    assert store.get("missing") is None
