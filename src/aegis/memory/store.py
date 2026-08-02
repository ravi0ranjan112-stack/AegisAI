from dataclasses import dataclass, field


@dataclass(slots=True)
class MemoryStore:
    entries: list[str] = field(default_factory=list)

    def add(self, text: str) -> None:
        self.entries.append(text)

    def search(self, query: str) -> list[str]:
        query = query.lower()
        return [item for item in self.entries if query in item.lower()]
