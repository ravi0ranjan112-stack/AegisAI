from aegis.vector.search import VectorSearch
from aegis.vector.store import VectorStore


class VectorManager:
    def __init__(self) -> None:
        self.store = VectorStore()
        self.searcher = VectorSearch(self.store)

    def execute(self, command: str) -> str:
        parts = command.strip().split(maxsplit=2)

        if not parts:
            return "Unknown command"

        match parts[0]:
            case "add" if len(parts) == 3:
                self.store.add(parts[1], parts[2])
                return "OK"

            case "search" if len(parts) >= 2:
                return "\n".join(self.searcher.search(parts[1]))

            case _:
                return "Unknown command"
