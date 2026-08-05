from aegis.memory.memory import Memory


class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, Memory] = {}

    # New API
    def save(self, key: str, value: str) -> None:
        self._items[key] = Memory(key, value)

    def get(self, key: str) -> str | None:
        memory = self._items.get(key)
        return None if memory is None else memory.value

    # Backward-compatible API
    def add(self, key: str, value: str = "") -> None:
        self.save(key, value)

    def search(self, query: str) -> list[str]:
        result: list[str] = []

        for memory in self._items.values():
            if query.lower() in memory.key.lower() or query.lower() in memory.value.lower():
                result.append(f"{memory.key} {memory.value}".strip())

        return result

    def clear(self) -> None:
        self._items.clear()
