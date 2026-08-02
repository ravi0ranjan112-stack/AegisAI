from aegis.tools.base import BaseTool
from aegis.workspace.context import WorkspaceContext

_CONTEXT = WorkspaceContext()


class WorkspaceTool(BaseTool):
    @property
    def name(self) -> str:
        return "workspace"

    def run(self, command: str) -> str:
        if command.strip() in {"", "refresh"}:
            return _CONTEXT.refresh()

        if command.strip() == "files":
            return _CONTEXT.cache.get("files")

        return "Unknown command."
