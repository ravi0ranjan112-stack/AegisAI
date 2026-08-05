from aegis.memory.store import MemoryStore


class MemoryManager:
    def __init__(self) -> None:
        self.store = MemoryStore()

    def remember(self, key: str, value: str) -> None:
        self.store.save(key, value)

    def recall(self, key: str) -> str | None:
        return self.store.get(key)

    def execute(self, command: str) -> str:
        result = "Unknown command"
        parts = command.strip().split(maxsplit=2)

        if parts:
            action = parts[0]

            if action == "remember" and len(parts) == 2:
                self.store.add(parts[1])
                result = "OK"
            elif action == "add" and len(parts) >= 3:
                self.store.add(parts[1], parts[2])
                result = "OK"
            elif action == "search" and len(parts) == 2:
                result = "\n".join(self.store.search(parts[1]))
            elif action in {"recall", "get"} and len(parts) == 2:
                value = self.recall(parts[1])
                result = value if value is not None else "Unknown"
            elif action == "clear":
                self.store.clear()
                result = "OK"

        return result
