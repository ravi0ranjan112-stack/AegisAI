from aegis.plugins.manager import PluginManager
from aegis.tools.base import BaseTool


class PluginTool(BaseTool):
    @property
    def name(self) -> str:
        return "plugin"

    def run(self, command: str) -> str:
        return PluginManager().execute(command)
