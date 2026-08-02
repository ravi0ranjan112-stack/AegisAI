from aegis.patch.diff import DiffGenerator
from aegis.patch.editor import FileEditor


class Patcher:
    def preview(
        self,
        path: str,
        old: str,
        new: str,
    ) -> str:
        return DiffGenerator().create(old, new)

    def apply(
        self,
        path: str,
        text: str,
    ) -> str:
        FileEditor().write(path, text)
        return "OK"
