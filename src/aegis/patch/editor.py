from pathlib import Path


class FileEditor:
    def read(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write(self, path: str, text: str) -> None:
        Path(path).write_text(text, encoding="utf-8")
