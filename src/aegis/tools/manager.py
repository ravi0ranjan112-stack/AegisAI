from aegis.tools.registry import ToolRegistry


class ToolManager:
    def __init__(self, registry: ToolRegistry) -> None:
        self._registry = registry

    def execute(
        self,
        tool_name: str,
        command: str,
    ) -> str:
        tool = self._registry.get(tool_name)
        return tool.run(command)
