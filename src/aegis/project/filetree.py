from pathlib import Path


class FileTree:
    def build(self, root: str = ".") -> list[str]:
        return sorted(str(path) for path in Path(root).rglob("*") if path.is_file())
