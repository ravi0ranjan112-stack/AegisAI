from collections import deque


class MemoryStore:
    def __init__(self, limit: int = 1000) -> None:
        self._entries: deque[str] = deque(maxlen=limit)

    def add(self, text: str) -> None:
        self._entries.append(text)

    def all(self) -> list[str]:
        return list(self._entries)

    def search(self, query: str) -> list[str]:
        q = query.lower()
        return [e for e in self._entries if q in e.lower()]

    def clear(self) -> None:
        self._entries.clear()
