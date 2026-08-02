from aegis.patch.editor import FileEditor
from aegis.patch.patcher import Patcher
from aegis.tools.base import BaseTool


class PatchTool(BaseTool):
    @property
    def name(self) -> str:
        return "patch"

    def run(self, command: str) -> str:
        action, _, rest = command.partition(" ")

        if action == "read":
            return FileEditor().read(rest)

        if action == "write":
            path, _, text = rest.partition(" ")
            return Patcher().apply(path, text)

        return "Usage: read|write"
