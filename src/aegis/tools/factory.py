from aegis.tools.file import FileTool
from aegis.tools.python import PythonTool
from aegis.tools.registry import ToolRegistry
from aegis.tools.shell import ShellTool


class ToolFactory:
    @staticmethod
    def create_registry() -> ToolRegistry:
        registry = ToolRegistry()

        registry.register(ShellTool())
        registry.register(FileTool())
        registry.register(PythonTool())

        return registry
