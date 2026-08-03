import json
from pathlib import Path

from aegis.memory.models import Memory


class MemoryPersistence:
    def save(self, path: str, memories: list[Memory]) -> None:
        Path(path).write_text(
            json.dumps(
                [{"key": m.key, "value": m.value} for m in memories],
                indent=2,
            ),
            encoding="utf-8",
        )

    def load(self, path: str) -> list[Memory]:
        p = Path(path)

        if not p.exists():
            return []

        data = json.loads(p.read_text(encoding="utf-8"))

        return [Memory(item["key"], item["value"]) for item in data]
