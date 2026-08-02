from pathlib import Path

from aegis.code.symbol import Symbol

_SYMBOLS: list[Symbol] = []


class CodeIndex:
    def build(self, root: str = ".") -> int:
        _SYMBOLS.clear()

        for path in Path(root).rglob("*.py"):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue

            for raw in text.splitlines():
                line = raw.strip()

                if line.startswith("class "):
                    name = line.split()[1].split("(")[0].rstrip(":")
                    _SYMBOLS.append(Symbol(name, "class", str(path)))

                elif line.startswith("def "):
                    name = line.split()[1].split("(")[0]
                    _SYMBOLS.append(Symbol(name, "function", str(path)))

        return len(_SYMBOLS)

    def search(self, query: str) -> list[Symbol]:
        q = query.lower()
        return [s for s in _SYMBOLS if q in s.name.lower()]
