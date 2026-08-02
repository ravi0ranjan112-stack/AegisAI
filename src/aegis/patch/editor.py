from pathlib import Path


class FileEditor:
    def read(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write(self, path: str, text: str) -> None:
        Path(path).write_text(text, encoding="utf-8")

    def replace(self, path: str, old: str, new: str) -> bool:
        file = Path(path)
        text = file.read_text(encoding="utf-8")

        if old not in text:
            return False

        file.write_text(text.replace(old, new), encoding="utf-8")
        return True
