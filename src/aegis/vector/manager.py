from aegis.vector.store import VectorStore


class VectorManager:
    def __init__(self) -> None:
        self._store = VectorStore()

    def execute(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "add":
            key, _, text = rest.partition(" ")
            self._store.add(key, text)
            return "OK"

        if action == "search":
            return "\n".join(self._store.search(rest))

        return "Unknown command"
