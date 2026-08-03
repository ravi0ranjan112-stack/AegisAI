from aegis.memory.retriever import MemoryRetriever
from aegis.memory.store import MemoryStore


class MemoryManager:
    def __init__(self) -> None:
        self._store = MemoryStore()
        self._retriever = MemoryRetriever(self._store)

    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            self._store.add(rest)
            return "OK"

        if action == "search":
            return "\n".join(self._retriever.retrieve(rest))

        if action == "clear":
            self._store.clear()
            return "OK"

        return "Unknown command"
