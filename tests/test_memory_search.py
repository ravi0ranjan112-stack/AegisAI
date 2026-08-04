from aegis.memory.index import MemoryIndex
from aegis.memory.search import MemorySearch


def test_memory_search() -> None:
    index = MemoryIndex()

    index.add("Python AI")
    index.add("Rust")
    index.add("AI Agent")

    search = MemorySearch(index)

    result = search.find("AI")

    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 3
