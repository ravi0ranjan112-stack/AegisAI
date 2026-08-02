from pathlib import Path

from aegis.code.symbol import Symbol

_SYMBOLS: list[Symbol] = []


class CodeIndex:
    def build(self, root: str = ".") -> int:
        _SYMBOLS.clear()

        for path in Path(root).rglob("*.py"):
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue

            for raw_line in text.splitlines():
                line = raw_line.strip()

                if line.startswith("class "):
                    _SYMBOLS.append(
                        Symbol(
                            name=line.split()[1].split("(")[0].rstrip(":"),
                            kind="class",
                            path=str(path),
                        )
                    )

                elif line.startswith("def "):
                    _SYMBOLS.append(
                        Symbol(
                            name=line.split()[1].split("(")[0],
                            kind="function",
                            path=str(path),
                        )
                    )

        return len(_SYMBOLS)

    def search(self, query: str) -> list[Symbol]:
        query = query.lower()
        return [s for s in _SYMBOLS if query in s.name.lower()]
