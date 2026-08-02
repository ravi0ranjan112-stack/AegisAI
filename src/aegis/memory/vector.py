from aegis.memory.store import MemoryStore


class MemoryIndex:
    def __init__(self) -> None:
        self._store = MemoryStore()

    def add(self, text: str) -> None:
        self._store.add(text)

    def query(self, text: str) -> str:
        matches = self._store.search(text)
        return "\n".join(matches) if matches else "No memory."
