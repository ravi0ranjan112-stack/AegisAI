from dataclasses import dataclass, field


@dataclass(slots=True)
class AgentHistory:
    entries: list[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.entries.append(message)

    def render(self) -> str:
        return "\n\n".join(self.entries)
