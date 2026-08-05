from dataclasses import dataclass, field


@dataclass(slots=True)
class Context:
    items: list[str] = field(default_factory=list)

    def add(self, text: str) -> None:
        self.items.append(text)
