from aegis.tools.registry import ToolRegistry
from aegis.tools.shell import ShellTool


class ToolFactory:
    @staticmethod
    def create_registry() -> ToolRegistry:
        registry = ToolRegistry()

        registry.register(ShellTool())

        return registry
