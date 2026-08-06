from aegis.memory.memory import Memory


class MemoryStore:
    def __init__(self) -> None:
        self._data: dict[str, Memory] = {}

    def save(self, key: str, value: str) -> None:
        self._data[key] = Memory(key, value)

    def get(self, key: str) -> str | None:
        memory = self._data.get(key)
        return None if memory is None else memory.value

    def add(self, key: str, value: str = "") -> None:
        self.save(key, value)

    def search(self, query: str) -> list[str]:
        results: list[str] = []

        for memory in self._data.values():
            if query.lower() in memory.key.lower() or query.lower() in memory.value.lower():
                results.append(f"{memory.key} {memory.value}".strip())

        return results

    def clear(self) -> None:
        self._data.clear()
