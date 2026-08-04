from aegis.memory.manager_v2 import MemoryManagerV2


def test_memory_manager_v2() -> None:
    m = MemoryManagerV2()

    m.remember("Python AI")
    m.remember("Rust")

    assert len(m.store.all()) == 2
    assert len(m.search.find("AI")) == 1
