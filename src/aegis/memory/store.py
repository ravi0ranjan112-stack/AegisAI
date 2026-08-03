from aegis.memory.models import Memory


class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, Memory] = {}

    def add(self, key: str, value: str | None = None) -> None:
        if value is None:
            value = key
        self._items[key] = Memory(key, value)

    def get(self, key: str) -> str | None:
        item = self._items.get(key)
        return item.value if item else None

    def search(self, query: str) -> list[str]:
        q = query.lower()
        return [memory.value for memory in self._items.values() if q in memory.value.lower()]

    def clear(self) -> None:
        self._items.clear()

    def all(self) -> list[str]:
        return [memory.value for memory in self._items.values()]
