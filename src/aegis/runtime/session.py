from dataclasses import dataclass, field


@dataclass(slots=True)
class RuntimeSession:
    values: dict[str, str] = field(default_factory=dict)

    def set(self, key: str, value: str) -> None:
        self.values[key] = value

    def get(self, key: str) -> str:
        return self.values.get(key, "")
